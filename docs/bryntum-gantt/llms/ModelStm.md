# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/stm/mixin/ModelStm.md

# [ModelStm](https://bryntum.com/docs/gantt/api/Core/data/stm/mixin/ModelStm)

Mixin making a model compatible with [StateTrackingManager](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager)

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isModelStm](https://bryntum.com/docs/gantt/api/Core/data/stm/mixin/ModelStm#property-isModelStm)
Identifies an object as an instance of [ModelStm](https://bryntum.com/docs/gantt/api/#Core/data/stm/mixin/ModelStm) class, or subclass thereof.

[isModelStm](https://bryntum.com/docs/gantt/api/Core/data/stm/mixin/ModelStm#property-isModelStm-static)
Identifies an object as an instance of [ModelStm](https://bryntum.com/docs/gantt/api/#Core/data/stm/mixin/ModelStm) class, or subclass thereof.

[stm](https://bryntum.com/docs/gantt/api/Core/data/stm/mixin/ModelStm#property-stm)
Reference to STM manager, if used

## Functions

Functions are methods available for calling on the class

[afterSet](https://bryntum.com/docs/gantt/api/Core/data/stm/mixin/ModelStm#function-afterSet)
Overridden to store initial data of the changed fields and to notify STM manager about the change action if anything has been changed in result.

The method is called from within [set](https://bryntum.com/docs/gantt/api/#Core/data/Model#function-set) method.

[beforeInsertChild](https://bryntum.com/docs/gantt/api/Core/data/stm/mixin/ModelStm#function-beforeInsertChild)
Called from [insertChild](https://bryntum.com/docs/gantt/api/#Core/data/mixin/TreeNode#function-insertChild) to obtain inserted records initial parents and parent index, to be able to restore the state back upon undo.

[afterInsertChild](https://bryntum.com/docs/gantt/api/Core/data/stm/mixin/ModelStm#function-afterInsertChild)
Called from [insertChild](https://bryntum.com/docs/gantt/api/#Core/data/mixin/TreeNode#function-insertChild) to notify [StateTrackingManager](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager) about children insertion. Provides it with all necessary context information collected in [beforeInsertChild](https://bryntum.com/docs/gantt/api/#Core/data/stm/mixin/ModelStm#function-beforeInsertChild) required to undo/redo the action.

[beforeRemoveChild](https://bryntum.com/docs/gantt/api/Core/data/stm/mixin/ModelStm#function-beforeRemoveChild)
Called from [removeChild](https://bryntum.com/docs/gantt/api/#Core/data/mixin/TreeNode#function-removeChild) to obtain removed records initial parent index, to be able to restore the state back upon undo.

[afterRemoveChild](https://bryntum.com/docs/gantt/api/Core/data/stm/mixin/ModelStm#function-afterRemoveChild)
Called from [removeChild](https://bryntum.com/docs/gantt/api/#Core/data/mixin/TreeNode#function-removeChild) to notify [StateTrackingManager](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager) about children removing. Provides it with all necessary context information collected in [beforeRemoveChild](https://bryntum.com/docs/gantt/api/#Core/data/stm/mixin/ModelStm#function-beforeRemoveChild) required to undo/redo the action.
