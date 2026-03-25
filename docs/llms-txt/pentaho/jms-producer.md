# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/jms-producer.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/jms-producer.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/jms-producer.md

# JMS Producer

The JMS Producer step publishes messages in near-real-time to the Apache ActiveMQ Java Messaging Service (JMS) server or IBM MQ middleware. You may use the JMS Producer step to define a transformation which publishes a [stream of records](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/streaming-analytics) to a JMS queue for every update of a warehouse. In turn, this queue could then launch another job that flushes an application cache.
