# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/configuration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.configuration

## Classes

### Configuration

```python  theme={"system"}
edgeimpulse_api.configuration.Configuration(
	host=None,
	api_key=None,
	api_key_prefix=None,
	username=None,
	password=None,
	access_token=None,
	server_index=None,
	server_variables=None,
	server_operation_index=None,
	server_operation_variables=None,
	ssl_ca_cert=None
)
```

| Parameters                        |     |
| --------------------------------- | --- |
| `host=None`                       | ` ` |
| `api_key=None`                    | ` ` |
| `api_key_prefix=None`             | ` ` |
| `username=None`                   | ` ` |
| `password=None`                   | ` ` |
| `access_token=None`               | ` ` |
| `server_index=None`               | ` ` |
| `server_variables=None`           | ` ` |
| `server_operation_index=None`     | ` ` |
| `server_operation_variables=None` | ` ` |
| `ssl_ca_cert=None`                | ` ` |

| Instance variables           |     |
| ---------------------------- | --- |
| `access_token`               | ` ` |
| `assert_hostname`            | ` ` |
| `cert_file`                  | ` ` |
| `connection_pool_maxsize`    | ` ` |
| `debug`                      | ` ` |
| `host`                       | ` ` |
| `key_file`                   | ` ` |
| `logger`                     | ` ` |
| `logger_file`                | ` ` |
| `logger_file_handler`        | ` ` |
| `logger_format`              | ` ` |
| `logger_stream_handler`      | ` ` |
| `password`                   | ` ` |
| `proxy`                      | ` ` |
| `proxy_headers`              | ` ` |
| `refresh_api_key_hook`       | ` ` |
| `retries`                    | ` ` |
| `safe_chars_for_path_param`  | ` ` |
| `server_operation_index`     | ` ` |
| `server_operation_variables` | ` ` |
| `socket_options`             | ` ` |
| `ssl_ca_cert`                | ` ` |
| `temp_folder_path`           | ` ` |
| `username`                   | ` ` |
| `verify_ssl`                 | ` ` |

***

**STATIC METHODS**

#### get\_default

```python  theme={"system"}
edgeimpulse_api.configuration.Configuration.get_default(
	
)
```

Return the default configuration.

This method returns newly created, based on default constructor,
object of Configuration class or returns a copy of default
configuration.

#### get\_default\_copy

```python  theme={"system"}
edgeimpulse_api.configuration.Configuration.get_default_copy(
	
)
```

Deprecated. Please use `get_default` instead.

Deprecated. Please use `get_default` instead.

#### set\_default

```python  theme={"system"}
edgeimpulse_api.configuration.Configuration.set_default(
	default
)
```

Set default instance of configuration.

It stores default configuration, which can be
returned by get\_default\_copy method.

| Parameters |     |
| ---------- | --- |
| `default`  | ` ` |

***

**METHODS**

#### auth\_settings

```python  theme={"system"}
edgeimpulse_api.configuration.Configuration.auth_settings(
	self
)
```

Gets Auth Settings dict for api client.

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### get\_api\_key\_with\_prefix

```python  theme={"system"}
edgeimpulse_api.configuration.Configuration.get_api_key_with_prefix(
	self,
	identifier,
	alias=None
)
```

Gets API key (with prefix if set).

| Parameters   |     |
| ------------ | --- |
| `self`       | ` ` |
| `identifier` | ` ` |
| `alias=None` | ` ` |

#### get\_basic\_auth\_token

```python  theme={"system"}
edgeimpulse_api.configuration.Configuration.get_basic_auth_token(
	self
)
```

Gets HTTP basic authentication header (string).

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### get\_host\_from\_settings

```python  theme={"system"}
edgeimpulse_api.configuration.Configuration.get_host_from_settings(
	self,
	index,
	variables=None,
	servers=None
)
```

Gets host URL based on the index and variables

| Parameters       |     |
| ---------------- | --- |
| `self`           | ` ` |
| `index`          | ` ` |
| `variables=None` | ` ` |
| `servers=None`   | ` ` |

#### get\_host\_settings

```python  theme={"system"}
edgeimpulse_api.configuration.Configuration.get_host_settings(
	self
)
```

Gets an array of host settings

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_debug\_report

```python  theme={"system"}
edgeimpulse_api.configuration.Configuration.to_debug_report(
	self
)
```

Gets the essential information for debugging.

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |


Built with [Mintlify](https://mintlify.com).