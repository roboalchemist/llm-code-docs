# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/DomSync.md

# [DomSync](https://bryntum.com/docs/gantt/api/Core/helper/DomSync)

A utility class for syncing DOM config objects to DOM elements. Syncing compares the new config with the previously used for that element, only applying the difference. Very much like a virtual DOM approach on a per element basis (element + its children).

Usage example:

```
DomSync.sync({
    domConfig: {
        className : 'b-outer',
        children : [
            {
                className : 'b-child',
                html      : 'Child 1',
                dataset   : {
                    custom : true
                }
            },
            {
                className : 'b-child',
                html      : 'Child 2',
                style     : {
                    fontWeight : 'bold',
                    color      : 'blue'
                }
            }
        ]
    },
    targetElement : target
});
```

## Functions

Functions are methods available for calling on the class

[checkEquality](https://bryntum.com/docs/gantt/api/Core/helper/DomSync#function-checkEquality-static)
Compares two DOM configs or properties of such objects for equality.

[sync](https://bryntum.com/docs/gantt/api/Core/helper/DomSync#function-sync-static)
Sync a DOM config to a target element

[addCls](https://bryntum.com/docs/gantt/api/Core/helper/DomSync#function-addCls-static)
Adds CSS classes to the element and to the cache.

[removeCls](https://bryntum.com/docs/gantt/api/Core/helper/DomSync#function-removeCls-static)
Adds CSS classes from the element and from the cache.

[removeChild](https://bryntum.com/docs/gantt/api/Core/helper/DomSync#function-removeChild-static)
Remove a child element without syncing, for example when dragging an element to some other parent. Removes it both from DOM and the parent elements syncMap

[addChild](https://bryntum.com/docs/gantt/api/Core/helper/DomSync#function-addChild-static)
Adds a child element without syncing, making it properly available for later syncs. Useful for example when dragging and dropping an element from some other parent.

[getChild](https://bryntum.com/docs/gantt/api/Core/helper/DomSync#function-getChild-static)
Get a child element using a dot separated syncIdMap path.

```
DomSync.getChild(eventWrap, 'event.percentBar');
```
