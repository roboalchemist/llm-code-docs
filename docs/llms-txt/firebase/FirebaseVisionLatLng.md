# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionLatLng.md.txt

# FirebaseVisionLatLng

public class **FirebaseVisionLatLng** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
An object representing a latitude/longitude pair. This is expressed as a pair of doubles
representing degrees latitude and degrees longitude. Unless specified otherwise, this must
conform to the [WGS84
standard](https://www.unoosa.org/pdf/icg/2012/template/WGS_84.pdf). Values must be within normalized ranges.  

### Public Method Summary

|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| double | [getLatitude](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionLatLng#getLatitude())() Gets the latitude in degrees.    |
| double | [getLongitude](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/common/FirebaseVisionLatLng#getLongitude())() Gets the longitude in degrees. |

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

#### public double **getLatitude** ()

Gets the latitude in degrees. It must be in the range \[-90.0, +90.0\].  

#### public double **getLongitude** ()

Gets the longitude in degrees. It must be in the range \[-180.0, +180.0\].