# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/firebase-a-i/backend.md.txt

# Firebase.AI.FirebaseAI.Backend Struct Reference

# Firebase.AI.FirebaseAI.Backend

Defines which backend [AI](https://firebase.google.com/docs/reference/unity/namespace/firebase/a-i#namespace_firebase_1_1_a_i) service is being used, provided to [FirebaseAI.GetInstance](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/firebase-a-i#class_firebase_1_1_a_i_1_1_firebase_a_i_1a727957806e59473b6fb1beff4ffa8438).

## Summary

|                                                                                                                                                                                                                                                  ### Public static functions                                                                                                                                                                                                                                                   ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GoogleAI](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/firebase-a-i/backend#struct_firebase_1_1_a_i_1_1_firebase_a_i_1_1_backend_1a2b353998ce5553ae347954c4aadb3b79)`()`                | [Backend](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/firebase-a-i/backend#struct_firebase_1_1_a_i_1_1_firebase_a_i_1_1_backend) The Google [AI](https://firebase.google.com/docs/reference/unity/namespace/firebase/a-i#namespace_firebase_1_1_a_i) backend service configuration. |
| [VertexAI](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/firebase-a-i/backend#struct_firebase_1_1_a_i_1_1_firebase_a_i_1_1_backend_1a27090e4367780f02f77ceaba0e09cbb3)`(string location)` | [Backend](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/firebase-a-i/backend#struct_firebase_1_1_a_i_1_1_firebase_a_i_1_1_backend) The Vertex [AI](https://firebase.google.com/docs/reference/unity/namespace/firebase/a-i#namespace_firebase_1_1_a_i) backend service configuration. |

|                                                                                                     ### Public functions                                                                                                      ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| [ToString](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/firebase-a-i/backend#struct_firebase_1_1_a_i_1_1_firebase_a_i_1_1_backend_1a85c248345001cc60602fd2d1ed8da9bd)`()` | `override readonly string` |

## Public static functions

### GoogleAI

```c#
Backend Firebase::AI::FirebaseAI::Backend::GoogleAI()
```  
The Google [AI](https://firebase.google.com/docs/reference/unity/namespace/firebase/a-i#namespace_firebase_1_1_a_i) backend service configuration.  

### VertexAI

```c#
Backend Firebase::AI::FirebaseAI::Backend::VertexAI(
  string location
)
```  
The Vertex [AI](https://firebase.google.com/docs/reference/unity/namespace/firebase/a-i#namespace_firebase_1_1_a_i) backend service configuration.

<br />

|                                                                                                                                                                                                                          Details                                                                                                                                                                                                                          ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `location` | The region identifier, defaulting to `us-central1`; see [Vertex AI regions](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations#available-regions) for a list of supported regions. | |

## Public functions

### ToString

```c#
override readonly string Firebase::AI::FirebaseAI::Backend::ToString()
```