import math
from dotenv import load_dotenv
from connexion.connexion import connexion

def Distance(lat1, lon1, lat2, lon2):
    R = 6371000  # Rayon de la Terre en mètres
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

# Fonction pour trouver les points dans un rayon donné
def find_points_within_radius(lat, lon, radius_km):
    collection = connexion("places")
    points_within_radius = []
    places = collection.find()
    for point in places:
        point_lat = point['lat']
        point_lon = point['long']
        distance = Distance(lat, lon, point_lat, point_lon)
        if distance <= radius_km:
            points_within_radius.append(point)

    return points_within_radius        

def find_closest_point(lat, lon):
    collection = connexion("places")
    places = collection.find()
    closest_point = None
    min_distance = float('inf')

    for point in places:
        point_lat = point['lat']
        point_lon = point['long']
        distance = Distance(lat, lon, point_lat, point_lon)
        if distance < min_distance:
            min_distance = distance
            closest_point = point

    if closest_point:
        closest_point['distance'] = min_distance
        closest_point['_id'] = str(closest_point['_id'])

    return closest_point

# print(find_closest_point(-18.91730, 47.5427332))
