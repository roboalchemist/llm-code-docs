# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/index.md

# Integrate Playwright with Anchor Browser

> Integrate Playwright and Anchor Browser

# What is Playwright?

[Playwright](https://playwright.dev/) is Microsoft's modern browser automation framework that enables reliable end-to-end testing and web scraping across all major browsers (Chromium, Firefox, and WebKit). It provides a unified API for controlling browsers programmatically, making it the industry standard for automated browser interactions.

## Why Playwright + Anchor Browser?

Anchor Browser leverages Playwright's robust browser automation capabilities to provide enterprise-grade reliability and cross-browser compatibility. While Playwright handles the low-level browser control, Anchor Browser adds:

* Cloud-hosted browser instances - No local browser management required
* AI-powered interactions - Natural language task execution beyond traditional scripting
* Enterprise security - Isolated environments with authentication and proxy support
* Self-healing automations - Built-in error recovery and adaptation to website changes

### Key Playwright Capabilities

* Multi-Browser Support - Test across Chrome, Firefox, and Safari with identical code
* Fast & Reliable - Auto-wait for elements, built-in retry logic, and parallel execution
* Powerful Debugging - Time-travel debugging, trace viewer, and UI mode for visual testing
* Visual Testing - Automated screenshot comparison and visual regression detection
* Precise Element Selection - Advanced locators for reliable element targeting

### How It Works with Anchor Browser

When you connect to Anchor Browser, you're using Playwright's familiar API but with cloud-hosted browsers:

```javascript node.js theme={null}
import { chromium } from 'playwright';
import AnchorClient from 'anchorbrowser';

const anchorClient = new AnchorClient({
  apiKey: process.env.ANCHOR_API_KEY,
});

// First create a session
const session = await anchorClient.sessions.create();
const cdp_url = session.data.cdp_url;

// Then connect using the session's CDP URL
const browser = await chromium.connectOverCDP(cdp_url);
console.log('Browser connected');

browser.close();
```

This gives you all of Playwright's power while eliminating infrastructure complexity and adding enterprise features.

### Use Cases

* Business Workflow Automation - Automate repetitive tasks in ERP, CRM, and financial systems
* End-to-End Testing - Automated testing of web applications across browsers
* Web Scraping - Reliable data extraction from dynamic websites
* UI Automation - Form filling, clicking, and complex user workflow automation
* Visual Monitoring - Automated screenshot comparison and regression testing
* Performance Testing - Page load timing and interaction performance measurement

## Next Steps

* [Quick Start with Playwright](/quickstart/use-via-code) - Get started in 5 minutes
* [Examples](/examples/form-filling) - Real-world Playwright automation scripts
* [Browser Configuration](/api-reference/browser-sessions/start-browser-session#body-browser) - Advanced browser settings and options
