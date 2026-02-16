# Sonar Chromium Browser | Native Search Omnibox and Context Menu

Source: https://docs.perplexity.ai/docs/cookbook/showcase/sonar-chromium-browser

Chromium browser patch with native Perplexity Sonar API integration providing omnibox answers and context-menu summarization

**Sonar Chromium Browser** is a Chromium browser patch that natively integrates Perplexity's Sonar API to provide AI-powered functionality directly in the browser. Users can type `sonar <query>` in the omnibox for instant AI answers or select text and right-click "Summarize with Sonar" for quick summaries, streamlining research and browsing workflows.

## Features

* **Omnibox AI Answers** with `sonar <query>` syntax for instant responses
* **Context-menu Summarization** for selected text with one-click access
* **Native Browser Integration** using Chromium's omnibox and context-menu APIs
* **Dual Model Support** using Sonar Pro for omnibox and Sonar for summaries
* **Debounced Input Handling** for efficient API usage
* **Custom Browser Build** demonstrating AI integration patterns

## Prerequisites

* Ubuntu 22.04 (WSL2 recommended)
* Chromium source code checkout
* Perplexity API key
* 16GB+ RAM for Chromium build
* Git and standard build tools

## Installation

```bash theme={null}
