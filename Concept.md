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
  * dom(AN[𝑖]): domain of the 𝑖-th node attribute 
  * dom(AE[𝑖]): domain of the 𝑖-th edge attribute
  * Weight: an edge property
    * "Distance" in a road network
    * "Strength of Connection" in a personal network
    * "Likelihook of interaction" in a biological network
    * "Certainty of information" in a knowledge network 
* Path Analytics
  * Walk: an alternating sequence of vertices and edges over a graph
  * Path: A walk with no repeating node except possibly for the first and last
  * Cycle: A path of length n ≥ 3 whose start and end vertices are the same
  * Acyclic: Graph with no cycles
  * Trail: A walk with no repeating edge
  * Reachability: node 𝑢 is reachable from node 𝑣 if there is a path from 𝑢 to 𝑣
  * Best path from node 1 to node 2:
     * Specification of “best” may include
       • Function to optimize
       • Nodes/edges to traverse
       • Nodes/edges to avoid
       • Preferences to satisfy
     * Method: 
       * Dijkstra
       * Find least weight path: Bi-directional Dijkstra algorithm
       * Goal-Directed Dijkstra
* Connectivity Analytics
  * How “robust” is the graph?
    * How easy is it to “break” the graph by removing a few nodes/edges?
  * How similar is the “structure” of graph G1 to graph G2?
    * What are some computable “features” that can describe the structure of a graph?
    * How can two graphs be compared based on these features? 
* Community Analytics
* Centrality Analytics

![image](https://user-images.githubusercontent.com/16402963/147615746-11c3a4db-2b05-4386-abb2-57aed5878475.png)
![image](https://user-images.githubusercontent.com/16402963/147615909-7b7895a3-e12f-4173-bed1-796415ebcfdd.png)
