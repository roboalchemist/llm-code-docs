# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/model/mixin/ProjectRevisionHandlerMixin.md

# [ProjectRevisionHandlerMixin](https://bryntum.com/docs/gantt/api/SchedulerPro/model/mixin/ProjectRevisionHandlerMixin)

This mixin allows applying revisions to the local project.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isProjectRevisionHandlerMixin](https://bryntum.com/docs/gantt/api/SchedulerPro/model/mixin/ProjectRevisionHandlerMixin#property-isProjectRevisionHandlerMixin)
Identifies an object as an instance of [ProjectRevisionHandlerMixin](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/mixin/ProjectRevisionHandlerMixin) class, or subclass thereof.

[isProjectRevisionHandlerMixin](https://bryntum.com/docs/gantt/api/SchedulerPro/model/mixin/ProjectRevisionHandlerMixin#property-isProjectRevisionHandlerMixin-static)
Identifies an object as an instance of [ProjectRevisionHandlerMixin](https://bryntum.com/docs/gantt/api/#SchedulerPro/model/mixin/ProjectRevisionHandlerMixin) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[queue](https://bryntum.com/docs/gantt/api/SchedulerPro/model/mixin/ProjectRevisionHandlerMixin#function-queue)
Use this method to organize project changes into transactions. Every queue call will create a sequential promise which cannot be interrupted by other queued functions. You can use async functions and await for any promises (including commitAsync) with one exception - you cannot await other queued calls and any other function/promise which awaits queued function. Otherwise, an unresolvable chain of promises will be created.

**NOTE**: Functions which call this method internally are marked with `on-queue` tag.

Examples:

```
// Invalid queue call which hangs promise chain
project.queue(async () => {
    const event = project.getEventStore().getById(1);
    await project.queue(() => {
        event.duration = 2;
        return project.commitAsync();
    })
})

// Valid queue call
project.queue(() => {
    const event = project.getEventStore().getById(1);

    // Consequent queue call will be chained after the current function in the next microtask.
    project.queue(() => {
        event.duration = 2;
        return project.commitAsync();
    })

    // Event duration is not yet changed - this condition is true
    if (event.duration !== 2) { }
})
```

[initRevisions](https://bryntum.com/docs/gantt/api/SchedulerPro/model/mixin/ProjectRevisionHandlerMixin#function-initRevisions)
Initializes revision feature on the project. Calling this API early is required for revisions to work.

[applyRevisions](https://bryntum.com/docs/gantt/api/SchedulerPro/model/mixin/ProjectRevisionHandlerMixin#function-applyRevisions)
Applies an array of revisions to a local project

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[revisionNotification](https://bryntum.com/docs/gantt/api/SchedulerPro/model/mixin/ProjectRevisionHandlerMixin#event-revisionNotification)
This event triggers when a new revision is added to the project. It is used to notify the backend about the new revision.

## Typedefs

Typedefs are type definitions for the class

[RevisionInfo](https://bryntum.com/docs/gantt/api/SchedulerPro/model/mixin/ProjectRevisionHandlerMixin#typedef-RevisionInfo)
