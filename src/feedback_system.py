import pandas as pd
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

FEEDBACK_FILE = os.path.join(BASE_DIR, "data", "feedback_log.csv")

# ---------------------------------------------------
# Save user feedback
# ---------------------------------------------------

def save_feedback(user_query, country, destinations, rating, interests):

    timestamp = datetime.now()

    sites = "|".join(destinations)

    interest_str = ",".join(interests)

    data = {
        "user_query": user_query,
        "country": country,
        "recommended_sites": sites,
        "rating": rating,
        "interests": interest_str,
        "timestamp": timestamp
    }

    df = pd.DataFrame([data])

    if os.path.exists(FEEDBACK_FILE):

        df.to_csv(
            FEEDBACK_FILE,
            mode="a",
            header=False,
            index=False
        )

    else:

        df.to_csv(
            FEEDBACK_FILE,
            index=False
        )


# ---------------------------------------------------
# Load feedback dataset
# ---------------------------------------------------

def load_feedback():

    if os.path.exists(FEEDBACK_FILE):

        return pd.read_csv(FEEDBACK_FILE)

    return pd.DataFrame()


# ---------------------------------------------------
# Calculate average rating
# ---------------------------------------------------

def average_rating(df):

    if df.empty:
        return 0

    return df["rating"].mean()


# ---------------------------------------------------
# Most liked destinations
# ---------------------------------------------------

def most_liked_destinations(df):

    if df.empty:
        return pd.Series()

    sites = df["recommended_sites"].str.split("|")

    exploded = sites.explode()

    return exploded.value_counts().head(10)


# ---------------------------------------------------
# User interest trends
# ---------------------------------------------------
def interest_trends(df):

    if df.empty:
        return None

    # Ensure column exists
    if "interests" not in df.columns:
        return None

    # Convert to string safely
    interests = df["interests"].fillna("").astype(str)

    # Split interests into lists
    interests = interests.apply(lambda x: x.split(","))

    # Flatten list
    interests = interests.explode()

    # Remove empty values
    interests = interests[interests != ""]

    # Count occurrences
    trends = interests.value_counts()

    return trends