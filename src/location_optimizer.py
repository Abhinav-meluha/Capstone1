def choose_best_region(recommendations):

    country_counts = recommendations["country"].value_counts()

    best_country = country_counts.index[0]

    filtered = recommendations[
        recommendations["country"] == best_country
    ]

    return filtered, best_country