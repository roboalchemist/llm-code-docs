# Source: https://docs.pentaho.com/rest-api/file-management-apis-repository-resource.md

# File Management APIs   Repository Resource

This service provides access to repository resources and contexts.

## Get repository resource

> Gets a resource identified by the compound key contextId and resourceId. \
> This request may include additional parameters used to render the resource.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repos/admin-plugin/resources/authenticationProviderModule/authenticationProviderAdmin.html\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repos/admin-plugin/resources/authenticationProviderModule/authenticationProviderAdmin.html>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - Repository Resource","description":"This service provides access to repository resources and contexts."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repos/{contextId}/{resourceId}":{"get":{"tags":["File Management APIs - Repository Resource"],"summary":"Get repository resource","produces":["*/*"],"description":"Gets a resource identified by the compound key contextId and resourceId. \nThis request may include additional parameters used to render the resource.\n\n**Example Request:**\n```\nGET pentaho/api/repos/admin-plugin/resources/authenticationProviderModule/authenticationProviderAdmin.html\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repos/admin-plugin/resources/authenticationProviderModule/authenticationProviderAdmin.html\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n","parameters":[{"name":"contextId","in":"path","required":true,"description":"Identifies the context in which the resource should be retrieved. This value may be a repository file ID, repository file extension or plugin ID.","schema":{"type":"string"}},{"name":"resourceId","in":"path","required":true,"description":"Identifies a resource to be retrieved. This value may be a static file residing in a publicly visible plugin folder, repository file ID or content generator ID.","schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully get the resource.","content":{"*/*":{"schema":{"type":"string"}}}},"404":{"description":"Failed to find the resource."}}}}}}
````

## Get repository resource with form data

> Gets a resource identified by the compound key contextId and resourceId. \
> This request may include additional parameters used to render the resource.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> POST pentaho/api/repos/xanalyzer/service/ajax/lookupXmiId\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X POST \\\
> &#x20; "<http://localhost:8080/pentaho/api/repos/xanalyzer/service/ajax/lookupXmiId>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Content-Type: application/x-www-form-urlencoded" \\\
> &#x20; -d "catalog=t\&cube=t\&time=1389817320072"\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - Repository Resource","description":"This service provides access to repository resources and contexts."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repos/{contextId}/{resourceId}":{"post":{"tags":["File Management APIs - Repository Resource"],"summary":"Get repository resource with form data","consumes":["application/x-www-form-urlencoded"],"produces":["*/*"],"description":"Gets a resource identified by the compound key contextId and resourceId. \nThis request may include additional parameters used to render the resource.\n\n**Example Request:**\n```\nPOST pentaho/api/repos/xanalyzer/service/ajax/lookupXmiId\n```\n\n**cURL Example:**\n```bash\ncurl -X POST \\\n  \"http://localhost:8080/pentaho/api/repos/xanalyzer/service/ajax/lookupXmiId\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Content-Type: application/x-www-form-urlencoded\" \\\n  -d \"catalog=t&cube=t&time=1389817320072\"\n```\n","parameters":[{"name":"contextId","in":"path","required":true,"description":"Identifies the context in which the resource should be retrieved. This value may be a repository file ID, repository file extension or plugin ID","schema":{"type":"string"}},{"name":"resourceId","in":"path","required":true,"description":"Identifies a resource to be retrieved. This value may be a static file residing in a publicly visible plugin folder, repository file ID or content generator ID","schema":{"type":"string"}}],"requestBody":{"required":false,"description":"Any arguments needed to render the resource","content":{"application/x-www-form-urlencoded":{"schema":{"type":"object","additionalProperties":{"type":"string"}}}}},"responses":{"200":{"description":"Successfully get the resource.","content":{"*/*":{"schema":{"type":"string"}}}},"404":{"description":"Failed to find the resource."}}}}}}
````

## Get default URI for file execution

> Takes a pathId to a file and generates a URI that represents the URL to call to generate content from that file.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repos/public:steel%20wheels:Invoice%20(report).prpt/default\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repos/public:steel%20wheels:Invoice%20(report).prpt/default>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - Repository Resource","description":"This service provides access to repository resources and contexts."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repos/{pathId}/default":{"get":{"tags":["File Management APIs - Repository Resource"],"summary":"Get default URI for file execution","produces":["*/*"],"description":"Takes a pathId to a file and generates a URI that represents the URL to call to generate content from that file.\n\n**Example Request:**\n```\nGET pentaho/api/repos/public:steel%20wheels:Invoice%20(report).prpt/default\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repos/public:steel%20wheels:Invoice%20(report).prpt/default\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n","parameters":[{"name":"pathId","in":"path","required":true,"description":"The path ID to a file","schema":{"type":"string"}}],"responses":{"303":{"description":"Successfully get the resource.","headers":{"Location":{"description":"URI that represents a forwarding URL to execute to generate content from the file","schema":{"type":"string"}}}},"404":{"description":"Failed to find the resource."}}}}}}
````
