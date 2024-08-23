import numpy as np
from sklearn.cluster import DBSCAN
from Find import find_closest_point

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

def get_stop(listData):
    processed_data = []
    for item in listData:
        result = find_closest_point(item.get("lat"), item.get("lon"))
        jsondata = {
            "lat": result.get("lat"),
            "lon": result.get("lon"),
            "people": item.get("people")
        }
        processed_data.append(jsondata)
    print(processed_data)
    return processed_data


def union(data):
    print(getCentroidePerCluster(data))
    dt = getCentroidePerCluster(data)
    get_stop(dt)