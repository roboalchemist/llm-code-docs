# Source: https://docs.startree.ai/thirdeye/worker-scaling.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Scaling Workers

ThirdEye is comprised of three components:

1. Coordinator
2. Scheduler
3. Worker

The coordinator receives REST API requests, can perform CRUD operations on ThirdEye entities, simulate detection pipeline, and run interactive root cause analysis (RCA).

The scheduler runs cron tasks and creates task objects.

The worker is responsible for doing the heavy lifting of running different kinds of tasks.

As we introduce more and more alerts, the task count grows proportionally. ThirdEye provides the flexibility to scale the workers horizontally as well as vertically to support the growing tasks.

## Vertical Scaling

The ThirdEye worker has an internal thread pool which it uses to run the tasks in parallel. We can
control the parallelism with the help of `maxParallelTasks` configuration.

### When to do this?

This should be configured based on the frequent load expected on the worker, for example if there
are 10 alerts which have detection scheduled for every minute then it makes sense to have 10 tasks
run in parallel.

### Configuration

For helm installation:

```yaml  theme={null}
...
worker:
  config:
    maxParallelTasks: 10    # default is 5
```

*values.yaml*

For bare metal installation:

```yaml  theme={null}
...
taskDriver:
  maxParallelTasks: 10
```

*server.yaml*

## Horizontal Scaling

ThirdEye workers are scaled by replicating them.

### When to do this?

This is a more flexible scaling as it allows us to scale up/down the number of workers based on sudden temporary changes in task rates, for example, if there are 5 alerts that run detection after every minute, but we also have another 10 alerts which just trigger once a day at 2 am, in this case it makes sense to spin up another worker before 2 am and take it down once the tasks are served.

<Note>
  HorizontalPodAutoscaler (HPA) is not yet supported in official ThirdEye Helm charts as the trigger to scale can vary based on the use case.
</Note>

### Configuration

For Helm installation, provide the number of replicas needed.

```yaml  theme={null}
...
worker:
  replicas: 2
  ...
  config:
    randomWorkerIdEnabled: true
```

*values.yaml*

For bare metal installation, run multiple workers on different ports.

```yaml  theme={null}
...
taskDriver:
  enabled: true
  randomWorkerIdEnabled: true
```

*server.yaml*

## FAQs

<AccordionGroup>
  <Accordion title="What is the max number of parallel tasks can be run in case of vertical scaling?">
    Each thread will require cpu time and heap memory so long-running and high memory demanding tasks will prefer less parallel threads while quick running and low memory demanding tasks can afford to have more parallelism. The default is 5.
  </Accordion>

  <Accordion title="What is the max number of workers one can set in case of horizontal scaling?">
    There is no limit as such from the ThirdEye side, but basically it will be (resources available)/(resources required per worker).
  </Accordion>

  <Accordion title="How about consistency and reliability? In which case (vertical or horizontal scaling) does ThirdEye perform well?">
    This is a scenario-based behavior as to which scaling suits best. Neither of the two methods will put ThirdEye in inconsistent state. As for reliability, as long as enough resources are available for a given setup, the system won't be affected by scaling.
  </Accordion>
</AccordionGroup>

Built with [Mintlify](https://mintlify.com).
