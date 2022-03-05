# Fraud Detection
## [Community Detection Algorithm](https://towardsdatascience.com/community-detection-algorithms-9bd8951e7dae)
* Difference between clustering and graph community detection:
   * Clustering is a machine learning technique in which similar data points are grouped into the same cluster based on their attributes. Even though clustering can be applied to networks, it is a broader field in unsupervised machine learning which deals with multiple attribute types. 
   * community detection is specially tailored for network analysis which depends on a single attribute type called edges.
* Algorithms
   * Method:
      * Agglomerative Methods: edges are added one by one to a graph which only contains nodes. Edges are added from the stronger edge to the weaker edge 
      * Divisive Methods: edges are removed one by one from a complete graph.
   * Algorithms:
      * Louvain Community Detection: 
         * This approach is based on modularity, which tries to maximize the difference between the actual number of edges in a community and the expected number of edges in the community.
         * works well in the limit of a few large communities. 
      * Surprise Community Detection: 
         * a measure based on classical probabilities known as Surprise has been introduced to evaluate the quality of a partition of a network into communities. The algorithm is almost similar to the Louvain community detection algorithm except that it uses surprises instead of modularity.
         * works well in the limit of many small communities
      * Leiden Community Detection
         * Louvain community detection has a tendency to discover communities that are internally disconnected (badly connected communities). 
         * Louvain has a tendency to discover very weekly connected communities. Therefore, they have proposed the much faster Leiden algorithm which guarantees that communities are well connected.
         * ![image](https://user-images.githubusercontent.com/16402963/156856025-624de759-873c-41cb-8f8c-3700ec275278.png)
      * Walktrap Community Detection
         * based on random walks in which distance between vertices are measured through random walks in the network. 
      
* Python packages: igraph, cdlib 
* [A survey of community detection methods in multilayer networks](https://link.springer.com/article/10.1007/s10618-020-00716-6)
* An example:
    * Feature: 
      * comminuty size 
         * community detection -- (using Union Find algorithm)
         * find sets of connected nodes in the graph, where every set is a community including multiple nodes and each node is reachable from other nodes
         * Example: identify agent susbicious patterns, find agent communities with multiple agents selling early lapset/not taken policies to each other (some domain knowledge required), in this case, agent has relationship with customer and policy (commision fraud, agents sell policy to each other) 
      * Node Similarity
        * Jaccard Similarity Score
        * measure the similarity between agent node pairs based on common neighbors connected 
        * flag agents who are closely connected with confirmed fraud agents via high-risk connections (e.g. sharing common personal info with each other or common customers)
      *  

## Dataset

* [Kaggle CC Fraud Detection](https://www.kaggle.com/kartik2112/fraud-detection/code?datasetId=817870&sortBy=voteCount&searchQuery=graph): Feb21-27
    * [Kaggle Implementation: NodeToVec](https://www.kaggle.com/jinfeijoy/cc-fraud-graph-analytics)   
    * [create features and generate plot](https://www.kaggle.com/jinfeijoy/cc-fraud-graph-analytics-traditional-method)
* [HEALTHCARE PROVIDER FRAUD DETECTION ANALYSIS](https://www.kaggle.com/rohitrox/healthcare-provider-fraud-detection-analysis): Feb28-Mar6
    * [Graph Analytics for Healthcare Fraud Risk Estimation](http://www.karlbranting.net/papers/FOSINT_Branting_et_al.pdf) 
    * https://medium.com/analytics-vidhya/healthcare-provider-fraud-detection-analysis-using-machine-learning-81ebf09ed955
    * https://rohansoni-jssaten2019.medium.com/healthcare-provider-fraud-detection-and-analysis-machine-learning-6af6366caff2
    * https://towardsdatascience.com/fraud-detection-with-graph-analytics-2678e817b69e
* [yelp fraud reviews](https://paperswithcode.com/dataset/yelpchi)
    
## Reference:

* https://medium.com/@mygreatlearning/graph-machine-learning-for-credit-card-fraud-analysis-f63baf3211e5
* https://towardsdatascience.com/fraud-detection-with-graph-analytics-2678e817b69e
* https://isb-institute-of-data-science.medium.com/knowledge-graph-for-financial-services-c9cb7c3fe2b9
* https://linkurious.com/blog/fraud-use-cases-graph-analytics/
* https://github.com/Zyxelo/GraphEnhancedMachineLearningForFraud 
* https://linkurious.com/blog/stolen-credit-cards-and-fraud-detection-with-neo4j/
* https://neo4j.com/blog/financial-fraud-detection-graph-data-science-analytics-feature-engineering/
