# Internals: The worker {#internals-worker}

::: {.contents local=""}
:::

## Introduction

The worker consists of 4 main components: the consumer, the scheduler,
the mediator and the task pool. All these components runs in parallel
working with two data structures: the ready queue and the ETA schedule.

## Data structures

### timer

The timer uses `heapq`{.interpreted-text role="mod"} to schedule
internal functions. It\'s very efficient and can handle hundred of
thousands of entries.

## Components

### Consumer

Receives messages from the broker using `Kombu`{.interpreted-text
role="pypi"}.

When a message is received it\'s converted into a
`celery.worker.request.Request`{.interpreted-text role="class"} object.

Tasks with an ETA, or rate-limit are entered into the
[timer]{.title-ref}, messages that can be immediately processed are sent
to the execution pool.

ETA and rate-limit when used together will result in the rate limit
being observed with the task being scheduled after the ETA.

### Timer

The timer schedules internal functions, like cleanup and internal
monitoring, but also it schedules ETA tasks and rate limited tasks. If
the scheduled tasks ETA has passed it is moved to the execution pool.

### TaskPool

This is a slightly modified `multiprocessing.Pool`{.interpreted-text
role="class"}. It mostly works the same way, except it makes sure all of
the workers are running at all times. If a worker is missing, it
replaces it with a new one.
