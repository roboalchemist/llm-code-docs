# Source: https://developers.make.com/custom-apps-documentation/component-blocks/api.md

# Communication

The Communication block defines how requests and responses are handled, as well as the output of a module. It may be a collection (single request + response) or an array of collections for multiple requests. Each collection follows the specification below.

## Specification

This is a complete form of the communication object. You can find detailed information on child pages.

```javascript
{
    "url": String,
    "encodeUrl": Boolean,
    "method": Enum[GET, POST, PUT, DELETE, OPTIONS],
    "qs": Flat Object,
    "headers": Flat Object,
    "body": Object|String|Array,
    "type": Enum[json, urlencoded, multipart/form-data, binary, text, string, raw],
    "ca": String,
    "condition": String|Boolean,
    "gzip": Boolean,
    "temp": Object,
    "aws": {
        "key": String,
        "secret": String,
        "session": String,
        "bucket": String,
        "sign_version": 2|4        
    },
    "response": {
        "type": {
            "*": Enum[json, urlencoded, xml, text, string, raw, binary, automatic],
            "[Number[-Number]]": Enum[json, urlencoded, xml, text, string, raw, binary, automatic]
        },
        "temp": Object,
        "iterate": {
            "container": String|Array,
            "condition": String|Boolean
        },
        "trigger": {
            "id": String,
            "date": String,
            "type": Enum[id, date],
            "order": Enum[asc, desc, unordered]
        },
        "output": String|Object|Array,
        "wrapper": String|Object|Array,
        "valid": String|Boolean,
        "error": {
            "message": String,
            "type": Enum[RuntimeError, DataError, RateLimitError, OutOfSpaceError, ConnectionError, InvalidConfigurationError, InvalidAccessTokenError, IncompleteDataError, DuplicateDataError],
            "[Number]": {
                "message": String,
                "type": Enum[RuntimeError, DataError, RateLimitError, OutOfSpaceError, ConnectionError, InvalidConfigurationError, InvalidAccessTokenError, IncompleteDataError, DuplicateDataError]
            }
        }
    },
    "pagination": {
        "mergeWithParent": Boolean,
        "url": String,
        "method": Enum[GET, POST, PUT, DELETE, OPTIONS],
        "headers": Flat Object,
        "qs": Flat Object,
        "body": Object|String|Array,
        "condition": String
    },
    "log": {
	"sanitize": Array
    },
    "repeat": {
        "condition": IMLString,  
        "delay": Number,                  
        "limit": Number                     
    }
}

```

## Escaping

If you need to access a key with certain special characters such as dots (`.`), spaces ( ) or dashes (`-`), you can use back ticks (`` `key.with.dots` ``) as an escape sequence in order to access the desired key.

{% tabs %}
{% tab title="Communication" %}

```json
"qs": {
    "query": "{{parameters.`key.with.dots`}}"
}
```

{% endtab %}

{% tab title="Parameters" %}

```json
{
    "name": "key.with.dots",
    "label": "Key With Dots",
    "type": "text"
}
```

{% endtab %}
{% endtabs %}

## Examples

### Action modules

{% tabs %}
{% tab title="Create a user" %}

```json
{
    "url": "/users",
    "method": "POST",
    "body": "{{parameters}}",
    "response": {
        "output": "{{body}}"
    }
}
```

{% endtab %}

{% tab title="Get a user" %}

```json
{
    "url": "/users/{{parameters.userId}}",
    "method": "GET",
    "response": {
        "output": "{{body}}"
    }
}
```

{% endtab %}
{% endtabs %}

### List module

{% tabs %}
{% tab title="Search users (cursor-based pagination)" %}

```json
{
    "url": "/users",
    "method": "GET",
    "qs": {
        "limit": "{{min(100, parameters.limit)}}", //per-page limit
        "search": "{{parameters.searchTerm}}"
    },
    "response": {
        "limit": "{{parameters.limit}}" // total limit of output bundles
        "output": {
            "iterate": "{{body.users}}",
            "output": "{{item}}"
        }
    },
    "pagination": {
        "condition": "{{body.nextPage}}",
        "qs": {
            "cursor": "{{body.nextPage}}"
        }
    }
}
```

{% endtab %}
{% endtabs %}
