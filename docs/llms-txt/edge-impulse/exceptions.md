# Source: https://docs.edgeimpulse.com/tools/libraries/sdks/studio/python/edgeimpulse/exceptions.md

# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/exceptions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.exceptions

## Functions

### render\_path

```python  theme={"system"}
edgeimpulse_api.exceptions.render_path(
	path_to_item
)
```

Returns a string representation of a path

| Parameters     |     |
| -------------- | --- |
| `path_to_item` | ` ` |

## Classes

### ApiAttributeError

```python  theme={"system"}
edgeimpulse_api.exceptions.ApiAttributeError(
	msg,
	path_to_item=None
)
```

The base exception class for all OpenAPIExceptions

Raised when an attribute reference or assignment fails.

| Parameters          |     |
| ------------------- | --- |
| `msg`               | ` ` |
| `path_to_item=None` | ` ` |

| Bases                                         |
| --------------------------------------------- |
| `edgeimpulse_api.exceptions.OpenApiException` |
| `builtins.AttributeError`                     |
| `builtins.Exception`                          |
| `builtins.BaseException`                      |

### ApiException

```python  theme={"system"}
edgeimpulse_api.exceptions.ApiException(
	status=None,
	reason=None,
	http_resp=None
)
```

The base exception class for all OpenAPIExceptions

| Parameters       |     |
| ---------------- | --- |
| `status=None`    | ` ` |
| `reason=None`    | ` ` |
| `http_resp=None` | ` ` |

| Bases                                         |
| --------------------------------------------- |
| `edgeimpulse_api.exceptions.OpenApiException` |
| `builtins.Exception`                          |
| `builtins.BaseException`                      |

| Classes                                            |
| -------------------------------------------------- |
| `edgeimpulse_api.exceptions.ForbiddenException`    |
| `edgeimpulse_api.exceptions.NotFoundException`     |
| `edgeimpulse_api.exceptions.ServiceException`      |
| `edgeimpulse_api.exceptions.UnauthorizedException` |

### ApiKeyError

```python  theme={"system"}
edgeimpulse_api.exceptions.ApiKeyError(
	msg,
	path_to_item=None
)
```

The base exception class for all OpenAPIExceptions

| Parameters          |     |
| ------------------- | --- |
| `msg`               | ` ` |
| `path_to_item=None` | ` ` |

| Bases                                         |
| --------------------------------------------- |
| `edgeimpulse_api.exceptions.OpenApiException` |
| `builtins.KeyError`                           |
| `builtins.LookupError`                        |
| `builtins.Exception`                          |
| `builtins.BaseException`                      |

### ApiTypeError

```python  theme={"system"}
edgeimpulse_api.exceptions.ApiTypeError(
	msg,
	path_to_item=None,
	valid_classes=None,
	key_type=None
)
```

The base exception class for all OpenAPIExceptions

Raises an exception for TypeErrors

| Parameters           |     |
| -------------------- | --- |
| `msg`                | ` ` |
| `path_to_item=None`  | ` ` |
| `valid_classes=None` | ` ` |
| `key_type=None`      | ` ` |

| Bases                                         |
| --------------------------------------------- |
| `edgeimpulse_api.exceptions.OpenApiException` |
| `builtins.TypeError`                          |
| `builtins.Exception`                          |
| `builtins.BaseException`                      |

### ApiValueError

```python  theme={"system"}
edgeimpulse_api.exceptions.ApiValueError(
	msg,
	path_to_item=None
)
```

The base exception class for all OpenAPIExceptions

| Parameters          |     |
| ------------------- | --- |
| `msg`               | ` ` |
| `path_to_item=None` | ` ` |

| Bases                                         |
| --------------------------------------------- |
| `edgeimpulse_api.exceptions.OpenApiException` |
| `builtins.ValueError`                         |
| `builtins.Exception`                          |
| `builtins.BaseException`                      |

### ForbiddenException

```python  theme={"system"}
edgeimpulse_api.exceptions.ForbiddenException(
	status=None,
	reason=None,
	http_resp=None
)
```

The base exception class for all OpenAPIExceptions

| Parameters       |     |
| ---------------- | --- |
| `status=None`    | ` ` |
| `reason=None`    | ` ` |
| `http_resp=None` | ` ` |

| Bases                                         |
| --------------------------------------------- |
| `edgeimpulse_api.exceptions.ApiException`     |
| `edgeimpulse_api.exceptions.OpenApiException` |
| `builtins.Exception`                          |
| `builtins.BaseException`                      |

### NotFoundException

```python  theme={"system"}
edgeimpulse_api.exceptions.NotFoundException(
	status=None,
	reason=None,
	http_resp=None
)
```

The base exception class for all OpenAPIExceptions

| Parameters       |     |
| ---------------- | --- |
| `status=None`    | ` ` |
| `reason=None`    | ` ` |
| `http_resp=None` | ` ` |

| Bases                                         |
| --------------------------------------------- |
| `edgeimpulse_api.exceptions.ApiException`     |
| `edgeimpulse_api.exceptions.OpenApiException` |
| `builtins.Exception`                          |
| `builtins.BaseException`                      |

### OpenApiException

```python  theme={"system"}
edgeimpulse_api.exceptions.OpenApiException(
	*args,
	**kwargs
)
```

The base exception class for all OpenAPIExceptions

| Parameters |     |
| ---------- | --- |
| `*args`    | ` ` |
| `**kwargs` | ` ` |

| Bases                    |
| ------------------------ |
| `builtins.Exception`     |
| `builtins.BaseException` |

| Classes                                        |
| ---------------------------------------------- |
| `edgeimpulse_api.exceptions.ApiAttributeError` |
| `edgeimpulse_api.exceptions.ApiException`      |
| `edgeimpulse_api.exceptions.ApiKeyError`       |
| `edgeimpulse_api.exceptions.ApiTypeError`      |
| `edgeimpulse_api.exceptions.ApiValueError`     |

### ServiceException

```python  theme={"system"}
edgeimpulse_api.exceptions.ServiceException(
	status=None,
	reason=None,
	http_resp=None
)
```

The base exception class for all OpenAPIExceptions

| Parameters       |     |
| ---------------- | --- |
| `status=None`    | ` ` |
| `reason=None`    | ` ` |
| `http_resp=None` | ` ` |

| Bases                                         |
| --------------------------------------------- |
| `edgeimpulse_api.exceptions.ApiException`     |
| `edgeimpulse_api.exceptions.OpenApiException` |
| `builtins.Exception`                          |
| `builtins.BaseException`                      |

### UnauthorizedException

```python  theme={"system"}
edgeimpulse_api.exceptions.UnauthorizedException(
	status=None,
	reason=None,
	http_resp=None
)
```

The base exception class for all OpenAPIExceptions

| Parameters       |     |
| ---------------- | --- |
| `status=None`    | ` ` |
| `reason=None`    | ` ` |
| `http_resp=None` | ` ` |

| Bases                                         |
| --------------------------------------------- |
| `edgeimpulse_api.exceptions.ApiException`     |
| `edgeimpulse_api.exceptions.OpenApiException` |
| `builtins.Exception`                          |
| `builtins.BaseException`                      |


Built with [Mintlify](https://mintlify.com).