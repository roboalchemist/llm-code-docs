# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mongodb-input/options-mongodb-input/input-options-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mongodb-input/options-mongodb-input/input-options-tab.md

# Input options tab

![Input options tab in Mongo Input](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-2194d871faf9a16357298ab1ca2467b76bc4d31d%2FPDI_TransStep_MongoDB_Input_Input_Options_Tab.png?alt=media)

In the **Input options** tab, specify which database and collection you want to retrieve information from. You can also indicate the read preferences and tag sets.

Enter the following information in the **Input options** fields:

| Option              | Definition                                                                                                                                            |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Database**        | Name of the database to retrieve data from. Click Get **DBs** to populate the drop-down menu with a list of databases on the server.                  |
| **Collection**      | Name of the collection to retrieve data from. Click **Get collections**to populate the drop-down menu with a list of collections within the database. |
| **Read preference** | Specify which node to read first: **primary**,**primary preferred**, **secondary**, **secondary preferred**, or **nearest**.                          |
