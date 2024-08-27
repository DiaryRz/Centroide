import os
import numpy as np
import requests
from sklearn.cluster import DBSCAN

def calculate_centroid(cluster):
    latitudes = [point[0] for point in cluster]
    longitudes = [point[1] for point in cluster]
    centroid_lat = sum(latitudes) / len(latitudes)
    centroid_lon = sum(longitudes) / len(longitudes)
    return (centroid_lat, centroid_lon)

def getCentroidePerCluster(data, distance_max=100, min_point_gpe=1):
    coordinates = transform_data(data)
    coords_in_radians = np.radians(coordinates)
    db = DBSCAN(eps=distance_max/6371.0, min_samples=min_point_gpe, algorithm='ball_tree', metric='haversine').fit(coords_in_radians)
    labels = db.labels_
    unique_labels = set(labels)
    results = []
    for label in unique_labels:
        if label == -1:
            continue
        # Points dans le cluster courant
        cluster_points = [data['data'][i] for i in range(len(coordinates)) if labels[i] == label]
        cluster_coords = [(point["lat"], point["lon"]) for point in cluster_points]
        centroid = calculate_centroid(cluster_coords)
        cluster_data = {
            "lat": centroid[0],
            "lon": centroid[1],
            "people": cluster_points
        }
        results.append(cluster_data)
    return results

def transform_data(data):
    data_field = data.get("data", [])
    coordinates = [(item["lat"], item["lon"]) for item in data_field]
    return coordinates

def get_stop(data):
    listData = getCentroidePerCluster(data)
    processed_data = []
    for item in listData:
        print(item.get("lat"))
        url = f'http://{os.getenv("endPoint")}/api/nearest_point?lat={item.get("lat")}&lon={item.get("lon")}'

        result = requests.get(url)
        if result.status_code == 201:
            data = result.json()
            jsondata = {
                "lat": data.get("lat"),
                "lon": data.get("lon"),
                "people": item.get("people")
            }
            processed_data.append(jsondata)
        else:
            return []
    return processed_data
