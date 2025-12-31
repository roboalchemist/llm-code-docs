# Source: https://firebase.google.com/docs/ai-logic/edit-images-imagen-expand-images.md.txt

<br />

<br />

| **Preview** : Using theFirebase AI LogicSDKs to accessImagenmodels is a feature that's in Preview, which means that it isn't subject to any SLA or deprecation policy and could change in backwards-incompatible ways.
|
| Editing withImagenis only supported if you're using theVertex AIGemini API. It's also currently only supported for Android and Flutter apps. Support for other platforms is coming later in the year.

<br />

<br />

This page describes how to use*outpainting* usingImagento**expand the content of an image beyond its original borders** using theFirebase AI LogicSDKs.

Outpainting is a type of*mask-based editing* . A*mask*is a digital overlay defining the specific area you want to edit.

<br />

**How it works**: You provide an original image and a corresponding masked image --- either auto-generated or provided by you --- that defines a mask of the new, expanded area. You can also optionally provide a text prompt describing what you want in the expanded area, or the model can intelligently decide what will logically continue the existing scene. The model generates the new content and fills in the masked area.

For example, you can change an image's aspect ratio or add more background context.

<br />

[arrow_downwardJump to code](https://firebase.google.com/docs/ai-logic/edit-images-imagen-expand-images#expand-image)

## Before you begin

<br />

|-------------------------------------------------------------------------|
| *Only available when using theVertex AIGemini APIas your API provider.* |

If you haven't already, complete the[getting started guide](https://firebase.google.com/docs/ai-logic/get-started), which describes how to set up your Firebase project, connect your app to Firebase, add the SDK, initialize the backend service for your chosen API provider, and create an`ImagenModel`instance.
| All our docs assume that you're using the[](https://firebase.google.com/support/releases)latest versionsof theFirebase AI LogicSDKs.

#### Models that support this capability

Imagenoffers image editing through its`capability`model:

- `imagen-3.0-capability-001`

Note that forImagenmodels, the`global`location is***not***supported.

<br />

## Expand content of an image

<br />

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Before trying this sample, complete the[Before you begin](https://firebase.google.com/docs/ai-logic/edit-images-imagen-expand-images#before-you-begin)section of this guide to set up your project and app.* |

<br />

The following sample shows how to expand an image beyond its original borders --- using a mask defined in an image that you provide. You provide the original image, a text prompt, and the masked image. Note the following about the original and masked image:

- The masked image must have the pixel dimensions of the targeted size of the final outpainted image.

- The original image must include additional padding to match the pixel dimensions of the masked image.

Providing a text prompt is optional if you want the model to intelligently decide what will logically continue the existing scene. If you want specific content within the expanded area, you need to specify that in a text prompt.  

### Swift

Image editing withImagenmodels isn't supported for Swift. Check back later this year!

### Kotlin

To expand an image, use[`editImage()`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel#editImage(kotlin.collections.List,kotlin.String,com.google.firebase.ai.type.ImagenEditingConfig))and set the editing config to use`ImagenEditMode.OUTPAINT`.  
Note that you can optionally use[`outpaintImage()`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel#outpaintImage(com.google.firebase.ai.type.ImagenInlineImage,com.google.firebase.ai.type.Dimensions,com.google.firebase.ai.type.ImagenImagePlacement,kotlin.String,com.google.firebase.ai.type.ImagenEditingConfig))instead of`editImage()`, and you don't need to specify the editing mode.
| **Note:** The SDK provides a helper function[`generateMaskAndPadForOutpainting()`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ImagenMaskReference)to generate a masked image with your specified dimensions and the original image centered within the expanded area.

Check out the[quickstart for sample code for outpainting](https://github.com/firebase/quickstart-android/blob/master/firebase-ai/app/src/main/java/com/google/firebase/quickstart/ai/feature/media/imagen/ImagenViewModel.kt).

<br />

### Java

To expand an image, use[`editImage()`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ImagenModel#editImage(kotlin.collections.List,kotlin.String,com.google.firebase.ai.type.ImagenEditingConfig))and set the editing config to use`ImagenEditMode.OUTPAINT`.  
Note that you can optionally use[`outpaintImage()`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ImagenModel#outpaintImage(com.google.firebase.ai.type.ImagenInlineImage,com.google.firebase.ai.type.Dimensions,com.google.firebase.ai.type.ImagenImagePlacement,kotlin.String,com.google.firebase.ai.type.ImagenEditingConfig))instead of`editImage()`, and you don't need to specify the editing mode.
| **Note:** The SDK provides a helper function[`generateMaskAndPadForOutpainting()`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ImagenMaskReference)to generate a masked image with your specified dimensions and the original image centered within the expanded area.

Check out the[quickstart for sample code for outpainting](https://github.com/firebase/quickstart-android/blob/master/firebase-ai/app/src/main/java/com/google/firebase/quickstart/ai/feature/media/imagen/ImagenViewModel.kt).

<br />

### Web

Image editing withImagenmodels isn't supported for Web apps. Check back later this year!

### Dart

To expand an image, use[`editImage()`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/ImagenModel/editImage.html)and set the editing config to use`ImagenEditMode.OUTPAINT`.

Check out the[quickstart for sample code for outpainting](https://github.com/firebase/flutterfire/blob/main/packages/firebase_ai/firebase_ai/example/lib/utils/image_utils.dart).

<br />

### Unity

Image editing withImagenmodels isn't supported for Unity. Check back later this year!

## Best practices and limitations

<br />

We recommend dilating the mask when editing an image. This can help smooth the borders of an edit and make it seem more convincing. Generally, a dilation value of 1% or 2% is recommended (`0.01`or`0.02`).

<br />

<br />

[Give feedback about your experience withFirebase AI Logic](https://firebase.google.com/docs/ai-logic/feedback)

<br />