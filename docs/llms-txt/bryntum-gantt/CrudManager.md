# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/data/CrudManager.md

# [CrudManager](https://bryntum.com/docs/gantt/api/Scheduler/data/CrudManager)

The Crud Manager (or "CM") is a class implementing centralized loading and saving of data in multiple stores. Loading the stores and saving all changes is done using two requests (`load` and `sync`). The stores managed by CRUD manager should not be configured with their own CRUD URLs or use [autoLoad](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-autoLoad)/[autoCommit](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-autoCommit).

This class uses JSON as its data encoding format.

Scheduler stores
----------------

The class supports Scheduler specific stores (namely: resource, event, assignment and dependency stores). For these stores, the CM has separate configs (`[resourceStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/CrudManager#config-resourceStore)`, `[eventStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/CrudManager#config-eventStore)`, `[assignmentStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/CrudManager#config-assignmentStore)`) to register them.

```
const crudManager = new CrudManager({
    autoLoad        : true,
    resourceStore   : resourceStore,
    eventStore      : eventStore,
    assignmentStore : assignmentStore,
    transport       : {
        load : {
            url : 'php/read.php'
        },
        sync : {
            url : 'php/save.php'
        }
    }
});
```

### Load response structure

The backend request (`php/read.php`) should return a JSON response:

```
{
  "success": true,
  "events": {
    "rows": [
      {
        "id": "e1",
        "name": "Client meeting",
        "startDate": "2017-01-01",
        "endDate": "2017-01-02",
        "iconCls": "fa fa-calendar"
      },
      {
        "id": "e2",
        "name": "Performance review",
        "startDate": "2017-01-03",
        "endDate": "2017-01-05",
        "iconCls": "fa fa-search"
      }
    ]
  },
  "resources": {
    "rows": [
      {
        "id": "r1",
        "name": "Mike Anderson",
        "category": "Consultants",
        "type": "Full time",
        "image": "mike"
      },
      {
        "id": "r2",
        "name": "Kevin Larson",
        "category": "Consultants",
        "type": "Full time",
        "image": "amit"
      }
    ]
  },
  "assignments": {
    "rows": [
        "resourceId": "r1",
        "eventId": "e1",
    ],
    [
        "resourceId": "r2",
        "eventId": "e1",
    ],
    [
        "resourceId": "r1",
        "eventId": "e2",
    ]
  }
}
```

### Sync request structure

The sync request (`php/save.php`) is a single endpoint for all the operations (create, update, and delete).

The general request structure includes the store that is modified and the operation name (`added`, `deleted`, or `updated`).

```
{
  "type": "sync",
  "requestId": 17156805380431,
  "events": {
    "added": [
      {
        // new event attributes
      },
    ],
    "updated": [
      {
        // updated attributes
      },
    ],
    "removed": [
      {
        // only the ID
      },
    ],
  }
}
```

To update an event in a scheduler, the request should look like:

```
{
  "type": "sync",
  "requestId": 17156805380431,
  "events": {
    "updated": [
      {
        "startDate": "2024-02-19T08:00:00+05:00",
        "endDate": "2024-02-19T09:00:00+05:00",
        "id": 7
      }
    ]
  }
}
```

Similarly, for a resource:

```
{
  "type": "sync",
  "requestId": 17156805528382,
  "resources": {
    "updated": [
      {
        "name": "James Shawn",
        "id": 5
      }
    ]
  }
}
```

This will update the resource name to **James Shawn**.

In case of creating a new event or resource, the request should look like:

```
{
  "type": "sync",
  "requestId": 17156805826393,
  "events": {
    "added": [
      {
        "startDate": "2024-02-19T07:30:00+05:00",
        "endDate": "2024-02-19T08:30:00+05:00",
        "duration": 0.041666666666666664,
        "durationUnit": "day",
        "cls": "",
        "name": "Walk the dog",
        "exceptionDates": [],
        "allDay": false,
        "$PhantomId": "_generatedModelClass_4a742332-6c83-45b4-9557-774f770d11d7"
      }
    ]
  },
  "assignments": {
    "added": [
      {
        "resourceId": 5,
        "eventId": "_generatedModelClass_4a742332-6c83-45b4-9557-774f770d11d7",
        "$PhantomId": "_generatedModelClass_d50b7d11-3550-4d70-9350-ca180e465ed3"
      }
    ]
  }
}
```

The above will create a `Walk the dog` event.

### Sync response structure

In case of `updated` and `removed`, the response only contains `success`:

```
{
    "success": true
}
```

The `added` case is different, where you need to return the `$PhantomId` with the server assigned `id`.

```
{
  "success": true,
  "events": {
    "rows": [
      {
        "$PhantomId": "_generatedModelClass_4a742332-6c83-45b4-9557-774f770d11d7",
        "id": "5a9bf309-ae4a-4bcb-bbc9-f38a94beb2a3"
      }
    ]
  },
  "assignments": {
    "rows": [
      {
        "$PhantomId": "_generatedModelClass_d50b7d11-3550-4d70-9350-ca180e465ed3",
        "id": "ca8f7274-c0af-4069-9ba2-218d71266318"
      }
    ]
  }
}
```

AJAX request configuration
--------------------------

To configure AJAX request parameters please take a look at the [AjaxTransport](https://bryntum.com/docs/gantt/api/#Scheduler/crud/transport/AjaxTransport) docs.

```
const crudManager = new CrudManager({
    autoLoad        : true,
    resourceStore,
    eventStore,
    assignmentStore,
    transport       : {
        load    : {
            url         : 'php/read.php',
            // use GET request
            method      : 'GET',
            // pass request JSON in "rq" parameter
            paramName   : 'rq',
            // extra HTTP request parameters
            params      : {
                foo     : 'bar'
            },
            // pass some extra Fetch API option
            credentials : 'include'
        },
        sync : {
            url : 'php/save.php'
        }
    }
});
```

Using inline data
-----------------

The CrudManager provides settable property [inlineData](https://bryntum.com/docs/gantt/api/#Scheduler/data/CrudManager#property-inlineData) that can be used to get data from all [crudStores](https://bryntum.com/docs/gantt/api/#Scheduler/data/CrudManager#property-crudStores) at once and to set this data as well. Populating the stores this way can be useful if you cannot or you do not want to use CrudManager for server requests but you pull the data by other means and have it ready outside CrudManager. Also, the data from all stores is available in a single assignment statement.

### Getting data

```
const data = scheduler.crudManager.inlineData;

// use the data in your application
```

You can read the inline data by `console.log(scheduler.crudManager.inlineData)`:

```
// the data should look like:
{
    "calendars": [],
    "events": [
        {
            "id": 1,
            "name": "Meeting",
            "startDate": "2020-03-23T07:00:00+05:00",
            "endDate": "2020-03-23T08:00:00+05:00",
            "duration": 3,
            "resourceId": 1
        },
        {
            "id": 2,
            "name": "Business",
            "startDate": "2020-03-23T11:00:00+05:00",
            "startDate": "2020-03-23T11:40:00+05:00",
            "duration": 2,
            "resourceId": 2
        }
    ],
    "resources": [
        {
            "id": 1,
            "parentId": null,
            "name": "George",
            "eventColor": "blue",
        },
        {
            "id": 2,
            "parentId": null,
            "name": "Rob",
            "eventColor": "blue",
        }
    ],
    "dependencies": [
        {
            "id": 1,
            "type": 2,
            "cls": "",
            "lag": 0,
            "lagUnit": "day",
            "fromEvent": 1,
            "toEvent": 2,
            "active": true
        }
    ],
    "timeRanges": [],
    "resourceTimeRanges": []
}
```

The `xxData` properties are deprecated and will be removed in the future. Use `xx` instead. For example `eventsData` is deprecated, use `events` instead. For now, both naming schemes are included in the data object

### Setting data

```
const data = // your function to pull server data

scheduler.crudManager.inlineData = data;
```

It should have the following structure:

```
scheduler.crudManager.inlineData = {
  resources: [
    {
      id   : 1,
      name : 'George',
      type : 'Operators',
    },
    {
      id   : 2,
      name : 'Rob',
      type : 'Operators',
    },
    {
      id   : 3,
      name : 'Mike',
      type : 'Main'
    },
  ],
  events: [
    {
      id           : 1,
      name         : 'Meeting',
      startDate    : '2020-03-23T07:00',
      duration     : 4,
      durationUnit : 'hour',
      percentDone  : 100,
      resourceId   : 1
    },
    {
      id           : 2,
      startDate    : '2020-03-23T11:00',
      name         : 'Get parts',
      durationUnit : 'hour',
      duration     : 3,
      percentDone  : 40,
      resourceId   : 2
    },
  ],
  dependencies: [
    {
      id        : 1,
      fromEvent : 1,
      toEvent   : 2
    },
  ],
};
```

Either you can pass the response in this format directly:

```
{
 resource: [],
 events: [],
 dependencies: [],
}
```

Or you can modify the response once received and assign it to `scheduler.crudManager.inlineData`.

The `xxData` properties are deprecated and will be removed in the future. Use `xx` instead. For example `eventsData` is deprecated, use `events` instead. For now, both naming schemes are included in the data object

Load order
----------

The CM is aware of the proper load order for Scheduler specific stores so you don't need to worry about it. If you provide any extra stores (using [stores](https://bryntum.com/docs/gantt/api/#Scheduler/data/CrudManager#config-stores) config) they will be added to the start of collection before the Scheduler specific stores. If you need a different loading order, you should use [addStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/CrudManager#function-addStore) method to register your store:

```
const crudManager = new CrudManager({
    resourceStore   : resourceStore,
    eventStore      : eventStore,
    assignmentStore : assignmentStore,
    // extra user defined stores will get to the start of collection
    // so they will be loaded first
    stores          : [ store1, store2 ],
    transport       : {
        load : {
            url : 'php/read.php'
        },
        sync : {
            url : 'php/save.php'
        }
    }
});

// append store3 to the end so it will be loaded last
crudManager.addStore(store3);

// now when we registered all the stores let's load them
crudManager.load();
```

Assignment store
----------------

The Crud Manager is designed to use [AssignmentStore](https://bryntum.com/docs/gantt/api/#Scheduler/data/AssignmentStore) for assigning events to one or multiple resources. However if server provides `resourceId` for any of the `events` then the Crud Manager enables backward compatible mode when an event could have a single assignment only. This also disables multiple assignments in Scheduler UI. In order to use multiple assignments server backend should be able to receive/send `assignments` for `load` and `sync` requests.

Project
-------

The Crud Manager automatically consumes stores of the provided project (namely its [eventStore](https://bryntum.com/docs/gantt/api/#Scheduler/model/ProjectModel#property-eventStore), [resourceStore](https://bryntum.com/docs/gantt/api/#Scheduler/model/ProjectModel#property-resourceStore), [assignmentStore](https://bryntum.com/docs/gantt/api/#Scheduler/model/ProjectModel#property-assignmentStore), [dependencyStore](https://bryntum.com/docs/gantt/api/#Scheduler/model/ProjectModel#property-dependencyStore), [timeRangeStore](https://bryntum.com/docs/gantt/api/#Scheduler/model/ProjectModel#property-timeRangeStore) and [resourceTimeRangeStore](https://bryntum.com/docs/gantt/api/#Scheduler/model/ProjectModel#property-resourceTimeRangeStore)):

```
const crudManager = new CrudManager({
    // crud manager will get stores from myAppProject project
    project   : myAppProject,
    transport : {
        load : {
            url : 'php/read.php'
        },
        sync : {
            url : 'php/save.php'
        }
    }
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[resourceStore](https://bryntum.com/docs/gantt/api/Scheduler/data/CrudManager#config-resourceStore)
A store with resources (or a config object).

[eventStore](https://bryntum.com/docs/gantt/api/Scheduler/data/CrudManager#config-eventStore)
A store with events (or a config object).

```
crudManager : {
     eventStore {
         storeClass : MyEventStore
     }
}
```

[assignmentStore](https://bryntum.com/docs/gantt/api/Scheduler/data/CrudManager#config-assignmentStore)
A store with assignments (or a config object).

[dependencyStore](https://bryntum.com/docs/gantt/api/Scheduler/data/CrudManager#config-dependencyStore)
A store with dependencies(or a config object).

[project](https://bryntum.com/docs/gantt/api/Scheduler/data/CrudManager#config-project)
A project that holds and links stores

[resourceTimeRangeStore](https://bryntum.com/docs/gantt/api/Scheduler/data/CrudManager#config-resourceTimeRangeStore)
A store with resource time ranges (or a config object).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isCrudManager](https://bryntum.com/docs/gantt/api/Scheduler/data/CrudManager#property-isCrudManager)
Identifies an object as an instance of [CrudManager](https://bryntum.com/docs/gantt/api/#Scheduler/data/CrudManager) class, or subclass thereof.

[isCrudManager](https://bryntum.com/docs/gantt/api/Scheduler/data/CrudManager#property-isCrudManager-static)
Identifies an object as an instance of [CrudManager](https://bryntum.com/docs/gantt/api/#Scheduler/data/CrudManager) class, or subclass thereof.

[timeRangeStore](https://bryntum.com/docs/gantt/api/Scheduler/data/CrudManager#property-timeRangeStore)
Store for [timeRanges](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TimeRanges) feature.

[resourceTimeRangeStore](https://bryntum.com/docs/gantt/api/Scheduler/data/CrudManager#property-resourceTimeRangeStore)
Store for [resourceTimeRanges](https://bryntum.com/docs/gantt/api/#Scheduler/feature/ResourceTimeRanges) feature.

[resourceStore](https://bryntum.com/docs/gantt/api/Scheduler/data/CrudManager#property-resourceStore)
Get/set the resource store bound to the CRUD manager.

[eventStore](https://bryntum.com/docs/gantt/api/Scheduler/data/CrudManager#property-eventStore)
Get/set the event store bound to the CRUD manager.

[assignmentStore](https://bryntum.com/docs/gantt/api/Scheduler/data/CrudManager#property-assignmentStore)
Get/set the assignment store bound to the CRUD manager.

[dependencyStore](https://bryntum.com/docs/gantt/api/Scheduler/data/CrudManager#property-dependencyStore)
Get/set the dependency store bound to the CRUD manager.
