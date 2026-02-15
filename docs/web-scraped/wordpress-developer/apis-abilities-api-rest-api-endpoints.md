# REST API endpoints

**Source:** [https://developer.wordpress.org/apis/abilities-api/rest-api-endpoints/](https://developer.wordpress.org/apis/abilities-api/rest-api-endpoints/)



# REST API endpoints




## In this article


Table of Contents- User access
- Controlling REST API Exposure
- SchemaAbility Object
- List AbilitiesDefinitionArgumentsExample RequestExample Response
- List CategoriesDefinitionArgumentsExample RequestExample Response
- Retrieve a CategoryDefinitionArgumentsExample RequestExample Response
- Retrieve an AbilityDefinitionArgumentsExample RequestExample Response
- Execute an AbilityDefinitionArgumentsExample Request (GET)Example Request (POST)Example Request (DELETE)Example Response (Success)Example Response (Error)
- AuthenticationUsing Application Passwords
- Error Responses



↑Back to top



The WordPress Abilities API provides REST endpoints that allow external systems to discover and execute abilities via HTTP requests.


## User access


Access to all Abilities REST API endpoints requires an authenticated user (see theAuthenticationsection). Access to execute individual Abilities is restricted based on thepermission_callback()of the Ability.


## Controlling REST API Exposure


By default, registered abilities arenotexposed via the REST API. You can control whether an individual ability appears in the REST API by using theshow_in_restmeta when registering the ability:


- show_in_rest => true: The ability is listed in REST API responses and can be executed via REST endpoints.
- show_in_rest => false(default): The ability is hidden from REST API listings and cannot be executed via REST endpoints. The ability remains available for internal PHP usage viawp_get_ability()and$ability->execute().


Abilities with metashow_in_rest => falsewill return arest_ability_not_founderror if accessed via REST endpoints.


## Schema


The Abilities API endpoints are available under the/wp-abilities/v1namespace.


### Ability Object


Abilities are represented in JSON with the following structure:


```
{
  "name": "wporg/get-site-info",
  "label": "Get Site Information",
  "description": "Retrieves basic information about the WordPress site.",
  "category": "site-information",
  "output_schema": {
    "type": "object",
    "properties": {
      "name": {
        "type": "string",
        "description": "Site name"
      },
      "url": {
        "type": "string",
        "format": "uri",
        "description": "Site URL"
      }
    }
  },
  "meta": {
    "annotations": {
      "instructions": "",
      "readonly": true,
      "destructive": false,
      "idempotent": false
    }
  }
}
```


## List Abilities


### Definition


GET /wp-abilities/v1/abilities


### Arguments


- page(integer): Current page of the collection. Default:1.
- per_page(integer): Maximum number of items to return per page. Default:50, Maximum:100.
- category(string): Filter abilities by category slug.


### Example Request


```
curl https://example.com/wp-json/wp-abilities/v1/abilities
```


### Example Response


```
[
  {
    "name": "wporg/get-site-info",
    "label": "Get Site Information",
    "description": "Retrieves basic information about the WordPress site.",
    "category": "site-information",
    "output_schema": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "Site name"
        },
        "url": {
          "type": "string",
          "format": "uri",
          "description": "Site URL"
        }
      }
    },
    "meta": {
      "annotations": {
        "instructions": "",
        "readonly": false,
        "destructive": true,
        "idempotent": false
      }
    }
  }
]
```


## List Categories


### Definition


GET /wp-abilities/v1/categories


### Arguments


- page(integer): Current page of the collection. Default:1.
- per_page(integer): Maximum number of items to return per page. Default:50, Maximum:100.


### Example Request


```
curl -u 'USERNAME:APPLICATION_PASSWORD' \
  https://example.com/wp-json/wp-abilities/v1/categories
```


### Example Response


```
[
  {
    "slug": "data-retrieval",
    "label": "Data Retrieval",
    "description": "Abilities that retrieve and return data from the WordPress site.",
    "meta": {},
    "_links": {
      "self": [
        {
          "href": "https://example.com/wp-json/wp-abilities/v1/categories/data-retrieval"
        }
      ],
      "collection": [
        {
          "href": "https://example.com/wp-json/wp-abilities/v1/categories"
        }
      ],
      "abilities": [
        {
          "href": "https://example.com/wp-json/wp-abilities/v1/?category=data-retrieval"
        }
      ]
    }
  }
]
```


## Retrieve a Category


### Definition


GET /wp-abilities/v1/categories/{slug}


### Arguments


- slug(string): The unique slug of the category.


### Example Request


```
curl -u 'USERNAME:APPLICATION_PASSWORD' \
  https://example.com/wp-json/wp-abilities/v1/categories/data-retrieval
```


### Example Response


```
{
  "slug": "data-retrieval",
  "label": "Data Retrieval",
  "description": "Abilities that retrieve and return data from the WordPress site.",
  "meta": {},
  "_links": {
    "self": [
      {
        "href": "https://example.com/wp-json/wp-abilities/v1/categories/data-retrieval"
      }
    ],
    "collection": [
      {
        "href": "https://example.com/wp-json/wp-abilities/v1/categories"
      }
    ],
    "abilities": [
      {
        "href": "https://example.com/wp-json/wp-abilities/v1?category=data-retrieval"
      }
    ]
  }
}
```


## Retrieve an Ability


### Definition


GET /wp-abilities/v1/(?P<namespace>[a-z0-9-]+)/(?P<ability>[a-z0-9-]+)


### Arguments


- namespace(string): The namespace part of the ability name.
- ability(string): The ability name part.


### Example Request


```
curl https://example.com/wp-json/wp-abilities/v1/my-plugin/get-site-info
```


### Example Response


```
{
  "name": "wporg/get-site-info",
  "label": "Get Site Information",
  "description": "Retrieves basic information about the WordPress site.",
  "category": "site-information",
  "output_schema": {
    "type": "object",
    "properties": {
      "name": {
        "type": "string",
        "description": "Site name"
      },
      "url": {
        "type": "string",
        "format": "uri",
        "description": "Site URL"
      }
    }
  },
  "meta": {
    "annotations": {
      "instructions": "",
      "readonly": true,
      "destructive": false,
      "idempotent": false
    }
  }
}
```


## Execute an Ability


Abilities are executed via the/runendpoint. The required HTTP method depends on the ability’s functionality andannotations:


- Read-only abilitiesmust useGET(readonly: true)
- Regular abilitiesmust useGETwhen they are readonly (readonly: true), andPOSTwhen they require an input (readonly: false)
- Destructive abilities(destructive: true) must useDELETE


This distinction ensures read-only operations use safe HTTP methods that can be cached and don’t modify server state.


### Definition


GET|POST|DELETE /wp-abilities/v1/(?P<namespace>[a-z0-9-]+)/(?P<ability>[a-z0-9-]+)/run


### Arguments


- namespace(string): The namespace part of the ability name.
- ability(string): The ability name part.
- input(integer|number|boolean|string|array|object|null): Optional input data for the ability as defined by its input schema.
- ForGETandDELETErequests: pass asinputquery parameter (URL-encoded JSON)
- ForPOSTrequests: pass in JSON body


### Example Request (GET)


```
# No input
curl https://example.com/wp-json/wp-abilities/v1/my-plugin/get-site-info/run

# With input (URL-encoded)
curl "https://example.com/wp-json/wp-abilities/v1/my-plugin/get-user-info/run?input=%7B%22user_id%22%3A1%7D"
```


### Example Request (POST)


```
# No input
curl -X POST https://example.com/wp-json/wp-abilities/v1/my-plugin/create-draft/run

# With input
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"input":{"option_name":"blogname","option_value":"New Site Name"}}' \
  https://example.com/wp-json/wp-abilities/v1/my-plugin/update-option/run
```


### Example Request (DELETE)


```
# With input (URL-encoded)
curl -X DELETE "https://example.com/wp-json/wp-abilities/v1/my-plugin/delete-post/run?input=%7B%22post_id%22%3A123%7D"
```


### Example Response (Success)


```
{
  "name": "My WordPress Site",
  "url": "https://example.com"
}
```


### Example Response (Error)


```
{
  "code": "ability_invalid_permissions",
  "message": "Ability \"my-plugin/update-option\" does not have necessary permission.",
  "data": {
    "status": 403
  }
}
```


## Authentication


The Abilities API supports all WordPress REST API authentication methods:


- Cookie authentication (same-origin requests)
- Application passwords (recommended for external access)
- Custom authentication plugins


### Using Application Passwords


```
curl -u 'USERNAME:APPLICATION_PASSWORD' \
  https://example.com/wp-json/wp-abilities/v1
```


## Error Responses


The API returns standard WordPress REST API error responses with these common codes:


- ability_missing_input_schema– the ability requires input but none was provided.
- ability_invalid_input– input validation failed according to the ability’s schema.
- ability_invalid_permissions– current user lacks permission to execute the ability.
- ability_invalid_output– output validation failed according to the ability’s schema.
- ability_invalid_execute_callback– the ability’s execute callback is not callable.
- rest_ability_not_found– the requested ability is not registered.
- rest_ability_category_not_found– the requested category is not registered.





First published


December 3, 2025






[PreviousPHP referencePrevious: PHP reference](https://developer.wordpress.org/apis/abilities-api/php-reference/)
[NextDashboard widgets APINext: Dashboard widgets API](https://developer.wordpress.org/apis/dashboard-widgets/)


