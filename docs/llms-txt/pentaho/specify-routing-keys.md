# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/amqp-consumer/options-amqp-consumer/use-an-existing-amqp-message-queue/specify-routing-keys.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/amqp-consumer/options-amqp-consumer/use-an-existing-amqp-message-queue/specify-routing-keys.md

# Specify Routing Keys

When using either **DIRECT** or **TOPIC** as the **Exchange type**, specify the appropriate routing key (or multiple keys) in the **Routing Keys** table. Routing keys are input as string names.

![Routing Keys table in Setup tab of AMQP Consumer](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-6d6f55601c76ea300a49719fd26a0ec6e92b685e%2FPDI_TransStep_AMQP-Consumer_Routing-Keys_Table.png?alt=media)

**Note:** If you select **DIRECT** as the **Exchange type**, and leave the **Exchange Name** blank, the queue name you specified in the **Queue name** option is used as the routing key, regardless of whether you specify any routing keys in the table.

Once you specify the routing key configuration for the Consumer step and run the transformation, this permanently binds the routing keys and the Consumer configuration to the specified queue. Even if you subsequently remove the routing keys from this routing key table, the binding will persist in the AMQP broker. For more information on how to verify the queue's bindings, see: <https://www.rabbitmq/rabbitmqctl.8.html#list_bindings>
