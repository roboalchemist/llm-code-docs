# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder.md.txt

# FirebaseVisionFaceDetectorOptions.Builder

public static class **FirebaseVisionFaceDetectorOptions.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Builder class of [FirebaseVisionFaceDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions).  

### Public Constructor Summary

|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [FirebaseVisionFaceDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder#FirebaseVisionFaceDetectorOptions.Builder())() Creates a new builder to build [FirebaseVisionFaceDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions). |

### Public Method Summary

|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseVisionFaceDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions)                 | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder#build())() Builds a face detector instance.                                                                                                                                          |
| [FirebaseVisionFaceDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder) | [enableTracking](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder#enableTracking())() Enables face tracking, which will maintain a consistent ID for each face when processing consecutive frames.                                            |
| [FirebaseVisionFaceDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder) | [setClassificationMode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder#setClassificationMode(int))(int classificationMode) Indicates whether to run additional classifiers for characterizing attributes such as "smiling" and "eyes open". |
| [FirebaseVisionFaceDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder) | [setContourMode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder#setContourMode(int))(int contourMode) Sets whether to detect no contours or all contours.                                                                                   |
| [FirebaseVisionFaceDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder) | [setLandmarkMode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder#setLandmarkMode(int))(int landmarkMode) Sets whether to detect no landmarks or all landmarks.                                                                              |
| [FirebaseVisionFaceDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder) | [setMinFaceSize](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder#setMinFaceSize(float))(float minFaceSize) Sets the smallest desired face size, expressed as a proportion of the width of the head to the image width.                       |
| [FirebaseVisionFaceDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder) | [setPerformanceMode](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder#setPerformanceMode(int))(int performanceMode) Extended option for controlling additional accuracy / speed trade-offs in performing face detection.                      |

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

## Public Constructors

#### public **FirebaseVisionFaceDetectorOptions.Builder** ()

Creates a new builder to build [FirebaseVisionFaceDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions).

## Public Methods

#### public [FirebaseVisionFaceDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions) **build** ()

Builds a face detector instance.  

#### public [FirebaseVisionFaceDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder) **enableTracking** ()

Enables face tracking, which will maintain a consistent ID for each face when
processing consecutive frames. Tracking should be disabled for handling a series of
non-consecutive still images.  

#### public [FirebaseVisionFaceDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder) **setClassificationMode** (int classificationMode)

Indicates whether to run additional classifiers for characterizing attributes such
as "smiling" and "eyes open".

Default: [NO_CLASSIFICATIONS](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#NO_CLASSIFICATIONS)  

##### Parameters

| classificationMode | the classification mode used by the detector. One of [NO_CLASSIFICATIONS](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#NO_CLASSIFICATIONS) or [ALL_CLASSIFICATIONS](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#ALL_CLASSIFICATIONS) |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### public [FirebaseVisionFaceDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder) **setContourMode** (int contourMode)

Sets whether to detect no contours or all contours. Processing time increases as the
number of contours to search for increases, so detecting all contours will increase the
overall detection time. Note that it would return up to 5 faces contours.

Default: [NO_CONTOURS](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#NO_CONTOURS)  

##### Parameters

| contourMode | the contour mode used by the detector. One of [NO_CONTOURS](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#NO_CONTOURS) or [ALL_CONTOURS](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#ALL_CONTOURS). |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### public [FirebaseVisionFaceDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder) **setLandmarkMode** (int landmarkMode)

Sets whether to detect no landmarks or all landmarks. Processing time increases as
the number of landmarks to search for increases, so detecting all landmarks will
increase the overall detection time. Detecting landmarks can improve pose
estimation.

Default: [NO_LANDMARKS](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#NO_LANDMARKS)  

##### Parameters

| landmarkMode | the landmark mode used by the detector. One of [NO_LANDMARKS](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#NO_LANDMARKS) or [ALL_LANDMARKS](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#ALL_LANDMARKS). |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### public [FirebaseVisionFaceDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder) **setMinFaceSize** (float minFaceSize)

Sets the smallest desired face size, expressed as a proportion of the width of the
head to the image width. For example, if a value of 0.1 is specified then the smallest
face to search for is roughly 10% of the width of the image being searched.

Setting the min face size is a performance vs. accuracy trade-off: setting the face
size smaller will enable the detector to find smaller faces but detection will take
longer; setting the face size larger will exclude smaller faces but will run
faster.

This is not a hard limit on face size; the detector may find faces slightly smaller
than specified.

Default minimum face size is 0.1.  

##### Parameters

| minFaceSize | the smallest head size to search for relative to the size of the image, in the range of 0.0 and 1.0. For example, a setting of 0.5 would indicate that detected faces need to fill at least half of the image width. |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### public [FirebaseVisionFaceDetectorOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions.Builder) **setPerformanceMode** (int performanceMode)

Extended option for controlling additional accuracy / speed trade-offs in performing
face detection. In general, choosing the more accurate mode will generally result in
longer runtime, whereas choosing the faster mode will generally result in detecting
fewer faces.

Default: [FAST](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#FAST)  

##### Parameters

| performanceMode | fast/accurate trade-off mode. One of [FAST](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#FAST) or [ACCURATE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions#ACCURATE). |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|