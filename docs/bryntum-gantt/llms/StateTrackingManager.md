# Source: https://bryntum.com/products/gantt/docs-llm/api/SchedulerPro/data/stm/StateTrackingManager.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/stm/StateTrackingManager.md

# [StateTrackingManager](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager)

Tracks the state of every store registered via [addStore](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager#function-addStore). It is [disabled](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager#config-disabled) by default so remember to call [enable](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager#function-enable) when your stores are registered and initial dataset is loaded. Use [undo](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager#function-undo) / [redo](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager#function-redo) method calls to restore state to a particular point in time

```
stm = new StateTrackingManager({
    autoRecord : true,
    listeners  : {
       recordingStop() {
           // your custom code to update undo/redo GUI controls
           updateUndoRedoControls();
       },
       restoringStop({ stm }) {
           // your custom code to update undo/redo GUI controls
           updateUndoRedoControls();
       },
       disabled() {
           // in Gantt, Scheduler and other scheduling products,
           // also need to update the undo/redo controls on `disabled`
           // event, due to implementation details
           updateUndoRedoControls();
       }
   },
   getTransactionTitle(transaction) {
       // your custom code to analyze the transaction and return custom transaction title
       const lastAction = transaction.queue[transaction.queue.length - 1];

       if (lastAction instanceof AddAction) {
           let title = 'Add new record';
       }

       return title;
   }
});

stm.addStore(userStore);
stm.addStore(companyStore);
stm.addStore(otherStore);

stm.enable();
```

**Note:** STM currently does not support undoing server side added and saved records. Therefore it's recommended to [reset the queue](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager#function-resetQueue) each time a tracked store(s) loads from or saves its changes to the server. If Crud Manager is used it can be done like this:

```
crudManager.on({
    requestDone() {
        stm.resetQueue();
    }
});
```

and in case individual stores are used:

```
ajaxStore.on({
    afterRequest({ exception }) {
        if (!exception) {
            stm.resetQueue();
        }
    }
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[disabled](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#config-disabled)
Default manager disabled state

[autoRecord](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#config-autoRecord)
Whether to start transaction recording automatically in case the Manager is enabled.

In the auto recording mode, the manager waits for the first change in any store being managed and starts a transaction, i.e. records any changes in its monitored stores. The transaction lasts for [autoRecordTransactionStopTimeout](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager#config-autoRecordTransactionStopTimeout) and afterward creates one undo/redo step, including all changes in the stores during that period of time.

In non auto recording mode you have to call [startTransaction](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager#function-startTransaction) / [stopTransaction](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager#function-stopTransaction) to start and end a transaction.

**NOTE**, enabling this option, will not enable the STM itself. This should be done with a separate call to [enable](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager#function-enable) method or by assigning `false` to [disabled](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager#property-disabled) property. If you don't enable the STM, it will not be tracking changes in the data.

If you use the `UndoRedo` widget in your app, it will enable STM automatically, on the `load` event of the project's crud manager (in the gantt case, the project is the crud manager). In other cases, you need to enable STM manually.

[autoRecordTransactionStopTimeout](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#config-autoRecordTransactionStopTimeout)
The transaction duration (in ms) for the auto recording mode [autoRecord](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager#config-autoRecord)

[autoRecordMergeUpdateActions](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#config-autoRecordMergeUpdateActions)
By the end of a transaction, with this config set to `true`, all model update actions will be merged to one action per model. Only the initial start value and the last change will be kept.

If non auto recording mode, you can call [mergeTransactionUpdateActions](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager#function-mergeTransactionUpdateActions).

[makeModelUpdateAction](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#config-makeModelUpdateAction)
Store model update action factory

[makeModelInsertChildAction](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#config-makeModelInsertChildAction)
Store insert child model action factory.

[makeModelRemoveChildAction](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#config-makeModelRemoveChildAction)
Store remove child model action factory.

[makeStoreModelAddAction](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#config-makeStoreModelAddAction)
Store add model action factory.

[makeStoreModelInsertAction](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#config-makeStoreModelInsertAction)
Store insert model action factory.

[makeStoreModelRemoveAction](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#config-makeStoreModelRemoveAction)
Store remove model action factory.

[makeStoreRemoveAllAction](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#config-makeStoreRemoveAllAction)
Store remove all models action factory.

[getTransactionTitle](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#config-getTransactionTitle)
Function to create a transaction title if none is provided. The function receives a transaction and should return a title.

[revisionsEnabled](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#config-revisionsEnabled)
Enables [revision](https://bryntum.com/docs/gantt/api/#Gantt/guides/revisions/overview.md) tracking by STM

[revisionQueueMaxLength](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#config-revisionQueueMaxLength)
Specifies length of the transaction queue when cleanup will be triggered

[revisionQueueCommittedMinLength](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#config-revisionQueueCommittedMinLength)
Specifies minimum length of last transactions

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isStateTrackingManager](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#property-isStateTrackingManager)
Identifies an object as an instance of [StateTrackingManager](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager) class, or subclass thereof.

[isStateTrackingManager](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#property-isStateTrackingManager-static)
Identifies an object as an instance of [StateTrackingManager](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager) class, or subclass thereof.

[revisionQueueMaxLength](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#property-revisionQueueMaxLength)
Specifies length of the transaction queue when cleanup will be triggered

[revisionQueueCommittedMinLength](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#property-revisionQueueCommittedMinLength)
Specifies minimum length of last transactions

[state](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#property-state)
Gets the current state of the manager

[position](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#property-position)
Gets current undo/redo queue position

[length](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#property-length)
Gets current undo/redo queue length

[stores](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#property-stores)
Gets all the stores registered in STM

[disabled](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#property-disabled)
Get/set manager disabled state

[isReady](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#property-isReady)
Checks manager ready state

[isRecording](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#property-isRecording)
Checks manager recording state

[isApplyingStash](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#property-isApplyingStash)
Checks if STM is restoring a stash

[autoRecord](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#property-autoRecord)
Gets/sets manager auto record option

[transaction](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#property-transaction)
Gets currently recording STM transaction.

[queue](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#property-queue)
Gets titles of all recorded undo/redo transactions

[isRestoring](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#property-isRestoring)
Gets manager restoring state.

[canUndo](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#property-canUndo)
Checks if the manager can undo.

[canRedo](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#property-canRedo)
Checks if the manager can redo.

## Functions

Functions are methods available for calling on the class

[hasStore](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-hasStore)
Checks if a store has been added to the manager

[addStore](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-addStore)
Adds a store instance to the manager

```
const stm = new StateTrackingManager({ ... })
const store = new Store({ ... });
stm.addStore(store);
```

[removeStore](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-removeStore)
Removes a store from the manager

[forEachStore](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-forEachStore)
Calls `fn` for each store registered in STM.

[enable](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-enable)
Enables manager

[disable](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-disable)
Disables manager

[startTransaction](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-startTransaction)
Starts undo/redo recording transaction.

[stopTransaction](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-stopTransaction)
Stops undo/redo recording transaction

[stopTransactionDelayed](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-stopTransactionDelayed)
Stops undo/redo recording transaction after [autoRecordTransactionStopTimeout](https://bryntum.com/docs/gantt/api/#Core/data/stm/StateTrackingManager#config-autoRecordTransactionStopTimeout) delay.

[rejectTransaction](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-rejectTransaction)
Rejects currently recorded transaction.

[undo](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-undo)
Undoes current undo/redo transaction.

[undoAll](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-undoAll)
Undoes all transactions.

[redo](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-redo)
Redoes current undo/redo transaction.

[redoAll](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-redoAll)
Redoes all transactions.

[resetQueue](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-resetQueue)
Resets undo/redo queue.

[resetUndoQueue](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-resetUndoQueue)
Resets undo queue.

[resetRedoQueue](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-resetRedoQueue)
Resets redo queue.

[notifyStoresAboutStateRestoringStop](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-notifyStoresAboutStateRestoringStop)

[onModelUpdate](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-onModelUpdate)
Method to call from model STM mixin upon model update

[onModelInsertChild](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-onModelInsertChild)
Method to call from model STM mixin upon tree model child insertion

[onModelRemoveChild](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-onModelRemoveChild)
Method to call from model STM mixin upon tree model child removal

[onStoreModelAdd](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-onStoreModelAdd)
Method to call from store STM mixin upon store models adding

[onStoreModelInsert](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-onStoreModelInsert)
Method to call from store STM mixin upon store models insertion

[onStoreModelRemove](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-onStoreModelRemove)
Method to call from store STM mixin upon store models removal

[onStoreRemoveAll](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-onStoreRemoveAll)
Method to call from store STM mixin upon store clear

[mergeTransactionUpdateActions](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-mergeTransactionUpdateActions)
Merges all update actions into one per model, keeping the oldest and the newest values.

[initRevision](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-initRevision)
This method sets revision number of the initial data set. It should be called once after loading the data to set a starting point to sync revisions with the backend.

[increaseRevision](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-increaseRevision)
This method takes transaction and creates local revision

[createDataCorrectionTransaction](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-createDataCorrectionTransaction)
This method creates special data revision which has no input state, only a data correction for a case when applying remote revisions lead to new changes. This revision will be sent, it should be persisted on the backend, and any client applying it should not see any changes after.

[createConflictResolutionRevision](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-createConflictResolutionRevision)
This method creates special conflict resolution revision which contains only conflict resolution actions. It is linked to the revision with a conflict via `conflictResolutionFor` property. Such revision cannot be rolled back locally because it will introduce the same conflict again.

[commitRevision](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-commitRevision)
Commits revision, can assign a new id for the local revision which is already applied, but was finally committed on the backend.

[cleanUpRevisions](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-cleanUpRevisions)
Clears committed revisions, we only need to use last one.

[markCurrentTransactionContentUserInput](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#function-markCurrentTransactionContentUserInput)
Used to distinguish user input from values calculated by the project. If any actions in the revision are marked as user input then checkout logic will only use user input. If nothing is marked, then revision is not treated specially.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[disabled](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#event-disabled)
Fired when the disabled state of the STM changes

[recordingStart](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#event-recordingStart)
Fired upon state recording operation starts.

[recordingStop](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#event-recordingStop)
Fired upon state recording operation stops.

[restoringStart](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#event-restoringStart)
Fired upon state restoration operation starts.

[restoringStop](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#event-restoringStop)
Fired upon state restoration operation stops.

[queueReset](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#event-queueReset)
Fired upon state undo/redo queue reset.

[checkoutStart](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#event-checkoutStart)
Fires when checkout starts.

[revisionRecordingStart](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#event-revisionRecordingStart)
Fires when recording remote revision starts.

[temporaryRevisionRecordingStart](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#event-temporaryRevisionRecordingStart)
Fires when recording temporary revision starts.

[revisionRecordingStop](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#event-revisionRecordingStop)
Fires when recording remote revision stops.

[temporaryRevisionRecordingStop](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#event-temporaryRevisionRecordingStop)
Fires when recording temporary revision stops. This revision is ignored because we already have a transaction with all the actions. It is only used to extract a conflict resolution.

[checkoutToHead](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#event-checkoutToHead)
Fires when STM is checked out to HEAD and moves to Ready/AutoReady state.

[revisionAdd](https://bryntum.com/docs/gantt/api/Core/data/stm/StateTrackingManager#event-revisionAdd)
Triggered when revision is added to the revision queue.
