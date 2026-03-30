# Source: https://docs.bugbug.io/debugging-tests/error-codes.md

# Error codes

### Element & Selector Errors

#### ELEMENT\_DOES\_NOT\_EXIST

It was not possible to find the element using the selector

**When occurs?**:

* Element doesn't exist
* Element removed from DOM during execution
* Page is not ready yet, so element is not available

**What to do?**:

* Ensure selected selector is stable (e.g., it does not contain any dynamic content)
* Re-record this step
* Add waiting conditions

#### ELEMENT\_REMOVED

Element was found but unexpectedly removed during the step execution and BugBug was not able to find it again.

**When occurs?**:

* Parent element removed
* JavaScript removes element
* Dynamic reload
* SPA navigation
* Iframe removed

#### SELECTOR\_REQUIRED

Related step has an empty selector.

**What to do?**:

* Provide a valid custom selector
* Re-record this step again

#### INVALID\_ELEMENT\_SELECTOR

Provided element selector is invalid.

**When occurs?**:

* Malformed XPath eg. `//div[[@id`
* Invalid CSS eg. `invalid:selector`
* Unclosed brackets eg. `div[@id="test"`
* Invalid pseudo-selector eg. `div:fst-child`

**What to do?**:

* Re-record this step
* Fix selector manually (e.g., use selector editor)
  * Fix syntax errors
  * Validate in DevTools
* Use [XPath Selector Builder](https://bugbug.io/xpath-selector-builder/), if needed

#### INTERACTION\_POSITION\_OUT\_OF\_VIEWPORT

It was not possible to reach interaction coordinates in the current viewport size.

**When occurs?**:

* Click at (2000,1500) in 1920x1080 viewport
* Selector points to container
* Element off-screen

**What to do?**:

* Check the selector, perhaps it incorrectly points to a large container instead of its child element
* Check the scroll coordinates in previous steps and make sure that the element is fully scrolled to view
* Check the interaction position settings

### Frame & Context Errors

#### FRAME\_DOES\_NOT\_EXIST

Related step was supposed to be executed in an iframe but the iframe was not found.

**When occurs?**:

* Iframe removed during step execution
* Conditional iframe
* Wrong iframe selector

**What to do?**:

* Take a look at the previous steps and find a "Switch context" step
* Make sure it uses a correct selector to a correct iframe
* You can also re-record some steps again
  * remove the "switch context" step and the following iframe steps
  * use "record from here"

#### FRAME\_LOADS\_TOO\_LONG

BugBug waited for a requested frame until it is ready, but loading took too much time.

**When occurs?**:

* Iframe stuck loading
* Third-party issues
* 404/server error
* CORS/CSP blocking

**What to do?**:

* Take a look at the previous steps and find a "Switch context" step.
* Make sure it uses a correct selector to a correct iframe.
* Re-record some steps again
  * remove the "switch context" step and the following iframe steps
  * use "record from here"
* Increase timeout
* Check console for CORS/CSP errors
* Check console for network errors

#### WINDOW\_OR\_TAB\_DOES\_NOT\_EXIST

Window or tab with specified number does not exist

**When occurs?**:

* Switch to tab #3 with only 2 tabs
* Tab closed during execution
* Different tab count than while recording

**What to do?**:

* Take a look at the previous steps and find a "Switch context" step
* Record this step again by using "record from here" or manually update the tab number
* Verify tab number (default tab number is 0)
* Ensure tabs are opened
* Check for accidental tab closures

#### TAB\_CLOSED

User closed tab during running test

**When occurs?**:

* Manual tab closure
* Clicking X button
* Keyboard shortcut Cmd/Ctrl+W

**What to do?**:

* Don't interact with browser during test
* Rerun without interference

#### WINDOW\_CLOSED

Window closed while the test was running

**When occurs?**:

* Too many "Close tab" steps
* Manual window closure
* Closing last tab
* Unexpected window\.close() calls

**What to do?**:

* Make sure you don't have too many steps that close tabs
* Don't close window during test
* Ensure at least one tab remains open
* Check for unexpected window\.close() calls

#### WINDOW\_MINIMIZED

The window with the running test has been minimized

**When occurs?**:

* User minimizes window
* Keyboard shortcut
* Forced by another app

**What to do?**:

* Don't minimize the window when a test is running
* Browser cannot execute steps when window is minimized
* Keep window visible during test execution
* Rerun without minimizing

#### UNEXPECTED\_WINDOW\_STATE\_CHANGE

The window with the running test has been minimized or lost focus by other user actions

**When occurs?**:

* MacOS Space switching
* Clicking other app
* System dialog
* Screen saver activation

**What to do?**:

* Avoid minimizing the window while a test is running
* If you are using MacOS, avoid switching from space with pending test run to another
* Disable notifications/screen saver
* Don't interact with other apps during test

### Form & Input Errors

#### UNCHANGABLE\_ELEMENT

Wrong type of element - expected a form input, textarea, select, checkbox or radio.

**When occurs?**:

* "Change"/"Type" step on `div`, `span`, `p`, `button` or other non-input element
* "Select option" step on non-select element
* "Clear" step on non-input element or element which value cannot be cleared

**What to do?**:

* Check if selector points to correct element
* Update selector to form input (input/textarea/select/checkbox/radio)
* Re-record step
* Use different step type

#### TYPED\_TEXT\_DIFFERENT\_THAN\_EXPECTED

The typing step was completed, but the end result was not as expected

**When occurs?**:

* User interference
* JavaScript modifies value in background
* Auto-complete changes value

**What to do?**:

* Rerun the test and remember not to interact with the page during execution
* Check for JavaScript modifications in your code
* Switch "Type" step to "Change" step
* Contact support if problem persists

#### INVALID\_FIELD\_VALUE

Could not verify that the value in the form was changed properly

**When occurs?**:

* New field value doesn't match expected value due to invalid execution
* User interference
* JavaScript modifies value in background
* Auto-complete changes value

**What to do?**:

* Verify value is valid
* Check for validation/event handlers that might modify the value
* Switch "Type" step to "Change" step
* Add wait after change to allow value to settle

#### INVALID\_OPTION\_INDEX

Provided option index is not a number

**When occurs?**:

* Index "abc" instead of "2"
* Variable resolves to non-numeric

**What to do?**:

* Use numeric index (0,1,2)
* Check variable value, if variable is used
* Use "Select by text/value" instead

#### MISSING\_OPTION\_VALUE

Option with provided value does not exist on available options list

**When occurs?**:

* Value "premium" doesn't exist
* Options changed since recording
* Dynamic options differ
* Typo in value

**What to do?**:

* Verify option exists
* Re-record step
* Check for typos
* Use select by text/index instead
* Ensure dynamic options loaded

#### MISSING\_OPTION\_TEXT

Option with provided text does not exist on available options list

**When occurs?**:

* Text "Szczecin" doesn't exist
* Text changed
* Language/locale changed
* Whitespace mismatch

**What to do?**:

* Verify exact text match (including whitespace)
* Re-record step
* Use "Select by value/index" instead
* Check locale changes

#### MISSING\_OPTION\_INDEX

Option with provided index does not exist on available options list

**When occurs?**:

* Index 5 with only 3 options
* List shortened
* Conditional options missing
* Zero-based indexing confusion

**What to do?**:

* Verify index exists (first option always has index 0)
* Use "Select by text/value" instead
* Check if app uses dynamic options
* Re-record step

#### SELECT\_OPTION\_FAILED

BugBug was not able to select expected option

**When occurs?**:

* Selected value differs from expected
* Options changed since recording
* Browser bug
* Multi-select fails

**What to do?**:

* Verify if options are correct
* Check for event handlers that might revert the selection
* Re-record step
* Contact support if problem persists

#### MULTIPLE\_OPTIONS\_WITH\_VALUE

Could not verify which option should be selected - multiple select options reference the same value

**When occurs?**:

* Duplicated options
* Application bug

**What to do?**:

* Use "Select by text/index" instead
* Contact support if problem persists

### Navigation & Page Loading Errors

#### MISSING\_GOTO\_STEP

Test doesn't start with goto step

**When occurs?**:

* First step is Click
* Deleted goto step
* Manual test without goto
* Copied steps without goto

**What to do?**:

* Every test should begin with a navigation to a URL, so you need to add a "Go to URL" step at the very beginning of the test
* Re-record test from the beginning

#### INVALID\_URL

Provided URL is not valid

**When occurs?**:

* "htp\://example.com" (typo)
* Missing protocol "example.com"
* Spaces in URL
* Variable resolves to invalid URL

**What to do?**:

* Check if URL starts with: "http\://" or "https\://"
* Verify variable resolves correctly
* Fix other typos
* Test URL in browser

#### PAGE\_LOADING\_ERROR

BugBug handles browser's error pages. Full list of those errors can be found [here](https://support.google.com/chrome/answer/95669?hl=en#zippy=%2Cpage-loading-errors):

**When occurs?**:

* Connection timeout (e.g. "ERR\_CONNECTION\_TIMED\_OUT")
* Internet disconnected (e.g. "ERR\_INTERNET\_DISCONNECTED")
* Server down (e.g. "ERR\_CONNECTION\_REFUSED")
* DNS failure (e.g. "ERR\_NAME\_NOT\_RESOLVED")
* SSL protocol error (e.g. "ERR\_SSL\_PROTOCOL\_ERROR")
* Invalid certificate (e.g. "ERR\_CERT\_INVALID")

**What to do?**:

* Verify URL accessible
* Check internet connection
* Verify server running
* Check SSL certificate
* Try URL in browser
* Contact server admin

### JavaScript & Code Execution Errors

#### CODE\_EXECUTION\_ERROR

JavaScript code has runtime error

**When occurs?**:

* Typo "consle.log"
* Syntax error missing brace
* Runtime error element doesn't exist
* ReferenceError undefined variable

**What to do?**:

* Fix syntax errors
* Test in browser console
* Add error handling
* Verify elements/variables exist
* Check console for details

#### INVALID\_EXECUTION\_RESULT

Function didn't return boolean, which is required for assertion

**When occurs?**:

* Returns string "true" not boolean
* Returns undefined/null
* Returns number 1
* Async doesn't resolve to boolean

**What to do?**:

* Ensure returns boolean (true/false)
* Convert with !!value or Boolean(value)
* Test in console

### Variable Errors

#### VARIABLE\_DOES\_NOT\_EXIST

Variable used in step definition doesn't exist

**When occurs?**:

* Using {{userEmail}}, which was never created
* Typo {{userName}} vs {{username}}
* Variable in different test
* Case-sensitive mismatch

**What to do?**:

* Make sure that you use a proper variable name
* Create variable before using (Set variable step)
* Check spelling and case
* Verify in same test/suite
* Use correct syntax {{variableName}}

#### VARIABLE\_NESTING\_LIMIT\_EXCEEDED

Nesting variables is limited to 3 levels and the variable you used contains too many nesting levels.

**When occurs?**:

* {{var1}} contains {{var2}} contains {{var3}} contains {{var4}}
* Complex chains
* Circular references

**What to do?**:

* Simplify to max 3 levels
* Break into separate steps
* Avoid circular references
* Use Execute step for complex values

### Event & Interaction Errors

#### EVENT\_DISPATCHED\_ON\_INVALID\_ELEMENT

BugBug found the element, but could not click it - some other element interrupted the click

**When occurs?**:

* Modal overlay covers button
* Cookie banner covers element
* Loading spinner appears
* Fixed header covers element

**What to do?**:

* Check the screenshots and analyze where the cursor is located
* Investigate why the target element could not be clicked
* Close covering elements first
* Add wait for covering elements to disappear
* Add additional test steps using "record from here" to make sure the clickable element is accessible

#### EVENT\_DISPATCH\_FAILED

BugBug found the element, dispatched the requested event, but could not resolve the event correctly

**When occurs?**:

* Need double-click not click
* Event listener prevents default
* Element disabled or pointer-events:none
* Framework blocks event
* Incorrect event type used

**What to do?**:

* This usually occurs when an incorrect event type is used (e.g., using "click" instead of "double-click")
* Try different step type
* Check if element enabled/interactive
* Verify no CSS preventing interaction
* Re-record step

### Other Step-Specific Errors

#### FAILED\_WAITING\_CONDITIONS

Waiting conditions timeout

**When occurs?**:

* Element never visible
* Network never idle
* Element can't get focus
* Element stays covered

**What to do?**:

* Increase step timeout
* Review and adjust conditions
* Check if achievable
* Remove/modify problematic conditions
* Add explicit waits

#### PROMPT\_DOES\_NOT\_EXIST

Prompt not found

**When occurs?**:

* Answer prompt step with no dialog
* Previous step didn't trigger alert
* Dialog auto-closed
* Page uses custom modal not browser prompt

**What to do?**:

* Ensure the prompt has been opened in a previous step
* Don't close the prompt manually when a test is running
* Remove Answer prompt step if none appears
* Check for custom modals

#### UNHANDLED\_PROMPT

Execution of this step was blocked by unhandled prompt

**When occurs?**:

* Alert without Answer prompt step
* Unexpected window\.confirm()
* JavaScript prompt() without handler
* "Leave site?" dialog

**What to do?**:

* Ensure the prompt has been closed in a previous step
* Record or add manually "Answer prompt" step to close the prompt
* Identify triggering step and add handler
* Check for unexpected prompts
* Disable beforeunload events if possible

#### NEXT\_STEP\_ELEMENT\_REQUIRED

Element from the next step was not found

**When occurs?**:

* Scroll until next step visible but next step has wrong selector
* Next step element doesn't exist
* Selector empty/invalid
* Next step deleted

**What to do?**:

* Related step is set to "Scroll until element from next step is visible" so the next step needs to have a correct selector
* Verify next step selector correct
* Ensure next step element exists
* Fix/add selector to next step

#### NEXT\_ACTIVE\_STEP\_WITH\_ELEMENT\_REQUIRED

Related step is set to "Scroll until element from next step is visible" so the next step needs to have a related element

**When occurs?**:

* Scroll until next step visible but next step is Execute JavaScript (no element)
* Next step is Wait/Set variable
* Next step disabled
* Next step is Goto

**What to do?**:

* Check what is the type of the next step
* Make sure that it is set to a type that has an element
* Change next step to one with element (Click, Change, etc.)
* Remove scroll until next step condition
* Add intermediate step with element

#### ASSERT\_FAILED

Assertion condition not met

**When occurs?**:

* Text equals "Success" but shows "Error"
* Element visible but hidden
* URL contains "/dashboard" but is "/login"
* Variable value mismatch

**What to do?**:

* Verify expected value correct
* Check page state
* Add wait before assertion
* Review test flow
* Update assertion to match behavior

#### SCROLL\_FAILED

Scroll operation failed

**When occurs?**:

* Scroll position doesn't match expected
* Page prevents scrolling with overflow:hidden
* JavaScript interferes
* Scroll target beyond boundaries

**What to do?**:

* Check page allows scrolling
* Verify scroll target reachable
* Check for JavaScript interference
* Adjust scroll coordinates

### Timeout & Performance Errors

#### TIMEOUT

Step couldn't complete within time limit.

**When occurs?**:

* Slow API response
* Page loads too long
* Complex JavaScript exceeds timeout

**What to do?**:

* Increase step timeout in settings
* Optimize page performance
* Add explicit wait steps
* Break into multiple steps
* Check network/server performance

#### SINGLE\_TEST\_TIME\_EXCEEDED

Test exceeded maximum test duration for current plan.

**When occurs?**:

* 65 minutes with 60 minute limit
* Free plan 10 min limit exceeded
* Waits/delays accumulate

**What to do?**:

* Optimize test to run faster
* Upgrade plan for higher limits
* Split into multiple shorter tests
* Reduce/remove explicit waits

### Browser & Extension Errors

#### UNSUPPORTED\_BROWSER

You are using an outdated and unsupported browser

**When occurs?**:

* Chrome 80 when minimum is 90
* Old version missing APIs
* Beta/canary with incompatible changes
* Chromium missing features

**What to do?**:

* We suggest updating it to the most recent version
* Update browser to latest stable version
* Use supported version (check docs)
* Switch to Chrome if using alternative

#### DEBUGGER\_DETACHED

Chrome debugger detached

**When occurs?**:

* User clicks "Cancel" on debugging notification
* Manually detaching from DevTools
* Debugger lost due to crash

**What to do?**:

* Don't click "Cancel" in the Chrome toolbar saying "BugBug is debugging your browser"
* Don't manually detach debugger
* Try to run the test again
* Restart browser if crashed

#### BLOCKED\_BY\_BROWSER\_POLICY

BugBug could not run on this page due to extension settings policy

**When occurs?**:

* Chrome Enterprise blocks extensions on domains
* Sandboxed iframe (reCAPTCHA) blocks execution
* Opera without "Allow access to search page results"
* Corporate IT policy restricts permissions
* Site access settings block domain

**What to do?**:

* If using Opera browser, turn on "Allow access to search page results" option in BugBug extension settings
* Verify if your app is using any sandboxed iframe which blocks BugBug from running (e.reCAPTCHA)
* If your organization is using Chrome Enterprise, contact your IT administrator
* Check extension site access settings

### Configuration & Settings Errors

#### INVALID\_CUSTOM\_HEADERS

Custom headers provided in project's browser settings are invalid

**When occurs?**:

* Header with spaces "invalid header:value"
* Missing colon "Authorization Bearer token"
* Invalid characters "X-Custom-Header!: value"
* Malformed list

**What to do?**:

* Verify they follow the correct format (e.g., key:value, x-second-key:value)
* Ensure colon separator between key and value
* Ensure headers' names do not contain any spaces or other forbidden characters
* Check line breaks in header list

#### INVALID\_DATA\_FORMAT

Provided data has not valid format

**When occurs?**:

* Invalid date "2024-13-45"
* Malformed JSON
* Invalid email format
* Wrong data type (string instead of number)

**What to do?**:

* You need to update a value in the field or re-record this step
* Fix date format
* Validate JSON syntax
* Correct email format
* Use correct data type

### System Errors

#### RUNTIME\_ERROR

Unexpected runtime error

**When occurs?**:

* "Failed to resume runner"
* Tab context not found
* Unexpected extension state
* Memory/resource exhaustion

**What to do?**:

* Rerun test
* Reload extension
* Restart browser
* Contact support with error details

#### INTERNAL\_ERROR

Critical internal error

**When occurs?**:

* Severe internal failures
* Unhandled exception in core logic
* Data corruption
* Critical bug

**What to do?**:

* Rerun test
* Reload extension
* Clear browser cache and extension data
* Contact support with detailed information

#### INITIALIZATION\_ERROR

Error during test run initialization

**When occurs?**:

* Failed browser session setup
* Can't connect debugger
* Error opening window
* Failed script injection

**What to do?**:

* Rerun test
* Restart browser
* Check browser permissions
* Ensure no other debugging tools attached
* Contact support

#### STEP\_RUN\_INITIALIZATION\_ERROR

Error during step run initialization

**When occurs?**:

* Failed step environment preparation
* Can't access step data
* Error setting up resources
* Previous state not cleaned

**What to do?**:

* Rerun test
* Check step configuration
* Verify test data valid
* Contact support

#### UNRECOGNIZED\_STEP\_TYPE

Step type not supported

**When occurs?**:

* Corrupted step data
* Test from newer version
* Database corruption
* Custom step type not recognized

**What to do?**:

* Update extension to latest version
* Re-create step with correct type
* Check for data corruption
* Contact support

#### FRAME\_IS\_NOT\_INITIALIZED

Frame exists but not initialized

**When occurs?**:

* Scripts not injected
* Iframe loads too quickly
* Security policy prevents injection

**What to do?**:

* Add wait step
* Increase timeout
* Check console for security errors
* Contact support

#### INVALID\_MOUSE\_INPUT\_PARAMS

Mouse parameters invalid

**When occurs?**:

* Invalid button type
* Negative coordinates
* Invalid modifier keys
* Corrupted event data

**What to do?**:

* Re-record step
* Check configuration for invalid values
* Contact support

#### FILE\_DOES\_NOT\_EXIST

Upload file doesn't exist

**When occurs?**:

* Non-existent file path
* File deleted/moved
* Wrong path

#### FILE\_UPLOAD\_ERROR

Generic file upload error

**When occurs?**:

* Insufficient permissions
* File locked by another process
* File size exceeds limits
* File type not accepted

**What to do?**:

* Check file permissions
* Ensure file not open elsewhere
* Verify file size within limits
* Check file type accepted
* Try different file

#### VALUE\_COMPUTING\_ERROR

There was an error while parsing variables

**When occurs?**:

* Single braces {variable}
* Malformed {{variable}
* Invalid characters {{user-name}}
* Nested braces

**What to do?**:

* If you are going to use variables, make sure you use double braces like this: {{variable}}
* Ensure complete syntax
* Use alphanumeric and underscores only
* Check for typos

#### WEBSOCKET\_ERROR

WebSocket connection error

**When occurs?**:

* Connection fails during cloud run
* Firewall blocks WebSocket
* WebSocket server down/unreachable
* Connection drops during test

**What to do?**:

* Check network/firewall settings
* Verify WebSocket server availability
* Check for network stability
* Contact support for cloud runs

#### WEBSOCKET\_SETUP\_ERROR

Failed to set up WebSocket

**When occurs?**:

* Can't establish initial connection for cloud runs
* Invalid WebSocket URL/credentials
* Proxy/firewall blocks handshake
* SSL/TLS certificate issues

**What to do?**:

* Verify WebSocket URL and credentials
* Check proxy/firewall settings
* Verify SSL/TLS certificates
* Contact support

#### REQUEST\_ERROR

API request failed

**When occurs?**:

* BugBug API is noit responsive
* Network timeout during request

**What to do?**:

* Verify network connection
* Contact support

#### LOGS\_UPLOAD\_TIMEOUT

Log upload exceeded timeout

**When occurs?**:

* Network issues prevent upload
* Very large log file
* Connection interrupted

**What to do?**:

* Optimize test or app to reduce log size
* Switch logs settings from to "Console logs"
* Disable logs

#### EXTENSION\_DOES\_NOT\_RESPONSE

Extension doesn't respond within timeout

**When occurs?**:

* Extension unresponsive
* Heavy page load causes hang
* Browser throttles extension
* Communication timeout

**What to do?**:

* Increase step timeout
* Reload extension and retry
* Check browser performance and close tabs
* Update browser
* Contact support

#### EXTENSION\_DISCONNECTED

Your BugBug extension has been disconnected

**When occurs?**:

* Network issues interrupt communication
* Extension reloaded during test
* Browser update forces restart
* Extension crashes

**What to do?**:

* Check your internet connection
* Don't reload extension during test
* Avoid browser updates during test
* Try again

#### EXTENSION\_DISCONNECTED\_ERROR

Your BugBug extension has been disconnected

**When occurs?**:

* Extension crashes due to memory
* Extension disabled by user
* Browser kills extension for resource usage
* Extension update interrupts test

**What to do?**:

* Check your internet connection
* Check extension status
* Close unnecessary tabs to free resources

#### TAKING\_SCREENSHOT\_TIMEOUT

Screenshot capture exceeded timeout

**When occurs?**:

* Screenshot takes >10 seconds
* Page with very large images/canvas
* Browser under heavy load
* Graphics driver issues

**What to do?**:

* Optimize page images/canvas size
* Close unnecessary tabs to reduce load
* Update graphics drivers

#### MISSING\_STEP\_SCREENSHOT

Step screenshot missing

**When occurs?**:

* Screenshot capture failed
* Browser API returned null
* Insufficient memory
* Tab closed before screenshot

**What to do?**:

* Ensure sufficient memory available
* Don't close tabs during test
* Rerun test
* Contact suppoer if issue persists

#### MISSING\_ELEMENT\_SCREENSHOT

Element screenshot missing

**When occurs?**:

* Element screenshot failed
* Element moved/disappeared
* Element outside viewport
* Browser API error

**What to do?**:

* Scroll element into view
* Rerun test
* Contact suppoer if issue persists
