asyncapi::operation_binding
# Struct OperationBinding 
Source 

```
pub struct OperationBinding {}
```

## Fields§
§`http: Option<HTTPOperationBinding>`

Protocol-specific information for an HTTP operation
§`ws: Option<WebSocketsOperationBinding>`

Protocol-specific information for a WebSockets operation
§`kafka: Option<KafkaOperationBinding>`

Protocol-specific information for a Kafka operation
§`anypointmq: Option<AnyPointMQOperationBinding>`

Protocol-specific information for an Anypoint MQ operation.
§`amqp: Option<AMQPOperationBinding>`

Protocol-specific information for an AMPQ operation
§`amqp1: Option<AMQP1OperationBinding>`

Protocol-specific information for an AMQP 1.0 operation
§`mqtt: Option<MQTTOperationBinding>`

Protocol-specific information for an MQTT operation
§`mqtt5: Option<MQTT5OperationBinding>`

Protocol-specific information for an MQTT 5 operation
§`nats: Option<NATSOperationBinding>`

Protocol-specific information for a NATS operation
§`jms: Option<JMSOperationBinding>`

Protocol-specific information for a JMS operation
§`sns: Option<SNSOperationBinding>`

Protocol-specific information for an SNS operation
§`solace: Option<SolaceOperationBinding>`

Protocol-specific information for a Solace operation
§`sqs: Option<SQSOperationBinding>`

Protocol-specific information for an SQS operation
§`stomp: Option<STOMPOperationBinding>`

Protocol-specific information for a STOMP operation
§`redis: Option<RedisOperationBinding>`

Protocol-specific information for a Redis operation
§`mercure: Option<MercureOperationBinding>`

Protocol-specific information for a Mercure operation
§`extensions: IndexMap<String, Value>`

This object can be extended with
Specification Extensions.

## Trait Implementations§