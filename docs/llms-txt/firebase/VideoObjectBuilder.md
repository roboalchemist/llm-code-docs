# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/VideoObjectBuilder.md.txt

# VideoObjectBuilder

public final class **VideoObjectBuilder** extends [IndexableBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder)\<[VideoObjectBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/VideoObjectBuilder)\>  
Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)
for a video object.

For reference, see: <https://schema.org/VideoObject>.  

### Public Method Summary

|--------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [VideoObjectBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/VideoObjectBuilder) | [setAuthor](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/VideoObjectBuilder#setAuthor(com.google.firebase.appindexing.builders.PersonBuilder))([PersonBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/PersonBuilder) author) Sets the author of the video object.                    |
| [VideoObjectBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/VideoObjectBuilder) | [setDuration](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/VideoObjectBuilder#setDuration(long))(long durationInSeconds) Sets the duration of the video object in seconds.                                                                                                                                                                |
| [VideoObjectBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/VideoObjectBuilder) | [setDurationWatched](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/VideoObjectBuilder#setDurationWatched(long))(long durationWatchedInSeconds) Sets the duration of the video object which the user has already watched in seconds.                                                                                                        |
| [VideoObjectBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/VideoObjectBuilder) | [setLocationCreated](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/VideoObjectBuilder#setLocationCreated(com.google.firebase.appindexing.builders.PlaceBuilder))([PlaceBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/PlaceBuilder) place) Sets the place where the video was taken. |
| [VideoObjectBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/VideoObjectBuilder) | [setSeriesName](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/VideoObjectBuilder#setSeriesName(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) seriesName) Sets the series name this video object belongs to.                                                                                   |
| [VideoObjectBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/VideoObjectBuilder) | [setUploadDate](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/VideoObjectBuilder#setUploadDate(java.util.Date))([Date](https://developer.android.com/reference/java/util/Date.html) uploadDate) Sets the date when this video object was uploaded.                                                                                         |

### Inherited Method Summary

From class [com.google.firebase.appindexing.builders.IndexableBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder)  

|-------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| final [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)                                             | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#build())() Finalize building the object.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| T                                                                                                                                                           | [put](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#put(java.lang.String,%20boolean...))([String](https://developer.android.com/reference/java/lang/String.html) key, boolean... values) Sets one or multiple boolean values for a property, replacing its previous values.                                                                                                                                                                                                                                       |
| \<S extends [IndexableBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder)\<?\>\> T       | [put](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#put(java.lang.String,%20S...))([String](https://developer.android.com/reference/java/lang/String.html) key, S... values) Sets one or multiple [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) values for a property.                                                                                                                                                                                |
| T                                                                                                                                                           | [put](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#put(java.lang.String,%20com.google.firebase.appindexing.Indexable...))([String](https://developer.android.com/reference/java/lang/String.html) key, [Indexable...](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) values) Sets one or multiple [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) values for a property, replacing its previous values. |
| T                                                                                                                                                           | [put](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#put(java.lang.String,%20java.lang.String...))([String](https://developer.android.com/reference/java/lang/String.html) key, [String...](https://developer.android.com/reference/java/lang/String.html) values) Sets one or multiple string values for a property, replacing its previous values.                                                                                                                                                               |
| T                                                                                                                                                           | [put](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#put(java.lang.String,%20long...))([String](https://developer.android.com/reference/java/lang/String.html) key, long... values) Sets one or multiple long values for a property, replacing its previous values.                                                                                                                                                                                                                                                |
| T                                                                                                                                                           | [setAlternateName](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#setAlternateName(java.lang.String...))([String...](https://developer.android.com/reference/java/lang/String.html) alternateNames) Sets the alternate names for the content.                                                                                                                                                                                                                                                                      |
| final T                                                                                                                                                     | [setDescription](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#setDescription(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) description) Sets the optional description of the content.                                                                                                                                                                                                                                                                               |
| T                                                                                                                                                           | [setId](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#setId(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) id) Sets the ID for the Indexable.                                                                                                                                                                                                                                                                                                                         |
| final T                                                                                                                                                     | [setImage](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#setImage(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) url) Sets the image of the content.                                                                                                                                                                                                                                                                                                                  |
| final \<S extends [IndexableBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder)\<?\>\> T | [setIsPartOf](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#setIsPartOf(S...))(S... collections) Sets the sub-group or collection that this Indexable is part of.                                                                                                                                                                                                                                                                                                                                                 |
| final T                                                                                                                                                     | [setKeywords](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#setKeywords(java.lang.String...))([String...](https://developer.android.com/reference/java/lang/String.html) keywords) Sets the keywords of the Indexable.                                                                                                                                                                                                                                                                                            |
| T                                                                                                                                                           | [setMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#setMetadata(com.google.firebase.appindexing.Indexable.Metadata.Builder))([Indexable.Metadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.Metadata.Builder) metadataBuilder) Sets the metadata.                                                                                                                                                                                              |
| final T                                                                                                                                                     | [setName](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#setName(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) name) Sets the name of the content, must not be null.                                                                                                                                                                                                                                                                                                  |
| final T                                                                                                                                                     | [setSameAs](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#setSameAs(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) webUrl) Sets the corresponding web URL.                                                                                                                                                                                                                                                                                                            |
| final T                                                                                                                                                     | [setUrl](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#setUrl(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) url) Sets the URL.                                                                                                                                                                                                                                                                                                                                       |

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

## Public Methods

#### public [VideoObjectBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/VideoObjectBuilder)
**setAuthor** ([PersonBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/PersonBuilder) author)

Sets the author of the video object.  

##### Parameters

| author | The author of the video object. |
|--------|---------------------------------|

#### public [VideoObjectBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/VideoObjectBuilder)
**setDuration** (long durationInSeconds)

Sets the duration of the video object in seconds.  

##### Parameters

| durationInSeconds | The duration of the video object in seconds. |
|-------------------|----------------------------------------------|

#### public [VideoObjectBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/VideoObjectBuilder)
**setDurationWatched** (long durationWatchedInSeconds)

Sets the duration of the video object which the user has already watched in
seconds.  

##### Parameters

| durationWatchedInSeconds | The duration of the video object which the user has already watched in seconds. The value must be less than or equal to the value used in [setDuration(long)](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/VideoObjectBuilder#setDuration(long)). |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### public [VideoObjectBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/VideoObjectBuilder)
**setLocationCreated** ([PlaceBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/PlaceBuilder) place)

Sets the place where the video was taken.  

#### public [VideoObjectBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/VideoObjectBuilder)
**setSeriesName** ([String](https://developer.android.com/reference/java/lang/String.html) seriesName)

Sets the series name this video object belongs to. The name can represent a channel
name, a subscription name or a playlist name.  

##### Parameters

| seriesName | The series name this video object belongs to. |
|------------|-----------------------------------------------|

#### public [VideoObjectBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/VideoObjectBuilder)
**setUploadDate** ([Date](https://developer.android.com/reference/java/util/Date.html) uploadDate)

Sets the date when this video object was uploaded.  

##### Parameters

| uploadDate | The date when this video object was uploaded. |
|------------|-----------------------------------------------|