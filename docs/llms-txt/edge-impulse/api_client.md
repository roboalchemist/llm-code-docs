# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api_client.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api_client

## Classes

### ApiClient

```python  theme={"system"}
edgeimpulse_api.api_client.ApiClient(
	configuration=None,
	header_name=None,
	header_value=None,
	cookie=None,
	pool_threads=1
)
```

| Parameters           |     |
| -------------------- | --- |
| `configuration=None` | ` ` |
| `header_name=None`   | ` ` |
| `header_value=None`  | ` ` |
| `cookie=None`        | ` ` |
| `pool_threads=1`     | ` ` |

| Class variables        |     |
| ---------------------- | --- |
| `NATIVE_TYPES_MAPPING` | ` ` |
| `PRIMITIVE_TYPES`      | ` ` |

| Instance variables |     |
| ------------------ | --- |
| `pool`             | ` ` |
| `user_agent`       | ` ` |

***

**STATIC METHODS**

#### get\_default

```python  theme={"system"}
edgeimpulse_api.api_client.ApiClient.get_default(
	
)
```

Return new instance of ApiClient.

This method returns newly created, based on default constructor,
object of ApiClient class or returns a copy of default
ApiClient.

#### set\_default

```python  theme={"system"}
edgeimpulse_api.api_client.ApiClient.set_default(
	default
)
```

Set default instance of ApiClient.

It stores default ApiClient.

| Parameters |     |
| ---------- | --- |
| `default`  | ` ` |

***

**METHODS**

#### call\_api

```python  theme={"system"}
edgeimpulse_api.api_client.ApiClient.call_api(
	self,
	resource_path,
	method,
	path_params=None,
	query_params=None,
	header_params=None,
	body=None,
	post_params=None,
	files=None,
	response_types_map=None,
	auth_settings=None,
	async_req=None,
	collection_formats=None
)
```

Makes the HTTP request (synchronous) and returns deserialized data.

To make an async\_req request, set the async\_req parameter.

| Parameters                |     |
| ------------------------- | --- |
| `self`                    | ` ` |
| `resource_path`           | ` ` |
| `method`                  | ` ` |
| `path_params=None`        | ` ` |
| `query_params=None`       | ` ` |
| `header_params=None`      | ` ` |
| `body=None`               | ` ` |
| `post_params=None`        | ` ` |
| `files=None`              | ` ` |
| `response_types_map=None` | ` ` |
| `auth_settings=None`      | ` ` |
| `async_req=None`          | ` ` |
| `collection_formats=None` | ` ` |

#### close

```python  theme={"system"}
edgeimpulse_api.api_client.ApiClient.close(
	self
)
```

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### deserialize

```python  theme={"system"}
edgeimpulse_api.api_client.ApiClient.deserialize(
	self,
	response,
	response_type
)
```

Deserializes response into an object.

| Parameters      |     |
| --------------- | --- |
| `self`          | ` ` |
| `response`      | ` ` |
| `response_type` | ` ` |

#### files\_parameters

```python  theme={"system"}
edgeimpulse_api.api_client.ApiClient.files_parameters(
	self,
	files=None
)
```

Builds form parameters.

| Parameters   |     |
| ------------ | --- |
| `self`       | ` ` |
| `files=None` | ` ` |

#### parameters\_to\_tuples

```python  theme={"system"}
edgeimpulse_api.api_client.ApiClient.parameters_to_tuples(
	self,
	params,
	collection_formats
)
```

Get parameters as list of tuples, formatting collections.

| Parameters           |     |
| -------------------- | --- |
| `self`               | ` ` |
| `params`             | ` ` |
| `collection_formats` | ` ` |

#### parameters\_to\_url\_query

```python  theme={"system"}
edgeimpulse_api.api_client.ApiClient.parameters_to_url_query(
	self,
	params,
	collection_formats
)
```

Get parameters as list of tuples, formatting collections.

| Parameters           |     |
| -------------------- | --- |
| `self`               | ` ` |
| `params`             | ` ` |
| `collection_formats` | ` ` |

#### request

```python  theme={"system"}
edgeimpulse_api.api_client.ApiClient.request(
	self,
	method,
	url,
	query_params=None,
	headers=None,
	post_params=None,
	body=None
)
```

Makes the HTTP request using RESTClient.

| Parameters          |     |
| ------------------- | --- |
| `self`              | ` ` |
| `method`            | ` ` |
| `url`               | ` ` |
| `query_params=None` | ` ` |
| `headers=None`      | ` ` |
| `post_params=None`  | ` ` |
| `body=None`         | ` ` |

#### sanitize\_for\_serialization

```python  theme={"system"}
edgeimpulse_api.api_client.ApiClient.sanitize_for_serialization(
	self,
	obj
)
```

Builds a JSON POST object.

If obj is None, return None.
If obj is str, int, long, float, bool, return directly.
If obj is datetime.datetime, datetime.date
convert to string in iso8601 format.
If obj is list, sanitize each element in the list.
If obj is dict, return the dict.
If obj is OpenAPI model, return the properties dict.

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |
| `obj`      | ` ` |

#### select\_header\_accept

```python  theme={"system"}
edgeimpulse_api.api_client.ApiClient.select_header_accept(
	self,
	accepts
)
```

Returns `Accept` based on an array of accepts provided.

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |
| `accepts`  | ` ` |

#### select\_header\_content\_type

```python  theme={"system"}
edgeimpulse_api.api_client.ApiClient.select_header_content_type(
	self,
	content_types
)
```

Returns `Content-Type` based on an array of content\_types provided.

| Parameters      |     |
| --------------- | --- |
| `self`          | ` ` |
| `content_types` | ` ` |

#### set\_default\_header

```python  theme={"system"}
edgeimpulse_api.api_client.ApiClient.set_default_header(
	self,
	header_name,
	header_value
)
```

| Parameters     |     |
| -------------- | --- |
| `self`         | ` ` |
| `header_name`  | ` ` |
| `header_value` | ` ` |

#### update\_params\_for\_auth

```python  theme={"system"}
edgeimpulse_api.api_client.ApiClient.update_params_for_auth(
	self,
	headers,
	queries,
	auth_settings,
	resource_path,
	method,
	body,
	request_auth=None
)
```

Updates header and query params based on authentication setting.

| Parameters          |     |
| ------------------- | --- |
| `self`              | ` ` |
| `headers`           | ` ` |
| `queries`           | ` ` |
| `auth_settings`     | ` ` |
| `resource_path`     | ` ` |
| `method`            | ` ` |
| `body`              | ` ` |
| `request_auth=None` | ` ` |


Built with [Mintlify](https://mintlify.com).