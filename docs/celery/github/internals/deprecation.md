# Celery Deprecation Time-line {#deprecation-timeline}

::: {.contents local=""}
:::

## Removals for version 5.0 {#deprecations-v5.0}

### Old Task API

#### Compat Task Modules {#deprecate-compat-task-modules}

-   Module `celery.decorators` will be removed:

    > This means you need to change:
    >
    > ``` python
    > from celery.decorators import task
    > ```
    >
    > Into:
    >
    > ``` python
    > from celery import task
    > ```

-   Module `celery.task` will be removed

    > This means you should change:
    >
    > ``` python
    > from celery.task import task
    > ```
    >
    > into:
    >
    > ``` python
    > from celery import shared_task
    > ```
    >
    > \-- and:
    >
    > ``` python
    > from celery import task
    > ```
    >
    > into:
    >
    > ``` python
    > from celery import shared_task
    > ```
    >
    > \-- and:
    >
    > ``` python
    > from celery.task import Task
    > ```
    >
    > into:
    >
    > ``` python
    > from celery import Task
    > ```

Note that the new `~celery.Task`{.interpreted-text role="class"} class
no longer uses `classmethod`{.interpreted-text role="func"} for these
methods:

> -   delay
> -   apply_async
> -   retry
> -   apply
> -   AsyncResult
> -   subtask

This also means that you can\'t call these methods directly on the
class, but have to instantiate the task first:

``` pycon
>>> MyTask.delay()          # NO LONGER WORKS


>>> MyTask().delay()        # WORKS!
```

### Task attributes

The task attributes:

-   `queue`
-   `exchange`
-   `exchange_type`
-   `routing_key`
-   `delivery_mode`
-   `priority`

is deprecated and must be set by `task_routes`{.interpreted-text
role="setting"} instead.

### Modules to Remove

-   `celery.execute`

    This module only contains `send_task`: this must be replaced with
    `@send_task`{.interpreted-text role="attr"} instead.

-   `celery.decorators`

    > See `deprecate-compat-task-modules`{.interpreted-text role="ref"}

-   `celery.log`

    > Use `@log`{.interpreted-text role="attr"} instead.

-   `celery.messaging`

    > Use `@amqp`{.interpreted-text role="attr"} instead.

-   `celery.registry`

    > Use `celery.app.registry`{.interpreted-text role="mod"} instead.

-   `celery.task.control`

    > Use `@control`{.interpreted-text role="attr"} instead.

-   `celery.task.schedules`

    > Use `celery.schedules`{.interpreted-text role="mod"} instead.

-   `celery.task.chords`

    > Use `celery.chord`{.interpreted-text role="func"} instead.

### Settings

#### `BROKER` Settings

  **Setting name**    **Replace with**
  ------------------- ------------------------------------------------
  `BROKER_HOST`       `broker_url`{.interpreted-text role="setting"}
  `BROKER_PORT`       `broker_url`{.interpreted-text role="setting"}
  `BROKER_USER`       `broker_url`{.interpreted-text role="setting"}
  `BROKER_PASSWORD`   `broker_url`{.interpreted-text role="setting"}
  `BROKER_VHOST`      `broker_url`{.interpreted-text role="setting"}

#### `REDIS` Result Backend Settings

  **Setting name**          **Replace with**
  ------------------------- ----------------------------------------------------
  `CELERY_REDIS_HOST`       `result_backend`{.interpreted-text role="setting"}
  `CELERY_REDIS_PORT`       `result_backend`{.interpreted-text role="setting"}
  `CELERY_REDIS_DB`         `result_backend`{.interpreted-text role="setting"}
  `CELERY_REDIS_PASSWORD`   `result_backend`{.interpreted-text role="setting"}
  `REDIS_HOST`              `result_backend`{.interpreted-text role="setting"}
  `REDIS_PORT`              `result_backend`{.interpreted-text role="setting"}
  `REDIS_DB`                `result_backend`{.interpreted-text role="setting"}
  `REDIS_PASSWORD`          `result_backend`{.interpreted-text role="setting"}

### Task_sent signal

The `task_sent`{.interpreted-text role="signal"} signal will be removed
in version 4.0. Please use the `before_task_publish`{.interpreted-text
role="signal"} and `after_task_publish`{.interpreted-text role="signal"}
signals instead.

### Result

Apply to: `~celery.result.AsyncResult`{.interpreted-text role="class"},
`~celery.result.EagerResult`{.interpreted-text role="class"}:

-   `Result.wait()` -\> `Result.get()`
-   `Result.task_id()` -\> `Result.id`
-   `Result.status` -\> `Result.state`.

#### Settings {#deprecations-v3.1}

  **Setting name**                    **Replace with**
  ----------------------------------- ----------------------------------------------------
  `CELERY_AMQP_TASK_RESULT_EXPIRES`   `result_expires`{.interpreted-text role="setting"}

## Removals for version 2.0 {#deprecations-v2.0}

-   The following settings will be removed:

  **Setting name**                                  **Replace with**
  ------------------------------------------------- ------------------------------------------
  [CELERY_AMQP_CONSUMER_QUEUES]{.title-ref}         [task_queues]{.title-ref}
  [CELERY_AMQP_CONSUMER_QUEUES]{.title-ref}         [task_queues]{.title-ref}
  [CELERY_AMQP_EXCHANGE]{.title-ref}                [task_default_exchange]{.title-ref}
  [CELERY_AMQP_EXCHANGE_TYPE]{.title-ref}           [task_default_exchange_type]{.title-ref}
  [CELERY_AMQP_CONSUMER_ROUTING_KEY]{.title-ref}    [task_queues]{.title-ref}
  [CELERY_AMQP_PUBLISHER_ROUTING_KEY]{.title-ref}   [task_default_routing_key]{.title-ref}

-   `CELERY_LOADER`{.interpreted-text role="envvar"} definitions without
    class name.

    > For example,, [celery.loaders.default]{.title-ref}, needs to
    > include the class name:
    > [celery.loaders.default.Loader]{.title-ref}.

-   

    `TaskSet.run`{.interpreted-text role="meth"}. Use `celery.task.base.TaskSet.apply_async`{.interpreted-text role="meth"}

    :   instead.
