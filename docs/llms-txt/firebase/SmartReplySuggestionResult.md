# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/SmartReplySuggestionResult.md.txt

# SmartReplySuggestionResult

public class **SmartReplySuggestionResult** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
**This class is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).

The suggested result from the [FirebaseSmartReply](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/FirebaseSmartReply) for the given text. It contains a list of [SmartReplySuggestion](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/SmartReplySuggestion)s.  

### Nested Class Summary

|------------|---|---|-----------------------------------------------------------------|
| @interface | [SmartReplySuggestionResult.Status](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/SmartReplySuggestionResult.Status) || All possible status codes for a Smart Reply suggestion attempt. |

### Constant Summary

|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| int | [STATUS_NOT_SUPPORTED_LANGUAGE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/SmartReplySuggestionResult#STATUS_NOT_SUPPORTED_LANGUAGE) | The Smart Reply model currently doesn't support the language used in the conversation. |
| int | [STATUS_NO_REPLY](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/SmartReplySuggestionResult#STATUS_NO_REPLY)                             | The Smart Reply model cannot determine an applicable reply.                            |
| int | [STATUS_SUCCESS](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/SmartReplySuggestionResult#STATUS_SUCCESS)                               | The Smart Reply model successfully generated (1-3) replies for you.                    |

### Public Method Summary

|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| int                                                                                                                                                                                                                      | [getStatus](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/SmartReplySuggestionResult#getStatus())() Gets the status of the Smart Reply suggestion result.             |
| [List](https://developer.android.com/reference/java/util/List.html)\<[SmartReplySuggestion](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/SmartReplySuggestion)\> | [getSuggestions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/SmartReplySuggestionResult#getSuggestions())() A list of the predicted responses sorted by confidence. |
| [String](https://developer.android.com/reference/java/lang/String.html)                                                                                                                                                  | [toString](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/SmartReplySuggestionResult#toString())()                                                                     |

### Inherited Method Summary

From class java.lang.Object  

|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [Object](https://developer.android.com/reference/java/lang/Object.html)          | clone()                                                                              |
| boolean                                                                          | equals([Object](https://developer.android.com/reference/java/lang/Object.html) arg0) |
| void                                                                             | finalize()                                                                           |
| final [Class](https://developer.android.com/reference/java/lang/Class.html)\<?\> | getClass()                                                                           |
| int                                                                              | hashCode()                                                                           |
| final void                                                                       | notify()                                                                             |
| final void                                                                       | notifyAll()                                                                          |
| [String](https://developer.android.com/reference/java/lang/String.html)          | toString()                                                                           |
| final void                                                                       | wait(long arg0, int arg1)                                                            |
| final void                                                                       | wait(long arg0)                                                                      |
| final void                                                                       | wait()                                                                               |

## Constants

#### public static final int
**STATUS_NOT_SUPPORTED_LANGUAGE**

The Smart Reply model currently doesn't support the language used in the
conversation.  
Constant Value: 101  

#### public static final int
**STATUS_NO_REPLY**

The Smart Reply model cannot determine an applicable reply.  
Constant Value: 200  

#### public static final int
**STATUS_SUCCESS**

The Smart Reply model successfully generated (1-3) replies for you.  
Constant Value: 0

## Public Methods

#### public int **getStatus** ()

Gets the status of the Smart Reply suggestion result.

Possible values are:

- [STATUS_SUCCESS](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/SmartReplySuggestionResult#STATUS_SUCCESS) and you can expect up to three suggestions in [getSuggestions()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/SmartReplySuggestionResult#getSuggestions()) in this case.
- [STATUS_NOT_SUPPORTED_LANGUAGE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/SmartReplySuggestionResult#STATUS_NOT_SUPPORTED_LANGUAGE) when the language used in the conversation is not supported by the Smart Reply model.
- [STATUS_NO_REPLY](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/SmartReplySuggestionResult#STATUS_NO_REPLY) when the Smart Reply model cannot determine an applicable reply.  

#### public [List](https://developer.android.com/reference/java/util/List.html)\<[SmartReplySuggestion](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/SmartReplySuggestion)\>
**getSuggestions** ()

A list of the predicted responses sorted by confidence.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **toString** ()