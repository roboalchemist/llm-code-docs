# Source: https://firebase.google.com/docs/ai-logic/generate-images-gemini.md.txt

> [!WARNING]
> **Preview:** Using the Firebase AI Logic SDKs to generate and edit images with Gemini models is a feature that's in Preview, which means that it isn't subject to any SLA or deprecation policy and could change in backwards-incompatible ways.

<br />

[Video](https://www.youtube.com/watch?v=UznJQ2l7PaA)

You can ask a Gemini model to generate and edit images using
both text-only and text-and-image prompts. When you use Firebase AI Logic,
you can make this request directly from your app.

With this capability, you can do things like:

- Iteratively generate images through conversation with natural language,
  adjusting images while maintaining consistency and context.

- Generate images with high-quality text rendering, including long strings of
  text.

- Generate interleaved text-image output. For example, a blog post with text and
  images in a single turn. Previously, this required stringing together multiple
  models.

- Generate images using Gemini's world knowledge and reasoning capabilities.

You can find a
[complete list of supported modalities and capabilities](https://firebase.google.com/docs/ai-logic/generate-images-gemini#supported-modalities-and-capabilities)
(along with example prompts) later on this page.

> [!IMPORTANT]
> **Important:** When using a Gemini model for image generation, the model cannot return *only* images; it always returns *both* text and images. Also note that you must include `responseModalities: ["TEXT", "IMAGE"]` in your model configuration.

[Jump to code for text-to-image](https://firebase.google.com/docs/ai-logic/generate-images-gemini#text-to-image)
[Jump to code for interleaved text \& images](https://firebase.google.com/docs/ai-logic/generate-images-gemini#interleaved-text-and-images)

[Jump to code for image editing](https://firebase.google.com/docs/ai-logic/generate-images-gemini#edit-images)
[Jump to code for iterative image editing](https://firebase.google.com/docs/ai-logic/generate-images-gemini#iterative-image-editing)

<br />

|---|
| **See other guides for additional options for working with images** [Analyze images](https://firebase.google.com/docs/ai-logic/analyze-images) [Analyze images on-device](https://firebase.google.com/docs/ai-logic/hybrid) [Generate structured output](https://firebase.google.com/docs/ai-logic/generate-structured-output) |

### Choosing between Gemini and Imagen models

The Firebase AI Logic SDKs support image generation and editing using
either a Gemini model or an Imagen model.

**For most use cases, start with Gemini** , and then choose
Imagen only for specialized tasks where image quality is critical.

Choose [**Gemini**](https://firebase.google.com/docs/ai-logic/generate-images-gemini)
when you want:

- To use world knowledge and reasoning to generate contextually relevant images.
- To seamlessly blend text and images or to interleave text and image output.
- To embed accurate visuals within long text sequences.
- To edit images conversationally while maintaining context.

Choose [**Imagen**](https://firebase.google.com/docs/ai-logic/generate-images-imagen)
when you want:

- To prioritize image quality, photorealism, artistic detail, or specific styles (for example, impressionism or anime).
- To infuse branding, style, or generation of logos and product designs.
- To explicitly specify the aspect ratio or format of generated images.

## Before you begin


|---|
| *Click your Gemini API provider to view provider-specific content and code on this page.* <button value="dev" default="">Gemini Developer API</button> <button value="vertex">Vertex AI Gemini API</button> |

<br />

If you haven't already, complete the
[getting started guide](https://firebase.google.com/docs/ai-logic/get-started), which describes how to
set up your Firebase project, connect your app to Firebase, add the SDK,
initialize the backend service for your chosen Gemini API provider, and
create a `GenerativeModel` instance.


> [!NOTE]
> All our docs assume that you're using the [](https://firebase.google.com/support/releases)latest versions of the Firebase AI Logic SDKs.

<br />

For testing and iterating on your prompts, we recommend using [Google AI Studio](https://aistudio.google.com).

#### Models that support this capability

- `gemini-3-pro-image-preview` (aka "Nano Banana Pro")
- `gemini-3.1-flash-image-preview` (aka "Nano Banana 2")
- `gemini-2.5-flash-image` (aka "Nano Banana")

> [!NOTE]
> **Important** : Be aware of the following:
>
> - The image-generating Gemini models require the [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing) regardless of your Gemini API provider.
> - Image generation is *not* supported by the general-use Gemini Pro or Flash models like `gemini-3.1-pro-preview` or `gemini-2.5-flash`.
> - When using `gemini-3-pro-image-preview` or `gemini-3.1-flash-image-preview` via Vertex AI Gemini API, you must [set the location where you
>   access the model](https://firebase.google.com/docs/ai-logic/locations?api=vertex) to `global`.
> - Firebase AI Logic does *not* yet support explicitly setting `aspect_ratio` or `image_size` for generated images, but you can tell the model in your prompt what settings you want. These features are coming soon!

Note that the SDKs also support
[image generation using Imagen models](https://firebase.google.com/docs/ai-logic/generate-images-imagen).

## Generate and edit images

You can generate and edit images using a Gemini model.

### Generate images (text-only input)


|---|
| *Before trying this sample, complete the [Before you begin](https://firebase.google.com/docs/ai-logic/generate-images-gemini#before-you-begin) section of this guide to set up your project and app. **In that section, you'll also click a button for your chosen Gemini API provider so that you see provider-specific content on this page**.* |

<br />

You can ask a Gemini model to generate images by prompting with text.

Make sure to create a `GenerativeModel` instance, include
`responseModalities: ["TEXT", "IMAGE"]` in your model
configuration, and call `generateContent`.

### Swift


    import FirebaseAILogic

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a Gemini model that supports image output
    let generativeModel = FirebaseAI.firebaseAI(backend: .googleAI()).generativeModel(
      modelName: "gemini-2.5-flash-image",
      // Configure the model to respond with text and images (required)
      generationConfig: GenerationConfig(responseModalities: [.text, .image])
    )

    // Provide a text prompt instructing the model to generate an image
    let prompt = "Generate an image of the Eiffel tower with fireworks in the background."

    // To generate an image, call `generateContent` with the text input
    let response = try await model.generateContent(prompt)

    // Handle the generated image
    guard let inlineDataPart = response.inlineDataParts.first else {
      fatalError("No image data in response.")
    }
    guard let uiImage = UIImage(data: inlineDataPart.data) else {
      fatalError("Failed to convert data to UIImage.")
    }

### Kotlin


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a Gemini model that supports image output
    val model = Firebase.ai(backend = GenerativeBackend.googleAI()).generativeModel(
        modelName = "gemini-2.5-flash-image",
        // Configure the model to respond with text and images (required)
        generationConfig = generationConfig {
    responseModalities = listOf(ResponseModality.TEXT, ResponseModality.IMAGE) }
    )

    // Provide a text prompt instructing the model to generate an image
    val prompt = "Generate an image of the Eiffel tower with fireworks in the background."

    // To generate image output, call `generateContent` with the text input
    val generatedImageAsBitmap = model.generateContent(prompt)
        // Handle the generated image
        .candidates.first().content.parts.filterIsInstance<ImagePart>().firstOrNull()?.image

### Java


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a Gemini model that supports image output
    GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI()).generativeModel(
        "gemini-2.5-flash-image",
        // Configure the model to respond with text and images (required)
        new GenerationConfig.Builder()
            .setResponseModalities(Arrays.asList(ResponseModality.TEXT, ResponseModality.IMAGE))
            .build()
    );

    GenerativeModelFutures model = GenerativeModelFutures.from(ai);

    // Provide a text prompt instructing the model to generate an image
    Content prompt = new Content.Builder()
            .addText("Generate an image of the Eiffel Tower with fireworks in the background.")
            .build();

    // To generate an image, call `generateContent` with the text input
    ListenableFuture<GenerateContentResponse> response = model.generateContent(prompt);
    Futures.addCallback(response, new FutureCallback<GenerateContentResponse>() {
        @Override
        public void onSuccess(GenerateContentResponse result) { 
            // iterate over all the parts in the first candidate in the result object
            for (Part part : result.getCandidates().get(0).getContent().getParts()) {
                if (part instanceof ImagePart) {
                    ImagePart imagePart = (ImagePart) part;
                    // The returned image as a bitmap
                    Bitmap generatedImageAsBitmap = imagePart.getImage();
                    break;
                }
            }
        }

        @Override
        public void onFailure(Throwable t) {
            t.printStackTrace();
        }
    }, executor);

### Web


    import { initializeApp } from "firebase/app";
    import { getAI, getGenerativeModel, GoogleAIBackend, ResponseModality } from "firebase/ai";

    // TODO(developer) Replace the following with your app's Firebase configuration
    // See: https://firebase.google.com/docs/web/learn-more#config-object
    const firebaseConfig = {
      // ...
    };

    // Initialize FirebaseApp
    const firebaseApp = initializeApp(firebaseConfig);

    // Initialize the Gemini Developer API backend service
    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    // Create a `GenerativeModel` instance with a model that supports your use case
    const model = getGenerativeModel(ai, {
      model: "gemini-2.5-flash-image",
      // Configure the model to respond with text and images (required)
      generationConfig: {
        responseModalities: [ResponseModality.TEXT, ResponseModality.IMAGE],
      },
    });

    // Provide a text prompt instructing the model to generate an image
    const prompt = 'Generate an image of the Eiffel Tower with fireworks in the background.';

    // To generate an image, call `generateContent` with the text input
    const result = model.generateContent(prompt);

    // Handle the generated image
    try {
      const inlineDataParts = result.response.inlineDataParts();
      if (inlineDataParts?.[0]) {
        const image = inlineDataParts[0].inlineData;
        console.log(image.mimeType, image.data);
      }
    } catch (err) {
      console.error('Prompt or candidate was blocked:', err);
    }

### Dart


    import 'package:firebase_ai/firebase_ai.dart';
    import 'package:firebase_core/firebase_core.dart';
    import 'firebase_options.dart';

    await Firebase.initializeApp(
      options: DefaultFirebaseOptions.currentPlatform,
    );

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a Gemini model that supports image output
    final model = FirebaseAI.googleAI().generativeModel(
      model: 'gemini-2.5-flash-image',
      // Configure the model to respond with text and images (required)
      generationConfig: GenerationConfig(responseModalities: [ResponseModalities.text, ResponseModalities.image]),
    );

    // Provide a text prompt instructing the model to generate an image
    final prompt = [Content.text('Generate an image of the Eiffel Tower with fireworks in the background.')];

    // To generate an image, call `generateContent` with the text input
    final response = await model.generateContent(prompt);
    if (response.inlineDataParts.isNotEmpty) {
      final imageBytes = response.inlineDataParts[0].bytes;
      // Process the image
    } else {
      // Handle the case where no images were generated
      print('Error: No images were generated.');
    }

### Unity


    using Firebase;
    using Firebase.AI;

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a Gemini model that supports image output
    var model = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI()).GetGenerativeModel(
      modelName: "gemini-2.5-flash-image",
      // Configure the model to respond with text and images (required)
      generationConfig: new GenerationConfig(
        responseModalities: new[] { ResponseModality.Text, ResponseModality.Image })
    );

    // Provide a text prompt instructing the model to generate an image
    var prompt = "Generate an image of the Eiffel Tower with fireworks in the background.";

    // To generate an image, call `GenerateContentAsync` with the text input
    var response = await model.GenerateContentAsync(prompt);

    var text = response.Text;
    if (!string.IsNullOrWhiteSpace(text)) {
      // Do something with the text
    }

    // Handle the generated image
    var imageParts = response.Candidates.First().Content.Parts
                             .OfType<ModelContent.InlineDataPart>()
                             .Where(part => part.MimeType == "image/png");
    foreach (var imagePart in imageParts) {
      // Load the Image into a Unity Texture2D object
      UnityEngine.Texture2D texture2D = new(2, 2);
      if (texture2D.LoadImage(imagePart.Data.ToArray())) {
        // Do something with the image
      }
    }

### Generate interleaved images and text


|---|
| *Before trying this sample, complete the [Before you begin](https://firebase.google.com/docs/ai-logic/generate-images-gemini#before-you-begin) section of this guide to set up your project and app. **In that section, you'll also click a button for your chosen Gemini API provider so that you see provider-specific content on this page**.* |

<br />

You can ask a Gemini model to generate interleaved images with its
text responses. For example, you can generate images of what each step of a
generated recipe might look like along with the step's instructions, and you
don't have to make separate requests to the model or different models.

Make sure to create a `GenerativeModel` instance, include
`responseModalities: ["TEXT", "IMAGE"]` in your model
configuration, and call `generateContent`.

### Swift


    import FirebaseAILogic

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a Gemini model that supports image output
    let generativeModel = FirebaseAI.firebaseAI(backend: .googleAI()).generativeModel(
      modelName: "gemini-2.5-flash-image",
      // Configure the model to respond with text and images (required)
      generationConfig: GenerationConfig(responseModalities: [.text, .image])
    )

    // Provide a text prompt instructing the model to generate interleaved text and images
    let prompt = """
    Generate an illustrated recipe for a paella.
    Create images to go alongside the text as you generate the recipe
    """

    // To generate interleaved text and images, call `generateContent` with the text input
    let response = try await model.generateContent(prompt)

    // Handle the generated text and image
    guard let candidate = response.candidates.first else {
      fatalError("No candidates in response.")
    }
    for part in candidate.content.parts {
      switch part {
      case let textPart as TextPart:
        // Do something with the generated text
        let text = textPart.text
      case let inlineDataPart as InlineDataPart:
        // Do something with the generated image
        guard let uiImage = UIImage(data: inlineDataPart.data) else {
          fatalError("Failed to convert data to UIImage.")
        }
      default:
        fatalError("Unsupported part type: \(part)")
      }
    }

### Kotlin


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a Gemini model that supports image output
    val model = Firebase.ai(backend = GenerativeBackend.googleAI()).generativeModel(
        modelName = "gemini-2.5-flash-image",
        // Configure the model to respond with text and images (required)
        generationConfig = generationConfig {
    responseModalities = listOf(ResponseModality.TEXT, ResponseModality.IMAGE) }
    )

    // Provide a text prompt instructing the model to generate interleaved text and images
    val prompt = """
        Generate an illustrated recipe for a paella.
        Create images to go alongside the text as you generate the recipe
        """.trimIndent()

    // To generate interleaved text and images, call `generateContent` with the text input
    val responseContent = model.generateContent(prompt).candidates.first().content

    // The response will contain image and text parts interleaved
    for (part in responseContent.parts) {
        when (part) {
            is ImagePart -> {
                // ImagePart as a bitmap
                val generatedImageAsBitmap: Bitmap? = part.asImageOrNull()
            }
            is TextPart -> {
                // Text content from the TextPart
                val text = part.text
            }
        }
    }

### Java


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a Gemini model that supports image output
    GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI()).generativeModel(
        "gemini-2.5-flash-image",
        // Configure the model to respond with text and images (required)
        new GenerationConfig.Builder()
            .setResponseModalities(Arrays.asList(ResponseModality.TEXT, ResponseModality.IMAGE))
            .build()
    );

    GenerativeModelFutures model = GenerativeModelFutures.from(ai);

    // Provide a text prompt instructing the model to generate interleaved text and images
    Content prompt = new Content.Builder()
            .addText("Generate an illustrated recipe for a paella.\n" +
                     "Create images to go alongside the text as you generate the recipe")
            .build();

    // To generate interleaved text and images, call `generateContent` with the text input
    ListenableFuture<GenerateContentResponse> response = model.generateContent(prompt);
    Futures.addCallback(response, new FutureCallback<GenerateContentResponse>() {
        @Override
        public void onSuccess(GenerateContentResponse result) {
            Content responseContent = result.getCandidates().get(0).getContent();
            // The response will contain image and text parts interleaved
            for (Part part : responseContent.getParts()) {
                if (part instanceof ImagePart) {
                    // ImagePart as a bitmap
                    Bitmap generatedImageAsBitmap = ((ImagePart) part).getImage();
                } else if (part instanceof TextPart){
                    // Text content from the TextPart
                    String text = ((TextPart) part).getText();
                }
            }
        }

        @Override
        public void onFailure(Throwable t) {
            System.err.println(t);
        }
    }, executor);

### Web


    import { initializeApp } from "firebase/app";
    import { getAI, getGenerativeModel, GoogleAIBackend, ResponseModality } from "firebase/ai";

    // TODO(developer) Replace the following with your app's Firebase configuration
    // See: https://firebase.google.com/docs/web/learn-more#config-object
    const firebaseConfig = {
      // ...
    };

    // Initialize FirebaseApp
    const firebaseApp = initializeApp(firebaseConfig);

    // Initialize the Gemini Developer API backend service
    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    // Create a `GenerativeModel` instance with a model that supports your use case
    const model = getGenerativeModel(ai, {
      model: "gemini-2.5-flash-image",
      // Configure the model to respond with text and images (required)
      generationConfig: {
        responseModalities: [ResponseModality.TEXT, ResponseModality.IMAGE],
      },
    });

    // Provide a text prompt instructing the model to generate interleaved text and images
    const prompt = 'Generate an illustrated recipe for a paella.\n.' +
      'Create images to go alongside the text as you generate the recipe';

    // To generate interleaved text and images, call `generateContent` with the text input
    const result = await model.generateContent(prompt);

    // Handle the generated text and image
    try {
      const response = result.response;
      if (response.candidates?.[0].content?.parts) {
        for (const part of response.candidates?.[0].content?.parts) {
          if (part.text) {
            // Do something with the text
            console.log(part.text)
          }
          if (part.inlineData) {
            // Do something with the image
            const image = part.inlineData;
            console.log(image.mimeType, image.data);
          }
        }
      }

    } catch (err) {
      console.error('Prompt or candidate was blocked:', err);
    }

### Dart


    import 'package:firebase_ai/firebase_ai.dart';
    import 'package:firebase_core/firebase_core.dart';
    import 'firebase_options.dart';

    await Firebase.initializeApp(
      options: DefaultFirebaseOptions.currentPlatform,
    );

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a Gemini model that supports image output
    final model = FirebaseAI.googleAI().generativeModel(
      model: 'gemini-2.5-flash-image',
      // Configure the model to respond with text and images (required)
      generationConfig: GenerationConfig(responseModalities: [ResponseModalities.text, ResponseModalities.image]),
    );

    // Provide a text prompt instructing the model to generate interleaved text and images
    final prompt = [Content.text(
      'Generate an illustrated recipe for a paella\n ' +
      'Create images to go alongside the text as you generate the recipe'
    )];

    // To generate interleaved text and images, call `generateContent` with the text input
    final response = await model.generateContent(prompt);

    // Handle the generated text and image
    final parts = response.candidates.firstOrNull?.content.parts
    if (parts.isNotEmpty) {
      for (final part in parts) {
        if (part is TextPart) {
          // Do something with text part
          final text = part.text
        }
        if (part is InlineDataPart) {
          // Process image
          final imageBytes = part.bytes
        }
      }
    } else {
      // Handle the case where no images were generated
      print('Error: No images were generated.');
    }

### Unity


    using Firebase;
    using Firebase.AI;

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a Gemini model that supports image output
    var model = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI()).GetGenerativeModel(
      modelName: "gemini-2.5-flash-image",
      // Configure the model to respond with text and images (required)
      generationConfig: new GenerationConfig(
        responseModalities: new[] { ResponseModality.Text, ResponseModality.Image })
    );

    // Provide a text prompt instructing the model to generate interleaved text and images
    var prompt = "Generate an illustrated recipe for a paella \n" +
      "Create images to go alongside the text as you generate the recipe";

    // To generate interleaved text and images, call `GenerateContentAsync` with the text input
    var response = await model.GenerateContentAsync(prompt);

    // Handle the generated text and image
    foreach (var part in response.Candidates.First().Content.Parts) {
      if (part is ModelContent.TextPart textPart) {
        if (!string.IsNullOrWhiteSpace(textPart.Text)) {
          // Do something with the text
        }
      } else if (part is ModelContent.InlineDataPart dataPart) {
        if (dataPart.MimeType == "image/png") {
          // Load the Image into a Unity Texture2D object
          UnityEngine.Texture2D texture2D = new(2, 2);
          if (texture2D.LoadImage(dataPart.Data.ToArray())) {
            // Do something with the image
          }
        }
      }
    }

### Edit images (text-and-image input)


|---|
| *Before trying this sample, complete the [Before you begin](https://firebase.google.com/docs/ai-logic/generate-images-gemini#before-you-begin) section of this guide to set up your project and app. **In that section, you'll also click a button for your chosen Gemini API provider so that you see provider-specific content on this page**.* |

<br />

You can ask a Gemini model to edit images by prompting with text and
one or more images.

Make sure to create a `GenerativeModel` instance, include
`responseModalities: ["TEXT", "IMAGE"]` in your model
configuration, and call `generateContent`.

### Swift


    import FirebaseAILogic

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a Gemini model that supports image output
    let generativeModel = FirebaseAI.firebaseAI(backend: .googleAI()).generativeModel(
      modelName: "gemini-2.5-flash-image",
      // Configure the model to respond with text and images (required)
      generationConfig: GenerationConfig(responseModalities: [.text, .image])
    )

    // Provide an image for the model to edit
    guard let image = UIImage(named: "scones") else { fatalError("Image file not found.") }

    // Provide a text prompt instructing the model to edit the image
    let prompt = "Edit this image to make it look like a cartoon"

    // To edit the image, call `generateContent` with the image and text input
    let response = try await model.generateContent(image, prompt)

    // Handle the generated image
    guard let inlineDataPart = response.inlineDataParts.first else {
      fatalError("No image data in response.")
    }
    guard let uiImage = UIImage(data: inlineDataPart.data) else {
      fatalError("Failed to convert data to UIImage.")
    }

### Kotlin


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a Gemini model that supports image output
    val model = Firebase.ai(backend = GenerativeBackend.googleAI()).generativeModel(
        modelName = "gemini-2.5-flash-image",
        // Configure the model to respond with text and images (required)
        generationConfig = generationConfig {
    responseModalities = listOf(ResponseModality.TEXT, ResponseModality.IMAGE) }
    )

    // Provide an image for the model to edit
    val bitmap = BitmapFactory.decodeResource(context.resources, R.drawable.scones)

    // Provide a text prompt instructing the model to edit the image
    val prompt = content {
        image(bitmap)
        text("Edit this image to make it look like a cartoon")
    }

    // To edit the image, call `generateContent` with the prompt (image and text input)
    val generatedImageAsBitmap = model.generateContent(prompt)
        // Handle the generated text and image
        .candidates.first().content.parts.filterIsInstance<ImagePart>().firstOrNull()?.image

### Java


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a Gemini model that supports image output
    GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI()).generativeModel(
        "gemini-2.5-flash-image",
        // Configure the model to respond with text and images (required)
        new GenerationConfig.Builder()
            .setResponseModalities(Arrays.asList(ResponseModality.TEXT, ResponseModality.IMAGE))
            .build()
    );

    GenerativeModelFutures model = GenerativeModelFutures.from(ai);

    // Provide an image for the model to edit
    Bitmap bitmap = BitmapFactory.decodeResource(resources, R.drawable.scones);

    // Provide a text prompt instructing the model to edit the image
    Content promptcontent = new Content.Builder()
            .addImage(bitmap)
            .addText("Edit this image to make it look like a cartoon")
            .build();

    // To edit the image, call `generateContent` with the prompt (image and text input)
    ListenableFuture<GenerateContentResponse> response = model.generateContent(promptcontent);
    Futures.addCallback(response, new FutureCallback<GenerateContentResponse>() {
        @Override
        public void onSuccess(GenerateContentResponse result) {
            // iterate over all the parts in the first candidate in the result object
            for (Part part : result.getCandidates().get(0).getContent().getParts()) {
                if (part instanceof ImagePart) {
                    ImagePart imagePart = (ImagePart) part;
                    Bitmap generatedImageAsBitmap = imagePart.getImage();
                    break;
                }
            }
        }

        @Override
        public void onFailure(Throwable t) {
            t.printStackTrace();
        }
    }, executor);

### Web


    import { initializeApp } from "firebase/app";
    import { getAI, getGenerativeModel, GoogleAIBackend, ResponseModality } from "firebase/ai";

    // TODO(developer) Replace the following with your app's Firebase configuration
    // See: https://firebase.google.com/docs/web/learn-more#config-object
    const firebaseConfig = {
      // ...
    };

    // Initialize FirebaseApp
    const firebaseApp = initializeApp(firebaseConfig);

    // Initialize the Gemini Developer API backend service
    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    // Create a `GenerativeModel` instance with a model that supports your use case
    const model = getGenerativeModel(ai, {
      model: "gemini-2.5-flash-image",
      // Configure the model to respond with text and images (required)
      generationConfig: {
        responseModalities: [ResponseModality.TEXT, ResponseModality.IMAGE],
      },
    });

    // Prepare an image for the model to edit
    async function fileToGenerativePart(file) {
      const base64EncodedDataPromise = new Promise((resolve) => {
        const reader = new FileReader();
        reader.onloadend = () => resolve(reader.result.split(',')[1]);
        reader.readAsDataURL(file);
      });
      return {
        inlineData: { data: await base64EncodedDataPromise, mimeType: file.type },
      };
    }

    // Provide a text prompt instructing the model to edit the image
    const prompt = "Edit this image to make it look like a cartoon";

    const fileInputEl = document.querySelector("input[type=file]");
    const imagePart = await fileToGenerativePart(fileInputEl.files[0]);

    // To edit the image, call `generateContent` with the image and text input
    const result = await model.generateContent([prompt, imagePart]);

    // Handle the generated image
    try {
      const inlineDataParts = result.response.inlineDataParts();
      if (inlineDataParts?.[0]) {
        const image = inlineDataParts[0].inlineData;
        console.log(image.mimeType, image.data);
      }
    } catch (err) {
      console.error('Prompt or candidate was blocked:', err);
    }

### Dart


    import 'package:firebase_ai/firebase_ai.dart';
    import 'package:firebase_core/firebase_core.dart';
    import 'firebase_options.dart';

    await Firebase.initializeApp(
      options: DefaultFirebaseOptions.currentPlatform,
    );

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a Gemini model that supports image output
    final model = FirebaseAI.googleAI().generativeModel(
      model: 'gemini-2.5-flash-image',
      // Configure the model to respond with text and images (required)
      generationConfig: GenerationConfig(responseModalities: [ResponseModalities.text, ResponseModalities.image]),
    );

    // Prepare an image for the model to edit
    final image = await File('scones.jpg').readAsBytes();
    final imagePart = InlineDataPart('image/jpeg', image);

    // Provide a text prompt instructing the model to edit the image
    final prompt = TextPart("Edit this image to make it look like a cartoon");

    // To edit the image, call `generateContent` with the image and text input
    final response = await model.generateContent([
      Content.multi([prompt,imagePart])
    ]);

    // Handle the generated image
    if (response.inlineDataParts.isNotEmpty) {
      final imageBytes = response.inlineDataParts[0].bytes;
      // Process the image
    } else {
      // Handle the case where no images were generated
      print('Error: No images were generated.');
    }

### Unity


    using Firebase;
    using Firebase.AI;

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a Gemini model that supports image output
    var model = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI()).GetGenerativeModel(
      modelName: "gemini-2.5-flash-image",
      // Configure the model to respond with text and images (required)
      generationConfig: new GenerationConfig(
        responseModalities: new[] { ResponseModality.Text, ResponseModality.Image })
    );

    // Prepare an image for the model to edit
    var imageFile = System.IO.File.ReadAllBytes(System.IO.Path.Combine(
      UnityEngine.Application.streamingAssetsPath, "scones.jpg"));
    var image = ModelContent.InlineData("image/jpeg", imageFile);

    // Provide a text prompt instructing the model to edit the image
    var prompt = ModelContent.Text("Edit this image to make it look like a cartoon.");

    // To edit the image, call `GenerateContent` with the image and text input
    var response = await model.GenerateContentAsync(new [] { prompt, image });

    var text = response.Text;
    if (!string.IsNullOrWhiteSpace(text)) {
      // Do something with the text
    }

    // Handle the generated image
    var imageParts = response.Candidates.First().Content.Parts
                             .OfType<ModelContent.InlineDataPart>()
                             .Where(part => part.MimeType == "image/png");
    foreach (var imagePart in imageParts) {
      // Load the Image into a Unity Texture2D object
      Texture2D texture2D = new Texture2D(2, 2);
      if (texture2D.LoadImage(imagePart.Data.ToArray())) {
        // Do something with the image
      }
    }

### Iterate and edit images using multi-turn chat


|---|
| *Before trying this sample, complete the [Before you begin](https://firebase.google.com/docs/ai-logic/generate-images-gemini#before-you-begin) section of this guide to set up your project and app. **In that section, you'll also click a button for your chosen Gemini API provider so that you see provider-specific content on this page**.* |

<br />

Using multi-turn chat, you can iterate with a Gemini model on the
images that it generates or that you supply.

Make sure to create a `GenerativeModel` instance, include
`responseModalities: ["TEXT", "IMAGE"]` in your model
configuration, and call `startChat()` and `sendMessage()` to send new user
messages.

> [!IMPORTANT]
> **Important:** If you're not familiar with the chat capability of the SDKs, we recommend reviewing the [text-only chat example](https://firebase.google.com/docs/ai-logic/chat#chat-prompt).

### Swift


    import FirebaseAILogic

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a Gemini model that supports image output
    let generativeModel = FirebaseAI.firebaseAI(backend: .googleAI()).generativeModel(
      modelName: "gemini-2.5-flash-image",
      // Configure the model to respond with text and images (required)
      generationConfig: GenerationConfig(responseModalities: [.text, .image])
    )

    // Initialize the chat
    let chat = model.startChat()

    guard let image = UIImage(named: "scones") else { fatalError("Image file not found.") }

    // Provide an initial text prompt instructing the model to edit the image
    let prompt = "Edit this image to make it look like a cartoon"

    // To generate an initial response, send a user message with the image and text prompt
    let response = try await chat.sendMessage(image, prompt)

    // Inspect the generated image
    guard let inlineDataPart = response.inlineDataParts.first else {
      fatalError("No image data in response.")
    }
    guard let uiImage = UIImage(data: inlineDataPart.data) else {
      fatalError("Failed to convert data to UIImage.")
    }

    // Follow up requests do not need to specify the image again
    let followUpResponse = try await chat.sendMessage("But make it old-school line drawing style")

    // Inspect the edited image after the follow up request
    guard let followUpInlineDataPart = followUpResponse.inlineDataParts.first else {
      fatalError("No image data in response.")
    }
    guard let followUpUIImage = UIImage(data: followUpInlineDataPart.data) else {
      fatalError("Failed to convert data to UIImage.")
    }

### Kotlin


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a Gemini model that supports image output
    val model = Firebase.ai(backend = GenerativeBackend.googleAI()).generativeModel(
        modelName = "gemini-2.5-flash-image",
        // Configure the model to respond with text and images (required)
        generationConfig = generationConfig {
    responseModalities = listOf(ResponseModality.TEXT, ResponseModality.IMAGE) }
    )

    // Provide an image for the model to edit
    val bitmap = BitmapFactory.decodeResource(context.resources, R.drawable.scones)

    // Create the initial prompt instructing the model to edit the image
    val prompt = content {
        image(bitmap)
        text("Edit this image to make it look like a cartoon")
    }

    // Initialize the chat
    val chat = model.startChat()

    // To generate an initial response, send a user message with the image and text prompt
    var response = chat.sendMessage(prompt)
    // Inspect the returned image
    var generatedImageAsBitmap = response
        .candidates.first().content.parts.filterIsInstance<ImagePart>().firstOrNull()?.image

    // Follow up requests do not need to specify the image again
    response = chat.sendMessage("But make it old-school line drawing style")
    generatedImageAsBitmap = response
        .candidates.first().content.parts.filterIsInstance<ImagePart>().firstOrNull()?.image

### Java


    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a Gemini model that supports image output
    GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI()).generativeModel(
        "gemini-2.5-flash-image",
        // Configure the model to respond with text and images (required)
        new GenerationConfig.Builder()
            .setResponseModalities(Arrays.asList(ResponseModality.TEXT, ResponseModality.IMAGE))
            .build()
    );

    GenerativeModelFutures model = GenerativeModelFutures.from(ai);

    // Provide an image for the model to edit
    Bitmap bitmap = BitmapFactory.decodeResource(resources, R.drawable.scones);

    // Initialize the chat
    ChatFutures chat = model.startChat();

    // Create the initial prompt instructing the model to edit the image
    Content prompt = new Content.Builder()
            .setRole("user")
            .addImage(bitmap)
            .addText("Edit this image to make it look like a cartoon")
            .build();

    // To generate an initial response, send a user message with the image and text prompt
    ListenableFuture<GenerateContentResponse> response = chat.sendMessage(prompt);
    // Extract the image from the initial response
    ListenableFuture<@Nullable Bitmap> initialRequest = Futures.transform(response, result -> {
        for (Part part : result.getCandidates().get(0).getContent().getParts()) {
            if (part instanceof ImagePart) {
                ImagePart imagePart = (ImagePart) part;
                return imagePart.getImage();
            }
        }
        return null;
    }, executor);

    // Follow up requests do not need to specify the image again
    ListenableFuture<GenerateContentResponse> modelResponseFuture = Futures.transformAsync(
            initialRequest,
            generatedImage -> {
                Content followUpPrompt = new Content.Builder()
                        .addText("But make it old-school line drawing style")
                        .build();
                return chat.sendMessage(followUpPrompt);
            },
            executor);

    // Add a final callback to check the reworked image
    Futures.addCallback(modelResponseFuture, new FutureCallback<GenerateContentResponse>() {
        @Override
        public void onSuccess(GenerateContentResponse result) {
            for (Part part : result.getCandidates().get(0).getContent().getParts()) {
                if (part instanceof ImagePart) {
                    ImagePart imagePart = (ImagePart) part;
                    Bitmap generatedImageAsBitmap = imagePart.getImage();
                    break;
                }
            }
        }

        @Override
        public void onFailure(Throwable t) {
            t.printStackTrace();
        }
    }, executor);

### Web


    import { initializeApp } from "firebase/app";
    import { getAI, getGenerativeModel, GoogleAIBackend, ResponseModality } from "firebase/ai";

    // TODO(developer) Replace the following with your app's Firebase configuration
    // See: https://firebase.google.com/docs/web/learn-more#config-object
    const firebaseConfig = {
      // ...
    };

    // Initialize FirebaseApp
    const firebaseApp = initializeApp(firebaseConfig);

    // Initialize the Gemini Developer API backend service
    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    // Create a `GenerativeModel` instance with a model that supports your use case
    const model = getGenerativeModel(ai, {
      model: "gemini-2.5-flash-image",
      // Configure the model to respond with text and images (required)
      generationConfig: {
        responseModalities: [ResponseModality.TEXT, ResponseModality.IMAGE],
      },
    });

    // Prepare an image for the model to edit
    async function fileToGenerativePart(file) {
      const base64EncodedDataPromise = new Promise((resolve) => {
        const reader = new FileReader();
        reader.onloadend = () => resolve(reader.result.split(',')[1]);
        reader.readAsDataURL(file);
      });
      return {
        inlineData: { data: await base64EncodedDataPromise, mimeType: file.type },
      };
    }

    const fileInputEl = document.querySelector("input[type=file]");
    const imagePart = await fileToGenerativePart(fileInputEl.files[0]);

    // Provide an initial text prompt instructing the model to edit the image
    const prompt = "Edit this image to make it look like a cartoon";

    // Initialize the chat
    const chat = model.startChat();

    // To generate an initial response, send a user message with the image and text prompt
    const result = await chat.sendMessage([prompt, imagePart]);

    // Request and inspect the generated image
    try {
      const inlineDataParts = result.response.inlineDataParts();
      if (inlineDataParts?.[0]) {
        // Inspect the generated image
        const image = inlineDataParts[0].inlineData;
        console.log(image.mimeType, image.data);
      }
    } catch (err) {
      console.error('Prompt or candidate was blocked:', err);
    }

    // Follow up requests do not need to specify the image again
    const followUpResult = await chat.sendMessage("But make it old-school line drawing style");

    // Request and inspect the returned image
    try {
      const followUpInlineDataParts = followUpResult.response.inlineDataParts();
      if (followUpInlineDataParts?.[0]) {
        // Inspect the generated image
        const followUpImage = followUpInlineDataParts[0].inlineData;
        console.log(followUpImage.mimeType, followUpImage.data);
      }
    } catch (err) {
      console.error('Prompt or candidate was blocked:', err);
    }

### Dart


    import 'package:firebase_ai/firebase_ai.dart';
    import 'package:firebase_core/firebase_core.dart';
    import 'firebase_options.dart';

    await Firebase.initializeApp(
      options: DefaultFirebaseOptions.currentPlatform,
    );

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a Gemini model that supports image output
    final model = FirebaseAI.googleAI().generativeModel(
      model: 'gemini-2.5-flash-image',
      // Configure the model to respond with text and images (required)
      generationConfig: GenerationConfig(responseModalities: [ResponseModalities.text, ResponseModalities.image]),
    );

    // Prepare an image for the model to edit
    final image = await File('scones.jpg').readAsBytes();
    final imagePart = InlineDataPart('image/jpeg', image);

    // Provide an initial text prompt instructing the model to edit the image
    final prompt = TextPart("Edit this image to make it look like a cartoon");

    // Initialize the chat
    final chat = model.startChat();

    // To generate an initial response, send a user message with the image and text prompt
    final response = await chat.sendMessage([
      Content.multi([prompt,imagePart])
    ]);

    // Inspect the returned image
    if (response.inlineDataParts.isNotEmpty) {
      final imageBytes = response.inlineDataParts[0].bytes;
      // Process the image
    } else {
      // Handle the case where no images were generated
      print('Error: No images were generated.');
    }

    // Follow up requests do not need to specify the image again
    final followUpResponse = await chat.sendMessage([
      Content.text("But make it old-school line drawing style")
    ]);

    // Inspect the returned image
    if (followUpResponse.inlineDataParts.isNotEmpty) {
      final followUpImageBytes = response.inlineDataParts[0].bytes;
      // Process the image
    } else {
      // Handle the case where no images were generated
      print('Error: No images were generated.');
    }

### Unity


    using Firebase;
    using Firebase.AI;

    // Initialize the Gemini Developer API backend service
    // Create a `GenerativeModel` instance with a Gemini model that supports image output
    var model = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI()).GetGenerativeModel(
      modelName: "gemini-2.5-flash-image",
      // Configure the model to respond with text and images (required)
      generationConfig: new GenerationConfig(
        responseModalities: new[] { ResponseModality.Text, ResponseModality.Image })
    );

    // Prepare an image for the model to edit
    var imageFile = System.IO.File.ReadAllBytes(System.IO.Path.Combine(
      UnityEngine.Application.streamingAssetsPath, "scones.jpg"));
    var image = ModelContent.InlineData("image/jpeg", imageFile);

    // Provide an initial text prompt instructing the model to edit the image
    var prompt = ModelContent.Text("Edit this image to make it look like a cartoon.");

    // Initialize the chat
    var chat = model.StartChat();

    // To generate an initial response, send a user message with the image and text prompt
    var response = await chat.SendMessageAsync(new [] { prompt, image });

    // Inspect the returned image
    var imageParts = response.Candidates.First().Content.Parts
                             .OfType<ModelContent.InlineDataPart>()
                             .Where(part => part.MimeType == "image/png");
    // Load the image into a Unity Texture2D object
    UnityEngine.Texture2D texture2D = new(2, 2);
    if (texture2D.LoadImage(imageParts.First().Data.ToArray())) {
      // Do something with the image
    }

    // Follow up requests do not need to specify the image again
    var followUpResponse = await chat.SendMessageAsync("But make it old-school line drawing style");

    // Inspect the returned image
    var followUpImageParts = followUpResponse.Candidates.First().Content.Parts
                             .OfType<ModelContent.InlineDataPart>()
                             .Where(part => part.MimeType == "image/png");
    // Load the image into a Unity Texture2D object
    UnityEngine.Texture2D followUpTexture2D = new(2, 2);
    if (followUpTexture2D.LoadImage(followUpImageParts.First().Data.ToArray())) {
      // Do something with the image
    }

<br />

*** ** * ** ***

## Supported features, limitations, and best practices

### Supported modalities and capabilities

The following are supported modalities and capabilities for image-generating
Gemini models. Each capability shows an example prompt and has an
example code sample above.

- **Text Image(s)
  (text-only to image)**

  - *Generate an image of the Eiffel tower with fireworks in the background.*
- **Text Image(s)
  (text rendering within image)**

  - *Generate a cinematic photo of a large building with this giant text
    projection mapped on the front of the building.*
- **Text Image(s) \& Text
  (interleaved)**

  - *Generate an illustrated recipe for a paella. Create images alongside the
    text as you generate the recipe.*

  - *Generate a story about a dog in a 3D cartoon animation style.
    For each scene, generate an image.*

- **Image(s) \& Text Image(s) \& Text
  (interleaved)**

  - \[image of a furnished room\] + *What other color sofas would work in my space? Can you update the image?*
- **Image editing (text-and-image to image)**

  - \[image of scones\] + *Edit this image to make it look like a cartoon*

  - \[image of a cat\] + \[image of a pillow\] +
    *Create a cross stitch of my cat on this pillow.*

- **Multi-turn image editing (chat)**

  - \[image of a blue car\] + *Turn this car into a convertible.* , then *Now change the color to yellow.*

Additionally, the Gemini 3 Pro Image and
Gemini 3.1 Flash Image models support
[grounding with Google Search](https://firebase.google.com/docs/ai-logic/grounding-google-search).

### Limitations and best practices

Firebase AI Logic does ***not*** yet support explicitly setting
`aspect_ratio` or `image_size` for generated images, but you can tell the model
in your prompt what settings you want. These features are coming soon!

The following are limitations and best practices for image-output from a
Gemini model.

- Image-generating Gemini models support the following:

  - Generating PNG images with these maximum dimensions:
    - `gemini-3-pro-image-preview` and `gemini-3.1-flash-image-preview`: 4K
    - `gemini-2.5-flash-image`: 1024 px
  - Generating and editing images of people.
  - Using safety filters that provide a flexible and less restrictive user experience.
- Image-generating Gemini models do ***not*** support the following:

  - Including audio or video inputs.
  - Generating *only* images.  
    The models will always return *both* text and images, and you must include `responseModalities: ["TEXT", "IMAGE"]` in your model configuration.
- For best performance, use the following languages:
  `en`, `es-mx`, `ja-jp`, `zh-cn`, `hi-in`.

- Image generation may not always trigger. Here are some known issues:

  - The model may output text only.  

    Try asking for image outputs explicitly (for example, "generate an image",
    "provide images as you go along", "update the image").

  - The model may stop generating partway through.  

    Try again or try a different prompt.

  - The model may generate text as an image.  

    Try asking for text outputs explicitly. For example, "generate narrative
    text along with illustrations."

- When generating text for an image, Gemini works best if you first
  generate the text and then ask for an image with the text.