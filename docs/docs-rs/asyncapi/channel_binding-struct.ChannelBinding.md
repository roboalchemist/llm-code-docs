asyncapi::channel_binding
# Struct ChannelBinding 
Source 

```
pub struct ChannelBinding {}
```

## Fields§
§`http: Option<HTTPChannelBinding>`

Protocol-specific information for an HTTP channel.
§`ws: Option<WebsocketsChannelBinding>`

Protocol-specific information for a WebSockets channel.
§`kafka: Option<KafkaChannelBinding>`

Protocol-specific information for a Kafka channel.
§`anypointmq: Option<AnyPointMQChannelBinding>`

Protocol-specific information for an Anypoint MQ channel.
§`amqp: Option<AMQPChannelBinding>`

Protocol-specific information for an AMQP 0-9-1 channel.
§`amqp1: Option<AMQPChannelBinding>`

Protocol-specific information for an AMQP 1.0 channel.
§`mqtt: Option<MQTTChannelBinding>`

Protocol-specific information for an MQTT channel.
§`mqtt5: Option<MQTT5ChannelBinding>`

Protocol-specific information for an MQTT 5 channel.
§`nats: Option<NATSChannelBinding>`

Protocol-specific information for a NATS channel.
§`jms: Option<JMSChannelBinding>`

Protocol-specific information for a JMS channel.
§`sns: Option<SNSChannelBinding>`

Protocol-specific information for an SNS channel.
§`solace: Option<SolaceChannelBinding>`

Protocol-specific information for a Solace channel.
§`sqs: Option<SQSChannelBinding>`

Protocol-specific information for an SQS channel.
§`stomp: Option<STOMPChannelBinding>`

Protocol-specific information for a STOMP channel.
§`redis: Option<RedisChannelBinding>`

Protocol-specific information for a Redis channel.
§`mercure: Option<MercureChannelBinding>`

Protocol-specific information for a Mercure channel.
§`ibmmq: Option<IBMMQChannelBinding>`

Protocol-specific information for an IBM MQ channel.
§`extensions: IndexMap<String, Value>`

This object can be extended with
Specification Extensions.

## Trait Implementations§