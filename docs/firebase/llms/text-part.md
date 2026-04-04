# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/text-part.md.txt

# Firebase.AI.ModelContent.TextPart Struct Reference

# Firebase.AI.ModelContent.TextPart

A text part containing a string value.

## Summary

### Inheritance

Inherits from: [Firebase.AI.ModelContent.Part](https://firebase.google.com/docs/reference/unity/interface/firebase/a-i/model-content/part)

| ### Constructors and Destructors ||
|---|---|
| [TextPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/text-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_text_part_1a983d40e956cb7e579b241ed1f3b9d003)`(string text)` Creates a [TextPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/text-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_text_part) with the given text. ||

|                                                                                                       ### Properties                                                                                                       ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| [IsThought](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/text-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_text_part_1ac44382588379d7269386d34efe0864c0) | `bool`               |
| [Text](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/text-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_text_part_1a55ebcd8aba25c4c352db358eac1d7add)      | `string` Text value. |

|                                                                                                            ### Public functions                                                                                                             ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| [ToJson](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/text-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_text_part_1a08f6d39ab1eb93c9c4c295342b20de2c)`()` | `Dictionary< string, object > Part.` |

## Properties

### IsThought

```c#
bool Firebase::AI::ModelContent::TextPart::IsThought
```  

### Text

```c#
string Firebase::AI::ModelContent::TextPart::Text
```  
Text value.

## Public functions

### TextPart

```c#
 Firebase::AI::ModelContent::TextPart::TextPart(
  string text
)
```  
Creates a [TextPart](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content/text-part#struct_firebase_1_1_a_i_1_1_model_content_1_1_text_part) with the given text.

<br />

|                                       Details                                       ||
|------------|-------------------------------------------------------------------------|
| Parameters | |--------|------------------------| | `text` | The text value to use. | |

### ToJson

```c#
Dictionary< string, object > Part. Firebase::AI::ModelContent::TextPart::ToJson()
```