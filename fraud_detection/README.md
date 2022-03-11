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
## Cases
* An example: insurance claim detection
    * Early Detection
      * example: nodes (policy(unique policy with status)/owner/agent/address/insured/sin), edges (agent-policy, policy-owner, agent-address, owner-address, owner-sin, insured-sin)  
      * 1. e.g. suspicious findings: confired fraud agent with policy/high #of not taken policies selling to duplicated customers/customers sharing address with agent/customers sharing common sin
      * 2. new agent recently appointed: ranking among the top by risk model due to high-risk connections detected by degree centrality and node similarity algorithm, sharing address with confirmed fraud agent, same person as customer sharing common sin
      * terminated the new suspicious agent to avoid futher loss
    * Graph Features: 
      * comminuty size (Size of Community within agent cross-sell)
         * community detection -- (using Union Find algorithm)
         * **find sets of connected nodes in the graph, where every set is a community including multiple nodes and each node is reachable from other nodes**
         * identify agent susbicious patterns (commision fraud), find agent communities with multiple agents selling early lapset/not taken policies to each other (some domain knowledge required), in this case, agent has relationship with customer and policy 
         * features: e.g. nodes (agent/PolicyStatus(This PolicyStatus should be all identical policy)), edge between agent and policy status (HasPolicy), edge between agent (SamePerson), PolicyStatus(NotTake, Lapsed, InforcePremiumPaying)
         * feature value: number of agent in this community
      * Node Similarity (Node Similarity score with misconduct agent)
        * Jaccard Similarity Score
        * measure the similarity between **agent node pairs** based on common neighbors connected 
        * flag agents who are closely connected with confirmed fraud agents via high-risk connections (e.g. sharing common personal info with each other or common customers)
        * features: e.g. nodes (agent/customers/Fraud), edge between agent and customers (connectedByPhone/Email), edge between agent and fraud (hasCase)
      * Degree Centrality (high risk degree centrality score)
        * number of direct connections of nodes in the graph
        * compute the score for agents based on high-risk-connections (e.g. sharing common personal infor with customers) 
        * how agent and customers are connected 
        * features: e.g. nodes (agent/customers), edge (connectedByAddress/Email/Phone)
        * feature value: how many connections this agent has in the graph that we may want to futher look at it 
      * Other features: #customer sharing phone/#customer sharing address/#Policy/#Policy Owned
* Entity resolution: disambiguate records related to real world entities by linking and grouping
  * apply similarity algorithms on personal attribute data to get similarity scores for profile pairs may fail
  * resolve transitive links by graph analytics: community detection, if all clients are in the same community, then they can be reachable to each other, then we determine they are the same person         
* Fraudulent Transactions
  * ![image](https://user-images.githubusercontent.com/16402963/156864780-6ba02d60-31d8-4d60-9438-8ede1bce7910.png)
  * Community Detection -- UnionFind (WCC) algorithm
    * find sets of connected nodes in the graph
    * every set is a community including multiple nodes and each node is reachable from other nodes
    * fraud ring: account community with known fraud account
    * extract account profile -> extract edges (common attributes) -> create communites -> rank communities -> save communities
  * Python-Spark-SQL: PySpark (need to design schema)
    * NetworkX, Pyspark, DL
  * traditional model 
    * features: recent profile change/current debit amount/pattern like add bill and pay immediately/common emails for young accounts/common receivers for young accounts
    * K-means: create K clusters of input data: 
      * find the distance of the records in the test set with each centroid
      * pick top n as alerts (greater than a threshold value=90%)
      * sort them by distance in descending error
    * individual model:
      * for each account, two models are built (IOF, LOF) in parallel 
      * each model's outlier scores are standardized (using its training set and test set)
      * another standardization is performed (once for all IOF, once for all LOF)
      * top alerts are selected (using intersection or max of average)     
## Cypher
* [Neo4j Notes](https://github.com/jinfeijoy/graph-analytics/blob/main/fraud_detection/neo4j_cypher_code.md)
* [Neo4j Python]()

## Dataset

* [Kaggle CC Fraud Detection](https://www.kaggle.com/kartik2112/fraud-detection/code?datasetId=817870&sortBy=voteCount&searchQuery=graph): Feb21-27
    * [Kaggle Implementation: NodeToVec](https://www.kaggle.com/jinfeijoy/cc-fraud-graph-analytics)   
    * [create features and generate plot](https://www.kaggle.com/jinfeijoy/cc-fraud-graph-analytics-traditional-method)
* [HEALTHCARE PROVIDER FRAUD DETECTION ANALYSIS](https://www.kaggle.com/rohitrox/healthcare-provider-fraud-detection-analysis): Feb28-Mar6
    * [Graph Analytics for Healthcare Fraud Risk Estimation](http://www.karlbranting.net/papers/FOSINT_Branting_et_al.pdf) 
    * https://medium.com/analytics-vidhya/healthcare-provider-fraud-detection-analysis-using-machine-learning-81ebf09ed955
    * https://rohansoni-jssaten2019.medium.com/healthcare-provider-fraud-detection-and-analysis-machine-learning-6af6366caff2
    * https://towardsdatascience.com/fraud-detection-with-graph-analytics-2678e817b69e
    * planning:
      * identify duplicated submission (Mar7 - Mar9)
        * Community Size
        * ![image](https://user-images.githubusercontent.com/16402963/157133394-f7c81d2a-b954-47da-bda7-85fcc5dd30ba.png)
        * if only simple compare the same amount/provider/date/pysician, it is more simple to use group by and count N
      * Create Graph Neo4j (Mar10)
      * Node Similarity (similarity score with misconduct provider(provider pair similarity)) (Mar11 - Marh12)
      * Degree Centrality (Service Not Provided) (Mar14 - Mar16)
      * Final Prediction (and node2Vec) (Mar17- Mar18)
      * Cypher code (Mar19 - Mar22)
* [yelp fraud reviews](https://paperswithcode.com/dataset/yelpchi)
    
## Reference:

* https://medium.com/@mygreatlearning/graph-machine-learning-for-credit-card-fraud-analysis-f63baf3211e5
* https://towardsdatascience.com/fraud-detection-with-graph-analytics-2678e817b69e
* https://isb-institute-of-data-science.medium.com/knowledge-graph-for-financial-services-c9cb7c3fe2b9
* https://linkurious.com/blog/fraud-use-cases-graph-analytics/
* https://github.com/Zyxelo/GraphEnhancedMachineLearningForFraud 
* https://linkurious.com/blog/stolen-credit-cards-and-fraud-detection-with-neo4j/
* https://neo4j.com/blog/financial-fraud-detection-graph-data-science-analytics-feature-engineering/
