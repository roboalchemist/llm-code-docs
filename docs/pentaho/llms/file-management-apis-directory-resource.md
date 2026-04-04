# Source: https://docs.pentaho.com/rest-api/file-management-apis-directory-resource.md

# File Management APIs   Directory Resource

This service provides operations for managing directories in the repository.

## Create new folder

> Creates a new folder with the specified name. \
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> PUT pentaho/api/repo/dirs/home:admin:newfolder\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X PUT \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/dirs/home:admin:newfolder>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - Directory Resource","description":"This service provides operations for managing directories in the repository."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/dirs/{pathId}":{"put":{"tags":["File Management APIs - Directory Resource"],"summary":"Create new folder","description":"Creates a new folder with the specified name. \n\n**Example Request:**\n```\nPUT pentaho/api/repo/dirs/home:admin:newfolder\n```\n\n**cURL Example:**\n```bash\ncurl -X PUT \\\n  \"http://localhost:8080/pentaho/api/repo/dirs/home:admin:newfolder\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n","parameters":[{"name":"pathId","in":"path","required":true,"description":"The path from the root folder to the root node of the tree to return usingcolon characters in place of / or \\ characters. To clarify /path/to/file, the encoded pathId would be :path:to:file.","schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully created folder."},"403":{"description":"Forbidden. Cannot create root level folder or contains illegal characters.","content":{"text/plain":{"schema":{"type":"string","enum":["couldNotCreateRootLevelFolder","containsIllegalCharacters"],"description":"Error message"}}}},"409":{"description":"Path already exists.","content":{"text/plain":{"schema":{"type":"string","description":"Error message indicating duplicate folder"}}}},"500":{"description":"Server Error."}}}}}}
````

## Check if folder is visible

> Determines whether a current user has permission to see the folder or not.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/dirs/home:admin:folder/isVisible\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/dirs/home:admin:folder/isVisible>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - Directory Resource","description":"This service provides operations for managing directories in the repository."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/dirs/{pathId}/isVisible":{"get":{"tags":["File Management APIs - Directory Resource"],"summary":"Check if folder is visible","description":"Determines whether a current user has permission to see the folder or not.\n\n**Example Request:**\n```\nGET pentaho/api/repo/dirs/home:admin:folder/isVisible\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/dirs/home:admin:folder/isVisible\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n","parameters":[{"name":"pathId","in":"path","required":true,"description":"The path from the root folder to the root node of the tree to return using colon characters in place of / or \\ characters. To clarify /path/to/file, the encoded pathId would be :path:to:file.","schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully returns a boolean value, either true or false","content":{"text/plain":{"schema":{"type":"string","enum":["true","false"],"description":"String \"true\" if the folder is visible to the current user, or \"false\" otherwise."}}}}}}}}}
````

## Get default save location

> Gets the default save location for the specified path.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/repo/dirs/home:admin:folder/defaultLocation\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/repo/dirs/home:admin:folder/defaultLocation>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - Directory Resource","description":"This service provides operations for managing directories in the repository."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/repo/dirs/{pathId}/defaultLocation":{"get":{"tags":["File Management APIs - Directory Resource"],"summary":"Get default save location","description":"Gets the default save location for the specified path.\n\n**Example Request:**\n```\nGET pentaho/api/repo/dirs/home:admin:folder/defaultLocation\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/repo/dirs/home:admin:folder/defaultLocation\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n","parameters":[{"name":"pathId","in":"path","required":true,"description":"The path from the root folder to the root node of the tree to return using colon characters in place of / or \\ characters. To clarify /path/to/file, the encoded pathId would be :path:to:file.","schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully returns a default open/save location","content":{"text/plain":{"schema":{"type":"string","description":"Path for a default save location"}}}}}}}}}
````
