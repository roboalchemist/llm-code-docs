# Source: https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/citation.md.txt

# Firebase.AI.Citation Struct Reference

# Firebase.AI.Citation

A struct describing a source attribution.

## Summary

|                                                                                                                               ### Properties                                                                                                                                ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [EndIndex](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/citation#struct_firebase_1_1_a_i_1_1_citation_1af3939937f3046c3504626c359b7b6aed)        | `int` The exclusive end of a sequence in a model response that derives from a cited source.       |
| [License](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/citation#struct_firebase_1_1_a_i_1_1_citation_1af493b750e9d772bcec8e90faf08618d0)         | `string` The license the cited source work is distributed under, if specified.                    |
| [PublicationDate](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/citation#struct_firebase_1_1_a_i_1_1_citation_1a16c7dad235c5ae95d99921b89b421e14) | `System.DateTime` The publication date of the cited source, if available.                         |
| [StartIndex](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/citation#struct_firebase_1_1_a_i_1_1_citation_1a4bbdeba2337d92bbd36d53ae8cde0c85)      | `int` The inclusive beginning of a sequence in a model response that derives from a cited source. |
| [Title](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/citation#struct_firebase_1_1_a_i_1_1_citation_1affa336cafca29858dfe14b3caad9d1ee)           | `string` The title of the cited source, if available.                                             |
| [Uri](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/citation#struct_firebase_1_1_a_i_1_1_citation_1a5bd5fbec676c3507b0138f4b696251e4)             | `System.Uri` A link to the cited source, if available.                                            |

## Properties

### EndIndex

```c#
int Firebase::AI::Citation::EndIndex
```  
The exclusive end of a sequence in a model response that derives from a cited source.  

### License

```c#
string Firebase::AI::Citation::License
```  
The license the cited source work is distributed under, if specified.  

### PublicationDate

```c#
System.DateTime Firebase::AI::Citation::PublicationDate
```  
The publication date of the cited source, if available.  

### StartIndex

```c#
int Firebase::AI::Citation::StartIndex
```  
The inclusive beginning of a sequence in a model response that derives from a cited source.  

### Title

```c#
string Firebase::AI::Citation::Title
```  
The title of the cited source, if available.  

### Uri

```c#
System.Uri Firebase::AI::Citation::Uri
```  
A link to the cited source, if available.