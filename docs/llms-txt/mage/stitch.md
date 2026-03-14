# Source: https://docs.mage.ai/integrations/stitch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Stitch in Mage

> Trigger syncs in Stitch.

## Configuration

Here are the following keyword arguments that can be used for configuration:

| Keyword argument | Description                                                                                                  | Sample value |
| ---------------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| `access_token`   | [Stitch API access token](https://www.stitchdata.com/docs/developers/stitch-connect/api#obtain-access-token) | `abc123`     |

***

## Example code

Trigger sync with `source_id`.

```python  theme={"system"}
from mage_ai.services.stitch.stitch import StitchClient


client = StitchClient(config=dict(access_token='access_token'))

sources = client.list_sources()
source_id = sources[0]['id'] # Get source id

client.start_replication_job(source_id) # Start replication job
```

Sample output:

```
Start replication job for source 11111. Job name: 111111.222222.sync.abcd1234-a96e-4b48-a10c-9de147a72d64.
Polling Stitch extraction status for source 11111. Current status: running.
Polling Stitch extraction status for source 11111. Current status: running.
Polling Stitch extraction status for source 11111. Current status: running.
Extraction for source 11111 completed.
Finish loading data for all streams: ['stream_1', 'stream_2'].
```


Built with [Mintlify](https://mintlify.com).