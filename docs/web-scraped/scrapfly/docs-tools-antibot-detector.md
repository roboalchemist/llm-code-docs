# Source: https://scrapfly.io/docs/tools/antibot-detector

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/tools/antibot-detector

Markdown Content:
Antibot Detector
----------------

Antibot Detector is a **free Chrome extension** that automatically identifies **26+ security technologies** including CAPTCHAs, anti-bot protection systems, and fingerprinting techniques with confidence scoring.

> **Quick Start:**[Install from Chrome Web Store](https://chromewebstore.google.com/detail/scrapfly/pdpakdgmjhkfimgaihlgaaiijlbilkca)| [View Source Code](https://github.com/scrapfly/Antibot-Detector)

[Detection Capabilities](https://scrapfly.io/docs/tools/antibot-detector#detection-capabilities)
------------------------------------------------------------------------------------------------

Antibot Detector identifies three main categories of security technologies using multi-layered detection:

#### CAPTCHA Systems

*   reCAPTCHA (v2/v3)
*   hCaptcha
*   FunCaptcha (Arkose Labs)
*   GeeTest
*   Cloudflare Turnstile

> **Pro Tip:**Use Antibot Detector to understand what security challenges you'll face when scraping a website, then use [Scrapfly's Anti-Scraping Protection](https://scrapfly.io/docs/scrape-api/anti-scraping-protection)to bypass them automatically.

[How It Works](https://scrapfly.io/docs/tools/antibot-detector#how-it-works)
----------------------------------------------------------------------------

Antibot Detector uses a sophisticated multi-layer detection approach that combines four complementary methods:

##### DOM Inspection

Scans HTML elements and attributes for telltale signs of CAPTCHA widgets and security scripts embedded in the page structure.

##### Network Monitoring

Analyzes HTTP headers, cookies, and network requests for security service signatures like challenge tokens and protection markers.

##### Window Properties

Checks for injected JavaScript objects that anti-bot services add to the browser's global scope for client-side validation.

##### API Interception

Hooks into browser APIs (Canvas, WebGL, Audio) to detect when fingerprinting techniques are actively collecting device information.

> **Performance:**Detection is optimized with LRU caching and early-exit patterns, achieving **60-80% faster**detection speeds with minimal browser overhead.

[Installation](https://scrapfly.io/docs/tools/antibot-detector#installation)
----------------------------------------------------------------------------

Choose your preferred installation method below. We recommend installing from the Chrome Web Store for automatic updates and the easiest setup.

#### Install from Chrome Web Store

The easiest way to install Antibot Detector is directly from the Chrome Web Store:

1.   **Visit the Chrome Web Store**
Go to the [Antibot Detector page on the Chrome Web Store](https://chromewebstore.google.com/detail/scrapfly/pdpakdgmjhkfimgaihlgaaiijlbilkca).

2.   **Click "Add to Chrome"**
Click the blue "Add to Chrome" button on the extension page.

3.   **Confirm Permissions**
A popup will appear asking you to confirm the extension's required permissions. Click "Add extension" to proceed.

4.   **Start Using Immediately**
The extension is now installed! Look for the Scrapfly icon in your browser toolbar. Visit any website to start detecting anti-bot technologies.

> **Benefits of Chrome Store Installation:**
> *   **Automatic updates:** Get new features and bug fixes without manual downloads
> *   **One-click installation:** No need to enable Developer Mode or load unpacked extensions
> *   **Verified by Google:** Additional security review by the Chrome Web Store team
> *   **Easy management:** Update and uninstall directly from Chrome's extension manager

> **That's it!**The extension is now ready to use. Visit any website and click the extension icon to see detected security technologies.

#### Step-by-Step Instructions

1.   **Download the Extension**
Visit the [GitHub Releases page](https://github.com/scrapfly/Antibot-Detector/releases) and download the latest `antibot-detector-vX.X.X.zip` file.

2.   **Extract the ZIP File**
Unzip the downloaded file to a permanent location on your computer (e.g., `~/antibot-detector`). **Important:** Don't delete this folder after installation, as Chrome loads extensions from this location.

3.   **Open Chrome Extensions Page**
In Google Chrome, navigate to `chrome://extensions/` or click the menu (⋮) → **Extensions** → **Manage Extensions**.

4.   **Enable Developer Mode**
Toggle the **Developer mode** switch in the top-right corner of the extensions page.

5.   **Load the Extension**
Click the **Load unpacked** button and select the extracted folder from step 2.

6.   **Pin the Extension (Optional)**
Click the puzzle piece icon (🧩) in Chrome's toolbar, find "Antibot Detector", and click the pin icon to keep it visible.

> **Success!**The extension is now installed and ready to use. Visit any website to start detecting security technologies.

#### Build from Source

> **Prerequisites:**Requires Node.js 18+ and npm installed on your system.

1.   **Clone the Repository**```
git clone https://github.com/scrapfly/Antibot-Detector.git
cd Antibot-Detector
``` 
2.   **Install Dependencies**`npm install` 
3.   **Build the Extension**`npm run build` 
This creates a production-ready build in the `dist/` directory.

4.   **Load in Chrome**
Open Chrome, navigate to `chrome://extensions/`, enable **Developer Mode**, click **Load unpacked**, and select the `dist/` folder.

 Development Mode

For active development with file watching and automatic reloading:

`npm run dev`

This watches for file changes and rebuilds automatically. Load the extension from `dist/` in Chrome, then reload the extension after each rebuild.

[How to Use](https://scrapfly.io/docs/tools/antibot-detector#usage)
-------------------------------------------------------------------

Once installed, Antibot Detector works automatically in the background. Here's how to use it effectively:

1

##### Install

Follow the [installation guide](https://scrapfly.io/docs/tools/antibot-detector#installation) above.

2

##### Browse

Visit any website. Detection runs automatically on page load.

3

##### View Results

Click the extension icon to see detected technologies with confidence scores.

4

##### Analyze

View history, export data, or use advanced capture tools for specific services.

### [Reading Detection Results](https://scrapfly.io/docs/tools/antibot-detector#reading-results)

The extension popup displays detected technologies with the following information:

| Element | Description |
| --- | --- |
| **Service Name** | The detected security technology (e.g., "Cloudflare", "reCAPTCHA v3") |
| **Confidence Score** | Percentage indicating detection certainty (higher = more confident). Scores combine evidence from multiple detection methods. |
| **Category Badge** | Color-coded badge: CAPTCHA, Anti-Bot, or Fingerprinting |
| **Detection Methods** | Expandable details showing which methods triggered (DOM, cookies, headers, etc.) |

[Key Features](https://scrapfly.io/docs/tools/antibot-detector#features)
------------------------------------------------------------------------

##### Multi-Layer Detection

Four detection methods working together for maximum accuracy:

*   **DOM Inspection:** Scans HTML elements for CAPTCHA widgets
*   **Network Monitoring:** Analyzes HTTP headers and cookies
*   **JavaScript API Hooks:** Intercepts fingerprinting attempts
*   **Window Properties:** Detects injected security objects

##### Optimized Performance

Built for speed with minimal browser overhead:

*   **12-hour caching:** Results cached per domain
*   **LRU pattern cache:** 60-80% faster pattern matching
*   **Early-exit detection:** Stops once match found
*   **~80% cache hit rate:** Typical performance metric

##### Detection History

Track detections across all your browsing sessions:

*   **Session tracking:** View all past detections by website
*   **Filtering:** Search by domain or technology type
*   **Export:** Save results as JSON for analysis
*   **Configurable retention:** Set history limit in settings

##### Advanced Capture Tools

Specialized tools for deep analysis of specific services:

*   **reCAPTCHA:** Extract sitekey and selectors
*   **Akamai:** Capture sensor data for analysis
*   **Imperva:** Extract challenge parameters
*   **Shape Security:** Analyze protection layers

##### Customizable Rules

Tailor detection to your specific needs:

*   **Rules Editor:** Create custom detection patterns
*   **Import/Export:** Share rules with your team
*   **URL Blacklist:** Exclude specific domains from detection
*   **JSON-based:** Easy to modify and extend

##### Privacy-First Design

Your data stays private:

*   **No data collection:** Zero telemetry or analytics
*   **100% local processing:** Everything runs in your browser
*   **No external requests:** No data sent to external servers
*   **Open source:** Fully auditable code on GitHub

[Common Use Cases](https://scrapfly.io/docs/tools/antibot-detector#use-cases)
-----------------------------------------------------------------------------

**Scenario:** You're planning to scrape a website and need to know what security challenges to expect.

**How Antibot Detector Helps:**

*   Quickly identify which anti-bot systems are protecting the site
*   Determine if CAPTCHAs are present (and which type)
*   Detect fingerprinting techniques that may block automated browsers
*   Plan your scraping strategy based on detected technologies

> **Pro Workflow:**Use Antibot Detector to identify challenges, then use [Scrapfly's ASP feature](https://scrapfly.io/docs/scrape-api/anti-scraping-protection)to bypass them automatically without writing custom code.

**Scenario:** You're auditing a website's security posture as part of a penetration test.

**How Antibot Detector Helps:**

*   Catalog all security layers protecting the application
*   Identify potential gaps in bot protection coverage
*   Document security technologies for reports
*   Compare security implementations across different pages

**Scenario:** You want to understand what security technologies competitors are using.

**How Antibot Detector Helps:**

*   Quickly survey security stacks across multiple competitor sites
*   Identify industry trends in anti-bot adoption
*   Export historical data for trend analysis
*   Benchmark your own security against competitors

**Scenario:** You're learning about web security and want to understand how anti-bot systems work in practice.

**How Antibot Detector Helps:**

*   See real-world examples of security technologies in action
*   Understand which detection methods reveal each technology
*   Compare different implementations across websites
*   Learn by examining the open-source detection logic

[Troubleshooting](https://scrapfly.io/docs/tools/antibot-detector#troubleshooting)
----------------------------------------------------------------------------------

**Possible Causes:**

*   The website genuinely has no detectable anti-bot technologies
*   Detection hasn't completed yet (wait a few seconds after page load)
*   Extension is disabled or not properly loaded

**Solutions:**

1.   Refresh the page and wait 3-5 seconds for detection to complete
2.   Verify the extension is enabled at `chrome://extensions`
3.   Check the browser console for errors (F12 → Console tab)
4.   Try a known-protected site like [nike.com](https://www.nike.com/) (has Akamai) or [ticketmaster.com](https://www.ticketmaster.com/) (has Cloudflare + Queue-it)

**Explanation:** First-time detection on a domain takes longer because the cache is empty. Subsequent visits to the same domain will be much faster (typically <1 second) due to 12-hour caching.

**Expected Performance:**

*   **First visit:** 2-4 seconds (building cache)
*   **Cached visits:**<1 second (instant results)
*   **Cache hit rate:** ~80% for typical browsing patterns

**Note:** Complex pages with many scripts may take slightly longer on first detection.

**Common Issues:**

*   **Chrome Version:** Ensure you're using Chrome 88+ (Manifest V3 requirement)
*   **Folder Deleted:** The extension folder must remain in its original location
*   **Permissions:** Check file permissions allow Chrome to read the extension files
*   **Conflicting Extensions:** Other extensions may interfere (try disabling temporarily)

**Reset Steps:**

1.   Remove the extension from `chrome://extensions`
2.   Delete and re-download/re-extract the extension files
3.   Follow the [installation steps](https://scrapfly.io/docs/tools/antibot-detector#installation) again carefully
4.   Check Chrome console for specific error messages

**Why This Happens:**

*   Anti-bot services constantly evolve their implementations
*   Some services use conditional loading (only appear for suspicious traffic)
*   Detection rules may need updates for new service versions

**How to Help:**

1.   **Report false positives:**[Open a GitHub issue](https://github.com/scrapfly/Antibot-Detector/issues) with the URL and detected technology
2.   **Report missing detections:** Include the URL and which technology you know is present
3.   **Contribute rules:** Submit a pull request with updated detection JSON files

_Detection accuracy improves with community contributions!_

[Frequently Asked Questions](https://scrapfly.io/docs/tools/antibot-detector#faq)
---------------------------------------------------------------------------------

Yes! Antibot Detector is **100% free** for personal and non-profit use under the [NPOSL-3.0 License](https://opensource.org/licenses/NPOSL-3.0).

**Commercial use** (e.g., using it as part of paid services or within a company) requires a separate commercial license. Contact [legal@scrapfly.io](mailto:legal@scrapfly.io) for commercial licensing inquiries.

**Absolutely not.** Antibot Detector is designed with privacy as a core principle:

*   ✅ **100% local processing** - all detection happens in your browser
*   ✅ **No telemetry** - zero analytics, tracking, or data collection
*   ✅ **No external requests** - doesn't communicate with any external servers
*   ✅ **Open source** - you can audit the entire codebase on [GitHub](https://github.com/scrapfly/Antibot-Detector)

Your browsing data and detection results never leave your computer.

Currently, Antibot Detector is **Chrome-only** (and Chromium-based browsers like Edge, Brave, Vivaldi).

**Why Chrome-only?** The extension uses Chrome's Manifest V3 API, which provides the best security and performance. While technically possible to port to Firefox, it would require significant adaptation due to Firefox's different extension architecture.

**Community contributions welcome:** If you're interested in porting to Firefox, feel free to fork the repo and submit a pull request!

**License Requirement:** Commercial use requires a separate license. However, **Antibot Detector is best used as a reconnaissance tool**, not for production scraping.

**Better Solution for Commercial Scraping:**

*   Use Antibot Detector to **identify** what protection a site uses
*   Use [Scrapfly's API](https://scrapfly.io/) to **bypass** those protections automatically
*   Scrapfly handles Cloudflare, DataDome, PerimeterX, Akamai, and more out-of-the-box

This workflow (detect → bypass with Scrapfly) is much more reliable than trying to build custom bypass logic for each anti-bot system.

Detection accuracy varies by technology type:

| Category | Typical Accuracy | Notes |
| --- | --- | --- |
| CAPTCHA | **95%+** | Very high accuracy due to distinctive DOM elements and scripts |
| Anti-Bot | **85-90%** | Good accuracy, but some services use obfuscation |
| Fingerprinting | **80-85%** | Harder to detect passive fingerprinting; works best for active techniques |

**Confidence scores** help you gauge reliability - higher scores (80%+) indicate very reliable detection.

Yes! Antibot Detector supports custom detection rules through the built-in **Rules Editor**:

1.   Click the extension icon → **Settings**
2.   Navigate to **Rules Editor**
3.   Create a new JSON rule file or edit existing ones
4.   Use the **Import/Export** feature to share rules with your team

**Rule Structure:** Detection rules are JSON-based and specify patterns for cookies, DOM elements, URLs, headers, and more.

**Contribute:** If you create rules for a new anti-bot service, please consider [submitting them as a PR](https://github.com/scrapfly/Antibot-Detector/pulls) to help the community!

Antibot Detector is actively maintained with updates based on:

*   **New anti-bot services:** Rules added as new technologies emerge
*   **Service updates:** Existing rules updated when services change their implementations
*   **Bug fixes:** Issues reported by the community are addressed promptly
*   **Performance improvements:** Ongoing optimizations to detection speed

**Stay updated:** Watch the [GitHub repository](https://github.com/scrapfly/Antibot-Detector) for release notifications, or check the [Releases page](https://github.com/scrapfly/Antibot-Detector/releases) for changelog details.

**Auto-updates:** If you installed from the [Chrome Web Store](https://chromewebstore.google.com/detail/scrapfly/pdpakdgmjhkfimgaihlgaaiijlbilkca), updates are automatic. For manual installations, re-download the latest release and reload the extension.

[Contributing](https://scrapfly.io/docs/tools/antibot-detector#contributing)
----------------------------------------------------------------------------

Antibot Detector is **open source** and welcomes community contributions! Here's how you can help:

##### Add New Detectors

Found an anti-bot service we don't detect yet?

1.   Create a JSON detector file in `detectors/`
2.   Specify detection patterns (cookies, DOM, headers, etc.)
3.   Include confidence scores per method
4.   Add test cases and documentation
5.   Submit a pull request!

[See contribution guide →](https://github.com/scrapfly/Antibot-Detector/blob/main/CONTRIBUTING.md)

##### Report Issues

Found a bug or false detection?

1.   Check [existing issues](https://github.com/scrapfly/Antibot-Detector/issues) first
2.   Include the URL where the issue occurs
3.   Describe expected vs. actual behavior
4.   Attach screenshots if relevant
5.   Include Chrome version and extension version

[Report an issue →](https://github.com/scrapfly/Antibot-Detector/issues/new)

> **Join the Community:**Star the [GitHub repository](https://github.com/scrapfly/Antibot-Detector), share with others, and help us build the most comprehensive anti-bot detection tool!

### Blog Posts

### Testing Tools

### Scrapfly Products

### Install & Download

### Source Code & Development
