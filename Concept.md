# Knowledge Graph

### Why Knowledge Graph
* Social Media:
  * Extracting Conversation Threads
  * Finding Interacting Groups
  * Finding influencers in a Community 
* Biological Networks:
  * Discovering Unkown Relationships (Connecting the dots: indirect associations between diseases/exploratory analysis)  
* Human Information Network
  * Match making problems (Job-candidate pairing)
  * Topical Influencer analysis (Who whould have maximal reach for task X)
  * Situation Detection, assessment (Threat detection) 
* Smart Cities
  * Planning for "smart cities"
  * estimating congestion patterns
  * demand response analyses
  * enerty-optimal routing 

### Graph Analytics
* Some Definitions:
  * V: set of vertices 
  * E: set of edges  
  * TN: set of node types 
  * f (TN->V): type assignment to nodes 
  * TE: a set of edge types 
  * g (TE->E): type assignment to edges 
  * AN: set of node attributes 
  * AE: set of edge attributes 
  * dom(AN[π]): domain of the π-th node attribute 
  * dom(AE[π]): domain of the π-th edge attribute
  * Weight: an edge property
    * "Distance" in a road network
    * "Strength of Connection" in a personal network
    * "Likelihook of interaction" in a biological network
    * "Certainty of information" in a knowledge network 
* Path Analytics
  * Walk: an alternating sequence of vertices and edges over a graph
  * Path: A walk with no repeating node except possibly for the first and last
  * Cycle: A path of length n β₯ 3 whose start and end vertices are the same
  * Acyclic: Graph with no cycles
  * Trail: A walk with no repeating edge
  * Reachability: node π’ is reachable from node π£ if there is a path from π’ to π£
  * Best path from node 1 to node 2:
     * Specification of βbestβ may include
       β’ Function to optimize
       β’ Nodes/edges to traverse
       β’ Nodes/edges to avoid
       β’ Preferences to satisfy
     * Method: 
       * Dijkstra
       * Find least weight path: Bi-directional Dijkstra algorithm
       * Goal-Directed Dijkstra
* Connectivity Analytics
  * How βrobustβ is the graph?
    * How easy is it to βbreakβ the graph by removing a few nodes/edges?
  * How similar is the βstructureβ of graph G1 to graph G2?
    * What are some computable βfeaturesβ that can describe the structure of a graph?
    * How can two graphs be compared based on these features? 
* Community Analytics
  * Topics 
    * βStaticβ Analyses
      * What are the communities at time T?
      * Who belong to a community?
      * How closely knit is this community?
    * Temporal/Evolution Analyses
       * How did this community form?
       * Which communities are stable?
       * Find strong transient communities β why did they form or dissolve?
    * Predictive Analyses
      * Is this community likely to grow?
      * Will these nodes continue as a community in future?
      * Are dominant roles emerging in this community?
  * Detecting a Community
    * The internal and external degree of a vertex
      * Internal β within πΆ
      * External β outside πΆ
    * For πΆ to be a community
      * πΉπππ (Intra-cluster density) ππππππ ππ ππππ πππ πΉπππ (Inter-cluster density) ππππππ ππ ππw   
  * Local Properties
    * Clique: the perfect community -- every two distinct vertices in the clique are adjacent
    * Near Cliques
      * n-clique: maximal subgraph such that the distance of each pair of its vertices is not larger than n
      * n-clan: an n-clique in which geodesic distance between nodes in the subgraph is no greater than n 
    * K-core: (dense parts of a graph) maximal subgraph in which each vertex is adjacent to at least k other vertices of the subgraph
  * Modularity: a global measure of cluster quality
    * fraction of the edges within the given groups minus the expected such fraction if edges were distributed at random
    * value of the modularity lies in the range (-1/2, 1) 
  * Evolving Communities 
* Centrality Analytics
  * Centrality and centralization
    * Centrality: measure of importance of a node (or edge) based on its position in the network  
    * Centralization: measure for a network and not a node
  * Different Measures of Centrality
    * Degree centrality: counts the number of edges incident upon a given node normalized by the possible number of edges (# of edges)/(N-1)
    * up Degree Centrality: consider a group as a single entity, count of the number of edges incidenton the group normalized by non-group members (# of eges into the group/# of non-group members)
    * Closeness Centrality: Sum of shortest-path distances from all other nodes(normalized)
      * Low closeness means node has short distance from other nodes
      * Low closeness nodes receive information sooner than other nodes
    * Betweenness Centrality: ratio of pairwise shortest paths thatws throude i and count of all shortest paths in the graph
      * measures fraction of shortest-path commodity flow passing through a node 
    * Eigenvector Centrality: a node is important if its neighbors are important, this measure is "local"
      * page rank is a variant of eigenvector centrality 
    * Katz Centrality
    * ... and many more ...
 

![image](https://user-images.githubusercontent.com/16402963/147615746-11c3a4db-2b05-4386-abb2-57aed5878475.png)
![image](https://user-images.githubusercontent.com/16402963/147615909-7b7895a3-e12f-4173-bed1-796415ebcfdd.png)
