# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder.md.txt

# TimerBuilder

public final class **TimerBuilder** extends [IndexableBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder)\<[TimerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder)\>  
Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)
for a timer.  

### Constant Summary

|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| [String](https://developer.android.com/reference/java/lang/String.html) | [EXPIRED](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder#EXPIRED) | The timer is expired.                    |
| [String](https://developer.android.com/reference/java/lang/String.html) | [MISSED](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder#MISSED)   | The timer is missed.                     |
| [String](https://developer.android.com/reference/java/lang/String.html) | [PAUSED](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder#PAUSED)   | The timer is paused.                     |
| [String](https://developer.android.com/reference/java/lang/String.html) | [RESET](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder#RESET)     | The timer is reset to its initial value. |
| [String](https://developer.android.com/reference/java/lang/String.html) | [STARTED](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder#STARTED) | The timer is started.                    |
| [String](https://developer.android.com/reference/java/lang/String.html) | [UNKNOWN](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder#UNKNOWN) | The timer is in an unknown error state.  |

### Public Method Summary

|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [TimerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder) | [setExpireTime](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder#setExpireTime(java.util.Calendar))([Calendar](https://developer.android.com/reference/java/util/Calendar.html) wallClockExpirationTime) Sets the wall clock time at which the timer will, or did, expire.                                                                                                                                                                              |
| [TimerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder) | [setIdentifier](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder#setIdentifier(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) identifier) Sets the immutable unique identifier of the timer.                                                                                                                                                                                                                |
| [TimerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder) | [setLength](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder#setLength(long))(long lengthInMilliseconds) Sets the total length of the timer when it was created, in milliseconds.                                                                                                                                                                                                                                                                       |
| [TimerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder) | [setMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder#setMessage(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) message) Sets the custom message associated with this timer.                                                                                                                                                                                                                        |
| [TimerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder) | [setRemainingTime](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder#setRemainingTime(long))(long remainingTimeInMilliseconds) Sets the amount of time remaining when the timer was started or stopped, in milliseconds.                                                                                                                                                                                                                                 |
| [TimerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder) | [setRingtone](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder#setRingtone(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) ringtone) Sets the ringtone to be played when the timer expires, as a content URI of the media to be played, or [AlarmClock.VALUE_RINGTONE_SILENT](https://developer.android.com/reference/android/provider/AlarmClock.html#VALUE_RINGTONE_SILENT) if no ringtone will be played. |
| [TimerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder) | [setTimerStatus](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder#setTimerStatus(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) status) Sets the current status of the timer.                                                                                                                                                                                                                               |
| [TimerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder) | [setVibrate](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder#setVibrate(boolean))(boolean vibrate) Sets whether or not to activate the device vibrator when the timer expires.                                                                                                                                                                                                                                                                         |

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

## Constants

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**EXPIRED**

The timer is expired.  
Constant Value: "Expired"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**MISSED**

The timer is missed.  
Constant Value: "Missed"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**PAUSED**

The timer is paused.  
Constant Value: "Paused"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**RESET**

The timer is reset to its initial value.  
Constant Value: "Reset"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**STARTED**

The timer is started.  
Constant Value: "Started"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**UNKNOWN**

The timer is in an unknown error state.  
Constant Value: "Unknown"

## Public Methods

#### public [TimerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder)
**setExpireTime** ([Calendar](https://developer.android.com/reference/java/util/Calendar.html) wallClockExpirationTime)

Sets the wall clock time at which the timer will, or did, expire.  

#### public [TimerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder)
**setIdentifier** ([String](https://developer.android.com/reference/java/lang/String.html) identifier)

Sets the immutable unique identifier of the timer.  

#### public [TimerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder)
**setLength** (long lengthInMilliseconds)

Sets the total length of the timer when it was created, in milliseconds.  

#### public [TimerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder)
**setMessage** ([String](https://developer.android.com/reference/java/lang/String.html) message)

Sets the custom message associated with this timer.  

#### public [TimerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder)
**setRemainingTime** (long remainingTimeInMilliseconds)

Sets the amount of time remaining when the timer was started or stopped, in
milliseconds.  

#### public [TimerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder)
**setRingtone** ([String](https://developer.android.com/reference/java/lang/String.html) ringtone)

Sets the ringtone to be played when the timer expires, as a content URI of the media
to be played, or [AlarmClock.VALUE_RINGTONE_SILENT](https://developer.android.com/reference/android/provider/AlarmClock.html#VALUE_RINGTONE_SILENT) if no ringtone will be played.  

#### public [TimerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder)
**setTimerStatus** ([String](https://developer.android.com/reference/java/lang/String.html) status)

Sets the current status of the timer.  

##### Parameters

| status | Must be one of { [STARTED](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder#STARTED), [PAUSED](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder#PAUSED), [EXPIRED](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder#EXPIRED), [MISSED](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder#MISSED), [RESET](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder#RESET), [UNKNOWN](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder#UNKNOWN) }. |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### public [TimerBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/TimerBuilder)
**setVibrate** (boolean vibrate)

Sets whether or not to activate the device vibrator when the timer expires.