# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.CalendarDateTime.md.txt

# FirebaseVisionBarcode.CalendarDateTime

public static class **FirebaseVisionBarcode.CalendarDateTime** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
DateTime data type used in calendar events. If hours/minutes/seconds are not specified in
the barcode value, they will be set to -1.  

### Public Method Summary

|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| int                                                                     | [getDay](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.CalendarDateTime#getDay())() Gets the day of the calendar date time.             |
| int                                                                     | [getHours](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.CalendarDateTime#getHours())() Gets the hours of the calendar date time.       |
| int                                                                     | [getMinutes](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.CalendarDateTime#getMinutes())() Gets the minutes of the calendar date time. |
| int                                                                     | [getMonth](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.CalendarDateTime#getMonth())() Gets the month of the calendar date time.       |
| [String](https://developer.android.com/reference/java/lang/String.html) | [getRawValue](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.CalendarDateTime#getRawValue())() Gets the raw value calendar date time.    |
| int                                                                     | [getSeconds](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.CalendarDateTime#getSeconds())() Gets the seconds of the calendar date time. |
| int                                                                     | [getYear](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.CalendarDateTime#getYear())() Gets the year of the calendar date time.          |
| boolean                                                                 | [isUtc](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcode.CalendarDateTime#isUtc())() Gets whether the date time is UTC.                    |

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

#### public int **getDay** ()

Gets the day of the calendar date time.  

#### public int **getHours** ()

Gets the hours of the calendar date time.  

#### public int **getMinutes** ()

Gets the minutes of the calendar date time.  

#### public int **getMonth** ()

Gets the month of the calendar date time.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getRawValue** ()

Gets the raw value calendar date time.  

#### public int **getSeconds** ()

Gets the seconds of the calendar date time.  

#### public int **getYear** ()

Gets the year of the calendar date time.  

#### public boolean **isUtc** ()

Gets whether the date time is UTC.