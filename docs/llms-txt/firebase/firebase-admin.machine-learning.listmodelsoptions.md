# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.listmodelsoptions.md.txt

# ListModelsOptions interface

Interface representing options for listing Models.

**Signature:**  

    export interface ListModelsOptions 

## Properties

|                                                                   Property                                                                   |  Type  |                           Description                            |
|----------------------------------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------|
| [filter](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.listmodelsoptions.md#listmodelsoptionsfilter) | string | An expression that specifies how to filter the results.Examples: |

    display_name = your_model
    display_name : experimental_*
    tags: face_detector AND tags: experimental
    state.published = true

See https://firebase.google.com/docs/ml/manage-hosted-models#list_your_projects_models \|
\| [pageSize](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.listmodelsoptions.md#listmodelsoptionspagesize) \| number \| The number of results to return in each page. \|
\| [pageToken](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.listmodelsoptions.md#listmodelsoptionspagetoken) \| string \| A token that specifies the result page to return. \|

## ListModelsOptions.filter

An expression that specifies how to filter the results.

Examples:  

    display_name = your_model
    display_name : experimental_*
    tags: face_detector AND tags: experimental
    state.published = true

See https://firebase.google.com/docs/ml/manage-hosted-models#list_your_projects_models

**Signature:**  

    filter?: string;

## ListModelsOptions.pageSize

The number of results to return in each page.

**Signature:**  

    pageSize?: number;

## ListModelsOptions.pageToken

A token that specifies the result page to return.

**Signature:**  

    pageToken?: string;