# Graph Neural Network

## Embedding:
* How does the GNN create the graph embedding? When the graph data is passed to the GNN, the features of each node are combined with those of its neighboring nodes. This is called “message passing.” If the GNN is composed of more than one layer, then subsequent layers repeat the message-passing operation, gathering data from neighbors of neighbors and aggregating them with the values obtained from the previous layer. For example, in a social network, the first layer of the GNN would combine the data of the user with those of their friends, and the next layer would add data from the friends of friends and so on. Finally, the output layer of the GNN produces the embedding, which is a vector representation of the node’s data and its knowledge of other nodes in the graph.
* Summary
  * Graph embedding classification 
    * whole graph embedding: this can be used when studying several graphs, such as molecules in chemistry
    * node embedding: is actually the most famous of all graph embedding technique and is often called “graph embedding”.
  * Transductive or inductive embedding
    * Transductive embedding: a low-dimension vector representation is derived for each node in a graph, but it is not possible to find the vector representation for a new node. In data science terms, the algorithm can not make prediction based on unknown data.
    * Inductive embedding on the other hand is more consistent with the training/prediction model we are used to see in Machine Learning. 
  * Matrix factorization
    * Locally Linear Embedding.
    * HOPE
  * Graph traversal & Random Walk & DeepWalk

## GNN
* ![image](https://user-images.githubusercontent.com/16402963/166850171-a7a2d4ce-e7bf-417d-aff9-c0b1aea4e5b4.png)
* Difficuties for graph data to fit Neural Networks:
  * Neural Networks requires fixed size input
  * ![image](https://user-images.githubusercontent.com/16402963/166850373-9b493e43-838b-4d32-84a4-25530fcbdd4c.png)
* Fundemental Idea of GNNs
  * ![image](https://user-images.githubusercontent.com/16402963/166850505-977c1031-a396-4e57-a89d-3291a9a578f3.png)
* How do Graph Neural Networks work
  * core GNN: message passing layers: combine node and edge information to node embeddings
  * ![image](https://user-images.githubusercontent.com/16402963/166850596-f97945a2-1640-4817-b2fc-7592d4ec89ec.png)
* What is happening in the Message Passing Layers: every single node knows something about other node (we know the neighbor first, then know the neighbor of the neighbors)
  * ![image](https://user-images.githubusercontent.com/16402963/166851058-3570b1b3-891c-4cda-a977-ba7d319398d1.png)
    * The local feature aggregation can be compared to learnable CNN kernels
* Computation Graph Representation
  * the number of layers in GNN defines how many of neighborhoods we perform
  * the number of MP-layers is a hyperparameter dependent on the graph data
* Over-smoothing in GNNs: too many layers may lead to over-smoothing
* Message Passing Update and Aggregation Functions
  * ![image](https://user-images.githubusercontent.com/16402963/166851558-ab040c68-3813-4a5e-b852-c54b97d1f668.png)
* **[Graph Representation Learning](https://www.cs.mcgill.ca/~wlh/grl_book/files/GRL_Book.pdf)**
* **[Graph neural networks: A review of methods and applications](https://arxiv.org/ftp/arxiv/papers/1812/1812.08434.pdf)**
  * The general design pipeline for GNN model:
    ![image](https://user-images.githubusercontent.com/16402963/166852662-f6884552-10ac-4d89-9787-c46055eac3bc.png)
* Python Packages
  ![image](https://user-images.githubusercontent.com/16402963/167731048-f52d8c6c-9aec-4fb8-97e8-b090f891b813.png)
* Model Explain
  * ![image](https://user-images.githubusercontent.com/16402963/167732936-1ff0816e-fcef-4894-acbb-7401d9d802cf.png)
  * [DIG: Dive into Graphs](https://diveintographs.readthedocs.io/en/latest/)


## Recommendation System:
* recommendation system with graph database: 
  * Bipartite Graph 
    * Link Prediction: 
      * ![image](https://user-images.githubusercontent.com/16402963/168924052-3f368e2d-7bbc-40ea-b91d-afe9569b4977.png)
    * Sample neighborhood / Aggregate feature information from neighbors / predict graph context and label using aggregated information
      * ![image](https://user-images.githubusercontent.com/16402963/168924422-fe142f78-fe87-418b-8aff-23aff1cef191.png)
  * Social Recommendation 
    * ![image](https://user-images.githubusercontent.com/16402963/168924535-b1cb049a-4f54-4b24-92fc-94d2f59df2f6.png)
  * Knowledge Graph Based Recommendation (Dynamic Graph)
    * ![image](https://user-images.githubusercontent.com/16402963/168924608-d9271639-2eaf-4c39-90cc-10cfa9c3146a.png)
    * ![image](https://user-images.githubusercontent.com/16402963/168924647-031734a2-cde7-41f1-89ca-f31e68db68d5.png)
   
* real time recommendation system: 
  * [Real-time Machine Learning For Recommendations](https://eugeneyan.com/writing/real-time-recommendations/) 

## Planning
* [Link Prediction](https://medium.com/@benalex/implement-your-own-music-recommender-with-graph-neural-networks-lightgcn-f59e3bf5f8f5): 22May17 - 22May27
* Social Recommendation: 22May28 - 22Jun4
* Real Time Recommendation: 

## Reference:
* **[Graph-based Fraud Detection Papers and Resources](https://github.com/safe-graph/graph-fraud-detection-papers)**
* [Top Trends of Graph Machine Learning in 2020](https://towardsdatascience.com/top-trends-of-graph-machine-learning-in-2020-1194175351a3)
* [Graph ML in 2022: Where Are We Now?](https://towardsdatascience.com/graph-ml-in-2022-where-are-we-now-f7f8242599e0) 
* [Graph Embedding](https://dmccreary.medium.com/understanding-graph-embeddings-79342921a97f) 
* [Graph embedding techniques](https://medium.com/@st3llasia/graph-embedding-techniques-7d5386c88c5)
* [Building a Recommender System Using Graph Neural Networks](https://medium.com/decathlontechnology/building-a-recommender-system-using-graph-neural-networks-2ee5fc4e706d)
* [Graph Neural Networks Model and Application (Youtube)](https://www.youtube.com/watch?v=zCEYiCxrL_0)
* Understanding Graph Neural Networks [Part1](https://www.youtube.com/watch?v=fOctJB4kVlM)// [Part2](https://www.youtube.com/watch?v=ABCGCf8cJOE&list=PLV8yxwGOxvvoNkzPfCx2i8an--Tkt7O8Z&index=2)// [Part3](https://www.youtube.com/watch?v=0YLZXjMHA-8&list=PLV8yxwGOxvvoNkzPfCx2i8an--Tkt7O8Z&index=3) //[Other GNN in This Playlist](https://www.youtube.com/playlist?list=PLV8yxwGOxvvoNkzPfCx2i8an--Tkt7O8Z)
* Real-time Recommendation:
   * [Real-time Recommendation System: Rolling Feature Matrix](https://towardsdatascience.com/real-time-recommendation-system-rolling-feature-matrix-f5ca701439df)
   * [LSTM for real-time recommendation systems](https://bond-kirill-alexandrovich.medium.com/lstm-for-real-time-recommendation-systems-f5191d564be5)
   * [Graph-based real-time recommendation systems](https://medium.com/quantyca/graph-based-real-time-recommendation-systems-8a6b3909b603)
   * [Real-time Machine Learning For Recommendations](https://eugeneyan.com/writing/real-time-recommendations/)
   * [An introduction to product recommender systems](https://www.dynamicyield.com/lesson/introduction-to-product-recommender-systems/)
   * [Recommender Systems For Business - A Gentle Introduction](https://www.width.ai/post/recommender-systems-recommendation-systems)
   * [Recommender Systems: Behind the Scenes of Machine Learning-Based Personalization](https://www.altexsoft.com/blog/recommender-system-personalization/)
