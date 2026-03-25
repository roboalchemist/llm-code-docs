# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/AjaxHelper.md

# [AjaxHelper](https://bryntum.com/docs/gantt/api/Core/helper/AjaxHelper)

Simplifies Ajax requests. Uses fetch & promises.

```
AjaxHelper.get('some-url').then(response => {
    // process request response here
});
```

Uploading file to server via FormData interface. Please visit [FormData](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/API/FormData) for details.

```
const formData = new FormData();
formData.append('file', 'fileNameToUpload');
AjaxHelper.post('file-upload-url', formData).then(response => {
    // process request response here
});
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[DEFAULT_FETCH_OPTIONS](https://bryntum.com/docs/gantt/api/Core/helper/AjaxHelper#property-DEFAULT_FETCH_OPTIONS-static)
Sets default options for [AjaxHelper#fetch()](https://bryntum.com/docs/gantt/api/#Core/helper/AjaxHelper#function-fetch-static) calls. Please see [FetchOptions](https://bryntum.com/docs/gantt/api/#Core/helper/AjaxHelper#typedef-FetchOptions) and [fetch API](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/fetch) for details.

```
// default content-type for all requests will be "application/json"
AjaxHelper.DEFAULT_FETCH_OPTIONS = {
    headers : {
        'content-type' : 'application/json'
    }
};
```

## Functions

Functions are methods available for calling on the class

[get](https://bryntum.com/docs/gantt/api/Core/helper/AjaxHelper#function-get-static)
Make a request (using GET) to the specified url.

[post](https://bryntum.com/docs/gantt/api/Core/helper/AjaxHelper#function-post-static)
POST data to the specified URL.

[fetch](https://bryntum.com/docs/gantt/api/Core/helper/AjaxHelper#function-fetch-static)
Fetch the specified resource using the `fetch` API.

[mockUrl](https://bryntum.com/docs/gantt/api/Core/helper/AjaxHelper#function-mockUrl-static)
Registers the passed URL to return the passed mocked up Fetch Response object to the AjaxHelper's promise resolve function.

## Typedefs

Typedefs are type definitions for the class

[FetchOptions](https://bryntum.com/docs/gantt/api/Core/helper/AjaxHelper#typedef-FetchOptions)
Options for the requests. Please see [fetch API](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/fetch) for details

To set default values for the options please use [DEFAULT\_FETCH\_OPTIONS](https://bryntum.com/docs/gantt/api/#Core/helper/AjaxHelper#property-DEFAULT_FETCH_OPTIONS-static) property:

```
// enable passing parameters in request body by default
AjaxHelper.DEFAULT_FETCH_OPTIONS = { addQueryParamsToBody : true };
```
