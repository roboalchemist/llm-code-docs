# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/rest.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.rest

## Classes

### RESTClientObject

```python  theme={"system"}
edgeimpulse_api.rest.RESTClientObject(
	configuration,
	pools_size=4,
	maxsize=None
)
```

| Parameters      |     |
| --------------- | --- |
| `configuration` | ` ` |
| `pools_size=4`  | ` ` |
| `maxsize=None`  | ` ` |

***

**METHODS**

#### delete\_request

```python  theme={"system"}
edgeimpulse_api.rest.RESTClientObject.delete_request(
	self,
	url,
	headers=None,
	query_params=None,
	body=None
)
```

| Parameters          |     |
| ------------------- | --- |
| `self`              | ` ` |
| `url`               | ` ` |
| `headers=None`      | ` ` |
| `query_params=None` | ` ` |
| `body=None`         | ` ` |

#### get\_request

```python  theme={"system"}
edgeimpulse_api.rest.RESTClientObject.get_request(
	self,
	url,
	headers=None,
	query_params=None
)
```

| Parameters          |     |
| ------------------- | --- |
| `self`              | ` ` |
| `url`               | ` ` |
| `headers=None`      | ` ` |
| `query_params=None` | ` ` |

#### head\_request

```python  theme={"system"}
edgeimpulse_api.rest.RESTClientObject.head_request(
	self,
	url,
	headers=None,
	query_params=None
)
```

| Parameters          |     |
| ------------------- | --- |
| `self`              | ` ` |
| `url`               | ` ` |
| `headers=None`      | ` ` |
| `query_params=None` | ` ` |

#### options\_request

```python  theme={"system"}
edgeimpulse_api.rest.RESTClientObject.options_request(
	self,
	url,
	headers=None,
	query_params=None,
	post_params=None,
	body=None
)
```

| Parameters          |     |
| ------------------- | --- |
| `self`              | ` ` |
| `url`               | ` ` |
| `headers=None`      | ` ` |
| `query_params=None` | ` ` |
| `post_params=None`  | ` ` |
| `body=None`         | ` ` |

#### patch\_request

```python  theme={"system"}
edgeimpulse_api.rest.RESTClientObject.patch_request(
	self,
	url,
	headers=None,
	query_params=None,
	post_params=None,
	body=None
)
```

| Parameters          |     |
| ------------------- | --- |
| `self`              | ` ` |
| `url`               | ` ` |
| `headers=None`      | ` ` |
| `query_params=None` | ` ` |
| `post_params=None`  | ` ` |
| `body=None`         | ` ` |

#### post\_request

```python  theme={"system"}
edgeimpulse_api.rest.RESTClientObject.post_request(
	self,
	url,
	headers=None,
	query_params=None,
	post_params=None,
	body=None
)
```

| Parameters          |     |
| ------------------- | --- |
| `self`              | ` ` |
| `url`               | ` ` |
| `headers=None`      | ` ` |
| `query_params=None` | ` ` |
| `post_params=None`  | ` ` |
| `body=None`         | ` ` |

#### put\_request

```python  theme={"system"}
edgeimpulse_api.rest.RESTClientObject.put_request(
	self,
	url,
	headers=None,
	query_params=None,
	post_params=None,
	body=None
)
```

| Parameters          |     |
| ------------------- | --- |
| `self`              | ` ` |
| `url`               | ` ` |
| `headers=None`      | ` ` |
| `query_params=None` | ` ` |
| `post_params=None`  | ` ` |
| `body=None`         | ` ` |

#### request

```python  theme={"system"}
edgeimpulse_api.rest.RESTClientObject.request(
	self,
	method,
	url,
	query_params=None,
	headers=None,
	body=None,
	post_params=None
)
```

Perform requests.

| Parameters          |     |
| ------------------- | --- |
| `self`              | ` ` |
| `method`            | ` ` |
| `url`               | ` ` |
| `query_params=None` | ` ` |
| `headers=None`      | ` ` |
| `body=None`         | ` ` |
| `post_params=None`  | ` ` |

### RESTResponse

```python  theme={"system"}
edgeimpulse_api.rest.RESTResponse(
	resp
)
```

The abstract base class for all I/O classes.

This class provides dummy implementations for many methods that
derived classes can override selectively; the default implementations
represent a file that cannot be read, written or seeked.

Even though IOBase does not declare read, readinto, or write because
their signatures will vary, implementations and clients should
consider those methods part of the interface. Also, implementations
may raise UnsupportedOperation when operations they do not support are
called.

The basic type used for binary data read from or written to a file is
bytes. Other bytes-like objects are accepted as method arguments too.
In some cases (such as readinto), a writable object is required. Text
I/O classes work with str data.

Note that calling any method (except additional calls to close(),
which are ignored) on a closed stream should raise a ValueError.

IOBase (and its subclasses) support the iterator protocol, meaning
that an IOBase object can be iterated over yielding the lines in a
stream.

IOBase also supports the :keyword:`with` statement. In this example,
fp is closed after the suite of the with statement is complete:

with open('spam.txt', 'r') as fp:
fp.write('Spam and eggs!')

| Parameters |     |
| ---------- | --- |
| `resp`     | ` ` |

| Bases         |
| ------------- |
| `io.IOBase`   |
| `_io._IOBase` |

***

**METHODS**

#### getheader

```python  theme={"system"}
edgeimpulse_api.rest.RESTResponse.getheader(
	self,
	name,
	default=None
)
```

Returns a given response header.

| Parameters     |     |
| -------------- | --- |
| `self`         | ` ` |
| `name`         | ` ` |
| `default=None` | ` ` |

#### getheaders

```python  theme={"system"}
edgeimpulse_api.rest.RESTResponse.getheaders(
	self
)
```

Returns a dictionary of the response headers.

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |


Built with [Mintlify](https://mintlify.com).