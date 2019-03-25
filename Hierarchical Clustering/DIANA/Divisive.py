import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import copy

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

    
    return sum
"""            
average_distance(point, cluster[3])
sum=0            
print(len(cluster[3]))
chosen_cluster=cluster[3]
remaining_points=new_cluster[2]
point=new_cluster[3]
average_distance(point, chosen_cluster)
for remaining_points in chosen_cluster:
    if np.array_equal(point[0],remaining_points[0])!=True:
        sum+=np.sum(np.abs(remaining_points[0]-point[0]))
        """
        
def average_distance(point, chosen_cluster):
    sum=0
    for remaining_points in chosen_cluster:
        sum+=np.sum(np.abs(remaining_points-point))
        
    return sum
"""
c=new_cluster[4]
sum=0
for remaining_points in chosen_cluster:
    sum+=np.sum(np.abs(c-point[0]))
    """
#chosen_cluster=list(dataset)

def max_point_index(chosen_cluster):
    point_index=0
    distances=list(np.zeros(len(chosen_cluster)))    
    for point_index in range(len(chosen_cluster)):
        distances[point_index]=average_distance(chosen_cluster[point_index], chosen_cluster)#/(len(chosen_cluster)-1)
    max_distance_index=np.argmax(distances)
    return max_distance_index


def new_clusters(test_cluster):
    new_cluster=[]
    max_distance_index=max_point_index(test_cluster)
    max_distance_point=test_cluster[max_distance_index]
    new_cluster.append(max_distance_point)
    test_cluster=list(test_cluster)
    test_cluster.pop(max_distance_index)
    return test_cluster, new_cluster


def cluster_difference(point, old_cluster, new_cluster):
    return ((average_distance(point, old_cluster)/(len(old_cluster)-1))-(average_distance(point, new_cluster)/(len(new_cluster))))


"""
for i in range(len(test_cluster)):
    if i==0:
        old_cluster,new_cluster=new_clusters(test_cluster)
        continue
    cluster_diff=cluster_difference(old_cluster[i], old_cluster, new_cluster)
    if temp_diff>cluster_diff:
        temp_diff=cluster_diff
        temp_index=i
        
new_cluster=[]

point=test_cluster[6]
old_cluster,new_cluster=new_clusters(test_cluster)
        """
        """
distances=list(np.zeros(len(test_cluster)))    
for point_index in range(len(test_cluster)):
    distances[point_index]=average_distance(test_cluster[point_index], test_cluster)/(len(test_cluster)-1)
max_distance_index=np.argmax(distances)
"""
point=test_cluster[6]

max_value=0
temp_diff=0
temp_index=0
old_cluster=[]
new_cluster=[]

test_cluster=copy.deepcopy(dataset)
dataset_cluster=list(copy.deepcopy(dataset))
#test_cluster=copy.deepcopy(cluster[3])
#a=clu
temp_old_cluster, temp_new_cluster = new_clusters(test_cluster)
old_cluster = copy.deepcopy(temp_old_cluster)
new_cluster = copy.deepcopy(temp_new_cluster) 

def iterate_cluster(old_cluster, new_cluster): 
    while True: 
        temp_index=0       
        temp_diff=0       
        for i in range(len(old_cluster)):   
            i=10
            cluster_diff=cluster_difference(old_cluster[i], old_cluster, new_cluster)
            if temp_diff<cluster_diff:
                temp_diff=cluster_diff
                temp_index=i
        if temp_diff==0:
            break    
        new_cluster.append(old_cluster[temp_index])
        old_cluster.pop(temp_index) 
        
    return old_cluster, new_cluster

final_cluster=[]

"""
while len(final_cluster)==len(dataset_cluster):
    max_value=0
    temp_diff=0
    temp_index=0
    old_cluster=[]
    new_cluster=[]
    test_cluster=copy.deepcopy(dataset)
    dataset_cluster=list(copy.deepcopy(dataset))
    temp_old_cluster, temp_new_cluster = new_clusters(test_cluster)
    old_cluster = copy.deepcopy(temp_old_cluster)
    new_cluster = copy.deepcopy(temp_new_cluster) 
    
    if 
    

test_cluster=copy.deepcopy(dataset)
dataset_cluster=list(copy.deepcopy(dataset))
"""    
    
                

for i in range(5):
    print(i)
