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
