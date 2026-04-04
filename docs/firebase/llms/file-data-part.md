# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/file-data-part.md.txt

# Firebase.AI.ModelContent.FileDataPart

File data stored in Cloud[Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage)for[Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase), referenced by a URI.

## Summary

### Inheritance

Inherits from:[Firebase.AI.ModelContent.Part](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part)

| ### Constructors and Destructors ||
|---|---|
| [FileDataPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/file-data-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_file_data_part_1aefa5c669ed92aa0388efe1e5853ab410)`(string mimeType, System.Uri uri)` Constructs a new file data part. ||

|                                                                                                                          ### Properties                                                                                                                           ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| [IsThought](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/file-data-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_file_data_part_1a003b8c5b0abe10cacf0dae5309661026) | `bool`                                            |
| [MimeType](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/file-data-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_file_data_part_1a1182e8587e75dd25c47c6e0911cc3cd1)  | `string` The IANA standard MIME type of the data. |
| [Uri](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/file-data-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_file_data_part_1a1cf1b448aef59eaa41003525e265a78b)       | `System.Uri` The URI of the file.                 |

|                                                                                                                 ### Public functions                                                                                                                  ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| [ToJson](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/file-data-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_file_data_part_1abfb360b0282dbc1047f6016e27ddf098)`()` | `Dictionary< string, object > Part.` |

## Properties

### IsThought

```c#
bool Firebase::AI::ModelContent::FileDataPart::IsThought
```  

### MimeType

```c#
string Firebase::AI::ModelContent::FileDataPart::MimeType
```  
The IANA standard MIME type of the data.  

### Uri

```c#
System.Uri Firebase::AI::ModelContent::FileDataPart::Uri
```  
The URI of the file.

## Public functions

### FileDataPart

```c#
 Firebase::AI::ModelContent::FileDataPart::FileDataPart(
  string mimeType,
  System.Uri uri
)
```  
Constructs a new file data part.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `mimeType` | The IANA standard MIME type of the uploaded file, for example,`"image/jpeg"`or`"video/mp4"`; see[media requirements](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/send-multimodal-prompts#media_requirements)for supported values.                                                                    | | `uri`      | The`"gs://"`-prefixed URI of the file in Cloud[Storage](https://firebase.google.com/docs/reference/unity/namespace/firebase/storage#namespace_firebase_1_1_storage)for[Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase), for example,`"gs://bucket-name/path/image.jpg"` | |

### ToJson

```c#
Dictionary< string, object > Part. Firebase::AI::ModelContent::FileDataPart::ToJson()
```