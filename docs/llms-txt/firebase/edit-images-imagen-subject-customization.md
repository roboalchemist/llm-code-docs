# Source: https://firebase.google.com/docs/ai-logic/edit-images-imagen-subject-customization.md.txt

<br />

<br />

| **Preview** : Using theFirebase AI LogicSDKs to accessImagenmodels is a feature that's in Preview, which means that it isn't subject to any SLA or deprecation policy and could change in backwards-incompatible ways.
|
| Editing withImagenis only supported if you're using theVertex AIGemini API. It's also currently only supported for Android and Flutter apps. Support for other platforms is coming later in the year.

<br />

<br />

This page describes how to use the*customization capability* fromImagento**edit or generate images based on a specified*subject*** using theFirebase AI LogicSDKs.

<br />

**How it works** : You provide a text prompt and at least one reference image that shows a specific subject (like a product, person, or animal companion). The model uses these inputs to generate a new image based on the specified*subject*in the reference images.

For example, you can ask the model to apply a cartoon style to a photo of a child or change the color of a bicycle in a picture.

<br />

| **Important:** Review the lists of*intended* and*unintended* [use cases](https://firebase.google.com/docs/ai-logic/edit-images-imagen-subject-customization#use-cases)so that you get better results with customization.

[arrow_downwardJump to code](https://firebase.google.com/docs/ai-logic/edit-images-imagen-subject-customization#send-request)

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

## Send a subject customization request

The following sample shows a subject customization request that asks the model to generate a new image based on the provided reference image (in this example, a cat). Since a cat is an**animal** , it uses the subject type`ImagenSubjectReferenceType.ANIMAL`.

If your subject is a*person* or a*product*, you can also use this example but with the following changes:

- If your subject is a**person** , use the subject type`ImagenSubjectReferenceType.PERSON`. You can send this type of request with or without a[face mesh control image](https://firebase.google.com/docs/ai-logic/edit-images-imagen-controlled-customization)to further guide image generation.

- If your subject is a**product** , use the subject type`ImagenSubjectReferenceType.PRODUCT`.

Review the[prompt templates](https://firebase.google.com/docs/ai-logic/edit-images-imagen-subject-customization#prompt-templates)later on this page to learn about writing prompts and how to use reference images within them.  

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
        val subjectReference = ImagenSubjectReference(
            image = referenceImage,
            referenceID = 1,
            description = "cat",
            subjectType = ImagenSubjectReferenceType.ANIMAL
        )

        // Provide a prompt that describes the final image.
        // The "[1]" links the prompt to the subject reference with ID 1.
        val prompt = "A cat[1] flying through outer space"

        // Use the editImage API to perform the subject customization.
        // Pass the list of references, the prompt, and an editing configuration.
        val editedImage = model.editImage(
            referenceImages = listOf(subjectReference),
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
    ImagenSubjectReference subjectReference = new ImagenSubjectReference.Builder()
            .setImage(referenceImage)
            .setReferenceID(1)
            .setDescription("cat")
            .setSubjectType(ImagenSubjectReferenceType.ANIMAL)
            .build();

    // Provide a prompt that describes the final image.
    // The "[1]" links the prompt to the subject reference with ID 1.
    String prompt = "A cat[1] flying through outer space";

    // Define the editing configuration.
    ImagenEditingConfig imagenEditingConfig = new ImagenEditingConfig.Builder()
            .setEditSteps(50) // Number of editing steps, a higher value can improve quality
            .build();

    // Use the editImage API to perform the subject customization.
    // Pass the list of references, the prompt, and an editing configuration.
    Futures.addCallback(model.editImage(Collections.singletonList(subjectReference), prompt, imagenEditingConfig), new FutureCallback<ImagenGenerationResponse>() {
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

    // Define the subject reference using the reference image.
    final subjectReference = ImagenSubjectReference(
      image: referenceImage,
      referenceId: 1,
      description: 'cat',
      subjectType: ImagenSubjectReferenceType.animal,
    );

    // Provide a prompt that describes the final image.
    // The "[1]" links the prompt to the subject reference with ID 1.
    final prompt = "A cat[1] flying through outer space.";

    try {
      // Use the editImage API to perform the subject customization.
      // Pass the list of references, the prompt, and an editing configuration.
      final response = await model.editImage(
        [subjectReference],
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

In the request, you provide reference images (up to 4 images) by defining an`ImagenSubjectReference`in which you specify a reference ID for an image (and optionally a subject description, as well). Note that multiple images can have the same reference ID (for example, multiple photos of the same cat).

Then, when writing the prompt, you refer to these IDs. For example, you use`[1]`in the prompt to refer to images with the reference ID`1`. If you provide a subject description, you can also include it in the prompt so that the prompt is easier for a human to read.
| **Important:** Review the lists of*intended* and*unintended* [use cases](https://firebase.google.com/docs/ai-logic/edit-images-imagen-subject-customization#use-cases)so that you get better results with customization.

The following table describes prompt templates that can be a starting point for writing prompts for customization based on a subject (like a product, person, or animal companion).

|                     Use case                     |                          Reference images                           |                                                                                                                                   Prompt template                                                                                                                                   |                                                                                                                                                                                                                                                                                                                    Example                                                                                                                                                                                                                                                                                                                     |
|--------------------------------------------------|---------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product image stylization - advertisement        | Subject image (up to 4)                                             | Create an image about<var translate="no">SUBJECT_DESCRIPTION [1]</var>to match the description:*${PROMPT}*                                                                                                                                                                          | Create an image about<var translate="no">Luxe Elixir hair oil, golden liquid in glass bottle [1]</var>to match the description:*A close-up, high-key image of a woman's hand holding<var translate="no">Luxe Elixir hair oil, golden liquid in glass bottle [1]</var>against a pure white background. The woman's hand is well-lit and the focus is sharp on the bottle, with a shallow depth of field blurring the background and emphasizing the product. The lighting is soft and diffused, creating a subtle glow around the bottle and hand. The overall composition is simple and elegant, highlighting the product's luxurious appeal.* |
| Product image stylization - attribute change     | Subject image (up to 4)                                             | Generate an image of a<var translate="no">SUBJECT_DESCRIPTION</var>but*${PROMPT}*                                                                                                                                                                                                   | Generate an image of a<var translate="no">Seiko watch [1]</var>but*in blue*.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Person image stylization*without*face mesh input | Subject image (up to 4)                                             | Create an image about<var translate="no">SUBJECT_DESCRIPTION [1]</var>to match the description: a portrait of<var translate="no">SUBJECT_DESCRIPTION [1]</var>*${PROMPT}*                                                                                                           | Create an image about<var translate="no">a woman with short hair[1]</var>to match the description: a portrait of<var translate="no">a woman with short hair[1]</var>*in 3d-cartoon style with blurred background. A cute and lovely character, with a smiling face, looking at the camera, pastel color tone ...*                                                                                                                                                                                                                                                                                                                              |
| Person image stylization*without*face mesh input | Subject image (up to 4)                                             | Create a<var translate="no">STYLE_DESCRIPTION [2]</var>image about<var translate="no">SUBJECT_DESCRIPTION [1]</var>to match the description: a portrait of<var translate="no">SUBJECT_DESCRIPTION [1]</var>*STYLE_PROMPT*                                                           | Create a<var translate="no">3d-cartoon style [2]</var>image about<var translate="no">a woman with short hair [1]</var>to match the description: a portrait of<var translate="no">a woman with short hair [1]</var>*in 3d-cartoon style with blurred background. A cute and lovely character, with a smiling face, looking at the camera, pastel color tone ...*                                                                                                                                                                                                                                                                                |
| Person image stylization*with*face mesh input    | Subject image (up to 3) *** ** * ** *** Face mesh control image (1) | Generate an image of<var translate="no">SUBJECT_DESCRIPTION [1]</var>with the<var translate="no">Face mesh from the control image [2]</var>.*${PROMPT}*                                                                                                                             | Generate an image of<var translate="no">the person [1]</var>with the<var translate="no">face mesh from the control image [2]</var>.*The person should be looking straight ahead with a neutral expression. The background should be a ...*                                                                                                                                                                                                                                                                                                                                                                                                     |
| Person image stylization*with*face mesh input    | Subject image (up to 3) *** ** * ** *** Face mesh control image (1) | Create an image about<var translate="no">SUBJECT_DESCRIPTION [1]</var>in the pose of the<var translate="no">CONTROL_IMAGE [2]</var>to match the description: a portrait of<var translate="no">SUBJECT_DESCRIPTION [1]</var>*${PROMPT}*                                              | Create an image about<var translate="no">a woman with short hair [1]</var>in the pose of the<var translate="no">control image [2]</var>to match the description: a portrait of<var translate="no">a woman with short hair [1]</var>*in 3d-cartoon style with blurred background. A cute and lovely character, with a smiling face, looking at the camera, pastel color tone ...*                                                                                                                                                                                                                                                               |
| Person image stylization*with*face mesh input    | Subject image (up to 3) *** ** * ** *** Face mesh control image (1) | Create a<var translate="no">STYLE_DESCRIPTION [3]</var>image about<var translate="no">SUBJECT_DESCRIPTION [1]</var>in the pose of the<var translate="no">CONTROL_IMAGE [2]</var>to match the description: a portrait of<var translate="no">SUBJECT_DESCRIPTION [1]</var>*${PROMPT}* | Create a<var translate="no">3d-cartoon style [3]</var>image about<var translate="no">a woman with short hair [1]</var>in the pose of the<var translate="no">control image [2]</var>to match the description: a portrait of<var translate="no">a woman with short hair [1]</var>*in 3d-cartoon style with blurred background. A cute and lovely character, with a smiling face, looking at the camera, pastel color tone ...*                                                                                                                                                                                                                   |

<br />

*** ** * ** ***

<br />

## Best practices and limitations

If you're using a person as your subject, we recommend that the face in your reference image has the following properties:

- Is centered and occupies at least half of the whole image
- Is rotated in frontal view in all directions (roll, pitch, and yaw)
- Isn't occluded by objects, such as sunglasses or masks

### Use cases

<br />

The customization capability offers free-style prompting, which can give the impression that the model can do more than it's trained to do. The following sections describe[*intended*use cases](https://firebase.google.com/docs/ai-logic/edit-images-imagen-subject-customization#intended-use-cases)for customization, and non-exhaustive[examples of*unintended*](https://firebase.google.com/docs/ai-logic/edit-images-imagen-subject-customization#unintended-use-cases)use cases.

We recommend using this capability for the intended use cases, since we've trained the model on those use cases and expect good results for them. Conversely, if you push the model to do things outside of the intended use cases, you should expect poor results.

<br />

#### Intended use cases

The following are***intended*** use cases for customization based on a*subject*:

- Stylize a photo of a person.

- Stylize a photo of a person, and preserve the person's facial expressions.

- (Low success) Place a product, such as a couch or a cookie, into different scenes with different product angles.

- Generate variations of a product that doesn't preserve exact details.

- Stylize a photo of a person, while preserving facial expression.

#### Examples of unintended use cases

The following is a non-exhaustive list of***unintended*** use cases for customization based on a*subject*. The model isn't trained for these use cases, and will likely produce poor results.

- Place two or more people in different scenes while preserving their identities.

- Place two or more people in different scenes while preserving their identities and specifying the style of the output image using an example image as input for the style.

- Stylize a photo of two or more people while preserving their identities.

- Place a pet into different scenes while preserving its identity.

- Stylize a photo of a pet and turn it into a drawing.

- Stylize a photo of a pet and turn it into a drawing, while preserving or specifying the style of the image (such as water color).

- Place a pet and a person into a different scene, preserving the identities of both.

- Stylize a photo of a pet and one or more people and turn it into a drawing.

- Place a two products into different scenes with different product angles.

- Place a product, such as a cookie or a couch, into different scenes with different product angles, and following a specific image style (such as photorealistic with specific colors, lighting styles, or animation).

- Place a product into a different scene, while preserving the specific composition of the scene as specified by a control image.

- Place two products into different scenes with different product angles, using a specific image as input (such as photorealistic with specific colors, lighting styles, or animation).

- Place two products into different scenes, while preserving the specific composition of the scene as specified by a control image.