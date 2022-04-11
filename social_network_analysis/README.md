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
  * Using **Gephi** can generate the similar plot as the 1st plot, export data from neoj to gephi can be found [here](https://neo4j.com/labs/apoc/4.1/export/gephi/), cookbook sample can be found [here](https://subscription.packtpub.com/book/big_data_/9781783987405/7/ch07lvl1sec83/previewing-and-fine-tuning-a-graph-in-the-default-curved-mode)
* **Task2**: Find an interesting book and get characters relationship (can be chinese version) (Apr7 - Apr14)
  * json file to neo4j (Apr7-9)
  * Explore 'honglou' code -- text processing (Apr11)
  * hands on 'honglou' (more plan after explore sample code)

### Reference
* [Social Network Analysis: From Graph Theory to Applications with Python](https://towardsdatascience.com/social-network-analysis-from-theory-to-applications-with-python-d12e9a34c2c7)
* [NETWORK OF THRONES](https://networkofthrones.wordpress.com/)
* [红楼梦](http://www.openkg.cn/dataset/honglou)
  * [人物关系图](https://echoma.github.io/novel_datamation/story_of_stone/graph.html)
  * [人物列表](https://www.wiki.zh-cn.nina.az/%E7%BA%A2%E6%A5%BC%E6%A2%A6%E4%BA%BA%E7%89%A9%E5%88%97%E8%A1%A8.html)
  * [文本分析](http://rstudio-pubs-static.s3.amazonaws.com/227559_ee7a18cc09364b9f8630de94cc12e9e2.html)
  * [知识图谱](https://blog.csdn.net/RHJlife/article/details/108586578) 
  * [graph dataset](https://github.com/echoma/think_before_act/tree/master/ss_wiki/1st/source/01_stone_story)
