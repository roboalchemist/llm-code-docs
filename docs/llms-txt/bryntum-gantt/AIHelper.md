# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/feature/ai/AIHelper.md

# [AIHelper](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIHelper)

Helper class for constructing AI tools

## Functions

Functions are methods available for calling on the class

[createBasicTool](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIHelper#function-createBasicTool-static)
Convenience function to easier create tools without repeating redundant code blocks. Assumes that the `parameters` are of type `object`.

[createConditionTool](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIHelper#function-createConditionTool-static)
Convenience function to easier create tools with support for `conditions` which in short is a way for the agent and the AI feature to communicate about datasets without actually reading the datasets. In essence, they are filters which is used when reading or modifying data to target the correct records.

[createGetRecordsTool](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIHelper#function-createGetRecordsTool-static)
Convenience function to easily create a specific read data tool for the agent.

[createUpdateRecordsTool](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIHelper#function-createUpdateRecordsTool-static)
Convenience function to easily create a specific update data tool for the agent.

[createDeleteRecordsTool](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIHelper#function-createDeleteRecordsTool-static)
Convenience function to easily create a specific delete records tool for the agent.

[createAddRecordTool](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIHelper#function-createAddRecordTool-static)
Convenience function to easily create a specific add records tool for the agent.

[collectLeafFilters](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIHelper#function-collectLeafFilters-static)
Recursively collects all leaf filters (filters with a property) from a filter tree.

[checkFilterConflicts](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIHelper#function-checkFilterConflicts-static)
Checks if new filters conflict with existing store filters. Returns an error message if conflicts are found, null otherwise.

## Typedefs

Typedefs are type definitions for the class

[AIToolCondition](https://bryntum.com/docs/gantt/api/Core/feature/ai/AIHelper#typedef-AIToolCondition)
An AI tool condition object
