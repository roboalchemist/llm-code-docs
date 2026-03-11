# Source: https://docs.xano.com/testing-debugging/testing-and-debugging-function-stacks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Testing And Debugging Function Stacks

## Testing a Function Stack

<Steps>
  <Step title="Click 'Run' at the top of your workflow to execute it.">
    <Frame>
            <img src="https://mintcdn.com/xano-997cb9ee/WBQXG-4Ngk82eYAW/images/fab65b1e-image.jpeg?fit=max&auto=format&n=WBQXG-4Ngk82eYAW&q=85&s=3ea6b719b266a4eedc61b30b82c536e8" alt="" width="111" height="46" data-path="images/fab65b1e-image.jpeg" />
    </Frame>

    Clicking this button opens the Run panel.
  </Step>

  <Step title="Populate any necessary inputs.">
    This information will be used to test your workflow. If you're copying and pasting JSON from another source, you can use the Format button to quickly turn it into a readable structure if necessary, although this will not impact the functionality of your test run.

    <Frame>
            <img src="https://mintcdn.com/xano-997cb9ee/WBQXG-4Ngk82eYAW/images/ff28e524-image.jpeg?fit=max&auto=format&n=WBQXG-4Ngk82eYAW&q=85&s=7b4701ad8e3ef5ddc194884aa98a0086" alt="" width="479" height="447" data-path="images/ff28e524-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Click 'Run' to execute the workflow.">
    <Tip>
      **Hint - Running in Safe Mode**

      If you're running into memory issues when running large function stacks or working with large data sets, you can run with Safe Mode by clicking the arrow next to the Run button and choosing **Safe Mode**.

      <Frame>
                <img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/14b7479a-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=a298dfba3bc7599ad6b6d3346cbe4589" alt="" width="455" height="222" data-path="images/14b7479a-image.jpeg" />
      </Frame>

      Safe Mode runs the function stack without retaining any context in memory, which can be very helpful when looping over a significant amount of data and you're experiencing crashes. *No context* just means that things like autocomplete won't work, and the output of debugging information will be limited.

      Any questions, please reach out to our support team!
    </Tip>
  </Step>

  <Step title="Review the response and timing, if desired.">
    #### Response

    The response block will show you what the workflow has returned, if applicable, once execution has completed.

    <Frame>
            <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/76a23daf-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=63def27a752ca11d48ac95715afba56d" alt="" width="469" height="524" data-path="images/76a23daf-image.jpeg" />
    </Frame>

    You can see the amount of time the request took to complete, and perform several actions from inside this block.

    Click the Copy button to copy the contents of the response

    Click the Copy Curl button to copy the request as a cURL command to be used outside of Xano

    Click **Create Unit Test** to create a [unit test](/testing-debugging/unit-tests) based on this run.

    Click **Activate Debugger** to activate the debugger — more on this below.

    #### Timing

    You can further review more information for each step that executed during this run in the Timing block.

    <Frame>
            <img src="https://mintcdn.com/xano-997cb9ee/pz6e9Ndbn8i3u8Zz/images/61c5a4f3-image.jpeg?fit=max&auto=format&n=pz6e9Ndbn8i3u8Zz&q=85&s=7571346a1259cada3d3693d07c7c8b9c" alt="" width="470" height="598" data-path="images/61c5a4f3-image.jpeg" />
    </Frame>

    This block will provide individual timings for each step, allowing you to quickly pinpoint any points of delay that could be improved. You can also click the \*\*> \*\*icon next to each step to review that step's output for further investigation.
  </Step>

  <Step title="What's next?">
    Run it again by clicking Run Again , reset everything back to the initial state by clicking Reset , or activate the debugger with Activate Debugger .

    You can also use this opportunity to define sample inputs and responses for your [Swagger (OpenAPI Documentation)](/the-function-stack/building-with-visual-development/apis/swagger-openapi-documentation).

    When [testing your function stacks](/testing-debugging/testing-and-debugging-function-stacks) in Xano, you can define sample input and output examples for your Swagger documentation.

    It is important that you do this to ensure that your documentation is as effective as possible, as well as for helping AI models understand what's expected when interacting with your APIs.

    <Steps>
      <Step title="In the 'response' section of the Run panel, click Set As Example">
        <Frame>
                    <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/a3c4ebc7-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=8d8e78274928ca9c7cd09a8b5ca37975" alt="" width="642" height="312" data-path="images/a3c4ebc7-image.jpeg" />
        </Frame>
      </Step>

      <Step title="Review the sample input and response, and make any necessary adjustments">
        <Warning>
          Make sure these do not include any sensitive information.
        </Warning>

        <Frame>
                    <img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/df1910c3-image.jpeg?fit=max&auto=format&n=_FyaEhYRFYQZinJ0&q=85&s=fd42faaa2cc429800cd1ea1dfeb5cc53" alt="" width="774" height="908" data-path="images/df1910c3-image.jpeg" />
        </Frame>
      </Step>

      <Step title="Click Save and you will see these defined in your Swagger documentation.">
        <Frame>
                    <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/d3752a34-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=a04294b4063e73fb62b3f37222f2abf7" alt="" width="1426" height="995" data-path="images/d3752a34-image.jpeg" />
        </Frame>

        If you need to make adjustments later, you can do so from the settings menu.

        <Frame>
                    <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/58f13ba2-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=7a0c09cd20fe99036fd1fe2920772911" alt="" width="586" height="364" data-path="images/58f13ba2-image.jpeg" />
        </Frame>
      </Step>
    </Steps>
  </Step>
</Steps>

***

## Using the Debugger

The Debugger is used to review each step of execution, one at a time, to pinpoint the cause of any issues that might arise during that run.

<Tip>
  You can also activate the debugger directly from [request history](/maintenance-monitoring-and-logging/request-history#activate-debugger-from-request-history) when viewing a specific API endpoint, allowing you to replay and debug live requests.
</Tip>

<Info>
  Please note that each step is not actually individually being executed; the
  full run has completed prior to the debugger being available.
</Info>

### Simple Mode

\*\*Stop \*\*- Stop Debugging

**Restart** - Restart the Debugger

**Next** - Move to the next step

As you move through each step, the current will be highlighted as shown below.

<Frame><img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/d89349d7-image.jpeg?fit=max&auto=format&n=_FyaEhYRFYQZinJ0&q=85&s=6b30f7b88a793fc7f67674a546f1911d" alt="" width="1348" height="48" data-path="images/d89349d7-image.jpeg" /></Frame>

Completed steps will be highlighted in green.

<Frame><img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/eeaa65f2-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=e7f01b9243c85de284c4bc96b8a8d368" alt="" width="1347" height="48" data-path="images/eeaa65f2-image.jpeg" /></Frame>

As you progress through each step, the **Variables** panel will update with current data.

<Frame><img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/3cef5ce7-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=af21851c79fdbe035fd893977fa60e56" alt="" width="2024" height="509" data-path="images/3cef5ce7-image.jpeg" /></Frame>

Clicking different steps in your function stack will bring the debugger to that point.

<Frame><img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/457ace8b-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=7d4fd5565962e54526e8db0784878bd9" alt="" width="800" height="306" data-path="images/457ace8b-image.jpeg" /></Frame>

### Advanced Options

Click **Turn On Advanced Options** to enable the advanced debugging options.

* **Step Over** - When working with nested function stacks (custom functions or middleware), if you don't need to debug those, just step right over them and continue with the next function in your function stack
* **Step Into / Step Out** - Step into or out of a nested function (custom function or middleware) and continue the debugging experience seamlessly
* **Continue** - Continue with execution of your function stack
* **Enable Breakpoints** - Enable or disable breakpoints as a whole
* **Step Forwards / Step Backwards** - Toggle forward or reverse execution of your function stack
* **Result** - View the result of your completed execution
* **Watches** - Use custom Javascript expressions for more complex data monitoring or calculation as your function stack executes
* **Variables** - View the current contents of your variables as the function stack executes
* **Copy** 📄 / **Add Watch** 👁️ - Copies the variable's current contents, or adds a variable to your Watches list
* **Breakpoints** - Hover over the icon on the left side of each function to establish a breakpoint. Breakpoints will cause the debugger to pause at that step.

## Unknown Errors and Debugger Errors

<Warning>**Unknown Error**</Warning>

<Warning>**The debugger encountered an error**</Warning>

If you see these messages, they could indicate one of the following:

* An unhandled exception in your logic
  * This means that you've likely ran across a rare error that we don't yet have specific messaging for. Please let us know about this so we can make an adjustment.
* Server resource issues

You can also try running your function stack in Safe Mode.

<Tip>
  **Hint - Running in Safe Mode**

  If you're running into memory issues when running large function stacks or working with large data sets, you can run with Safe Mode by clicking the arrow next to the Run button and choosing **Safe Mode**.

  {" "}

  <Frame>  <img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/14b7479a-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=a298dfba3bc7599ad6b6d3346cbe4589" alt="" width="455" height="222" data-path="images/14b7479a-image.jpeg" /></Frame>
  Safe Mode runs the function stack without retaining any context in memory, which
  can be very helpful when looping over a significant amount of data and you're
  experiencing crashes. *No context* just means that things like autocomplete
  won't work, and the output of debugging information will be limited.

  Any questions, please reach out to our support team!
</Tip>

For assistance with either of these errors, please reach out to our support team. You can also review our documentation on [memory usage](/troubleshooting-and-support/troubleshooting-performance/ram-usage) to narrow down the cause.


Built with [Mintlify](https://mintlify.com).