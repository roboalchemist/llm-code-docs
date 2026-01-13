# Source: https://docs.datadoghq.com/api/latest/scim/

# SCIM
Provision Datadog users and teams using SCIM APIs.
Note: SCIM provisioning for Datadog teams is only available for select organizations at this point. Request access by contacting Datadog support, or see the [SCIM page](https://docs.datadoghq.com/account_management/scim/) for more information.
## [List users](https://docs.datadoghq.com/api/latest/scim/#list-users)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/scim/#list-users-v2)


GET https://api.ap1.datadoghq.com/api/v2/scim/Usershttps://api.ap2.datadoghq.com/api/v2/scim/Usershttps://api.datadoghq.eu/api/v2/scim/Usershttps://api.ddog-gov.com/api/v2/scim/Usershttps://api.datadoghq.com/api/v2/scim/Usershttps://api.us3.datadoghq.com/api/v2/scim/Usershttps://api.us5.datadoghq.com/api/v2/scim/Users
### Overview
List users in the organization. Results are paginated by `startIndex` and `count` parameters. Results can be narrowed down by the `filter` parameter. This endpoint requires all of the following permissions:
* `user_access_invite`
* `user_access_manage`
  

### Arguments
#### Query Strings
Name
Type
Description
startIndex
integer
Specifies the start index to fetch the results (1-indexed).
count
integer
Specifies the number of users to be returned.
filter
string
Specifies the url encoded filter to use to narrow down the results. Filter should be of the form `userName eq <user name>`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/scim/#ListSCIMUsers-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/scim/#ListSCIMUsers-400-v2)
  * [429](https://docs.datadoghq.com/api/latest/scim/#ListSCIMUsers-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


List users response object.
Field
Type
Description
Resources
[object]
List of users matching the request criteria.
active
boolean
A Boolean value indicating the User's administrative status.
emails
[object]
Email addresses for the user.
primary
boolean
Boolean indicating if this email is the primary email address.
type
enum
The type of email. Allowed enum values: `work`
value
string
Email addresses for the user.
id
string
The identifier of the resource. Not required when creating a user.
meta
object
Metadata associated with a user.
created
date-time
The date and time the user was created.
lastModified
date-time
The date and time the user was last changed.
location
string
URL identifying the resource.
resourceType
string
Type of resource.
name
object
The components of user's real name
formatted
string
The full name, including all middle names, titles, and suffixes as appropriate, formatted for display.
schemas
[string]
User JSON Schemas.
title
string
The user's title.
userName
string
Unique identifier for the User.
itemsPerPage
int64
Number of users returned per page.
schemas
[string]
List response JSON Schemas.
startIndex
int64
Starting index of the users for this page (1-indexed).
totalResults
int64
Total number of users matching the request criteria.
```
{
  "Resources": [
    {
      "active": true,
      "emails": [
        {
          "primary": true,
          "type": "work",
          "value": "john.doe@datadoghq.com"
        }
      ],
      "id": "e43536e9-33fe-43f8-90b8-d3e39a7dd6ad",
      "meta": {
        "created": "2024-11-22T15:05:52.055138963Z",
        "lastModified": "2024-11-22T15:05:52.055139017Z",
        "location": "https://app.datadoghq.com/api/scim/v2/Users/e43536e9-33fe-43f8-90b8-d3e39a7dd6ad",
        "resourceType": "User"
      },
      "name": {
        "formatted": "John Doe"
      },
      "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User"
      ],
      "title": "Mr.",
      "userName": "john.doe@datadoghq.com"
    },
    {
      "active": true,
      "emails": [
        {
          "primary": true,
          "type": "work",
          "value": "jane.doe@datadoghq.com"
        }
      ],
      "id": "79ef0d28-f257-4829-97e6-d23d2a26cb1a",
      "meta": {
        "created": "2024-11-22T15:05:52.055139748Z",
        "lastModified": "2024-11-22T15:05:52.055139813Z",
        "location": "https://app.datadoghq.com/api/scim/v2/Users/79ef0d28-f257-4829-97e6-d23d2a26cb1a",
        "resourceType": "User"
      },
      "name": {
        "formatted": "Jane Doe"
      },
      "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User"
      ],
      "title": "Mrs.",
      "userName": "jane.doe@datadoghq.com"
    }
  ],
  "itemsPerPage": 2,
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:ListResponse"
  ],
  "startIndex": 1,
  "totalResults": 2
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/scim/?code-lang=curl)


#####  List users
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scim/Users" \
-H "Accept: application/json" \
-H "Authorization: Bearer ${DD_BEARER_TOKEN}"  

                
```

* * *
## [Create user](https://docs.datadoghq.com/api/latest/scim/#create-user)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/scim/#create-user-v2)


POST https://api.ap1.datadoghq.com/api/v2/scim/Usershttps://api.ap2.datadoghq.com/api/v2/scim/Usershttps://api.datadoghq.eu/api/v2/scim/Usershttps://api.ddog-gov.com/api/v2/scim/Usershttps://api.datadoghq.com/api/v2/scim/Usershttps://api.us3.datadoghq.com/api/v2/scim/Usershttps://api.us5.datadoghq.com/api/v2/scim/Users
### Overview
Create a new user. This endpoint requires all of the following permissions:
* `user_access_invite`
* `user_access_manage`
  

### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


Field
Type
Description
active
boolean
A Boolean value indicating the User's administrative status.
emails
[object]
Email addresses for the user.
primary
boolean
Boolean indicating if this email is the primary email address.
type
enum
The type of email. Allowed enum values: `work`
value
string
Email addresses for the user.
id
string
The identifier of the resource. Not required when creating a user.
meta
object
Metadata associated with a user.
created
date-time
The date and time the user was created.
lastModified
date-time
The date and time the user was last changed.
location
string
URL identifying the resource.
resourceType
string
Type of resource.
name
object
The components of user's real name
formatted
string
The full name, including all middle names, titles, and suffixes as appropriate, formatted for display.
schemas
[string]
User JSON Schemas.
title
string
The user's title.
userName
string
Unique identifier for the User.
```
{
  "active": false,
  "emails": [
    {
      "primary": false,
      "type": "string",
      "value": "string"
    }
  ],
  "id": "string",
  "meta": {
    "created": "2024-10-17T12:53:35.793Z",
    "lastModified": "2024-10-19T12:53:35.793Z",
    "location": "https://app.datadoghq.com/api/scim/v2/Users/13a95654-b76d-478d-8636-157a7e461d7c",
    "resourceType": "User"
  },
  "name": {
    "formatted": "string"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User"
  ],
  "title": "string",
  "userName": "string"
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/scim/#CreateSCIMUser-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/scim/#CreateSCIMUser-400-v2)
  * [429](https://docs.datadoghq.com/api/latest/scim/#CreateSCIMUser-429-v2)


Created
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


Definition of a user.
Field
Type
Description
active
boolean
A Boolean value indicating the User's administrative status.
emails
[object]
Email addresses for the user.
primary
boolean
Boolean indicating if this email is the primary email address.
type
enum
The type of email. Allowed enum values: `work`
value
string
Email addresses for the user.
id
string
The identifier of the resource. Not required when creating a user.
meta
object
Metadata associated with a user.
created
date-time
The date and time the user was created.
lastModified
date-time
The date and time the user was last changed.
location
string
URL identifying the resource.
resourceType
string
Type of resource.
name
object
The components of user's real name
formatted
string
The full name, including all middle names, titles, and suffixes as appropriate, formatted for display.
schemas
[string]
User JSON Schemas.
title
string
The user's title.
userName
string
Unique identifier for the User.
```
{
  "active": false,
  "emails": [
    {
      "primary": false,
      "type": "string",
      "value": "string"
    }
  ],
  "id": "string",
  "meta": {
    "created": "2024-10-17T12:53:35.793Z",
    "lastModified": "2024-10-19T12:53:35.793Z",
    "location": "https://app.datadoghq.com/api/scim/v2/Users/13a95654-b76d-478d-8636-157a7e461d7c",
    "resourceType": "User"
  },
  "name": {
    "formatted": "string"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User"
  ],
  "title": "string",
  "userName": "string"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/scim/?code-lang=curl)


#####  Create user
Copy
```
                  ## json-request-body
# 
  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scim/Users" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${DD_BEARER_TOKEN}" \
-d @- << EOF
{
  "active": true,
  "emails": [
    {
      "primary": true,
      "type": "work",
      "value": "john.doe@datadoghq.com"
    }
  ],
  "name": {
    "formatted": "John Doe"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User"
  ],
  "title": "Mr.",
  "userName": "john.doe@datadoghq.com"
}
EOF  

                
```

* * *
## [Get user](https://docs.datadoghq.com/api/latest/scim/#get-user)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/scim/#get-user-v2)


GET https://api.ap1.datadoghq.com/api/v2/scim/Users/{user_uuid}https://api.ap2.datadoghq.com/api/v2/scim/Users/{user_uuid}https://api.datadoghq.eu/api/v2/scim/Users/{user_uuid}https://api.ddog-gov.com/api/v2/scim/Users/{user_uuid}https://api.datadoghq.com/api/v2/scim/Users/{user_uuid}https://api.us3.datadoghq.com/api/v2/scim/Users/{user_uuid}https://api.us5.datadoghq.com/api/v2/scim/Users/{user_uuid}
### Overview
Get a single user using the `user_uuid`. This endpoint requires all of the following permissions:
* `user_access_invite`
* `user_access_manage`
  

### Arguments
#### Path Parameters
Name
Type
Description
user_uuid [_required_]
string
None
### Response
  * [200](https://docs.datadoghq.com/api/latest/scim/#GetSCIMUser-200-v2)
  * [404](https://docs.datadoghq.com/api/latest/scim/#GetSCIMUser-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/scim/#GetSCIMUser-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


Definition of a user.
Field
Type
Description
active
boolean
A Boolean value indicating the User's administrative status.
emails
[object]
Email addresses for the user.
primary
boolean
Boolean indicating if this email is the primary email address.
type
enum
The type of email. Allowed enum values: `work`
value
string
Email addresses for the user.
id
string
The identifier of the resource. Not required when creating a user.
meta
object
Metadata associated with a user.
created
date-time
The date and time the user was created.
lastModified
date-time
The date and time the user was last changed.
location
string
URL identifying the resource.
resourceType
string
Type of resource.
name
object
The components of user's real name
formatted
string
The full name, including all middle names, titles, and suffixes as appropriate, formatted for display.
schemas
[string]
User JSON Schemas.
title
string
The user's title.
userName
string
Unique identifier for the User.
```
{
  "active": false,
  "emails": [
    {
      "primary": false,
      "type": "string",
      "value": "string"
    }
  ],
  "id": "string",
  "meta": {
    "created": "2024-10-17T12:53:35.793Z",
    "lastModified": "2024-10-19T12:53:35.793Z",
    "location": "https://app.datadoghq.com/api/scim/v2/Users/13a95654-b76d-478d-8636-157a7e461d7c",
    "resourceType": "User"
  },
  "name": {
    "formatted": "string"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User"
  ],
  "title": "string",
  "userName": "string"
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/scim/?code-lang=curl)


#####  Get user
Copy
```
                  # Path parameters  
export user_uuid="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scim/Users/${user_uuid}" \
-H "Accept: application/json" \
-H "Authorization: Bearer ${DD_BEARER_TOKEN}"  

                
```

* * *
## [Update user](https://docs.datadoghq.com/api/latest/scim/#update-user)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/scim/#update-user-v2)


PUT https://api.ap1.datadoghq.com/api/v2/scim/Users/{user_uuid}https://api.ap2.datadoghq.com/api/v2/scim/Users/{user_uuid}https://api.datadoghq.eu/api/v2/scim/Users/{user_uuid}https://api.ddog-gov.com/api/v2/scim/Users/{user_uuid}https://api.datadoghq.com/api/v2/scim/Users/{user_uuid}https://api.us3.datadoghq.com/api/v2/scim/Users/{user_uuid}https://api.us5.datadoghq.com/api/v2/scim/Users/{user_uuid}
### Overview
Update the user with the given `user_uuid`. This endpoint requires all of the following permissions:
* `user_access_invite`
* `user_access_manage`
  

### Arguments
#### Path Parameters
Name
Type
Description
user_uuid [_required_]
string
None
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


Field
Type
Description
active
boolean
A Boolean value indicating the User's administrative status.
emails
[object]
Email addresses for the user.
primary
boolean
Boolean indicating if this email is the primary email address.
type
enum
The type of email. Allowed enum values: `work`
value
string
Email addresses for the user.
id
string
The identifier of the resource. Not required when creating a user.
meta
object
Metadata associated with a user.
created
date-time
The date and time the user was created.
lastModified
date-time
The date and time the user was last changed.
location
string
URL identifying the resource.
resourceType
string
Type of resource.
name
object
The components of user's real name
formatted
string
The full name, including all middle names, titles, and suffixes as appropriate, formatted for display.
schemas
[string]
User JSON Schemas.
title
string
The user's title.
userName
string
Unique identifier for the User.
```
{
  "active": false,
  "emails": [
    {
      "primary": false,
      "type": "string",
      "value": "string"
    }
  ],
  "id": "string",
  "meta": {
    "created": "2024-10-17T12:53:35.793Z",
    "lastModified": "2024-10-19T12:53:35.793Z",
    "location": "https://app.datadoghq.com/api/scim/v2/Users/13a95654-b76d-478d-8636-157a7e461d7c",
    "resourceType": "User"
  },
  "name": {
    "formatted": "string"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User"
  ],
  "title": "string",
  "userName": "string"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/scim/#UpdateSCIMUser-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/scim/#UpdateSCIMUser-400-v2)
  * [404](https://docs.datadoghq.com/api/latest/scim/#UpdateSCIMUser-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/scim/#UpdateSCIMUser-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


Definition of a user.
Field
Type
Description
active
boolean
A Boolean value indicating the User's administrative status.
emails
[object]
Email addresses for the user.
primary
boolean
Boolean indicating if this email is the primary email address.
type
enum
The type of email. Allowed enum values: `work`
value
string
Email addresses for the user.
id
string
The identifier of the resource. Not required when creating a user.
meta
object
Metadata associated with a user.
created
date-time
The date and time the user was created.
lastModified
date-time
The date and time the user was last changed.
location
string
URL identifying the resource.
resourceType
string
Type of resource.
name
object
The components of user's real name
formatted
string
The full name, including all middle names, titles, and suffixes as appropriate, formatted for display.
schemas
[string]
User JSON Schemas.
title
string
The user's title.
userName
string
Unique identifier for the User.
```
{
  "active": false,
  "emails": [
    {
      "primary": false,
      "type": "string",
      "value": "string"
    }
  ],
  "id": "string",
  "meta": {
    "created": "2024-10-17T12:53:35.793Z",
    "lastModified": "2024-10-19T12:53:35.793Z",
    "location": "https://app.datadoghq.com/api/scim/v2/Users/13a95654-b76d-478d-8636-157a7e461d7c",
    "resourceType": "User"
  },
  "name": {
    "formatted": "string"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User"
  ],
  "title": "string",
  "userName": "string"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/scim/?code-lang=curl)


#####  Update user
Copy
```
                  ## json-request-body
# 
  
# Path parameters  
export user_uuid="CHANGE_ME"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scim/Users/${user_uuid}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${DD_BEARER_TOKEN}" \
-d @- << EOF
{
  "active": true,
  "emails": [
    {
      "primary": true,
      "type": "work",
      "value": "john.doe@datadoghq.com"
    }
  ],
  "id": "e43536e9-33fe-43f8-90b8-d3e39a7dd6ad",
  "name": {
    "formatted": "John Doe"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User"
  ],
  "title": "Mr.",
  "userName": "john.doe@datadoghq.com"
}
EOF  

                
```

* * *
## [Patch user](https://docs.datadoghq.com/api/latest/scim/#patch-user)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/scim/#patch-user-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/scim/Users/{user_uuid}https://api.ap2.datadoghq.com/api/v2/scim/Users/{user_uuid}https://api.datadoghq.eu/api/v2/scim/Users/{user_uuid}https://api.ddog-gov.com/api/v2/scim/Users/{user_uuid}https://api.datadoghq.com/api/v2/scim/Users/{user_uuid}https://api.us3.datadoghq.com/api/v2/scim/Users/{user_uuid}https://api.us5.datadoghq.com/api/v2/scim/Users/{user_uuid}
### Overview
Patch the user with the given `user_uuid`. This endpoint requires all of the following permissions:
* `user_access_invite`
* `user_access_manage`
  

### Arguments
#### Path Parameters
Name
Type
Description
user_uuid [_required_]
string
None
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


Field
Type
Description
Operations
[object]
A list of update operations to be performed on a user.
op
enum
The operation to be performed. Allowed enum values: `add,replace`
path
string
An attribute path describing the target of the operation.
value
New value to use for the patch operation.
schemas
[string]
Input JSON Schemas
```
{
  "Operations": [
    {
      "op": "string",
      "path": "title",
      "value": "undefined"
    }
  ],
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ]
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/scim/#PatchSCIMUser-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/scim/#PatchSCIMUser-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/scim/#PatchSCIMUser-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/scim/#PatchSCIMUser-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/scim/#PatchSCIMUser-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


Definition of a user.
Field
Type
Description
active
boolean
A Boolean value indicating the User's administrative status.
emails
[object]
Email addresses for the user.
primary
boolean
Boolean indicating if this email is the primary email address.
type
enum
The type of email. Allowed enum values: `work`
value
string
Email addresses for the user.
id
string
The identifier of the resource. Not required when creating a user.
meta
object
Metadata associated with a user.
created
date-time
The date and time the user was created.
lastModified
date-time
The date and time the user was last changed.
location
string
URL identifying the resource.
resourceType
string
Type of resource.
name
object
The components of user's real name
formatted
string
The full name, including all middle names, titles, and suffixes as appropriate, formatted for display.
schemas
[string]
User JSON Schemas.
title
string
The user's title.
userName
string
Unique identifier for the User.
```
{
  "active": false,
  "emails": [
    {
      "primary": false,
      "type": "string",
      "value": "string"
    }
  ],
  "id": "string",
  "meta": {
    "created": "2024-10-17T12:53:35.793Z",
    "lastModified": "2024-10-19T12:53:35.793Z",
    "location": "https://app.datadoghq.com/api/scim/v2/Users/13a95654-b76d-478d-8636-157a7e461d7c",
    "resourceType": "User"
  },
  "name": {
    "formatted": "string"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User"
  ],
  "title": "string",
  "userName": "string"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/scim/?code-lang=curl)


#####  Patch user
Copy
```
                  ## json-request-body
# 
  
# Path parameters  
export user_uuid="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scim/Users/${user_uuid}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${DD_BEARER_TOKEN}" \
-d @- << EOF
{
  "Operations": [
    {
      "op": "replace",
      "path": "title",
      "value": "CEO"
    },
    {
      "op": "replace",
      "value": {
        "name": {
          "formatted": "John Doe"
        }
      }
    }
  ],
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ]
}
EOF  

                
```

* * *
## [Delete user](https://docs.datadoghq.com/api/latest/scim/#delete-user)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/scim/#delete-user-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/scim/Users/{user_uuid}https://api.ap2.datadoghq.com/api/v2/scim/Users/{user_uuid}https://api.datadoghq.eu/api/v2/scim/Users/{user_uuid}https://api.ddog-gov.com/api/v2/scim/Users/{user_uuid}https://api.datadoghq.com/api/v2/scim/Users/{user_uuid}https://api.us3.datadoghq.com/api/v2/scim/Users/{user_uuid}https://api.us5.datadoghq.com/api/v2/scim/Users/{user_uuid}
### Overview
Delete the group with the given `user_uuid`. This endpoint requires all of the following permissions:
* `user_access_invite`
* `user_access_manage`
  

### Arguments
#### Path Parameters
Name
Type
Description
user_uuid [_required_]
string
None
### Response
  * [204](https://docs.datadoghq.com/api/latest/scim/#DeleteSCIMUser-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/scim/#DeleteSCIMUser-400-v2)
  * [404](https://docs.datadoghq.com/api/latest/scim/#DeleteSCIMUser-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/scim/#DeleteSCIMUser-429-v2)


No Content
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/scim/?code-lang=curl)


#####  Delete user
Copy
```
                  # Path parameters  
export user_uuid="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scim/Users/${user_uuid}" \
-H "Authorization: Bearer ${DD_BEARER_TOKEN}"  

                
```

* * *
## [List groups](https://docs.datadoghq.com/api/latest/scim/#list-groups)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/scim/#list-groups-v2)


GET https://api.ap1.datadoghq.com/api/v2/scim/Groupshttps://api.ap2.datadoghq.com/api/v2/scim/Groupshttps://api.datadoghq.eu/api/v2/scim/Groupshttps://api.ddog-gov.com/api/v2/scim/Groupshttps://api.datadoghq.com/api/v2/scim/Groupshttps://api.us3.datadoghq.com/api/v2/scim/Groupshttps://api.us5.datadoghq.com/api/v2/scim/Groups
### Overview
List groups in the organization. Results are paginated by `startIndex` and `count` parameters. Results can be narrowed down by the `filter` parameter. This endpoint requires all of the following permissions:
* `user_access_invite`
* `user_access_manage`
  

### Arguments
#### Query Strings
Name
Type
Description
startIndex
integer
Specifies the start index to fetch the results (1-indexed).
count
integer
Specifies the number of groups to be returned.
filter
string
Specifies the url encoded filter to use to narrow down the results. Filters can be in the form of `displayName eq <group name>` or `externalId eq <external id of group>` or `id eq <group id> and members eq <user uuid>` or `members eq <user uuid> and id eq <group id>`.
### Response
  * [200](https://docs.datadoghq.com/api/latest/scim/#ListSCIMGroups-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/scim/#ListSCIMGroups-400-v2)
  * [429](https://docs.datadoghq.com/api/latest/scim/#ListSCIMGroups-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


List groups response object.
Field
Type
Description
Resources
[object]
List of groups matching the request criteria.
displayName
string
A human-readable name for the group.
externalId
string
An identifier for the resource as defined by the provisioning client.
id
string
The identifier of the resource. Not required when creating a group.
members
[object]
A list of members belonging to the team.
$ref
string
The URI corresponding to a resource that is a member of this group.
display
string
Full name of the user.
type
string
A label indicating the type of resource. Only supported value is "User".
value
string
The identifier of the member of this group.
meta
object
Metadata associated with a group.
created
date-time
The date and time the group was created.
lastModified
date-time
The date and time the group was last changed.
location
string
URL identifying the resource.
resourceType
string
Type of resource.
schemas
[string]
Group JSON Schemas.
itemsPerPage
int64
Number of groups returned per page.
schemas
[string]
List response JSON Schemas.
startIndex
int64
Starting index of the groups for this page (1-indexed).
totalResults
int64
Total number of groups matching the request criteria.
```
{
  "Resources": [
    {
      "displayName": "Group 1",
      "externalId": "group1",
      "id": "e43536e9-33fe-43f8-90b8-d3e39a7dd6ad",
      "members": [
        {
          "$ref": "https://app.datadoghq.com/api/scim/v2/Users/d34a5f93-5690-4d3f-a293-f2ad5c7a82a4",
          "display": "John Doe",
          "type": "User",
          "value": "d34a5f93-5690-4d3f-a293-f2ad5c7a82a4"
        },
        {
          "$ref": "https://app.datadoghq.com/api/scim/v2/Users/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
          "display": "Jane Doe",
          "type": "User",
          "value": "429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6"
        }
      ],
      "meta": {
        "created": "2024-11-22T15:05:52.055138963Z",
        "lastModified": "2024-11-22T15:05:52.055139017Z",
        "location": "https://app.datadoghq.com/api/scim/v2/Groups/e43536e9-33fe-43f8-90b8-d3e39a7dd6ad",
        "resourceType": "Group"
      },
      "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:Group"
      ]
    },
    {
      "displayName": "Group 2",
      "externalId": "group2",
      "id": "79ef0d28-f257-4829-97e6-d23d2a26cb1a",
      "members": [
        {
          "$ref": "https://app.datadoghq.com/api/scim/v2/Users/29da9fb7-8fca-4e87-bf58-86652253deae",
          "display": "Alice Smith",
          "type": "User",
          "value": "29da9fb7-8fca-4e87-bf58-86652253deae"
        },
        {
          "$ref": "https://app.datadoghq.com/api/scim/v2/Users/f85e3868-ad7b-47e3-a8a9-ff1eade2bbf9",
          "display": "Bob Smith",
          "type": "User",
          "value": "f85e3868-ad7b-47e3-a8a9-ff1eade2bbf9"
        }
      ],
      "meta": {
        "created": "2024-11-22T15:05:52.055139748Z",
        "lastModified": "2024-11-22T15:05:52.055139813Z",
        "location": "https://app.datadoghq.com/api/scim/v2/Groups/79ef0d28-f257-4829-97e6-d23d2a26cb1a",
        "resourceType": "Group"
      },
      "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:Group"
      ]
    }
  ],
  "itemsPerPage": 2,
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:ListResponse"
  ],
  "startIndex": 1,
  "totalResults": 2
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/scim/?code-lang=curl)


#####  List groups
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scim/Groups" \
-H "Accept: application/json" \
-H "Authorization: Bearer ${DD_BEARER_TOKEN}"  

                
```

* * *
## [Create group](https://docs.datadoghq.com/api/latest/scim/#create-group)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/scim/#create-group-v2)


POST https://api.ap1.datadoghq.com/api/v2/scim/Groupshttps://api.ap2.datadoghq.com/api/v2/scim/Groupshttps://api.datadoghq.eu/api/v2/scim/Groupshttps://api.ddog-gov.com/api/v2/scim/Groupshttps://api.datadoghq.com/api/v2/scim/Groupshttps://api.us3.datadoghq.com/api/v2/scim/Groupshttps://api.us5.datadoghq.com/api/v2/scim/Groups
### Overview
Create a new group. The group may contain members. This endpoint requires all of the following permissions:
* `user_access_invite`
* `user_access_manage`
  

### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


Field
Type
Description
displayName
string
A human-readable name for the group.
externalId
string
An identifier for the resource as defined by the provisioning client.
id
string
The identifier of the resource. Not required when creating a group.
members
[object]
Members of the group.
$ref
string
The URI corresponding to a SCIM resource that is a member of this group.
display
string
A human-readable name for the group member.
type
string
A label indicating the type of resource.
value
string
The identifier of the member of this group.
meta
object
Metadata associated with a group.
created
date-time
The date and time the group was created.
lastModified
date-time
The date and time the group was last changed.
location
string
URL identifying the resource.
resourceType
string
Type of resource.
schemas
[string]
Input JSON Schemas.
```
{
  "displayName": "string",
  "externalId": "string",
  "id": "string",
  "members": [
    {
      "$ref": "https://app.datadoghq.com/api/scim/v2/Users/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
      "display": "John Doe",
      "type": "User",
      "value": "429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6"
    }
  ],
  "meta": {
    "created": "2024-10-17T12:53:35.793Z",
    "lastModified": "2024-10-19T12:53:35.793Z",
    "location": "https://app.datadoghq.com/api/scim/v2/Groups/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
    "resourceType": "Group"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Group"
  ]
}
```

Copy
### Response
  * [201](https://docs.datadoghq.com/api/latest/scim/#CreateSCIMGroup-201-v2)
  * [400](https://docs.datadoghq.com/api/latest/scim/#CreateSCIMGroup-400-v2)
  * [429](https://docs.datadoghq.com/api/latest/scim/#CreateSCIMGroup-429-v2)


Created
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


Definition of a group.
Field
Type
Description
displayName
string
A human-readable name for the group.
externalId
string
An identifier for the resource as defined by the provisioning client.
id
string
The identifier of the resource. Not required when creating a group.
members
[object]
Members of the group.
$ref
string
The URI corresponding to a SCIM resource that is a member of this group.
display
string
A human-readable name for the group member.
type
string
A label indicating the type of resource.
value
string
The identifier of the member of this group.
meta
object
Metadata associated with a group.
created
date-time
The date and time the group was created.
lastModified
date-time
The date and time the group was last changed.
location
string
URL identifying the resource.
resourceType
string
Type of resource.
schemas
[string]
Input JSON Schemas.
```
{
  "displayName": "string",
  "externalId": "string",
  "id": "string",
  "members": [
    {
      "$ref": "https://app.datadoghq.com/api/scim/v2/Users/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
      "display": "John Doe",
      "type": "User",
      "value": "429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6"
    }
  ],
  "meta": {
    "created": "2024-10-17T12:53:35.793Z",
    "lastModified": "2024-10-19T12:53:35.793Z",
    "location": "https://app.datadoghq.com/api/scim/v2/Groups/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
    "resourceType": "Group"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Group"
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/scim/?code-lang=curl)


#####  Create group
Copy
```
                  ## json-request-body
# 
  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scim/Groups" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${DD_BEARER_TOKEN}" \
-d @- << EOF
{
  "displayName": "Group 1",
  "externalId": "group1",
  "members": [
    {
      "$ref": "https://app.datadoghq.com/api/scim/v2/Users/d34a5f93-5690-4d3f-a293-f2ad5c7a82a4",
      "display": "John Doe",
      "type": "User",
      "value": "d34a5f93-5690-4d3f-a293-f2ad5c7a82a4"
    },
    {
      "$ref": "https://app.datadoghq.com/api/scim/v2/Users/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
      "display": "Jane Doe",
      "type": "User",
      "value": "429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6"
    }
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Group"
  ]
}
EOF  

                
```

* * *
## [Get group](https://docs.datadoghq.com/api/latest/scim/#get-group)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/scim/#get-group-v2)


GET https://api.ap1.datadoghq.com/api/v2/scim/Groups/{group_id}https://api.ap2.datadoghq.com/api/v2/scim/Groups/{group_id}https://api.datadoghq.eu/api/v2/scim/Groups/{group_id}https://api.ddog-gov.com/api/v2/scim/Groups/{group_id}https://api.datadoghq.com/api/v2/scim/Groups/{group_id}https://api.us3.datadoghq.com/api/v2/scim/Groups/{group_id}https://api.us5.datadoghq.com/api/v2/scim/Groups/{group_id}
### Overview
Get a single group using the `group_id`. This endpoint requires all of the following permissions:
* `user_access_invite`
* `user_access_manage`
  

### Arguments
#### Path Parameters
Name
Type
Description
group_id [_required_]
string
None
### Response
  * [200](https://docs.datadoghq.com/api/latest/scim/#GetSCIMGroup-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/scim/#GetSCIMGroup-400-v2)
  * [404](https://docs.datadoghq.com/api/latest/scim/#GetSCIMGroup-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/scim/#GetSCIMGroup-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


Definition of a group.
Field
Type
Description
displayName
string
A human-readable name for the group.
externalId
string
An identifier for the resource as defined by the provisioning client.
id
string
The identifier of the resource. Not required when creating a group.
members
[object]
Members of the group.
$ref
string
The URI corresponding to a SCIM resource that is a member of this group.
display
string
A human-readable name for the group member.
type
string
A label indicating the type of resource.
value
string
The identifier of the member of this group.
meta
object
Metadata associated with a group.
created
date-time
The date and time the group was created.
lastModified
date-time
The date and time the group was last changed.
location
string
URL identifying the resource.
resourceType
string
Type of resource.
schemas
[string]
Input JSON Schemas.
```
{
  "displayName": "string",
  "externalId": "string",
  "id": "string",
  "members": [
    {
      "$ref": "https://app.datadoghq.com/api/scim/v2/Users/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
      "display": "John Doe",
      "type": "User",
      "value": "429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6"
    }
  ],
  "meta": {
    "created": "2024-10-17T12:53:35.793Z",
    "lastModified": "2024-10-19T12:53:35.793Z",
    "location": "https://app.datadoghq.com/api/scim/v2/Groups/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
    "resourceType": "Group"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Group"
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/scim/?code-lang=curl)


#####  Get group
Copy
```
                  # Path parameters  
export group_id="CHANGE_ME"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scim/Groups/${group_id}" \
-H "Accept: application/json" \
-H "Authorization: Bearer ${DD_BEARER_TOKEN}"  

                
```

* * *
## [Update group](https://docs.datadoghq.com/api/latest/scim/#update-group)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/scim/#update-group-v2)


PUT https://api.ap1.datadoghq.com/api/v2/scim/Groups/{group_id}https://api.ap2.datadoghq.com/api/v2/scim/Groups/{group_id}https://api.datadoghq.eu/api/v2/scim/Groups/{group_id}https://api.ddog-gov.com/api/v2/scim/Groups/{group_id}https://api.datadoghq.com/api/v2/scim/Groups/{group_id}https://api.us3.datadoghq.com/api/v2/scim/Groups/{group_id}https://api.us5.datadoghq.com/api/v2/scim/Groups/{group_id}
### Overview
Update the group with the given `group_id`. This endpoint requires all of the following permissions:
* `user_access_invite`
* `user_access_manage`
  

### Arguments
#### Path Parameters
Name
Type
Description
group_id [_required_]
string
None
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


Field
Type
Description
displayName
string
A human-readable name for the group.
externalId
string
An identifier for the resource as defined by the provisioning client.
id
string
The identifier of the resource. Not required when creating a group.
members
[object]
Members of the group.
$ref
string
The URI corresponding to a SCIM resource that is a member of this group.
display
string
A human-readable name for the group member.
type
string
A label indicating the type of resource.
value
string
The identifier of the member of this group.
meta
object
Metadata associated with a group.
created
date-time
The date and time the group was created.
lastModified
date-time
The date and time the group was last changed.
location
string
URL identifying the resource.
resourceType
string
Type of resource.
schemas
[string]
Input JSON Schemas.
```
{
  "displayName": "string",
  "externalId": "string",
  "id": "string",
  "members": [
    {
      "$ref": "https://app.datadoghq.com/api/scim/v2/Users/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
      "display": "John Doe",
      "type": "User",
      "value": "429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6"
    }
  ],
  "meta": {
    "created": "2024-10-17T12:53:35.793Z",
    "lastModified": "2024-10-19T12:53:35.793Z",
    "location": "https://app.datadoghq.com/api/scim/v2/Groups/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
    "resourceType": "Group"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Group"
  ]
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/scim/#UpdateSCIMGroup-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/scim/#UpdateSCIMGroup-400-v2)
  * [404](https://docs.datadoghq.com/api/latest/scim/#UpdateSCIMGroup-404-v2)
  * [409](https://docs.datadoghq.com/api/latest/scim/#UpdateSCIMGroup-409-v2)
  * [429](https://docs.datadoghq.com/api/latest/scim/#UpdateSCIMGroup-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


Definition of a group.
Field
Type
Description
displayName
string
A human-readable name for the group.
externalId
string
An identifier for the resource as defined by the provisioning client.
id
string
The identifier of the resource. Not required when creating a group.
members
[object]
Members of the group.
$ref
string
The URI corresponding to a SCIM resource that is a member of this group.
display
string
A human-readable name for the group member.
type
string
A label indicating the type of resource.
value
string
The identifier of the member of this group.
meta
object
Metadata associated with a group.
created
date-time
The date and time the group was created.
lastModified
date-time
The date and time the group was last changed.
location
string
URL identifying the resource.
resourceType
string
Type of resource.
schemas
[string]
Input JSON Schemas.
```
{
  "displayName": "string",
  "externalId": "string",
  "id": "string",
  "members": [
    {
      "$ref": "https://app.datadoghq.com/api/scim/v2/Users/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
      "display": "John Doe",
      "type": "User",
      "value": "429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6"
    }
  ],
  "meta": {
    "created": "2024-10-17T12:53:35.793Z",
    "lastModified": "2024-10-19T12:53:35.793Z",
    "location": "https://app.datadoghq.com/api/scim/v2/Groups/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
    "resourceType": "Group"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Group"
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Conflict
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/scim/?code-lang=curl)


#####  Update group
Copy
```
                  ## json-request-body
# 
  
# Path parameters  
export group_id="CHANGE_ME"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scim/Groups/${group_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${DD_BEARER_TOKEN}" \
-d @- << EOF
{
  "displayName": "Group 1",
  "externalId": "group1",
  "id": "e43536e9-33fe-43f8-90b8-d3e39a7dd6ad",
  "members": [
    {
      "$ref": "https://app.datadoghq.com/api/scim/v2/Users/d34a5f93-5690-4d3f-a293-f2ad5c7a82a4",
      "display": "John Doe",
      "type": "User",
      "value": "d34a5f93-5690-4d3f-a293-f2ad5c7a82a4"
    },
    {
      "$ref": "https://app.datadoghq.com/api/scim/v2/Users/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
      "display": "Jane Doe",
      "type": "User",
      "value": "429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6"
    }
  ],
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Group"
  ]
}
EOF  

                
```

* * *
## [Patch group](https://docs.datadoghq.com/api/latest/scim/#patch-group)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/scim/#patch-group-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/scim/Groups/{group_id}https://api.ap2.datadoghq.com/api/v2/scim/Groups/{group_id}https://api.datadoghq.eu/api/v2/scim/Groups/{group_id}https://api.ddog-gov.com/api/v2/scim/Groups/{group_id}https://api.datadoghq.com/api/v2/scim/Groups/{group_id}https://api.us3.datadoghq.com/api/v2/scim/Groups/{group_id}https://api.us5.datadoghq.com/api/v2/scim/Groups/{group_id}
### Overview
Patch the group with the given `group_id`. This endpoint requires all of the following permissions:
* `user_access_invite`
* `user_access_manage`
  

### Arguments
#### Path Parameters
Name
Type
Description
group_id [_required_]
string
None
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


Field
Type
Description
Operations
[object]
A list of update operations to be performed on a group.
op
enum
The operation to be performed. Allowed enum values: `add,replace,remove`
path
string
An attribute path describing the target of the operation.
value
JSON element containing the target values required to apply the patch operation.
schemas
[string]
Input JSON Schemas
```
{
  "Operations": [
    {
      "op": "string",
      "path": "members",
      "value": "{\n    \"displayName\": \"Real new group\",\n    \"id\": \"80df3a9b-24f5-4ebf-9ba0-714455453621\"\n}"
    }
  ],
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ]
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/scim/#PatchSCIMGroup-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/scim/#PatchSCIMGroup-400-v2)
  * [404](https://docs.datadoghq.com/api/latest/scim/#PatchSCIMGroup-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/scim/#PatchSCIMGroup-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


Definition of a group.
Field
Type
Description
displayName
string
A human-readable name for the group.
externalId
string
An identifier for the resource as defined by the provisioning client.
id
string
The identifier of the resource. Not required when creating a group.
members
[object]
Members of the group.
$ref
string
The URI corresponding to a SCIM resource that is a member of this group.
display
string
A human-readable name for the group member.
type
string
A label indicating the type of resource.
value
string
The identifier of the member of this group.
meta
object
Metadata associated with a group.
created
date-time
The date and time the group was created.
lastModified
date-time
The date and time the group was last changed.
location
string
URL identifying the resource.
resourceType
string
Type of resource.
schemas
[string]
Input JSON Schemas.
```
{
  "displayName": "string",
  "externalId": "string",
  "id": "string",
  "members": [
    {
      "$ref": "https://app.datadoghq.com/api/scim/v2/Users/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
      "display": "John Doe",
      "type": "User",
      "value": "429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6"
    }
  ],
  "meta": {
    "created": "2024-10-17T12:53:35.793Z",
    "lastModified": "2024-10-19T12:53:35.793Z",
    "location": "https://app.datadoghq.com/api/scim/v2/Groups/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
    "resourceType": "Group"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Group"
  ]
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/scim/?code-lang=curl)


#####  Patch group
Copy
```
                  ## json-request-body
# 
  
# Path parameters  
export group_id="CHANGE_ME"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scim/Groups/${group_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${DD_BEARER_TOKEN}" \
-d @- << EOF
{
  "Operations": [
    {
      "op": "replace",
      "path": "None",
      "value": {
        "displayName": "Real new group",
        "id": "e43536e9-33fe-43f8-90b8-d3e39a7dd6ad"
      }
    },
    {
      "op": "add",
      "path": "None",
      "value": {
        "members": [
          {
            "$ref": "https://app.datadoghq.com/api/scim/v2/Users/f85e3868-ad7b-47e3-a8a9-ff1eade2bbf9",
            "displayName": "Bob Smith",
            "value": "f85e3868-ad7b-47e3-a8a9-ff1eade2bbf9"
          }
        ]
      }
    },
    {
      "op": "remove",
      "path": "members[value eq \"fddf0cf2-9b60-11ef-ad4b-d6754a54a839\"]",
      "value": null
    }
  ],
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ]
}
EOF  

                
```

* * *
## [Delete group](https://docs.datadoghq.com/api/latest/scim/#delete-group)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/scim/#delete-group-v2)


DELETE https://api.ap1.datadoghq.com/api/v2/scim/Groups/{group_id}https://api.ap2.datadoghq.com/api/v2/scim/Groups/{group_id}https://api.datadoghq.eu/api/v2/scim/Groups/{group_id}https://api.ddog-gov.com/api/v2/scim/Groups/{group_id}https://api.datadoghq.com/api/v2/scim/Groups/{group_id}https://api.us3.datadoghq.com/api/v2/scim/Groups/{group_id}https://api.us5.datadoghq.com/api/v2/scim/Groups/{group_id}
### Overview
Delete the group with the given `group_id`. This endpoint requires all of the following permissions:
* `user_access_invite`
* `user_access_manage`
  

### Arguments
#### Path Parameters
Name
Type
Description
group_id [_required_]
string
None
### Response
  * [204](https://docs.datadoghq.com/api/latest/scim/#DeleteSCIMGroup-204-v2)
  * [400](https://docs.datadoghq.com/api/latest/scim/#DeleteSCIMGroup-400-v2)
  * [404](https://docs.datadoghq.com/api/latest/scim/#DeleteSCIMGroup-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/scim/#DeleteSCIMGroup-429-v2)


No Content
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/scim/)
  * [Example](https://docs.datadoghq.com/api/latest/scim/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/scim/?code-lang=curl)


#####  Delete group
Copy
```
                  # Path parameters  
export group_id="CHANGE_ME"  
# Curl command  
curl -X DELETE "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/scim/Groups/${group_id}" \
-H "Authorization: Bearer ${DD_BEARER_TOKEN}"  

                
```

* * *
![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=2c16c66e-1697-4d4d-854b-7e6a58c5d6c4&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=5af3065b-38be-4441-b8da-ced925f663db&pt=SCIM&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fscim%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=2c16c66e-1697-4d4d-854b-7e6a58c5d6c4&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=5af3065b-38be-4441-b8da-ced925f663db&pt=SCIM&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fscim%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=71882614-3d1f-4fd7-a824-5a2dc16e9886&bo=2&sid=72532930f0c011f0ad9469533a6ec7f2&vid=72534e40f0c011f08d852dd084c80453&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=SCIM&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fscim%2F&r=&lt=1546&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=322923)
