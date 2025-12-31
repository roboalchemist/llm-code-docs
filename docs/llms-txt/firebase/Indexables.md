# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables.md.txt

# Indexables

public final class **Indexables** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Provides convenience methods to construct [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)s
for common data types.  

### Public Method Summary

|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static [AggregateRatingBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AggregateRatingBuilder)                     | [aggregateRatingBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#aggregateRatingBuilder())() Returns a builder for an aggregate rating.                                                                                                                                                                                                                                                                                  |
| static [AlarmBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder)                                         | [alarmBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#alarmBuilder())() Returns a builder for an alarm.                                                                                                                                                                                                                                                                                                                 |
| static [AlarmInstanceBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder)                         | [alarmInstanceBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#alarmInstanceBuilder())() Returns a builder for an alarm instance.                                                                                                                                                                                                                                                                                        |
| static [AudiobookBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AudiobookBuilder)                                 | [audiobookBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#audiobookBuilder())() Returns a builder for an audiobook.                                                                                                                                                                                                                                                                                                     |
| static [BookBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/BookBuilder)                                           | [bookBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#bookBuilder())() Returns a builder for a book.                                                                                                                                                                                                                                                                                                                     |
| static [ConversationBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/ConversationBuilder)                           | [conversationBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#conversationBuilder())() Returns a builder for a conversation.                                                                                                                                                                                                                                                                                             |
| static [DigitalDocumentBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/DigitalDocumentBuilder)                     | [digitalDocumentBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#digitalDocumentBuilder())() Returns a builder for a generic digital document.                                                                                                                                                                                                                                                                           |
| static [DigitalDocumentPermissionBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/DigitalDocumentPermissionBuilder) | [digitalDocumentPermissionBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#digitalDocumentPermissionBuilder())() Returns a builder for a digital document permission.                                                                                                                                                                                                                                                    |
| static [MessageBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder)                                     | [emailMessageBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#emailMessageBuilder())() Returns a builder for an email message.                                                                                                                                                                                                                                                                                           |
| static [GeoShapeBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/GeoShapeBuilder)                                   | [geoShapeBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#geoShapeBuilder())() Returns a builder for a geo area describe by a shape.                                                                                                                                                                                                                                                                                     |
| static [LocalBusinessBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/LocalBusinessBuilder)                         | [localBusinessBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#localBusinessBuilder())() Returns a builder for a local business.                                                                                                                                                                                                                                                                                         |
| static [MessageBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder)                                     | [messageBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#messageBuilder())() Returns a builder for a generic message.                                                                                                                                                                                                                                                                                                    |
| static [MusicAlbumBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MusicAlbumBuilder)                               | [musicAlbumBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#musicAlbumBuilder())() Returns a builder for a music album.                                                                                                                                                                                                                                                                                                  |
| static [MusicGroupBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MusicGroupBuilder)                               | [musicGroupBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#musicGroupBuilder())() Returns a builder for a music group.                                                                                                                                                                                                                                                                                                  |
| static [MusicPlaylistBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MusicPlaylistBuilder)                         | [musicPlaylistBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#musicPlaylistBuilder())() Returns a builder for a music playlist.                                                                                                                                                                                                                                                                                         |
| static [MusicRecordingBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MusicRecordingBuilder)                       | [musicRecordingBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#musicRecordingBuilder())() Returns a builder for a song or other music recording.                                                                                                                                                                                                                                                                        |
| static [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)                                                        | [newSimple](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#newSimple(java.lang.String,%20java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) name, [String](https://developer.android.com/reference/java/lang/String.html) url) Constructs a generic [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) with just a name and URL. |
| static [DigitalDocumentBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/DigitalDocumentBuilder)                     | [noteDigitalDocumentBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#noteDigitalDocumentBuilder())() Returns a builder for a note.                                                                                                                                                                                                                                                                                       |
| static [PersonBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/PersonBuilder)                                       | [personBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#personBuilder())() Returns a builder for a person.                                                                                                                                                                                                                                                                                                               |
| static [PlaceBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/PlaceBuilder)                                         | [placeBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#placeBuilder())() Returns a builder for a place.                                                                                                                                                                                                                                                                                                                  |
| static [PostalAddressBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/PostalAddressBuilder)                         | [postalAddressBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#postalAddressBuilder())() Returns a builder for a postal address.                                                                                                                                                                                                                                                                                         |
| static [DigitalDocumentBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/DigitalDocumentBuilder)                     | [presentationDigitalDocumentBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#presentationDigitalDocumentBuilder())() Returns a builder for a presentation digital document.                                                                                                                                                                                                                                              |
| static [ReservationBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/ReservationBuilder)                             | [reservationBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#reservationBuilder())() Returns a builder for a reservation.                                                                                                                                                                                                                                                                                                |
| static [LocalBusinessBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/LocalBusinessBuilder)                         | [restaurantBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#restaurantBuilder())() Returns a builder for a restaurant.                                                                                                                                                                                                                                                                                                   |
| static [DigitalDocumentBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/DigitalDocumentBuilder)                     | [spreadsheetDigitalDocumentBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#spreadsheetDigitalDocumentBuilder())() Returns a builder for a spreadsheet digital document.                                                                                                                                                                                                                                                 |
| static [StickerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/StickerBuilder)                                     | [stickerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#stickerBuilder())() Returns a builder for a sticker.                                                                                                                                                                                                                                                                                                            |
| static [StickerPackBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/StickerPackBuilder)                             | [stickerPackBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#stickerPackBuilder())() Returns a builder for a sticker pack.                                                                                                                                                                                                                                                                                               |
| static [StopwatchBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/StopwatchBuilder)                                 | [stopwatchBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#stopwatchBuilder())() Returns a builder for a stopwatch.                                                                                                                                                                                                                                                                                                      |
| static [StopwatchLapBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/StopwatchLapBuilder)                           | [stopwatchLapBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#stopwatchLapBuilder())() Returns a builder for a stopwatch lap.                                                                                                                                                                                                                                                                                            |
| static [DigitalDocumentBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/DigitalDocumentBuilder)                     | [textDigitalDocumentBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#textDigitalDocumentBuilder())() Returns a builder for a text digital document.                                                                                                                                                                                                                                                                      |
| static [TimerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder)                                         | [timerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables#timerBuilder())() Returns a builder for a timer.                                                                                                                                                                                                                                                                                                                  |

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

## Public Methods

#### public static [AggregateRatingBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AggregateRatingBuilder) **aggregateRatingBuilder** ()

Returns a builder for an aggregate rating.

The aggregate rating builder can only be used as a parameter of other builders.

Refer to [AggregateRatingBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AggregateRatingBuilder) for details.  

#### public static [AlarmBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder)
**alarmBuilder** ()

Returns a builder for an alarm.

Refer to [AlarmBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder)
for details.  

#### public static [AlarmInstanceBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder) **alarmInstanceBuilder** ()

Returns a builder for an alarm instance.

Refer to [AlarmInstanceBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder) for details.  

#### public static [AudiobookBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AudiobookBuilder)
**audiobookBuilder** ()

Returns a builder for an audiobook.

Refer to [AudiobookBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AudiobookBuilder) for details.  

#### public static [BookBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/BookBuilder)
**bookBuilder** ()

Returns a builder for a book.

Refer to [BookBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/BookBuilder)
for details.  

#### public static [ConversationBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/ConversationBuilder) **conversationBuilder** ()

Returns a builder for a conversation.

Refer to [ConversationBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/ConversationBuilder) for details.  

#### public static [DigitalDocumentBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/DigitalDocumentBuilder) **digitalDocumentBuilder** ()

Returns a builder for a generic digital document.

Refer to [DigitalDocumentBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/DigitalDocumentBuilder) for details.  

#### public static [DigitalDocumentPermissionBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/DigitalDocumentPermissionBuilder) **digitalDocumentPermissionBuilder** ()

Returns a builder for a digital document permission.

Refer to [DigitalDocumentPermissionBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/DigitalDocumentPermissionBuilder) for details.  

#### public static [MessageBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder)
**emailMessageBuilder** ()

Returns a builder for an email message.

Refer to [MessageBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder)
for details.  

#### public static [GeoShapeBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/GeoShapeBuilder)
**geoShapeBuilder** ()

Returns a builder for a geo area describe by a shape.

Refer to [GeoShapeBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/GeoShapeBuilder) for details.  

#### public static [LocalBusinessBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/LocalBusinessBuilder) **localBusinessBuilder** ()

Returns a builder for a local business.

Refer to [LocalBusinessBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/LocalBusinessBuilder) for details.  

#### public static [MessageBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder)
**messageBuilder** ()

Returns a builder for a generic message.

Refer to [MessageBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MessageBuilder)
for details.  

#### public static [MusicAlbumBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MusicAlbumBuilder)
**musicAlbumBuilder** ()

Returns a builder for a music album.

Refer to [MusicAlbumBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MusicAlbumBuilder) for details.  

#### public static [MusicGroupBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MusicGroupBuilder)
**musicGroupBuilder** ()

Returns a builder for a music group.

Refer to [MusicGroupBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MusicGroupBuilder) for details.  

#### public static [MusicPlaylistBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MusicPlaylistBuilder) **musicPlaylistBuilder** ()

Returns a builder for a music playlist.

Refer to [MusicPlaylistBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MusicPlaylistBuilder) for details.  

#### public static [MusicRecordingBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MusicRecordingBuilder) **musicRecordingBuilder** ()

Returns a builder for a song or other music recording.

Refer to [MusicRecordingBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/MusicRecordingBuilder) for details.  

#### public static [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)
**newSimple** ([String](https://developer.android.com/reference/java/lang/String.html) name, [String](https://developer.android.com/reference/java/lang/String.html) url)

Constructs a generic [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)
with just a name and URL.

Refer to classes in the [com.google.firebase.appindexing.builders](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/package-summary) package for details.  

##### Parameters

| name |  The name of the [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable), must not be null.  |
| url  | The URL of the [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable), must be a valid URL. |
|------|------------------------------------------------------------------------------------------------------------------------------------------------|

#### public static [DigitalDocumentBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/DigitalDocumentBuilder) **noteDigitalDocumentBuilder** ()

Returns a builder for a note.

Refer to [DigitalDocumentBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/DigitalDocumentBuilder) for details.  

#### public static [PersonBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/PersonBuilder)
**personBuilder** ()

Returns a builder for a person.

Refer to [PersonBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/PersonBuilder)
for details.  

#### public static [PlaceBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/PlaceBuilder)
**placeBuilder** ()

Returns a builder for a place.

Refer to [PlaceBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/PlaceBuilder)
for details.  

#### public static [PostalAddressBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/PostalAddressBuilder) **postalAddressBuilder** ()

Returns a builder for a postal address.

The postal address builder can only be used as a parameter of other builders.

Refer to [PostalAddressBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/PostalAddressBuilder) for details.  

#### public static [DigitalDocumentBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/DigitalDocumentBuilder) **presentationDigitalDocumentBuilder** ()

Returns a builder for a presentation digital document.

Refer to [DigitalDocumentBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/DigitalDocumentBuilder) for details.  

#### public static [ReservationBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/ReservationBuilder)
**reservationBuilder** ()

Returns a builder for a reservation.

Refer to [ReservationBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/ReservationBuilder) for details.  

#### public static [LocalBusinessBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/LocalBusinessBuilder) **restaurantBuilder** ()

Returns a builder for a restaurant.

Refer to [LocalBusinessBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/LocalBusinessBuilder) for details.  

#### public static [DigitalDocumentBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/DigitalDocumentBuilder) **spreadsheetDigitalDocumentBuilder** ()

Returns a builder for a spreadsheet digital document.

Refer to [DigitalDocumentBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/DigitalDocumentBuilder) for details.  

#### public static [StickerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/StickerBuilder)
**stickerBuilder** ()

Returns a builder for a sticker.

Refer to [StickerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/StickerBuilder)
for details.  

#### public static [StickerPackBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/StickerPackBuilder)
**stickerPackBuilder** ()

Returns a builder for a sticker pack.

Refer to [StickerPackBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/StickerPackBuilder) for details.  

#### public static [StopwatchBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/StopwatchBuilder)
**stopwatchBuilder** ()

Returns a builder for a stopwatch.

Refer to [StopwatchBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/StopwatchBuilder) for details.  

#### public static [StopwatchLapBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/StopwatchLapBuilder) **stopwatchLapBuilder** ()

Returns a builder for a stopwatch lap.

Refer to [StopwatchLapBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/StopwatchLapBuilder) for details.  

#### public static [DigitalDocumentBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/DigitalDocumentBuilder) **textDigitalDocumentBuilder** ()

Returns a builder for a text digital document.

Refer to [DigitalDocumentBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/DigitalDocumentBuilder) for details.  

#### public static [TimerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder)
**timerBuilder** ()

Returns a builder for a timer.

Refer to [TimerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder)
for details.