# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/request-options.md.txt

# Firebase.AI.RequestOptions Struct Reference

# Firebase.AI.RequestOptions

Configuration parameters for sending requests to the backend.

## Summary

| ### Constructors and Destructors ||
|---|---|
| [RequestOptions](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/request-options#struct_firebase_1_1_a_i_1_1_request_options_1a225b2d25645b4a83497f1c0bac297071)`(TimeSpan? timeout)` Initialize a [RequestOptions](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/request-options#struct_firebase_1_1_a_i_1_1_request_options) object. ||

## Public functions

### RequestOptions

```c#
 Firebase::AI::RequestOptions::RequestOptions(
  TimeSpan? timeout
)
```  
Initialize a [RequestOptions](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/request-options#struct_firebase_1_1_a_i_1_1_request_options) object.

<br />

|                                                                                          Details                                                                                          ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------|------------------------------------------------------------------------| | `timeout` | The request's timeout interval. Defaults to 180 seconds if given null. | |