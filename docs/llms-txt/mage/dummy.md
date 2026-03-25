# Source: https://docs.mage.ai/guides/streaming/destinations/dummy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Dummy

Dummy sink will print the message optionally and discard the message. This dummy sink will be useful when users want to trigger other pipelines or 3rd party services using the ingested data in transformer.

## Config

```yaml  theme={"system"}
connector_type: dummy
print_msg: true
```


Built with [Mintlify](https://mintlify.com).