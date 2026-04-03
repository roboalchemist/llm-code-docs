# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder.md.txt

# AlarmInstanceBuilder

public class **AlarmInstanceBuilder** extends [IndexableBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/IndexableBuilder)\<[AlarmInstanceBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder)\>  
Builder to construct an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)
for an alarm instance.  

### Constant Summary

|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| [String](https://developer.android.com/reference/java/lang/String.html) | [DISMISSED](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder#DISMISSED) | The alarm has been dismissed.                               |
| [String](https://developer.android.com/reference/java/lang/String.html) | [FIRED](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder#FIRED)         | The alarm has fired.                                        |
| [String](https://developer.android.com/reference/java/lang/String.html) | [MISSED](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder#MISSED)       | The alarm has been missed.                                  |
| [String](https://developer.android.com/reference/java/lang/String.html) | [SCHEDULED](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder#SCHEDULED) | The alarm is scheduled to fire at some point in the future. |
| [String](https://developer.android.com/reference/java/lang/String.html) | [SNOOZED](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder#SNOOZED)     | The alarm has been snoozed.                                 |
| [String](https://developer.android.com/reference/java/lang/String.html) | [UNKNOWN](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder#UNKNOWN)     | The alarm is in an unknown error state.                     |

### Public Method Summary

|------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AlarmInstanceBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder) | [setAlarmStatus](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder#setAlarmStatus(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) status) Sets the current status of the instance.                               |
| [AlarmInstanceBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder) | [setScheduledTime](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder#setScheduledTime(java.util.Calendar))([Calendar](https://developer.android.com/reference/java/util/Calendar.html) scheduledTime) Sets the time an alarm instance is scheduled to fire. |

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
**DISMISSED**

The alarm has been dismissed.  
Constant Value: "Dismissed"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**FIRED**

The alarm has fired.  
Constant Value: "Fired"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**MISSED**

The alarm has been missed.  
Constant Value: "Missed"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**SCHEDULED**

The alarm is scheduled to fire at some point in the future.  
Constant Value: "Scheduled"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**SNOOZED**

The alarm has been snoozed.  
Constant Value: "Snoozed"  

#### public static final [String](https://developer.android.com/reference/java/lang/String.html)
**UNKNOWN**

The alarm is in an unknown error state.  
Constant Value: "Unknown"

## Public Methods

#### public [AlarmInstanceBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder) **setAlarmStatus**
([String](https://developer.android.com/reference/java/lang/String.html) status)

Sets the current status of the instance.  

##### Parameters

| status | Must be one of { [FIRED](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder#FIRED), [SNOOZED](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder#SNOOZED), [MISSED](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder#MISSED), [DISMISSED](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder#DISMISSED), [SCHEDULED](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder#SCHEDULED) }. A status change does not imply a change in scheduledTime. |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### public [AlarmInstanceBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/AlarmInstanceBuilder) **setScheduledTime** ([Calendar](https://developer.android.com/reference/java/util/Calendar.html) scheduledTime)

Sets the time an alarm instance is scheduled to fire.