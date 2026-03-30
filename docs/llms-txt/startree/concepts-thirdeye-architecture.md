# Source: https://docs.startree.ai/thirdeye/concepts-thirdeye-components/concepts-thirdeye-architecture.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# ThirdEye Architecture

**High level system architecture of ThirdEye**

<p>
  <img src="https://mintcdn.com/startree/DzRCNOlJNN6ss-9j/img/thirdeye/ThirdEyeArchitecture.png?fit=max&auto=format&n=DzRCNOlJNN6ss-9j&q=85&s=42128c9a9e73f3111c69998cd925154e" alt="architecture" width="80%" data-path="img/thirdeye/ThirdEyeArchitecture.png" />

  ThirdEye Architecture
</p>

<img src="https://mintcdn.com/startree/DzRCNOlJNN6ss-9j/img/thirdeye/_architecture.png?fit=max&auto=format&n=DzRCNOlJNN6ss-9j&q=85&s=85f5eae65595ecfba6cb480993e46cbe" alt="Building blocks" width="2005" height="897" data-path="img/thirdeye/_architecture.png" />

### UI

This is the service that serves the web interface. It communicates with the backend.

### Coordinator

The **Coordinator** is the entry point of the REST API. The request are (optionally) authenticated and authorized. The coordinator can perform CRUD operations on ThirdEye entities,
simulate detection pipeline, and run interactive RCA.

### Scheduler

The **Scheduler** runs the task crons and create the task objects. The tasks are persisted in the database and polled by the workers. The 2 main type of tasks are detection tasks and notification tasks.

### Worker

**Workers** run the tasks. Here is the execution principle:

* workers wait for tasks to be added to the queue
* once a worker finds a new task, it assigns it to itself (gets a lock)
* on successfully getting a lock, the worker executes the task
* upon completion, the worker captures the results and persists them into the db

## Notes

UI, coordinator, and worker can be scaled independently based on their respective load. The scheduler is not replicated.

Built with [Mintlify](https://mintlify.com).
