# Source: https://firebase.google.com/docs/ai-logic/edit-images-imagen-style-customization.md.txt

<br />

<br />

| **Preview** : Using theFirebase AI LogicSDKs to accessImagenmodels is a feature that's in Preview, which means that it isn't subject to any SLA or deprecation policy and could change in backwards-incompatible ways.
|
| Editing withImagenis only supported if you're using theVertex AIGemini API. It's also currently only supported for Android and Flutter apps. Support for other platforms is coming later in the year.

<br />

<br />

This page describes how to use the*customization capability* fromImagento**edit or generate images based on a specified*style*** using theFirebase AI LogicSDKs.

<br />

**How it works** : You provide a text prompt and at least one reference image that shows a specific style (like a pattern, texture, or design style). The model uses these inputs to generate a new image based on the specified*style*in the reference images.

For example, you can generate a new image of a kitchen based on an image from a popular retail catalog that you provide.

<br />

| **Important:** Review the lists of*intended* and*unintended* [use cases](https://firebase.google.com/docs/ai-logic/edit-images-imagen-style-customization#use-cases)so that you get better results with customization.

[arrow_downwardJump to code](https://firebase.google.com/docs/ai-logic/edit-images-imagen-style-customization#send-request)

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

## Send a style customization request

The following sample shows a style customization request that asks the model to generate a new image with the style of the provided reference image (in this example, Van Gogh's "Starry Night").

Review the[prompt templates](https://firebase.google.com/docs/ai-logic/edit-images-imagen-style-customization#prompt-templates)later on this page to learn about writing prompts and how to use reference images within them.  

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

        // Define the style reference using the reference image.
        val styleReference = ImagenStyleReference(
            image = referenceImage,
            referenceID = 1,
            description = "Van Gogh style"
        )

        // Provide a prompt that describes the final image.
        // The "[1]" links the prompt to the style reference with ID 1.
        val prompt = "A cat flying through outer space, in the Van Gogh style[1]"

        // Use the editImage API to perform the style customization.
        // Pass the list of references, the prompt, and an editing configuration.
        val editedImage = model.editImage(
            referenceImages = listOf(styleReference),
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

    // Define the style reference using the reference image.
    ImagenStyleReference subjectReference = new ImagenStyleReference.Builder()
            .setImage(referenceImage)
            .setReferenceID(1)
            .setDescription("Van Gogh style")
            .build();

    // Provide a prompt that describes the final image.
    // The "[1]" links the prompt to the style reference with ID 1.
    String prompt = "A cat flying through outer space, in the Van Gogh style[1]";

    // Define the editing configuration.
    ImagenEditingConfig imagenEditingConfig = new ImagenEditingConfig.Builder()
            .setEditSteps(50) // Number of editing steps, a higher value can improve quality
            .build();

    // Use the editImage API to perform the style customization.
    // Pass the list of references, the prompt, and the editing configuration.
    Futures.addCallback(model.editImage(Collections.singletonList(styleReference), prompt, imagenEditingConfig), new FutureCallback<ImagenGenerationResponse>() {
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

    // Define the style reference using the reference image.
    final styleReference = ImagenStyleReference(
      image: referenceImage,
      referenceId: 1,
      description: 'Van Gogh style',
    );

    // Provide a prompt that describes the final image.
    // The "[1]" links the prompt to the style reference with ID 1.
    final prompt = "A cat flying through outer space, in the Van Gogh style[1]";

    try {
      // Use the editImage API to perform the style customization.
      // Pass the list of references, the prompt, and an editing configuration.
      final response = await model.editImage(
        [styleReference],
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

In the request, you provide reference images (up to 4 images) by defining an`ImagenStyleReference`in which you specify a reference ID for an image (and optionally a style description, as well). Note that multiple images can have the same reference ID (for example, multiple photos of the same pattern).

Then, when writing the prompt, you refer to these IDs. For example, you use`[1]`in the prompt to refer to images with the reference ID`1`. If you provide a subject description, you can also include it in the prompt so that the prompt is easier for a human to read.
| **Important:** Review the lists of*intended* and*unintended* [use cases](https://firebase.google.com/docs/ai-logic/edit-images-imagen-style-customization#use-cases)so that you get better results with customization.

The following table provides prompt templates that can be a starting point for writing prompts for customization based on style.

|                     Use case                     |                        Reference images                        |                                                                                                            Prompt template                                                                                                             |                                                                                                                                                                                     Example                                                                                                                                                                                      |
|--------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Object style                                     | Subject image (1-4)                                            | Generate an image in<var translate="no">STYLE_DESCRIPTION [1]</var>based on the following caption:<var translate="no">IMAGE_DESCRIPTION</var>.                                                                                         | Generate an image in<var translate="no">neon sign style [1]</var>based on the following caption:<var translate="no">a sign saying have a great day</var>.                                                                                                                                                                                                                        |
| Person image stylization without face mesh input | Subject image (1-4)                                            | Create an image about<var translate="no">SUBJECT_DESCRIPTION [1]</var>to match the description: a portrait of<var translate="no">SUBJECT_DESCRIPTION [1]</var>*${PROMPT}*                                                              | Create an image about<var translate="no">a woman with short hair[1]</var>to match the description: a portrait of<var translate="no">a woman with short hair[1]</var>*in 3d-cartoon style with blurred background. A cute and lovely character, with a smiling face, looking at the camera, pastel color tone ...*                                                                |
| Person image stylization with face mesh input    | Subject image (1-3) *** ** * ** *** Facemesh control image (1) | Create an image about<var translate="no">SUBJECT_DESCRIPTION [1]</var>in the pose of the<var translate="no">CONTROL_IMAGE [2]</var>to match the description: a portrait of<var translate="no">SUBJECT_DESCRIPTION [1]</var>*${PROMPT}* | Create an image about<var translate="no">a woman with short hair [1]</var>in the pose of the<var translate="no">control image [2]</var>to match the description: a portrait of<var translate="no">a woman with short hair [1]</var>*in 3d-cartoon style with blurred background. A cute and lovely character, with a smiling face, looking at the camera, pastel color tone ...* |

<br />

*** ** * ** ***

<br />

## Best practices and limitations

### Use cases

<br />

The customization capability offers free-style prompting, which can give the impression that the model can do more than it's trained to do. The following sections describe[*intended*use cases](https://firebase.google.com/docs/ai-logic/edit-images-imagen-style-customization#intended-use-cases)for customization, and non-exhaustive[examples of*unintended*](https://firebase.google.com/docs/ai-logic/edit-images-imagen-style-customization#unintended-use-cases)use cases.

We recommend using this capability for the intended use cases, since we've trained the model on those use cases and expect good results for them. Conversely, if you push the model to do things outside of the intended use cases, you should expect poor results.

<br />

#### Intended use cases

The following are***intended*** use cases for customization based on a*style*:

- Generate an image from text input that follows the specific style provided by a reference image.

- Alter a photo of a person.

- Alter a photo of a person and preserve their facial expression.

#### Examples of unintended use cases

The following is a non-exhaustive list of***unintended*** use cases for customization based on a*style*. The model isn't trained for these use cases, and will likely produce poor results.

- Generate an image from text and using a reference image, with the intent to have some level of control of the generated composition from the reference image.

- Generate an image of a person from a reference image that has a person with a particular facial expression.

- Place two people in a different scene, preserve their identities, and while specifying the style of the output image (such as an oil painting) using a reference image.

- Stylize a photo of a pet and turn it into a drawing, while preserving or specifying the composition of the image.

- Place a product, such as a cookie or a couch, into different scenes with different product angles, and following a specific image style (such as photorealistic with specific colors, lighting styles, or animation).