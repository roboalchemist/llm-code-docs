# Source: https://github.com/iOfficeAI/AionUi/wiki/FAQ

# ❓ AionUi Frequently Asked Questions

This FAQ covers the most common questions and issues users encounter when using AionUi.

**[English](FAQ)** | [简体中文](FAQ-Chinese)

---

## 🚀 Installation & Setup

### Q: How do I install AionUi?

**A:** AionUi is available for Windows, macOS, and Linux. Download the latest release from our [GitHub releases page](https://github.com/iOfficeAI/AionUi/releases) and follow the installation instructions for your operating system.

### Q: What are the system requirements?

**A:** 
- **Operating System**: Windows 10+, macOS 10.15+, or Linux (Ubuntu 18.04+)
- **Memory**: Minimum 4GB RAM, recommended 8GB+
- **Storage**: At least 2GB free space
- **Network**: Internet connection for AI model access

### Q: Can I run AionUi on older operating systems?

**A:** AionUi requires modern operating systems due to its Electron-based architecture. We recommend updating to supported versions for the best experience.

---

## 🔑 Authentication & API Keys

### Q: Do I need to create API keys for all platforms?

**A:** No, you can start with just one platform. We recommend beginning with Google Gemini (free) or OpenAI (if you have credits). You can add more platforms later as needed.

### Q: How do I get a Google Gemini API key?

**A:** 
1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Navigate to "Get API Key" and create a new key
4. Copy the key and paste it into AionUi's LLM settings

### Q: My API key isn't working. What should I check?

**A:** 
- Verify the key is correctly copied (no extra spaces or characters)
- Check if the key has expired or been revoked
- Ensure you have sufficient credits/quota remaining
- Try regenerating the key from the platform's dashboard

### Q: Can I use multiple API keys for the same platform?

**A:** Yes! AionUi supports multiple API keys per platform with automatic rotation. This helps with rate limits and reliability.

---

## 🤖 AI Models & Agents

### Q: What's the difference between Gemini CLI and Multi-Agent Mode?

**A:** Main differences:
- **Gemini CLI Mode**: AionUi's built-in core functionality, used by default after download, supports image generation, tool scheduling and other complete features
- **Multi-Agent Mode**: Requires users to install external CLI tools themselves, AionUi recognizes and integrates them through ACP protocol, currently has relatively simple functionality, future MCP settings will enhance integration

### Q: Which agent should I choose?

**A:** Selection recommendations:
- **Daily use**: Recommend Gemini CLI mode, most complete functionality, ready to use out of the box
- **Professional needs**: If you need specific CLI tool functionality (like Claude Code, Qwen Code, etc.), choose Multi-Agent Mode
- **Future planning**: MCP functionality will allow Multi-Agent Mode to enjoy more unified features

### Q: How do I switch between different AI models?

**A:** Model switching is not currently supported. Switching to different agents will automatically use their default models:
- Gemini CLI Mode: Uses configured default models
- Multi-Agent Mode: Choose different agents on the welcome page, each agent uses its default model
- **Note**: Model switching during current conversation is not currently supported

### Q: Why can't I see image generation tools?

**A:** Check the following configuration:
- Enable image generation in "Tools Settings"
- Select a model that supports image generation
- Refer to [Image Generation Configuration Guide](AionUi-Image-Generation-Tool-Model-Configuration-Guide)

---

## 🖼️ Image Generation

### Q: Which image generation models are recommended?

**A:** We recommend Gemini 2.5 Flash Image Preview for high-quality image generation. Check Google AI Studio for current pricing policies.

### Q: How do I configure image generation?

**A:** 
1. Set up a platform with image models (Gemini or OpenRouter)
2. Go to Settings → Tools → Image Generation
3. Select an image generation model
4. Test with a simple prompt like "Generate a sunset landscape"

### Q: My image generation is slow. How can I improve it?

**A:** 
- Choose faster models (like Gemini image models)
- Reduce image resolution requirements
- Check your internet connection
- Consider upgrading to premium models for better performance

---

## 🔧 Configuration & Settings

### Q: Where are my settings stored?

**A:** All conversations are saved locally:
- **macOS**: `~/Library/Application Support/AionUi/`
- **Windows**: `%APPDATA%/AionUi/`
- **Linux**: `~/.config/AionUi/`

### Q: How do I backup my configuration?

**A:** 
1. Manually copy the configuration file directory
2. Export your configuration file
3. Store it safely for future restoration

### Q: Can I reset AionUi to default settings?

**A:** Yes, you can reset settings:
1. Close AionUi completely
2. Delete the configuration folder
3. Restart AionUi to create fresh settings

---

## 🚨 Troubleshooting

### Q: AionUi won't start. What should I do?

**A:** 
1. Check if another instance is already running
2. Restart your computer
3. Reinstall AionUi if the problem persists
4. Check our [GitHub issues](https://github.com/iOfficeAI/AionUi/issues) for known problems

### Q: I'm getting "API key invalid" errors.

**A:** 
- Verify the key is correctly entered
- Check if the key has expired
- Ensure you have sufficient credits
- Try regenerating the key

### Q: My conversations are not saving.

**A:** 
- Check if you have write permissions to the AionUi data directory
- Ensure sufficient disk space is available
- Try restarting AionUi

### Q: The interface is slow or unresponsive.

**A:** 
- Close unnecessary applications to free up memory
- Check your internet connection
- Try reducing the number of concurrent conversations
- Restart AionUi

---

## 🔄 Updates & Maintenance

### Q: How do I update AionUi?

**A:** 
- **Automatic**: AionUi will notify you of updates
- **Manual**: Download the latest version from GitHub releases
- **Settings**: Check for updates in Settings → About

### Q: Will updating affect my settings and conversations?

**A:** No, updates preserve your settings and conversation history. However, we recommend backing up important data before major updates.

### Q: How often is AionUi updated?

**A:** We release updates regularly with new features, bug fixes, and improvements. Follow our [GitHub releases](https://github.com/iOfficeAI/AionUi/releases) for the latest updates.

---

## 🔒 Security & Privacy

### Q: Is my data secure?

**A:** 
- Conversations are stored locally on your device
- API keys are encrypted and stored securely
- We don't collect personal data without your consent
- Review our privacy policy for detailed information

### Q: How do I delete my conversation history?

**A:** 
1. Manually delete conversation data from the configuration file directory
2. Or delete the entire configuration folder to reset all data
3. Restart AionUi to apply changes

---


## 🤝 Community & Support

### Q: Where can I get help?

**A:** 
- **GitHub Issues**: Report bugs and request features
- **GitHub Discussions**: Ask questions and share tips
- **Documentation**: Check our comprehensive guides
- **Community**: Join our user community for support

### Q: How can I contribute to AionUi?

**A:** 
- **Code**: Submit pull requests for bug fixes and features
- **Documentation**: Help improve our guides and tutorials
- **Testing**: Report issues and provide feedback
- **Community**: Help other users in discussions

### Q: Is AionUi open source?

**A:** Yes! AionUi is open source and available on GitHub. We welcome contributions from the community.

---

## 📚 Additional Resources

- **[Getting Started Guide](Getting-Started)**: Complete setup tutorial
- **[LLM Configuration](LLM-Configuration)**: Detailed model setup guide
- **[Multi-Agent Mode Setup](ACP-Setup)**: External CLI tool integration
- **[Image Generation Setup](AionUi-Image-Generation-Tool-Model-Configuration-Guide)**: Image generation configuration

---

*Still have questions? [Open an issue](https://github.com/iOfficeAI/AionUi/issues) or [start a discussion](https://github.com/iOfficeAI/AionUi/discussions) on GitHub!*

