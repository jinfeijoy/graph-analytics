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



### Reference
* [Social Network Analysis: From Graph Theory to Applications with Python](https://towardsdatascience.com/social-network-analysis-from-theory-to-applications-with-python-d12e9a34c2c7)
* [NETWORK OF THRONES](https://networkofthrones.wordpress.com/)
