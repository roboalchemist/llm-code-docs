# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.machinelearning.md.txt

# MachineLearning class

The Firebase `MachineLearning` service interface.

**Signature:**  

    export declare class MachineLearning 

## Properties

|                                                              Property                                                              | Modifiers | Type |                                                                               Description                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------|-----------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [app](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.machinelearning.md#machinelearningapp) |           | App  | The [App](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.app.md#app_interface) associated with the current `MachineLearning` service instance. |

## Methods

|                                                                               Method                                                                               | Modifiers |                                    Description                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------|
| [createModel(model)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.machinelearning.md#machinelearningcreatemodel)          |           | Creates a model in the current Firebase project.                                  |
| [deleteModel(modelId)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.machinelearning.md#machinelearningdeletemodel)        |           | Deletes a model from the current project.                                         |
| [getModel(modelId)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.machinelearning.md#machinelearninggetmodel)              |           | Gets the model specified by the given ID.                                         |
| [listModels(options)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.machinelearning.md#machinelearninglistmodels)          |           | Lists the current project's models.                                               |
| [publishModel(modelId)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.machinelearning.md#machinelearningpublishmodel)      |           | Publishes a Firebase ML model.A published model can be downloaded to client apps. |
| [unpublishModel(modelId)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.machinelearning.md#machinelearningunpublishmodel)  |           | Unpublishes a Firebase ML model.                                                  |
| [updateModel(modelId, model)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.machinelearning.md#machinelearningupdatemodel) |           | Updates a model's metadata or model file.                                         |

## MachineLearning.app

The [App](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app.app.md#app_interface) associated with the current `MachineLearning` service instance.

**Signature:**  

    get app(): App;

## MachineLearning.createModel()

Creates a model in the current Firebase project.

**Signature:**  

    createModel(model: ModelOptions): Promise<Model>;

### Parameters

| Parameter |                                                         Type                                                          |     Description      |
|-----------|-----------------------------------------------------------------------------------------------------------------------|----------------------|
| model     | [ModelOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.md#modeloptions) | The model to create. |

**Returns:**

Promise\<[Model](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.model.md#model_class)\>

A Promise fulfilled with the created model.

## MachineLearning.deleteModel()

Deletes a model from the current project.

**Signature:**  

    deleteModel(modelId: string): Promise<void>;

### Parameters

| Parameter |  Type  |          Description           |
|-----------|--------|--------------------------------|
| modelId   | string | The ID of the model to delete. |

**Returns:**

Promise\<void\>

## MachineLearning.getModel()

Gets the model specified by the given ID.

**Signature:**  

    getModel(modelId: string): Promise<Model>;

### Parameters

| Parameter |  Type  |         Description         |
|-----------|--------|-----------------------------|
| modelId   | string | The ID of the model to get. |

**Returns:**

Promise\<[Model](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.model.md#model_class)\>

A Promise fulfilled with the model object.

## MachineLearning.listModels()

Lists the current project's models.

**Signature:**  

    listModels(options?: ListModelsOptions): Promise<ListModelsResult>;

### Parameters

| Parameter |                                                                            Type                                                                             |     Description      |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| options   | [ListModelsOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.listmodelsoptions.md#listmodelsoptions_interface) | The listing options. |

**Returns:**

Promise\<[ListModelsResult](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.listmodelsresult.md#listmodelsresult_interface)\>

A promise that resolves with the current (filtered) list of models and the next page token. For the last page, an empty list of models and no page token are returned.

## MachineLearning.publishModel()

Publishes a Firebase ML model.

A published model can be downloaded to client apps.

**Signature:**  

    publishModel(modelId: string): Promise<Model>;

### Parameters

| Parameter |  Type  |           Description           |
|-----------|--------|---------------------------------|
| modelId   | string | The ID of the model to publish. |

**Returns:**

Promise\<[Model](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.model.md#model_class)\>

A Promise fulfilled with the published model.

## MachineLearning.unpublishModel()

Unpublishes a Firebase ML model.

**Signature:**  

    unpublishModel(modelId: string): Promise<Model>;

### Parameters

| Parameter |  Type  |            Description            |
|-----------|--------|-----------------------------------|
| modelId   | string | The ID of the model to unpublish. |

**Returns:**

Promise\<[Model](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.model.md#model_class)\>

A Promise fulfilled with the unpublished model.

## MachineLearning.updateModel()

Updates a model's metadata or model file.

**Signature:**  

    updateModel(modelId: string, model: ModelOptions): Promise<Model>;

### Parameters

| Parameter |                                                         Type                                                          |          Description           |
|-----------|-----------------------------------------------------------------------------------------------------------------------|--------------------------------|
| modelId   | string                                                                                                                | The ID of the model to update. |
| model     | [ModelOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.md#modeloptions) | The model fields to update.    |

**Returns:**

Promise\<[Model](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.model.md#model_class)\>

A Promise fulfilled with the updated model.