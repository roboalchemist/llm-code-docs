# Source: https://docs.pentaho.com/rest-api/data-source-apis-analysis-resource.md

# Data Source APIs   Analysis Resource

This service allows for listing, downloading, uploading, and removal of Analysis files or Mondrian schemas in the BA Platform.

## Get list of analysis data source IDs

> Get a list of analysis data source ids.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/plugin/data-access/api/datasource/analysis/catalog\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Data Source APIs - Analysis Resource","description":"This service allows for listing, downloading, uploading, and removal of Analysis files or Mondrian schemas in the BA Platform."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/data-access/api/datasource/analysis/catalog":{"get":{"tags":["Data Source APIs - Analysis Resource"],"summary":"Get list of analysis data source IDs","description":"Get a list of analysis data source ids.\n\n**Example Request:**\n```\nGET pentaho/plugin/data-access/api/datasource/analysis/catalog\n```\n","responses":{"200":{"description":"Successfully retrieved the list of analysis IDs","content":{"application/xml":{"schema":{"type":"object","description":"List of catalog IDs in XML format"}},"application/json":{"schema":{"type":"object","description":"List of catalog IDs in JSON format"}}}}}}}}}
````

## Download analysis schema file

> Download the analysis files for a given analysis id.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/plugin/data-access/api/datasource/analysis/catalog/SampleSchema\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Data Source APIs - Analysis Resource","description":"This service allows for listing, downloading, uploading, and removal of Analysis files or Mondrian schemas in the BA Platform."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/data-access/api/datasource/analysis/catalog/{catalogId}":{"get":{"tags":["Data Source APIs - Analysis Resource"],"summary":"Download analysis schema file","description":"Download the analysis files for a given analysis id.\n\n**Example Request:**\n```\nGET pentaho/plugin/data-access/api/datasource/analysis/catalog/SampleSchema\n```\n","parameters":[{"name":"catalog","in":"path","description":"String Id of the analysis data to retrieve.","required":true,"schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully downloaded the analysis file","content":{"application/octet-stream":{"schema":{"type":"string","format":"binary","description":"Analysis file data XML"}}}},"401":{"description":"Unauthorized","content":{"text/plain":{"schema":{"type":"string","description":"Unauthorized access error"}}}},"500":{"description":"Unable to download analysis file","content":{"text/plain":{"schema":{"type":"string","description":"Internal server error"}}}}}}}}}
````

## Import analysis schema

> Import Analysis Schema.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> PUT pentaho/plugin/data-access/api/datasource/analysis/catalog/SampleSchema\
> \`\`\`\
> Request body should contain multipart/form-data with the analysis file to upload.\
> \
> \*\*Example cURL Command:\*\*\
> \`\`\`bash\
> curl -v -H "Content-Type: multipart/form-data" -X PUT \\\
> &#x20; -F uploadInput=@/Users/username/Downloads/SampleData2.mondrian.xml \\\
> &#x20; -F overwrite=true \\\
> &#x20; -F xmlaEnabledFlag=false \\\
> &#x20; -F parameters="Datasource=SampleData" \\\
> &#x20; -u admin:password \\\
> &#x20; <http://localhost:8080/yourdomain/plugin/data-access/api/datasource/analysis/catalog/SampleData2\\>
> \`\`\`\
> \
> \*\*Example Mondrian Schema XML for uploadInput:\*\*\
> \`\`\`xml\
> \<?xml version="1.0"?>\
> \<Schema name="SampleData2">\
> &#x20; \<!-- Shared dimensions -->\
> &#x20; \<Dimension name="Region">\
> &#x20;   \<Hierarchy hasAll="true" allMemberName="All Regions">\
> &#x20;     \<Table name="QUADRANT\_ACTUALS"/>\
> &#x20;     \<Level name="Region" column="REGION" uniqueMembers="true"/>\
> &#x20;   \</Hierarchy>\
> &#x20; \</Dimension>\
> &#x20; \<Dimension name="Department">\
> &#x20;   \<Hierarchy hasAll="true" allMemberName="All Departments">\
> &#x20;     \<Table name="QUADRANT\_ACTUALS"/>\
> &#x20;     \<Level name="Department" column="DEPARTMENT" uniqueMembers="true"/>\
> &#x20;   \</Hierarchy>\
> &#x20; \</Dimension>\
> &#x20; \<Dimension name="Positions">\
> &#x20;   \<Hierarchy hasAll="true" allMemberName="All Positions">\
> &#x20;     \<Table name="QUADRANT\_ACTUALS"/>\
> &#x20;     \<Level name="Positions" column="POSITIONTITLE" uniqueMembers="true"/>\
> &#x20;   \</Hierarchy>\
> &#x20; \</Dimension>\
> &#x20; \<Cube name="Quadrant Analysis">\
> &#x20;   \<Table name="QUADRANT\_ACTUALS"/>\
> &#x20;   \<DimensionUsage name="Region" source="Region"/>\
> &#x20;   \<DimensionUsage name="Department" source="Department"/>\
> &#x20;   \<DimensionUsage name="Positions" source="Positions"/>\
> &#x20;   \<Measure name="Actual" column="ACTUAL" aggregator="sum" formatString="#,###.00"/>\
> &#x20;   \<Measure name="Budget" column="BUDGET" aggregator="sum" formatString="#,###.00"/>\
> &#x20;   \<Measure name="Variance" column="VARIANCE" aggregator="sum" formatString="#,###.00"/>\
> &#x20;   \<!-- \<CalculatedMember name="Variance Percent" dimension="Measures"\
> &#x20;        formula="(\[Measures].\[Variance]/\[Measures].\[Budget])\*100" /> -->\
> &#x20; \</Cube>\
> \</Schema>\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Data Source APIs - Analysis Resource","description":"This service allows for listing, downloading, uploading, and removal of Analysis files or Mondrian schemas in the BA Platform."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/data-access/api/datasource/analysis/catalog/{catalogId}":{"put":{"tags":["Data Source APIs - Analysis Resource"],"summary":"Import analysis schema","description":"Import Analysis Schema.\n\n**Example Request:**\n```\nPUT pentaho/plugin/data-access/api/datasource/analysis/catalog/SampleSchema\n```\nRequest body should contain multipart/form-data with the analysis file to upload.\n\n**Example cURL Command:**\n```bash\ncurl -v -H \"Content-Type: multipart/form-data\" -X PUT \\\n  -F uploadInput=@/Users/username/Downloads/SampleData2.mondrian.xml \\\n  -F overwrite=true \\\n  -F xmlaEnabledFlag=false \\\n  -F parameters=\"Datasource=SampleData\" \\\n  -u admin:password \\\n  http://localhost:8080/yourdomain/plugin/data-access/api/datasource/analysis/catalog/SampleData2\n```\n\n**Example Mondrian Schema XML for uploadInput:**\n```xml\n<?xml version=\"1.0\"?>\n<Schema name=\"SampleData2\">\n  <!-- Shared dimensions -->\n  <Dimension name=\"Region\">\n    <Hierarchy hasAll=\"true\" allMemberName=\"All Regions\">\n      <Table name=\"QUADRANT_ACTUALS\"/>\n      <Level name=\"Region\" column=\"REGION\" uniqueMembers=\"true\"/>\n    </Hierarchy>\n  </Dimension>\n  <Dimension name=\"Department\">\n    <Hierarchy hasAll=\"true\" allMemberName=\"All Departments\">\n      <Table name=\"QUADRANT_ACTUALS\"/>\n      <Level name=\"Department\" column=\"DEPARTMENT\" uniqueMembers=\"true\"/>\n    </Hierarchy>\n  </Dimension>\n  <Dimension name=\"Positions\">\n    <Hierarchy hasAll=\"true\" allMemberName=\"All Positions\">\n      <Table name=\"QUADRANT_ACTUALS\"/>\n      <Level name=\"Positions\" column=\"POSITIONTITLE\" uniqueMembers=\"true\"/>\n    </Hierarchy>\n  </Dimension>\n  <Cube name=\"Quadrant Analysis\">\n    <Table name=\"QUADRANT_ACTUALS\"/>\n    <DimensionUsage name=\"Region\" source=\"Region\"/>\n    <DimensionUsage name=\"Department\" source=\"Department\"/>\n    <DimensionUsage name=\"Positions\" source=\"Positions\"/>\n    <Measure name=\"Actual\" column=\"ACTUAL\" aggregator=\"sum\" formatString=\"#,###.00\"/>\n    <Measure name=\"Budget\" column=\"BUDGET\" aggregator=\"sum\" formatString=\"#,###.00\"/>\n    <Measure name=\"Variance\" column=\"VARIANCE\" aggregator=\"sum\" formatString=\"#,###.00\"/>\n    <!-- <CalculatedMember name=\"Variance Percent\" dimension=\"Measures\"\n         formula=\"([Measures].[Variance]/[Measures].[Budget])*100\" /> -->\n  </Cube>\n</Schema>\n```\n","parameters":[{"name":"catalogName","in":"path","description":"The catalog name.","required":true,"schema":{"type":"string"}}],"requestBody":{"required":true,"description":"Multipart form data containing the analysis file to upload","content":{"multipart/form-data":{"schema":{"type":"object","properties":{"uploadInput":{"type":"string","format":"binary","description":"Analysis file to upload (Mondrian XML schema file)"},"schemaFileInfo":{"type":"string","description":"User selected name for the file","required":false},"origCatalogName":{"type":"string","description":"The original catalog name","required":false},"datasourceName":{"type":"string","description":"The datasource name","required":false},"overwrite":{"type":"string","description":"Whether to overwrite existing analysis data","enum":[true,false]},"xmlaEnabledFlag":{"type":"string","description":"Enable XMLA flag","enum":[true,false]},"parameters":{"type":"string","description":"Import parameters"}}}}}},"responses":{"200":{"description":"Successfully imported the analysis schema","content":{"text/plain":{"schema":{"type":"string","description":"Success message"}}}},"401":{"description":"Import failed because publish is prohibited","content":{"text/plain":{"schema":{"type":"string","description":"Unauthorized access error"}}}},"403":{"description":"Access Control Forbidden","content":{"text/plain":{"schema":{"type":"string","description":"Access Control Forbidden"}}}},"409":{"description":"Content already exists (use overwrite flag to force)","content":{"text/plain":{"schema":{"type":"string","description":"Error message"}}}},"412":{"description":"Analysis datasource import failed. Error code or message included in response entity","content":{"text/plain":{"schema":{"type":"string","description":"Analysis datasource import failed. Error code or message included in response entity"}}}},"500":{"description":"Unspecified general error has occurred","content":{"text/plain":{"schema":{"type":"string","description":"Internal server error"}}}}}}}}}
````

## Remove analysis data

> Remove the analysis data for a given analysis ID.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> DELETE pentaho/plugin/data-access/api/datasource/analysis/catalog/{catalog}\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Data Source APIs - Analysis Resource","description":"This service allows for listing, downloading, uploading, and removal of Analysis files or Mondrian schemas in the BA Platform."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/data-access/api/datasource/analysis/catalog/{catalogId}":{"delete":{"tags":["Data Source APIs - Analysis Resource"],"summary":"Remove analysis data","description":"Remove the analysis data for a given analysis ID.\n\n**Example Request:**\n```\nDELETE pentaho/plugin/data-access/api/datasource/analysis/catalog/{catalog}\n```\n","parameters":[{"name":"catalog","in":"path","description":"ID of the analysis data to remove.","required":true,"schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully removed the analysis data","content":{"text/plain":{"schema":{"type":"string","description":"Success message"}}}},"401":{"description":"User is not authorized to delete the analysisdatasource","content":{"text/plain":{"schema":{"type":"string","description":"Unauthorized access error"}}}},"500":{"description":"Unable to remove analysis data","content":{"text/plain":{"schema":{"type":"string","description":"Internal server error"}}}}}}}}}
````
