import numpy as np
from sklearn.cluster import DBSCAN
import folium
import random

def calculate_centroid(cluster):
    latitudes = [point[0] for point in cluster]
    longitudes = [point[1] for point in cluster]
    centroid_lat = sum(latitudes) / len(latitudes)
    centroid_lon = sum(longitudes) / len(longitudes)
    return (centroid_lat, centroid_lon)

def getCentroide(data, distance_max, min_point_gpe):
    coordinates = transform_data(data)
    coords_in_radians = np.radians(coordinates)
    db = DBSCAN(eps=distance_max/6371.0, min_samples=min_point_gpe, algorithm='ball_tree', metric='haversine').fit(coords_in_radians)
    labels = db.labels_
    unique_labels = set(labels)
    centroids = []
    clusters = []
    for label in unique_labels:
        if label == -1:
            continue
        cluster_points = [coordinates[i] for i in range(len(coordinates)) if labels[i] == label]
        clusters.append(cluster_points)
        centroid = calculate_centroid(cluster_points)
        centroids.append(centroid)
    return centroids, clusters

def getCentroidePerCluster(data, distance_max, min_point_gpe):
    coordinates = transform_data(data)
    coords_in_radians = np.radians(coordinates)
    
    # Clustering avec DBSCAN
    db = DBSCAN(eps=distance_max/6371.0, min_samples=min_point_gpe, algorithm='ball_tree', metric='haversine').fit(coords_in_radians)
    labels = db.labels_
    unique_labels = set(labels)
    
    # Calcul des centroïdes et structuration des données
    results = []
    for label in unique_labels:
        if label == -1:
            continue
        
        # Points dans le cluster courant
        cluster_points = [data['data'][i] for i in range(len(coordinates)) if labels[i] == label]
        
        # Calcul du centroïde
        cluster_coords = [(point["lat"], point["lon"]) for point in cluster_points]
        centroid = calculate_centroid(cluster_coords)
        
        # Structurer les données du cluster
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

coordinates = [
    #Andoharam
    (-18.98599180954815, 47.53280089575227),
    (-18.98599180954815, 47.53280089575227),
    (-18.987335167653004, 47.53358170249357),
    (-18.988582152580197, 47.53241936891142),
    (-18.986974493189617, 47.53164663883979),
    (-18.99504030639858, 47.53549234333591),
    (-18.994763, 47.533380),
    (-18.993646, 47.532840),
    (-18.993444238251453, 47.53445886039471),
    (-18.989675433415755, 47.531004175557065),
    (-18.989675, 47.531007),
    (-18.986510, 47.530828),
    (-18.979446, 47.530751),
    
    #tanjombato
    
    (-18.957213, 47.527939),
    (-18.955459, 47.525435),
    (-18.956046, 47.531642),
    (-18.957579, 47.528403),
    (-18.952388902633615, 47.52785874765359),
    (-18.95244976348816, 47.526004316962755),
    (-18.953832958952763, 47.52526722464976),
    (-18.95201653197291, 47.5246956656011),
    
    #Anosy Mahamasina
    (-18.920491629583854, 47.52299479693875),
    (-18.91881520462395, 47.523420117202576),
    (-18.91822126718852, 47.52018970864501),
    (-18.917665646387025, 47.51965299492681),
    (-18.920692799463076, 47.53021511461895),
    (-18.918479917663035, 47.528645480380966),
    (-18.91688011037723, 47.52761255978923),
    (-18.915855076098513, 47.52669103258746),
    (-18.913494146913454, 47.52690935674842),

    
    #analakely
    (-18.9048758763294, 47.526493318511775),
    (-18.90589139750237, 47.52651357186476),
    (-18.904530980920715, 47.525855338148475),
    (-18.908315210890773, 47.524154057154014),
    (-18.90812255486552, 47.5209706833917),
    (-18.904846083536476, 47.52159853708809),
    (-18.904003004478167, 47.522560570982264),
    (-18.89924369958069, 47.52367865930732),
    (-18.900959587829703, 47.517320381182856),
    
    #Ankadifotsy
    (-18.898425414390974, 47.52420153519465),
    (-18.898262523601566, 47.525997040614484),
    (-18.89729448363962, 47.525652697109315),
    (-18.897233980946442, 47.52459998982573),
    (-18.897289829568763, 47.523468575437455),
    (-18.898555726898564, 47.52659226296182),
    (-18.898644153206085, 47.52715305098668)
    
    
]


distance_max = 0.5 # En km
min_point_gpe = 1  # Min nb points pour former le gpe

# centroids, clusters = getCentroide(coordinates, distance_max, min_point_gpe)
# print("Centroids of clusters:", centroids)

# # Créer une carte centrée sur un point moyen
# map_center = calculate_centroid(coordinates)
# map = folium.Map(location=map_center, zoom_start=13)

# folium.TileLayer(
#     tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
#     attr='Esri',
#     name='Esri Satellite',
#     overlay=False,
#     control=True
# ).add_to(map)

# folium.LayerControl().add_to(map)


# # Ajouter les clusters et les centroïdes à la carte
# for cluster in clusters:
#     if len(cluster) > 0:
#         cluster_polygon = folium.Polygon(cluster, color='blue', fill=True, fill_color='blue', fill_opacity=0.3)
#         map.add_child(cluster_polygon)
#         for point in cluster:
#             folium.Marker(location=point, icon=folium.Icon(color='blue')).add_to(map)

# for centroid in centroids:
#     folium.Marker(location=centroid, icon=folium.Icon(color='red', icon='info-sign')).add_to(map)

# # Sauvegarder la carte dans un fichier HTML
# map.save('clusters_map.html')
