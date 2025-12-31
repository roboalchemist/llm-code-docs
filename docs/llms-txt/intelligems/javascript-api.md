# Source: https://docs.intelligems.io/developer-resources/javascript-api.md

# Javascript API

## Overview

The Intelligems JS API lives on the window object: `window.igData`.

The 3 main attributes attached to the `igData` object are:

1. [User Object](https://docs.intelligems.io/developer-resources/javascript-api/user-object) (`igData.user`) - Used for retrieving user, test group, and experiment info.
2. [Price Object](https://docs.intelligems.io/developer-resources/javascript-api/price-object) (`igData.price`) - Used for complicated or custom price testing integrations.
3. [Campaigns Object](https://docs.intelligems.io/developer-resources/javascript-api/campaigns-object) (`igData.campaigns`) - Used for customizing your onsite campaign experience

## Load Timing

As soon as Intelligems is fully loaded on the site, we will set the `igData` object on the window. As soon as this happens, we will fire a window event: `ig:ready`

### Event-based Ready Detection

Here's an example of how you might perform an action when Intelligems is loaded using events:

```javascript
window.addEventListener('ig:ready', () => {
 const experiments = window.igData?.user.getExperiments();
 if (experiments.length) console.log("I have live experiments");
})
```

### Callback-based Ready Detection

For a more convenient approach, you can use the `window.onIgReady` callback system. This property supports both single functions and arrays of functions:

```javascript
// Single callback function
window.onIgReady = () => {
  const experiments = window.igData?.user.getExperiments();
  if (experiments.length) console.log("I have live experiments");
};

// Array of callback functions
window.onIgReady = [
  () => console.log("First callback executed"),
  () => console.log("Second callback executed"),
  () => {
    const experiments = window.igData?.user.getExperiments();
    console.log(`Found ${experiments.length} experiments`);
  }
];
```

**Key Features:**

* **Immediate execution**: If you set `window.onIgReady` after Intelligems is already loaded, the callbacks will execute immediately
* **Error handling**: Each callback is executed safely with error handling to prevent one failing callback from breaking others
* **Flexible**: Supports both single functions and arrays of functions
* **Compatible**: Works alongside the existing `ig:ready` event system
