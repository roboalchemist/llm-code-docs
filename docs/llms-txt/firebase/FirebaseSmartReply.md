# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/text/FirebaseSmartReply.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/FirebaseSmartReply.md.txt

# FirebaseSmartReply

public class **FirebaseSmartReply** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
implements [Closeable](https://developer.android.com/reference/java/io/Closeable.html)  
**This class is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).

Entry class for Firebase Smart Reply, which automatically suggests meaningful replies to a
user input message.  

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                                                                                                                                                                                                                                                            | [close](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/FirebaseSmartReply#close())() Closes the underlying resources including models used for reply inference.                                                                                                                                                                                                                                                                                                                              |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[SmartReplySuggestionResult](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/SmartReplySuggestionResult)\> | [suggestReplies](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/FirebaseSmartReply#suggestReplies(java.util.List<com.google.firebase.ml.naturallanguage.smartreply.FirebaseTextMessage>))([List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseTextMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/FirebaseTextMessage)\> textMessages) Returns suggested meaningful replies to a user input message. |

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

From interface java.io.Closeable  

|---------------|---------|
| abstract void | close() |

From interface java.lang.AutoCloseable  

|---------------|---------|
| abstract void | close() |

## Public Methods

#### public void **close** ()

Closes the underlying resources including models used for reply inference.  

##### Throws

| [IOException](https://developer.android.com/reference/java/io/IOException.html) |   |
|---------------------------------------------------------------------------------|---|

#### public [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)\<[SmartReplySuggestionResult](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/SmartReplySuggestionResult)\>
**suggestReplies** ([List](https://developer.android.com/reference/java/util/List.html)\<[FirebaseTextMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/FirebaseTextMessage)\> textMessages)

Returns suggested meaningful replies to a user input message.

Right now, English is the only supported language.  

##### Parameters

| textMessages | A list of messages from which the API generates smart replies. The messages list should contain most recent conversation context for all users participating in the conversation in chronological order. Internally, SmartReply considers the last N messages (N changes with model) to generate the best reply suggestions. |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- A [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) that asynchronously returns a [SmartReplySuggestionResult](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/SmartReplySuggestionResult) which contains a list of [SmartReplySuggestion](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/naturallanguage/smartreply/SmartReplySuggestion)s. All the replies are sorted by an internal confidence value (highest to lowest).