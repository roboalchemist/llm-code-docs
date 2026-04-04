# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/override/salesforce/DomHelperOverrideGetCommonAncestor.md

# [DomHelperOverrideGetCommonAncestor](https://bryntum.com/docs/gantt/api/Core/override/salesforce/DomHelperOverrideGetCommonAncestor)

In some cases root LWC element might report that it doesn't contain own children:

```
to.parentElement....parentElement === from // true
from.contains(to) // false
```

At the same time shadow root reports it correctly:

```
from.parentElement.contains(to) // true
```

It means that method goes one level too high and we need to take first child of the shadow root.
