# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/ScrollButtons.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/ScrollButtons.md

# [ScrollButtons](https://bryntum.com/docs/gantt/api/Gantt/feature/ScrollButtons)

This feature injects buttons in each row that scrolls the task bar into view. It can optionally show a label along with the button, using the [labelRenderer](https://bryntum.com/docs/gantt/api/#Gantt/feature/ScrollButtons#config-labelRenderer).

```
new Gantt({
    appendTo          : 'container',
    features : {
        scrollButtons : {
            labelRenderer({ taskRecord }) {
                return `${taskRecord.wbsCode} ${StringHelper.encodeHtml(taskRecord.name)}`;
            }
        }
    }
```

This feature is **disabled** by default.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isScrollButtons](https://bryntum.com/docs/gantt/api/Gantt/feature/ScrollButtons#property-isScrollButtons)
Identifies an object as an instance of [ScrollButtons](https://bryntum.com/docs/gantt/api/#Gantt/feature/ScrollButtons) class, or subclass thereof.

[isScrollButtons](https://bryntum.com/docs/gantt/api/Gantt/feature/ScrollButtons#property-isScrollButtons-static)
Identifies an object as an instance of [ScrollButtons](https://bryntum.com/docs/gantt/api/#Gantt/feature/ScrollButtons) class, or subclass thereof.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[scrollButtonClick](https://bryntum.com/docs/gantt/api/Gantt/feature/ScrollButtons#event-scrollButtonClick)
Fires on owner when the scroll button is clicked, return `false` to prevent default scroll behavior
