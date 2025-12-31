# Source: https://firebase.google.com/docs/ml-kit/ios/detect-faces.md.txt

# Source: https://firebase.google.com/docs/ml-kit/android/detect-faces.md.txt

# Source: https://firebase.google.com/docs/ml-kit/detect-faces.md.txt

# Face Detection

plat_iosplat_android  
| This page describes an old version of the Face Detection API, which was part of ML Kit for Firebase. Development of this API has been moved to the standalone ML Kit SDK, which you can use with or without Firebase.[Learn more](https://developers.google.com/ml-kit/migration).
|
| See[Face Detection](https://developers.google.com/ml-kit/vision/face-detection)for the latest documentation.

![](https://firebase.google.com/static/docs/ml-kit/images/face_detection@2x.png)

With ML Kit's face detection API, you can detect faces in an image, identify key facial features, and get the contours of detected faces.

With face detection, you can get the information you need to perform tasks like embellishing selfies and portraits, or generating avatars from a user's photo. Because ML Kit can perform face detection in real time, you can use it in applications like video chat or games that respond to the player's expressions.

[iOS](https://firebase.google.com/docs/ml-kit/ios/detect-faces)[Android](https://firebase.google.com/docs/ml-kit/android/detect-faces)

If you're a Flutter developer, you might be interested in[FlutterFire](https://github.com/FirebaseExtended/flutterfire/tree/master/packages/firebase_ml_vision), which includes a plugin for Firebase's ML Vision APIs.
| This is a beta release of ML Kit for Firebase. This API might be changed in backward-incompatible ways and is not subject to any SLA or deprecation policy.

## Key capabilities

|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Recognize and locate facial features | Get the coordinates of the eyes, ears, cheeks, nose, and mouth of every face detected.                                                                                                                                |
| Get the contours of facial features  | Get the contours of detected faces and their eyes, eyebrows, lips, and nose.                                                                                                                                          |
| Recognize facial expressions         | Determine whether a person is smiling or has their eyes closed.                                                                                                                                                       |
| Track faces across video frames      | Get an identifier for each individual person's face that is detected. This identifier is consistent across invocations, so you can, for example, perform image manipulation on a particular person in a video stream. |
| Process video frames in real time    | Face detection is performed on the device, and is fast enough to be used in real-time applications, such as video manipulation.                                                                                       |

## Example results

### Example 1

![](https://firebase.google.com/static/docs/ml-kit/images/examples/1024px-Physicist_Stephen_Hawking_in_Zero_Gravity_NASA.jpg)

For each face detected:

|                                                                                                                                           Face 1 of 3                                                                                                                                           ||
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Bounding polygon**      | (884.880004882812, 149.546676635742), (1030.77197265625, 149.546676635742), (1030.77197265625, 329.660278320312), (884.880004882812, 329.660278320312)                                                                                                               |
| **Angles of rotation**    | Y: -14.054030418395996, Z: -55.007488250732422                                                                                                                                                                                                                       |
| **Tracking ID**           | 2                                                                                                                                                                                                                                                                    |
| **Facial landmarks**      | |---------------------|--------------------------------------| | **Left eye**        | (945.869323730469, 211.867126464844) | | **Right eye**       | (971.579467773438, 247.257247924805) | | **Bottom of mouth** | (907.756591796875, 259.714477539062) | ... etc. |
| **Feature probabilities** | |--------------------|---------------------| | **Smiling**        | 0.88979166746139526 | | **Left eye open**  | 0.98635888937860727 | | **Right eye open** | 0.99258323386311531 |                                                                                  |

### Example 2 (face contour detection)

When you have face contour detection enabled, you also get a list of points for each facial feature that was detected. These points represent the shape of the feature. The following image illustrates how these points map to a face (click the image to enlarge):

[![](https://firebase.google.com/static/docs/ml-kit/images/examples/face_contours.svg)](https://firebase.google.com/static/docs/ml-kit/images/examples/face_contours.svg)

|                                                                                                                                                                                                               Facial feature contours                                                                                                                                                                                                                ||
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Nose bridge**      | (505.149811, 221.201797), (506.987122, 313.285919)                                                                                                                                                                                                                                                                                                                                                                             |
| **Left eye**         | (404.642029, 232.854431), (408.527283, 231.366623), (413.565796, 229.427856), (421.378296, 226.967682), (432.598755, 225.434143), (442.953064, 226.089508), (453.899811, 228.594818), (461.516418, 232.650467), (465.069580, 235.600845), (462.170410, 236.316147), (456.233643, 236.891602), (446.363922, 237.966888), (435.698914, 238.149323), (424.320740, 237.235168), (416.037720, 236.012115), (409.983459, 234.870300) |
| **Top of upper lip** | (421.662048, 354.520813), (428.103882, 349.694061), (440.847595, 348.048737), (456.549988, 346.295532), (480.526489, 346.089294), (503.375702, 349.470459), (525.624634, 347.352783), (547.371155, 349.091980), (560.082031, 351.693268), (570.226685, 354.210175), (575.305420, 359.257751)                                                                                                                                   |
| (etc.)               |                                                                                                                                                                                                                                                                                                                                                                                                                                |