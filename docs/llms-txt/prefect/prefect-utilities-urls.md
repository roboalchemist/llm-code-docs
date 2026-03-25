# Source: https://docs.prefect.io/v3/api-ref/python/prefect-utilities-urls.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# urls

# `prefect.utilities.urls`

## Functions

### `validate_restricted_url` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/urls.py#L69" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
validate_restricted_url(url: str) -> None
```

Validate that the provided URL is safe for outbound requests.  This prevents
attacks like SSRF (Server Side Request Forgery), where an attacker can make
requests to internal services (like the GCP metadata service, localhost addresses,
or in-cluster Kubernetes services)

**Args:**

* `url`: The URL to validate.

**Raises:**

* `ValueError`: If the URL is a restricted URL.

### `convert_class_to_name` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/urls.py#L117" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
convert_class_to_name(obj: Any) -> str
```

Convert CamelCase class name to dash-separated lowercase name

### `url_for` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/urls.py#L126" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
url_for(obj: Union['PrefectFuture[Any]', 'Block', 'Variable', 'Automation', 'Resource', 'ReceivedEvent', BaseModel, str], obj_id: Optional[Union[str, UUID]] = None, url_type: URLType = 'ui', default_base_url: Optional[str] = None, **additional_format_kwargs: Any) -> Optional[str]
```

Returns the URL for a Prefect object.

Pass in a supported object directly or provide an object name and ID.

**Args:**

* `obj`:
  A Prefect object to get the URL for, or its URL name and ID.
* `obj_id`:
  The UUID of the object.
* `url_type`:
  Whether to return the URL for the UI (default) or API.
* `default_base_url`:
  The default base URL to use if no URL is configured.
* `additional_format_kwargs`:
  Additional keyword arguments to pass to the URL format.

**Returns:**

* Optional\[str]: The URL for the given object or None if the object is not supported.

**Examples:**

url\_for(my\_flow\_run)
url\_for(obj=my\_flow\_run)
url\_for("flow-run", obj\_id="123e4567-e89b-12d3-a456-426614174000")


Built with [Mintlify](https://mintlify.com).