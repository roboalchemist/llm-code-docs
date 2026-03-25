# Source: https://bryntum.com/products/gantt/docs-llm/guide/Gantt/integration/nodejs.md

<h1 class="title-with-image"><img src="Core/logo/nodejs.svg" alt="Bryntum Gantt supports Node.js"/>
Using Bryntum Gantt with Node.js</h1>

Bryntum components are designed to work in a browser environment. However there are data level classes that don't need a browser and thus can be used in Node.js.
These primarily consist of the `ProjectModel` class and its associated task, resource, dependency, and calendar models, along with the corresponding stores and other required classes.

The classes are available in two bundles in the
Bryntum Gantt:

* **`gantt.node.cjs`**: The Node.js bundle in CommonJS format
* **`gantt.node.mjs`**: The Node.js bundle in ES modules format

<div class="note">

Node.js bundles are only available for the <strong>licensed version</strong> of Bryntum Gantt.

</div>

These bundles are part of both the [`@bryntum/gantt`](#Gantt/guides/npm-repository.md) npm package and the distribution which you can download from the [Bryntum Customer Zone](https://customerzone.bryntum.com).
<div class="note">

For the distribution, the bundles can be found in the <code>build</code> folder.

</div>

## Importing Node.js bundle classes

If your code uses modern ES modules (and you have installed the [`@bryntum/gantt`](#Gantt/guides/npm-repository.md) package) you can import from the mjs-bundle like this:

```javascript
import { ProjectModel } from '@bryntum/gantt/gantt.node.mjs'; 
new ProjectModel({
    // ProjectModel config
});
```

And if your code uses CommonJS modules you can import the corresponding bundle like this:

```javascript
const { ProjectModel } = require('@bryntum/gantt/gantt.node.cjs'); 
new ProjectModel({
    // ProjectModel config
});
```

## Example use cases

Some examples of what you can do with the Node.js bundle include the following:

* Use the Bryntum Gantt data model types for TypeScript projects.
* Set up live Bryntum Gantt updates using a WebSocket server.
* Use the project's scheduling engine on the server to handle scheduling calculations and conflicts
  from a central location.

## Data model TypeScript types

If you are using TypeScript, you can import the data model types of Bryntum Gantt
[stores](#Gantt/guides/data/project_data.md).
For example, the following code uses an Express.js API endpoint to save a created Bryntum Gantt task to a database:

```typescript
import { TaskModelConfig } from '@bryntum/gantt/gantt.node.mjs';

// ...

app.post('/api/task/create', async(req, res) => {
    // expect incoming data to have TaskModel fields
    const data : TaskModelConfig = req.body;
    const newTask = await Task.create(data);

    res.status(200).json({
        success : true,
        data    : newTask
    });
});
```

A [model](#Core/data/Model) defines a record that can be added to a store. The models for the primary data stores are:
`TaskModel`, `ResourceModel`, `AssignmentModel`, `DependencyModel`, and `CalendarModel`.

## Live updates

Another example of Node.js code running Bryntum Gantt could be
an application where users collaborate on the same project in real-time and use the
[revisions feature](#Gantt/guides/revisions/overview.md) that enables live updates across multiple clients.

In that case all changes are synchronized across different clients through a central server, while each client maintains its own local [ProjectModel](#Gantt/model/ProjectModel) instance.
The server dispatches changes and resolves possible conflicts.

To implement live updates, you need to:

1. **Enable the revisions feature** in your client-side Bryntum Gantt as described in the [Real time - Revisions](#Gantt/guides/revisions/overview.md) guide.
2. **Create a server** that a client-side Bryntum Gantt can connect to, which follows the [Revisions Feature Protocol Implementation](#Gantt/guides/revisions/protocol.md) to coordinate changes between clients.

Take a look at our [Node.js Gantt WebSocket server code](https://github.com/bryntum/gantt-websocket-server/blob/main),
which uses a WebSocket implementation to create a real-time connection with a client-side application. This server can work with our client-side [Bryntum Gantt realtime updates demo](https://bryntum.com/products/gantt/examples/realtime-updates/).

## Handling scheduling calculations and conflicts

The Bryntum Gantt project has a special scheduling engine that automatically calculates task parameters. It is built
on top of [ChronoGraph](https://github.com/bryntum/chronograph), an open-source reactive computational engine developed
by Bryntum. The scheduling engine normalizes dates and durations, handles references between models, and detects
scheduling conflicts.

You can use the [ProjectModel](#Gantt/model/ProjectModel) server-side as a central place for handling scheduling
calculations and conflicts. This can be useful when your project data is updated outside of the Bryntum Gantt UI,
for example, through external APIs.

You can create a project model in Node.js and populate it with data from your database:

```typescript
import { ProjectModel } from '@bryntum/Gantt/Gantt.node.mjs';
import { Dependency, Task } from './models';

export async function buildProjectModel(): Promise<ProjectModel> {
    // fetch data from the database
    const [tasks, dependencies] = await Promise.all([
        Task.findAll(),
        Dependency.findAll()
    ]);

    const project = new ProjectModel({
        tasks,
        dependencies
    });

    return project;
}
```

You can then use the project model in your API endpoints to check for scheduling conflicts, such as in this example
Express.js API endpoint, which saves created Bryntum Gantt tasks to a database:

```typescript
// ...

let project: ProjectModel;

(async() => {
    project = await buildProjectModel();
})();

// ...

app.post('/api/task/create', async(req, res) => {
    const { data } : { data: TaskModelConfig } = req.body;

    try {
        const task   = project.taskStore.add(data)[0];
        // To guarantee data is in a calculated state, wait for calculations to finish:
        const result = await project.commitAsync();

        if (result.rejectedWith) {
            console.error('Scheduling error', result.rejectedWith);
            return res.status(400).json({
                success   : false,
                conflicts : 'There was a scheduling error'
            });
        }

        // save to the database the new task data calculated by the Engine
        const saved = await Task.create(task.toJSON());
        return res.json({ success : true, data : saved });
    }
    catch (e: any) {
        res.status(500).json({ success : false, error : e.message });
    }
});
```

If a scheduling conflict exists, the `Task.create()` method will not save the task to the database.

To connect to this Express.js API from a client-side Bryntum Gantt, you can set the project's `createUrl`:

```typescript
const gantt = new Gantt({
    appendTo : 'gantt-div',
    project  : {
        taskStore : {
            readUrl    : '/api/task/get',
            createUrl  : '/api/task/create',
            autoLoad   : true,
            autoCommit : true
        }
    },
    // ...
```

## Available class imports

There are many imports available for classes and helpers, including:

* [TaskModel](#Gantt/model/TaskModel)
* [TaskStore](#Gantt/data/TaskStore)

* [ProjectModel](#Gantt/model/ProjectModel)
* [DateHelper](#Core/helper/DateHelper)
* [CalendarIntervalModel](#Gantt/model/CalendarIntervalModel)
* [RecurrenceModel](#Scheduler/model/RecurrenceModel)

Refer to the [Bryntum Gantt documentation](https://bryntum.com/products/gantt/docs/) for a full list of the available classes and helpers.
