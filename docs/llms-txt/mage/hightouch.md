# Source: https://docs.mage.ai/integrations/hightouch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Hightouch in Mage

> Trigger syncs in Hightouch.

## Configuration

Here are the following keyword arguments that can be used for configuration:

| Keyword argument | Description                                                               | Sample value |
| ---------------- | ------------------------------------------------------------------------- | ------------ |
| `api_key`        | [Hightouch API key](https://hightouch.com/docs/developer-tools/api-guide) | `abc123`     |

***

## Example code

Trigger sync with `sync_id`.

```python  theme={"system"}
from mage_ai.services.hightouch.hightouch import HightouchClient


client = HightouchClient(config=dict(api_key='api_key'))
syncs = client.list_syncs()      # Get all the syncs
sync_id = syncs['data'][0]['id'] # Get sync id
client.sync_and_poll(sync_id)    # Trigger sync and poll status
```

Sample output:

```
Polling Hightouch Sync [id]. Current status: querying. 0% completed.
Polling Hightouch Sync [id]. Current status: success. 100% completed.
Sync request status: success. Polling complete
```


Built with [Mintlify](https://mintlify.com).