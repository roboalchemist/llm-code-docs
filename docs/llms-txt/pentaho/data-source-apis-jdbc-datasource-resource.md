# Source: https://docs.pentaho.com/rest-api/data-source-apis-jdbc-datasource-resource.md

# Data Source APIs   JDBC Datasource Resource

This service provides methods for listing, creating, downloading, uploading, and removal of JDBC data sources.

## Get list of JDBC datasource IDs

> Get a list of JDBC datasource IDs.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/plugin/data-access/api/datasource/jdbc/connection\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/plugin/data-access/api/datasource/jdbc/connection>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Accept: application/json"\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Data Source APIs - JDBC Datasource Resource","description":"This service provides methods for listing, creating, downloading, uploading, and removal of JDBC data sources."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/data-access/api/datasource/jdbc/connection":{"get":{"tags":["Data Source APIs - JDBC Datasource Resource"],"summary":"Get list of JDBC datasource IDs","description":"Get a list of JDBC datasource IDs.\n\n**Example Request:**\n```\nGET pentaho/plugin/data-access/api/datasource/jdbc/connection\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/plugin/data-access/api/datasource/jdbc/connection\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Accept: application/json\"\n```\n","responses":{"200":{"description":"Successfully retrieved the list of JDBC datasource IDs","content":{"application/xml":{"schema":{"type":"object","description":"List of JDBC datasource IDs in XML format"}},"application/json":{"schema":{"type":"object","description":"List of JDBC datasource IDs in JSON format"}}}},"500":{"description":"Internal error retrieving JDBC datasource IDs","content":{"text/plain":{"schema":{"type":"string","description":"Internal server error"}}}}}}}}}
````

## Add or update a JDBC datasource connection

> Add or update a JDBC datasource connection.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> PUT pentaho/plugin/data-access/api/datasource/jdbc/connection/TestDatasource\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X PUT \\\
> &#x20; "<http://localhost:8080/pentaho/plugin/data-access/api/datasource/jdbc/connection/TestDatasource>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Content-Type: application/json" \\\
> &#x20; -d '{\
> &#x20;   "changed": true,\
> &#x20;   "usingConnectionPool": true,\
> &#x20;   "connectSql": "",\
> &#x20;   "databaseName": "SampleData",\
> &#x20;   "databasePort": "9001",\
> &#x20;   "hostname": "localhost",\
> &#x20;   "name": "TestDataSourceResource",\
> &#x20;   "password": "password",\
> &#x20;   "username": "pentaho\_user",\
> &#x20;   "attributes": {},\
> &#x20;   "connectionPoolingProperties": {},\
> &#x20;   "extraOptions": {},\
> &#x20;   "accessType": "NATIVE",\
> &#x20;   "databaseType": {\
> &#x20;     "defaultDatabasePort": 9001,\
> &#x20;     "extraOptionsHelpUrl": "<http://hsqldb.sourceforge.net/doc/guide/ch04.html#N109DA",\\>
> &#x20;     "name": "Hypersonic",\
> &#x20;     "shortName": "HYPERSONIC",\
> &#x20;     "supportedAccessTypes": \["NATIVE", "ODBC", "JNDI"]\
> &#x20;   }\
> &#x20; }'\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Data Source APIs - JDBC Datasource Resource","description":"This service provides methods for listing, creating, downloading, uploading, and removal of JDBC data sources."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"DatabaseConnection":{"type":"object","description":"Database connection configuration","properties":{"id":{"type":"string","description":"Unique identifier for the database connection"},"name":{"type":"string","description":"Name of the database connection"},"hostname":{"type":"string","description":"Database server hostname"},"databaseName":{"type":"string","description":"Name of the database"},"databasePort":{"type":"string","description":"Database server port"},"username":{"type":"string","description":"Database username"},"password":{"type":"string","description":"Database password (may be encrypted or nullified for security)"},"accessType":{"type":"string","description":"Type of database access"},"accessTypeValue":{"type":"string","description":"Value for the access type"},"connectSql":{"type":"string","description":"SQL to execute on connection"},"usingConnectionPool":{"type":"boolean","description":"Whether to use connection pooling"},"initialPoolSize":{"type":"integer","description":"Initial connection pool size"},"maximumPoolSize":{"type":"integer","description":"Maximum connection pool size"},"partitioned":{"type":"boolean","description":"Whether the database is partitioned"},"changed":{"type":"boolean","description":"Whether the connection has been modified"},"quoteAllFields":{"type":"boolean","description":"Whether to quote all field names"},"streamingResults":{"type":"boolean","description":"Whether to use streaming results"},"forcingIdentifiersToLowerCase":{"type":"boolean","description":"Whether to force identifiers to lowercase"},"forcingIdentifiersToUpperCase":{"type":"boolean","description":"Whether to force identifiers to uppercase"},"usingDoubleDecimalAsSchemaTableSeparator":{"type":"boolean","description":"Whether to use double decimal as schema table separator"},"dataTablespace":{"type":"string","description":"Data tablespace name"},"indexTablespace":{"type":"string","description":"Index tablespace name"},"informixServername":{"type":"string","description":"Informix server name"},"SQLServerInstance":{"type":"string","nullable":true,"description":"SQL Server instance name"},"attributes":{"type":"object","description":"Additional connection attributes","additionalProperties":{"type":"string"}},"connectionPoolingProperties":{"type":"object","description":"Connection pooling properties","additionalProperties":{"type":"string"}},"extraOptions":{"type":"object","description":"Extra connection options","additionalProperties":{"type":"string"}},"databaseType":{"type":"object","description":"Database type information","properties":{"name":{"type":"string","description":"Database type name"},"shortName":{"type":"string","description":"Short name for the database type"},"defaultDatabasePort":{"type":"integer","description":"Default port for this database type"},"extraOptionsHelpUrl":{"type":"string","description":"URL for extra options help"},"supportedAccessTypes":{"type":"array","description":"Supported access types for this database","items":{"type":"string"}}}}}}}},"paths":{"/data-access/api/datasource/jdbc/connection/{connectionId}":{"put":{"tags":["Data Source APIs - JDBC Datasource Resource"],"summary":"Add or update a JDBC datasource connection","description":"Add or update a JDBC datasource connection.\n\n**Example Request:**\n```\nPUT pentaho/plugin/data-access/api/datasource/jdbc/connection/TestDatasource\n```\n\n**cURL Example:**\n```bash\ncurl -X PUT \\\n  \"http://localhost:8080/pentaho/plugin/data-access/api/datasource/jdbc/connection/TestDatasource\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Content-Type: application/json\" \\\n  -d '{\n    \"changed\": true,\n    \"usingConnectionPool\": true,\n    \"connectSql\": \"\",\n    \"databaseName\": \"SampleData\",\n    \"databasePort\": \"9001\",\n    \"hostname\": \"localhost\",\n    \"name\": \"TestDataSourceResource\",\n    \"password\": \"password\",\n    \"username\": \"pentaho_user\",\n    \"attributes\": {},\n    \"connectionPoolingProperties\": {},\n    \"extraOptions\": {},\n    \"accessType\": \"NATIVE\",\n    \"databaseType\": {\n      \"defaultDatabasePort\": 9001,\n      \"extraOptionsHelpUrl\": \"http://hsqldb.sourceforge.net/doc/guide/ch04.html#N109DA\",\n      \"name\": \"Hypersonic\",\n      \"shortName\": \"HYPERSONIC\",\n      \"supportedAccessTypes\": [\"NATIVE\", \"ODBC\", \"JNDI\"]\n    }\n  }'\n```\n","parameters":[{"name":"connectionId","in":"path","required":true,"description":"The ID of the JDBC datasource to add or update","schema":{"type":"string"}}],"requestBody":{"required":true,"content":{"application/json":{"schema":{"$ref":"#/components/schemas/DatabaseConnection"}}}},"responses":{"204":{"description":"JDBC datasource added successfully."},"304":{"description":"Datasource was not modified"},"401":{"description":"User is not authorized to add JDBC datasources.","content":{"text/plain":{"schema":{"type":"string","description":"Unauthorized access error"}}}},"500":{"description":"An unexpected error occurred while adding the JDBC datasource.","content":{"text/plain":{"schema":{"type":"string","description":"Internal server error"}}}}}}}}}
````

## Export a JDBC datasource connection

> Export a JDBC datasource connection.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/plugin/data-access/api/datasource/jdbc/connection/TestDataSourceResource\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/plugin/data-access/api/datasource/jdbc/connection/TestDataSourceResource>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Accept: application/json"\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Data Source APIs - JDBC Datasource Resource","description":"This service provides methods for listing, creating, downloading, uploading, and removal of JDBC data sources."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"DatabaseConnection":{"type":"object","description":"Database connection configuration","properties":{"id":{"type":"string","description":"Unique identifier for the database connection"},"name":{"type":"string","description":"Name of the database connection"},"hostname":{"type":"string","description":"Database server hostname"},"databaseName":{"type":"string","description":"Name of the database"},"databasePort":{"type":"string","description":"Database server port"},"username":{"type":"string","description":"Database username"},"password":{"type":"string","description":"Database password (may be encrypted or nullified for security)"},"accessType":{"type":"string","description":"Type of database access"},"accessTypeValue":{"type":"string","description":"Value for the access type"},"connectSql":{"type":"string","description":"SQL to execute on connection"},"usingConnectionPool":{"type":"boolean","description":"Whether to use connection pooling"},"initialPoolSize":{"type":"integer","description":"Initial connection pool size"},"maximumPoolSize":{"type":"integer","description":"Maximum connection pool size"},"partitioned":{"type":"boolean","description":"Whether the database is partitioned"},"changed":{"type":"boolean","description":"Whether the connection has been modified"},"quoteAllFields":{"type":"boolean","description":"Whether to quote all field names"},"streamingResults":{"type":"boolean","description":"Whether to use streaming results"},"forcingIdentifiersToLowerCase":{"type":"boolean","description":"Whether to force identifiers to lowercase"},"forcingIdentifiersToUpperCase":{"type":"boolean","description":"Whether to force identifiers to uppercase"},"usingDoubleDecimalAsSchemaTableSeparator":{"type":"boolean","description":"Whether to use double decimal as schema table separator"},"dataTablespace":{"type":"string","description":"Data tablespace name"},"indexTablespace":{"type":"string","description":"Index tablespace name"},"informixServername":{"type":"string","description":"Informix server name"},"SQLServerInstance":{"type":"string","nullable":true,"description":"SQL Server instance name"},"attributes":{"type":"object","description":"Additional connection attributes","additionalProperties":{"type":"string"}},"connectionPoolingProperties":{"type":"object","description":"Connection pooling properties","additionalProperties":{"type":"string"}},"extraOptions":{"type":"object","description":"Extra connection options","additionalProperties":{"type":"string"}},"databaseType":{"type":"object","description":"Database type information","properties":{"name":{"type":"string","description":"Database type name"},"shortName":{"type":"string","description":"Short name for the database type"},"defaultDatabasePort":{"type":"integer","description":"Default port for this database type"},"extraOptionsHelpUrl":{"type":"string","description":"URL for extra options help"},"supportedAccessTypes":{"type":"array","description":"Supported access types for this database","items":{"type":"string"}}}}}}}},"paths":{"/data-access/api/datasource/jdbc/connection/{name}":{"get":{"tags":["Data Source APIs - JDBC Datasource Resource"],"summary":"Export a JDBC datasource connection","description":"Export a JDBC datasource connection.\n\n**Example Request:**\n```\nGET pentaho/plugin/data-access/api/datasource/jdbc/connection/TestDataSourceResource\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/plugin/data-access/api/datasource/jdbc/connection/TestDataSourceResource\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Accept: application/json\"\n```\n","parameters":[{"name":"name","in":"path","required":true,"description":"The name of the JDBC datasource to retrieve","schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully retrieved the JDBC datasource","content":{"application/xml":{"schema":{"$ref":"#/components/schemas/DatabaseConnection"}},"application/json":{"schema":{"$ref":"#/components/schemas/DatabaseConnection"}}}},"500":{"description":"An error occurred retrieving the JDBC datasource","content":{"text/plain":{"schema":{"type":"string","description":"Internal server error"}}}}}}}}}
````

## Remove JDBC datasource by name

> Remove the JDBC data source for a given JDBC name.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> DELETE pentaho/plugin/data-access/api/datasource/jdbc/connection/TestDataSourceResource\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X DELETE \\\
> &#x20; "<http://localhost:8080/pentaho/plugin/data-access/api/datasource/jdbc/connection/TestDataSourceResource>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Data Source APIs - JDBC Datasource Resource","description":"This service provides methods for listing, creating, downloading, uploading, and removal of JDBC data sources."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/data-access/api/datasource/jdbc/connection/{name}":{"delete":{"tags":["Data Source APIs - JDBC Datasource Resource"],"summary":"Remove JDBC datasource by name","description":"Remove the JDBC data source for a given JDBC name.\n\n**Example Request:**\n```\nDELETE pentaho/plugin/data-access/api/datasource/jdbc/connection/TestDataSourceResource\n```\n\n**cURL Example:**\n```bash\ncurl -X DELETE \\\n  \"http://localhost:8080/pentaho/plugin/data-access/api/datasource/jdbc/connection/TestDataSourceResource\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n","parameters":[{"name":"name","in":"path","required":true,"description":"The name of the JDBC datasource to remove","schema":{"type":"string"}}],"responses":{"204":{"description":"JDBC datasource removed successfully."},"304":{"description":"User is not authorized to remove the JDBC datasource or the connection does not exist."},"500":{"description":"An unexpected error occurred while deleting the JDBC datasource.","content":{"text/plain":{"schema":{"type":"string","description":"Internal server error"}}}}}}}}}
````
