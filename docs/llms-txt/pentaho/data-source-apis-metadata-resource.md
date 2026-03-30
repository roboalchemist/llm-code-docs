# Source: https://docs.pentaho.com/rest-api/data-source-apis-metadata-resource.md

# Data Source APIs   Metadata Resource

This service allows for listing, download, and removal of Metadata data sources in the BA Platform.

## Get Metadata datasource IDs

> Get the Metadata datasource IDs.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/plugin/data-access/api/datasource/metadata/domain\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/plugin/data-access/api/datasource/metadata/domain>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Accept: application/json"\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Data Source APIs - Metadata Resource","description":"This service allows for listing, download, and removal of Metadata data sources in the BA Platform."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/data-access/api/datasource/metadata/domain":{"get":{"tags":["Data Source APIs - Metadata Resource"],"summary":"Get Metadata datasource IDs","description":"Get the Metadata datasource IDs.\n\n**Example Request:**\n```\nGET pentaho/plugin/data-access/api/datasource/metadata/domain\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/plugin/data-access/api/datasource/metadata/domain\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Accept: application/json\"\n```\n","responses":{"200":{"description":"Successfully retrieved the list of existing metadata IDs","content":{"application/xml":{"schema":{"type":"object","description":"List of metadata IDs in XML format"}},"application/json":{"schema":{"type":"object","description":"List of metadata IDs in JSON format"}}}}}}}}}
````

## Export a metadata datasource

> Export a metadata datasource.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/plugin/data-access/api/datasource/metadata/domain/SampleData2\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/plugin/data-access/api/datasource/metadata/domain/SampleData2>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Accept: application/octet-stream"\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Data Source APIs - Metadata Resource","description":"This service allows for listing, download, and removal of Metadata data sources in the BA Platform."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/data-access/api/datasource/metadata/domain/{domainId}":{"get":{"tags":["Data Source APIs - Metadata Resource"],"summary":"Export a metadata datasource","description":"Export a metadata datasource.\n\n**Example Request:**\n```\nGET pentaho/plugin/data-access/api/datasource/metadata/domain/SampleData2\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/plugin/data-access/api/datasource/metadata/domain/SampleData2\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Accept: application/octet-stream\"\n```\n","parameters":[{"name":"domainId","in":"path","required":true,"description":"The ID of the Metadata datasource to export","schema":{"type":"string"}}],"responses":{"200":{"description":"Metadata datasource export succeeded","content":{"application/octet-stream":{"schema":{"type":"string","format":"binary","description":"The metadata XMI file"}}}},"401":{"description":"User is not authorized to export the Metadata datasource","content":{"text/plain":{"schema":{"type":"string","description":"Unauthorized access error"}}}},"500":{"description":"Failure to export Metadata datasource","content":{"text/plain":{"schema":{"type":"string","description":"Internal server error"}}}}}}}}}
````

## Import a Metadata datasource

> Import a Metadata datasource.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> PUT pentaho/plugin/data-access/api/datasource/metadata/domain/SampleData\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X PUT \\\
> &#x20; "<http://localhost:8080/pentaho/plugin/data-access/api/datasource/metadata/domain/SampleData>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Content-Type: multipart/form-data" \\\
> &#x20; -F "metadataFile=@SampleData2.xmi;type=text/xml" \\\
> &#x20; -F "domainId=SampleData2" \\\
> &#x20; -F "overwrite=true"\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Data Source APIs - Metadata Resource","description":"This service allows for listing, download, and removal of Metadata data sources in the BA Platform."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/data-access/api/datasource/metadata/domain/{domainId}":{"put":{"tags":["Data Source APIs - Metadata Resource"],"summary":"Import a Metadata datasource","description":"Import a Metadata datasource.\n\n**Example Request:**\n```\nPUT pentaho/plugin/data-access/api/datasource/metadata/domain/SampleData\n```\n\n**cURL Example:**\n```bash\ncurl -X PUT \\\n  \"http://localhost:8080/pentaho/plugin/data-access/api/datasource/metadata/domain/SampleData\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Content-Type: multipart/form-data\" \\\n  -F \"metadataFile=@SampleData2.xmi;type=text/xml\" \\\n  -F \"domainId=SampleData2\" \\\n  -F \"overwrite=true\"\n```\n","parameters":[{"name":"domainId","in":"path","required":true,"description":"Unique identifier for the metadata datasource","schema":{"type":"string"}}],"requestBody":{"required":true,"description":"Multipart form data containing the metadata file to upload","content":{"multipart/form-data":{"schema":{"type":"object","properties":{"domainId":{"type":"string","description":"Domain identifier for the metadata datasource","required":false},"metadataFile":{"type":"string","format":"binary","description":"Input stream for the metadata.xmi file"},"metadataFileInfo":{"type":"string","description":"User selected name for the file (FormDataContentDisposition)","required":false},"localeFiles":{"type":"array","items":{"type":"string","format":"binary"},"description":"List of locale files","required":false},"localeFilesInfo":{"type":"array","items":{"type":"string"},"description":"List of FormDataContentDisposition for locale files","required":false},"overwrite":{"type":"boolean","description":"Flag for overwriting existing version of the file","default":false},"acl":{"type":"string","description":"Access control list data","required":false}}}}}},"responses":{"201":{"description":"Indicates successful import","content":{"text/plain":{"schema":{"type":"string","description":"Success message"}}}},"401":{"description":"Import failed because publish is prohibited","content":{"text/plain":{"schema":{"type":"string","description":"Unauthorized access error"}}}},"403":{"description":"Access Control Forbidden","content":{"text/plain":{"schema":{"type":"string","description":"Access Control Forbidden"}}}},"409":{"description":"Content already exists (use overwrite flag to force)","content":{"text/plain":{"schema":{"type":"string","description":"Error message"}}}},"412":{"description":"Metadata datasource import failed. Error code or message included in response entity","content":{"text/plain":{"schema":{"type":"string","description":"Metadata datasource import failed. Error code or message included in response entity"}}}},"500":{"description":"Unspecified general error has occurred","content":{"text/plain":{"schema":{"type":"string","description":"Internal server error"}}}}}}}}}
````

## Remove metadata datasource

> Remove the metadata for a given metadata ID.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> DELETE pentaho/plugin/data-access/api/datasource/metadata/domain/SampleData2\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X DELETE \\\
> &#x20; "<http://localhost:8080/pentaho/plugin/data-access/api/datasource/metadata/domain/SampleData2>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"Data Source APIs - Metadata Resource","description":"This service allows for listing, download, and removal of Metadata data sources in the BA Platform."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/data-access/api/datasource/metadata/domain/{domainId}":{"delete":{"tags":["Data Source APIs - Metadata Resource"],"summary":"Remove metadata datasource","description":"Remove the metadata for a given metadata ID.\n\n**Example Request:**\n```\nDELETE pentaho/plugin/data-access/api/datasource/metadata/domain/SampleData2\n```\n\n**cURL Example:**\n```bash\ncurl -X DELETE \\\n  \"http://localhost:8080/pentaho/plugin/data-access/api/datasource/metadata/domain/SampleData2\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n","parameters":[{"name":"domainId","in":"path","required":true,"description":"The ID of the Metadata datasource to remove","schema":{"type":"string"}}],"responses":{"200":{"description":"Metadata datasource removed."},"401":{"description":"User is not authorized to delete the Metadata datasource.","content":{"text/plain":{"schema":{"type":"string","description":"Unauthorized access error"}}}}}}}}}
````
