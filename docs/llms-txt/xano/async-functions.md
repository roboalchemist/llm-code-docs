# Source: https://docs.xano.com/the-function-stack/building-with-visual-development/custom-functions/async-functions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Async Functions

> Use async functions to ensure that your custom functions execute exactly as you intend

## What are async functions?

When working with custom functions in Xano, you can choose to have them execute asynchronously. An async function works like a [background task](/the-function-stack/building-with-visual-development/background-tasks), allowing your main process to continue without waiting for the custom function to finish.

## When should I use async functions?

Asynchronous execution can be particularly beneficial in scenarios where you don't want certain tasks to hold up the entire process. For instance, if you're running a complex data fetch or a time-consuming operation, doing it asynchronously means your main application or interface remains responsive to user inputs while the background operation continues independently. This can enhance user experience by reducing wait times.

Here are a few examples of when to use async functions:

* **Loading Data:** When fetching data from a server, such as pulling in user information or loading a list of products, async functions allow the page to display its initial content quickly without waiting for the entire data request to complete.
* **File Uploads:** Starting a file upload process without freezing the interface lets users continue interacting with the application while the file is being processed.
* **Notification Systems:** Sending notifications through email or messaging services asynchronously ensures that users continue their tasks without interruption while the messages are sent in the background.

## Enabling Async Execution

<Steps>
  <Step title="Insert a custom function into your function stack.">
    If you haven't built any custom functions yet, you can review our documentation on them [here](/the-function-stack/functions/custom-functions).
  </Step>

  <Step title="Click 'Synchronous' on the function to change the execution mode.">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/pz6e9Ndbn8i3u8Zz/images/6423d305-image.jpeg?fit=max&auto=format&n=pz6e9Ndbn8i3u8Zz&q=85&s=b4c0d5c0eb0345c3168266d14c93f51a" width="105" height="30" data-path="images/6423d305-image.jpeg" />
    </Frame>
  </Step>

  <Step title="If necessary, retrieve the output of the async function.">
    If a function is set to async, it will return an ID that represents that execution, similar to the value shown below.

    ```
    6f10cc09-d3e0-4ead-9a98-a0bc66bbe673
    ```

    You can use the **Async Function Await** function to retrieve the output of the function once execution completes. Just provide it with an array of the ID(s) returned when the function runs.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/dd91ac5a-image.jpeg?fit=max&auto=format&n=_FyaEhYRFYQZinJ0&q=85&s=ec85d8fdae8da6172c37aaf03004c603" width="647" height="578" data-path="images/dd91ac5a-image.jpeg" />
    </Frame>
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).