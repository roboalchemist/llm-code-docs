# Source: https://firebase.google.com/docs/reference/js/ai.singlerequestoptions.md.txt

# SingleRequestOptions interface

Options that can be provided per-request. Extends the base [RequestOptions](https://firebase.google.com/docs/reference/js/ai.requestoptions.md#requestoptions_interface) (like `timeout` and `baseUrl`) with request-specific controls like cancellation via `AbortSignal`.

Options specified here will override any default [RequestOptions](https://firebase.google.com/docs/reference/js/ai.requestoptions.md#requestoptions_interface) configured on a model (for example, [GenerativeModel](https://firebase.google.com/docs/reference/js/ai.generativemodel.md#generativemodel_class)).

**Signature:**

    export interface SingleRequestOptions extends RequestOptions 

**Extends:** [RequestOptions](https://firebase.google.com/docs/reference/js/ai.requestoptions.md#requestoptions_interface)

## Properties

| Property | Type | Description |
|---|---|---|
| [signal](https://firebase.google.com/docs/reference/js/ai.singlerequestoptions.md#singlerequestoptionssignal) | AbortSignal | An `AbortSignal` instance that allows cancelling ongoing requests (like `generateContent` or `generateImages`).If provided, calling `abort()` on the corresponding `AbortController` will attempt to cancel the underlying HTTP request. An `AbortError` will be thrown if cancellation is successful.Note that this will not cancel the request in the backend, so any applicable billing charges will still be applied despite cancellation. |

## SingleRequestOptions.signal

An `AbortSignal` instance that allows cancelling ongoing requests (like `generateContent` or `generateImages`).

If provided, calling `abort()` on the corresponding `AbortController` will attempt to cancel the underlying HTTP request. An `AbortError` will be thrown if cancellation is successful.

Note that this will not cancel the request in the backend, so any applicable billing charges will still be applied despite cancellation.

**Signature:**

    signal?: AbortSignal;

### Example

    const controller = new AbortController();
    const model = getGenerativeModel({
      // ...
    });
    model.generateContent(
      "Write a story about a magic backpack.",
      { signal: controller.signal }
    );

    // To cancel request:
    controller.abort();