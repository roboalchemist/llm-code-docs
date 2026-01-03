::: currentmodule
celery.app.amqp
:::

::: automodule
celery.app.amqp

::: {.contents local=""}
:::

# AMQP

::: autoclass
AMQP

::: attribute
Connection

Broker connection class used. Default is
`kombu.Connection`{.interpreted-text role="class"}.
:::

::: attribute
Consumer

Base Consumer class used. Default is `kombu.Consumer`{.interpreted-text
role="class"}.
:::

::: attribute
Producer

Base Producer class used. Default is `kombu.Producer`{.interpreted-text
role="class"}.
:::

::: attribute
queues

All currently defined task queues (a `Queues`{.interpreted-text
role="class"} instance).
:::

::: attribute
argsrepr_maxsize

Max size of positional argument representation used for logging
purposes. Default is 1024.
:::

::: attribute
kwargsrepr_maxsize

Max size of keyword argument representation used for logging purposes.
Default is 1024.
:::

::: automethod
Queues
:::

::: automethod
Router
:::

::: automethod
flush_routes
:::

::: autoattribute
create_task_message
:::

::: autoattribute
send_task_message
:::

::: autoattribute
default_queue
:::

::: autoattribute
default_exchange
:::

::: autoattribute
producer_pool
:::

::: autoattribute
router
:::

::: autoattribute
routes
:::
:::

# Queues

::: {.autoclass members="" undoc-members=""}
Queues
:::
:::
