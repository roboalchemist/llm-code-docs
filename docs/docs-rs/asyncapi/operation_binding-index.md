asyncapi
# Module operation_binding 
Source 
## Structs§
AMQP1OperationBindingThis object MUST NOT contain any properties. Its name is reserved for future use.AMQPOperationBindingThis object contains information about the operation representation in AMQP.AnyPointMQOperationBindingThis object MUST NOT contain any properties. Its name is reserved for future use.HTTPOperationBindingExamplesJMSOperationBindingThis object MUST NOT contain any properties. Its name is reserved for future use.KafkaOperationBindingThis object contains information about the operation representation in Kafka.MQTT5OperationBindingThis object MUST NOT contain any properties. Its name is reserved for future use.MQTTOperationBindingThis object contains information about the operation representation in MQTT.MercureOperationBindingThis object MUST NOT contain any properties. Its name is reserved for future use.NATSOperationBindingOperationBindingMap describing protocol-specific definitions for an operation.RedisOperationBindingThis object MUST NOT contain any properties. Its name is reserved for future use.SNSOperationBindingThis object MUST NOT contain any properties. Its name is reserved for future use.SQSOperationBindingThis object MUST NOT contain any properties. Its name is reserved for future use.STOMPOperationBindingThis object MUST NOT contain any properties. Its name is reserved for future use.SolaceDestinationEach destination has the following structure. Note that bindings under a
‘subscribe’ operation define the behaviour of publishers, and those under a
‘publish’ operation define how subscribers are configured.SolaceDestinationQueueSolaceDestinationTopicSolaceOperationBindingWe need the ability to support several bindings for each operation, see the
Example
section for details.WebSocketsOperationBindingThis object MUST NOT contain any properties. Its name is reserved for future use.
## Enums§
SolaceDestinationDeliveryMode‘direct’ or ‘persistent’. This determines the quality of service for
publishing messages as documented
here.
Default is ‘persistent’.SolaceDestinationQueueAccessTypeSolaceDestinationType