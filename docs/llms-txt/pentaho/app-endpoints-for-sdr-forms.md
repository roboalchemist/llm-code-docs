# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/work-with-the-streamlined-data-refinery/install-and-configure-the-streamlined-data-refinery/app-endpoints-for-sdr-forms.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/install-and-configure-the-streamlined-data-refinery/app-endpoints-for-sdr-forms.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/install-and-configure-the-streamlined-data-refinery/app-endpoints-for-sdr-forms.md

# App endpoints for SDR forms

These are a few API endpoints that you can also use to run the app. To perform a command, alter this example to match your parameters:

```
http://*\{host\}*/pentaho/plugin/*\{pluginID\}*/api/*\{command\}*
```

Here are a couple of examples using some parameters:

* **Genre Selector API**

  ```
  http://localhost:8080/pentaho/plugin/SDR/api/genre
  ```
* **Example Response**

  ```
  {"metadata":[{"colIndex":0,"colType":"String","colName":"GenreID"},{"colIndex":1,"colType":"String","colName":"Genre"}],"queryInfo":{"totalRows":18},"resultset":[["Action","Action"],["Adventure","Adventure"],["Animation","Animation"],["Childrens","Childrens"],["Comedy","Comedy"],["Crime","Crime"],["Documentary","Documentary"],["Drama","Drama"],["Fantasy","Fantasy"],["Film-Noir","Film-Noir"],["Horror","Horror"],["Musical","Musical"],["Mystery","Mystery"],["Romance","Romance"],["Sci-Fi","Sci-Fi"],["Thriller","Thriller"],["War","War"],["Western","Western"]]}
  ```
* **Gender Selector API**

  ```
  http://localhost:8080/pentaho/plugin/SDR/api/gender
  ```
* **Example Response**

  ```
  {"metadata":[{"colIndex":0,"colType":"String","colName":"GenderID"},{"colIndex":1,"colType":"String","colName":"Gender"}],"queryInfo":{"totalRows":2},"resultset":[["M","Male"],["F","Female"]]}
  ```

Here is a list of app endpoint parameters:

| Endpoint               | Description                                                                                                          |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **genre**              | Populates the options for the **genre** selector.                                                                    |
| **gender**             | Populates the options for the **gender** selector.                                                                   |
| **occupation**         | Populates the options for the **occupation** selector.                                                               |
| **income**             | Populates the options for the **income** selector.                                                                   |
| **firstdate**          | Returns the limit dates for the data to be processed.                                                                |
| **data\_source\_name** | Returns the names of all data sources available on the server.                                                       |
| **latest\_requests**   | Returns the latest 10 requests made in a table, instead of inside of a popup.                                        |
| **sdr\_data**          | Processes the request and returns the status of the data.                                                            |
| **refresh**            | Refreshes the kettle and dashboard elements to reflect any saved changes. Clears the cache for all kettle endpoints. |
