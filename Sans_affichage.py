import numpy as np
from sklearn.cluster import DBSCAN
from geopy.distance import great_circle
from geopy.point import Point

def calculate_centroid(cluster):
    latitudes = [point[0] for point in cluster]
    longitudes = [point[1] for point in cluster]
    centroid_lat = sum(latitudes) / len(latitudes)
    centroid_lon = sum(longitudes) / len(longitudes)
    return (centroid_lat, centroid_lon)

def getCentroide(coordinates, distance_max, min_point_gpe):
    coords_in_radians = np.radians(coordinates)
    db = DBSCAN(eps=distance_max/6371.0, min_samples=min_point_gpe, algorithm='ball_tree', metric='haversine').fit(coords_in_radians)
    labels = db.labels_
    unique_labels = set(labels)
    centroids = []
    for label in unique_labels:
        #Aucun cluster
        if label == -1:
            continue
        cluster_points = [coordinates[i] for i in range(len(coordinates)) if labels[i] == label]
        # print(cluster_points)
        centroid = calculate_centroid(cluster_points)
        centroids.append(centroid)
    return centroids

coordinates = [
    (40.7128, -74.0060),
    (48.8566, 2.3522),  
    (40.7127, -74.0059),
    (48.8567, 2.3523),
    (-18.859335, 47.510035),
    (-18.862061, 47.511425),
    (40.7130, -74.0065),
    (48.8570, 2.3530),
    (-18.862438, 47.508311)
]

distance_max = 100  #En Km de avadika radiant avy eo
min_point_gpe = 2  # Minimum number of points to form a cluster

centroids = getCentroide(coordinates, distance_max, min_point_gpe)
print("Centroids of clusters:", centroids)