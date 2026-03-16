# Source: https://scrapfly.io/docs/scrape-api/javascript-scenario

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/scrape-api/javascript-scenario

Markdown Content:
Javascript Scenario
-------------------

Scrapfly's [js_scenario](https://scrapfly.io/docs/scrape-api/getting-started#api_param_js_scenario) provides an ability to fully control a headless web browser. Javascript Scenario can be used to issue browser commands like clicking buttons, filling in forms, scrolling and executing custom javascript code. Currently these actions are supported:

[click](https://scrapfly.io/docs/scrape-api/javascript-scenario#click)[fill](https://scrapfly.io/docs/scrape-api/javascript-scenario#fill)[condition](https://scrapfly.io/docs/scrape-api/javascript-scenario#condition)[wait](https://scrapfly.io/docs/scrape-api/javascript-scenario#wait)[scroll](https://scrapfly.io/docs/scrape-api/javascript-scenario#scroll)[execute](https://scrapfly.io/docs/scrape-api/javascript-scenario#execute)[select](https://scrapfly.io/docs/scrape-api/javascript-scenario#select)

> This feature requires [Javascript Rendering enabled](https://scrapfly.io/docs/scrape-api/javascript-rendering)and the target page must be of HTML type.

Javascript scenario details are available in the API response `result.browser_data.js_scenario` as well as the monitoring dashboard:

javascript scenario view on monitoring dashboard

[Usage](https://scrapfly.io/docs/scrape-api/javascript-scenario#usage)
----------------------------------------------------------------------

Javascript scenario consists of one or multiple browser actions that are passed to Scrapfly as a [base64 encoded](https://scrapfly.io/web-scraping-tools/base64) JSON array. An average scenario looks something like this:

```
[
    {"fill": {"selector": "#username", "value":"demo"}},
    {"fill": {"selector": "#password", "value":"demo"}},
    {"click": {"selector": "form input[type='submit']"}},
    {"wait_for_navigation": {"timeout": 5000}}
]
```

Each scenario step is a JSON object with a single key that represents the action to be performed and details of the action.

Once you design your javascript scenario use Scrapfly's [base64 encoding](https://scrapfly.io/web-scraping-tools/base64) online tool to convert it to a base64 encoded string that can be passed to the API for execution.

### [Note on Timeouts](https://scrapfly.io/docs/scrape-api/javascript-scenario#timeouts)

The entire Javascript Scenario has an execution **budget of 25 seconds**. Scrapfly does a rough estimation on the maximum JS scenario execution time and will reject any scenarios that are estimated to take more than 25 seconds.

> For long-running javascript scenario requiring more than 25s - You can check our guide on [how timeout works](https://scrapfly.io/docs/scrape-api/understand-timeout)
> 
> * * *
> 
> **TL;DR**`retry=false`timeout after `90s`by default and you can customize the timeout with `retry=false&timeout=120000`

### [Full example with API Player](https://scrapfly.io/docs/scrape-api/javascript-scenario#full-example-player)

The best way to get familiar with Javascript Scenarios is to use the [Scrapfly Web Player](https://scrapfly.io/dashboard/playground/web-scraper) to design and test your scenario. However, here's an example to get you started. The below scenario will login to [web-scraping.dev/login](https://scrapfly.io/docs/scrape-api/javascript-scenario) by performing these steps:

*   Select username input box and fill value `user123`
*   Select password input box and fill value `password`
*   Select and click login button
*   Wait for navigation to acknowledge button click for maximum of 5 seconds

```
[
    {"fill": {"selector": "input[name=username]", "value":"user123"}},
    {"fill": {"selector": "input[name=password]", "value":"password"}},
    {"click": {"selector": "button[type='submit']"}},
    {"wait_for_navigation": {"timeout": 5000}}
]
```

Then, this scenario can be base64 encoded and passed to Scrapfly API for execution:

```
curl -G \
--request "GET" \
--url "https://api.scrapfly.io/scrape" \
--data-urlencode "render_js=true" \
--data-urlencode "js_scenario=W3siZmlsbCI6eyJzZWxlY3RvciI6ImlucHV0W25hbWU9dXNlcm5hbWVdIiwidmFsdWUiOiJ1c2VyMTIzIn19LHsiZmlsbCI6eyJzZWxlY3RvciI6ImlucHV0W25hbWU9cGFzc3dvcmRdIiwidmFsdWUiOiJwYXNzd29yZCJ9fSx7ImNsaWNrIjp7InNlbGVjdG9yIjoiYnV0dG9uW3R5cGU9J3N1Ym1pdCddIn19LHsid2FpdF9mb3JfbmF2aWdhdGlvbiI6eyJ0aW1lb3V0Ijo1MDAwfX1d" \
--data-urlencode "key=__API_KEY__" \
--data-urlencode "url=https://web-scraping.dev/login"
```

`https://api.scrapfly.io/scrape?render_js=true&js_scenario=W3siZmlsbCI6eyJzZWxlY3RvciI6ImlucHV0W25hbWU9dXNlcm5hbWVdIiwidmFsdWUiOiJ1c2VyMTIzIn19LHsiZmlsbCI6eyJzZWxlY3RvciI6ImlucHV0W25hbWU9cGFzc3dvcmRdIiwidmFsdWUiOiJwYXNzd29yZCJ9fSx7ImNsaWNrIjp7InNlbGVjdG9yIjoiYnV0dG9uW3R5cGU9J3N1Ym1pdCddIn19LHsid2FpdF9mb3JfbmF2aWdhdGlvbiI6eyJ0aW1lb3V0Ijo1MDAwfX1d&key=&url=https%3A%2F%2Fweb-scraping.dev%2Flogin`

### [Example of response with scenario](https://scrapfly.io/docs/scrape-api/javascript-scenario#example-response)

```
...
"result": {
    ...,
    "browser_data": {
        "xhr_call": [...],
        "local_storage_data": {
            "csm-hit": "tb:s-5B0K136YR4QK89MQ8RG0|1596420691120&t:1596420692684&adb:adblk_no",
            "csm:adb": "adblk_no",
            "csm-bf": "[\"5B0K136YR4QK89MQ8RG0\"]",
            "a-font-class": "a-ember"
        },
        "session_storage_data": {
            "csm-hit": "tb:s-5B0K136YR4QK89MQ8RG0|1596420691120&t:1596420692684&adb:adblk_no",
            "csm:adb": "adblk_no",
            "csm-bf": "[\"5B0K136YR4QK89MQ8RG0\"]",
            "a-font-class": "a-ember"
        },
        "websockets": [],
        "javascript_evaluation_result": null,
        "js_scenario": {
            "duration": 4.92,
            "executed": 4,
            "steps": [
                {
                    "action": "fill",
                    "config": {
                        "selector": "input[name=username]",
                        "value": "user123"
                    },
                    "duration": 1.11,
                    "executed": true,
                    "result": null,
                    "success": true
                },
                {
                    "action": "fill",
                    "config": {
                        "selector": "input[name=password]",
                        "value": "password"
                    },
                    "duration": 0.47,
                    "executed": true,
                    "result": null,
                    "success": true
                },
                {
                    "action": "click",
                    "config": {
                        "ignore_if_not_visible": false,
                        "selector": "button[type='submit']"
                    },
                    "duration": 0.52,
                    "executed": true,
                    "result": null,
                    "success": true
                },
                {
                    "action": "wait_for_navigation",
                    "config": {
                        "expect_url": null,
                        "timeout": 5000
                    },
                    "duration": 1.81,
                    "executed": true,
                    "result": null,
                    "success": true
                }
            ]
        },
    },
    ...
}
...
```

Scenario Step Types
-------------------

Currently, 8 scenario types are supported. Each scenario type has a different set of mandatory and optional parameters.

*   [MANDATORY] param_name:type
*   [OPTIONAL] param_name:type

### [Click](https://scrapfly.io/docs/scrape-api/javascript-scenario#click)

selector:string ignore_if_not_visible:bool=false timeout budget (ms): +2500
Click on a visible element. It's a native click which emits a [trusted event](https://developer.mozilla.org/en-US/docs/Web/API/Event/isTrusted) - **it's not simulated using javascript.**

#### [Internal Workflow](https://scrapfly.io/docs/scrape-api/javascript-scenario#internal-click)

    *   Waits for the element to be visible
    *   Moves the viewport to the element (mouse and scroll as a human would)
    *   Focuses the element
    *   Left clicks

#### [Parameters](https://scrapfly.io/docs/scrape-api/javascript-scenario#parameters-click)

    *   selector:string Accept CSS Selector and XPATH Selector
    *   ignore_if_not_visible:bool Wait the element if visible or skip if not
    *   multiple:bool If multiple elements match, click on all matched elements

#### [Usage](https://scrapfly.io/docs/scrape-api/javascript-scenario#usage-click)

`{"click": {"selector": ".cookie-gdpr-consent", "ignore_if_not_visible": true)}}`

`{"click": {"selector": "submit.btn"}}`

### [Fill](https://scrapfly.io/docs/scrape-api/javascript-scenario#fill)

selector:string value:string timeout budget (ms): +${timeout} +500
Type a text value in the targeted element. The typing is not simulated using javascript - it's from a real keyboard input.

#### [Internal Workflow](https://scrapfly.io/docs/scrape-api/javascript-scenario#internal-fill)

    *   Waits for the element to be visible
    *   Moves the viewport to the element (mouse and scroll as a human would)
    *   Focuses the element
    *   Types the text value into the input as a human would

#### [Parameters](https://scrapfly.io/docs/scrape-api/javascript-scenario#parameters-fill)

    *   selector:string Any **valid** CSS and XPATH Selector
    *   value:string Value to type in element
    *   clear:boolean Clear the input field before writing

#### [Usage](https://scrapfly.io/docs/scrape-api/javascript-scenario#usage-fill)

`{"fill": {"selector": "#name", "value": "John Do")}}`

### [Condition](https://scrapfly.io/docs/scrape-api/javascript-scenario#condition)

Condition are exclusive to one of

    *   status_code:int
    *   selector:string
        *   selector_state:string=existing
        *   timeout:int=1000

action:string=continue
### Parameters

    *   selector:string Any **valid** CSS or XPATH selector
    *   selector_state:string Can be `existing` or `not_existing`
    *   action:string Action when the condition is met, can be `continue`, `exit_success`, `exit_failed`

Play the scenario only if the condition is met. For example, it can stop processing scenario if non-200 status code is encountered.

#### [Internal Workflow](https://scrapfly.io/docs/scrape-api/javascript-scenario#internal-condition)

    *   Checks whether response status code matches the required status code codintions

#### [Usage](https://scrapfly.io/docs/scrape-api/javascript-scenario#usage-condition)

`{"condition": {"status_code": 200}}`

### [Wait](https://scrapfly.io/docs/scrape-api/javascript-scenario#wait)

timeout budget (ms): +${wait}
Pause during the scenario to give browser some time to load. Note that the pause time is part of the scenario budget

#### [Parameters](https://scrapfly.io/docs/scrape-api/javascript-scenario#parameters-wait)

There are no parameters - pass the wait time in milliseconds directly

#### [Usage](https://scrapfly.io/docs/scrape-api/javascript-scenario#usage-wait)

`{"wait": 2000}`

### [Scroll](https://scrapfly.io/docs/scrape-api/javascript-scenario#scroll)

element:string=body selector:string=bottom timeout budget (ms): +500
Scroll to the selector (or the bottom of the page if no selector provided). If the element parameter is a valid selector, the scrolling wil be executed within the selected element. The scroll is not simulated using javascript - it's created with a real mouse input.

#### [Internal Workflow](https://scrapfly.io/docs/scrape-api/javascript-scenario#internal-scroll)

    *   Waits for the selector to be visible (if set)
    *   Waits for the element to be visible (if set) and binds scroll to the element
    *   Scrolls the page as a human would

#### [Parameters](https://scrapfly.io/docs/scrape-api/javascript-scenario#parameters-scroll)

    *   element:string=body a valid css selector or xpath or "body"
    *   selector:string a valid css selector or xpath or "bottom" as target to scroll
    *   infinite:int=0 infinite scroll - number of scroll iteration
    *   click_selector:string a valid css selector or xpath to click on after the scroll - like a "view more" button

#### [Usage](https://scrapfly.io/docs/scrape-api/javascript-scenario#usage-scroll)

`{"scroll": {"selector": "bottom"}}`

`{"scroll": {"selector": "#pricing"}}`

`{"scroll": {"element": "#scrollable-list", "selector": "bottom", "infinite": 2}}`

### [Execute](https://scrapfly.io/docs/scrape-api/javascript-scenario#execute)

timeout:int=3000 timeout budget (ms): +${timeout}
Execute a javascript script and store the result if a result is returned

#### [Internal Workflow](https://scrapfly.io/docs/scrape-api/javascript-scenario#internal-execute)

    *   The Javascript code is executed
    *    If the javascript code returns a value - it's stored and available in API response `result.browser_data.js_scenario.steps`. Note that each "execute" step has a `result` entry. 
    *   Supports async/await function

#### [Parameters](https://scrapfly.io/docs/scrape-api/javascript-scenario#parameters-execute)

    *   script:string Script to execute. It can return a serializable value
    *   timeout:int Timeout to wait after the script execution have started - expressed in millisecond

#### [Usage](https://scrapfly.io/docs/scrape-api/javascript-scenario#usage-execute)

`{"execute": {"script": "document.querySelector(\"body\").style.backgroundColor = \"red\";}"}`

`{"execute": {"script": "return navigator.userAgent", "timeout": "1000"}`

### [Wait For Navigation](https://scrapfly.io/docs/scrape-api/javascript-scenario#wait_for_navigation)

timeout:int=1000 timeout budget (ms): +${timeout} + 1500
Time to wait to detect a navigation / changing page. The given timeout + 1500 (1.5s) is added to the scenario budget - this additional time represent the average duration of a standard page loading (with assets, xhr, etc). For example if you set a timeout of 1000, 2500 is counted.

#### [Parameters](https://scrapfly.io/docs/scrape-api/javascript-scenario#parameters-wait-nav)

    *   timeout:int Maximum timeout to wait for a navigation - expressed in millisecond

#### [Usage](https://scrapfly.io/docs/scrape-api/javascript-scenario#usage-wait-nav)

`{"wait_for_navigation": {}}`

`{"wait_for_navigation": {"timeout": 5000}}`

### [Wait For Selector](https://scrapfly.io/docs/scrape-api/javascript-scenario#wait_for_selector)

selector:string=body state:string=visible timeout budget (ms): +${timeout}
Wait the element is visible (if state=visible) in the page or the element disappear (state=hidden). If the selector is not present in the desired state until the timeout this step failed and the scenario is aborted. The timeout is added to the scenario budget

#### [Parameters](https://scrapfly.io/docs/scrape-api/javascript-scenario#parameters-wait-sel)

    *   selector:string=body a valid css selector or xpath or "body"
    *   state:string=visible state of the element in the page "visible" or "hidden"
    *   timeout:int=5000 Timeout to wait before fail - expressed in milliseconds 

#### [Usage](https://scrapfly.io/docs/scrape-api/javascript-scenario#usage-wait-sel)

`{"wait_for_selector": {"selector": "#pricing"}}`

`{"wait_for_selector": {"selector": "#loading", "state": "hidden", "timeout": 10000}}`

### [Select](https://scrapfly.io/docs/scrape-api/javascript-scenario#select)

selector:string value:string option_selector:string text:string index:int timeout:int=5000 timeout budget (ms): +${timeout}
Select an option from a dropdown menu. Supports both native HTML `<select>` elements and custom dropdown implementations (e.g., React Select, Material UI Select, custom dropdown widgets). The selection uses real human-like interaction - **it's not simulated using javascript.**

#### [Internal Workflow](https://scrapfly.io/docs/scrape-api/javascript-scenario#internal-select)

    *   Waits for the dropdown trigger element to be visible
    *   For native `<select>`: selects the option matching the given value
    *   For custom dropdowns: clicks the trigger, waits for options to appear, then clicks the matching option

#### [Parameters](https://scrapfly.io/docs/scrape-api/javascript-scenario#parameters-select)

    *   selector:string CSS or XPath selector for the dropdown trigger element
    *   value:string For native `<select>` - match by the option's `value` attribute
    *   option_selector:string For custom dropdowns - CSS selector for the option elements
    *   text:string Match option by visible text (used with `option_selector`)
    *   index:int Match option by zero-based index (used with `option_selector`)
    *   timeout:int=5000 Maximum time to wait - expressed in milliseconds

> Use `value`for native `<select>`elements, or `option_selector`for custom dropdowns. When using `option_selector`, optionally add `text`or `index`to narrow the match.

#### [Usage](https://scrapfly.io/docs/scrape-api/javascript-scenario#usage-select)

**Native `<select>` element:**

`{"select": {"selector": "select#country", "value": "US"}}`

**Custom dropdown - match by CSS attribute:**

`{"select": {"selector": ".country-select", "option_selector": ".option[value='US']"}}`

**Custom dropdown - match by visible text:**

`{"select": {"selector": ".dropdown-trigger", "option_selector": ".dropdown-item", "text": "Germany"}}`

**Custom dropdown - match by index:**

`{"select": {"selector": ".dropdown-trigger", "option_selector": "[role='option']", "index": 2}}`
