# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.md.txt

# firebase-admin.machine-learning package

Firebase Machine Learning.

## Functions

|                                                                    Function                                                                    |                                                                                                                                                                                                        Description                                                                                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [getMachineLearning(app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.md#getmachinelearning_8a40afc) | Gets the [MachineLearning](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.machinelearning.md#machinelearning_class) service for the default app or a given app.`getMachineLearning()` can be called with no arguments to access the default app's `MachineLearning` service or as `getMachineLearning(app)` to access the `MachineLearning` service associated with a specific app. |

## Classes

|                                                                       Class                                                                       |                    Description                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| [MachineLearning](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.machinelearning.md#machinelearning_class) | The Firebase `MachineLearning` service interface. |
| [Model](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.model.md#model_class)                               | A Firebase ML Model output object.                |

## Interfaces

|                                                                                Interface                                                                                |                    Description                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| [GcsTfliteModelOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.gcstflitemodeloptions.md#gcstflitemodeloptions_interface) |                                                    |
| [ListModelsOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.listmodelsoptions.md#listmodelsoptions_interface)             | Interface representing options for listing Models. |
| [ListModelsResult](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.listmodelsresult.md#listmodelsresult_interface)                | Response object for a listModels operation.        |
| [ModelOptionsBase](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.modeloptionsbase.md#modeloptionsbase_interface)                | Firebase ML Model input objects                    |
| [TFLiteModel](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.tflitemodel.md#tflitemodel_interface)                               | A TensorFlow Lite Model output object              |

## Type Aliases

|                                                      Type Alias                                                       | Description |
|-----------------------------------------------------------------------------------------------------------------------|-------------|
| [ModelOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.md#modeloptions) |             |

## getMachineLearning(app)

Gets the [MachineLearning](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.machinelearning.md#machinelearning_class) service for the default app or a given app.

`getMachineLearning()` can be called with no arguments to access the default app's `MachineLearning` service or as `getMachineLearning(app)` to access the `MachineLearning` service associated with a specific app.

**Signature:**  

    export declare function getMachineLearning(app?: App): MachineLearning;

### Parameters

| Parameter | Type |                                                           Description                                                            |
|-----------|------|----------------------------------------------------------------------------------------------------------------------------------|
| app       | App  | Optional app whose `MachineLearning` service to return. If not provided, the default `MachineLearning` service will be returned. |

**Returns:**

[MachineLearning](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.machinelearning.md#machinelearning_class)

The default `MachineLearning` service if no app is provided or the `MachineLearning` service associated with the provided app.

### Example 1

    // Get the MachineLearning service for the default app
    const defaultMachineLearning = getMachineLearning();

### Example 2

    // Get the MachineLearning service for a given app
    const otherMachineLearning = getMachineLearning(otherApp);

## ModelOptions

**Signature:**  

    export type ModelOptions = ModelOptionsBase | GcsTfliteModelOptions;