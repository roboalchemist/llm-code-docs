# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/data/util/ModelPersistencyManager.md

# [ModelPersistencyManager](https://bryntum.com/docs/gantt/api/Scheduler/data/util/ModelPersistencyManager)

This class manages model persistency, it listens to model stores' beforesync event and removes all non persistable records from sync operation. The logic has meaning only for CRUD-less sync operations.
