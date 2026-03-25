# Source: https://docs.pentaho.com/rest-api/user-role-management-apis-system-users-resource.md

# User Role Management APIs   System Users Resource

This service allows for listing system users in the BA Platform.

## Get list of users

> Returns the list of users in the platform, this list is in an xml format as shown in the example response.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/users\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/users>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Accept: application/xml"\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`xml\
> \<?xml version="1.0" encoding="UTF-8"?>\
> &#x20; \<users>\
> &#x20;   \<user>pat\</user>\
> &#x20;   \<user>admin\</user>\
> &#x20;   \<user>suzy\</user>\
> &#x20;   \<user>tiffany\</user>\
> &#x20;   \<user>enco\*de:te^s\_t$\</user>\
> &#x20; \</users>\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> Response object containing an xml list of users in the platform.<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"User Role Management APIs - System Users Resource","description":"This service allows for listing system users in the BA Platform."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}},"schemas":{"UserList":{"type":"object","description":"List of users in the platform","properties":{"users":{"type":"array","description":"Array of usernames","items":{"type":"string"}}},"xml":{"name":"userList"}}}},"paths":{"/users":{"get":{"tags":["User Role Management APIs - System Users Resource"],"summary":"Get list of users","produces":["application/xml"],"description":"Returns the list of users in the platform, this list is in an xml format as shown in the example response.\n\n**Example Request:**\n```\nGET pentaho/api/users\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/users\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Accept: application/xml\"\n```\n\n**Example Response:**\n```xml\n<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n  <users>\n    <user>pat</user>\n    <user>admin</user>\n    <user>suzy</user>\n    <user>tiffany</user>\n    <user>enco*de:te^s_t$</user>\n  </users>\n```\n\n**Returns:**\nResponse object containing an xml list of users in the platform.\n","responses":{"200":{"description":"Response object containing an xml list of the users in the platform","content":{"application/xml":{"schema":{"$ref":"#/components/schemas/UserList"}}}},"403":{"description":"Response due to the requesting user not having sufficient privileges"},"500":{"description":"Internal server error occurs when the server cannot retrieve the list of users"}}}}}}
````
