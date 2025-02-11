import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

np.random.seed(3)

onehotencoder = OneHotEncoder(categorical_features = [0])
#X = onehotencoder.fit_transform(X).toarray()
with open('dataset.txt','r') as f:
    textual_data = []
    protein = ""
    string = ""
    max_len = -1
    for line in f.readlines():
        # print(line)
        if ">" in line:
            continue
        else:
            protein += line[:-1]
            if line[-2] == "*":
                protein = protein[:-1]
                textual_data += [protein]
                max_len = max(max_len,len(protein))
                protein = ""
            elif line[-1] == "*":
                protein = protein
                textual_data += [protein]
                max_len = max(max_len,len(protein))
                protein = ""
            string += protein

         
    string_list = sorted(list(set(string)))# extract the amino acids       
    mapping_from_acid_to_vector = {acid : string_list.index(acid) for acid in string_list}
    dataset = np.zeros((len(textual_data),max_len,len(mapping_from_acid_to_vector)))
    
    for data_string in range(len(textual_data)):
        for acid_position in range(len(textual_data[data_string])):
            dataset[data_string][acid_position][mapping_from_acid_to_vector[textual_data[data_string][acid_position]]] = 1
            
def compute_distance(feature_center, point):
    return np.sum(np.power(feature_center-point,2))    
    
#def kmeans(data,num_cluster_centers,epochs=1000):
num_cluster_centers=50
#cluster = np.array((num_cluster_centers, dataset.shape[1],dataset.shape[2]))
center_indexes = np.random.random_integers(0,dataset.shape[0],num_cluster_centers)
feature_centers = dataset[center_indexes]

epochs=5
for epoch in range(epochs):
    distances = np.zeros((num_cluster_centers,1))
    cluster=[]
    for i in range(num_cluster_centers):
        cluster.append([])
    #cluster=tempcluster
    for datapoint in range(dataset.shape[0]):
        for centroid in range(num_cluster_centers):
            distances[centroid] = compute_distance(feature_centers[centroid,:],dataset[datapoint,:])
            cluster_index = np.argmin(distances)
        #print(cluster_index)
        cluster[cluster_index].append([dataset[datapoint]])
        
    for centroid in range(num_cluster_centers):
        cluster_sum = np.sum(cluster[centroid],axis=0)        
        if len(cluster[centroid])!=0:
            feature_centers[centroid]=np.zeros((dataset.shape[1],dataset.shape[2]))
            for index in range(cluster_sum.shape[1]):
                mode_index=np.argmax(cluster_sum[0][index])
                feature_centers[centroid][index][mode_index]=1
                
s=0                
for centroid in range(num_cluster_centers):
    print(len(cluster[centroid]))
    s+=len(cluster[centroid])
print(s) 
point=[cluster[3][4]]
a=[cluster[3][4]]
a!=point

"""
final_cluster=[]    
acid_cluster=[]
for kthcluster in cluster:
    acid=''
    for point in kthcluster:
        i=0
        for row in point[0]:
            acid+=string_list[np.argmax(row)]
            if i==20:
                for text in textual_data:
                    if acid in text:
                        acid=text
                        break
            i+=1
        acid_cluster.append(acid)
    final_cluster.append(acid_cluster)
    
len(final_cluster[4])
acid_cluster[0]                  
        # print('dashapetapoint ',datapoint)
#        distances = compute_distance(feature_centers,dataset[datapoint,:])
#        cluster_index = np.argmin(distances)
#       cluster[datapoint,0] = cluster_index
len(textual_data[4])
len(acid)
len(text)
"""
    
    