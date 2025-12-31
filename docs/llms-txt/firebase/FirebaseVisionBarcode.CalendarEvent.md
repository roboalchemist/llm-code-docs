# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.CalendarEvent.md.txt

# FirebaseVisionBarcode.CalendarEvent

public static class **FirebaseVisionBarcode.CalendarEvent** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
A calendar event extracted from QRCode.  

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://developer.android.com/reference/java/lang/String.html)                                                                                                   | [getDescription](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.CalendarEvent#getDescription())() Gets the description of the calendar event. |
| [FirebaseVisionBarcode.CalendarDateTime](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.CalendarDateTime) | [getEnd](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.CalendarEvent#getEnd())() Gets the end date time of the calendar event.               |
| [String](https://developer.android.com/reference/java/lang/String.html)                                                                                                   | [getLocation](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.CalendarEvent#getLocation())() Gets the location of the calendar event.          |
| [String](https://developer.android.com/reference/java/lang/String.html)                                                                                                   | [getOrganizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.CalendarEvent#getOrganizer())() Gets the organizer of the calendar event.       |
| [FirebaseVisionBarcode.CalendarDateTime](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.CalendarDateTime) | [getStart](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.CalendarEvent#getStart())() Gets the start date time of the calendar event.         |
| [String](https://developer.android.com/reference/java/lang/String.html)                                                                                                   | [getStatus](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.CalendarEvent#getStatus())() Gets the status of the calendar event.                |
| [String](https://developer.android.com/reference/java/lang/String.html)                                                                                                   | [getSummary](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.CalendarEvent#getSummary())() Gets the summary of the calendar event.             |

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

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getDescription** ()

Gets the description of the calendar event.  

#### public [FirebaseVisionBarcode.CalendarDateTime](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.CalendarDateTime) **getEnd** ()

Gets the end date time of the calendar event.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getLocation** ()

Gets the location of the calendar event.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getOrganizer** ()

Gets the organizer of the calendar event.  

#### public [FirebaseVisionBarcode.CalendarDateTime](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.CalendarDateTime) **getStart** ()

Gets the start date time of the calendar event.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getStatus** ()

Gets the status of the calendar event.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getSummary** ()

Gets the summary of the calendar event.