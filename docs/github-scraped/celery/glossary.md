# Glossary

::: {.glossary sorted=""}

acknowledged

:   Workers acknowledge messages to signify that a message has been
    handled. Failing to acknowledge a message will cause the message to
    be redelivered. Exactly when a transaction is considered a failure
    varies by transport. In AMQP the transaction fails when the
    connection/channel is closed (or lost), but in Redis/SQS the
    transaction times out after a configurable amount of time (the
    `visibility_timeout`).

ack

:   Short for `acknowledged`{.interpreted-text role="term"}.

early acknowledgment

:   Task is `acknowledged`{.interpreted-text role="term"} just-in-time
    before being executed, meaning the task won\'t be redelivered to
    another worker if the machine loses power, or the worker instance is
    abruptly killed, mid-execution.

    Configured using `task_acks_late`{.interpreted-text role="setting"}.

late acknowledgment

:   Task is `acknowledged`{.interpreted-text role="term"} after
    execution (both if successful, or if the task is raising an error),
    which means the task will be redelivered to another worker in the
    event of the machine losing power, or the worker instance being
    killed mid-execution.

    Configured using `task_acks_late`{.interpreted-text role="setting"}.

early ack

:   Short for `early acknowledgment`{.interpreted-text role="term"}

late ack

:   Short for `late acknowledgment`{.interpreted-text role="term"}

ETA

:   \"Estimated Time of Arrival\", in Celery and Google Task Queue,
    etc., used as the term for a delayed message that should not be
    processed until the specified ETA time. See
    `calling-eta`{.interpreted-text role="ref"}.

request

:   Task messages are converted to *requests* within the worker. The
    request information is also available as the task\'s
    `context`{.interpreted-text role="term"} (the `task.request`
    attribute).

calling

:   Sends a task message so that the task function is
    `executed <executing>`{.interpreted-text role="term"} by a worker.

kombu

:   Python messaging library used by Celery to send and receive
    messages.

billiard

:   Fork of the Python multiprocessing library containing improvements
    required by Celery.

executing

:   Workers *execute* task `requests <request>`{.interpreted-text
    role="term"}.

apply

:   Originally a synonym to `call <calling>`{.interpreted-text
    role="term"} but used to signify that a function is executed by the
    current process.

context

:   The context of a task contains information like the id of the task,
    it\'s arguments and what queue it was delivered to. It can be
    accessed as the tasks `request` attribute. See
    `task-request-info`{.interpreted-text role="ref"}

idempotent

:   Idempotence is a mathematical property that describes a function
    that can be called multiple times without changing the result.
    Practically it means that a function can be repeated many times
    without unintended effects, but not necessarily side-effect free in
    the pure sense (compare to `nullipotent`{.interpreted-text
    role="term"}).

    Further reading: <https://en.wikipedia.org/wiki/Idempotent>

nullipotent

:   describes a function that\'ll have the same effect, and give the
    same result, even if called zero or multiple times (side-effect
    free). A stronger version of `idempotent`{.interpreted-text
    role="term"}.

reentrant

:   describes a function that can be interrupted in the middle of
    execution (e.g., by hardware interrupt or signal), and then safely
    called again later. Reentrancy isn\'t the same as
    `idempotence <idempotent>`{.interpreted-text role="term"} as the
    return value doesn\'t have to be the same given the same inputs, and
    a reentrant function may have side effects as long as it can be
    interrupted; An idempotent function is always reentrant, but the
    reverse may not be true.

cipater

:   Celery release 3.1 named after song by Autechre
    (<http://www.youtube.com/watch?v=OHsaqUr_33Y>)

prefetch multiplier

:   The `prefetch count`{.interpreted-text role="term"} is configured by
    using the `worker_prefetch_multiplier`{.interpreted-text
    role="setting"} setting, which is multiplied by the number of pool
    slots (threads/processes/greenthreads).

[prefetch count]{.title-ref}

:   Maximum number of unacknowledged messages a consumer can hold and if
    exceeded the transport shouldn\'t deliver any more messages to that
    consumer. See `optimizing-prefetch-limit`{.interpreted-text
    role="ref"}.

pidbox

:   A process mailbox, used to implement remote control commands.
:::
