# Source: https://docs.datadoghq.com/api/latest/service-dependencies/

# Service Dependencies
APM Service Map API. For more information, visit the [Service Map page](https://docs.datadoghq.com/tracing/visualization/services_map/).
## [Get all APM service dependencies](https://docs.datadoghq.com/api/latest/service-dependencies/#get-all-apm-service-dependencies)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/service-dependencies/#get-all-apm-service-dependencies-v1)


**Note: This endpoint is in public beta. If you have any feedback, contact[Datadog support](https://docs.datadoghq.com/help/).**
GET https://api.ap1.datadoghq.com/api/v1/service_dependencieshttps://api.ap2.datadoghq.com/api/v1/service_dependencieshttps://api.datadoghq.eu/api/v1/service_dependencieshttps://api.ddog-gov.com/api/v1/service_dependencieshttps://api.datadoghq.com/api/v1/service_dependencieshttps://api.us3.datadoghq.com/api/v1/service_dependencieshttps://api.us5.datadoghq.com/api/v1/service_dependencies
### Overview
Get a list of services from APM and their dependencies. The services retrieved are filtered by environment and a primary tag, if one is defined.
### Arguments
#### Query Strings
Name
Type
Description
env [_required_]
string
Specify what APM environment to query service dependencies by.
primary_tag
string
Specify what primary tag to query service dependencies by.
start
integer
Specify the start of the timeframe in epoch seconds to query for. (defaults to 1 hour before end parameter)
end
integer
Specify the end of the timeframe in epoch seconds to query for. (defaults to current time)
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-dependencies/#ListServiceDependencies-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/service-dependencies/#ListServiceDependencies-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/service-dependencies/#ListServiceDependencies-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/service-dependencies/#ListServiceDependencies-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-dependencies/)
  * [Example](https://docs.datadoghq.com/api/latest/service-dependencies/)


An object containing a list of APM services and their dependencies.
Field
Type
Description
<any-key>
object
An object containing an APM service's dependencies.
calls [_required_]
[string]
A list of dependencies.
```
{
  "servica_a": {
    "calls": [
      "service_b",
      "service_c"
    ]
  },
  "service_b": {
    "calls": [
      "service_o"
    ]
  },
  "service_c": {
    "calls": [
      "service_o"
    ]
  },
  "service_o": {
    "calls": []
  }
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-dependencies/)
  * [Example](https://docs.datadoghq.com/api/latest/service-dependencies/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/service-dependencies/)
  * [Example](https://docs.datadoghq.com/api/latest/service-dependencies/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/service-dependencies/)
  * [Example](https://docs.datadoghq.com/api/latest/service-dependencies/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/service-dependencies/?code-lang=curl)


#####  Get all APM service dependencies
Copy
```
                  # Required query arguments  
export env="prod"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/service_dependencies?env=${env}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

* * *
## [Get one APM service's dependencies](https://docs.datadoghq.com/api/latest/service-dependencies/#get-one-apm-services-dependencies)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/service-dependencies/#get-one-apm-services-dependencies-v1)


**Note: This endpoint is in public beta. If you have any feedback, contact[Datadog support](https://docs.datadoghq.com/help/).**
GET https://api.ap1.datadoghq.com/api/v1/service_dependencies/{service}https://api.ap2.datadoghq.com/api/v1/service_dependencies/{service}https://api.datadoghq.eu/api/v1/service_dependencies/{service}https://api.ddog-gov.com/api/v1/service_dependencies/{service}https://api.datadoghq.com/api/v1/service_dependencies/{service}https://api.us3.datadoghq.com/api/v1/service_dependencies/{service}https://api.us5.datadoghq.com/api/v1/service_dependencies/{service}
### Overview
Get a specific service’s immediate upstream and downstream services. The services retrieved are filtered by environment and a primary tag, if one is defined.
### Arguments
#### Path Parameters
Name
Type
Description
service [_required_]
string
The name of the service go get dependencies for.
#### Query Strings
Name
Type
Description
env [_required_]
string
Specify what APM environment to query service dependencies by.
primary_tag
string
Specify what primary tag to query service dependencies by.
start
integer
Specify the start of the timeframe in epoch seconds to query for. (defaults to 1 hour before end parameter)
end
integer
Specify the end of the timeframe in epoch seconds to query for. (defaults to current time)
### Response
  * [200](https://docs.datadoghq.com/api/latest/service-dependencies/#ListSingleServiceDependencies-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/service-dependencies/#ListSingleServiceDependencies-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/service-dependencies/#ListSingleServiceDependencies-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/service-dependencies/#ListSingleServiceDependencies-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/service-dependencies/)
  * [Example](https://docs.datadoghq.com/api/latest/service-dependencies/)


An object with information on APM services that call, and are called by a given service.
Expand All
Field
Type
Description
called_by
[string]
List of service names that call the given service.
calls
[string]
List of service names called by the given service.
name
string
Name of the APM service being searched for.
```
{
  "called_by": [
    "service-a",
    "service-b"
  ],
  "calls": [
    "service-d",
    "service-e"
  ],
  "name": "service-c"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/service-dependencies/)
  * [Example](https://docs.datadoghq.com/api/latest/service-dependencies/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Authentication Error
  * [Model](https://docs.datadoghq.com/api/latest/service-dependencies/)
  * [Example](https://docs.datadoghq.com/api/latest/service-dependencies/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/service-dependencies/)
  * [Example](https://docs.datadoghq.com/api/latest/service-dependencies/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/service-dependencies/?code-lang=curl)


#####  Get one APM service's dependencies
Copy
```
                  # Path parameters  
export service="service-c"  
# Required query arguments  
export env="prod"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/service_dependencies/${service}?env=${env}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

* * *
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=449953a2-ded0-4cfd-8128-f6afaec2f2f4&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=1cfc1407-1ec0-4cb1-b7a6-766f3c572316&pt=Service%20Dependencies&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fservice-dependencies%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=449953a2-ded0-4cfd-8128-f6afaec2f2f4&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=1cfc1407-1ec0-4cb1-b7a6-766f3c572316&pt=Service%20Dependencies&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fservice-dependencies%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=4526f9cc-6e3b-4592-9a51-c2b58a472b99&bo=2&sid=8e9f03d0f0c011f0b53019aafced3101&vid=8e9f5e80f0c011f0a7890579f054930f&vids=1&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Service%20Dependencies&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fservice-dependencies%2F&r=&lt=901&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=40741)
