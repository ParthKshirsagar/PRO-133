from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import csv

data = []

with open('final.csv') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)

headers = data[0]
data_rows = data[1:]

star_masses = []
star_radiuses = []
star_gravities = []
star_names = []
for star_data in data_rows:
    try:
        star_masses.append(float(star_data[2]))
    except: pass
    try:
        star_radiuses.append(float(star_data[3]))
    except: pass
    try:
        star_gravities.append(float(star_data[8]))
    except: pass
    star_names.append(star_data[0])

X = []
for index, star_mass in enumerate(star_masses):
    temp_list = [star_radiuses[index], star_mass]
    X.append(temp_list)

WCSS = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    WCSS.append(kmeans.inertia_)

plt.figure(figsize=(10,5))
sns.lineplot(range(1,11), WCSS, marker='o', color='red')
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()