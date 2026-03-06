from datetime import datetime, timedelta
from src.route_optimizer import optimize_route


def generate_itinerary(destinations, start_date, days):

    itinerary = []

    # Convert start date
    start = datetime.strptime(start_date, "%Y-%m-%d")

    # Remove duplicate destinations
    destinations = destinations.drop_duplicates(subset=["Site Name"]).reset_index(drop=True)

    # Optimize route using city distance
    optimized_route = optimize_route(destinations)

    # Convert optimized route to list of site names
    ordered_sites = [place["Site Name"] for place in optimized_route]

    # Generate itinerary
    for i in range(days):

        date = start + timedelta(days=i)

        destination = ordered_sites[i % len(ordered_sites)]

        itinerary.append({
            "date": date.strftime("%Y-%m-%d"),
            "destination": destination
        })

    return itinerary