# Source: https://firebase.google.com/docs/ai-logic/generate-images-imagen.md.txt

<br />

TheFirebase AI LogicSDKs give you access to theImagenmodels (via the[Imagen API](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api)) so that you can generate images from a text prompt. With this capability, you can do things like:  

- Generate images from prompts written in natural language
- Generate images in a wide range of formats and styles
- Render text in images

This guide describes how to generate images usingImagenby only providing a text prompt.

Note, though, thatImagencan also generate images based on a reference image using its[*customization capability*](https://firebase.google.com/docs/ai-logic/edit-images-imagen-overview#customization)(currently only for Android and Flutter). In the request, you provide a text prompt and a reference image that guides the model to generate a new image based on the specified style, subject (like a product, person, or animal), or a control. For example, you can generate a new image from a photo of a cat or a drawing of a rocket and the moon.

[arrow_downwardJump to code for text-only input](https://firebase.google.com/docs/ai-logic/generate-images-imagen#text-only-input)

### Choosing betweenGeminiandImagenmodels

TheFirebase AI LogicSDKs support image generation and editing using either aGeminimodel or anImagenmodel.

**For most use cases, start withGemini** , and then chooseImagenonly for specialized tasks where image quality is critical.

Choose[**Gemini**](https://firebase.google.com/docs/ai-logic/generate-images-gemini)when you want:

- To use world knowledge and reasoning to generate contextually relevant images.
- To seamlessly blend text and images or to interleave text and image output.
- To embed accurate visuals within long text sequences.
- To edit images conversationally while maintaining context.

Choose[**Imagen**](https://firebase.google.com/docs/ai-logic/generate-images-imagen)when you want:

- To prioritize image quality, photorealism, artistic detail, or specific styles (for example, impressionism or anime).
- To infuse branding, style, or generation of logos and product designs.
- To explicitly specify the aspect ratio or format of generated images.

## Before you begin

<br />

|----------------------------------------------------------------------------------------------------------------------------------|
| *Click yourGemini APIprovider to view provider-specific content and code on this page.* Gemini Developer APIVertex AI Gemini API |

<br />

If you haven't already, complete the[getting started guide](https://firebase.google.com/docs/ai-logic/get-started), which describes how to set up your Firebase project, connect your app to Firebase, add the SDK, initialize the backend service for your chosen API provider, and create an`ImagenModel`instance.

<br />

| All our docs assume that you're using the[](https://firebase.google.com/support/releases)latest versionsof theFirebase AI LogicSDKs.

<br />

#### Models that support this capability

TheGemini Developer APIsupports image generation by the latest stableImagenmodels. This limitation of supportedImagenmodels is applicable regardless of how you access theGemini Developer API.

- `imagen-4.0-generate-001`
- `imagen-4.0-fast-generate-001`
- `imagen-4.0-ultra-generate-001`
- `imagen-3.0-generate-002`

## Generate images from text-only input

You can ask anImagenmodel to generate images by prompting only with text. You can generate[one image](https://firebase.google.com/docs/ai-logic/generate-images-imagen#text-only-input-gen-one-img)or[multiple images](https://firebase.google.com/docs/ai-logic/generate-images-imagen#text-only-input-gen-multiple-imgs).

You can also set many different[configuration options for image generation](https://firebase.google.com/docs/ai-logic/model-parameters#imagen), like aspect ratio and image format.
| **Note:** If you want to provide a reference image in the request, you can use the[*customization capability*](https://firebase.google.com/docs/ai-logic/edit-images-imagen-overview#customization)(currently only for Android and Flutter).

### Generate one image from text-only input

<br />

|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Before trying this sample, complete the[Before you begin](https://firebase.google.com/docs/ai-logic/generate-images-imagen#before-you-begin)section of this guide to set up your project and app. **In that section, you'll also click a button for your chosenGemini APIprovider so that you see provider-specific content on this page**.* |

<br />

You can ask anImagenmodel to generate a single image by prompting only with text.

Make sure to create an`ImagenModel`instance and call`generateImages`.  

### Swift


    import FirebaseAILogic

    // Initialize the Gemini Developer API backend service
    let ai = FirebaseAI.firebaseAI(backend: .googleAI())

    // Create an `ImagenModel` instance with a model that supports your use case
    let model = ai.imagenModel(modelName: "imagen-4.0-generate-001")

    // Provide an image generation prompt
    let prompt = "An astronaut riding a horse"

    // To generate an image, call `generateImages` with the text prompt
    let response = try await model.generateImages(prompt: prompt)

    // Handle the generated image
    guard let image = response.images.first else {
      fatalError("No image in the response.")
    }
    let uiImage = UIImage(data: image.data)

### Kotlin


    suspend fun generateImage() {
      // Initialize the Gemini Developer API backend service
      val ai = Firebase.ai(backend = GenerativeBackend.googleAI())

      // Create an `ImagenModel` instance with an Imagen model that supports your use case
      val model = ai.imagenModel("imagen-4.0-generate-001")

      // Provide an image generation prompt
      val prompt = "An astronaut riding a horse"

      // To generate an image, call `generateImages` with the text prompt
      val imageResponse = model.generateImages(prompt)

      // Handle the generated image
      val image = imageResponse.images.first()

      val bitmapImage = image.asBitmap()
    }

### Java


    // Initialize the Gemini Developer API backend service
    // Create an `ImagenModel` instance with an Imagen model that supports your use case
    ImagenModel imagenModel = FirebaseAI.getInstance(GenerativeBackend.googleAI())
            .imagenModel(
                    /* modelName */ "imagen-4.0-generate-001");

    ImagenModelFutures model = ImagenModelFutures.from(imagenModel);

    // Provide an image generation prompt
    String prompt = "An astronaut riding a horse";

    // To generate an image, call `generateImages` with the text prompt
    Futures.addCallback(model.generateImages(prompt), new FutureCallback<ImagenGenerationResponse<ImagenInlineImage>>() {
        @Override
        public void onSuccess(ImagenGenerationResponse<ImagenInlineImage> result) {
            if (result.getImages().isEmpty()) {
                Log.d("TAG", "No images generated");
            }
            Bitmap bitmap = result.getImages().get(0).asBitmap();
            // Use the bitmap to display the image in your UI
        }

        @Override
        public void onFailure(Throwable t) {
            // ...
        }
    }, Executors.newSingleThreadExecutor());

### Web


    import { initializeApp } from "firebase/app";
    import { getAI, getGenerativeModel, GoogleAIBackend } from "firebase/ai";

    // TODO(developer) Replace the following with your app's Firebase configuration
    // See: https://firebase.google.com/docs/web/learn-more#config-object
    const firebaseConfig = {
      // ...
    };

    // Initialize FirebaseApp
    const firebaseApp = initializeApp(firebaseConfig);

    // Initialize the Gemini Developer API backend service
    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    // Create an `ImagenModel` instance with an Imagen model that supports your use case
    const model = getImagenModel(ai, { model: "imagen-4.0-generate-001" });

    // Provide an image generation prompt
    const prompt = "An astronaut riding a horse.";

    // To generate an image, call `generateImages` with the text prompt
    const response = await model.generateImages(prompt)

    // If fewer images were generated than were requested,
    // then `filteredReason` will describe the reason they were filtered out
    if (response.filteredReason) {
      console.log(response.filteredReason);
    }

    if (response.images.length == 0) {
      throw new Error("No images in the response.")
    }

    const image = response.images[0];

### Dart

    import 'package:firebase_ai/firebase_ai.dart';
    import 'package:firebase_core/firebase_core.dart';
    import 'firebase_options.dart';

    // Initialize FirebaseApp
    await Firebase.initializeApp(
      options: DefaultFirebaseOptions.currentPlatform,
    );

    // Initialize the Gemini Developer API backend service
    final model = FirebaseAI.googleAI();

    // Create an `ImagenModel` instance with an Imagen model that supports your use case
    final model = ai.imagenModel(model: 'imagen-4.0-generate-001');

    // Provide an image generation prompt
    const prompt = 'An astronaut riding a horse.';

    // To generate an image, call `generateImages` with the text prompt
    final response = await model.generateImages(prompt);

    if (response.images.isNotEmpty) {
      final image = response.images[0];
      // Process the image
    } else {
      // Handle the case where no images were generated
      print('Error: No images were generated.');
    }

### Unity


    using Firebase.AI;

    // Initialize the Gemini Developer API backend service
    var ai = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI());

    // Create an `ImagenModel` instance with a model that supports your use case
    var model = ai.GetImagenModel(modelName: "imagen-4.0-generate-001");

    // Provide an image generation prompt
    var prompt = "An astronaut riding a horse";

    // To generate an image, call `generateImages` with the text prompt
    var response = await model.GenerateImagesAsync(prompt: prompt);

    // Handle the generated image
    if (response.Images.Count == 0) {
      throw new Exception("No image in the response.");
    }
    var image = response.Images[0].AsTexture2D();

Learn how to choose a[model](https://firebase.google.com/docs/ai-logic/models)appropriate for your use case and app.

### Generate multiple images from text-only input

<br />

|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Before trying this sample, complete the[Before you begin](https://firebase.google.com/docs/ai-logic/generate-images-imagen#before-you-begin)section of this guide to set up your project and app. **In that section, you'll also click a button for your chosenGemini APIprovider so that you see provider-specific content on this page**.* |

<br />

By default,Imagenmodels generate only one image per request. However, you can ask anImagenmodel to generate multiple images per request by providing an[`ImagenGenerationConfig`](https://firebase.google.com/docs/ai-logic/model-parameters#imagen)when creating the`ImagenModel`instance.

Make sure to create an`ImagenModel`instance and call`generateImages`.  

### Swift


    import FirebaseAILogic

    // Initialize the Gemini Developer API backend service
    let ai = FirebaseAI.firebaseAI(backend: .googleAI())

    // Create an `ImagenModel` instance with a model that supports your use case
    let model = ai.imagenModel(
      modelName: "imagen-4.0-generate-001",
      // Configure the model to generate multiple images for each request
      // See: https://firebase.google.com/docs/ai-logic/model-parameters
      generationConfig: ImagenGenerationConfig(numberOfImages: 4)
    )

    // Provide an image generation prompt
    let prompt = "An astronaut riding a horse"

    // To generate images, call `generateImages` with the text prompt
    let response = try await model.generateImages(prompt: prompt)

    // If fewer images were generated than were requested,
    // then `filteredReason` will describe the reason they were filtered out
    if let filteredReason = response.filteredReason {
      print(filteredReason)
    }

    // Handle the generated images
    let uiImages =  response.images.compactMap { UIImage(data: $0.data) }

### Kotlin


    suspend fun generateImage() {
      // Initialize the Gemini Developer API backend service
      val ai = Firebase.ai(backend = GenerativeBackend.googleAI())

      // Create an `ImagenModel` instance with an Imagen model that supports your use case
      val model = ai.imagenModel(
        modelName = "imagen-4.0-generate-001",
        // Configure the model to generate multiple images for each request
        // See: https://firebase.google.com/docs/ai-logic/model-parameters
        generationConfig = ImagenGenerationConfig(numberOfImages = 4)
      )

      // Provide an image generation prompt
      val prompt = "An astronaut riding a horse"

      // To generate images, call `generateImages` with the text prompt
      val imageResponse = model.generateImages(prompt)

      // If fewer images were generated than were requested,
      // then `filteredReason` will describe the reason they were filtered out
      if (imageResponse.filteredReason != null) {
        Log.d(TAG, "FilteredReason: ${imageResponse.filteredReason}")
      }

      for (image in imageResponse.images) {
        val bitmap = image.asBitmap()
        // Use the bitmap to display the image in your UI
      }
    }

### Java


    // Configure the model to generate multiple images for each request
    // See: https://firebase.google.com/docs/ai-logic/model-parameters
    ImagenGenerationConfig imagenGenerationConfig = new ImagenGenerationConfig.Builder()
            .setNumberOfImages(4)
            .build();

    // Initialize the Gemini Developer API backend service
    // Create an `ImagenModel` instance with an Imagen model that supports your use case
    ImagenModel imagenModel = FirebaseAI.getInstance(GenerativeBackend.googleAI())
            .imagenModel(
                    /* modelName */ "imagen-4.0-generate-001",
                    /* imageGenerationConfig */ imagenGenerationConfig);

    ImagenModelFutures model = ImagenModelFutures.from(imagenModel);

    // Provide an image generation prompt
    String prompt = "An astronaut riding a horse";

    // To generate images, call `generateImages` with the text prompt
    Futures.addCallback(model.generateImages(prompt), new FutureCallback<ImagenGenerationResponse<ImagenInlineImage>>() {
        @Override
        public void onSuccess(ImagenGenerationResponse<ImagenInlineImage> result) {
            // If fewer images were generated than were requested,
            // then `filteredReason` will describe the reason they were filtered out
            if (result.getFilteredReason() != null){
                Log.d("TAG", "FilteredReason: " + result.getFilteredReason());
            }

            // Handle the generated images
            List<ImagenInlineImage> images = result.getImages();
            for (ImagenInlineImage image : images) {
                Bitmap bitmap = image.asBitmap();
                // Use the bitmap to display the image in your UI
            }
        }

        @Override
        public void onFailure(Throwable t) {
            // ...
        }
    }, Executors.newSingleThreadExecutor());

### Web


    import { initializeApp } from "firebase/app";
    import { getAI, getGenerativeModel, GoogleAIBackend } from "firebase/ai";

    // TODO(developer) Replace the following with your app's Firebase configuration
    // See: https://firebase.google.com/docs/web/learn-more#config-object
    const firebaseConfig = {
      // ...
    };

    // Initialize FirebaseApp
    const firebaseApp = initializeApp(firebaseConfig);

    // Initialize the Gemini Developer API backend service
    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    // Create an `ImagenModel` instance with an Imagen model that supports your use case
    const model = getImagenModel(
      ai,
      {
        model: "imagen-4.0-generate-001",
        // Configure the model to generate multiple images for each request
        // See: https://firebase.google.com/docs/ai-logic/model-parameters
        generationConfig: {
          numberOfImages: 4
        }
      }
    );

    // Provide an image generation prompt
    const prompt = "An astronaut riding a horse.";

    // To generate images, call `generateImages` with the text prompt
    const response = await model.generateImages(prompt)

    // If fewer images were generated than were requested,
    // then `filteredReason` will describe the reason they were filtered out
    if (response.filteredReason) {
      console.log(response.filteredReason);
    }

    if (response.images.length == 0) {
      throw new Error("No images in the response.")
    }

    const images = response.images[0];

### Dart

    import 'package:firebase_ai/firebase_ai.dart';
    import 'package:firebase_core/firebase_core.dart';
    import 'firebase_options.dart';

    // Initialize FirebaseApp
    await Firebase.initializeApp(
      options: DefaultFirebaseOptions.currentPlatform,
    );

    // Initialize the Gemini Developer API backend service
    final ai = FirebaseAI.googleAI();

    // Create an `ImagenModel` instance with an Imagen model that supports your use case
    final model = ai.imagenModel(
      model: 'imagen-4.0-generate-001',
      // Configure the model to generate multiple images for each request
      // See: https://firebase.google.com/docs/ai-logic/model-parameters
      generationConfig: ImagenGenerationConfig(numberOfImages: 4),
    );

    // Provide an image generation prompt
    const prompt = 'An astronaut riding a horse.';

    // To generate images, call `generateImages` with the text prompt
    final response = await model.generateImages(prompt);

    // If fewer images were generated than were requested,
    // then `filteredReason` will describe the reason they were filtered out
    if (response.filteredReason != null) {
      print(response.filteredReason);
    }

    if (response.images.isNotEmpty) {
      final images = response.images;
      for(var image in images) {
      // Process the image
      }
    } else {
      // Handle the case where no images were generated
      print('Error: No images were generated.');
    }

### Unity


    using Firebase.AI;

    // Initialize the Gemini Developer API backend service
    var ai = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI());

    // Create an `ImagenModel` instance with a model that supports your use case
    var model = ai.GetImagenModel(
      modelName: "imagen-4.0-generate-001",
      // Configure the model to generate multiple images for each request
      // See: https://firebase.google.com/docs/ai-logic/model-parameters
      generationConfig: new ImagenGenerationConfig(numberOfImages: 4)
    );

    // Provide an image generation prompt
    var prompt = "An astronaut riding a horse";

    // To generate an image, call `generateImages` with the text prompt
    var response = await model.GenerateImagesAsync(prompt: prompt);

    // If fewer images were generated than were requested,
    // then `filteredReason` will describe the reason they were filtered out
    if (!string.IsNullOrEmpty(response.FilteredReason)) {
      UnityEngine.Debug.Log("Filtered reason: " + response.FilteredReason);
    }

    // Handle the generated images
    var images = response.Images.Select(image => image.AsTexture2D());

Learn how to choose a[model](https://firebase.google.com/docs/ai-logic/models)appropriate for your use case and app.

<br />

*** ** * ** ***

## Supported features and requirements

TheImagenmodels offer many features related to image generation. This section describes what's supported*when using the models withFirebase AI Logic*.

### Supported capabilities and features

| **Note:** Some of these capabilities and features aren't supported by theImagen 4models. See details about[Imagen 4](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate-001),[Imagen 4 Fast](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-fast-generate-001), and[Imagen 4 Ultra](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-ultra-generate-001)in theGoogle Clouddocumentation.

**Firebase AI Logicsupports these features ofImagenmodels:**

- Generating people, faces, and text within generated images

- [Editing images or including images in the request](https://firebase.google.com/docs/ai-logic/edit-images-imagen-overview)when using theVertex AIGemini API(currently only for Android and Flutter)

- Adding a watermark to generated images

- [Verifying digital watermarks](https://cloud.google.com/vertex-ai/generative-ai/docs/image/verify-watermark)when using theVertex AIGemini API  
  If you want to verify that an image has a watermark, you can upload the image intoVertex AI Studiousing its**Media**tab.

- Configuring[image generation parameters](https://firebase.google.com/docs/ai-logic/model-parameters), like number of generated images, aspect ratio, and watermarking

- Configuring[safety settings](https://firebase.google.com/docs/ai-logic/safety-settings)

**Firebase AI Logicdoes*not* support these advanced features ofImagenmodels:**

- [Setting the language of the input text](https://cloud.google.com/vertex-ai/generative-ai/docs/image/set-text-prompt-language)

- Disabling[prompt rewriter](https://cloud.google.com/vertex-ai/generative-ai/docs/image/use-prompt-rewriter)(the`enhancePrompt`parameter). This means that an LLM-based prompt rewriting tool will always automatically add more detail to the provided prompt to deliver higher quality images that better reflect the prompt provided.

- Writing a generated image directly intoGoogle Cloud Storageas part of the response from the model (the`storageUri`parameter). Instead, images are always returned as base64-encoded image bytes in the response.  
  If you want to upload a generated image toCloud Storage, you can use[Cloud Storage for Firebase](https://firebase.google.com/docs/storage).

### Specifications and limitations

|           Property (per request)            |                                                                              Value                                                                              |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Max number of input tokens                  | 480 tokens                                                                                                                                                      |
| Max number of output images                 | 4 images                                                                                                                                                        |
| Supported output image resolutions (pixels) | - 1024x1024 pixels (1:1 aspect ratio) - 896x1280 (3:4 aspect ratio) - 1280x896 (4:3 aspect ratio) - 768x1408 (9:16 aspect ratio) - 1408x768 (16:9 aspect ratio) |

<br />

*** ** * ** ***

## What else can you do?

- Start thinking about preparing for production (see the[production checklist](https://firebase.google.com/docs/ai-logic/production-checklist)), including:
  - [Setting upFirebase App Check](https://firebase.google.com/docs/ai-logic/app-check)to protect theGemini APIfrom abuse by unauthorized clients.
  - [IntegratingFirebase Remote Config](https://firebase.google.com/docs/ai-logic/solutions/remote-config)to update values in your app (like model name) without releasing a new app version.

<br />

#### Learn how to control content generation

- [Understand prompt design](https://firebase.google.com/docs/ai-logic/prompt-design), including best practices, strategies, and example prompts.
- [ConfigureImagenmodel parameters](https://firebase.google.com/docs/ai-logic/model-parameters)like aspect ratio, person generation, and watermarking.
- [Use safety settings](https://firebase.google.com/docs/ai-logic/safety-settings)to adjust the likelihood of getting responses that may be considered harmful.

<br />

<br />

#### Learn more about the supported models

Learn about the[models available for various use cases](https://firebase.google.com/docs/ai-logic/models)and their[quotas](https://firebase.google.com/docs/ai-logic/quotas)and[pricing](https://firebase.google.com/docs/ai-logic/pricing).

<br />

<br />

[Give feedback about your experience withFirebase AI Logic](https://firebase.google.com/docs/ai-logic/feedback)

<br />