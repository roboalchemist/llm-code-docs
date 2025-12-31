# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder.md.txt

# IndexableBuilder

public abstract class **IndexableBuilder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  

|---|---|---|
| Known Direct Subclasses [AggregateRatingBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AggregateRatingBuilder), [AlarmBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder), [AlarmInstanceBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder), [AudiobookBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AudiobookBuilder), [BookBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/BookBuilder), [ConversationBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/ConversationBuilder), [DigitalDocumentBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/DigitalDocumentBuilder), [DigitalDocumentPermissionBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/DigitalDocumentPermissionBuilder), [GeoShapeBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/GeoShapeBuilder), [Indexable.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.Builder), and [12 others.](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#) |------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | [AggregateRatingBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AggregateRatingBuilder)                     | Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) for aggregate rating.                       | | [AlarmBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder)                                         | Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) for an alarm.                               | | [AlarmInstanceBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder)                         | Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) for an alarm instance.                      | | [AudiobookBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AudiobookBuilder)                                 | Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) for an audiobook.                           | | [BookBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/BookBuilder)                                           | Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) for a book.                                 | | [ConversationBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/ConversationBuilder)                           | Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) for a conversation.                         | | [DigitalDocumentBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/DigitalDocumentBuilder)                     | Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) for a digital document of different types.  | | [DigitalDocumentPermissionBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/DigitalDocumentPermissionBuilder) | Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) for a permission on a digital document.     | | [GeoShapeBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/GeoShapeBuilder)                                   | Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) for a geographic area described by a shape. | | [Indexable.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.Builder)                                        | The builder for [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable).                                                    | | [LocalBusinessBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/LocalBusinessBuilder)                         | Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) for a local business.                       | | [MessageBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder)                                     | Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) for a message.                              | | [MusicAlbumBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MusicAlbumBuilder)                               | Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) for a music album.                          | | [MusicGroupBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MusicGroupBuilder)                               | Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) for a music group.                          | | [MusicPlaylistBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MusicPlaylistBuilder)                         | Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) for a music playlist.                       | | [MusicRecordingBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MusicRecordingBuilder)                       | Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) for a song or other music recording.        | | [PersonBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/PersonBuilder)                                       | Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) for a person.                               | | [PhotographBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/PhotographBuilder)                               | Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) for a photo.                                | | [PlaceBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/PlaceBuilder)                                         | Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) for a place object.                         | | [PostalAddressBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/PostalAddressBuilder)                         | Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) for a postal address.                       | | [ReservationBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/ReservationBuilder)                             | Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) for a reservation.                          | | [StickerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/StickerBuilder)                                     | Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) for a sticker.                              | | [StickerPackBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/StickerPackBuilder)                             | Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) for a sticker pack.                         | | [StopwatchBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/StopwatchBuilder)                                 | Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) for a stopwatch.                            | | [StopwatchLapBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/StopwatchLapBuilder)                           | Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) for a lap.                                  | | [TimerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder)                                         | Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) for a timer.                                | | [VideoObjectBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/VideoObjectBuilder)                             | Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) for a video object.                         | |||

The basic abstract builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable).  

### Protected Constructor Summary

|---|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [IndexableBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#IndexableBuilder(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) type) Builder for a basic Indexable. |

### Public Method Summary

|-------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| final [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)                                             | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#build())() Finalize building the object.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| T                                                                                                                                                           | [put](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#put(java.lang.String,%20boolean...))([String](https://developer.android.com/reference/java/lang/String.html) key, boolean... values) Sets one or multiple boolean values for a property, replacing its previous values.                                                                                                                                                                                                                                       |
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

### Protected Method Summary

|-------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \<S extends [IndexableBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder)\<?\>\> T | [put](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder#put(java.lang.String,%20S...))([String](https://developer.android.com/reference/java/lang/String.html) key, S... values) Sets one or multiple [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) values for a property. |

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

## Protected Constructors

#### protected **IndexableBuilder** ([String](https://developer.android.com/reference/java/lang/String.html) type)

Builder for a basic Indexable.  

##### Parameters

| type | The schema.org type of the Indexable, must not be null or empty. |
|------|------------------------------------------------------------------|

## Public Methods

#### public final [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)
**build** ()

Finalize building the object. The [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)
being returned can be put into the index via the [FirebaseAppIndex](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex)
interface.  

#### public T **put** ([String](https://developer.android.com/reference/java/lang/String.html) key, boolean... values)

Sets one or multiple boolean values for a property, replacing its previous
values.  

##### Parameters

|  key   |   The schema.org property. Must not be null.   |
| values | The boolean values of the schema.org property. |
|--------|------------------------------------------------|

#### public T **put** ([String](https://developer.android.com/reference/java/lang/String.html) key, [Indexable...](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) values)

Sets one or multiple [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)
values for a property, replacing its previous values.  

##### Parameters

|  key   |                                                                                                                                                                                                       The schema.org property. Must not be null.                                                                                                                                                                                                        |
| values | The values represented as an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable). Null values are ignored. [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)s must be constructed using [Indexable.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.Builder) or convenience methods. |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Throws

| [FirebaseAppIndexingInvalidArgumentException](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndexingInvalidArgumentException) |   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|

#### public T **put** ([String](https://developer.android.com/reference/java/lang/String.html) key, [String...](https://developer.android.com/reference/java/lang/String.html) values)

Sets one or multiple string values for a property, replacing its previous
values.  

##### Parameters

|  key   |               The schema.org property. Must not be null.               |
| values | The string values of the schema.org property. Null values are ignored. |
|--------|------------------------------------------------------------------------|

#### public T **put** ([String](https://developer.android.com/reference/java/lang/String.html) key, long... values)

Sets one or multiple long values for a property, replacing its previous values.  

##### Parameters

|  key   | The schema.org property. Must not be null.  |
| values | The long values of the schema.org property. |
|--------|---------------------------------------------|

#### public T **setAlternateName** ([String...](https://developer.android.com/reference/java/lang/String.html) alternateNames)

Sets the alternate names for the content.  

#### public final T **setDescription** ([String](https://developer.android.com/reference/java/lang/String.html) description)

Sets the optional description of the content.  

##### Parameters

| description | The description of the content. |
|-------------|---------------------------------|

#### public T **setId** ([String](https://developer.android.com/reference/java/lang/String.html) id)

Sets the ID for the Indexable.  

#### public final T **setImage** ([String](https://developer.android.com/reference/java/lang/String.html) url)

Sets the image of the content.  

##### Parameters

| url | The web URL or [content URI](https://developer.android.com/guide/topics/providers/content-provider-basics.html#ContentURIs) of the image. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------|

#### public final T **setIsPartOf** (S... collections)

Sets the sub-group or collection that this Indexable is part of.  

#### public final T **setKeywords** ([String...](https://developer.android.com/reference/java/lang/String.html) keywords)

Sets the keywords of the Indexable. For example, email message can have keywords
like promotion, finance; photograph can have the keywords for people, object and the
place name where the photograph was taken.  

##### Parameters

| keywords | The keywords of the Indexable. Null values are ignored. |
|----------|---------------------------------------------------------|

#### public T **setMetadata** ([Indexable.Metadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.Metadata.Builder) metadataBuilder)

Sets the metadata. If not invoked default metadata values are applied.

May only be called once and only on top-level [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)s.  

##### Parameters

| metadataBuilder | The [Indexable.Metadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.Metadata.Builder) which builds the metadata. |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### public final T **setName** ([String](https://developer.android.com/reference/java/lang/String.html) name)

Sets the name of the content, must not be null. For more information, visit [these guidelines](https://support.google.com/webmasters/answer/35624#3) for providing a
descriptive name.  

#### public final T **setSameAs** ([String](https://developer.android.com/reference/java/lang/String.html) webUrl)

Sets the corresponding web URL. The web URL is a reference web page that
unambiguously indicates the item's identity.  

##### Parameters

| webUrl | The reference web page that unambiguously indicates the item's identity. |
|--------|--------------------------------------------------------------------------|

#### public final T **setUrl** ([String](https://developer.android.com/reference/java/lang/String.html) url)

Sets the URL. The URL must be openable by the app. This is mandatory to be set. The
URL uniquely identifies the [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)
within the app.  

##### Parameters

| url | The deep link URL which is not longer than [Indexable.MAX_URL_LENGTH](https://firebase.google.com/docs/reference/android) and openable by the app. The URL must be handled by app intent filter. Find detailed information on handling deep links [here](https://developer.android.com/training/app-links/index.html). |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Protected Methods

#### protected T **put** ([String](https://developer.android.com/reference/java/lang/String.html) key, S... values)

Sets one or multiple [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)
values for a property.  

##### Parameters

|  key   |                                                                       The schema.org property. Must not be null.                                                                        |
| values | The values represented as an [IndexableBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder). Null values are ignored. |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|