# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/WalkHelper.md

# [WalkHelper](https://bryntum.com/docs/gantt/api/Core/helper/WalkHelper)

Tree walking helper

## Functions

Functions are methods available for calling on the class

[preWalk](https://bryntum.com/docs/gantt/api/Core/helper/WalkHelper#function-preWalk-static)
Pre-walks any hierarchical data structure

[walkWhile](https://bryntum.com/docs/gantt/api/Core/helper/WalkHelper#function-walkWhile-static)
Pre-walks any hierarchical data structure while the passed `fn` returns true

[preWalkWithParent](https://bryntum.com/docs/gantt/api/Core/helper/WalkHelper#function-preWalkWithParent-static)
Pre-walks any hierarchical data structure, passing along a link to the parent node

[preWalkUnordered](https://bryntum.com/docs/gantt/api/Core/helper/WalkHelper#function-preWalkUnordered-static)
Pre-walk unordered.

Like [preWalk](https://bryntum.com/docs/gantt/api/#Core/helper/WalkHelper#function-preWalk-static) but doesn't reverse children before walk, thus children will be walked last child first - first child last

[postWalk](https://bryntum.com/docs/gantt/api/Core/helper/WalkHelper#function-postWalk-static)
Post-walks any hierarchical data structure

[prePostWalk](https://bryntum.com/docs/gantt/api/Core/helper/WalkHelper#function-prePostWalk-static)
Pre-/Post-walks any hierarchical data structure calling inFn each node when it walks in, and outFn when it walks out.
