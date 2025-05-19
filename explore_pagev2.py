import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map


def clean_experience(x):
    if x == 'More than 50 years':
        return 50.0
    if x == 'Less than 1 year':
        return 0.5
    try:
        return float(x)
    except:
        return None


def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    return 'Less than a Bachelors'


@st.cache_data
def load_data():
    df = pd.read_csv("din/survey_results_public.csv")
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedComp"]]
    df = df[df["ConvertedComp"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed full-time"]
    df = df.drop("Employment", axis=1)

    country_map = shorten_categories(df.Country.value_counts(), 400)
    df["Country"] = df["Country"].map(country_map)
    df = df[df["ConvertedComp"] <= 250000]
    df = df[df["ConvertedComp"] >= 10000]
    df = df[df["Country"] != "Other"]

    df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)
    df = df.dropna(subset=['YearsCodePro'])

    df["EdLevel"] = df["EdLevel"].apply(clean_education)
    df = df.rename({"ConvertedComp": "Salary"}, axis=1)
    return df

df = load_data()

# Define a custom autopct function to show percentage and count for the pie chart
def autopct_func(pct, allvals):
    absolute = int(pct/100.*sum(allvals))
    return f'{pct:.1f}%\n({absolute})'


def show_explore_page():
    st.title("Summary of Power BI Developer Salaries")

    st.write(
        """
    ### Based on Survey Conducted in 2020
    """
    )

    # Create columns for the selectboxes
    col1, col2 = st.columns(2)

    with col1:
        # Add Country Slicer with "All" option
        countries = sorted(df['Country'].unique().tolist())
        all_countries_option = "All Countries"
        country_options = [all_countries_option] + countries
        # Ensure unique key
        selected_country = st.selectbox("Select Country", country_options, key="country_select")

    with col2:
        # Add Education Level Slicer with "All" option
        education_levels = ['All Education Levels'] + sorted(df['EdLevel'].unique().tolist())
        # Ensure unique key
        selected_education = st.selectbox("Select Education Level", education_levels, key="education_select")


    # Add Years of Experience Slider
    max_years = min(int(df['YearsCodePro'].max()), 40)
    # Ensure unique key
    selected_experience = st.slider("Select Years of Professional Coding Experience", 0, 40, (0, max_years), key="experience_slider")


    # Filter data based on selections
    df_filtered = df.copy() # Start with a copy of the full data

    if selected_country != all_countries_option:
        df_filtered = df_filtered[df_filtered['Country'] == selected_country]

    if selected_education != 'All Education Levels':
        df_filtered = df_filtered[df_filtered['EdLevel'] == selected_education]


    df_filtered = df_filtered[(df_filtered['YearsCodePro'] >= selected_experience[0]) & (df_filtered['YearsCodePro'] <= selected_experience[1])]

    # Displaying the selections
    st.write(f"### Data Filtered by:")
    st.write(f"- Country: {selected_country}")
    st.write(f"- Education Level: {selected_education}")
    st.write(f"- Years of Experience: {selected_experience[0]} to {selected_experience[1]}")


    if df_filtered.empty:
        st.warning("No data available for the selected criteria.")
    else:
        # Create a 2x2 grid of subplots
        fig, axes = plt.subplots(2, 2, figsize=(12, 10)) # Adjust figsize as needed

        # --- Plot 1: Mean Salary Based On Education Level (Top-Left) ---
        education_order = ['Less than a Bachelors', 'Bachelor’s degree', 'Master’s degree', 'Post grad']
        df_filtered['EdLevel'] = pd.Categorical(df_filtered['EdLevel'], categories=education_order, ordered=True)
        data_education = df_filtered.groupby(["EdLevel"])["Salary"].mean().sort_index()

        ax_edu = axes[0, 0] # Select the top-left axis
        bars = ax_edu.bar(data_education.index, data_education.values)

        for bar in bars:
            yval = bar.get_height()
            if not np.isnan(yval):
                ax_edu.text(bar.get_x() + bar.get_width()/2.0, yval, f'${yval:,.0f}', va='bottom', ha='center', fontsize=8)

        ax_edu.set_ylabel("Mean Salary (USD)")
        ax_edu.set_title("Mean Salary by Education Level")
        ax_edu.tick_params(axis='x', labelsize=8, rotation=15)


        # --- Plot 2: Mean Salary Based On Experience (Top-Right - Scatter) ---
        data_experience = df_filtered.groupby(["YearsCodePro"])["Salary"].mean()

        ax_exp = axes[0, 1] # Select the top-right axis
        ax_exp.scatter(data_experience.index, data_experience.values, alpha=0.5)
        ax_exp.set_xlabel("Years of Professional Coding Experience")
        ax_exp.set_ylabel("Mean Salary (USD)")
        ax_exp.set_title("Mean Salary by Experience")
        ax_exp.tick_params(axis='x', labelsize=8)
        ax_exp.tick_params(axis='y', labelsize=8)


        # --- Plot 3: Distribution of Salaries (Bottom-Left) ---
        ax_dist = axes[1, 0] # Select the bottom-left axis
        ax_dist.hist(df_filtered['Salary'], bins=20)
        ax_dist.set_xlabel("Salary (USD)")
        ax_dist.set_ylabel("Number of Respondents")
        ax_dist.set_title("Distribution of Salaries")
        ax_dist.tick_params(axis='x', labelsize=8)
        ax_dist.tick_params(axis='y', labelsize=8)


        # --- Plot 4: Breakdown of Respondents by Country (Bottom-Right - Conditional) ---
        ax_pie = axes[1, 1] # Select the bottom-right axis
        if selected_country == all_countries_option:
             data_country_counts = df_filtered["Country"].value_counts()

             if not data_country_counts.empty:
                 ax_pie.pie(data_country_counts, labels=data_country_counts.index, autopct=lambda pct: autopct_func(pct, data_country_counts.values), shadow=True, startangle=90, textprops={'fontsize': 8})
                 ax_pie.axis("equal")
                 ax_pie.set_title("Breakdown by Country (Filtered)")
             else:
                 ax_pie.set_title("No Country Data for Selected Criteria")
                 ax_pie.text(0.5, 0.5, "No data", horizontalalignment='center', verticalalignment='center', transform=ax_pie.transAxes, fontsize=12, color='gray')
        else:
            ax_pie.clear()
            ax_pie.set_title("Country Breakdown (Select 'All Countries')")
            ax_pie.text(0.5, 0.5, "Select 'All Countries'\nto see this breakdown", horizontalalignment='center', verticalalignment='center', transform=ax_pie.transAxes, fontsize=10, color='gray')
            ax_pie.axis('off')


        plt.tight_layout()

        st.pyplot(fig)

show_explore_page()