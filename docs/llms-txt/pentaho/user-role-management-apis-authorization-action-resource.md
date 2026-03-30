# Source: https://docs.pentaho.com/rest-api/user-role-management-apis-authorization-action-resource.md

# User Role Management APIs   Authorization Action Resource

Resource deals with the Authorization Action in the BA Platform. This service validates if a current user is authorized to perform a specific action.

## Validate user authorization

> Validates if a current user is authorized to perform a specific action.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/authorization/action/isauthorized\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/authorization/action/isauthorized?authAction=org.pentaho.repository.read>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ="\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`\
> false\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> A boolean response based on the current user being authorized to perform a specific action within the system.<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"User Role Management APIs - Authorization Action Resource","description":"Resource deals with the Authorization Action in the BA Platform. This service validates if a current user is authorized to perform a specific action."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/authorization/action/isauthorized":{"get":{"tags":["User Role Management APIs - Authorization Action Resource"],"summary":"Validate user authorization","produces":["text/plain"],"description":"Validates if a current user is authorized to perform a specific action.\n\n**Example Request:**\n```\nGET pentaho/api/authorization/action/isauthorized\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/authorization/action/isauthorized?authAction=org.pentaho.repository.read\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\"\n```\n\n**Example Response:**\n```\nfalse\n```\n\n**Returns:**\nA boolean response based on the current user being authorized to perform a specific action within the system.\n","parameters":[{"name":"authAction","in":"query","required":true,"description":"Authorization Action to be validated for the current user","schema":{"type":"string"}}],"responses":{"200":{"description":"Returns a boolean response","content":{"text/plain":{"schema":{"type":"string","description":"Boolean value indicating authorization status"}}}}}}}}}
````
