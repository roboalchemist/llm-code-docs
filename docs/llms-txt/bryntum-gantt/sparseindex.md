# Source: https://bryntum.com/products/gantt/docs-llm/guide/Gantt/data/sparseindex.md

# Using sparse indexes

As described in the `Grid` guides, `Store` can use sparse indexes. This means that the store will not update a
continuous index of all records, but instead will only modify the `sparseIndex` property of records that have been moved
in the UI.

In a `Gantt` application, the stores are embedded into a [ProjectModel](#Gantt/model/ProjectModel), and by default not
configured to use `sparseIndex`. To enable this feature, the `useSparseIndex` config must be set to `true` on the store
instance. In most cases, this will be the `taskStore` of the project:

```javascript
const project = new ProjectModel({
    taskStore : {
        useSparseIndex : true
    }
});
```

Utilizing this feature is only meaningful in conjunction with persistent storage, as the sparse index values must be
saved and restored when loading data.

See also [Project data loading and saving](#Gantt/guides/data/project_data.md).

## How it works

See more detailed information in the `Grid` guide:
[Using sparse indexes](#Grid/guides/data/sparseindex.md#how-it-works).
