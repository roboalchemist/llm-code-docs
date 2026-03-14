# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/DependencyMenu.md

# [DependencyMenu](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyMenu)

Displays a context menu when right-clicking dependency lines. Items are populated by other features and/or application code.

### Default dependency menu items

Here is the list of menu items provided by the feature and populated by the other features:

Reference

Text

Weight

Feature

Description

`edit`

Edit

100

[DependencyEdit](https://bryntum.com/docs/gantt/api/#Scheduler/feature/DependencyEdit)

Edit in the dependency editor. Hidden when read-only

`delete`

Delete

500

_This feature_

Remove dependency. Hidden when read-only

### Customizing the menu items

The menu items in the dependency menu can be customized, existing items can be changed or removed, and new items can be added. This is handled using the `items` config of the feature.

Add extra items for all dependencies:

```
const scheduler = new Scheduler({
    features : {
        dependencyMenu : {
            items : {
                extraItem : {
                    text : 'Extra',
                    icon : 'fa fa-fw fa-flag',
                    onItem({ dependencyRecord }) {
                        dependencyRecord.critical = true;
                    }
                }
            }
        }
    }
});
```

Remove existing items:

```
const scheduler = new Scheduler({
    features : {
        dependencyMenu : {
            items : {
                delete : false
            }
        }
    }
});
```

Customize existing item:

```
const scheduler = new Scheduler({
    features : {
        dependencyMenu : {
            items : {
                delete : {
                    text : 'Delete link'
                }
            },
            // Process items before menu is shown
            processItems({ dependencyRecord, items}) {
                 // Push an extra item
                 if (dependencyRecord.isCritical === 'conference') {
                     items.markAsCriticalItem = {
                         text : 'Mark as critical',
                         onItem({ dependencyRecord }) {
                             // Do cool things
                         }
                     };
                 }

                 // Do not show menu for secret links
                 if (dependencyRecord.isSecret === 'secret') {
                     return false;
                 }
            }
        }
    }
});
```

The `processItems` implementation may be an `async` function which `awaits` a result to mutate the `items` object.

Note that the [menuContext](https://bryntum.com/docs/gantt/api/#Scheduler/feature/DependencyMenu#property-menuContext) is applied to the Menu's `item` event, so your `onItem` handler's single event parameter also contains the following properties:

* **source** The [Scheduler](https://bryntum.com/docs/gantt/api/#Scheduler/view/Scheduler) whose UI was right-clicked.
* **targetElement** The element right-clicked on.
* **dependencyRecord** The [dependency record](https://bryntum.com/docs/gantt/api/#Scheduler/model/DependencyModel) clicked on.

This feature is **enabled** by default from version 7.0

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[processItems](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyMenu#config-processItems)
A function called before displaying the menu that allows manipulations of its items. Returning `false` from this function prevents the menu being shown.

```
features         : {
   dependencyMenu : {
        processItems({ items, dependencyRecord }) {
            // Add or hide existing items here as needed
            items.myAction = {
                text   : 'Cool action',
                icon   : 'fa fa-fw fa-ban',
                onItem : () => console.log(`Clicked ${dependencyRecord.name}`),
                weight : 1000 // Move to end
            };

           if (!dependencyRecord.allowDelete) {
                items.delete.hidden = true;
            }
        }
    }
},
```

[items](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyMenu#config-items)
This is a preconfigured set of items used to create the default context menu. The default options are listed at the top of the page.

To remove existing items, set corresponding keys `null`:

```
const scheduler = new Scheduler({
    features : {
        dependencyMenu : {
            items : {
                delete   : null
            }
        }
    }
});
```

See the feature config in the above example for details.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDependencyMenu](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyMenu#property-isDependencyMenu)
Identifies an object as an instance of [DependencyMenu](https://bryntum.com/docs/gantt/api/#Scheduler/feature/DependencyMenu) class, or subclass thereof.

[isDependencyMenu](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyMenu#property-isDependencyMenu-static)
Identifies an object as an instance of [DependencyMenu](https://bryntum.com/docs/gantt/api/#Scheduler/feature/DependencyMenu) class, or subclass thereof.

[menuContext](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyMenu#property-menuContext)
An informational object containing contextual information about the last activation of the context menu.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[dependencyMenuBeforeShow](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyMenu#event-dependencyMenuBeforeShow)
This event fires on the owning Scheduler before the context menu is shown for a dependency. Allows manipulation of the items to show in the same way as in `processItems`. Returning `false` from a listener prevents the menu from being shown.

[dependencyMenuItem](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyMenu#event-dependencyMenuItem)
This event fires on the owning Scheduler when an item is selected in the context menu.

[dependencyMenuShow](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyMenu#event-dependencyMenuShow)
This event fires on the owning Scheduler after showing the context menu for an event

## Typedefs

Typedefs are type definitions for the class

[DependencyMenuContext](https://bryntum.com/docs/gantt/api/Scheduler/feature/DependencyMenu#typedef-DependencyMenuContext)
A context object passed to any `processItems` method defined for a context menu feature, and the basis of events fired by context menu features.
