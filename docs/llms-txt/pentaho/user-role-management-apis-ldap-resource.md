# Source: https://docs.pentaho.com/rest-api/user-role-management-apis-ldap-resource.md

# User Role Management APIs   LDAP Resource

Resource allows reading and updating LDAP settings.

## Get LDAP attributes

> Retrieve the LDAP attributes of the repository.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> GET pentaho/api/ldap/config/getAttributeValues\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X GET \\\
> &#x20; "<http://localhost:8080/pentaho/api/ldap/config/getAttributeValues>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Accept: application/json"\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`json\
> {\
> &#x20; "attributes": \[\
> &#x20;   {\
> &#x20;     "key": "allAuthoritiesSearch.searchBase",\
> &#x20;     "value": "ou=roles"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "allUsernamesSearch.searchBase",\
> &#x20;     "value": "ou=users"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "userSearch.searchFilter",\
> &#x20;     "value": "(cn={0})"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "securityProvider",\
> &#x20;     "value": "jackrabbit"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "populator.groupRoleAttribute",\
> &#x20;     "value": "cn"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "allUsernamesSearch.usernameAttribute",\
> &#x20;     "value": "uid"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "populator.groupSearchBase",\
> &#x20;     "value": "ou=roles"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "contextSource.providerUrl",\
> &#x20;     "value": "ldap\://localhost:10389/ou=system"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "populator.searchSubtree",\
> &#x20;     "value": "false"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "allUsernamesSearch.searchFilter",\
> &#x20;     "value": "objectClass=Person"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "populator.convertToUpperCase",\
> &#x20;     "value": "false"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "populator.rolePrefix",\
> &#x20;     "value": ""\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "contextSource.password",\
> &#x20;     "value": "secret"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "userSearch.searchBase",\
> &#x20;     "value": "ou=users"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "allAuthoritiesSearch.roleAttribute",\
> &#x20;     "value": "cn"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "adminUser",\
> &#x20;     "value": "uid=admin,ou=users"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "contextSource.userDn",\
> &#x20;     "value": "uid=admin,ou=system"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "allAuthoritiesSearch.searchFilter",\
> &#x20;     "value": "(objectClass=organizationalRole)"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "populator.groupSearchFilter",\
> &#x20;     "value": "(roleOccupant={0})"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "adminRole",\
> &#x20;     "value": "cn=Administrator,ou=roles"\
> &#x20;   }\
> &#x20; ]\
> }\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> An AttributeSet object containing LDAP attributes of the repository.<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"User Role Management APIs - LDAP Resource","description":"Resource allows reading and updating LDAP settings."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/ldap/config/getAttributeValues":{"get":{"tags":["User Role Management APIs - LDAP Resource"],"summary":"Get LDAP attributes","produces":["application/json"],"description":"Retrieve the LDAP attributes of the repository.\n\n**Example Request:**\n```\nGET pentaho/api/ldap/config/getAttributeValues\n```\n\n**cURL Example:**\n```bash\ncurl -X GET \\\n  \"http://localhost:8080/pentaho/api/ldap/config/getAttributeValues\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Accept: application/json\"\n```\n\n**Example Response:**\n```json\n{\n  \"attributes\": [\n    {\n      \"key\": \"allAuthoritiesSearch.searchBase\",\n      \"value\": \"ou=roles\"\n    },\n    {\n      \"key\": \"allUsernamesSearch.searchBase\",\n      \"value\": \"ou=users\"\n    },\n    {\n      \"key\": \"userSearch.searchFilter\",\n      \"value\": \"(cn={0})\"\n    },\n    {\n      \"key\": \"securityProvider\",\n      \"value\": \"jackrabbit\"\n    },\n    {\n      \"key\": \"populator.groupRoleAttribute\",\n      \"value\": \"cn\"\n    },\n    {\n      \"key\": \"allUsernamesSearch.usernameAttribute\",\n      \"value\": \"uid\"\n    },\n    {\n      \"key\": \"populator.groupSearchBase\",\n      \"value\": \"ou=roles\"\n    },\n    {\n      \"key\": \"contextSource.providerUrl\",\n      \"value\": \"ldap://localhost:10389/ou=system\"\n    },\n    {\n      \"key\": \"populator.searchSubtree\",\n      \"value\": \"false\"\n    },\n    {\n      \"key\": \"allUsernamesSearch.searchFilter\",\n      \"value\": \"objectClass=Person\"\n    },\n    {\n      \"key\": \"populator.convertToUpperCase\",\n      \"value\": \"false\"\n    },\n    {\n      \"key\": \"populator.rolePrefix\",\n      \"value\": \"\"\n    },\n    {\n      \"key\": \"contextSource.password\",\n      \"value\": \"secret\"\n    },\n    {\n      \"key\": \"userSearch.searchBase\",\n      \"value\": \"ou=users\"\n    },\n    {\n      \"key\": \"allAuthoritiesSearch.roleAttribute\",\n      \"value\": \"cn\"\n    },\n    {\n      \"key\": \"adminUser\",\n      \"value\": \"uid=admin,ou=users\"\n    },\n    {\n      \"key\": \"contextSource.userDn\",\n      \"value\": \"uid=admin,ou=system\"\n    },\n    {\n      \"key\": \"allAuthoritiesSearch.searchFilter\",\n      \"value\": \"(objectClass=organizationalRole)\"\n    },\n    {\n      \"key\": \"populator.groupSearchFilter\",\n      \"value\": \"(roleOccupant={0})\"\n    },\n    {\n      \"key\": \"adminRole\",\n      \"value\": \"cn=Administrator,ou=roles\"\n    }\n  ]\n}\n```\n\n**Returns:**\nAn AttributeSet object containing LDAP attributes of the repository.\n","responses":{"200":{"description":"Successfully retrieved the LDAP attributes of the repository","content":{"application/json":{"schema":{"type":"object","properties":{"attributes":{"type":"array","items":{"type":"object","properties":{"key":{"type":"string","description":"LDAP attribute key"},"value":{"type":"string","description":"LDAP attribute value"}}}}}}}}},"500":{"description":"Server Error"}}}}}}
````

## Set LDAP attributes

> Writes LDAP attributes with new authentication parameters.\
> \
> \*\*Example Request:\*\*\
> \`\`\`\
> PUT pentaho/api/ldap/config/setAttributeValues\
> \`\`\`\
> \
> \*\*PUT data:\*\*\
> \`\`\`json\
> {\
> &#x20; "attributes": \[\
> &#x20;   {\
> &#x20;     "key": "allAuthoritiesSearch.searchBase",\
> &#x20;     "value": "ou=roles"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "allUsernamesSearch.searchBase",\
> &#x20;     "value": "ou=users"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "userSearch.searchFilter",\
> &#x20;     "value": "(cn={0})"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "securityProvider",\
> &#x20;     "value": "jackrabbit"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "populator.groupRoleAttribute",\
> &#x20;     "value": "cn"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "allUsernamesSearch.usernameAttribute",\
> &#x20;     "value": "uid"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "populator.groupSearchBase",\
> &#x20;     "value": "ou=roles"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "contextSource.providerUrl",\
> &#x20;     "value": "ldap\://localhost:10389/ou=system"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "populator.searchSubtree",\
> &#x20;     "value": "false"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "allUsernamesSearch.searchFilter",\
> &#x20;     "value": "objectClass=Person"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "populator.convertToUpperCase",\
> &#x20;     "value": "false"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "populator.rolePrefix",\
> &#x20;     "value": ""\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "contextSource.password",\
> &#x20;     "value": "secret"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "userSearch.searchBase",\
> &#x20;     "value": "ou=users"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "allAuthoritiesSearch.roleAttribute",\
> &#x20;     "value": "cn"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "adminUser",\
> &#x20;     "value": "uid=admin,ou=users"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "contextSource.userDn",\
> &#x20;     "value": "uid=admin,ou=system"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "allAuthoritiesSearch.searchFilter",\
> &#x20;     "value": "(objectClass=organizationalRole)"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "populator.groupSearchFilter",\
> &#x20;     "value": "(roleOccupant={0})"\
> &#x20;   },\
> &#x20;   {\
> &#x20;     "key": "adminRole",\
> &#x20;     "value": "cn=Administrator,ou=roles"\
> &#x20;   }\
> &#x20; ]\
> }\
> \`\`\`\
> \
> \*\*cURL Example:\*\*\
> \`\`\`bash\
> curl -X PUT \\\
> &#x20; "<http://localhost:8080/pentaho/api/ldap/config/setAttributeValues>" \\\
> &#x20; -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \\\
> &#x20; -H "Content-Type: application/json" \\\
> &#x20; -d '{\
> &#x20;   "attributes": \[\
> &#x20;     {\
> &#x20;       "key": "allAuthoritiesSearch.searchBase",\
> &#x20;       "value": "ou=roles"\
> &#x20;     },\
> &#x20;     {\
> &#x20;       "key": "allUsernamesSearch.searchBase",\
> &#x20;       "value": "ou=users"\
> &#x20;     }\
> &#x20;   ]\
> &#x20; }'\
> \`\`\`\
> \
> \*\*Example Response:\*\*\
> \`\`\`\
> This response does not contain data.\
> \`\`\`\
> \
> \*\*Returns:\*\*\
> A jax-rs Response object with the appropriate status code, header, and body.<br>

````json
{"openapi":"3.0.3","info":{"title":"Pentaho Data Integration and Analytics","version":"0.0.1"},"tags":[{"name":"User Role Management APIs - LDAP Resource","description":"Resource allows reading and updating LDAP settings."}],"security":[{"basicAuth":[]}],"components":{"securitySchemes":{"basicAuth":{"type":"http","scheme":"basic","description":"HTTP Basic Authentication"}}},"paths":{"/ldap/config/setAttributeValues":{"put":{"tags":["User Role Management APIs - LDAP Resource"],"summary":"Set LDAP attributes","consumes":["application/json"],"description":"Writes LDAP attributes with new authentication parameters.\n\n**Example Request:**\n```\nPUT pentaho/api/ldap/config/setAttributeValues\n```\n\n**PUT data:**\n```json\n{\n  \"attributes\": [\n    {\n      \"key\": \"allAuthoritiesSearch.searchBase\",\n      \"value\": \"ou=roles\"\n    },\n    {\n      \"key\": \"allUsernamesSearch.searchBase\",\n      \"value\": \"ou=users\"\n    },\n    {\n      \"key\": \"userSearch.searchFilter\",\n      \"value\": \"(cn={0})\"\n    },\n    {\n      \"key\": \"securityProvider\",\n      \"value\": \"jackrabbit\"\n    },\n    {\n      \"key\": \"populator.groupRoleAttribute\",\n      \"value\": \"cn\"\n    },\n    {\n      \"key\": \"allUsernamesSearch.usernameAttribute\",\n      \"value\": \"uid\"\n    },\n    {\n      \"key\": \"populator.groupSearchBase\",\n      \"value\": \"ou=roles\"\n    },\n    {\n      \"key\": \"contextSource.providerUrl\",\n      \"value\": \"ldap://localhost:10389/ou=system\"\n    },\n    {\n      \"key\": \"populator.searchSubtree\",\n      \"value\": \"false\"\n    },\n    {\n      \"key\": \"allUsernamesSearch.searchFilter\",\n      \"value\": \"objectClass=Person\"\n    },\n    {\n      \"key\": \"populator.convertToUpperCase\",\n      \"value\": \"false\"\n    },\n    {\n      \"key\": \"populator.rolePrefix\",\n      \"value\": \"\"\n    },\n    {\n      \"key\": \"contextSource.password\",\n      \"value\": \"secret\"\n    },\n    {\n      \"key\": \"userSearch.searchBase\",\n      \"value\": \"ou=users\"\n    },\n    {\n      \"key\": \"allAuthoritiesSearch.roleAttribute\",\n      \"value\": \"cn\"\n    },\n    {\n      \"key\": \"adminUser\",\n      \"value\": \"uid=admin,ou=users\"\n    },\n    {\n      \"key\": \"contextSource.userDn\",\n      \"value\": \"uid=admin,ou=system\"\n    },\n    {\n      \"key\": \"allAuthoritiesSearch.searchFilter\",\n      \"value\": \"(objectClass=organizationalRole)\"\n    },\n    {\n      \"key\": \"populator.groupSearchFilter\",\n      \"value\": \"(roleOccupant={0})\"\n    },\n    {\n      \"key\": \"adminRole\",\n      \"value\": \"cn=Administrator,ou=roles\"\n    }\n  ]\n}\n```\n\n**cURL Example:**\n```bash\ncurl -X PUT \\\n  \"http://localhost:8080/pentaho/api/ldap/config/setAttributeValues\" \\\n  -H \"Authorization: Basic YWRtaW46cGFzc3dvcmQ=\" \\\n  -H \"Content-Type: application/json\" \\\n  -d '{\n    \"attributes\": [\n      {\n        \"key\": \"allAuthoritiesSearch.searchBase\",\n        \"value\": \"ou=roles\"\n      },\n      {\n        \"key\": \"allUsernamesSearch.searchBase\",\n        \"value\": \"ou=users\"\n      }\n    ]\n  }'\n```\n\n**Example Response:**\n```\nThis response does not contain data.\n```\n\n**Returns:**\nA jax-rs Response object with the appropriate status code, header, and body.\n","requestBody":{"required":true,"description":"An AttributeSet representing the new authentication parameters","content":{"application/json":{"schema":{"type":"object","properties":{"attributes":{"type":"array","items":{"type":"object","properties":{"key":{"type":"string","description":"LDAP attribute key"},"value":{"type":"string","description":"LDAP attribute value"}}}}}}}}},"responses":{"200":{"description":"Successfully updated the LDAP attributes of the repository"},"500":{"description":"Server Error"}}}}}}
````
