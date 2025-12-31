# Source: https://firebase.google.com/docs/reference/android/com/google/android/gms/measurement/AppMeasurement.md.txt

# AppMeasurement

Also: ["Google Play services"](https://developers.google.com/android/reference/com/google/android/gms/measurement/AppMeasurement.html)  
public class **AppMeasurement** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
**This class was deprecated.**   

Use [FirebaseAnalytics](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics)
instead.  

### Public Method Summary

|-------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static [AppMeasurement](https://firebase.google.com/docs/reference/android/com/google/android/gms/measurement/AppMeasurement) | [getInstance](https://firebase.google.com/docs/reference/android/com/google/android/gms/measurement/AppMeasurement#getInstance(android.content.Context))([Context](https://developer.android.com/reference/android/content/Context.html) context) *This method was deprecated. Use [getInstance(Context)](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#getInstance(android.content.Context)) instead.* |
| void                                                                                                                          | [setMeasurementEnabled](https://firebase.google.com/docs/reference/android/com/google/android/gms/measurement/AppMeasurement#setMeasurementEnabled(boolean))(boolean enabled) *This method was deprecated. Please use [setAnalyticsCollectionEnabled(boolean)](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setAnalyticsCollectionEnabled(boolean)) instead.*                                          |

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

#### public static [AppMeasurement](https://firebase.google.com/docs/reference/android/com/google/android/gms/measurement/AppMeasurement)
**getInstance** ([Context](https://developer.android.com/reference/android/content/Context.html) context)

Also: ["Google Play services"](https://developers.google.com/android/reference/com/google/android/gms/measurement/AppMeasurement.html#getInstance(android.content.Context))  
**This method was deprecated.**   

Use [getInstance(Context)](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#getInstance(android.content.Context)) instead.  

#### public void **setMeasurementEnabled** (boolean enabled)

Also: ["Google Play services"](https://developers.google.com/android/reference/com/google/android/gms/measurement/AppMeasurement.html#setMeasurementEnabled(boolean))  
**This method was deprecated.**   

Please use [setAnalyticsCollectionEnabled(boolean)](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setAnalyticsCollectionEnabled(boolean)) instead.  
Sets whether analytics collection is enabled for this app on this device. This
setting is persisted across app sessions. By default it is enabled.  

##### Parameters

| enabled | Whether analytics collection is enabled for this app on this device. |
|---------|----------------------------------------------------------------------|