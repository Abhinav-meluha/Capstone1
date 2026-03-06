import numpy as np
from math import radians, cos, sin, sqrt, atan2


def haversine_distance(lat1, lon1, lat2, lon2):

    R = 6371  # Earth radius (km)

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))

    return R * c


def optimize_route(destinations):

    destinations = destinations.reset_index(drop=True)

    visited = [0]
    route = [destinations.iloc[0]]

    remaining = list(range(1, len(destinations)))

    while remaining:

        last = visited[-1]

        last_lat = destinations.iloc[last]["latitude"]
        last_lon = destinations.iloc[last]["longitude"]

        nearest = None
        nearest_distance = float("inf")

        for i in remaining:

            lat = destinations.iloc[i]["latitude"]
            lon = destinations.iloc[i]["longitude"]

            dist = haversine_distance(last_lat, last_lon, lat, lon)

            if dist < nearest_distance:
                nearest_distance = dist
                nearest = i

        visited.append(nearest)
        route.append(destinations.iloc[nearest])
        remaining.remove(nearest)

    return route