# Browser Provider

The Browser Provider enables automated web browser interactions for testing complex web applications and JavaScript-heavy websites where simpler providers are not sufficient.

This provider uses [Playwright](https://playwright.dev/) to control headless browsers, allowing you to navigate pages, interact with elements, and extract data from dynamic websites. Playwright supports Chromium (Chrome, Edge), Firefox, and WebKit (Safari engine) browsers.

## When to Use the Browser Provider

The Browser Provider should only be used when simpler alternatives are not possible:

1. **Try these first:**
   - [HTTP Provider](/docs/providers/http/) - For API calls and simple HTML responses
   - [WebSocket Provider](/docs/providers/websocket/) - For real-time connections
   - [Custom Python Provider](/docs/providers/python/) - For custom logic with existing libraries
   - [Custom JavaScript Provider](/docs/providers/custom-api/) - For Node.js-based solutions

2. **Use Browser Provider only when:**
   - The application requires JavaScript execution to render content
   - You need to interact with complex UI elements (dropdowns, modals, etc.)
   - Authentication requires browser-based workflows (OAuth, SSO)
   - You need to test actual user interactions (clicks, typing, scrolling)

### Important Considerations

When using browser automation:

1. **Rate Limiting**: Always implement delays between requests to avoid overwhelming servers
2. **Anti-Bot Detection**: Many websites employ anti-bot measures that can detect and block automated browsers
3. **Resource Usage**: Browser automation is 10-100x slower than direct API calls and consumes significant CPU/memory
4. **Legal Compliance**: Always check the website's Terms of Service and robots.txt before automating

## Prerequisites

The browser provider requires Playwright and related packages. These are optional dependencies, so you'll need to install them:

```bash
npm install playwright @playwright/browser-chromium playwright-extra puppeteer-extra-plugin-stealth
```

Note: Currently, promptfoo's browser provider only supports Chromium-based browsers (Chrome, Edge). The provider uses `playwright-extra` with the Chromium engine for enhanced stealth capabilities.

## Configuration

To use the Browser Provider, set the provider `id` to `browser` and define a series of `steps` to execute:

```yaml
providers:
  - id: browser
    config:
      steps:
        - action: navigate
          args:
            url: https://example.com/search?q={{prompt}}
        - action: type
          args:
            selector: #search-input
            text: {{prompt}}
        - action: click
          args:
            selector: #search-button
        - action: extract
          args:
            selector: #results
          name: searchResults
      transformResponse: extracted.searchResults
```

### Connecting to Existing Browser Sessions

You can connect to an existing Chrome browser session (e.g., with OAuth authentication already completed):

```yaml
providers:
  - id: browser
    config:
      connectOptions:
        debuggingPort: 9222  # Chrome debugging port
      steps:
        - action: navigate
          runOnce: true
          args:
            url: https://example.com/search?q={{prompt}}
```

**Setup Instructions**:

1. Start Chrome with debugging: `chrome --remote-debugging-port=9222 --user-data-dir=/tmp/test`
2. Complete authentication manually
3. Run your tests

**Connection Options**:

- `debuggingPort`: Port number for Chrome DevTools Protocol (default: 9222)
- `mode`: Connection mode - `cdp` (default) or `websocket`
- `wsEndpoint`: Direct WebSocket endpoint (when using `mode: websocket`)

### Multi-Turn Session Persistence

For multi-turn strategies like Hydra, Crescendo, or GOAT, you can persist the browser session across turns. This keeps the same page open and maintains conversation state in chat-based applications.

```yaml
providers:
  - id: browser
    config:
      persistSession: true  # Keep page open across turns
      connectOptions:
        debuggingPort: 9222
      steps:
        - action: navigate
          runOnce: true
          args:
            url: https://example.com/chat
        - action: wait
          runOnce: true
          args:
            ms: 3000
        - action: type
          args:
            selector: #chat-input
            text: {{prompt}}
        - action: wait
          args:
            ms: 5000
        - action: extract
          args:
            script: |
              // Extract the latest AI response
              const messages = document.querySelectorAll('#chat-message');
              return messages[messages.length - 1]?.textContent || '';
          name: response
      transformResponse: extracted.response
```

**Key options:**

- `persistSession: true` - Keep the browser page open between `callApi()` invocations
- `runOnce: true` on steps - Execute only on the first turn (skip on subsequent turns)

This is essential for testing multi-turn jailbreak strategies against chat interfaces where you need to maintain conversation context.

## Supported Actions

The Browser Provider supports the following actions:

### Core Actions

#### Navigate to a specified URL

```yaml
- action: navigate
  args:
    url: https://example.com/search?q={{prompt}}
```

#### Click on an element

```yaml
- action: click
  args:
    selector: #button
    optional: true  # Won't fail if element doesn't exist
```

#### Enter text

```yaml
- action: type
  args:
    selector: #input[name="username"]
    text: {{username}}
```

#### Type text into an input field

```yaml
- action: type
  args:
    selector: #input[name="username"]
    text: {{username}}
    runOnce: true
```

#### Wait for a specified amount of time

```yaml
- action: wait
  args:
    ms: 3000
```

#### Wait for new child elements to appear under a parent

```yaml
- action: waitForNewChildren
  args:
    parentSelector: #results-container
    delay: 500
    timeout: 10000
```

#### Take a screenshot of the page

```yaml
- action: screenshot
  args:
    path: screenshot.png
    fullPage: true
```

### Action Parameters

| Action | Required Args | Optional Args | Description |
| --- | --- | --- | --- |
| navigate | `url`: string | - | URL to navigate to |
| click | `selector`: string | `optional`: boolean, `runOnce`: boolean | CSS selector of element to click |
| extract | (`selector` OR `script`): string, `name`: string | - | CSS selector or JS script, and variable name |
| screenshot | `path`: string | `fullPage`: boolean | File path to save screenshot |
| type | `selector`: string, `text`: string | `runOnce`: boolean | Type text into an input field |
| wait | `ms`: number | - | Wait for a specified amount of time |
| waitForNewChildren | `parentSelector`: string | `delay`: number, `timeout`: number | Parent element to watch |
| screenshot | `path`: string | `fullPage`: boolean | File path to save screenshot |

Each action in the `steps` array should be an object with the following structure:

```typescript
{
  action: string;
  args: { [key: string]: any; };
  name?: string;
  runOnce?: boolean;
}
```

Each step in the `steps` array should have the following structure:

- `action`: Specifies the type of action to perform (e.g., `navigate`, `click`, `type`).
- `args`: Contains the required and optional arguments for the action.
- `name` (optional): Used to name extracted content in the `extract` action.
- `runOnce` (optional): If `true`, the step only executes on the first turn. Used with `persistSession` for multi-turn strategies.

Steps are executed sequentially, enabling complex web interactions.

All string values in `args` support Nunjucks templating, allowing use of variables like `{{prompt}}`.

## Advanced Features

### Playwright Recorder Tools

The easiest way to create browser automation scripts is to record your interactions:

#### Chrome Extension (Recommended)

The [Playwright Recorder Chrome Extension](https://chrome.google.com/webstore/detail/playwright-recorder/pbbgjmghmjcpeelnheiphabndacpdfbc) is particularly helpful for quickly generating selectors:

1. Install the extension from the Chrome Web Store
2. Navigate to your target website
3. Click the extension icon and start recording
4. Perform your actions (click, type, etc.)
5. Stop recording and copy the generated selectors/code
6. Adapt the code for promptfoo's browser provider format

This extension is especially useful because it:

- Shows selectors in real-time as you hover over elements
- Generates multiple selector options (CSS, text, XPath)
- Allows you to copy individual selectors without recording full actions

#### Playwright Inspector (All Browsers)

For cross-browser recording, use Playwright's built-in recorder:

```bash
npx playwright codegen https://example.com
```

This opens an interactive browser window where you can perform actions and see generated code in real-time. You can choose between Chromium, Firefox, or WebKit.

### Selector Strategies

Playwright supports various selector strategies:

| Strategy | Example | Description |
| --- | --- | --- |
| CSS | `#submit-button` | Standard CSS selectors |
| Text | `text=Submit` | Find elements by text content |
| Role | `role=button[name="Submit"]` | ARIA role-based selectors |
| Test ID | `data-testid=submit` | Data attribute selectors |
| XPath | `xpath=//button[@type="submit"]` | XPath expressions |

For the most reliable selectors:

- Prefer stable attributes like IDs and data-testid
- Use role-based selectors for accessibility
- Avoid position-based selectors that can break with layout changes

### Debugging

#### 1. Disable Headless Mode

See exactly what's happening in the browser:

```yaml
providers:
  - id: browser
    config:
      headless: false  # Opens visible browser window
```

#### 2. Enable Debug Logging

Get detailed information about each action:

```bash
npx promptfoo@latest eval --verbose
```

#### 3. Take Screenshots

Capture the page state during execution:

```yaml
steps:
  - action: navigate
    args:
      url: https://example.com
  - action: screenshot
    args:
      path: debug-{{_attempt}}.png
```

### Performance Optimization

1. **Use headless mode in production**: It's faster and uses fewer resources
2. **Minimize wait times**: Only wait as long as necessary
3. **Batch operations**: Group related actions together
4. **Reuse browser contexts**: For multiple tests against the same site

### Best Practices for Rate Limiting

Implementing proper rate limiting is crucial to avoid detection and server overload:

```yaml
providers:
  - id: browser
    config:
      steps:
        - action: wait
          args:
            ms: 2000
        - action: navigate
          args:
            url: https://example.com
        - action: wait
          args:
            ms: 1000
        - action: click
          args:
            selector: #button
        - action: wait
          args:
            ms: 3000
```

**Tips for avoiding detection:**

- Randomize delays between actions (1-3 seconds)
- Use the stealth plugin (included with playwright-extra)
- Avoid patterns that look automated
- Consider using different user agents
- Respect robots.txt and rate limits

### Dealing with Anti-Bot Measures

Many websites implement anti-bot detection systems (like Cloudflare, reCAPTCHA, etc.). Here's how to handle common scenarios:

#### Common Anti-Bot Challenges

| Challenge | Detection Method | Mitigation Strategy |
| --- | --- | --- |
| Browser fingerprinting | JavaScript checks for automation | Stealth plugin helps mask automation |
| Behavior analysis | Mouse movements, typing patterns | Add realistic delays and interactions |
| IP rate limiting | Too many requests from one IP | Implement proper delays, use proxies cautiously |
| CAPTCHA challenges | Human verification tests | Consider if the site allows automation |
| User-Agent detection | Checking for headless browsers | Use realistic user agent strings |

#### Example with Anti-Bot Considerations

```yaml
providers:
  - id: browser
    config:
      headless: false  # Some sites detect headless mode
      steps:
        - action: wait
          args:
            ms: 3000
        - action: navigate
          args:
            url: {{url}}
        - action: wait
          args:
            ms: 5000
        - action: type
          args:
            selector: #search
            text: {{query}}
            delay: 100  # Delay between keystrokes
```

**Note**: If a website has strong anti-bot measures, it's often a sign that automation is not welcome. Always respect the website owner's wishes and consider reaching out for API access instead.

## Example: Testing a Login Flow

Here's a complete example testing a login workflow:

```yaml
# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json
description: Test login functionality
prompts:
  - 'Login with username {{username}} and password {{password}}'
providers:
  - id: browser
    config:
      headless: true
      steps:
        - action: navigate
          args:
            url: https://example.com/login
        - action: type
          args:
            selector: #username
            text: {{username}}
        - action: type
          args:
            selector: #password
            text: {{password}}
        - action: click
          args:
            selector: button[type="submit"]
        - action: wait
          args:
            ms: 2000
        - action: extract
          args:
            selector: .welcome-message
          name: welcomeText
      transformResponse: |
        return {
          output: extracted.welcomeText,
          success: extracted.welcomeText.includes("Welcome")
        };
tests:
  - vars:
      username: testuser
      password: testpass123
    assert:
      - type: javascript
        value: output.success === true
```

## Troubleshooting

### Common Issues and Solutions

| Issue | Cause | Solution |
| --- | --- | --- |
| "Element not found" | Selector incorrect or element not loaded | • Verify selector in DevTools<br>• Add wait before action<br>• Check if element is in iframe |
| "Timeout waiting for selector" | Page loads slowly or element never appears | • Increase timeout<br>• Add explicit wait actions<br>• Check for failed network requests |
| "Access denied" or 403 errors | Anti-bot detection triggered | • Use headless: false<br>• Add more delays<br>• Check if automation is allowed |
| "Click intercepted" | Element covered by overlay | • Wait for overlays to disappear<br>• Scroll element into view<br>• Use force click option |
| Inconsistent results | Timing or detection issues | • Add consistent delays<br>• Use stealth plugin<br>• Test during off-peak hours |

### Debugging Anti-Bot Detection

If you suspect anti-bot measures are blocking your automation:

```yaml
providers:
  - id: browser
    config:
      headless: false  # Always start with headed mode for debugging
      steps:
        - action: navigate
          args:
            url: {{url}}
        - action: screenshot
          args:
            path: debug-landing.png  # Check if you hit a challenge page
        - action: wait
          args:
            ms: 10000  # Longer wait to see what happens
        - action: screenshot
          args:
            path: debug-after-wait.png
```

## Useful Resources

- [Playwright Documentation](https://playwright.dev/docs/intro) - Official Playwright docs
- [Playwright Browsers Guide](https://playwright.dev/docs/browsers) - Detailed information about supported browsers
- [Playwright Selectors Guide](https://playwright.dev/docs/selectors) - Learn about CSS, text, and other selector strategies
- [Playwright Best Practices](https://playwright.dev/docs/best-practices) - Tips for reliable automation
- [Playwright Inspector](https://playwright.dev/docs/inspector) - Interactive tool for authoring and debugging tests
- [Chrome DevTools Guide](https://developer.chrome.com/docs/devtools/) - For inspecting elements and finding selectors

---

For more examples, check out the [headless-browser example](https://github.com/promptfoo/promptfoo/tree/main/examples/headless-browser) in our GitHub repository.