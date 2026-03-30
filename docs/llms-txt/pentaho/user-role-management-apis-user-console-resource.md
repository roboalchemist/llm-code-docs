# Source: https://docs.pentaho.com/rest-api/user-role-management-apis-user-console-resource.md

# User Role Management APIs   User Console Resource

The UserConsoleResource service provides both shared and user-specific state or settings related with the use of the Pentaho User Console.

## Check if user is administrator

> Returns whether the current user is an administrator.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/mantle/isAdministrator\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/mantle/isAdministrator>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`\
> true\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> String true if the user is an administrator, or false otherwise.<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"User Role Management APIs - User Console Resource","description":"The UserConsoleResource service provides both shared and user-specific state or settings related with the use of the Pentaho User Console."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/mantle/isAdministrator":{"get":{"tags":["User Role Management APIs - User Console Resource"],"summary":"Check if user is administrator","produces":["text/plain"],"description":"Returns whether the current user is an administrator.\n\n**Example Request:**\n```\nGET pentaho/api/mantle/isAdministrator\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/mantle/isAdministrator\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n\n**Example Response:**\n```\ntrue\n```\n\n**Returns:**\nString true if the user is an administrator, or false otherwise.\n","responses":{"200":{"description":"Returns the boolean response","content":{"text/plain":{"schema":{"type":"string","description":"Boolean value indicating administrator status"}}}}}}}}}
````

## Check if user is authenticated

> Returns whether the user is an authenticated user or not.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/mantle/isAuthenticated\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/mantle/isAuthenticated>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`\
> true\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> String true if the user is authenticated, or false otherwise.<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"User Role Management APIs - User Console Resource","description":"The UserConsoleResource service provides both shared and user-specific state or settings related with the use of the Pentaho User Console."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/mantle/isAuthenticated":{"get":{"tags":["User Role Management APIs - User Console Resource"],"summary":"Check if user is authenticated","produces":["text/plain"],"description":"Returns whether the user is an authenticated user or not.\n\n**Example Request:**\n```\nGET pentaho/api/mantle/isAuthenticated\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/mantle/isAuthenticated\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n\n**Example Response:**\n```\ntrue\n```\n\n**Returns:**\nString true if the user is authenticated, or false otherwise.\n","responses":{"200":{"description":"Returns the boolean response","content":{"text/plain":{"schema":{"type":"string","description":"Boolean value indicating authentication status"}}}},"401":{"description":"User is not authenticated"}}}}}}
````
