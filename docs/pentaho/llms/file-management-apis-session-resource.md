# Source: https://docs.pentaho.com/rest-api/file-management-apis-session-resource.md

# File Management APIs   Session Resource

This service provides session-related operations for workspace management.

## Get user workspace directory

> Returns the current user's workspace folder path.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/session/userWorkspaceDir\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/session/userWorkspaceDir>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - Session Resource","description":"This service provides session-related operations for workspace management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/session/userWorkspaceDir":{"get":{"tags":["File Management APIs - Session Resource"],"summary":"Get user workspace directory","produces":["text/plain"],"description":"Returns the current user's workspace folder path.\n\n**Example Request:**\n```\nGET pentaho/api/session/userWorkspaceDir\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/session/userWorkspaceDir\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n","responses":{"200":{"description":"Returns the requested file path","content":{"text/plain":{"schema":{"type":"string","description":"String object containing the workspace folder path"}}}}}}}}}
````

## Get workspace directory for specific user

> Returns the workspace folder path for the selected user.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/session/workspaceDirForUser/admin\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/session/workspaceDirForUser/admin>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"File Management APIs - Session Resource","description":"This service provides session-related operations for workspace management."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/session/workspaceDirForUser/{user}":{"get":{"tags":["File Management APIs - Session Resource"],"summary":"Get workspace directory for specific user","produces":["text/plain"],"description":"Returns the workspace folder path for the selected user.\n\n**Example Request:**\n```\nGET pentaho/api/session/workspaceDirForUser/admin\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/session/workspaceDirForUser/admin\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n","parameters":[{"name":"user","in":"path","required":true,"description":"String of the user name","schema":{"type":"string"}}],"responses":{"200":{"description":"Returns the workspace file path for the specified user","content":{"text/plain":{"schema":{"type":"string","description":"String object containing the workspace folder path"}}}},"500":{"description":"File path failed to be retrieved. This could be caused by an invalid user request"}}}}}}
````
