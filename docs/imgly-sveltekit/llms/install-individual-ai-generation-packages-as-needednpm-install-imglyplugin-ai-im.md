# Install individual AI generation packages as needednpm install @imgly/plugin-ai-image-generation-webnpm install @imgly/plugin-ai-video-generation-webnpm install @imgly/plugin-ai-audio-generation-webnpm install @imgly/plugin-ai-text-generation-web
```

Import the providers from their respective packages:

```
// Import providers from individual AI generation packagesimport Anthropic from '@imgly/plugin-ai-text-generation-web/anthropic';import FalAiImage from '@imgly/plugin-ai-image-generation-web/fal-ai';import OpenAiImage from '@imgly/plugin-ai-image-generation-web/open-ai';import FalAiVideo from '@imgly/plugin-ai-video-generation-web/fal-ai';import Elevenlabs from '@imgly/plugin-ai-audio-generation-web/elevenlabs';
// Import middleware utilitiesimport { uploadMiddleware } from '@imgly/plugin-ai-generation-web';
```

## 2\. Initialize CE.SDK[#](#2-initialize-cesdk)

Initialize CE.SDK with Video mode to utilize all AI capabilities:

```
// Initialize CE.SDK with Video mode for full AI capabilitiesawait cesdk.addDefaultAssetSources();await cesdk.addDemoAssetSources({  sceneMode: 'Video',  withUploadAssetSources: true});
// Add navigation bar actionscesdk.ui.insertNavigationBarOrderComponent('last', {  id: 'ly.img.actions.navigationBar',  children: [    'ly.img.importScene.navigationBar',    'ly.img.exportImage.navigationBar'  ]});
// Create a video scene to utilize all AI capabilitiesawait cesdk.createVideoScene();
```

## 3\. Configure UI Components[#](#3-configure-ui-components)

### AI Dock Button[#](#ai-dock-button)

The main entry point for AI features is the AI dock button. Position it at the beginning of the dock:

```
// Configure AI Apps dock positioncesdk.ui.setDockOrder(['ly.img.ai.apps.dock', ...cesdk.ui.getDockOrder()]);
```

### Canvas Menu Options[#](#canvas-menu-options)

AI text and image transformations are available in the canvas context menu:

```
// Add AI options to canvas menucesdk.ui.setCanvasMenuOrder([  'ly.img.ai.text.canvasMenu',  'ly.img.ai.image.canvasMenu',  ...cesdk.ui.getCanvasMenuOrder()]);
```

## 4\. Add the AI Apps Plugin[#](#4-add-the-ai-apps-plugin)

Configure the AI Apps plugin with all providers:

```
// Add the AI Apps plugin with all providerscesdk.addPlugin(  AiApps({    // IMPORTANT: dryRun mode simulates generation without API calls    // Perfect for testing and development - remove for production use    dryRun: true,    providers: {      // Text generation and transformation      text2text: Anthropic.AnthropicProvider({        proxyUrl: 'http://your-proxy-server.com/api/proxy',        headers: {          'x-client-version': '1.0.0',          'x-request-source': 'cesdk-tutorial'        },        // Optional: Configure default property values        properties: {          temperature: { default: 0.7 },          maxTokens: { default: 500 }        }      }),
      // Image generation - Multiple providers with selection UI      text2image: [        FalAiImage.RecraftV3({          proxyUrl: 'http://your-proxy-server.com/api/proxy',          headers: {            'x-client-version': '1.0.0',            'x-request-source': 'cesdk-tutorial'          },          // Add upload middleware to store generated images on your server          middleware: [            uploadMiddleware(async (output) => {              // Upload the generated image to your server              const result = await uploadToYourStorageServer(output.url);
              // Return the output with your server's URL              return {                ...output,                url: result.permanentUrl              };            })          ]        }),        // Alternative with icon style support        FalAiImage.Recraft20b({          proxyUrl: 'http://your-proxy-server.com/api/proxy',          headers: {            'x-client-version': '1.0.0',            'x-request-source': 'cesdk-tutorial'          },          // Configure dynamic defaults based on style type          properties: {            style: { default: 'broken_line' },            image_size: { default: 'square_hd' }          }        }),        // Additional image provider for user selection        OpenAiImage.GptImage1.Text2Image({          proxyUrl: 'http://your-proxy-server.com/api/proxy',          headers: {            'x-api-key': 'your-key',            'x-request-source': 'cesdk-tutorial'          }        })      ],
      // Image-to-image transformation      image2image: FalAiImage.GeminiFlashEdit({        proxyUrl: 'https://your-server.com/api/fal-ai-proxy',        headers: {          'x-client-version': '1.0.0',          'x-request-source': 'cesdk-tutorial'        }      }),
      // Video generation - Multiple providers      text2video: [        FalAiVideo.MinimaxVideo01Live({          proxyUrl: 'https://your-server.com/api/fal-ai-proxy',          headers: {            'x-client-version': '1.0.0',            'x-request-source': 'cesdk-tutorial'          }        }),        FalAiVideo.PixverseV35TextToVideo({          proxyUrl: 'https://your-server.com/api/fal-ai-proxy',          headers: {            'x-client-version': '1.0.0',            'x-request-source': 'cesdk-tutorial'          }        })      ],      image2video: FalAiVideo.MinimaxVideo01LiveImageToVideo({        proxyUrl: 'https://your-server.com/api/fal-ai-proxy',        headers: {          'x-client-version': '1.0.0',          'x-request-source': 'cesdk-tutorial'        }      }),
      // Audio generation      text2speech: Elevenlabs.ElevenMultilingualV2({        proxyUrl: 'https://your-server.com/api/elevenlabs-proxy',        headers: {          'x-client-version': '1.0.0',          'x-request-source': 'cesdk-tutorial'        }      }),      text2sound: Elevenlabs.ElevenSoundEffects({        proxyUrl: 'https://your-server.com/api/elevenlabs-proxy',        headers: {          'x-client-version': '1.0.0',          'x-request-source': 'cesdk-tutorial'        }      })    }  }));
```

### Testing with Dry-Run Mode[#](#testing-with-dry-run-mode)

During development, use `dryRun: true` to simulate AI generation without making actual API calls:

```
// IMPORTANT: dryRun mode simulates generation without API calls// Perfect for testing and development - remove for production usedryRun: true,
```

This helps verify your integration and UI flows without incurring API costs or requiring valid API keys.

## 5\. AI Provider Configuration[#](#5-ai-provider-configuration)

Each AI provider type serves a specific purpose and creates different types of content:

### Text Generation (Anthropic)[#](#text-generation-anthropic)

```
// Text generation and transformationtext2text: Anthropic.AnthropicProvider({  proxyUrl: 'http://your-proxy-server.com/api/proxy',  headers: {    'x-client-version': '1.0.0',    'x-request-source': 'cesdk-tutorial'  },  // Optional: Configure default property values  properties: {    temperature: { default: 0.7 },    maxTokens: { default: 500 }  }}),
```

The text provider enables capabilities like:

*   Improving writing quality
*   Fixing spelling and grammar
*   Making text shorter or longer
*   Changing tone (professional, casual, friendly)
*   Translating to different languages
*   Custom text transformations

### Image Generation[#](#image-generation)

Configure multiple image providers with selection UI:

```
// Image generation - Multiple providers with selection UItext2image: [  FalAiImage.RecraftV3({    proxyUrl: 'http://your-proxy-server.com/api/proxy',    headers: {      'x-client-version': '1.0.0',      'x-request-source': 'cesdk-tutorial'    },    // Add upload middleware to store generated images on your server    middleware: [      uploadMiddleware(async (output) => {        // Upload the generated image to your server        const result = await uploadToYourStorageServer(output.url);
        // Return the output with your server's URL        return {          ...output,          url: result.permanentUrl        };      })    ]  }),  // Alternative with icon style support  FalAiImage.Recraft20b({    proxyUrl: 'http://your-proxy-server.com/api/proxy',    headers: {      'x-client-version': '1.0.0',      'x-request-source': 'cesdk-tutorial'    },    // Configure dynamic defaults based on style type    properties: {      style: { default: 'broken_line' },      image_size: { default: 'square_hd' }    }  }),  // Additional image provider for user selection  OpenAiImage.GptImage1.Text2Image({    proxyUrl: 'http://your-proxy-server.com/api/proxy',    headers: {      'x-api-key': 'your-key',      'x-request-source': 'cesdk-tutorial'    }  })],
// Image-to-image transformationimage2image: FalAiImage.GeminiFlashEdit({  proxyUrl: 'https://your-server.com/api/fal-ai-proxy',  headers: {    'x-client-version': '1.0.0',    'x-request-source': 'cesdk-tutorial'  }}),
```

When multiple providers are configured, users will see a selection box to choose between them.

Image generation features include:

*   Creating images from text descriptions
*   Multiple style options (realistic, illustration, vector)
*   Various size presets and custom dimensions
*   Transforming existing images based on text prompts

### Video Generation[#](#video-generation)

```
// Video generation - Multiple providerstext2video: [  FalAiVideo.MinimaxVideo01Live({    proxyUrl: 'https://your-server.com/api/fal-ai-proxy',    headers: {      'x-client-version': '1.0.0',      'x-request-source': 'cesdk-tutorial'    }  }),  FalAiVideo.PixverseV35TextToVideo({    proxyUrl: 'https://your-server.com/api/fal-ai-proxy',    headers: {      'x-client-version': '1.0.0',      'x-request-source': 'cesdk-tutorial'    }  })],image2video: FalAiVideo.MinimaxVideo01LiveImageToVideo({  proxyUrl: 'https://your-server.com/api/fal-ai-proxy',  headers: {    'x-client-version': '1.0.0',    'x-request-source': 'cesdk-tutorial'  }}),
```

Video generation capabilities include:

*   Creating videos from text descriptions
*   Transforming still images into videos
*   Fixed output dimensions (typically 1280×720)
*   5-second video duration

### Audio Generation (ElevenLabs)[#](#audio-generation-elevenlabs)

```
// Audio generationtext2speech: Elevenlabs.ElevenMultilingualV2({  proxyUrl: 'https://your-server.com/api/elevenlabs-proxy',  headers: {    'x-client-version': '1.0.0',    'x-request-source': 'cesdk-tutorial'  }}),text2sound: Elevenlabs.ElevenSoundEffects({  proxyUrl: 'https://your-server.com/api/elevenlabs-proxy',  headers: {    'x-client-version': '1.0.0',    'x-request-source': 'cesdk-tutorial'  }})
```

Audio generation features include:

*   Text-to-speech with multiple voices
*   Multilingual support
*   Adjustable speaking speed
*   Sound effect generation from text descriptions
*   Creating ambient sounds and effects

## 6\. Using Middleware[#](#6-using-middleware)

The AI generation framework supports middleware that can enhance or modify the generation process. Middleware functions are executed in sequence and can perform operations before generation, after generation, or both.

### Upload Middleware[#](#upload-middleware)

The `uploadMiddleware` is useful when you need to store generated content on your server before it’s used. First, create a helper function for your storage server:

```
/** * Upload to your image storage server. * Replace this mock with your actual storage API call. */async function uploadToYourStorageServer(imageUrl: string) {  // In production, upload the image to your server:  // const response = await fetch('https://your-server.com/api/store-image', {  //   method: 'POST',  //   headers: { 'Content-Type': 'application/json' },  //   body: JSON.stringify({  //     imageUrl,  //     metadata: { source: 'ai-generation' }  //   })  // });  // return await response.json();
  // Mock: Return a fake response  return { permanentUrl: imageUrl };}
```

Then use `uploadMiddleware` to process generated outputs before they’re added to the scene:

```
// Add upload middleware to store generated images on your servermiddleware: [  uploadMiddleware(async (output) => {    // Upload the generated image to your server    const result = await uploadToYourStorageServer(output.url);
    // Return the output with your server's URL    return {      ...output,      url: result.permanentUrl    };  })]
```

Use cases for upload middleware:

*   Storing generated assets in your own cloud storage
*   Adding watermarks or processing assets before use
*   Tracking/logging generated content
*   Implementing licensing or rights management

### Rate Limiting Middleware[#](#rate-limiting-middleware)

To prevent abuse of AI services, you can implement rate limiting:

```
import { rateLimitMiddleware } from '@imgly/plugin-ai-generation-web';
// In your provider configurationmiddleware: [  rateLimitMiddleware({    maxRequests: 10,    timeWindowMs: 60 * 60 * 1000, // 1 hour    onRateLimitExceeded: (input, options, info) => {      // Show a notice to the user      console.log(`Rate limit reached: ${info.currentCount}/${info.maxRequests}`);      return false; // Reject the request    }  })]
```

### Custom Error Handling Middleware[#](#custom-error-handling-middleware)

You can create custom middleware for error handling:

```
const errorMiddleware = async (input, options, next) => {  try {    return await next(input, options);  } catch (error) {    // Handle error (show UI notification, log, etc.)    console.error('Generation failed:', error);    // You can rethrow or return a fallback    throw error;  }};
```

### Middleware Order[#](#middleware-order)

The order of middleware is important - they’re executed in the sequence provided:

```
middleware: [  // Executes first  rateLimitMiddleware({ maxRequests: 10, timeWindowMs: 3600000 }),
  // Executes second (only if rate limit wasn't exceeded)  loggingMiddleware(),
  // Executes third (after generation completes)  uploadMiddleware(async (output) => { /* ... */ })]
```

## 7\. Controlling Features with Feature API[#](#7-controlling-features-with-feature-api)

You can control which AI features are available to users using CE.SDK’s Feature API:

```
// Control AI features with Feature API// Disable specific quick actionscesdk.feature.enable(  'ly.img.plugin-ai-image-generation-web.quickAction.editImage',  false);cesdk.feature.enable(  'ly.img.plugin-ai-text-generation-web.quickAction.translate',  false);
// Control input types for image/video generationcesdk.feature.enable(  'ly.img.plugin-ai-image-generation-web.fromText',  true);cesdk.feature.enable(  'ly.img.plugin-ai-image-generation-web.fromImage',  false);
// Hide provider selection dropdownscesdk.feature.enable(  'ly.img.plugin-ai-image-generation-web.providerSelect',  false);
// Control style groups for specific providerscesdk.feature.enable(  'ly.img.plugin-ai-image-generation-web.fal-ai/recraft-v3.style.vector',  false);
```

This is useful for:

*   Creating different feature tiers for different user groups
*   Simplifying the UI by hiding unused features
*   Temporarily disabling features during maintenance

For more details on available feature flags, see the [@imgly/plugin-ai-generation-web documentation](https://github.com/imgly/plugins/tree/main/packages/plugin-ai-generation-web#available-feature-flags).

## 8\. Proxy Server Configuration[#](#8-proxy-server-configuration)

For security reasons, you should never include your AI service API keys directly in client-side code. Instead, you should set up proxy services that securely forward requests to AI providers while keeping your API keys secure on the server side.

Each AI provider configuration requires a `proxyUrl` parameter, which should point to your server-side endpoint that handles authentication and forwards requests to the AI service:

```
text2image: FalAiImage.RecraftV3({    proxyUrl: 'http://your-proxy-server.com/api/proxy'});
```

Your proxy server should handle authentication, forward requests to the appropriate AI service providers, and manage response streaming for optimal performance.

## API Reference[#](#api-reference)

| Method | Category | Purpose |
| --- | --- | --- |
| `cesdk.addPlugin()` | Plugin | Register and initialize the AI Apps plugin with CE.SDK |
| `AiApps()` | Plugin | Create unified plugin instance with all AI provider types |
| `Anthropic.AnthropicProvider()` | Text | Configure Claude for text generation and transformation |
| `FalAiImage.RecraftV3()` | Image | Configure RecraftV3 text-to-image with vector/raster support |
| `FalAiImage.Recraft20b()` | Image | Configure Recraft20b text-to-image with icon styles |
| `FalAiImage.GeminiFlashEdit()` | Image | Configure Gemini Flash for image-to-image transformation |
| `OpenAiImage.GptImage1.Text2Image()` | Image | Configure GPT Image for text-to-image generation |
| `FalAiVideo.MinimaxVideo01Live()` | Video | Configure Minimax Video for text-to-video generation |
| `FalAiVideo.MinimaxVideo01LiveImageToVideo()` | Video | Configure Minimax Video for image-to-video transformation |
| `FalAiVideo.PixverseV35TextToVideo()` | Video | Configure Pixverse for text-to-video generation |
| `Elevenlabs.ElevenMultilingualV2()` | Audio | Configure ElevenLabs for multilingual text-to-speech |
| `Elevenlabs.ElevenSoundEffects()` | Audio | Configure ElevenLabs for sound effect generation |
| `uploadMiddleware()` | Middleware | Process and store generated outputs before use |
| `rateLimitMiddleware()` | Middleware | Limit generation requests per time window |
| `cesdk.feature.enable()` | Feature | Control visibility of AI features and providers |
| `cesdk.ui.setDockOrder()` | UI | Position AI Apps button in the dock |
| `cesdk.ui.setCanvasMenuOrder()` | UI | Add AI options to canvas context menu |
| `engine.asset.findAssets()` | Asset | Query generated assets from provider history sources |

## Next Steps[#](#next-steps)

*   [Proxy Server](sveltekit/user-interface/ai-integration/proxy-server-61f901/) — Set up secure API communication for production
*   [Text Generation](sveltekit/user-interface/ai-integration/text-generation-3e8302/) — Deep dive into text generation and transformation
*   [Image Generation](sveltekit/user-interface/ai-integration/image-generation-0540d9/) — Advanced image generation configuration
*   [Video Generation](sveltekit/user-interface/ai-integration/video-generation-b3122d/) — Video generation with multiple providers
*   [Audio Generation](sveltekit/user-interface/ai-integration/audio-generation-2d502a/) — Text-to-speech and sound effects
*   [Custom Provider](sveltekit/user-interface/ai-integration/custom-provider-16e851/) — Create custom AI providers
*   [Asset Library Basics](sveltekit/import-media/asset-panel/basics-f29078/) — Work with generated assets

---



[Source](https:/img.ly/docs/cesdk/sveltekit/user-interface/ai-integration/image-generation-0540d9)