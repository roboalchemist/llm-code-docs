# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.listmodelsresult.md.txt

# ListModelsResult interface

Response object for a listModels operation.

**Signature:**  

    export interface ListModelsResult 

## Properties

|                                                                     Property                                                                     |                                                          Type                                                           |                                              Description                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [models](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.listmodelsresult.md#listmodelsresultmodels)       | [Model](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.model.md#model_class)\[\] | A list of models in your project.                                                                      |
| [pageToken](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.listmodelsresult.md#listmodelsresultpagetoken) | string                                                                                                                  | A token you can use to retrieve the next page of results. If null, the current page is the final page. |

## ListModelsResult.models

A list of models in your project.

**Signature:**  

    readonly models: Model[];

## ListModelsResult.pageToken

A token you can use to retrieve the next page of results. If null, the current page is the final page.

**Signature:**  

    readonly pageToken?: string;