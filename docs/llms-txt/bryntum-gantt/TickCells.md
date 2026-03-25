# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/TickCells.md

# [TickCells](https://bryntum.com/docs/gantt/api/Scheduler/feature/TickCells)

A feature allowing you to display values in the time axis cell for each row in a scheduler.

This feature is **disabled** by default.

```
const scheduler = new Scheduler({
     features : {
         tickCells : {
             resourceTicksData : [
                 {
                     id           : 1,
                     startDate    : '2024-06-03',
                     value        : 20,
                     resourceId   : 1,
                     durationUnit : 'day',
                     duration     : 1
                 }
             ],
             tickRenderer({ value = 0 }) {
                 const
                     hours = Math.floor(value),
                     hourFraction =  60 * (value - hours);
                 return value ? `${hours}:${String(hourFraction).padStart(2, '0')}` : '';
             }
         }
     }
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[resourceTickStore](https://bryntum.com/docs/gantt/api/Scheduler/feature/TickCells#config-resourceTickStore)
Store that holds resource ticks - instances of [ResourceTickModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceTickModel). A store will be automatically created if none is specified.

[entityName](https://bryntum.com/docs/gantt/api/Scheduler/feature/TickCells#config-entityName)
Used to configure tick entity name

[rangeCls](https://bryntum.com/docs/gantt/api/Scheduler/feature/TickCells#config-rangeCls)
Used to configure tick cell wrapper class

[cls](https://bryntum.com/docs/gantt/api/Scheduler/feature/TickCells#config-cls)
Used to configure tick cell class

[resourceTicksData](https://bryntum.com/docs/gantt/api/Scheduler/feature/TickCells#config-resourceTicksData)
The initial data, to fill the [resourceTickStore](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TickCells#config-resourceTickStore) with. Should be an array of [ResourceTickModel](https://bryntum.com/docs/gantt/api/#Scheduler/model/ResourceTickModel) or configuration objects.

[tickRenderer](https://bryntum.com/docs/gantt/api/Scheduler/feature/TickCells#config-tickRenderer)
Renderer function. Should return textual content or a [DomConfig](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#typedef-DomConfig) object.

```
new Scheduler({
    features : {
        tickCells : {
            tickRenderer : resourceTick => {
                 const
                     hours = Math.floor(resourceTick.value),
                     hourFraction = 60 * (value - hours);
                 return value ? `${hours}:${String(hourFraction).padStart(2, '0')}` : '';
            }
        }
    }
});
```

[showEditor](https://bryntum.com/docs/gantt/api/Scheduler/feature/TickCells#config-showEditor)
Config used to show or not the tick editor on cell double click.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTickCells](https://bryntum.com/docs/gantt/api/Scheduler/feature/TickCells#property-isTickCells)
Identifies an object as an instance of [TickCells](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TickCells) class, or subclass thereof.

[isTickCells](https://bryntum.com/docs/gantt/api/Scheduler/feature/TickCells#property-isTickCells-static)
Identifies an object as an instance of [TickCells](https://bryntum.com/docs/gantt/api/#Scheduler/feature/TickCells) class, or subclass thereof.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[change](https://bryntum.com/docs/gantt/api/Scheduler/feature/TickCells#event-change)
Fired when data store changes.
