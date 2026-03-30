# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/amqp-consumer/options-amqp-consumer/use-an-existing-amqp-message-queue/specify-headers.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/amqp-consumer/options-amqp-consumer/use-an-existing-amqp-message-queue/specify-headers.md

# Specify Headers

When using **Headers** as the **Exchange type**, specify the *Name* and *Value* associated with the appropriate headers in the **Headers** table. Only string values are accepted.

![Headers table](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-ec6658c4920f7bca39edf165245ef608d10dc7a8%2FPDI_TransStep_AMQP-Consumer_Headers_Table.png?alt=media)

There are two options for specifying headers:

* **Match all headers**

  For a message to be delivered to the AMQP Consumer step's queue, the producer message must contain all the header key/value pairs in the AMQP Consumer step.

  Be aware that the producer may have more headers than specified in the AMQP Consumer step. Producer headers must match all the specified consumer headers; however, not all the specified consumer headers must match all producer headers.
* **Match any header**

  For a message to be delivered to the AMQP Consumer step's queue, at least one header key/value pair must match on both the AMQP Consumer step and the producer.

Once you specify the headers configuration for the AMQP Consumer step and run the transformation, this permanently binds the headers and the consumer configuration to the specified queue. Even if you subsequently remove the headers from this table, the binding will persist in the AMQP broker. For more information on how to verify the queue's bindings, see: [https://www.rabbitmq/rabbitmqctl.8.html#list\_bindings.](https://www.rabbitmq/rabbitmqctl.8.html#list_bindings)
