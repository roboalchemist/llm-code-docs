asyncapi::server_binding
# Struct ServerBinding 
Source 

```
pub struct ServerBinding {}
```

## Fields§
§`http: Option<HTTPServerBinding>`

Protocol-specific information for an HTTP server.
§`ws: Option<WebsocketsServerBinding>`

Protocol-specific information for a WebSockets server.
§`kafka: Option<KafkaServerBinding>`

Protocol-specific information for a Kafka server.
§`anypointmq: Option<AnyPointMQServerBinding>`

Protocol-specific information for an Anypoint MQ server.
§`amqp: Option<AMPQServerBinding>`

Protocol-specific information for an AMQP 0-9-1 server.
§`ampq1: Option<AMPQ1ServerBinding>`

Protocol-specific information for an AMQP 1.0 server.
§`mqtt: Option<MQTTServerBinding>`

Protocol-specific information for an MQTT server.
§`mqtt5: Option<MQTT5ServerBinding>`

Protocol-specific information for an MQTT 5 server.
§`nats: Option<NATSServerBinding>`

Protocol-specific information for a NATS server.
§`jms: Option<JMSServerBinding>`

Protocol-specific information for a JMS server.
§`sns: Option<SNSServerBinding>`

Protocol-specific information for an SNS server.
§`solace: Option<SolaceServerBinding>`

Protocol-specific information for a Solace server.
§`sqs: Option<SQSServerBinding>`

Protocol-specific information for an SQS server.
§`stomp: Option<STOMPServerBinding>`

Protocol-specific information for a STOMP server.
§`redis: Option<RedisServerBinding>`

Protocol-specific information for a Redis server.
§`mercure: Option<MercureServerBinding>`

Protocol-specific information for a Mercure server.
§`ibmmq: Option<IBMMQServerBinding>`

Protocol-specific information for an IBM MQ server.
§`extensions: IndexMap<String, Value>`

This object can be extended with
Specification Extensions.

## Trait Implementations§