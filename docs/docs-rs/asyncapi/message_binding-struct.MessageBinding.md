asyncapi::message_binding
# Struct MessageBinding 
Source 

```
pub struct MessageBinding {}
```

## Fields§
§`http: Option<HTTPMessageBinding>`

Protocol-specific information for an HTTP message, i.e., a request or a response.
§`ws: Option<WebSocketMessageBinding>`

Protocol-specific information for a WebSockets message.
§`kafka: Option<KafkaMessageBinding>`

Protocol-specific information for a Kafka message.
§`anypointmq: Option<AnyPointMQMessageBinding>`

Protocol-specific information for an Anypoint MQ message.
§`amqp: Option<AMQPMessageBinding>`

Protocol-specific information for an AMQP 0-9-1 message.
§`qmqp1: Option<AMQP1MessageBinding>`

Protocol-specific information for an AMQP 1.0 message.
§`mqtt: Option<MQTTMessageBinding>`

Protocol-specific information for an MQTT message.
§`mqtt5: Option<MQTT5MessageBinding>`

Protocol-specific information for an MQTT 5 message.
§`nats: Option<NATSMessageBinding>`

Protocol-specific information for a NATS message.
§`jms: Option<JMSMessageBinding>`

Protocol-specific information for a JMS message.
§`sns: Option<SNSMessageBinding>`

Protocol-specific information for an SNS message.
§`solace: Option<SolaceMessageBinding>`

Protocol-specific information for a Solace message.
§`sqs: Option<SQSMessageBinding>`

Protocol-specific information for an SQS message.
§`stomp: Option<STOMPMessageBinding>`

Protocol-specific information for a STOMP message.
§`redis: Option<RedisMessageBinding>`

Protocol-specific information for a Redis message.
§`mercure: Option<MercureMessageBinding>`

Protocol-specific information for a Mercure message.
§`ibmmq: Option<IBMMQMessageBinding>`

Protocol-specific information for an IBM MQ message.
§`extensions: IndexMap<String, Value>`

This object can be extended with
Specification Extensions.

## Trait Implementations§