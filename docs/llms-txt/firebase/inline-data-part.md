# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/inline-data-part.md.txt

# Firebase.AI.ModelContent.InlineDataPart Struct Reference

# Firebase.AI.ModelContent.InlineDataPart

Data with a specified media type.

## Summary

Note: Not all media types may be supported by the [AI](https://firebase.google.com/docs/reference/unity/namespace/firebase/a-i#namespace_firebase_1_1_a_i) model.

### Inheritance

Inherits from: [Firebase.AI.ModelContent.Part](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part)

| ### Constructors and Destructors ||
|---|---|
| [InlineDataPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/inline-data-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_inline_data_part_1a43e09adae06aeaf9a3a357f1262b2834)`(string mimeType, byte[] data)` Creates an [InlineDataPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/inline-data-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_inline_data_part) from data and a MIME type. ||

|                                                                                                                             ### Properties                                                                                                                              ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| [Data](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/inline-data-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_inline_data_part_1ae22274e17a7b296e64ae45a4d75ebfbb)      | `byte[]` The data provided in the inline data part. |
| [IsThought](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/inline-data-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_inline_data_part_1a8d055a3ca9719a1fe9cae0c12cae58f2) | `bool`                                              |
| [MimeType](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/inline-data-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_inline_data_part_1aa7070431d458d0c2ffd3a37c8cec0fd8)  | `string` The IANA standard MIME type of the data.   |

|                                                                                                                   ### Public functions                                                                                                                    ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| [ToJson](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/inline-data-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_inline_data_part_1a09892d303eaa2443121a1f06c220a7dd)`()` | `Dictionary< string, object > Part.` |

## Properties

### Data

```c#
byte[] Firebase::AI::ModelContent::InlineDataPart::Data
```  
The data provided in the inline data part.  

### IsThought

```c#
bool Firebase::AI::ModelContent::InlineDataPart::IsThought
```  

### MimeType

```c#
string Firebase::AI::ModelContent::InlineDataPart::MimeType
```  
The IANA standard MIME type of the data.

## Public functions

### InlineDataPart

```c#
 Firebase::AI::ModelContent::InlineDataPart::InlineDataPart(
  string mimeType,
  byte[] data
)
```  
Creates an [InlineDataPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/inline-data-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_inline_data_part) from data and a MIME type.

Important: Supported input types depend on the model on the model being used; see \[input files and requirements\](<https://firebase.google.com/docs/vertex-ai/input-file-requirements>) for more details.

<br />

|                                                                                                                                                                                                                                                                                                                                                          Details                                                                                                                                                                                                                                                                                                                                                           ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `mimeType` | The IANA standard MIME type of the data, for example, `"image/jpeg"` or `"video/mp4"`; see [input files and requirements](https://firebase.google.com/docs/vertex-ai/input-file-requirements) for supported values. | | `data`     | The data representation of an image, video, audio or document; see [input files and requirements](https://firebase.google.com/docs/vertex-ai/input-file-requirements) for supported media types.                    | |

### ToJson

```c#
Dictionary< string, object > Part. Firebase::AI::ModelContent::InlineDataPart::ToJson()
```