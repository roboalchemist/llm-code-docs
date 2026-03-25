# Source: https://developers.make.com/api-documentation/api-reference/custom-properties.md

# Custom properties

The following endpoints allow you to create and list custom property structures.

To use custom properties, you have to:

1. Create a custom properties structure.
2. Create custom properties structure items.
3. Fill the items with data.

Read more about custom properties in the [custom properties feature documentation](https://www.make.com/en/help/scenarios/custom-scenario-properties).

## List custom property structures

> Gets a list of custom properties structures in the organization.

```json
{"openapi":"3.0.0","info":{"title":"Web API v2 - Public ","version":"1.0.0"},"tags":[{"name":"Custom properties","description":"The following endpoints allow you to create and list custom property structures.\n\nTo use custom properties, you have to:\n\n1. [Create a custom properties structure](./post--custom-property-structures.md).\n2. [Create custom properties structure items](./structure-items/post--custom-property-structures--custompropertystructureid--custom-property-structure-items.md).\n3. [Fill the items with data](../scenarios/custom-properties-data/post--scenarios--scenarioid--custom-properties.md).\n\nRead more about custom properties in the [custom properties feature documentation](https://www.make.com/en/help/scenarios/custom-scenario-properties).\n"}],"servers":[{"url":"https://eu1.make.com/api/v2","description":"EU1 production zone"},{"url":"https://eu2.make.com/api/v2","description":"EU2 production zone"},{"url":"https://us1.make.com/api/v2","description":"US1 production zone"},{"url":"https://us2.make.com/api/v2","description":"US2 production zone"},{"url":"https://eu1.make.celonis.com/api/v2","description":"Celonis EU1 production zone"},{"url":"https://us1.make.celonis.com/api/v2","description":"Celonis US1 production zone"}],"security":[{"token":["custom-property-structures:read"]}],"components":{"securitySchemes":{"token":{"type":"apiKey","name":"Authorization","in":"header","description":"Authorize the API call with your API token in the `Authorization` header with the value: `Token your-api-token`.\n\nIf you don't have an API token yet, please refer to the [\"Authentication\" section](/api-documentation/authentication) to learn how to create one.\n"}}},"paths":{"/custom-property-structures":{"get":{"tags":["Custom properties"],"summary":"List custom property structures","description":"Gets a list of custom properties structures in the organization.","parameters":[{"name":"organizationId","in":"query","schema":{"type":"integer"},"required":true,"description":"The ID of the organization."}],"responses":{"200":{"description":"Successful response","content":{"application/json":{"schema":{"type":"object","properties":{"customPropertyStructures":{"type":"array","items":{"type":"object","properties":{"id":{"type":"integer"},"created":{"type":"string","format":"date-time"},"belongers":{"type":"array","items":{"type":"object","properties":{"belongerId":{"type":"integer"},"belongerType":{"type":"string"},"associatedTypes":{"type":"array","items":{"type":"string"}}}}}}}}}}}}}}}}}}
```

## Create a custom property structure

> Creates a custom properties structure. You can have only one custom properties structure for each combination of \`associatedType\`, \`belongerType\`and \`belongerId\` values.\
> \
> For example, you can create only one custom properties structure for scenarios in a specific organization.\
> \
> To create a structure for custom scenario properties, fill in the request body:\
> \
> \- \`associatedType\`: \`scenario\`\
> \- \`belongerType\`: \`organization\`\
> \
> Check out the example API call.\
> \
> To define the custom properties structure items, use the API call \[to create custom properties structure item]\(./structure-items/post--custom-property-structures--custompropertystructureid--custom-property-structure-items.md).<br>

```json
{"openapi":"3.0.0","info":{"title":"Web API v2 - Public ","version":"1.0.0"},"tags":[{"name":"Custom properties","description":"The following endpoints allow you to create and list custom property structures.\n\nTo use custom properties, you have to:\n\n1. [Create a custom properties structure](./post--custom-property-structures.md).\n2. [Create custom properties structure items](./structure-items/post--custom-property-structures--custompropertystructureid--custom-property-structure-items.md).\n3. [Fill the items with data](../scenarios/custom-properties-data/post--scenarios--scenarioid--custom-properties.md).\n\nRead more about custom properties in the [custom properties feature documentation](https://www.make.com/en/help/scenarios/custom-scenario-properties).\n"}],"servers":[{"url":"https://eu1.make.com/api/v2","description":"EU1 production zone"},{"url":"https://eu2.make.com/api/v2","description":"EU2 production zone"},{"url":"https://us1.make.com/api/v2","description":"US1 production zone"},{"url":"https://us2.make.com/api/v2","description":"US2 production zone"},{"url":"https://eu1.make.celonis.com/api/v2","description":"Celonis EU1 production zone"},{"url":"https://us1.make.celonis.com/api/v2","description":"Celonis US1 production zone"}],"security":[{"token":["custom-property-structures:write"]}],"components":{"securitySchemes":{"token":{"type":"apiKey","name":"Authorization","in":"header","description":"Authorize the API call with your API token in the `Authorization` header with the value: `Token your-api-token`.\n\nIf you don't have an API token yet, please refer to the [\"Authentication\" section](/api-documentation/authentication) to learn how to create one.\n"}}},"paths":{"/custom-property-structures":{"post":{"tags":["Custom properties"],"summary":"Create a custom property structure","description":"Creates a custom properties structure. You can have only one custom properties structure for each combination of `associatedType`, `belongerType`and `belongerId` values.\n\nFor example, you can create only one custom properties structure for scenarios in a specific organization.\n\nTo create a structure for custom scenario properties, fill in the request body:\n\n- `associatedType`: `scenario`\n- `belongerType`: `organization`\n\nCheck out the example API call.\n\nTo define the custom properties structure items, use the API call [to create custom properties structure item](./structure-items/post--custom-property-structures--custompropertystructureid--custom-property-structure-items.md).\n","requestBody":{"content":{"application/json":{"schema":{"type":"object","properties":{"associatedType":{"description":"The type of the entity which uses the custom properties structure. Fill in `scenario` to create custom scenario properties structure.","type":"string"},"belongerType":{"description":"The type of the entity that owns the custom properties structure. Fill in `organization` to create custom scenario properties structure.","type":"string"},"belongerId":{"description":"The ID of the entity that owns the custom properties structure.","type":"integer"}},"required":["associatedType","belongerType","belongerId"]}}}},"responses":{"200":{"description":"Successful response","content":{"application/json":{"schema":{"type":"object","properties":{"id":{"type":"integer"},"created":{"type":"string","format":"date-time"},"belongers":{"type":"array","items":{"type":"object","properties":{"belongerId":{"type":"integer"},"belongerType":{"type":"string"},"associatedTypes":{"type":"array","items":{"type":"string"}}}}}}}}}}}}}}}
```
