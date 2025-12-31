# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder.md.txt

# AlarmBuilder

public final class **AlarmBuilder** extends [IndexableBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder)\<[AlarmBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder)\>  
Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)
for an alarm.  

### Constant Summary

|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|---|
| [String](https://developer.android.com/reference/java/lang/String.html) | [FRIDAY](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder#FRIDAY)       |   |
| [String](https://developer.android.com/reference/java/lang/String.html) | [MONDAY](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder#MONDAY)       |   |
| [String](https://developer.android.com/reference/java/lang/String.html) | [SATURDAY](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder#SATURDAY)   |   |
| [String](https://developer.android.com/reference/java/lang/String.html) | [SUNDAY](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder#SUNDAY)       |   |
| [String](https://developer.android.com/reference/java/lang/String.html) | [THURSDAY](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder#THURSDAY)   |   |
| [String](https://developer.android.com/reference/java/lang/String.html) | [TUESDAY](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder#TUESDAY)     |   |
| [String](https://developer.android.com/reference/java/lang/String.html) | [WEDNESDAY](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder#WEDNESDAY) |   |

### Public Method Summary

|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AlarmBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder) | [setAlarmInstances](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder#setAlarmInstances(com.google.firebase.appindexing.builders.AlarmInstanceBuilder...))([AlarmInstanceBuilder...](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder) alarmInstanceBuilders) Sets the instances, if any, associated with this alarm.                                                                                                                                                                                                                                                                                                            |
| [AlarmBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder) | [setDayOfWeek](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder#setDayOfWeek(java.lang.String...))([String...](https://developer.android.com/reference/java/lang/String.html) daysOfWeek) Sets the scheduled days for a repeating alarm.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [AlarmBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder) | [setEnabled](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder#setEnabled(boolean))(boolean enabled) Sets whether or not the alarm is currently active and has at least one associated instance in the [AlarmInstanceBuilder.SCHEDULED](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder#SCHEDULED), [AlarmInstanceBuilder.FIRED](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder#FIRED) or [AlarmInstanceBuilder.SCHEDULED](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder#SCHEDULED) state. |
| [AlarmBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder) | [setHour](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder#setHour(int))(int hour) Sets the hour that the alarm will fire.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [AlarmBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder) | [setIdentifier](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder#setIdentifier(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) identifier) Sets the immutable unique identifier of the alarm.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [AlarmBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder) | [setMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder#setMessage(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) message) Sets the custom message associated with this alarm.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [AlarmBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder) | [setMinute](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder#setMinute(int))(int minute) Sets the minute that the alarm will fire.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [AlarmBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder) | [setRingtone](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder#setRingtone(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) ringtone) Sets the ringtone to be played when the alarm fires, as a content URI of the media to be played, or [AlarmClock.VALUE_RINGTONE_SILENT](https://developer.android.com/reference/android/provider/AlarmClock.html#VALUE_RINGTONE_SILENT) if no ringtone will be played.                                                                                                                                                                                                                                           |
| [AlarmBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder) | [setVibrate](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder#setVibrate(boolean))(boolean vibrate) Sets whether or not to activate the device vibrator when the alarm fires.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

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
**FRIDAY**

Constant Value: "Friday"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**MONDAY**

Constant Value: "Monday"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**SATURDAY**

Constant Value: "Saturday"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**SUNDAY**

Constant Value: "Sunday"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**THURSDAY**

Constant Value: "Thursday"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**TUESDAY**

Constant Value: "Tuesday"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**WEDNESDAY**

Constant Value: "Wednesday"

## Public Methods

#### public [AlarmBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder)
**setAlarmInstances** ([AlarmInstanceBuilder...](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder) alarmInstanceBuilders)

Sets the instances, if any, associated with this alarm.  

#### public [AlarmBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder)
**setDayOfWeek** ([String...](https://developer.android.com/reference/java/lang/String.html) daysOfWeek)

Sets the scheduled days for a repeating alarm.  

##### Parameters

| daysOfWeek | Must be one or more of { [MONDAY](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder#MONDAY), [TUESDAY](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder#TUESDAY), [WEDNESDAY](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder#WEDNESDAY), [THURSDAY](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder#THURSDAY), [FRIDAY](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder#FRIDAY), [SATURDAY](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder#SATURDAY), [SUNDAY](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder#SUNDAY) }. |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### public [AlarmBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder)
**setEnabled** (boolean enabled)

Sets whether or not the alarm is currently active and has at least one associated
instance in the [AlarmInstanceBuilder.SCHEDULED](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder#SCHEDULED), [AlarmInstanceBuilder.FIRED](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder#FIRED) or [AlarmInstanceBuilder.SCHEDULED](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder#SCHEDULED) state.  

#### public [AlarmBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder)
**setHour** (int hour)

Sets the hour that the alarm will fire.  

##### Parameters

| hour | Must be 0-23, inclusive |
|------|-------------------------|

#### public [AlarmBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder)
**setIdentifier** ([String](https://developer.android.com/reference/java/lang/String.html) identifier)

Sets the immutable unique identifier of the alarm.  

#### public [AlarmBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder)
**setMessage** ([String](https://developer.android.com/reference/java/lang/String.html) message)

Sets the custom message associated with this alarm.  

#### public [AlarmBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder)
**setMinute** (int minute)

Sets the minute that the alarm will fire.  

##### Parameters

| minute | Must be 0-59, inclusive |
|--------|-------------------------|

#### public [AlarmBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder)
**setRingtone** ([String](https://developer.android.com/reference/java/lang/String.html) ringtone)

Sets the ringtone to be played when the alarm fires, as a content URI of the media
to be played, or [AlarmClock.VALUE_RINGTONE_SILENT](https://developer.android.com/reference/android/provider/AlarmClock.html#VALUE_RINGTONE_SILENT) if no ringtone will be played.  

#### public [AlarmBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmBuilder)
**setVibrate** (boolean vibrate)

Sets whether or not to activate the device vibrator when the alarm fires.