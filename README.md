# Clustering Systems

This repository contains implementations of **K-Means Clustering** and
**Hierarchical Clustering**.

### K-Means

### Hierarchical Clustering

The current hierarchical clustering algorithms uses **agglomeration** and **division** to create the
clusters and uses the following linkages:
1. Single Link (MIN)
2. Complete Link (MAX)
3. Group Average (AVG)

The agglomerative hierarchical clustering script is divided into two classes:
1. Agglomerative_Hierarchical
2. Proximity_Matrix
3. Divisive_Hierarchical

### Results

The algorithms were run on a dataset consisting of amino acid sequences. The results are
published as dendrograms:

**K-Means Clustering**

The K-means algorithm currently clusters the sequences into 311 clusters.

**Hierarchical clustering**:

1. ***Single Link***

![Single Link](https://github.com/nsurampu/Clustering-Systems/blob/master/Hierarchical%20Clustering/Agglomerative/agglomerative-single-link-dendrogram.png)

2. ***Complete Link***

![Complete Link](https://github.com/nsurampu/Clustering-Systems/blob/master/Hierarchical%20Clustering/Agglomerative/agglomerative-complete-link-dendrogram.png)

3. ***Group Average***

![Group Average](https://github.com/nsurampu/Clustering-Systems/blob/master/Hierarchical%20Clustering/Agglomerative/agglomerative-single-link-dendrogram.png)

4. ***DIANA***

![DIANA](https://github.com/nsurampu/Clustering-Systems/blob/master/Hierarchical%20Clustering/DIANA/DIANA-dendrogram.png)

### Libraries Used
1. Numpy
2. Scipy
3. Matplotlib

### Authors

![Naren Surampudi](https://github.com/nsurampu/)
<br>![Aditya Srikanth]
<br>![Prateek Das Gupta]
