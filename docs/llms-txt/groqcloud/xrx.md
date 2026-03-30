# Source: https://console.groq.com/docs/xrx

---
description: Learn how to build AI-powered, multimodal applications with xRx and Groq, supporting text, voice, reasoning, and more.
title: xRx + Groq: Easily Build Rich Multi-Modal Experiences - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## [xRx + Groq: Easily Build Rich Multi-Modal Experiences](#xrx--groq-easily-build-rich-multimodal-experiences)

[xRx](https://github.com/8090-inc/xrx-core) is an open-source framework for building AI-powered applications that interact with users across multiple modalities — multimodality input (x), reasoning (R), and multimodality output (x). It allows developers to create sophisticated AI systems that seamlessly integrate text, voice, and other interaction forms, providing users with truly immersive experiences.

**Key Features:**

* **Multimodal Interaction**: Effortlessly integrate audio, text, widgets and other modalities for both input and output.
* **Advanced Reasoning**: Utilize comprehensive reasoning systems to enhance user interactions with intelligent and context-aware responses.
* **Modular Architecture**: Easily extend and customize components with a modular system of reusable building blocks.
* **Observability and Guardrails**: Built-in support for LLM observability and guardrails, allowing developers to monitor, debug, and optimize reasoning agents effectively.

### [Quick Start Guide (2 minutes + build time)](#quick-start-guide-2-minutes--build-time)

The easiest way to use xRx is to start with an example app and customize it. You can either explore the sample apps collection or try our AI voice tutor for calculus that includes a whiteboard and internal math engine.

### [Option 1: Sample Apps Collection](#option-1-sample-apps-collection)

#### [1\. Clone the Repository](#1-clone-the-repository)

curl

```
git clone --recursive https://github.com/8090-inc/xrx-sample-apps.git
```

Note: The `--recursive` flag is required as each app uses the xrx-core submodule.

#### [2\. Navigate to Sample Apps](#2-navigate-to-sample-apps)

curl

```
cd xrx-sample-apps
```

#### [3\. Choose and Configure an Application](#3-choose-and-configure-an-application)

1. Navigate to your chosen app's directory
2. Copy the environment template:  
curl  
```  
cp env-example.txt .env  
```
3. Configure the required environment variables:  
   * Each application has its own set of required variables  
   * Check the `.env.example` file in the app's directory  
   * Set all required API keys and configuration

> **Tip**: We recommend opening only the specific app folder in your IDE for a cleaner workspace.

#### [4\. Follow App-Specific Setup](#4-follow-appspecific-setup)

* Each application has its own README with specific instructions
* Complete any additional setup steps outlined in the app's README
* Ensure all dependencies are properly configured

#### [5\. Launch the Application](#5-launch-the-application)

curl

```
docker-compose up --build
```

Your app will be available at `localhost:3000`

For detailed instructions and troubleshooting, refer to the README in each application's directory.

### [Option 2: AI Voice Tutor](#option-2-ai-voice-tutor)

[Math-Tutor on Groq](https://github.com/bklieger-groq/mathtutor-on-groq) is a voice-enabled math tutor powered by Groq that calculates and renders live problems and instruction with LaTeX in seconds! The application demonstrates voice interaction, whiteboard capabilities, and mathematical abilties.

#### [1\. Clone the Repository](#1-clone-the-repository)

curl

```
git clone --recursive https://github.com/bklieger-groq/mathtutor-on-groq.git
```

#### [2\. Configure Environment](#2-configure-environment)

curl

```
cp env-example.txt .env
```

Edit `.env` with your API keys:

curl

```
LLM_API_KEY="your_groq_api_key_here"
GROQ_STT_API_KEY="your_groq_api_key_here"
ELEVENLABS_API_KEY="your_elevenlabs_api_key"  # For text-to-speech
```

You can obtain:

* Groq API key from the [Groq Console](https://console.groq.com)
* [ElevenLabs API key](https://elevenlabs.io/app/settings/api-keys) for voice synthesis

#### [3\. Launch the Tutor](#3-launch-the-tutor)

curl

```
docker-compose up --build
```

Access the tutor at `localhost:3000`

**Challenge**: Modify the math tutor to teach another topic, such as economics, and accept images of problems as input!

For more information on building applications with xRx and Groq, see:

* [xRx Documentation](https://github.com/8090-inc/xrx-sample-apps)
* [xRx Example Applications](https://github.com/8090-inc/xrx-sample-apps)
* [xRx Video Walkthrough](https://www.youtube.com/watch?v=qyXTjpLvg74)