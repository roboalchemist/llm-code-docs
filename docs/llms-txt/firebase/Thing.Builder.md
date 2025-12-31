# Source: https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder.md.txt

# Thing.Builder

public static class **Thing.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  

|---|---|---|
| Known Direct Subclasses [Action.Builder](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Action.Builder) |------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------| | [Action.Builder](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Action.Builder) | *This class is deprecated. Please [Migrate to the Firebase App Indexing API](https://firebase.google.com/docs/app-indexing/android/migrate)* | |||

**This class is deprecated.**   

Please [Migrate to the
Firebase App Indexing API](https://firebase.google.com/docs/app-indexing/android/migrate)  

### Public Constructor Summary

|---|----------------------------------------------------------------------------------------------------------------------------|
|   | [Builder](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder#Builder())() |

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Thing](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing)                 | [build](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder#build())() Build the [Thing](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing) object.                                                                                                                                                                |
| [Thing.Builder](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder) | [put](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder#put(java.lang.String,%20com.google.android.gms.appindexing.Thing))([String](https://developer.android.com/reference/java/lang/String.html) key, [Thing](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing) value) Sets a property of the content.        |
| [Thing.Builder](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder) | [put](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder#put(java.lang.String,%20com.google.android.gms.appindexing.Thing[]))([String](https://developer.android.com/reference/java/lang/String.html) key, [Thing\[\]](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing) values) Sets properties of the content. |
| [Thing.Builder](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder) | [put](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder#put(java.lang.String,%20java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) key, [String](https://developer.android.com/reference/java/lang/String.html) value) Sets a property of the content.                                                             |
| [Thing.Builder](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder) | [put](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder#put(java.lang.String,%20java.lang.String[]))([String](https://developer.android.com/reference/java/lang/String.html) key, [String\[\]](https://developer.android.com/reference/java/lang/String.html) values) Sets a property of the content.                                                      |
| [Thing.Builder](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder) | [put](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder#put(java.lang.String,%20boolean))([String](https://developer.android.com/reference/java/lang/String.html) key, boolean value) Sets a property of the content.                                                                                                                                      |
| [Thing.Builder](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder) | [setDescription](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder#setDescription(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) description) Sets the optional description of the content.                                                                                                                    |
| [Thing.Builder](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder) | [setId](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder#setId(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) id) Sets the optional web URL of the content.                                                                                                                                                   |
| [Thing.Builder](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder) | [setName](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder#setName(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) name) Sets the name of the content.                                                                                                                                                         |
| [Thing.Builder](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder) | [setType](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder#setType(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) type) Sets the schema.org type of the content.                                                                                                                                              |
| [Thing.Builder](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder) | [setUrl](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder#setUrl(android.net.Uri))([Uri](https://developer.android.com/reference/android/net/Uri.html) url) Sets the URL of the content in the app.                                                                                                                                                       |

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

## Public Constructors

#### public **Builder** ()

## Public Methods

#### public [Thing](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing)
**build** ()

Build the [Thing](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing)
object.  

#### public [Thing.Builder](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder)
**put** ([String](https://developer.android.com/reference/java/lang/String.html) key, [Thing](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing) value)

Sets a property of the content.  

##### Parameters

|  key  |                                                                           The schema.org property. Must not be null.                                                                            |
| value | The value of the schema.org property represented as a [Thing](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing). If null, the value will be ignored. |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### public [Thing.Builder](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder)
**put** ([String](https://developer.android.com/reference/java/lang/String.html) key, [Thing\[\]](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing) values)

Sets properties of the content.  

##### Parameters

|  key   |                                                                   The schema.org property. Must not be null.                                                                    |
| values | The array of values represented as a [Thing](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing). If null, the values will be ignored. |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### public [Thing.Builder](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder)
**put** ([String](https://developer.android.com/reference/java/lang/String.html) key, [String](https://developer.android.com/reference/java/lang/String.html) value)

Sets a property of the content.  

##### Parameters

|  key  |                The schema.org property. Must not be null.                 |
| value | The value of the schema.org property. If null, the value will be ignored. |
|-------|---------------------------------------------------------------------------|

#### public [Thing.Builder](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder)
**put** ([String](https://developer.android.com/reference/java/lang/String.html) key, [String\[\]](https://developer.android.com/reference/java/lang/String.html) values)

Sets a property of the content.  

##### Parameters

|  key   |            The schema.org property. Must not be null.            |
| values | The array of string values. If null, the values will be ignored. |
|--------|------------------------------------------------------------------|

#### public [Thing.Builder](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder)
**put** ([String](https://developer.android.com/reference/java/lang/String.html) key, boolean value)

Sets a property of the content.  

##### Parameters

|  key  | The schema.org property. Must not be null. |
| value |   The value of the schema.org property.    |
|-------|--------------------------------------------|

#### public [Thing.Builder](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder)
**setDescription** ([String](https://developer.android.com/reference/java/lang/String.html) description)

Sets the optional description of the content.  

##### Parameters

| description | The description of the content. |
|-------------|---------------------------------|

#### public [Thing.Builder](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder)
**setId** ([String](https://developer.android.com/reference/java/lang/String.html) id)

Sets the optional web URL of the content.  

##### Parameters

| id | The equivalent web url for the content. |
|----|-----------------------------------------|

#### public [Thing.Builder](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder)
**setName** ([String](https://developer.android.com/reference/java/lang/String.html) name)

Sets the name of the content.  

##### Parameters

| name | The name of the content, must not be null. For more information, visit [these guidelines](https://support.google.com/webmasters/answer/35624#3) for providing a descriptive name. |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### public [Thing.Builder](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder)
**setType** ([String](https://developer.android.com/reference/java/lang/String.html) type)

Sets the schema.org type of the content.  

##### Parameters

| type | The schema.org type of the content. |
|------|-------------------------------------|

#### public [Thing.Builder](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/Thing.Builder)
**setUrl** ([Uri](https://developer.android.com/reference/android/net/Uri.html) url)

Sets the URL of the content in the app.  

##### Parameters

| url | The app URI of the content, must not be null. The URI must either be an HTTP(S) URL, or use the [App Indexing](https://developer.android.com/training/app-indexing/enabling-app-indexing.html) format. In either case, the app calling this method needs to handle corresponding incoming Intents and take users to that content. |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|