# Source: https://docs.architect.co/sdk-reference/connection-management.md

# Connection management

* [Get cpty status](#get-cpty-status)

## Get cpty status

Get the status of a cpty connection.

{% tabs %}
{% tab title="Python" %}

```python
status = await client.cpty_status(kind="binance")
```

{% endtab %}
{% endtabs %}

Returned fields:

* `connected`: true iff all component connections are connected, e.g. sockets are connected
* `stale`: true iff any component connection is stale, e.g. missed a protocol heartbeat
* `logged_in`: true iff all component connections are logged in (if relevant)
* `connections`: map of individual connections statuses relevant to the cpty
* `connections.connected`: connection is physically established, e.g. socket is connected
* `connections.last_heartbeat`: UNIX timestamp (seconds) of last heartbeat from connection, or `-1` for never
* `connections.last_heartbeat_stale_threshold`: threshold in seconds for considering a connection stale, e.g. if a heartbeat is missed
* `connections.logged_in`: true if connection is logged in, or `null` if not relevant
