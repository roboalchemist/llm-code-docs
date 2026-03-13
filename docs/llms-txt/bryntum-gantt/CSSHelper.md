# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/CSSHelper.md

# [CSSHelper](https://bryntum.com/docs/gantt/api/Core/helper/CSSHelper)

Provides methods to add and manipulate CSS style rules.

Note that this class is incompatible with [CSP](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)

```
this.criticalRule = CSSHelper.insertRule(`#${this.id} .b-sch-event.critical {background-color:${this.criticalColor}}`);
```

## Functions

Functions are methods available for calling on the class

[insertRule](https://bryntum.com/docs/gantt/api/Core/helper/CSSHelper#function-insertRule-static)
Inserts a CSS style rule based upon the passed text

[findRule](https://bryntum.com/docs/gantt/api/Core/helper/CSSHelper#function-findRule-static)
Looks up the first rule which matched the passed selector.

[getCSSVersion](https://bryntum.com/docs/gantt/api/Core/helper/CSSHelper#function-getCSSVersion-static)
Returns current CSS version
