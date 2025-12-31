# Source: https://firebase.google.com/docs/ml-kit/object-detection.md.txt

# Object Detection and Tracking

plat_iosplat_android  
| This page describes an old version of the Object Detection and Tracking API, which was part of ML Kit for Firebase. Development of this API has been moved to the standalone ML Kit SDK, which you can use with or without Firebase.[Learn more](https://developers.google.com/ml-kit/migration).
|
| See[Object Detection and Tracking](https://developers.google.com/ml-kit/vision/object-detection)for the latest documentation.

![](https://firebase.google.com/static/docs/ml-kit/images/object_detection@2x.png)

With ML Kit's on-device object detection and tracking API, you can localize and track in real time the most prominent objects in an image or live camera feed. You can also optionally classify detected objects into one of several general categories.

Object detection and tracking with coarse classification is useful for building live visual search experiences. Because object detection and tracking happens quickly and completely on the device, it works well as the front end of a longer visual search pipeline. After you detect and filter objects, you can pass them to a cloud backend, such as[Cloud Vision Product Search](https://cloud.google.com/vision/product-search/docs/), or to a custom model, such as one you trained using[AutoML Vision Edge](https://firebase.google.com/docs/ml-kit/automl-vision-edge).

[iOS](https://firebase.google.com/docs/ml-kit/ios/detect-objects)[Android](https://firebase.google.com/docs/ml-kit/android/detect-objects)
| This is a beta release of ML Kit for Firebase. This API might be changed in backward-incompatible ways and is not subject to any SLA or deprecation policy.

## Key capabilities

|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Fast object detection and tracking | Detect objects and get their location in the image. Track objects across images.                                                                                                                                |
| Optimized on-device model          | The object detection and tracking model is optimized for mobile devices and intended for use in real-time applications, even on lower-end devices.                                                              |
| Prominent object detection         | Automatically determine the most prominent object in an image.                                                                                                                                                  |
| Coarse classification              | Classify objects into broad categories, which you can use to filter out objects you're not interested in. The following categories are supported: home goods, fashion goods, food, plants, places, and unknown. |

## Example results

### Tracking the most prominent object across images

|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](https://firebase.google.com/static/docs/ml-kit/images/examples/montpellier1.jpg) | |---------------------------|--------------------------------------------| | Tracking ID               | 0                                          | | Bounds                    | (95, 45), (496, 45), (496, 240), (95, 240) | | Category                  | PLACE                                      | | Classification confidence | 0.9296875                                  | |
| ![](https://firebase.google.com/static/docs/ml-kit/images/examples/montpellier2.jpg) | |---------------------------|--------------------------------------------| | Tracking ID               | 0                                          | | Bounds                    | (84, 46), (478, 46), (478, 247), (84, 247) | | Category                  | PLACE                                      | | Classification confidence | 0.8710938                                  | |
| ![](https://firebase.google.com/static/docs/ml-kit/images/examples/montpellier3.jpg) | |---------------------------|--------------------------------------------| | Tracking ID               | 0                                          | | Bounds                    | (53, 45), (519, 45), (519, 240), (53, 240) | | Category                  | PLACE                                      | | Classification confidence | 0.8828125                                  | |

Photo: Christian Ferrer \[CC BY-SA 4.0\]

### Multiple objects in a static image

![](https://firebase.google.com/static/docs/ml-kit/images/examples/640px-shoes.jpg)

|                                Object 0                                 ||
|---------------------------|----------------------------------------------|
| Bounds                    | (1, 97), (332, 97), (332, 332), (1, 332)     |
| Category                  | FASHION_GOOD                                 |
| Classification confidence | 0.95703125                                   |
| Bounds                    | (186, 80), (337, 80), (337, 226), (186, 226) |
| Category                  | FASHION_GOOD                                 |
| Classification confidence | 0.84375                                      |
| Bounds                    | (296, 80), (472, 80), (472, 388), (296, 388) |
| Category                  | FASHION_GOOD                                 |
| Classification confidence | 0.94921875                                   |
| Bounds                    | (439, 83), (615, 83), (615, 306), (439, 306) |
| Category                  | FASHION_GOOD                                 |
| Classification confidence | 0.9375                                       |