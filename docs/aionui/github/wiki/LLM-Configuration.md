# Source: https://github.com/iOfficeAI/AionUi/wiki/LLM-Configuration

# ⚙️ AionUi LLM Configuration Tutorial

This tutorial will detail how to configure various large language models in AionUi, including Gemini, OpenAI, ModelScope, OpenRouter and other platforms, as well as advanced features like multi-API key rotation.

**[English](LLM-Configuration)** | [简体中文](LLM-Configuration-Chinese)

## 🎯 Configuration Overview

AionUi supports multiple LLM platforms, each with different configuration methods:

| Platform | Authentication | Multi-Key Support | Special Features |
|----------|----------------|-------------------|------------------|
| **Gemini** | API Key / Google Login | ✅ | Image generation, tool calling |
| **OpenAI** | API Key | ✅ | Function calling, image generation |
| **ModelScope** | API Key | ❌ | Chinese optimization |
| **OpenRouter** | API Key | ❌ | Multi-model aggregation |
| **Custom Platform** | API Key | ✅ | OpenAI-compatible interface |

---

## 🌟 Method 1: Google Account Login (Recommended)

### Advantages
- **No API Key Required**: Direct Google account login
- **Auto Update**: Token automatically refreshes, no manual maintenance
- **Secure & Reliable**: Uses OAuth 2.0 standard authentication
- **Complete Features**: Supports all Gemini functionality

### Configuration Steps

1. **Enter Gemini Settings**
   - Click the "Settings" icon in the left sidebar
   - Select "Gemini Settings"

2. **Google Login**
   - Click the "Google Login" button
   - Complete Google account login in the popup browser window
   - Authorize AionUi to access your Google account

![Google login configuration screenshot - showing login button and authorization page](assets/Images/login%20before.png)

3. **Verify Login Status**
   - After successful login, the interface will display your Google account information
   - You can click "Logout" button to switch accounts

![Google account status screenshot - showing logged-in account info](assets/Images/login%20setting.png)

### Common Login Issues

If you encounter problems with Google login, try the following solutions:

#### 1. Network Issues
- **VPN Setup**: It's recommended to set VPN to US region
- **Proxy Configuration**: Fill in proxy address in Gemini settings
- **Network Check**: Ensure stable network connection and normal access to Google services

#### 2. Cloud Project ID Issues
- **Solution**: Need to create Google Cloud Project, detailed steps please refer to the "📋 Google Cloud Project ID Creation Detailed Tutorial" section in [Getting Started Guide](Getting-Started)

---

## 🔑 Method 2: API Key Configuration

![LLM configuration interface screenshot - showing model configuration and platform selection](assets/Images/model%20setting.png)

### Gemini Platform Configuration

1. **Get Gemini API Key**
   - Visit [Google AI Studio](https://aistudio.google.com/)
   - Login with Google account
   - Create new API Key in "API Keys" page

2. **Configure in AionUi**
   - Click the "Settings" icon in the left sidebar
   - Select "Model Settings"
   - Click "Add Model" button
   - Select platform: **Gemini**
   - Enter API Key
   - System will automatically fetch available model list


### Custom Platform Configuration

1. **Get API Key**
   - Visit the corresponding platform's API Key management page
   - Login to account and create new API Key
   - Copy API Key for later use

2. **Configure in AionUi**
   - Select platform: **Custom Platform**
   - Enter corresponding Base URL
   - Enter API Key
   - Select models to use

**Common Platform Base URLs**:
- **OpenAI**: `https://api.openai.com/v1`
- **Anthropic**: `https://api.anthropic.com/v1`
- **xAI**: `https://api.x.ai/v1`
- **DeepSeek**: `https://api.deepseek.com`
- **Moonshot**: `https://api.moonshot.cn/v1`
- **Zhipu**: `https://open.bigmodel.cn/api/paas/v4`


### ModelScope Platform Configuration

1. **Get ModelScope API Key**
   - Visit [ModelScope](https://modelscope.cn/my/myaccesstoken)
   - Login with Alibaba Cloud account
   - Create access token

2. **Configure in AionUi**
   - Select platform: **ModelScope**
   - Base URL: `https://api-inference.modelscope.cn/v1`
   - Enter ModelScope API Key
   - Select models (like qwen-turbo, qwen-plus, etc.)


### OpenRouter Platform Configuration

1. **Get OpenRouter API Key**
   - Visit [OpenRouter](https://openrouter.ai/keys)
   - Register OpenRouter account
   - Create API Key

2. **Configure in AionUi**
   - Select platform: **OpenRouter**
   - Base URL: `https://openrouter.ai/api/v1`
   - Enter OpenRouter API Key
   - Select models (supports various open-source and commercial models)


---

## 🔄 Multi-API Key Rotation Configuration

### Feature Description
AionUi supports automatic multi-API key rotation to improve service reliability and availability:

- **Automatic Rotation**: Automatically switch to next key when current key encounters errors
- **Smart Blacklist**: Failed keys are temporarily blacklisted for 90 seconds
- **Error Recovery**: Blacklisted keys automatically recover after expiration
- **Load Balancing**: Randomly select starting key to distribute request pressure

### Configuration Method

1. **Enter Multiple Keys in API Key Field**
   ```
   sk-xxx1,sk-xxx2,sk-xxx3
   ```
   Or use line breaks:
   ```
   sk-xxx1
   sk-xxx2
   sk-xxx3
   ```

2. **Supported Platforms**
   - ✅ **Gemini**: Supports multi-key rotation
   - ✅ **OpenAI**: Supports multi-key rotation
   - ❌ **ModelScope**: Not currently supported
   - ❌ **OpenRouter**: Not currently supported

![Multi-API Key configuration screenshot - showing multiple key input format](assets/Images/multi-key.png)

### Rotation Mechanism Details

1. **Error Detection**
   - Detect errors like 401 (authentication failed), 429 (rate limit), 503 (service unavailable)
   - Automatically add current key to blacklist

2. **Automatic Switching**
   - Randomly select next key from available key list
   - Update environment variables, reinitialize client

3. **Blacklist Management**
   - Failed keys are blacklisted for 90 seconds
   - Blacklisted keys automatically recover after expiration
   - Avoid performance issues from frequent switching

---

## ❓ Common Questions

### Q: How to know if configuration is successful?
**A**: Check methods:
- Can see configured platforms and models in model list
- Can select configured models in conversation interface
- Can receive normal replies when sending messages

### Q: Multi-API key rotation not working?
**A**: Check points:
- Ensure key format is correct (comma or line break separated)
- Check if platform supports multi-key (currently only Gemini and OpenAI support)
- Check console logs to understand rotation status

### Q: Model list empty or loading failed?
**A**: Possible reasons:
- API key invalid or expired
- Base URL configuration error
- Network connection issues
- Platform service temporarily unavailable

### Q: How to switch between different models?
**A**: Switching methods:
- Select different models when starting a new conversation
- Model switching during current conversation is not currently supported
- System will remember your selection preferences

### Q: Configured models not visible in conversation?
**A**: Check configuration:
- Ensure model supports `function_calling` capability
- Re-save configuration and restart application

---

## 📚 Related Documentation

- **Quick Start**: [Quick Start Guide](Getting-Started)
- **Image Generation Configuration**: [Image Generation Setup](AionUi-Image-Generation-Tool-Model-Configuration-Guide)
- **Multi-Agent Mode Configuration**: [Multi-Agent Mode Setup](ACP-Setup)
- **Common Questions**: [FAQ](FAQ)

---

**Need Help?**
- 🐛 [Report Issues](https://github.com/iOfficeAI/AionUi/issues)
- 💬 [Community Discussions](https://github.com/iOfficeAI/AionUi/discussions)
- 📖 [Complete Documentation](Home)

*After configuration, you can enjoy multi-platform, multi-model AI experience!*