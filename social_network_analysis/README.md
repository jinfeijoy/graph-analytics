## Social Network Analytics

### [Centrality](https://networkofthrones.wordpress.com/a-primer-on-network-analysis/)
* Degree Centrality: Do you have many connections?
* Weighted Degree Centrality: Do you have many interactions?
* Eigenvector Centrality: Do you have many connections to important people?
* PageRank Centrality: Do you have many interactions with important people?
* Betweenness Centrality: Do you help to connect different parts of the network?

### Case One: A Game of Thrones
* After compiling an exhaustive list of characters and their nicknames, we generated a network for the first volume, “A Game of Thrones,” by linking two characters each time they appeared within fifteen words of one another. Each link corresponds to an interaction (either direct or indirect) between these characters.
* ![image](https://user-images.githubusercontent.com/16402963/160734201-2c5da042-1662-4f3a-b105-8a68da96f981.png)
* Network science techniques draw out the hidden patterns in this complex relational data. Community detection discovers six main communities in “A Game of Thrones.” A suite of centrality measures highlights the different ways in which characters play essential roles. Prominence in this interaction network corresponds to narrative importance. PageRank’s feedback loop is particularly effective in this regard: encounters between prominent characters accelerate narrative development. PageRank rightly identifies Ned Stark as the clear protagonist of the first book.

### Task
* **Task1**: Implement Game Thrones characters relationship (Apr1 - Apr7)
  * [google colab](https://colab.research.google.com/drive/1UsA0qwJggviZCnEwDq7BN6ch7Q0UzDSB) 
  * ![Screen Shot 2022-04-02 at 9 40 03 PM](https://user-images.githubusercontent.com/16402963/161407577-518ee71b-7d39-4e64-99ef-12704bba835c.png)
  * [Neo4j PageRank Calculation](https://towardsdatascience.com/how-to-get-started-with-the-new-graph-data-science-library-of-neo4j-3c8fff6107b)
  * [Neo4j Bloom](https://medium.com/neo4j/hands-on-with-the-neo4j-graph-data-science-sandbox-7b780be5a44f)
  * [Neo4j Bloom Implementation](https://github.com/jinfeijoy/graph-analytics/blob/main/fraud_detection/neo4j_cypher_code.md)
    * ![image](https://user-images.githubusercontent.com/16402963/161659310-c3969c3a-0250-43e3-8d16-a5dabf968fa7.png)
 
* **Task2**: Find an interesting book and get characters relationship (can be chinese version) (Apr8 - Apr14)

### Reference
* [Social Network Analysis: From Graph Theory to Applications with Python](https://towardsdatascience.com/social-network-analysis-from-theory-to-applications-with-python-d12e9a34c2c7)
* [NETWORK OF THRONES](https://networkofthrones.wordpress.com/)
