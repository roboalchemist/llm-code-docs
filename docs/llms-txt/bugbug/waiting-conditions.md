# Source: https://docs.bugbug.io/preventing-failed-tests/waiting-conditions.md

# Waiting conditions

## Smart waiting before running a step

Before running each test step, BugBug will do a series of checks if your page is ready for this action.&#x20;

For example, before BugBug tries to click a button, it will check if the page finished loading, if the button exists and if it's visible. If those conditions are met, BugBug will attempt to click the button. Such conditions are called **"*****Waiting conditions*****"**.

Benefits:

* **more stable tests**
* you don't need to hardcode manual delays
* more intelligent tests running, behaving more like a human and not a machine

## Available waiting conditions&#x20;

### Document readyState is complete

BugBug waits until your page is ready to interact with and if all the basic assets are loaded. In technical terms this is waiting for `onload` window event.

### Page network requests are finished

BugBug waits until your page has finished loading additional data via other network requests.&#x20;

Even after the page is loaded, your web app needs to request additional data from a server. BugBug will wait until your server requests are more or less finished - by default BugBug will stop waiting when there are not more than 2 unfinished requests for more than 1 second. You can change this in Project Settings.

### Element is visible

BugBug will not interact with the element until it is visible. For example, if you have a "Done" button than only appears after several seconds, BugBug will wait until it appears. That's why you should avoid adding manual delays/sleep.

### Element is not covered by the other one

Same as in "Element is visible" above. BugBug will try not to click something that is covered by another element.

### Element is not animating

This ensures that the animation of the element stopped before BugBug interacts with it.&#x20;

For example, if you have a collapsed section that expands with an animation, BugBug **will wait until it is fully expanded before interacting with its contents**.

This waiting condition is enabled if during the recording you clicked an element that was not animating. If the element has a looping animation, BugBug will disable this waiting condition by default.

### Element must be active

This applies to form elements, that can have a `disabled` attribute. BugBug will hold the step execution until the form element is active. This waiting condition is automatically disabled if during the recording you actually clicked on a disabled element.

### Element has focus

This applies to text input elements. BugBug will wait before typing the letters until it verifies that a text `input` or `textarea` has focus, (meaning that the blinking typing cursor is present the right field)

### Element has an attribute

BugBug will check if element has a attribute with expected value, before interacting with it.

You can add this waiting condition manually, by clicking on "Add condition" in step's "Waiting condition" section.

It requires the expected value to be specified using a specific pattern: `key="value"`, where `key` is the attribute name and `value` is the expected attribute value, e.g. `class="bugbug"`.

### Page will navigate after step execution

This is a special waiting condition that is added automatically by BugBug while recording. If BugBug notices that after a click there's a change in the URL, BugBug will not continue running the next step immediately - it will wait until the URL changes. This also applies to URL history state changes for Single Page Applications.

## Enable or disable waiting conditions

Global waiting conditions can be set up in the project settings.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F4lP77zb3Mk7qsLFDeguj%2FScreenshot%202022-04-11%20at%2018.39.36.png?alt=media\&token=f7e33698-b850-4d27-b480-92d2a945bb72)

You can override waiting conditions per each step. Sometimes you need to disable one of them to prevent unnecessary failed tests.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FRkz8oaNZfPO9pTFytqER%2Fimage.png?alt=media\&token=e9f2b38e-a154-418e-ac51-2396430bef03)

## Skipped waiting conditions

If some waiting conditions are not met, BugBug will anyway try to perform the action. For example, if the page networking has not finished, BugBug will anyway click the button after 30 seconds.&#x20;

You will be notified about skipped waiting conditions by a different green indicator![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FK728O2urlEVlpTbR6p46%2FScreenshot%202022-04-11%20at%2017.59.19.png?alt=media\&token=74c4ecc5-1fe2-45a1-8a4e-186ca914dda8)

[More about test statues](https://docs.bugbug.io/running-tests/statuses)
