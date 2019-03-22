import os
import pickle
import math

def total_distance(point, cluster, matrix):
    cdist = 0
    for cpoint in cluster:
        cdist = cdist + matrix[point][cpoint]

    return cdist

def clustering(n, clusters, matrix):
    K = len(clusters)

    while K < n:
        print(K)
        temp_K = K
        temp_clusters = []
        for cluster in clusters:
            cluster_A = cluster
            # print(cluster_A)
            if len(cluster_A) > 1:
                cluster_B = []
                flag = True
                while flag:
                    avg_dist = 0
                    mv_point = None
                    if len(cluster_B) == 0:
                        for point in cluster_A:
                            temp_avg_dist = total_distance(point, cluster_A, matrix) / len(cluster_A)
                            if temp_avg_dist > avg_dist:
                                avg_dist = temp_avg_dist
                                mv_point = point
                        if mv_point == None:
                            temp_clusters.append(cluster_A)
                            flag = False
                        else:
                            # print(mv_point, avg_dist)
                            cluster_B.append(mv_point)
                            cluster_A.remove(mv_point)
                    else:
                        while True:
                            avg_dist = 0
                            mv_point = None
                            for point in cluster_A:
                                temp_avg_dist_A = total_distance(point, cluster_A, matrix) / len(cluster_A)
                                temp_avg_dist_B = total_distance(point, cluster_B, matrix) / len(cluster_B)
                                temp_avg_dist = temp_avg_dist_A - temp_avg_dist_B
                                if temp_avg_dist > avg_dist:
                                    avg_dist = temp_avg_dist
                                    mv_point = point

                            if avg_dist == 0:
                                flag = False
                                # print(len(cluster_A), len(cluster_B))
                                break
                            if mv_point != None:
                                # print(mv_point)
                                cluster_B.append(mv_point)
                                cluster_A.remove(mv_point)
                if len(cluster_B) != 0:
                    temp_clusters.append(cluster_A)
                    temp_clusters.append(cluster_B)
            else:
                temp_clusters.append(cluster)

        clusters = []
        for cluster in temp_clusters:
            clusters.append(cluster)

        K = len(clusters)
        if temp_K == K:
            break

    print(clusters)

if __name__ == "__main__":
    matrix_file = "proximity_matrix.pkl"
    matrix_f = open(matrix_file, 'rb')
    matrix = pickle.load(matrix_f)
    matrix_f.close()
    # raw_data = open("matrix_data.txt", 'rb')
    # data = pickle.load(raw_data)
    # new_data = data.tolist()
    # initial_cluster = [data]
    matrix = matrix[0:10]
    points = [p for p in range(0, len(matrix))]
    initial_cluster = [points]
    clustering(len(matrix), initial_cluster, matrix)
    # print(matrix[119][120])
