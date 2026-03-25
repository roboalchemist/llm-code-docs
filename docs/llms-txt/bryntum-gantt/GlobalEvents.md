# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/GlobalEvents.md

# [GlobalEvents](https://bryntum.com/docs/gantt/api/Core/GlobalEvents)

A singleton firing global application level events like 'theme'.

```
GlobalEvents.on({
   theme({ theme }) {
       // react to theme changes here
   }
});
```

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[theme](https://bryntum.com/docs/gantt/api/Core/GlobalEvents#event-theme)
Fired after the theme is changed
