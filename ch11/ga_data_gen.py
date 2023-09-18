import pandas as pd
import random
from datetime import datetime, timedelta

# Create synthetic Google Analytics data for a jewelry website
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)
jewelry_categories = ["Necklaces", "Earrings", "Bracelets", "Rings"]
traffic_sources = ["Organic Search", "Direct", "Referral", "Social"]

data = {
    "date": [],
    "category": [],
    "source": [],
    "sessions": [],
    "pageviews": [],
    "transaction_revenue": []
}

current_date = start_date
while current_date <= end_date:
    num_sessions = random.randint(100, 1000)
    for _ in range(num_sessions):
        category = random.choice(jewelry_categories)
        source = random.choice(traffic_sources)
        sessions = random.randint(1, 5)
        pageviews = sessions * random.randint(1, 5)
        transaction_revenue = round(random.uniform(10, 500), 2)
        
        data["date"].append(current_date)
        data["category"].append(category)
        data["source"].append(source)
        data["sessions"].append(sessions)
        data["pageviews"].append(pageviews)
        data["transaction_revenue"].append(transaction_revenue)
    
    current_date += timedelta(days=1)

# Create a DataFrame
df = pd.DataFrame(data)

# Save the synthetic data to a CSV file
df.to_csv("synthetic_google_analytics_data_2022.csv", index=False)
