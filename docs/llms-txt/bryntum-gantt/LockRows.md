# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/LockRows.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/LockRows.md

# [LockRows](https://bryntum.com/docs/gantt/api/Grid/feature/LockRows)

This feature allows records which satisfy a certain condition to be locked at the top of the grid.

By default, the condition is that a certain named field have a truthy value. The field which decides this status defaults to `'fixed'`, but that is configurable using the [fieldName](https://bryntum.com/docs/gantt/api/#Grid/feature/LockRows#config-fieldName) property.

When used with [fieldName](https://bryntum.com/docs/gantt/api/#Grid/feature/LockRows#config-fieldName), the [CellMenu](https://bryntum.com/docs/gantt/api/#Grid/feature/CellMenu) context menu appears with an extra option to toggle the value of that field in the contextual record.

For more granular control, use the [filterFn](https://bryntum.com/docs/gantt/api/#Grid/feature/LockRows#config-filterFn) to decide which records should be locked.

Please note that this feature will not work with the [Split](https://bryntum.com/docs/gantt/api/#Grid/feature/Split) feature.

This feature will not work properly when Store uses [lazyLoad](https://bryntum.com/docs/gantt/api/#Core/data/Store#config-lazyLoad)

* Caveats
    -------

This features utilizes the [Split](https://bryntum.com/docs/gantt/api/#Grid/feature/Split) feature behinds the scenes to create a split view of the grid. Each part of the view is a separate grid instance, which means that certain operations are limited to one part of the grid at the time - for example drag selection and shift + click selection.

The top view (locked rows) is the original grid instance, and the bottom view is a clone of the original grid instance. During locking, both views use stores chained of the original store to filter out the records that should be locked or not.

To access the original store, use the [originalStore](https://bryntum.com/docs/gantt/api/#Grid/feature/LockRows#property-originalStore) property of the grid instance.

When using [RowCopyPaste](https://bryntum.com/docs/gantt/api/#Grid/feature/RowCopyPaste), cutting and pasting among locked rows is not allowed. The results of those actions would be confusing, since for example cutting a locked row and pasting it among the normal rows would return it to the locked rows again.

Additionally, these features are currently not supported while using LockRows:

* Summary feature
* RowReorder feature: Rows cannot be dragged between different sections
* PdfExport feature
* Export to Excel
* Tree

This feature is **disabled** by default.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[fieldName](https://bryntum.com/docs/gantt/api/Grid/feature/LockRows#config-fieldName)
The field name whose truthy/falsy state decides whether a record is locked at the top of the grid.

Is overridden if a [filterFn](https://bryntum.com/docs/gantt/api/#Grid/feature/LockRows#config-filterFn) is provided.

[filterFn](https://bryntum.com/docs/gantt/api/Grid/feature/LockRows#config-filterFn)
A function, or the name of a function in the Grid's ownership hierarchy, that decides whether a record is locked at the top of the grid.

If a function is provided, it will be called with this feature as its `this` reference.

Overrides the [fieldName](https://bryntum.com/docs/gantt/api/#Grid/feature/LockRows#config-fieldName) property.

[bottomGridConfig](https://bryntum.com/docs/gantt/api/Grid/feature/LockRows#config-bottomGridConfig)
An object containing grid configuration for the bottom grid instance.

Configuring the bottom grid instance:

```
new Grid({
    features : {
       lockRows : {
           bottomGridConfig : {
               hideHeaders : false,
               features : {
                   filterBar : true
               }
           }
       }
   }
});
```

```
const App = props => {
    const lockRowsFeature : {
        bottomGridConfig : {
            hideHeaders : false,
            features : {
                filterBar : true
            }
        }
    }

    return <bryntum-grid lockRowsFeature={lockRowsFeature} />
}
```

```
<bryntum-grid :lock-rows-feature="lockRowsFeature" />
```

```
export default {
    setup() {
        return {
            lockRowsFeature : {
                 bottomGridConfig : {
                     hideHeaders : false,
                     features : {
                         filterBar : true
                     }
                 }
             }
        };
    }
}
```

```
<bryntum-grid [lockRowsFeature]="lockRowsFeature"></bryntum-grid>
```

```
export class AppComponent {
     lockRowsFeature : {
         bottomGridConfig : {
             hideHeaders : false,
             features : {
                 filterBar : true
             }
         }
     }
 }
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isLockRows](https://bryntum.com/docs/gantt/api/Grid/feature/LockRows#property-isLockRows)
Identifies an object as an instance of [LockRows](https://bryntum.com/docs/gantt/api/#Grid/feature/LockRows) class, or subclass thereof.

[isLockRows](https://bryntum.com/docs/gantt/api/Grid/feature/LockRows#property-isLockRows-static)
Identifies an object as an instance of [LockRows](https://bryntum.com/docs/gantt/api/#Grid/feature/LockRows) class, or subclass thereof.

[originalStore](https://bryntum.com/docs/gantt/api/Grid/feature/LockRows#property-originalStore)
Locking rows leads to two chained stores that holds a subset of the records, one for the locked records and one for the rest. This property holds the original store, if you need to access it.

```
// With 100 rows, 5 of which are locked
console.log(grid.store.count); // 5
console.log(grid.originalStore.count); // 100
```

## Functions

Functions are methods available for calling on the class

[lockRows](https://bryntum.com/docs/gantt/api/Grid/feature/LockRows#function-lockRows)
Enables row locking by splitting the grid into two synchronized views and filtering records into a top `locked` section and a bottom `unlocked` section.

Provide either [fieldName](https://bryntum.com/docs/gantt/api/#Grid/feature/LockRows#config-fieldName) or [filterFn](https://bryntum.com/docs/gantt/api/#Grid/feature/LockRows#config-filterFn) (or both) via the `options` object. If both are provided, `filterFn` takes precedence.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[lockRows](https://bryntum.com/docs/gantt/api/Grid/feature/LockRows#event-lockRows)
Fires when row locking is enabled.

[unlockRows](https://bryntum.com/docs/gantt/api/Grid/feature/LockRows#event-unlockRows)
Fires when row locking is disabled.
