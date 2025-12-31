# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision.md.txt

# FirebaseVision

public class **FirebaseVision** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Entry class for Firebase machine learning vision services.

To use this class, get an instance via [getInstance()](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getInstance())
or [getInstance(FirebaseApp)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getInstance(com.google.firebase.FirebaseApp)), and then get an instance of a detector. The code below
is an example of getting an instance of a face detector:  


     FirebaseVisionFaceDetector faceDetector = FirebaseVision.getInstance().getVisionFaceDetector();
     
See individual detector classes for details.  

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseVisionDocumentTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentTextRecognizer)     | [getCloudDocumentTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getCloudDocumentTextRecognizer(com.google.firebase.ml.vision.document.FirebaseVisionCloudDocumentRecognizerOptions))([FirebaseVisionCloudDocumentRecognizerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionCloudDocumentRecognizerOptions) options) Gets a [FirebaseVisionDocumentTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentTextRecognizer) that can detect document text in a supplied image. |
| [FirebaseVisionDocumentTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentTextRecognizer)     | [getCloudDocumentTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getCloudDocumentTextRecognizer())() Gets a [FirebaseVisionDocumentTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentTextRecognizer) that can detect document text in a supplied image with default options.                                                                                                                                                                                                                                                             |
| [FirebaseVisionImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler)                            | [getCloudImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getCloudImageLabeler(com.google.firebase.ml.vision.label.FirebaseVisionCloudImageLabelerOptions))([FirebaseVisionCloudImageLabelerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionCloudImageLabelerOptions) options) Gets a cloud version of [FirebaseVisionImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler) that can detect labels in a supplied image.                                                          |
| [FirebaseVisionImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler)                            | [getCloudImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getCloudImageLabeler())() Gets a cloud version of [FirebaseVisionImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler) that can detect labels in a supplied image with default options.                                                                                                                                                                                                                                                                                              |
| [FirebaseVisionTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextRecognizer)                         | [getCloudTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getCloudTextRecognizer())() Gets a [FirebaseVisionTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextRecognizer) to perform optical character recognition with cloud model and default options.                                                                                                                                                                                                                                                                                          |
| [FirebaseVisionTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextRecognizer)                         | [getCloudTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getCloudTextRecognizer(com.google.firebase.ml.vision.text.FirebaseVisionCloudTextRecognizerOptions))([FirebaseVisionCloudTextRecognizerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions) options) Gets a [FirebaseVisionTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextRecognizer) to perform optical character recognition with cloud model and provided options.                            |
| static [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision)                                                   | [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getInstance())() Gets an instance of [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision) associated with the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).                                                                                                                                                                                                                                                                                    |
| static [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision)                                                   | [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getInstance(com.google.firebase.FirebaseApp))([FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) app) Gets an instance of [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision) associated with the supplied [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).                                                                                                                                               |
| [FirebaseVisionImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler)                            | [getOnDeviceAutoMLImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getOnDeviceAutoMLImageLabeler(com.google.firebase.ml.vision.label.FirebaseVisionOnDeviceAutoMLImageLabelerOptions))([FirebaseVisionOnDeviceAutoMLImageLabelerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceAutoMLImageLabelerOptions) options) *This method is deprecated. The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).*                                                 |
| [FirebaseVisionImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler)                            | [getOnDeviceImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getOnDeviceImageLabeler())() *This method is deprecated. The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).*                                                                                                                                                                                                                                                                                                                                                 |
| [FirebaseVisionImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler)                            | [getOnDeviceImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getOnDeviceImageLabeler(com.google.firebase.ml.vision.label.FirebaseVisionOnDeviceImageLabelerOptions))([FirebaseVisionOnDeviceImageLabelerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceImageLabelerOptions) options) *This method is deprecated. The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).*                                                                               |
| [FirebaseVisionObjectDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetector)                      | [getOnDeviceObjectDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getOnDeviceObjectDetector())() *This method is deprecated. The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).*                                                                                                                                                                                                                                                                                                                                             |
| [FirebaseVisionObjectDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetector)                      | [getOnDeviceObjectDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getOnDeviceObjectDetector(com.google.firebase.ml.vision.objects.FirebaseVisionObjectDetectorOptions))([FirebaseVisionObjectDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions) options) *This method is deprecated. The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).*                                                                                         |
| [FirebaseVisionTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextRecognizer)                         | [getOnDeviceTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getOnDeviceTextRecognizer())() *This method is deprecated. The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).*                                                                                                                                                                                                                                                                                                                                             |
| [FirebaseVisionBarcodeDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetector)                    | [getVisionBarcodeDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getVisionBarcodeDetector(com.google.firebase.ml.vision.barcode.FirebaseVisionBarcodeDetectorOptions))([FirebaseVisionBarcodeDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions) options) *This method is deprecated. The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).*                                                                                        |
| [FirebaseVisionBarcodeDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetector)                    | [getVisionBarcodeDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getVisionBarcodeDetector())() *This method is deprecated. The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).*                                                                                                                                                                                                                                                                                                                                               |
| [FirebaseVisionCloudLandmarkDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/landmark/FirebaseVisionCloudLandmarkDetector) | [getVisionCloudLandmarkDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getVisionCloudLandmarkDetector())() Gets a [FirebaseVisionCloudLandmarkDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/landmark/FirebaseVisionCloudLandmarkDetector) that can detect landmark in a supplied image with default options.                                                                                                                                                                                                                                                              |
| [FirebaseVisionCloudLandmarkDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/landmark/FirebaseVisionCloudLandmarkDetector) | [getVisionCloudLandmarkDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getVisionCloudLandmarkDetector(com.google.firebase.ml.vision.cloud.FirebaseVisionCloudDetectorOptions))([FirebaseVisionCloudDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions) options) Gets a [FirebaseVisionCloudLandmarkDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/landmark/FirebaseVisionCloudLandmarkDetector) that can detect landmark in a supplied image.                                      |
| [FirebaseVisionFaceDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetector)                             | [getVisionFaceDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getVisionFaceDetector())() *This method is deprecated. The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).*                                                                                                                                                                                                                                                                                                                                                     |
| [FirebaseVisionFaceDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetector)                             | [getVisionFaceDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#getVisionFaceDetector(com.google.firebase.ml.vision.face.FirebaseVisionFaceDetectorOptions))([FirebaseVisionFaceDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions) options) *This method is deprecated. The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).*                                                                                                             |
| boolean                                                                                                                                                                    | [isStatsCollectionEnabled](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#isStatsCollectionEnabled())() Determines whether stats collection in [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision) is enabled or disabled                                                                                                                                                                                                                                                                                                                                               |
| void                                                                                                                                                                       | [setStatsCollectionEnabled](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision#setStatsCollectionEnabled(boolean))(boolean enable) Enables stats collection in ML Kit vision.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

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

#### public [FirebaseVisionDocumentTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentTextRecognizer) **getCloudDocumentTextRecognizer** ([FirebaseVisionCloudDocumentRecognizerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionCloudDocumentRecognizerOptions) options)

Gets a [FirebaseVisionDocumentTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentTextRecognizer) that can detect document text in a
supplied image.  

##### Parameters

| options | the options for the cloud text detector. |
|---------|------------------------------------------|

##### Returns

- an instance of [FirebaseVisionDocumentTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentTextRecognizer). Note that text detector instance will be the same instance if the supplied options are the same and under the same [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision).  

#### public [FirebaseVisionDocumentTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentTextRecognizer) **getCloudDocumentTextRecognizer** ()

Gets a [FirebaseVisionDocumentTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentTextRecognizer) that can detect document text in a
supplied image with default options.  

##### Returns

- an instance of [FirebaseVisionDocumentTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentTextRecognizer). Note that multiple calls of this API would always return the same cloud document text instance and under the same [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision).  

#### public [FirebaseVisionImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler) **getCloudImageLabeler** ([FirebaseVisionCloudImageLabelerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionCloudImageLabelerOptions) options)

Gets a cloud version of [FirebaseVisionImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler) that can detect labels in a supplied image.  

##### Parameters

| options | the options for the cloud image labeler. |
|---------|------------------------------------------|

##### Returns

- an instance of [FirebaseVisionImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler). Note that image labeler instance will be the same instance if the supplied options are the same and under the same [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision).  

#### public [FirebaseVisionImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler) **getCloudImageLabeler** ()

Gets a cloud version of [FirebaseVisionImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler) that can detect labels in a supplied image with
default options.  

##### Returns

- an instance of [FirebaseVisionImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler). Note that multiple calls of this API would always return the same cloud label instance and under the same [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision).  

#### public [FirebaseVisionTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextRecognizer) **getCloudTextRecognizer** ()

Gets a [FirebaseVisionTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextRecognizer) to perform optical character recognition with
cloud model and default options.  

##### Returns

- an instance of [FirebaseVisionTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextRecognizer). Note there is only one instance of cloud [FirebaseVisionTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextRecognizer) and under the same [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision).  

#### public [FirebaseVisionTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextRecognizer) **getCloudTextRecognizer** ([FirebaseVisionCloudTextRecognizerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionCloudTextRecognizerOptions) options)

Gets a [FirebaseVisionTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextRecognizer) to perform optical character recognition with
cloud model and provided options.  

##### Returns

- an instance of [FirebaseVisionTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextRecognizer). Note that the returned instance will be the same if the supplied options are the same and under the same [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision).  

#### public static [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision)
**getInstance** ()

Gets an instance of [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision)
associated with the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).  

#### public static [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision)
**getInstance** ([FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) app)

Gets an instance of [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision)
associated with the supplied [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).  

##### Parameters

| app | the [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) to associate this [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision) with. |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### public [FirebaseVisionImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler) **getOnDeviceAutoMLImageLabeler** ([FirebaseVisionOnDeviceAutoMLImageLabelerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceAutoMLImageLabelerOptions) options)

**This method is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).  
Gets an on device version of [FirebaseVisionImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler) that labels a supplied image, using a model
trained from Firebase AutoML.  

##### Parameters

| options | the options for the on device automl image labeler. |
|---------|-----------------------------------------------------|

##### Returns

- an instance of [FirebaseVisionImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler). Note that multiple calls of this API would always return the same image labeler instance and under the same [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision).  

##### Throws

| [FirebaseMLException](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException) | if failed to instantiate a [FirebaseVisionImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler). |
|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### public [FirebaseVisionImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler) **getOnDeviceImageLabeler** ()

**This method is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).  
Gets an on device version of [FirebaseVisionImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler) that labels a supplied image with a default
[FirebaseVisionOnDeviceImageLabelerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceImageLabelerOptions).  

##### Returns

- an instance of [FirebaseVisionImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler). Note that multiple calls of this API would always return the same image label detector instance and under the same [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision).  

#### public [FirebaseVisionImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler) **getOnDeviceImageLabeler** ([FirebaseVisionOnDeviceImageLabelerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionOnDeviceImageLabelerOptions) options)

**This method is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).  
Gets an on device version of [FirebaseVisionImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler) that labels a supplied image.  

##### Parameters

| options | the options for the on device image labeler. |
|---------|----------------------------------------------|

##### Returns

- an instance of [FirebaseVisionImageLabeler](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/label/FirebaseVisionImageLabeler). Note that image labeler instance will be the same instance if the supplied options are the same and under the same [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision).  

#### public [FirebaseVisionObjectDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetector) **getOnDeviceObjectDetector** ()

**This method is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).  
Gets a [FirebaseVisionObjectDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetector) that can detect objects in a supplied image
with default options.  

##### Returns

- an instance of [FirebaseVisionObjectDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetector). Note that multiple calls of this API would always return the same object detector instance and under the same [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision).  

#### public [FirebaseVisionObjectDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetector) **getOnDeviceObjectDetector** ([FirebaseVisionObjectDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetectorOptions) options)

**This method is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).  
Gets a [FirebaseVisionObjectDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetector) that can detect objects in a supplied image
with given options.  

##### Returns

- an instance of [FirebaseVisionObjectDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/objects/FirebaseVisionObjectDetector). Note that multiple calls of this API would always return the same object detector instance if the supplied options are the same and under the same [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision).  

#### public [FirebaseVisionTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextRecognizer) **getOnDeviceTextRecognizer** ()

**This method is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).  
Gets a [FirebaseVisionTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextRecognizer) to perform optical character recognition with
on-device model.  

##### Returns

- an instance of [FirebaseVisionTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextRecognizer). Note there is only one instance of on-device [FirebaseVisionTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/text/FirebaseVisionTextRecognizer) and under the same [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision).  

#### public [FirebaseVisionBarcodeDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetector) **getVisionBarcodeDetector** ([FirebaseVisionBarcodeDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions) options)

**This method is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).  
Gets a [FirebaseVisionBarcodeDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetector) that can detect barcodes in a supplied
image.  

##### Parameters

| options | the options for the barcode detector. |
|---------|---------------------------------------|

##### Returns

- an instance of [FirebaseVisionBarcodeDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetector). Note that barcode detector instance will be the same instance if the supplied options are the same and under the same [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision).  

#### public [FirebaseVisionBarcodeDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetector) **getVisionBarcodeDetector** ()

**This method is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).  
Gets a [FirebaseVisionBarcodeDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetector) that can detect barcodes in a supplied image
with a default [FirebaseVisionBarcodeDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetectorOptions).  

##### Returns

- an instance of [FirebaseVisionBarcodeDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/barcode/FirebaseVisionBarcodeDetector). Note that multiple calls of this API would always return the same barcode detector instance and under the same [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision).  

#### public [FirebaseVisionCloudLandmarkDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/landmark/FirebaseVisionCloudLandmarkDetector) **getVisionCloudLandmarkDetector** ()

Gets a [FirebaseVisionCloudLandmarkDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/landmark/FirebaseVisionCloudLandmarkDetector) that can detect landmark in a supplied
image with default options.  

##### Returns

- an instance of [FirebaseVisionCloudLandmarkDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/landmark/FirebaseVisionCloudLandmarkDetector). Note that multiple calls of this API would always return the same cloud landmark instance and under the same [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision).  

#### public [FirebaseVisionCloudLandmarkDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/landmark/FirebaseVisionCloudLandmarkDetector) **getVisionCloudLandmarkDetector** ([FirebaseVisionCloudDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/FirebaseVisionCloudDetectorOptions) options)

Gets a [FirebaseVisionCloudLandmarkDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/landmark/FirebaseVisionCloudLandmarkDetector) that can detect landmark in a supplied
image.  

##### Parameters

| options | the options for the cloud landmark detector. |
|---------|----------------------------------------------|

##### Returns

- an instance of [FirebaseVisionCloudLandmarkDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/cloud/landmark/FirebaseVisionCloudLandmarkDetector). Note that landmark detector instance will be the same instance if the supplied options are the same and under the same [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision).  

#### public [FirebaseVisionFaceDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetector) **getVisionFaceDetector** ()

**This method is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).  
Gets a [FirebaseVisionFaceDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetector) that detects faces in a supplied image with a
default [FirebaseVisionFaceDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions).  

##### Returns

- an instance of [FirebaseVisionFaceDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetector). Note that multiple calls of this API would always return the same cloud face instance and under the same [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision).  

#### public [FirebaseVisionFaceDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetector) **getVisionFaceDetector** ([FirebaseVisionFaceDetectorOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetectorOptions) options)

**This method is deprecated.**   

The standalone ML Kit SDK replaces this API. For more information, refer to the [migration guide](https://developers.google.com/ml-kit/migration).  
Gets a [FirebaseVisionFaceDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetector) that detects faces in a supplied image.  

##### Parameters

| options | the options for the face detector. |
|---------|------------------------------------|

##### Returns

- an instance of [FirebaseVisionFaceDetector](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/face/FirebaseVisionFaceDetector). Note that face detector instance will be the same instance if the supplied options are the same and under the same [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision).  

#### public boolean **isStatsCollectionEnabled** ()

Determines whether stats collection in [FirebaseVision](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/FirebaseVision)
is enabled or disabled  

##### Returns

- true if stats collection is enabled and false otherwise.  

#### public void **setStatsCollectionEnabled** (boolean enable)

Enables stats collection in ML Kit vision. The stats include API calls counts,
errors, API call durations, options, etc. No personally identifiable information is
logged.

The setting is per [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp),
and it is persistent together with app's private data. It means if the user uninstalls
the app or clears all app data, the setting will be erased. The best practice is to set
the flag in each initialization.

By default the logging is enabled. You have to specifically set it to false to
disable logging.