# Source: https://docs.perplexity.ai/cookbook/showcase/perplexity-client.md

# Perplexity Client | Desktop AI Chat Interface with API Controls

> An Electron-based desktop client for Perplexity API with advanced features like temperature control, model selection, custom system prompts, and API debugging mode

**Perplexity Client** is an Electron-based desktop application that provides a polished interface for interacting with Perplexity's Sonar API. Unlike typical chat interfaces, it exposes advanced API parameters like temperature, top-p, and max tokens, making it ideal for developers who want fine-grained control over their AI interactions while enjoying a beautiful, macOS-inspired UI.

<img src="https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-main.png?fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=c91b22238629fc7e43163c6f76c222e7" alt="Perplexity Client Interface" data-og-width="1344" width="1344" data-og-height="750" height="750" data-path="cookbook/static/img/perplexity-client-main.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-main.png?w=280&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=001711ef8733edd16bc2e3ac5892227a 280w, https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-main.png?w=560&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=6725d11643c1a82cfbd32398bf55dd81 560w, https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-main.png?w=840&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=f43af5447d623db30453a61884b544a2 840w, https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-main.png?w=1100&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=c46c5a555d73aa083ce950a343f03cb9 1100w, https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-main.png?w=1650&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=8aa9d5aa5324d0b5ef8e994cd128b23c 1650w, https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-main.png?w=2500&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=5d266a4b15de3e1fcd48232b12d439c5 2500w" />

## Features

* **Multiple Sonar Models** with support for Sonar, Sonar Pro, and Sonar Reasoning Pro
* **Custom Spaces** with save/load functionality for different use cases
* **API Parameter Controls** including temperature, top-p, and max tokens adjustments
* **API Debugging Mode** showing full request/response payloads for troubleshooting
* **Token Usage Tracking** to monitor API consumption and costs
* **Focus Modes** for specialized tasks like coding, writing, and research

## Prerequisites

* Node.js v16 or higher
* npm or yarn
* Perplexity API key

## Installation

```bash  theme={null}
# Clone the repository
git clone https://github.com/straight-heart/Perplexity-client-.git
cd Perplexity-client-

# Install dependencies
npm install

npm run dev
```

## Build

Build the application for your platform:

```bash  theme={null}
npm run build:win    # Windows
npm run build:mac    # macOS
npm run build:linux  # Linux
```

## Configuration

API keys are managed directly within the application:

1. Launch the app and open Settings (gear icon)
2. In the **API Keys** section, click **Add Key**
3. Enter your Perplexity API key
4. The key is stored securely and persists across sessions

For custom system prompts, use the **Spaces** feature to save and switch between different instruction sets.

## Usage

1. **Launch**: Run `npm run dev` or use the built application
2. **Add API Key**: Open Settings and add your Perplexity API key
3. **Select Model**: Use the dropdown to choose between Sonar variants
4. **Create Spaces**: Set up custom system prompts for different tasks
5. **Chat**: Start conversing with real-time streaming responses
6. **Debug**: Enable API debugging to see full request/response details
7. **Track Usage**: Monitor token consumption in the Settings panel

## Screenshots

| Feature                      | Preview                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Spaces (Custom Instructions) | <img src="https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-spaces.png?fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=b9051c79cf4ee9117e0922590ee10283" alt="Spaces" data-og-width="313" width="313" data-og-height="103" height="103" data-path="cookbook/static/img/perplexity-client-spaces.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-spaces.png?w=280&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=84d5d584b1abc0207b44a2758a1b6e4a 280w, https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-spaces.png?w=560&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=4d96b50c0f6446bece3dbdf2e7160c89 560w, https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-spaces.png?w=840&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=30b7f87a6cd6693cfe58759f12cbd3f6 840w, https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-spaces.png?w=1100&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=83b5cf70ed53fe6d7c0b71d850fbf129 1100w, https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-spaces.png?w=1650&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=f99d9a5bbe1574a8d8b8ddbd48c0355c 1650w, https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-spaces.png?w=2500&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=47ca04dc84da5dfe82456697db752539 2500w" />                                     |
| Model & Parameter Controls   | <img src="https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-parameters.png?fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=1558ed437194b75a0a9e94e0cb47ef35" alt="Parameters" data-og-width="313" width="313" data-og-height="278" height="278" data-path="cookbook/static/img/perplexity-client-parameters.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-parameters.png?w=280&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=f680d93ca9ce05d5809b78d57a3535c8 280w, https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-parameters.png?w=560&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=9067dc369a2e3db2484c98e96f31a25a 560w, https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-parameters.png?w=840&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=55f1840797e497708443b0fa9d31b1ed 840w, https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-parameters.png?w=1100&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=f86b245eea7c67fbf57fdee93953ab98 1100w, https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-parameters.png?w=1650&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=3f665a802546a881b88c8a2c5ac849f7 1650w, https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-parameters.png?w=2500&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=da018c0456628131a9d51faa3c6cdbe1 2500w" /> |
| API Debugging Mode           | <img src="https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-debug.png?fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=867e92fc8519c4ea6370f5d50e64ac41" alt="Debug" data-og-width="828" width="828" data-og-height="555" height="555" data-path="cookbook/static/img/perplexity-client-debug.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-debug.png?w=280&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=673a1a3e6769a427faa564855f5614bd 280w, https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-debug.png?w=560&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=5ccb08897f42ba08fc0946d0921cb95c 560w, https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-debug.png?w=840&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=189033bd0ac67d74d5e4fc5e702ca17d 840w, https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-debug.png?w=1100&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=d7e9695d5ed6379b132d15d5e340c9e1 1100w, https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-debug.png?w=1650&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=edfdaa98e722ecbb43f615bc10141fd3 1650w, https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-debug.png?w=2500&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=b14f8ca08a495f594b3d8cf27d45557a 2500w" />                                              |
| Theme Selection              | <img src="https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-themes.png?fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=eed7ea3c2793e8716d8745d35ac4bff4" alt="Themes" data-og-width="473" width="473" data-og-height="216" height="216" data-path="cookbook/static/img/perplexity-client-themes.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-themes.png?w=280&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=256d6fc16437a82e8cd2c6cdb5fa8bcd 280w, https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-themes.png?w=560&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=151a3115311f92154e8e06aa0ca94dad 560w, https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-themes.png?w=840&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=fff48f1ad8916999ee5315219cda8aa1 840w, https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-themes.png?w=1100&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=cb1e5f917773192fabce806df7ba9b55 1100w, https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-themes.png?w=1650&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=0f6627cb65bcfd04a969790c11e86f3f 1650w, https://mintcdn.com/perplexity/0IKRIb5gmMrclqVS/cookbook/static/img/perplexity-client-themes.png?w=2500&fit=max&auto=format&n=0IKRIb5gmMrclqVS&q=85&s=64fa07121d3cfceb3d25ce8f3f973614 2500w" />                                     |

## Limitations

* Desktop only (Windows, macOS, Linux) — no mobile or web version
* Requires internet connection for API calls
* API key required for functionality

## Links

* [GitHub Repository](https://github.com/straight-heart/Perplexity-client-)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.perplexity.ai/llms.txt