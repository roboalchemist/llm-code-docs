# Source: https://docs.mage.ai/guides/streaming/sources/rabbitmq.md

# Source: https://docs.mage.ai/guides/streaming/destinations/rabbitmq.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# RabbitMQ

## Basic config

```yaml  theme={"system"}
connector_type: rabbitmq
connection_host: 'localhost'
connection_port: 5672
queue_name: 'queue_name'
username: 'guest'
password: 'guest'
amqp_url_virtual_host: '%2f'
url_protocol: 'amqp'
```


Built with [Mintlify](https://mintlify.com).