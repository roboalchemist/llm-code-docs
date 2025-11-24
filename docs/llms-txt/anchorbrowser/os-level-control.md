# Source: https://docs.anchorbrowser.io/advanced/os-level-control.md

# OS-Level Control

> Direct operating system control for precise browser automation and AI agent interactions

# OS-Level Control

OS-level control provides direct access to operating system primitives like mouse movements, keyboard input, and screen interactions within your browser sessions. This approach offers more precise control than traditional web automation methods and is particularly powerful when combined with AI agents and vision-based models.

## Why OS-Level Control?

### Superior AI Agent Performance

**Vision-based AI models perform significantly better** when they can interact with the browser using the same primitives humans use:

* **OS-level UI elements**: Dropdowns, context menus, and system dialogs that aren't part of the webpage DOM.
* **Visual coordinate targeting**: AI agents can directly click on elements they see in screenshots
* **Keyboard shortcuts work naturally**: `Ctrl+F` for searching, `Ctrl+L` for browser navbar interaction, `Ctrl+T` for new tabs

<Expandable title="Key List for Keyboard Shortcuts">
  ## Supported Keys For Keyboard Shortcuts

  |         |            |      |       |            |             |           |   |
  | ------- | ---------- | ---- | ----- | ---------- | ----------- | --------- | - |
  | `A`-`Z` | `Up`       | `F1` | `F7`  | `Control`  | `Enter`     | `Command` |   |
  | `0`-`9` | `Down`     | `F2` | `F8`  | `Ctrl`     | `Return`    | `Cmd`     |   |
  | `Space` | `Left`     | `F3` | `F9`  | `Alt`      | `Backspace` | `Windows` |   |
  | `Home`  | `Right`    | `F4` | `F10` | `Shift`    | `Delete`    | `Win`     |   |
  | `End`   | `PageUp`   | `F5` | `F11` | `CapsLock` | `Escape`    | `Insert`  |   |
  | `Tab`   | `PageDown` | `F6` | `F12` | `NumLock`  | `Esc`       | `Ins`     |   |
</Expandable>

## Core Capabilities - Beyond Traditional Web Automation

Control mouse interactions with pixel-level precision:

### Basic Click

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';
  const anchor_client = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});

  const response = await anchor_client.sessions.mouse.click("Your Session ID", {
  // Single click at coordinates
      x: 100,
      y: 700,
  });
    console.log(response.data.status)
  ```

  ```python python theme={null}
    from anchorbrowser import Anchorbrowser
    import os

    client = Anchorbrowser(
        api_key = os.getenv("ANCHOR_API_KEY")
    )
    response = client.sessions.mouse.click(
        session_id = "Your Session ID",
      # Single click at coordinates
        x = 100,
        y = 700,
    )
    print(response.data['status'])
  ```
</CodeGroup>

### Advanced Mouse Control

<CodeGroup>
  ```javascript node.js theme={null}
    import AnchorBrowser from 'anchorbrowser';
    const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
    const sessionId = "Your Session ID";

    // Double-click for text selection
    await anchorClient.sessions.mouse.doubleClick(sessionId, {
      x: 500, 
      y: 200
    });

    // Mouse down and up for custom gestures
    await anchorClient.sessions.mouse.down(sessionId, {
      x: 100, 
      y: 100, 
    });

    // Move while holding down (drag)
    await anchorClient.sessions.mouse.move(sessionId, {
      x: 300, 
      y: 300
    });

    // Release
    await anchorClient.sessions.mouse.up(sessionId, {
      x: 300, 
      y: 300
    });
  ```

  ```python python theme={null}
    from anchorbrowser import Anchorbrowser
    import os
    anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
    session_id = "Your Session ID"

    # Double-click for text selection
    anchor_client.sessions.mouse.double_click(session_id, x = 500, y = 200)

    # Mouse down and up for custom gestures
    anchor_client.sessions.mouse.down(session_id, x = 100, y = 100)

    # Move while holding down (drag)
    anchor_client.sessions.mouse.move(session_id, x = 300, y = 300)

    # Release
    anchor_client.sessions.mouse.up(session_id, x = 300, y = 300)
  ```
</CodeGroup>

### Drag and Drop

Perform complex drag and drop operations in a single command:

<CodeGroup>
  ```javascript node.js theme={null}
    import AnchorBrowser from 'anchorbrowser';
    const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
    const sessionId = "Your Session ID";

    // Drag and Drop
    await anchorClient.sessions.dragAndDrop(sessionId, {
      startX: 200,
      startY: 150,
      endX: 600,
      endY: 400,
    });
  ```

  ```python python theme={null}
    from anchorbrowser import Anchorbrowser
    import os
    anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
    session_id = "Your Session ID"

    # Drag and Drop
    anchor_client.sessions.drag_and_drop(session_id,
      start_x = 200,
      start_y = 150,
      end_x = 600,
      end_y = 400
      )
  ```
</CodeGroup>

### Keyboard Input

Send text and keyboard shortcuts with human-like timing:

#### Text Input

<CodeGroup>
  ```javascript node.js theme={null}
    import AnchorBrowser from 'anchorbrowser';
    const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
    const sessionId = "Your Session ID";

    // Type text with optional delay between keystrokes
    await anchorClient.sessions.keyboard.type(sessionId, {
      text: "Hello, world!",
      delay: 50 // milliseconds between keystrokes
    });
  ```

  ```python python theme={null}
    from anchorbrowser import Anchorbrowser
    import os
    anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
    session_id = "Your Session ID"

    # Type text with optional delay between keystrokes
    anchor_client.sessions.keyboard.type(session_id,
      text = "Hello, world!",
      delay = 50 # milliseconds between keystrokes
      )
  ```
</CodeGroup>

#### Keyboard Shortcuts

<CodeGroup>
  ```javascript node.js theme={null}
    import AnchorBrowser from 'anchorbrowser';
    const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
    const sessionId = "Your Session ID";

    // Execute keyboard shortcuts
    anchorClient.sessions.keyboard.shortcut(sessionId, {
      keys: ['Ctrl', 'a'], // Select all
      holdTime: 100 // Hold keys for 100ms
    });

  // Common shortcuts
  const shortcuts = {
    selectAll: ['Ctrl', 'a'],
    copy: ['Ctrl', 'c'],
    paste: ['Ctrl', 'v'],
    undo: ['Ctrl', 'z'],
    newTab: ['Ctrl', 't'],
    closeTab: ['Ctrl', 'w'],
    focusAddressBar: ['Ctrl', 'l']
  };
  ```

  ```python python theme={null}
    from anchorbrowser import Anchorbrowser
    import os
    anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
    session_id = "Your Session ID"

    # Execute keyboard shortcuts
    anchor_client.sessions.keyboard.shortcut(session_id,
      keys = ['Ctrl', 'a'],
      hold_time = 100 # Hold keys for 100ms
      )

    # Common shortcuts
    shortcuts = {
      'select_all': ['Ctrl', 'a'],
      'copy': ['Ctrl', 'c'],
      'paste': ['Ctrl', 'v'],
      'undo': ['Ctrl', 'z'],
      'new_tab': ['Ctrl', 't'],
      'close_tab': ['Ctrl', 'w'],
      'focus_address_bar': ['Ctrl', 'l']
    }
  ```
</CodeGroup>

### Scrolling

Control page scrolling with precision:

```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';
  const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
  const sessionId = "Your Session ID";

  // Scroll at specific coordinates
  anchorClient.sessions.scroll(sessionId, {
    x: 400,           // Where to perform scroll (cursor position)
    y: 300,           // Where to perform scroll (cursor position)
    deltaX: 0,        // Horizontal scroll amount (does not correlate with pixels)
    deltaY: 200,      // Vertical scroll amount (does not correlate with pixels, positive = down)
    steps: 5          // Number of steps for smooth scrolling
  });
```

```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os
  anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
  session_id = "Your Session ID"

  # Scroll at specific coordinates
  anchor_client.sessions.scroll(session_id,
    x = 400,           # Where to perform scroll (cursor position)
    y = 300,           # Where to perform scroll (cursor position)
    delta_x = 0,        # Horizontal scroll amount (does not correlate with pixels)
    delta_y = 200,      # Vertical scroll amount (does not correlate with pixels, positive = down)
    steps = 5          # Number of steps for smooth scrolling
    )
```

### Screenshots

Capture visual state for AI analysis:

<CodeGroup>
  ```javascript node.js theme={null}
    import AnchorBrowser from 'anchorbrowser';
    import { writeFile } from 'node:fs/promises';
    const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
    const sessionId = "Your Session ID";

    // Take screenshot of current browser state
    const response = await anchorClient.sessions.retrieveScreenshot(sessionId);
    console.log(response);
    const imageBuffer = response.body;

    // Process screenshot with vision AI model (add code below)
    console.log(imageBuffer);

    // Or save screenshot to file
    const ab = await response.arrayBuffer();   // rs is a web ReadableStream
    await writeFile('image.png', Buffer.from(ab));
  ```

  ```python python theme={null}
    from anchorbrowser import Anchorbrowser
    import os
    anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
    session_id = "Your Session ID"

    # Take screenshot of current browser state
    response = anchor_client.sessions.retrieve_screenshot(session_id)
    print(response)

    # Save screenshot to file
    with open("image.png", "wb") as f:
        for chunk in response.iter_bytes(chunk_size=8192):
            f.write(chunk)

    # Process screenshot with vision AI model (add code below)
    print(f"Received {response}")
  ```
</CodeGroup>

### Clipboard Operations

Manage clipboard content programmatically:

#### Reading Clipboard

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';
  const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
  const sessionId = "Your Session ID";

  // Get current clipboard content
  const response = await anchorClient.sessions.clipboard.get(sessionId);
  console.log('Clipboard content:', response.data.text);
  ```

  ```python python theme={null}
    from anchorbrowser import Anchorbrowser
    import os
    anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
    session_id = "Your Session ID"

    # Get current clipboard content
    response = anchor_client.sessions.clipboard.get(session_id)
    print(response)
  ```
</CodeGroup>

#### Setting Clipboard

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';
  const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
  const sessionId = "Your Session ID";

  // Set clipboard content
  await anchorClient.sessions.clipboard.set(sessionId, {
    text: "Content to copy"
  });

  // Trigger copy operation (copies selected text)
  const copyResponse = await anchorClient.sessions.copy(sessionId);

  // Trigger paste operation
  await anchorClient.sessions.paste(sessionId, {
    text: "Text to paste"
  });
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os
  anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
  session_id = "Your Session ID"

  # Set clipboard content
  anchor_client.sessions.clipboard.set(session_id, text="Content to copy")

  # Trigger copy operation (copies selected text)
  copy_response = anchor_client.sessions.copy(session_id)

  # Trigger paste operation
  anchor_client.sessions.paste(session_id, text="Text to paste")
  ```
</CodeGroup>

### Navigation

Direct URL navigation at the OS level on the currently selected tab:

<CodeGroup>
  ```javascript node.js theme={null}
  import AnchorBrowser from 'anchorbrowser';
  const anchorClient = new AnchorBrowser({apiKey: process.env.ANCHOR_API_KEY});
  const sessionId = "Your Session ID";

  // Navigate to a specific URL (completely OS-level, operates on selected tab)
  const response = await anchorClient.sessions.goto(sessionId, {
    url: "https://example.com"
  });
  console.log("Navigation response:", response);
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os
  anchor_client = Anchorbrowser(api_key=os.getenv("ANCHOR_API_KEY"))
  session_id = "Your Session ID"

  # Navigate to a specific URL (completely OS-level, operates on selected tab)
  response = anchor_client.sessions.goto(session_id, url="https://example.com")
  print("Navigation response:", response)
  ```
</CodeGroup>

## AI Agent Integration Patterns

### OpenAI Computer Use Integration

Anchor includes an integrated **OpenAI Computer Use agent** that leverages OS-level control for enhanced AI interactions. This agent can perform complex tasks by combining vision models with precise OS-level operations.

```python python theme={null}
class AnchorBrowser(BasePlaywrightComputer):
    """
    Computer implementation for Anchor browser (https://anchorbrowser.io)
    Uses OS-level control endpoints for browser automation within the container.

    IMPORTANT: The `goto` and navigation tools are already implemented and recommended
    when using the Anchor computer to help the agent navigate more effectively.
    """

    def __init__(self, width: int = 1024, height: int = 900, session_id: str = None):
        """Initialize the Anchor browser session"""
        super().__init__()
        self.dimensions = (width, height)
        self.session_id = session_id
        self.base_url = "http://localhost:8484/api/os-control"

    def screenshot(self) -> str:
        """
        Capture a screenshot using OS-level control API.
        
        Returns:
            str: A base64 encoded string of the screenshot for AI model consumption.
        """
        try:
            response = requests.get(f"{self.base_url}/screenshot")
            
            if not response.ok:
                print(f"OS-level screenshot failed, falling back to standard screenshot")
                return super().screenshot()
                
            # OS-level API returns binary PNG data, encoded for AI models
            return base64.b64encode(response.content).decode('utf-8')
            
        except Exception as error:
            print(f"OS-level screenshot failed, falling back: {error}")
            return super().screenshot()

    def click(self, x: int, y: int, button: str = "left") -> None:
        """
        Click at the specified coordinates using OS-level control.
        
        Args:
            x: The x-coordinate to click.
            y: The y-coordinate to click.
            button: The mouse button to use ('left', 'right').
        """
        try:
            response = requests.post(
                f"{self.base_url}/mouse/click",
                json={"x": x, "y": y, "button": button}
            )
            
            if not response.ok:
                print(f"OS-level click failed, falling back to standard click")
                super().click(x, y, button)
                
        except Exception as error:
            print(f"OS-level click failed, falling back: {error}")
            super().click(x, y, button)

    def type(self, text: str) -> None:
        """
        Type text using OS-level control with realistic delays.
        """
        try:
            response = requests.post(
                f"{self.base_url}/keyboard/type",
                json={"text": text, "delay": 30}
            )
            
            if not response.ok:
                print(f"OS-level type failed, falling back to standard type")
                super().type(text)
                
        except Exception as error:
            print(f"OS-level type failed, falling back: {error}")
            super().type(text)

    def keypress(self, keys: List[str]) -> None:
        """
        Press keyboard shortcut using OS-level control.
        
        Args:
            keys: List of keys to press simultaneously (e.g., ['Ctrl', 'c']).
        """
        try:
            response = requests.post(
                f"{self.base_url}/keyboard/shortcut",
                json={"keys": keys, "holdTime": 100}
            )
            
            if not response.ok:
                print(f"OS-level keyboard shortcut failed, falling back")
                # Fallback to standard implementation
                for key in keys:
                    self._page.keyboard.down(key)
                for key in reversed(keys):
                    self._page.keyboard.up(key)
                
        except Exception as error:
            print(f"OS-level keyboard shortcut failed: {error}")
```

### Usage with OpenAI Models

The integrated computer use agent works seamlessly with OpenAI's vision models:

```python  theme={null}
# Initialize the agent with your session
agent = AnchorBrowser(width=1440, height=900, session_id="your-session-id")

# The agent can now:
# 1. Take screenshots for AI analysis
screenshot = agent.screenshot()

# 2. Perform precise clicks based on AI vision
agent.click(x=400, y=300)

# 3. Type text naturally
agent.type("Hello from AI agent!")

# 4. Execute keyboard shortcuts
agent.keypress(['Ctrl', 'l'])  # Focus address bar
agent.keypress(['Ctrl', 'f'])  # Open search
```

The computer use integration provides **automatic fallbacks** to standard browser automation if OS-level operations aren't available, ensuring reliability across different environments.

## Limitations and Considerations

### Session Requirements

* **Headful Sessions Only**: OS-level control requires a visible desktop environment
* **Performance Impact**: Screenshots and precise positioning may be slower than DOM-based automation

***

OS-level control opens up powerful possibilities for AI-driven browser automation, enabling more natural and effective interactions that mirror human behavior while providing the precision needed for reliable automation workflows.
