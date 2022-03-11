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
    MERGE (b) <- [:Provice_Service] - (p)
    MERGE (p) <- [:Wrok_at] - (ph)
    ```