# Cypher code

## Load Data (csv file)
* the line can be found [here](https://neo4j.com/docs/cypher-manual/current/clauses/load-csv/), and medium size csv file from [here](https://neo4j.com/developer/guide-import-csv/#_load_csv_for_medium_sized_datasets)
* [Importing csv file in neo4j](https://towardsdatascience.com/importing-csv-files-in-neo4j-f3553f1a76cf)
* save data to file location, for example here is "C:\Users\luoyan011\.Neo4jDesktop\relate-data\dbmss\dbms-d9142c37-be6a-45de-b65e-5e1dcc81ad69"
* load file and print: 
  ```buildoutcfg
  LOAD CSV WITH HEADERS FROM "file:///top_3_community.csv" AS line WITH line RETURN line LIMIT 5
  ```
* load file and create graph db: 
    ```buildoutcfg
    LOAD CSV WITH HEADERS FROM "file:///top_3_community.csv" AS line
    CREATE (a:test {BeneID: line.BeneID, 
                   ClaimID: line.ClaimID, 
                   ClaimStartDt: line.ClaimStartDt, 
                   ClaimEndDt: line.ClaimEndDt, 
                   Provider: line.Provider, 
                   ClaimAmt: TOINTEGER(line.InscClaimAmtReimbursed), 
                   Physician: line.AttendingPhysician, 
                   DeductAmt: TOINTEGER(line.DeductibleAmtPaid), 
                   ClmCode: line.ClmDiagnosisCode_1, 
                   Fraud: line.PotentialFraud
                   })
    ```
* match variable 
  * **a:test** is the label, Provider and Physician are two of the property of each node,  
  *
    ```buildoutcfg
    MATCH (a:test {Provider:'PRV55215'}) RETURN a.Physician
    ```
* merge data and create relationship
  * ```buildoutcfg
    LOAD CSV WITH HEADERS FROM "file:///top_3_community.csv" AS ROW
    MERGE (c: Claim {ID: ROW.ClaimID})
    MERGE (b: Beneficial {ID: ROW.BeneID})
    MERGE (p: Provider {ID: ROW.Provider, Label:ROW.PotentialFraud})
    MERGE (ph: Physician {ID: ROW.AttendingPhysician})
    MERGE (c) - [:Link_to] - (b)
    MERGE (c) - [:Link_to] - (p)
    MERGE (c) - [:Link_to] - (ph)
    MERGE (b) <- [:Provice_Service] - (p)
    MERGE (p) <- [:Wrok_at] - (ph)
    ```

## Calculations
* Similarity Calculation
  * https://www.markhneedham.com/blog/2018/09/28/neo4j-graph-algorithms-cosine-game-of-thrones/
  
* Find degree of node Provider:
  * ```buildoutcfg
    MATCH (n:Provider)-[r]-()
    RETURN n.ID, count(distinct r) as degree
    ORDER by degree
    ```
* Find 2nd neighbors of 'BENE27147'
  * ```buildoutcfg
    MATCH (b)-[:Link_to*..2]-(c)
    WHERE b.ID='BENE27147'
    RETURN distinct b, c
    ```
* [Path analytics](https://www.coursera.org/learn/big-data-graph-analytics/supplement/b0Z7F/path-analytics-in-neo4j-with-cypher-supplementary-resources)
* Same Node Different Pair Similarity
  * [Jaccard Similarity Calculation](https://stackoverflow.com/questions/49503383/computing-similarity-between-all-nodes-neo4j-getting-different-values-for-a-no)
  ```buildoutcfg
  MATCH (p:Provider) WITH COLLECT(p) AS Providers
  UNWIND Providers as provider1
  UNWIND Providers as provider2 
  
  MATCH(provider1)-[:Provice_Service]->(common_bene:Beneficial)<-[:Provice_Service]-(provider2) WHERE ID(provider1) > ID(provider2)
  WITH provider1, provider2, COLLECT(common_bene) AS intersection_bene
  
  MATCH (provider1)-[:Provice_Service]->(pv1_b:Beneficial)
  WITH provider1, provider2, intersection_bene, 
       COLLECT(pv1_b) AS s1
  
  MATCH (provider2)-[:Provice_Service]->(pv2_b:Beneficial)
  WITH provider1,provider2,intersection_bene, s1, 
       COLLECT(pv2_b) AS s2
  
  RETURN provider1, provider2,
         (1.0 * SIZE(intersection_bene)) / (SIZE(s1) + SIZE(s2) - SIZE(intersection_bene)) AS jaccard
  ````
  * [Jaccard Similarity Function](https://neo4j.com/docs/graph-data-science/current/alpha-algorithms/jaccard/)
  ```buildoutcfg
  MATCH (p:Provider) WITH COLLECT(p) AS Providers
  UNWIND Providers as provider1
  UNWIND Providers as provider2 
  
  MATCH(provider1)-[:Provice_Service]->(common_bene:Beneficial)<-[:Provice_Service]-(provider2) WHERE ID(provider1) > ID(provider2)
  WITH provider1, provider2, COLLECT(common_bene) AS intersection_bene
  
  MATCH (provider1)-[:Provice_Service]->(pv1_b:Beneficial)
  WITH provider1, provider2, intersection_bene, 
       COLLECT(id(pv1_b)) AS s1
  
  MATCH (provider2)-[:Provice_Service]->(pv2_b:Beneficial)
  WITH provider1,provider2,intersection_bene, s1, 
       COLLECT(id(pv2_b)) AS s2
  
  RETURN provider1.ID, provider1.Label,
        provider2.ID, provider2.Label,
       gds.alpha.similarity.jaccard(s1, s2) AS similarity
  ```

## Example: Entity Resolution
* Object: to detect same person with different name due to typo or initial
* Create graph database:
    ```buildoutcfg
    LOAD CSV WITH HEADERS FROM "file:///wh_visitor_clean_data.csv" AS ROW
    MERGE (c: caller {NAME: ROW.CALLER_NAME})
    MERGE (v: visitor {NAME: ROW.VISITOR_NAME})
    MERGE (vf: visitor_nf {NAME: ROW.NAMEFIRST})
    MERGE (vm: visitor_nm {NAME: ROW.NAMEMID})
    MERGE (vl: visitor_nl {NAME: ROW.NAMELAST})
    MERGE (c) - [:Link_to] - (v)
    MERGE (v) - [:same_lastname] - (vl)
    MERGE (v) - [:same_midname] - (vm)
    MERGE (v) - [:same_firstname] - (vf)
    ```
* Show same person example:
  ![image](https://user-images.githubusercontent.com/16402963/159086215-546df4c0-ae96-42e5-b039-d2e14a62ccd6.png)

* 
