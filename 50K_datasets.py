import pandas as pd
import numpy as np

# Define the number of samples
num_samples = 50000

# Generate realistic data for each feature
data = {
    "Business Age (years)": np.random.randint(1, 51, num_samples),
    "Industry": np.random.choice(['Manufacturing', 'Services', 'Agriculture', 'Construction', 'Retail'], num_samples),
}

# Generate "Annual Revenue (RM)" and "Number of Employees" based on Malaysian SME definitions
data["Annual Revenue (RM)"] = np.where(
    data["Industry"] == "Manufacturing",
    np.random.normal(2000000, 800000, num_samples).clip(100000, 50000000).astype(int),
    np.where(
        data["Industry"] == "Retail",
        np.random.normal(800000, 400000, num_samples).clip(50000, 20000000).astype(int),
        np.random.normal(1000000, 500000, num_samples).clip(50000, 30000000).astype(int)
    )
)

data["Number of Employees"] = np.where(
    data["Industry"] == "Manufacturing",
    np.random.choice(
        [np.random.randint(1, 6),  # Micro
         np.random.randint(6, 76),  # Small
         np.random.randint(76, 201)],  # Medium
        num_samples
    ),
    np.random.choice(
        [np.random.randint(1, 6),  # Micro
         np.random.randint(6, 31),  # Small
         np.random.randint(31, 76)],  # Medium
        num_samples
    )
)

# Generate other features
data["Existing Loan"] = np.random.choice([0, 1], num_samples, p=[0.6, 0.4])  # 60% no loan, 40% has loan
data["Credit Score"] = np.random.normal(700, 50, num_samples).astype(int).clip(300, 850)  # Skewed higher
data["Profit Margin (%)"] = np.where(
    data["Industry"] == "Retail",
    np.random.normal(12, 4, num_samples).astype(int).clip(5, 25),
    np.random.normal(18, 6, num_samples).astype(int).clip(5, 35)
)
data["Loan Amount Requested (RM)"] = (
    data["Annual Revenue (RM)"] * np.random.uniform(0.1, 0.4, num_samples)
).astype(int).clip(20000, 1000000)
data["Location"] = np.random.choice([
    'Johor', 'Kedah', 'Kelantan', 'Malacca', 'Negeri Sembilan', 
    'Pahang', 'Penang', 'Perak', 'Perlis', 'Sabah', 
    'Sarawak', 'Selangor', 'Terengganu', 'Kuala Lumpur'
], num_samples)

# Add a more realistic "Loan Eligibility" based on conditions
data["Loan Eligibility"] = (
    (data["Credit Score"] > 680) & 
    (data["Profit Margin (%)"] > 15) & 
    (data["Existing Loan"] == 0) & 
    (data["Annual Revenue (RM)"] > 200000)  # Ensure revenue is above a realistic threshold
).astype(int)

# Create a DataFrame
df = pd.DataFrame(data)

# Save the dataset to a CSV file
df.to_csv("loan_eligibility_dataset.csv", index=False)

print("saved as 'loan_eligibility_dataset.csv'.")