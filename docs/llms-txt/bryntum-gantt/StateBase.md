# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/stm/state/StateBase.md

# [StateBase](https://bryntum.com/docs/gantt/api/Core/data/stm/state/StateBase)

Abstract class for STM states

Every on\* method should return a state for the STM which it should switch to or throw an exception that this call at this state is illegal.

Interface of this class mirrors interface of [StateTrackingManager](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager).
