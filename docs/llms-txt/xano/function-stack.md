# Source: https://docs.xano.com/building/build-visually/function-stack.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Function Stack

> Build a function stack in the visual builder

## What is the Function Stack?

The function stack is a hybrid between a traditional code view and a visual builder. It shows you each function in execution order, but in a way that is understandable for non-technical users.

## What does a Function Stack look like?

The Function Stack will be comprised of *up to* three different sections — **inputs**, the **function stack**, and the **response**. Different function stack types may not contain all of the available sections listed below.

<img src="https://mintcdn.com/xano-997cb9ee/bCVIC1Tg3ccBy86J/images/function-stack-20251008-151532.png?fit=max&auto=format&n=bCVIC1Tg3ccBy86J&q=85&s=83a823406de212241627eead7c43832e" alt="function-stack-20251008-151532" width="1171" height="1307" data-path="images/function-stack-20251008-151532.png" />

## Navigating the Function Stack

The Function Stack can be navigated using mouse or keyboard shortcuts, or both. It's designed to feel similar to a traditional code editor, but with the added benefit of visual development and quick editing.

In the Function Stack view, you’ll see different sections depending on what you’re building.

<Frame caption="An example Function Stack of an API endpoint">
    <img src="https://mintcdn.com/xano-997cb9ee/GK7krl3WPzHY1W81/images/function-stack-20251010-143853.png?fit=max&auto=format&n=GK7krl3WPzHY1W81&q=85&s=71323d65d8cb6221fb1dd859ff643eb1" alt="function-stack-20251010-143853" width="949" height="822" data-path="images/function-stack-20251010-143853.png" />
</Frame>

Each section has “Add” buttons that let you create new items in that area, such as inputs or functions.

<Frame caption="Add buttons in a Function Stack">
    <img src="https://mintcdn.com/xano-997cb9ee/GK7krl3WPzHY1W81/images/function-stack-20251010-143931.png?fit=max&auto=format&n=GK7krl3WPzHY1W81&q=85&s=8ac656330692d553b8c403a89c9c8a8e" alt="function-stack-20251010-143931" width="598" height="827" data-path="images/function-stack-20251010-143931.png" />
</Frame>

You can also hover over an existing function in the function stack and click the <span class="ui-bubble"><Icon icon="circle-plus" /></span> icon to insert a new function directly below it. Hovering over any function reveals additional options such as cloning, disabling, or deleting that step.

<Frame caption="Additional function options">
    <img src="https://mintcdn.com/xano-997cb9ee/GK7krl3WPzHY1W81/images/function-stack-20251010-144526.png?fit=max&auto=format&n=GK7krl3WPzHY1W81&q=85&s=fde7c27a025b5182e44ef51f1fdb4273" alt="function-stack-20251010-144526" width="989" height="169" data-path="images/function-stack-20251010-144526.png" />
</Frame>

You can click and drag functions to reorder them within the stack, giving you fine-grained control over execution flow.
To work more efficiently, hold Shift and select multiple functions to perform bulk actions such as disabling, deleting, or copying them to another workflow.

<Frame caption="Click and drag functions to reorder them within the stack">
  <video id="functionstack-drag" autoPlay muted loop playsInline preload="auto" className="w-full aspect-video rounded-xl" src="https://mintcdn.com/xano-997cb9ee/GK7krl3WPzHY1W81/images/functionstack-drag.webm?fit=max&auto=format&n=GK7krl3WPzHY1W81&q=85&s=026b09ec9b945912b7f8b85e0e2d747b" data-path="images/functionstack-drag.webm" />
</Frame>

The Function Stack has two different layout modes that can be switched using the toggle right above the stack:

* <Icon icon="line-height" /> Comfortable view, which spaces out functions for easy reading.
* <Icon icon="align-justify" /> Compact view, which condenses the layout for scanning large workflows.

<Frame caption="Switch between comfortable and compact view">
  <iframe src="https://demo.arcade.software/WQR390zuv69rooQfKjV5?embed" title="https://demo.arcade.software/WQR390zuv69rooQfKjV5?embed" allowFullScreen allow="clipboard-write" class="contentkit-webframe" width="1000" height="500" />
</Frame>

A built-in search bar lets you quickly find functions, variables, or any element in your stack without scrolling.

<Frame caption="Search for functions, variables, or any element in your stack">
    <img src="https://mintcdn.com/xano-997cb9ee/GK7krl3WPzHY1W81/images/function-stack-20251010-145212.png?fit=max&auto=format&n=GK7krl3WPzHY1W81&q=85&s=055a5c293ed50f6fd9934af2375587c0" alt="function-stack-20251010-145212" width="953" height="380" data-path="images/function-stack-20251010-145212.png" />
</Frame>

Prefer working with your keyboard? Xano provides a range of keyboard shortcuts for power users. You can review and customize them from the shortcuts panel directly in the Function Stack view\..

## Building with the Function Stack

Add a function by clicking the <span class="ui-bubble"><Icon icon="circle-plus" /> Add Function</span> button below the function stack, hover over a function and click the <span class="ui-bubble"><Icon icon="circle-plus" /></span> sign, or use your up and down arrow keys to select a row, and press A on your keyboard to add a new function.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/bCVIC1Tg3ccBy86J/images/function-stack-20251008-154316.png?fit=max&auto=format&n=bCVIC1Tg3ccBy86J&q=85&s=171f653b607bbe5b9ff0d9ae121432f5" alt="function-stack-20251008-154316" width="962" height="525" data-path="images/function-stack-20251008-154316.png" />
</Frame>

<br />

<Card title="Learn more about working with functions" icon="square-arrow-up-right" horizontal href="/building/logic/core-components/functions" />

Each function will have a different set of options available to you, so it's best to consult that function's specific documentation for more information.

After you add a function, Xano will sometimes suggest the most likely next step; for example, adding a Query All Records will suggest a loop after. You can choose to add the suggestion, ignore it, or just continue working and Xano will dismiss the suggestion automatically.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/bCVIC1Tg3ccBy86J/images/function-stack-20251008-154710.png?fit=max&auto=format&n=bCVIC1Tg3ccBy86J&q=85&s=36a35184964106ead1cfe174655499e2" alt="function-stack-20251008-154710" width="973" height="239" data-path="images/function-stack-20251008-154710.png" />
</Frame>

You can click the <Icon icon="x" /> icon to tell Xano to never suggest that specific addition again, or to disable suggestions.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/bCVIC1Tg3ccBy86J/images/function-stack-20251008-154802.png?fit=max&auto=format&n=bCVIC1Tg3ccBy86J&q=85&s=f93f732bcdceb5046b9b8c961d3fbfb6" alt="function-stack-20251008-154802" width="414" height="234" data-path="images/function-stack-20251008-154802.png" />
</Frame>

## What's next?

<Card title="Deployment" icon="rocket" href="/deployment" horizontal>
  Learn how deploying your changes to production works
</Card>

<Card title="Building Logic - Core Components" icon="cube" href="/building/logic/core-components" horizontal>
  Learn about the core components of building logic
</Card>

<Card title="Check out another way to build visually" icon="share-nodes" href="/building/build-visually/canvas-view" horizontal>
  Learn about the Canvas View, a visual first but more code-like building experience
</Card>


Built with [Mintlify](https://mintlify.com).