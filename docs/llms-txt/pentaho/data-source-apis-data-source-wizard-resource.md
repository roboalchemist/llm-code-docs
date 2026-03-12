# Source: https://docs.pentaho.com/rest-api/data-source-apis-data-source-wizard-resource.md

# Data Source APIs   Data Source Wizard Resource

This service allows for listing, downloading, and removal of DSW data sources in the BA Platform.

## Get list of DSW datasource IDs

> Get a list of Data Source Wizard (DSW) datasource ids.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/plugin/data-access/api/datasource/dsw/domain\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Data Source APIs - Data Source Wizard Resource","description":"This service allows for listing, downloading, and removal of DSW data sources in the BA Platform."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/data-access/api/datasource/dsw/domain":{"get":{"tags":["Data Source APIs - Data Source Wizard Resource"],"summary":"Get list of DSW datasource IDs","description":"Get a list of Data Source Wizard (DSW) datasource ids.\n\n**Example Request:**\n```\nGET pentaho/plugin/data-access/api/datasource/dsw/domain\n```\n","responses":{"200":{"description":"Successfully retrieved the list of DSW IDs","content":{"application/xml":{"schema":{"type":"object","description":"List of DSW IDs in XML format"}},"application/json":{"schema":{"type":"object","description":"List of DSW IDs in JSON format"}}}}}}}}}
````

## Export DSW data source

> Export the DSW data source for the given DSW ID. The response will be zipped if there is\
> more than one file. The response will contain an XMI and/or a mondrian cube definition file.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/plugin/data-access/api/datasource/dsw/domain/jmeter-dsw-pentaho-test.xmi\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Data Source APIs - Data Source Wizard Resource","description":"This service allows for listing, downloading, and removal of DSW data sources in the BA Platform."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/data-access/api/datasource/dsw/domain/{dswId}":{"get":{"tags":["Data Source APIs - Data Source Wizard Resource"],"summary":"Export DSW data source","description":"Export the DSW data source for the given DSW ID. The response will be zipped if there is\nmore than one file. The response will contain an XMI and/or a mondrian cube definition file.\n\n**Example Request:**\n```\nGET pentaho/plugin/data-access/api/datasource/dsw/domain/jmeter-dsw-pentaho-test.xmi\n```\n","parameters":[{"name":"dswId","in":"path","description":"The id of the DSW datasource to export","required":true,"schema":{"type":"string"}}],"responses":{"200":{"description":"DSW datasource export succeeded","content":{"application/octet-stream":{"schema":{"type":"string","format":"binary","description":"An encrypted .XMI file or a .zip with encoded .XMI files"}}}},"401":{"description":"User is not authorized to export DSW datasource","content":{"text/plain":{"schema":{"type":"string","description":"Unauthorized access error"}}}},"500":{"description":"Failure to export DSW datasource","content":{"text/plain":{"schema":{"type":"string","description":"Internal server error"}}}}}}}}}
````

## Remove DSW data source

> Remove the DSW data source for a given DSW ID.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> DELETE pentaho/plugin/data-access/api/datasource/dsw/domain/jmeter-dsw-pentaho-test.xmi\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Data Source APIs - Data Source Wizard Resource","description":"This service allows for listing, downloading, and removal of DSW data sources in the BA Platform."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/data-access/api/datasource/dsw/domain/{dswId}":{"delete":{"tags":["Data Source APIs - Data Source Wizard Resource"],"summary":"Remove DSW data source","description":"Remove the DSW data source for a given DSW ID.\n\n**Example Request:**\n```\nDELETE pentaho/plugin/data-access/api/datasource/dsw/domain/jmeter-dsw-pentaho-test.xmi\n```\n","parameters":[{"name":"dswId","in":"path","description":"The id of the DSW datasource to remove","required":true,"schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully removed the DSW data source","content":{"text/plain":{"schema":{"type":"string","description":"Success message"}}}},"401":{"description":"User is not authorized to delete the DSW datasource","content":{"text/plain":{"schema":{"type":"string","description":"Unauthorized access error"}}}},"500":{"description":"Failure to remove DSW data source","content":{"text/plain":{"schema":{"type":"string","description":"Internal server error"}}}}}}}}}
````
