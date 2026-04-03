# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/segment.md.txt

# Firebase.AI.Segment Struct Reference

# Firebase.AI.Segment

Represents a specific segment within a [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) struct, often used to pinpoint the exact location of text or data that grounding information refers to.

## Summary

|                                                                                                                                                                                                 ### Properties                                                                                                                                                                                                 ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [EndIndex](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/segment#struct_firebase_1_1_a_i_1_1_segment_1a4d8735a90f26d3927a7ee4d42c87ccb8)   | `int` The zero-based end index of the segment within the specified `Part`, measured in UTF-8 bytes.                                                                                                                                         |
| [PartIndex](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/segment#struct_firebase_1_1_a_i_1_1_segment_1af0eb055dd42b2cdadb4f0511a9e5a4dd)  | `int` The zero-based index of the `Part` object within the `parts` array of its parent [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) object. |
| [StartIndex](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/segment#struct_firebase_1_1_a_i_1_1_segment_1a298b3d890585374b466c3cee0778a72d) | `int` The zero-based start index of the segment within the specified `Part`, measured in UTF-8 bytes.                                                                                                                                       |
| [Text](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/segment#struct_firebase_1_1_a_i_1_1_segment_1ad3a1b47209779d8a0692020ee53232c5)       | `string` The text corresponding to the segment from the response.                                                                                                                                                                           |

## Properties

### EndIndex

```c#
int Firebase::AI::Segment::EndIndex
```  
The zero-based end index of the segment within the specified `Part`, measured in UTF-8 bytes.

This offset is exclusive, meaning the character at this index is not included in the segment.  

### PartIndex

```c#
int Firebase::AI::Segment::PartIndex
```  
The zero-based index of the `Part` object within the `parts` array of its parent [ModelContent](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/model-content#struct_firebase_1_1_a_i_1_1_model_content) object.

This identifies which part of the content the segment belongs to.  

### StartIndex

```c#
int Firebase::AI::Segment::StartIndex
```  
The zero-based start index of the segment within the specified `Part`, measured in UTF-8 bytes.

This offset is inclusive, starting from 0 at the beginning of the part's content.  

### Text

```c#
string Firebase::AI::Segment::Text
```  
The text corresponding to the segment from the response.