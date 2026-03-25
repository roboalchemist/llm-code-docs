# Source: https://docs.nats.io/nats-concepts/connectivity.md

# Connectivity

NATS supports several kinds of connectivity *directly* to the NATS servers.

* Plain NATS connections
* TLS encrypted NATS connections
* [WebSocket](https://github.com/nats-io/nats.ws) NATS connections
* [MQTT](https://docs.nats.io/running-a-nats-service/configuration/mqtt) client connections

There is also a number of adapters available to bridge traffic to and from other messaging systems

* [Kafka Bridge](https://github.com/nats-io/nats-kafka)
* [JMS](https://github.com/nats-io/nats-jms-bridge) which can also be used to bridge MQ and RabbitMQ, since they both offer a JMS interface
