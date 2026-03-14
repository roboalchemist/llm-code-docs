# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/eventlayout/ProVerticalLayout.md

# [ProVerticalLayout](https://bryntum.com/docs/gantt/api/SchedulerPro/eventlayout/ProVerticalLayout)

Assists with event layout in vertical mode, you can implement a custom layout using the [layoutFn](https://bryntum.com/docs/gantt/api/#SchedulerPro/eventlayout/ProVerticalLayout#config-layoutFn). Example usage:

```
new SchedulerPro({
    mode : 'vertical',
    eventLayout : {
        layoutFn(items, resource, scheduler) {
            items.forEach(item => {
                item.top = Math.round(Math.random() * 100);
                item.height = Math.round(Math.random() * 100);
            });

            return 150; // The resource column width
        }
    }
})
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[type](https://bryntum.com/docs/gantt/api/SchedulerPro/eventlayout/ProVerticalLayout#config-type)
Type of vertical layout. Supported values are `mixed`, `pack` and `none`.

[layoutFn](https://bryntum.com/docs/gantt/api/SchedulerPro/eventlayout/ProVerticalLayout#config-layoutFn)
Supply a function to manually layout events. It accepts event layout data and should set `top` and `height` for every provided data item (left and width are calculated according to the event start date and duration). The function should return the total row height in pixels.

If you need a reference to the SchedulerPro instance, you can get that from the function scope (arrow function doesn't work here):

```
new SchedulerPro({
    mode : 'vertical',
    eventLayout : {
        layoutFn(items, resource, scheduler) {
            items.forEach(item => {
                item.left = Math.round(Math.random() * 100);
                item.width = Math.round(Math.random() * 100);
            });

            return 150;
        }
    }
})
```
