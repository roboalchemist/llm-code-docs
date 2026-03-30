# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/data/AssignmentsManipulationStore.md

# [AssignmentsManipulationStore](https://bryntum.com/docs/gantt/api/Gantt/data/AssignmentsManipulationStore)

Special store class for _single_ task/event assignments manipulation, used by [AssignmentGrid](https://bryntum.com/docs/gantt/api/#Gantt/widget/AssignmentGrid)

Contains a collection of [AssignmentModel](https://bryntum.com/docs/gantt/api/#Gantt/model/AssignmentModel) records.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[projectEvent](https://bryntum.com/docs/gantt/api/Gantt/data/AssignmentsManipulationStore#config-projectEvent)
Event model to manipulate assignments of, the event should be part of a project.

[floatAssignedResources](https://bryntum.com/docs/gantt/api/Gantt/data/AssignmentsManipulationStore#config-floatAssignedResources)
Flag indicating whether assigned resources should be placed (floated) before unassigned ones.

[liveFloatAssignedResources](https://bryntum.com/docs/gantt/api/Gantt/data/AssignmentsManipulationStore#config-liveFloatAssignedResources)
Flag indicating whether assigned resources should be floated live

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAssignmentsManipulationStore](https://bryntum.com/docs/gantt/api/Gantt/data/AssignmentsManipulationStore#property-isAssignmentsManipulationStore)
Identifies an object as an instance of [AssignmentsManipulationStore](https://bryntum.com/docs/gantt/api/#Gantt/data/AssignmentsManipulationStore) class, or subclass thereof.

[isAssignmentsManipulationStore](https://bryntum.com/docs/gantt/api/Gantt/data/AssignmentsManipulationStore#property-isAssignmentsManipulationStore-static)
Identifies an object as an instance of [AssignmentsManipulationStore](https://bryntum.com/docs/gantt/api/#Gantt/data/AssignmentsManipulationStore) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[fillFromMasterStores](https://bryntum.com/docs/gantt/api/Gantt/data/AssignmentsManipulationStore#function-fillFromMasterStores)
Fills this store from master [resource](https://bryntum.com/docs/gantt/api/#Gantt/data/ResourceStore) store and [assignment](https://bryntum.com/docs/gantt/api/#Gantt/data/AssignmentStore) store.
