# Source: https://firebase.google.com/docs/ai-logic/edit-images-imagen-controlled-customization.md.txt

<br />

<br />

| **Preview** : Using theFirebase AI LogicSDKs to accessImagenmodels is a feature that's in Preview, which means that it isn't subject to any SLA or deprecation policy and could change in backwards-incompatible ways.
|
| Editing withImagenis only supported if you're using theVertex AIGemini API. It's also currently only supported for Android and Flutter apps. Support for other platforms is coming later in the year.

<br />

<br />

This page describes how to use the*customization capability* fromImagento**edit or generate images based on a specified*control*** using theFirebase AI LogicSDKs.

<br />

**How it works** : You provide a text prompt and at least one*control*reference image (like a drawing or a Canny edge image). The model uses these inputs to generate a new image based on the control images.

For example, you can provide the model with a drawing of a rocket ship and the moon along with a text prompt to create a watercolor painting based on the drawing.

<br />

| **Important:** Review the lists of*intended* and*unintended* [use cases](https://firebase.google.com/docs/ai-logic/edit-images-imagen-controlled-customization#use-cases)so that you get better results with customization.

[arrow_downwardJump to code](https://firebase.google.com/docs/ai-logic/edit-images-imagen-controlled-customization#send-request)

#### Types of control reference images

The reference image for controlled customization can be a*scribble* , a*Canny edge image* , or a*face mesh*.

<br />

What's a scribble?

<br />

- A***scribble***is a rough, hand-drawn sketch or outline that provides the model with a basic structure, spatial arrangement, and layout to follow. The text prompt provides the details, color, and texture for the generated image.

  Example: You provide a drawing of a house, a tree, and a sun, and you also provide a text prompt like "A whimsical watercolor painting of a cottage with a large oak tree next to it at sunrise." The model will then generate an image that matches the described scene while following the general layout from your drawing.

<br />

<br />

<br />

What's a Canny edge image?

<br />

- A***Canny edge image*** is where an algorithm, specifically the[Canny edge detector](https://en.wikipedia.org/wiki/Canny_edge_detector), has been applied to a source image to map the edges of objects within the image. These edges help the model maintain the precise structure of the objects while changing the style, color, or other attributes specified by the text prompt.

  Example: You have a photo of a dog sitting on a couch. You run the Canny edge detector on the photo to get an image of just the dog's and couch's outlines. You then use this edge map as the control image and a text prompt like "a photo of a golden retriever puppy on a leather sofa." The model will generate a new photo that matches the exact pose of the original dog and the composition of the couch, but with a golden retriever puppy and a leather sofa instead of the original subjects.

<br />

<br />

<br />

What's a face mesh?

<br />

- A***face mesh***is an image that helps the model understand and replicate a specific face. It's a digital representation of a human face in 3D, typically a network of interconnected points (vertices) and triangles that define the shape and contours of the face. This provides the model with key landmarks (like the eyes, nose, and mouth) and textures.

<br />

<br />

<br />

*** ** * ** ***

<br />

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

## Send a controlled customization request

The following sample shows a controlled customization request that asks the model to generate a new image based on the provided reference image (in this example, a drawing of space, like a rocket and the moon). Since the reference image is a**rough, hand-drawn sketch or outline** , it uses the control type`CONTROL_TYPE_SCRIBBLE`.

If your reference image is a*Canny edge image* or a*face mesh*, you can also use this example but with the following changes:

- If your reference image is a[**Canny edge image**](https://firebase.google.com/docs/ai-logic/edit-images-imagen-controlled-customization#what-is-a-canny-edge-image), use the control type`CONTROL_TYPE_CANNY`.

- If your reference image is a[**face mesh**](https://firebase.google.com/docs/ai-logic/edit-images-imagen-controlled-customization#what-is-a-face-mesh), use the control type`CONTROL_TYPE_FACE_MESH`. This control can only be used with[subject customization of people](https://firebase.google.com/docs/ai-logic/edit-images-imagen-subject-customization).

Review the[prompt templates](https://firebase.google.com/docs/ai-logic/edit-images-imagen-controlled-customization#prompt-templates)later on this page to learn about writing prompts and how to use reference images within them.  

### Swift

Image editing withImagenmodels isn't supported for Swift. Check back later this year!

### Kotlin

    // Using this SDK to access Imagen models is a Preview release and requires opt-in
    @OptIn(PublicPreviewAPI::class)
    suspend fun customizeImage() {
        // Initialize the Vertex AI Gemini API backend service
        // Optionally specify the location to access the model (for example, `us-central1`)
        val ai = Firebase.ai(backend = GenerativeBackend.vertexAI(location = "us-central1"))

        // Create an `ImagenModel` instance with an Imagen "capability" model
        val model = ai.imagenModel("imagen-3.0-capability-001")

        // This example assumes 'referenceImage' is a pre-loaded Bitmap.
        // In a real app, this might come from the user's device or a URL.
        val referenceImage: Bitmap = TODO("Load your reference image Bitmap here")

        // Define the subject reference using the reference image.
        val controlReference = ImagenControlReference(
            image = referenceImage,
            referenceID = 1,
            controlType = CONTROL_TYPE_SCRIBBLE
        )

        // Provide a prompt that describes the final image.
        // The "[1]" links the prompt to the subject reference with ID 1.
        val prompt = "A cat flying through outer space arranged like the space scribble[1]"

        // Use the editImage API to perform the controlled customization.
        // Pass the list of references, the prompt, and an editing configuration.
        val editedImage = model.editImage(
            referenceImages = listOf(controlReference),
            prompt = prompt,
            config = ImagenEditingConfig(
                editSteps = 50 // Number of editing steps, a higher value can improve quality
            )
        )

        // Process the result
    }

### Java

    // Initialize the Vertex AI Gemini API backend service
    // Optionally specify the location to access the model (for example, `us-central1`)
    // Create an `ImagenModel` instance with an Imagen "capability" model
    ImagenModel imagenModel = FirebaseAI.getInstance(GenerativeBackend.vertexAI("us-central1"))
            .imagenModel(
                    /* modelName */ "imagen-3.0-capability-001");

    ImagenModelFutures model = ImagenModelFutures.from(imagenModel);

    // This example assumes 'referenceImage' is a pre-loaded Bitmap.
    // In a real app, this might come from the user's device or a URL.
    Bitmap referenceImage = null; // TODO("Load your image Bitmap here");

    // Define the subject reference using the reference image.
    ImagenControlReference controlReference = new ImagenControlReference.Builder()
            .setImage(referenceImage)
            .setReferenceID(1)
            .setControlType(CONTROL_TYPE_SCRIBBLE)
            .build();

    // Provide a prompt that describes the final image.
    // The "[1]" links the prompt to the subject reference with ID 1.
    String prompt = "A cat flying through outer space arranged like the space scribble[1]";

    // Define the editing configuration.
    ImagenEditingConfig imagenEditingConfig = new ImagenEditingConfig.Builder()
            .setEditSteps(50) // Number of editing steps, a higher value can improve quality
            .build();

    // Use the editImage API to perform the controlled customization.
    // Pass the list of references, the prompt, and an editing configuration.
    Futures.addCallback(model.editImage(Collections.singletonList(controlReference), prompt, imagenEditingConfig), new FutureCallback<ImagenGenerationResponse>() {
        @Override
        public void onSuccess(ImagenGenerationResponse result) {
            if (result.getImages().isEmpty()) {
                Log.d("TAG", "No images generated");
            }
            Bitmap bitmap = ((ImagenInlineImage) result.getImages().get(0)).asBitmap();
            // Use the bitmap to display the image in your UI
        }

        @Override
        public void onFailure(Throwable t) {
            // ...
        }
    }, Executors.newSingleThreadExecutor());

### Web

Image editing withImagenmodels isn't supported for Web apps. Check back later this year!

### Dart

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

    // This example assumes 'referenceImage' is a pre-loaded Uint8List.
    // In a real app, this might come from the user's device or a URL.
    final Uint8List referenceImage = Uint8List(0); // TODO: Load your reference image data here

    // Define the control reference using the reference image.
    final controlReference = ImagenControlReference(
      image: referenceImage,
      referenceId: 1,
        controlType: ImagenControlType.scribble,
    );

    // Provide a prompt that describes the final image.
    // The "[1]" links the prompt to the subject reference with ID 1.
    final prompt = "A cat flying through outer space arranged like the space scribble[1]";

    try {
      // Use the editImage API to perform the controlled customization.
      // Pass the list of references, the prompt, and an editing configuration.
      final response = await model.editImage(
        [controlReference],
        prompt,
        config: ImagenEditingConfig(
          editSteps: 50, // Number of editing steps, a higher value can improve quality
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

## Prompt templates

In the request, you provide reference images (up to 4 images) by defining an`ImagenControlReference`in which you specify a reference ID for an image. Note that multiple images can have the same reference ID (for example, multiple scribbles of the same idea).

Then, when writing the prompt, you refer to these IDs. For example, you use`[1]`in the prompt to refer to images with the reference ID`1`.
| **Important:** Review the lists of*intended* and*unintended* [use cases](https://firebase.google.com/docs/ai-logic/edit-images-imagen-controlled-customization#use-cases)so that you get better results with customization.

The following table provides prompt templates that can be a starting point for writing prompts for customization based on a control.

|                   Use case                   |                        Reference images                        |                                                                                                                    Prompt template                                                                                                                     |                                                                                                                                                                                               Example                                                                                                                                                                                               |
|----------------------------------------------|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Controlled customization                     | Scribble map (1)                                               | Generate an image that aligns with the<var translate="no">scribble map [1]</var>to match the description:*${STYLE_PROMPT} ${PROMPT}*.                                                                                                                  | Generate an image that aligns with the<var translate="no">scribble map [1]</var>to match the description:*The image should be in the style of an impressionistic oil painting with relaxed brushstrokes. It possesses a naturally-lit ambience and noticeable brushstrokes. A side-view of a car. The car is parked on a wet, reflective road surface, with city lights reflecting in the puddles.* |
| Controlled customization                     | Canny control image (1)                                        | Generate an image aligning with the<var translate="no">edge map [1]</var>to match the description:*${STYLE_PROMPT} ${PROMPT}*                                                                                                                          | Generate an image aligning with the<var translate="no">edge map [1]</var>to match the description:*The image should be in the style of an impressionistic oil painting, with relaxed brushstrokes. It posses a naturally-lit ambience and noticeable brushstrokes. A side-view of a car. The car is parked on a wet, reflective road surface, with city lights reflecting in the puddles.*          |
| Person image stylization with FaceMesh input | Subject image (1-3) *** ** * ** *** FaceMesh control image (1) | Create an image about<var translate="no">SUBJECT_DESCRIPTION [1]</var>in the pose of the<var translate="no">CONTROL_IMAGE [2]</var>to match the description: a portrait of<var translate="no">SUBJECT_DESCRIPTION [1]</var>*${PROMPT}*                 | Create an image about<var translate="no">a woman with short hair [1]</var>in the pose of the<var translate="no">control image [2]</var>to match the description: a portrait of<var translate="no">a woman with short hair [1]</var>*in 3D-cartoon style with a blurred background. A cute and lovely character, with a smiling face, looking at the camera, pastel color tone ...*                  |
| Person image stylization with FaceMesh input | Subject image (1-3) *** ** * ** *** FaceMesh control image (1) | Create a*${STYLE_PROMPT}* image about<var translate="no">SUBJECT_DESCRIPTION [1]</var>in the pose of the<var translate="no">CONTROL_IMAGE [2]</var>to match the description: a portrait of<var translate="no">SUBJECT_DESCRIPTION [1]</var>*${PROMPT}* | Create a*3D-cartoon style* image about<var translate="no">a woman with short hair [1]</var>in the pose of the<var translate="no">control image [2]</var>to match the description: a portrait of<var translate="no">a woman with short hair [1]</var>*in 3D-cartoon style with a blurred background. A cute and lovely character, with a smiling face, looking at the camera, pastel color tone ...* |

<br />

*** ** * ** ***

<br />

## Best practices and limitations

### Use cases

<br />

The customization capability offers free-style prompting, which can give the impression that the model can do more than it's trained to do. The following sections describe[*intended*use cases](https://firebase.google.com/docs/ai-logic/edit-images-imagen-controlled-customization#intended-use-cases)for customization, and non-exhaustive[examples of*unintended*](https://firebase.google.com/docs/ai-logic/edit-images-imagen-controlled-customization#unintended-use-cases)use cases.

We recommend using this capability for the intended use cases, since we've trained the model on those use cases and expect good results for them. Conversely, if you push the model to do things outside of the intended use cases, you should expect poor results.

<br />

#### Intended use cases

The following are***intended*** use cases for customization based on a*control*:

- Generate an image that follows the prompt and the canny edge control images.

- Generate an image that follows the prompt and the scribble images.

- Stylize a photo of a person while preserving the facial expression.

#### Examples of unintended use cases

The following is a non-exhaustive list of***unintended*** use cases for customization based on a*control*. The model isn't trained for these use cases, and will likely produce poor results.

- Generate an image using a style specified in the prompt.

- Generate an image from text that follows a specific style provided by a reference image, with some level of control on the image composition using control image.

- Generate an image from text that follows a specific style provided by a reference image, with some level of control on the image composition using a control scribble.

- Generate an image from text that follows a specific style provided by the reference image, with some level of control on the image composition using a control image. The person in the image has a specific facial expression.

- Stylize a photo of two or more people, and preserve their facial expressions.

- Stylize a photo of a pet, and turn it into a drawing. Preserve or specify the composition of the image (for example, watercolor).