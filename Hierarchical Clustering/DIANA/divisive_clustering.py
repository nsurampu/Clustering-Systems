def move_sample(sample, cluster1, cluster2):
    cluster1 = cluster1 - sample
    cluster2 = cluster2 + sample

    return [cluster1, cluster2]

def distance(self, sample1, sample2):
    edist = 0
    for i in range(len(sample1)):
        dist = 0
        for j in range(len(sample1[i])):
            dist = dist + abs(sample1[i][j] - sample2[i][j])
            edist = edist + dist

    return math.sqrt(edist)

def dissimilarity(sample, cluster):
    diss = 0
    for other_sample in cluster:
        diss = diss + distance(sample, other_sample)

    return diss

def clustering():
    K = 0
    clusters =

    while K < final_clusters:
        for cluster in clusters:
            cluster_B = []
            iteration = 1
            while points_to_move:
                cluster_A_diss = 0
                cluster_A_item = NULL
                if iteration == 1:
                    for item1 in cluster_A:
                        diss = 0
                        for item2 in cluster_A:
                            diss = diss + dissimilarity(item1, item2) / (len(cluster_A) - 1)
                        if diss > cluster_A_diss:
                            move_result = move_sample(sample, cluster_A, cluster_B)
                            cluster_A = move_result[0]
                            cluster_B = move_result[1]
                else:
                    for item1 in cluster_A:
                        diss_A = 0
                        diss_B = 0
                        for item2 in cluster_A:
                            diss_A = diss_A + dissimilarity(item1, item2) / (len(cluster_A) - 1)
                        for item_2 in cluster_B:
                            diss_B = diss_B + dissimilarity(item1, item2) / (len(cluster_B))
                        diss = diss_A - diss_B
                        if diss < 0:
                            break
                        else:
                            if diss > cluster_A_diss:
                                move_result = move_sample(sample, cluster_A, cluster_B)
                                cluster_A = move_result[0]
                                cluster_B = move_result[1]
                iteration = iteration + 1

            temp_clusters.append(cluster_A, cluster_B)

    clusters = temp_clusters
    K = len(clusters)
