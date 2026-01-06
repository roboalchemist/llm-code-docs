# Source: https://github.com/iOfficeAI/AionUi/wiki/AionUi-Image-Generation-Tool-Model-Configuration-Guide

# AionUi Image Generation Tool Model Configuration Guide

> This guide will help you configure multiple image generation models:
> 1) Gemini official 2.5 Flash Image Preview model configuration
> 2) OpenRouter platform paid image model configuration
> 3) Model selection and usage recommendations

**[English](AionUi-Image-Generation-Tool-Model-Configuration-Guide)** | [简体中文](AionUi-Image-Generation-Tool-Model-Configuration-Guide-Chinese)

---

## 1. Gemini Official Image Model Configuration (Recommended)

### 1.1 Get Gemini API Key

1. Visit Google AI Studio: `https://aistudio.google.com/`
2. Log in with your Google account.
3. Create a new API Key on the API Keys page.


### 1.2 Bind Gemini in AionUi

1. Open AionUi → Settings → LLM Settings.
2. Add new model, select "Google" platform.
3. Enter Gemini API Key and save.

![Configure LLM Example](assets/Images/configure%20llm.png)

### 1.3 Configure Gemini Image Model

1. Open AionUi → Settings → Tools Configuration → Image Generation Tool.
2. Select Gemini model that supports image generation from Google platform.
3. Confirm the model supports image generation functionality and save configuration.

![Set Tool LLM Example](assets/Images/set%20tool%20llm.png)

---

## 2. OpenRouter Platform Image Model Configuration

### 2.1 Get OpenRouter API Key

1. Visit `https://openrouter.ai/`, register and log in with Google / GitHub / email.
2. Open Keys page: `https://openrouter.ai/keys`.
3. Click "Create Key", name your key (e.g., "AionUi"), create and copy to save (only shown once).

![Create API Key Example](assets/Images/open%20router%20create%20key.jpeg)

**Important**: OpenRouter has discontinued free image models. You need to purchase credits to use paid models.

### 2.2 Bind OpenRouter in AionUi

1. Open AionUi → Settings → LLM Settings.
2. Add new model, select "OpenRouter" platform.
3. Paste the API Key copied in the previous step into the key input field and save.

### 2.3 Configure Image Model

1. Open AionUi → Settings → Tools Configuration → Image Generation Tool.
2. In model selection, choose models with image generation capabilities from OpenRouter platform:
   - Look for models containing keywords like `image`, `dall-e`, `midjourney`, `stable-diffusion`, `flux`
   - Select image generation models suitable for your needs
   - Pay attention to model pricing and usage limits

---

## 3. Verify Configuration Success

1. Return to chat, select LLM that supports tool calling to start new conversation.
2. Input "What tools do you have?" should show tool list including `image-generation`.
   ![Tool List Example](assets/Images/tool%20check.png)
3. Try sending image generation command, e.g.: "Generate a 1024×1024 blue neon cyberpunk city nightscape" to verify.
   ![Image Generation Test Example](assets/Images/image%20generation%20test.png)

---

## 4. Frequently Asked Questions

### 4.1 Model Selection Recommendations

In image generation tool settings, you need to select an image model. Choose appropriate model based on your needs:

- **High Quality**: Recommend Gemini 2.5 Flash Image Preview
- **Creative Design**: Choose models supporting high-quality image generation (like DALL-E series, Midjourney, etc.)
- **Fast Generation**: Choose models with faster generation speed (like Flux series, Gemini image models, etc.)

**Cost Considerations**:
- **Official Models**: Choose Gemini official models
- **Sufficient Budget**: Choose commercial image generation models for best quality
- **Balanced Cost-Performance**: Choose cost-effective image generation models

### 4.2 Configuration Issues
- **Invalid API Key**: Check if key is correctly copied and activated
- **Model Unavailable**: Confirm model name is correct and platform configuration is correct
- **Generation Failed**: Check network connection and ensure sufficient account balance

### 4.3 Usage Issues
- **Tools Not Showing**: Confirm image model is correctly configured, restart AionUi and retry
- **Poor Generation Quality**: Try adjusting prompt descriptions or switch to other image models
- **Slow Generation Speed**: Choose models with faster generation speed or check network connection

### 4.4 Platform Support Information
Currently AionUi supports image generation models from Gemini and OpenRouter platforms. We are continuously developing support for more platforms, including ModelScope, Hugging Face and other open-source model platforms. Stay tuned!

---

## 5. Reference Links

- **OpenRouter**: `https://openrouter.ai/` | `https://openrouter.ai/models`
- **Google AI Studio**: `https://aistudio.google.com/`
- **AionUi Official Documentation**: Check latest configuration instructions