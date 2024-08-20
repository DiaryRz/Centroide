# Utilise une image Python officielle comme image de base
FROM python:3.11-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier requirements.txt dans le conteneur
COPY requirements/requirements.txt .

# Installe les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie le code de l'application dans le conteneur
COPY . .

# Définit la commande à exécuter lorsque le conteneur démarre
CMD ["python", "app.py"]
