import pickle
import os
import argparse
from pprint import pprint
import numpy as np
import math
from scipy.cluster.hierarchy import dendrogram
import matplotlib.pyplot as plt

class Agglomerative_Hierarchical:
    """
    This class contains functions which comprise the core implementation of agglomerative
    hierarchical clustering.

    @author : Naren Surampudi
    """

    def matrix_min(self, matrix, traversed_points):
        """
        This function returns the minimum value in matrix. Traverse points are avoided in
        minimum calculation.

        Parameters
        ----------
        matrix : list
            The matrix whose minimum element is to be calculated.
        traversed_points : list
            The list of points already traverse elsewhere.

        Returns
        -------
        type : list
            A list consisting of the minimum element's coordinates.
        """
        min_val = 9999
        min_i = 0
        min_j = 0
        for i in range(len(matrix)):
        	for j in range(len(matrix[i])):
        		if i not in traversed_points and j not in  traversed_points:
        			if matrix[i][j] < min_val and matrix[i][j] > 0:
        				min_val = matrix[i][j]
        				min_i = i
        				min_j = j

        return [min_i, min_j]

    def min_cluster_distance(self, matrix, cluster1, cluster2):
        """
        This function calculates the minimum distance between two clusters of points.

        Parameters
        ----------
        matrix : list
            The matrix to be operated upon.
        cluster1 : list
            Cluster of points.
        cluster2 : list
            Cluster of points.

        Returns
        -------
        type : int
            Minimum distance between the two passed clusters.
        """
        dist_list = []

        if isinstance(cluster1, int):
        	cluster1 = [cluster1]
        elif isinstance(cluster2, int):
        	cluster2 = [cluster2]
        for point1 in cluster1:
        	for point2 in cluster2:
        		dist = matrix[point1][point2]
        		if dist > 0:
        			dist_list.append(dist)

        return min(dist_list)

    def max_cluster_distance(self, matrix, cluster1, cluster2):
        """
        This function calculates the maximum distance between two clusters of points.

        Parameters
        ----------
        matrix : list
            The matrix to be operated upon.
        cluster1 : list
            Cluster of points.
        cluster2 : list
            Cluster of points.

        Returns
        -------
        type : int
            Maximum distance between the two passed clusters.
        """
        dist_list = []

        if isinstance(cluster1, int):
        	cluster1 = [cluster1]
        elif isinstance(cluster2, int):
        	cluster2 = [cluster2]
        for point1 in cluster1:
        	for point2 in cluster2:
        		dist = matrix[point1][point2]
        		if dist > 0:
        			dist_list.append(dist)

        return max(dist_list)

    def avg_cluster_distance(self, matrix, cluster1, cluster2):
        """
        This function calculates the average distance between two clusters of points.

        Parameters
        ----------
        matrix : list
            The matrix to be operated upon.
        cluster1 : list
            Cluster of points.
        cluster2 : list
            Cluster of points.

        Returns
        -------
        type : int
            Average distance between the two passed clusters.
        """
        dist_list = []

        if isinstance(cluster1, int):
        	cluster1 = [cluster1]
        elif isinstance(cluster2, int):
        	cluster2 = [cluster2]
        for point1 in cluster1:
        	for point2 in cluster2:
        		dist = matrix[point1][point2]
        		if dist > 0:
        			dist_list.append(dist)

        return sum(dist_list) / ((len(cluster1) * len(cluster2)))

    def matrix_gen(self, matrix, cluster, flag):
        """
        This function generates a new proximity matrix after cluster calculation.

        Parameters
        ----------
        matrix : list
            The matrix to be operated upon.
        cluster : list
            The newly formed cluster of points.
        flag : int
            A parameter that specifies the type of linkage to use.

        Returns
        -------
        type : list
            The newly calculated proximity matrix.
        """
        matrix = np.asarray(matrix)
        dist_vector = []
        for cluster1 in range(matrix.shape[0]):
        	if flag == 0:
        		dist_vector.append(self.min_cluster_distance(matrix.tolist(), cluster, cluster1))
        	elif flag == 1:
        		dist_vector.append(self.max_cluster_distance(matrix.tolist(), cluster, cluster1))
        	elif flag == 2:
        		dist_vector.append(self.avg_cluster_distance(matrix.tolist(), cluster, cluster1))
        matrix = np.vstack((matrix, dist_vector))
        dist_vector.append(0)
        matrix = np.column_stack((matrix, np.asarray(dist_vector)))
        matrix.tolist()

        return matrix

    def clustering(self, matrix, flag):
        """
        This function progressively performs agglomerative clustering. The heart of the entire
        class that calls all other relevant methods.

        Parameters
        ----------
        matrix : list
            The proximity matrix to be operated upon.
        flag : int
            A parameter that specifies the type of linkage to use.

        Returns
        -------
        type : list
            A list consisting of the final priority matrix and the linkage matrix.
        """
        total = len(matrix[0])
        K = 1
        linkage_matrix = np.zeros(shape=(total-1, 4))
        traversed_points = []
        cluster_numbers = {}
        lflag = total

        while K < total:
        	cluster = self.matrix_min(matrix, traversed_points)
        	if cluster[0] not in traversed_points and cluster[1] not in traversed_points:
        		matrix = self.matrix_gen(matrix, cluster, flag)
        		temp = 0
        		if str(cluster[0]) in cluster_numbers.keys():
        			temp = temp + cluster_numbers[str(cluster[0])]
        		else:
        			temp = temp + 1
        		if str(cluster[1]) in cluster_numbers.keys():
        			temp = temp + cluster_numbers[str(cluster[1])]
        		else:
        			temp = temp + 1
        		linkage_matrix[K-1] = [cluster[0], cluster[1], matrix[cluster[0]][cluster[1]], temp]
        		lflag = lflag + 1
        		cluster_numbers[str(lflag)] = temp
        		traversed_points.append(cluster[0])
        		traversed_points.append(cluster[1])
        	K = K + 1

        return [matrix, linkage_matrix]

class Proximity_Matrix:
    """
    This class is called in the very beginning, when calculating the proximity matrix for
    the first time from the data.
    """

    def distance(self, sample1, sample2):
        """Short summary.

        Parameters
        ----------
        sample1 : list
            A sample in the data.
        sample2 : list
            A sample in the data.

        Returns
        -------
        type : float
            The distance between the two samples.
        """
        edist = 0
        for i in range(len(sample1)):
        	dist = 0
        	for j in range(len(sample1[i])):
        		dist = dist + abs(sample1[i][j] - sample2[i][j])
        		edist = edist + dist

        return math.sqrt(edist)

    def raw_matrix(self, data):
        """
        This function calculates the first proximity matrix.

        Parameters
        ----------
        data : list
            The processed data, obtained from raw data.

        Returns
        -------
        type : list
            The very first proximity matrix.
        """
        matrix = []

        for sample1 in data:
        	l = []
        	for sample2 in data:
        		dist = self.distance(sample1, sample2)
        		l.append(dist)
        	matrix.append(l)

        return matrix

if __name__ == "__main__":

    agglomerative = Agglomerative_Hierarchical()
    proximity = Proximity_Matrix()

    parser = argparse.ArgumentParser(description="Choose hierarchy link")
    parser.add_argument('link', help="Which link to use")
    args = parser.parse_args()
    link = vars(args)['link']
    c_flag = None
    # test = True
    test = False   # Flags for running the program in testing mode.

    if test:   # The proximity matrix to be used for testing.
        matrix = [[0, 0.23, 0.22, 0.37, 0.34, 0.24],
        		  [0.23, 0, 0.14, 0.19, 0.14, 0.24],
        		  [0.22, 0.14, 0, 0.16, 0.28, 0.1],
        		  [0.37, 0.19, 0.16, 0, 0.28, 0.22],
        		  [0.34, 0.14, 0.28, 0.28, 0, 0.39],
        		  [0.24, 0.24, 0.1, 0.22,0.39, 0]]
    else:
        matrix_file = "proximity_matrix.pkl"
    if os.path.isfile(matrix_file):
    	matrix_f = open(matrix_file, 'rb')
    	matrix = pickle.load(matrix_f)
    	matrix_f.close()
    else:
    	dfile = open('matrix_data.txt', 'rb')
    	data = pickle.load(dfile)
    	# data = data[0:100]
    	matrix = proximity.raw_matrix(data)
    	matrix_f = open(matrix_file, 'wb')
    	pickle.dump(matrix, matrix_f)
    	matrix_f.close()
    	dfile.close()

    if link == "single-link":
        c_flag = 0
    elif link == "complete-link":
        c_flag = 1
    elif link == "group-average":
        c_flag = 2

    linkage_matrix = agglomerative.clustering(matrix, c_flag)[1]

    l_file = open(link + ".pkl", 'wb')
    # l_file = open(link + ".pkl", 'rb')
    pickle.dump(linkage_matrix, l_file)
    # linkage_matrix = pickle.load(l_file)
    l_file.close()

    pprint(linkage_matrix)

    fig = plt.figure(figsize=(8, 4))
    dendrogram = dendrogram(linkage_matrix)   # Draw dendrogram of final clusters.
    plt.show()
