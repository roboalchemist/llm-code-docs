# Source: https://firebase.google.com/docs/ai-logic/edit-images-imagen-insert-objects.md.txt

<br />

<br />

| **Preview** : Using theFirebase AI LogicSDKs to accessImagenmodels is a feature that's in Preview, which means that it isn't subject to any SLA or deprecation policy and could change in backwards-incompatible ways.
|
| Editing withImagenis only supported if you're using theVertex AIGemini API. It's also currently only supported for Android and Flutter apps. Support for other platforms is coming later in the year.

<br />

<br />

This page describes how to use*inpainting* usingImagento**insert an object into an image** using theFirebase AI LogicSDKs.

Inpainting is a type of*mask-based editing* . A*mask*is a digital overlay defining the specific area you want to edit.

<br />

**How it works**: You provide an original image and a corresponding masked image --- either auto-generated or provided by you --- that defines a mask over an area where you want to add new content. You also provide a text prompt describing what you want to add. The model then generates and adds new content within the masked area.

For example, you can mask a table and prompt the model to add a vase of flowers.

<br />

[arrow_downwardJump to code for auto-generated mask](https://firebase.google.com/docs/ai-logic/edit-images-imagen-insert-objects#mask-auto-generated)[arrow_downwardJump to code for providing the mask](https://firebase.google.com/docs/ai-logic/edit-images-imagen-insert-objects#mask-provided)

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

## Insert objects using an auto-generated mask

<br />

|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Before trying this sample, complete the[Before you begin](https://firebase.google.com/docs/ai-logic/edit-images-imagen-insert-objects#before-you-begin)section of this guide to set up your project and app.* |

<br />

The following sample shows how to use inpainting to insert content into an image --- using automatic mask generation. You provide the original image and a text prompt, andImagenautomatically detects and creates a mask area to modify the original image.
**Note:** Another way to auto-generate a mask for common objects in images is by using`ImagenSemanticMask`(instead of`ImagenBackgroundMask`) and specifying the[object class ID](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api-customization#segment-ids)for the object. For example, you can specify a class ID of`67`and the model will detect any tables in the image and create a mask over them.  

### Swift

Image editing withImagenmodels isn't supported for Swift. Check back later this year!

### Kotlin

To insert objects with an auto-generated mask, specify`ImagenBackgroundMask`. Use[`editImage()`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel#editImage(kotlin.collections.List,kotlin.String,com.google.firebase.ai.type.ImagenEditingConfig))and set the editing config to use`ImagenEditMode.INPAINT_INSERTION`.  

    // Using this SDK to access Imagen models is a Preview release and requires opt-in
    @OptIn(PublicPreviewAPI::class)
    suspend fun customizeImage() {
        // Initialize the Vertex AI Gemini API backend service
        // Optionally specify the location to access the model (for example, `us-central1`)
        val ai = Firebase.ai(backend = GenerativeBackend.vertexAI(location = "us-central1"))

        // Create an `ImagenModel` instance with an Imagen "capability" model
        val model = ai.imagenModel("imagen-3.0-capability-001")

        // This example assumes 'originalImage' is a pre-loaded Bitmap.
        // In a real app, this might come from the user's device or a URL.
        val originalImage: Bitmap = TODO("Load your original image Bitmap here")

        // Provide the prompt describing the content to be inserted.
        val prompt = "a vase of flowers on the table"

        // Use the editImage API to insert the new content.
        // Pass the original image, the prompt, and an editing configuration.
        val editedImage = model.editImage(
            referenceImages = listOf(
                ImagenRawImage(originalImage.toImagenInlineImage()),
                ImagenBackgroundMask(), // Use ImagenBackgroundMask() to auto-generate the mask.
            ),
            prompt = prompt,
            // Define the editing configuration for inpainting and insertion.
            config = ImagenEditingConfig(ImagenEditMode.INPAINT_INSERTION)
        )

        // Process the resulting 'editedImage' Bitmap, for example, by displaying it in an ImageView.
    }

### Java

To insert objects with an auto-generated mask, specify`ImagenBackgroundMask`. Use[`editImage()`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ImagenModel#editImage(kotlin.collections.List,kotlin.String,com.google.firebase.ai.type.ImagenEditingConfig))and set the editing config to use`ImagenEditMode.INPAINT_INSERTION`.  

    // Initialize the Vertex AI Gemini API backend service
    // Optionally specify the location to access the model (for example, `us-central1`)
    // Create an `ImagenModel` instance with an Imagen "capability" model
    ImagenModel imagenModel = FirebaseAI.getInstance(GenerativeBackend.vertexAI("us-central1"))
            .imagenModel(
                    /* modelName */ "imagen-3.0-capability-001");

    ImagenModelFutures model = ImagenModelFutures.from(imagenModel);

    // This example assumes 'originalImage' is a pre-loaded Bitmap.
    // In a real app, this might come from the user's device or a URL.
    Bitmap originalImage = null; // TODO("Load your image Bitmap here");

    // Provide the prompt describing the content to be inserted.
    String prompt = "a vase of flowers on the table";

    // Define the list of sources for the editImage call.
    // This includes the original image and the auto-generated mask.
    ImagenRawImage rawOriginalImage =
        new ImagenRawImage(ImagenInlineImageKt.toImagenInlineImage(originalImage));
    // Use ImagenBackgroundMask() to auto-generate the mask.
    ImagenBackgroundMask rawMaskedImage = new ImagenBackgroundMask();

    ImagenEditingConfig config = new ImagenEditingConfig();

    // Use the editImage API to insert the new content.
    // Pass the original image, the auto-generated masked image, the prompt, and an editing configuration.
    Futures.addCallback(model.editImage(Arrays.asList(rawOriginalImage, rawMaskedImage), prompt, config),
        new FutureCallback<ImagenGenerationResponse>() {
            @Override
            public void onSuccess(ImagenGenerationResponse result) {
                if (result.getImages().isEmpty()) {
                    Log.d("ImageEditor", "No images generated");
                }
                Bitmap editedImage = ((ImagenInlineImage) result.getImages().get(0)).asBitmap();
                // Process and use the bitmap to display the image in your UI
            }

            @Override
            public void onFailure(Throwable t) {
                // ...
            }
        }, Executors.newSingleThreadExecutor());

### Web

Image editing withImagenmodels isn't supported for Web apps. Check back later this year!

### Dart

To insert objects with an auto-generated mask, specify`ImagenBackgroundMask`. Use[`editImage()`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/ImagenModel/editImage.html)and set the editing config to use`ImagenEditMode.inpaintInsertion`.  

    import 'dart:typed_data';
    import 'package:firebase_ai/firebase_ai.dart';
    import 'package:firebase_core/firebase_core.dart';
    import 'firebase_options.dart';

    // Initialize FirebaseApp
    await Firebase.initializeApp(
      options: DefaultFirebaseOptions.currentPlatform,
    );

    // Initialize the Vertex AI Gemini API backend service
    // Optionally specify a location to access the model (for example, `us-central1`)
    final ai = FirebaseAI.vertexAI(location: 'us-central1');

    // Create an `ImagenModel` instance with an Imagen "capability" model
    final model = ai.imagenModel(model: 'imagen-3.0-capability-001');

    // This example assumes 'originalImage' is a pre-loaded Uint8List.
    // In a real app, this might come from the user's device or a URL.
    final Uint8List originalImage = Uint8List(0); // TODO: Load your original image data here.

    // Provide the prompt describing the content to be inserted.
    final prompt = 'a vase of flowers on the table';

    try {
      // Use the editImage API to insert the new content.
      // Pass the original image, the prompt, and an editing configuration.
      final response = await model.editImage(
        sources: [
          ImagenRawImage(originalImage),
          ImagenBackgroundMask(), // Use ImagenBackgroundMask() to auto-generate the mask.
        ],
        prompt: prompt,
        // Define the editing configuration for inpainting and insertion.
        config: const ImagenEditingConfig(
          editMode: ImagenEditMode.inpaintInsertion,
        ),
      );

      // Process the result.
      if (response.images.isNotEmpty) {
        final editedImage = response.images.first.bytes;
        // Use the editedImage (a Uint8List) to display the image, save it, etc.
        print('Image successfully generated!');
      } else {
        // Handle the case where no images were generated.
        print('Error: No images were generated.');
      }
    } catch (e) {
      // Handle any potential errors during the API call.
      print('An error occurred: $e');
    }

### Unity

Image editing withImagenmodels isn't supported for Unity. Check back later this year!

## Insert objects using a provided mask

<br />

|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Before trying this sample, complete the[Before you begin](https://firebase.google.com/docs/ai-logic/edit-images-imagen-insert-objects#before-you-begin)section of this guide to set up your project and app.* |

<br />

The following sample shows how to use inpainting to insert content into an image --- using a mask defined in an image that you provide. You provide the original image, a text prompt, and the masked image.  

### Swift

Image editing withImagenmodels isn't supported for Swift. Check back later this year!

### Kotlin

To insert objects and provide your own masked image, specify`ImagenRawMask`with the masked image. Use[`editImage()`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/ImagenModel#editImage(kotlin.collections.List,kotlin.String,com.google.firebase.ai.type.ImagenEditingConfig))and set the editing config to use`ImagenEditMode.INPAINT_INSERTION`.  

    // Using this SDK to access Imagen models is a Preview release and requires opt-in
    @OptIn(PublicPreviewAPI::class)
    suspend fun customizeImage() {
        // Initialize the Vertex AI Gemini API backend service
        // Optionally specify the location to access the model (for example, `us-central1`)
        val ai = Firebase.ai(backend = GenerativeBackend.vertexAI(location = "us-central1"))

        // Create an `ImagenModel` instance with an Imagen "capability" model
        val model = ai.imagenModel("imagen-3.0-capability-001")

        // This example assumes 'originalImage' is a pre-loaded Bitmap.
        // In a real app, this might come from the user's device or a URL.
        val originalImage: Bitmap = TODO("Load your original image Bitmap here")

        // This example assumes 'maskImage' is a pre-loaded Bitmap that contains the masked area.
        // In a real app, this might come from the user's device or a URL.
        val maskImage: Bitmap = TODO("Load your masked image Bitmap here")

        // Provide the prompt describing the content to be inserted.
        val prompt = "a vase of flowers on the table"

        // Use the editImage API to insert the new content.
        // Pass the original image, the masked image, the prompt, and an editing configuration.
        val editedImage = model.editImage(
            referenceImages = listOf(
                ImagenRawImage(originalImage.toImagenInlineImage()),
                ImagenRawMask(maskImage.toImagenInlineImage()), // Use ImagenRawMask() to provide your own masked image.
            ),
            prompt = prompt,
            // Define the editing configuration for inpainting and insertion.
            config = ImagenEditingConfig(ImagenEditMode.INPAINT_INSERTION)
        )

        // Process the resulting 'editedImage' Bitmap, for example, by displaying it in an ImageView.
    }

### Java

To insert objects and provide your own masked image, specify`ImagenRawMask`with the masked image. Use[`editImage()`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/ImagenModel#editImage(kotlin.collections.List,kotlin.String,com.google.firebase.ai.type.ImagenEditingConfig))and set the editing config to use`ImagenEditMode.INPAINT_INSERTION`.  

    // Initialize the Vertex AI Gemini API backend service
    // Optionally specify the location to access the model (for example, `us-central1`)
    // Create an `ImagenModel` instance with an Imagen "capability" model
    ImagenModel imagenModel = FirebaseAI.getInstance(GenerativeBackend.vertexAI("us-central1"))
            .imagenModel(
                    /* modelName */ "imagen-3.0-capability-001");

    ImagenModelFutures model = ImagenModelFutures.from(imagenModel);

    // This example assumes 'originalImage' is a pre-loaded Bitmap.
    // In a real app, this might come from the user's device or a URL.
    Bitmap originalImage = null; // TODO("Load your original image Bitmap here");

    // This example assumes 'maskImage' is a pre-loaded Bitmap that contains the masked area.
    // In a real app, this might come from the user's device or a URL.
    Bitmap maskImage = null; // TODO("Load your masked image Bitmap here");

    // Provide the prompt describing the content to be inserted.
    String prompt = "a vase of flowers on the table";

    // Define the list of source images for the editImage call.
    ImagenRawImage rawOriginalImage =
        new ImagenRawImage(ImagenInlineImageKt.toImagenInlineImage(originalImage));
    // Use ImagenRawMask() to provide your own masked image.
    ImagenBackgroundMask rawMaskedImage =
        new ImagenRawMask(ImagenInlineImageKt.toImagenInlineImage(maskImage));

    ImagenEditingConfig config = new ImagenEditingConfig();

    // Use the editImage API to insert the new content.
    // Pass the original image, the masked image, the prompt, and an editing configuration.
    Futures.addCallback(model.editImage(Arrays.asList(rawOriginalImage, rawMaskedImage), prompt, config), new FutureCallback<ImagenGenerationResponse>() {
        @Override
        public void onSuccess(ImagenGenerationResponse result) {
            if (result.getImages().isEmpty()) {
                Log.d("ImageEditor", "No images generated");
            }
            Bitmap editedImage = ((ImagenInlineImage) result.getImages().get(0)).asBitmap();
            // Process and use the bitmap to display the image in your UI
        }

        @Override
        public void onFailure(Throwable t) {
            // ...
        }
    }, Executors.newSingleThreadExecutor());

### Web

Image editing withImagenmodels isn't supported for Web apps. Check back later this year!

### Dart

To insert objects and provide your own masked image, specify`ImagenRawMask`with the masked image. Use[`editImage()`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/ImagenModel/editImage.html)and set the editing config to use`ImagenEditMode.inpaintInsertion`.  

    import 'dart:typed_data';
    import 'package:firebase_ai/firebase_ai.dart';
    import 'package:firebase_core/firebase_core.dart';
    import 'firebase_options.dart';

    // Initialize FirebaseApp
    await Firebase.initializeApp(
      options: DefaultFirebaseOptions.currentPlatform,
    );

    // Initialize the Vertex AI Gemini API backend service
    // Optionally specify a location to access the model (for example, `us-central1`)
    final ai = FirebaseAI.vertexAI(location: 'us-central1');

    // Create an `ImagenModel` instance with an Imagen "capability" model
    final model = ai.imagenModel(model: 'imagen-3.0-capability-001');

    // This example assumes 'originalImage' is a pre-loaded Uint8List.
    // In a real app, this might come from the user's device or a URL.
    final Uint8List originalImage = Uint8List(0); // TODO: Load your original image data here.

    // This example assumes 'maskImage' is a pre-loaded Uint8List that contains the masked area.
    // In a real app, this might come from the user's device or a URL.
    final Uint8List maskImage = Uint8List(0); // TODO: Load your masked image data here.

    // Provide the prompt describing the content to be inserted.
    final prompt = 'a vase of flowers on the table';

    try {
      // Use the editImage API to insert the new content.
      // Pass the original image, the prompt, and an editing configuration.
      final response = await model.editImage(
        sources: [
          ImagenRawImage(originalImage),
          ImagenRawMask(maskImage), // Use ImagenRawMask() to provide your own masked image.
        ],
        prompt: prompt,
        // Define the editing configuration for inpainting and insertion.
        config: const ImagenEditingConfig(
          editMode: ImagenEditMode.inpaintInsertion,
        ),
      );

      // Process the result.
      if (response.images.isNotEmpty) {
        final editedImage = response.images.first.bytes;
        // Use the editedImage (a Uint8List) to display the image, save it, etc.
        print('Image successfully generated!');
      } else {
        // Handle the case where no images were generated.
        print('Error: No images were generated.');
      }
    } catch (e) {
      // Handle any potential errors during the API call.
      print('An error occurred: $e');
    }

### Unity

Image editing withImagenmodels isn't supported for Unity. Check back later this year!

## Best practices and limitations

<br />

We recommend dilating the mask when editing an image. This can help smooth the borders of an edit and make it seem more convincing. Generally, a dilation value of 1% or 2% is recommended (`0.01`or`0.02`).

<br />

<br />

[Give feedback about your experience withFirebase AI Logic](https://firebase.google.com/docs/ai-logic/feedback)

<br />