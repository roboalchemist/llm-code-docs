# Source: https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Action.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder.md.txt

# Action.Builder

public static class **Action.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  

|---|---|---|
| Known Direct Subclasses [AssistActionBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AssistActionBuilder) |----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------| | [AssistActionBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AssistActionBuilder) | Constructs an action to report completion of the Action triggered from Assistant. | |||

The builder for [Action](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action).  

### Constant Summary

|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [String](https://developer.android.com/reference/java/lang/String.html) | [ACTIVATE_ACTION](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#ACTIVATE_ACTION)             | The act of starting or activating something.                                                                  |
| [String](https://developer.android.com/reference/java/lang/String.html) | [ADD_ACTION](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#ADD_ACTION)                       | The act of editing by adding something to a collection (e.g. an item to a shopping cart or movie to a queue). |
| [String](https://developer.android.com/reference/java/lang/String.html) | [BOOKMARK_ACTION](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#BOOKMARK_ACTION)             | The act of bookmarking something (e.g. an article or song).                                                   |
| [String](https://developer.android.com/reference/java/lang/String.html) | [COMMENT_ACTION](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#COMMENT_ACTION)               | The act of commenting on something (e.g. an article or social media post).                                    |
| [String](https://developer.android.com/reference/java/lang/String.html) | [LIKE_ACTION](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#LIKE_ACTION)                     | The act of liking something (e.g. a book, song or article).                                                   |
| [String](https://developer.android.com/reference/java/lang/String.html) | [LISTEN_ACTION](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#LISTEN_ACTION)                 | The act of listening to something (e.g. music or a podcast).                                                  |
| [String](https://developer.android.com/reference/java/lang/String.html) | [SEND_ACTION](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#SEND_ACTION)                     | The act of sending a message.                                                                                 |
| [String](https://developer.android.com/reference/java/lang/String.html) | [SHARE_ACTION](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#SHARE_ACTION)                   | The act of sharing something (e.g. a document or social media post)                                           |
| [String](https://developer.android.com/reference/java/lang/String.html) | [STATUS_TYPE_ACTIVE](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#STATUS_TYPE_ACTIVE)       | The status of an active action (i.e. an action that has started but not yet completed).                       |
| [String](https://developer.android.com/reference/java/lang/String.html) | [STATUS_TYPE_COMPLETED](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#STATUS_TYPE_COMPLETED) | The status of a completed action.                                                                             |
| [String](https://developer.android.com/reference/java/lang/String.html) | [STATUS_TYPE_FAILED](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#STATUS_TYPE_FAILED)       | The status of a failed action.                                                                                |
| [String](https://developer.android.com/reference/java/lang/String.html) | [VIEW_ACTION](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#VIEW_ACTION)                     | The act of viewing something (e.g. an article or profile).                                                    |
| [String](https://developer.android.com/reference/java/lang/String.html) | [WATCH_ACTION](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#WATCH_ACTION)                   | The act of watching something (e.g. a video, movie or TV show).                                               |

### Public Constructor Summary

|---|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#Builder(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) type) The constructor. |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Action](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action)                       | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#build())() Builds the action.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Action.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder)       | [put](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#put(java.lang.String,%20double...))([String](https://developer.android.com/reference/java/lang/String.html) key, double... values) Sets one or multiple double values for a property, replacing its previous values.                                                                                                                                                                                                                                          |
| [Action.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder)       | [put](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#put(java.lang.String,%20boolean...))([String](https://developer.android.com/reference/java/lang/String.html) key, boolean... values) Sets one or multiple boolean values for a property, replacing its previous values.                                                                                                                                                                                                                                       |
| [Action.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder)       | [put](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#put(java.lang.String,%20com.google.firebase.appindexing.Indexable...))([String](https://developer.android.com/reference/java/lang/String.html) key, [Indexable...](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) values) Sets one or multiple [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) values for a property, replacing its previous values. |
| [Action.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder)       | [put](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#put(java.lang.String,%20java.lang.String...))([String](https://developer.android.com/reference/java/lang/String.html) key, [String...](https://developer.android.com/reference/java/lang/String.html) values) Sets one or multiple string values for a property, replacing its previous values.                                                                                                                                                               |
| [Action.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder)       | [put](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#put(java.lang.String,%20long...))([String](https://developer.android.com/reference/java/lang/String.html) key, long... values) Sets one or multiple long values for a property, replacing its previous values.                                                                                                                                                                                                                                                |
| [Action.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder)       | [setActionStatus](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#setActionStatus(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) actionStatus) Sets the status of the action.                                                                                                                                                                                                                                                                                           |
| [Action.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder)       | [setMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#setMetadata(com.google.firebase.appindexing.Action.Metadata.Builder))([Action.Metadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Metadata.Builder) metadataBuilder) Sets the metadata for this action.                                                                                                                                                                                       |
| final [Action.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder) | [setName](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#setName(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) name) Sets the name of the action (e.g. Ride using Waymo LLC).                                                                                                                                                                                                                                                                                         |
| [Action.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder)       | [setObject](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#setObject(java.lang.String,%20java.lang.String,%20java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) name, [String](https://developer.android.com/reference/java/lang/String.html) url, [String](https://developer.android.com/reference/java/lang/String.html) webUrl) Sets the object that the action is taken on (e.g. the article being viewed, or the song being listened to).                             |
| [Action.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder)       | [setObject](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#setObject(java.lang.String,%20java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) name, [String](https://developer.android.com/reference/java/lang/String.html) url) Sets the object that the action is taken on (e.g. the article being viewed, or the song being listened to).                                                                                                                                 |
| [Action.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder)       | [setResult](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#setResult(com.google.firebase.appindexing.Indexable...))([Indexable...](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) values) Sets the result of the action.                                                                                                                                                                                                                                            |
| final [Action.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder) | [setUrl](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder#setUrl(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) url) Sets the URL of the action.                                                                                                                                                                                                                                                                                                                         |

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

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**ACTIVATE_ACTION**

The act of starting or activating something.  
Constant Value: "ActivateAction"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**ADD_ACTION**

The act of editing by adding something to a collection (e.g. an item to a
shopping cart or movie to a queue).  
Constant Value: "AddAction"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**BOOKMARK_ACTION**

The act of bookmarking something (e.g. an article or song).  
Constant Value: "BookmarkAction"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**COMMENT_ACTION**

The act of commenting on something (e.g. an article or social media post).  
Constant Value: "CommentAction"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**LIKE_ACTION**

The act of liking something (e.g. a book, song or article).  
Constant Value: "LikeAction"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**LISTEN_ACTION**

The act of listening to something (e.g. music or a podcast).  
Constant Value: "ListenAction"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**SEND_ACTION**

The act of sending a message.  
Constant Value: "SendAction"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**SHARE_ACTION**

The act of sharing something (e.g. a document or social media post)  
Constant Value: "ShareAction"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**STATUS_TYPE_ACTIVE**

The status of an active action (i.e. an action that has started but not yet
completed).  
Constant Value: "//schema.org/ActiveActionStatus"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**STATUS_TYPE_COMPLETED**

The status of a completed action.  
Constant Value: "//schema.org/CompletedActionStatus"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**STATUS_TYPE_FAILED**

The status of a failed action.  
Constant Value: "//schema.org/FailedActionStatus"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**VIEW_ACTION**

The act of viewing something (e.g. an article or profile).  
Constant Value: "ViewAction"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**WATCH_ACTION**

The act of watching something (e.g. a video, movie or TV show).  
Constant Value: "WatchAction"

## Public Constructors

#### public **Builder** ([String](https://developer.android.com/reference/java/lang/String.html) type)

The constructor.  

##### Parameters

| type | The Schema.org type best describing this action (use one of the constants on this class, or refer to <https://schema.org/Action> for a list of standard action types). |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Public Methods

#### public [Action](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action)
**build** ()

Builds the action.  

#### public [Action.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder)
**put** ([String](https://developer.android.com/reference/java/lang/String.html) key, double... values)

Sets one or multiple double values for a property, replacing its previous
values.  

##### Parameters

|  key   |  The property. Must not be null.   |
| values | The double values of the property. |
|--------|------------------------------------|

#### public [Action.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder)
**put** ([String](https://developer.android.com/reference/java/lang/String.html) key, boolean... values)

Sets one or multiple boolean values for a property, replacing its previous
values.  

##### Parameters

|  key   |   The property. Must not be null.   |
| values | The boolean values of the property. |
|--------|-------------------------------------|

#### public [Action.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder)
**put** ([String](https://developer.android.com/reference/java/lang/String.html) key, [Indexable...](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) values)

Sets one or multiple [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)
values for a property, replacing its previous values.  

##### Parameters

|  key   |                                                                                                                                                                                                       The schema.org property. Must not be null.                                                                                                                                                                                                        |
| values | The values represented as an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable). Null values are ignored. [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)s must be constructed using [Indexable.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.Builder) or convenience methods. |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Throws

| [FirebaseAppIndexingInvalidArgumentException](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndexingInvalidArgumentException) |   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|

#### public [Action.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder)
**put** ([String](https://developer.android.com/reference/java/lang/String.html) key, [String...](https://developer.android.com/reference/java/lang/String.html) values)

Sets one or multiple string values for a property, replacing its previous
values.  

##### Parameters

|  key   |               The property. Must not be null.               |
| values | The string values of the property. Null values are ignored. |
|--------|-------------------------------------------------------------|

#### public [Action.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder)
**put** ([String](https://developer.android.com/reference/java/lang/String.html) key, long... values)

Sets one or multiple long values for a property, replacing its previous values.  

##### Parameters

|  key   | The property. Must not be null.  |
| values | The long values of the property. |
|--------|----------------------------------|

#### public [Action.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder)
**setActionStatus** ([String](https://developer.android.com/reference/java/lang/String.html) actionStatus)

Sets the status of the action. Optional.  

#### public [Action.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder)
**setMetadata** ([Action.Metadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Metadata.Builder) metadataBuilder)

Sets the metadata for this action. Optional.  

#### public final [Action.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder)
**setName** ([String](https://developer.android.com/reference/java/lang/String.html) name)

Sets the name of the action (e.g. Ride using Waymo LLC).  

#### public [Action.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder)
**setObject** ([String](https://developer.android.com/reference/java/lang/String.html) name, [String](https://developer.android.com/reference/java/lang/String.html) url, [String](https://developer.android.com/reference/java/lang/String.html) webUrl)

Sets the object that the action is taken on (e.g. the article being viewed, or
the song being listened to).  

##### Parameters

|  name  |                The name of the object (e.g. the title of an article, or name of a song). Must not be null.                |
|  url   | The URL of the object (this URL needs to be handled by the app to take the user to the right place). Must be a valid URL. |
| webUrl |                         The web URL of the object, if different from `url`. Must be a valid URL.                          |
|--------|---------------------------------------------------------------------------------------------------------------------------|

#### public [Action.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder)
**setObject** ([String](https://developer.android.com/reference/java/lang/String.html) name, [String](https://developer.android.com/reference/java/lang/String.html) url)

Sets the object that the action is taken on (e.g. the article being viewed, or
the song being listened to).  

##### Parameters

| name |                The name of the object (e.g. the title of an article, or name of a song). Must not be null.                |
| url  | The URL of the object (this URL needs to be handled by the app to take the user to the right place). Must be a valid URL. |
|------|---------------------------------------------------------------------------------------------------------------------------|

#### public [Action.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder)
**setResult** ([Indexable...](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) values)

Sets the result of the action. Optional.  

##### Parameters

| values | Results of performing the action. |
|--------|-----------------------------------|

##### Throws

| [FirebaseAppIndexingInvalidArgumentException](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndexingInvalidArgumentException) |   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|

#### public final [Action.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Builder)
**setUrl** ([String](https://developer.android.com/reference/java/lang/String.html) url)

Sets the URL of the action.

Must match Object URL when both are set.  

##### Parameters

| url | The URL to start an activity to (re)perform the action. Must be a valid URL. |
|-----|------------------------------------------------------------------------------|