# Source: https://docs.datadoghq.com/developers/guide/query-the-infrastructure-list-via-the-api.md

---
title: Query the Infrastructure List with the API
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Developers > Developer Guides > Query the Infrastructure List with the
  API
---

# Query the Infrastructure List with the API

If you're a more advanced Datadog user, you may want to use [the API](https://docs.datadoghq.com/api/) to query general data about infrastructureâthe kind of data that you can find in your [infrastructure list](https://app.datadoghq.com/infrastructure) or the [host map](https://app.datadoghq.com/infrastructure/map). You can do this with an API GET request on the [api/v1/hosts](https://docs.datadoghq.com/api/v1/hosts/) endpoint.

## Examples{% #examples %}

If, for example, you want to query general data from all your hosts that include the `env:prod` and `role:elasticsearch` tag, you can make the following API call with Python's `requests` library:

```python
import requests
s = requests.session()
s.params = {
  'api_key': '<DATADOG_API_KEY>',
  'application_key': '<YOUR_APPLICATION_KEY>',
  'filter': 'env:prod,role:elasticsearch'
}
infra_link = 'https://app.datadoghq.com/api/v1/hosts'
infra_content = s.request(
  method='GET', url=infra_link, params=s.params
).json()
```

To iterate over all the hosts in your infrastructure, use the following:

```python
import requests
def iterate_all_hosts():
  s = requests.session()
  s.params = {
    'api_key': '<DATADOG_API_KEY>',
    'application_key': '<YOUR_APPLICATION_KEY>',
    'include_muted_hosts_data': False,
    'include_hosts_metadata': False,
    'start': 0
  }
  infra_link = 'https://app.datadoghq.com/api/v1/hosts?count=1000'
  while True:
    response = s.request(method='GET', url=infra_link, params=s.params).json()
    for host in response['host_list']:
        yield host
    if response['total_returned'] == 0:
        return
    s.params['start'] += response['total_returned']

for host in iterate_all_hosts():
    print(host['host_name'])
```
