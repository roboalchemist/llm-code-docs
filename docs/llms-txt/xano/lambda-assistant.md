# Source: https://docs.xano.com/building/build-with-ai/lambda-assistant.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Lambda Assistant

> Learn how to use the Lambda Assistant to help build Lambda functions for your backend

The Lambda Assistant can help you build Lambda functions in JavaScript or TypeScript. In most cases, a Lambda isn't necessary, but it can still be helpful if you want to utilize an NPM package that has functionality Xano doesn't support natively.

### Using the Lambda Assistant

<Steps>
  <Step title="Find the Lambda Assistant">
    <Frame caption="You'll find the Lambda Assistant in the top-right corner of the Lambda function.">
            <img src="https://mintcdn.com/xano-997cb9ee/NgWyYUIOE6OPGYha/images/lambda-assistant-20251011-084421.png?fit=max&auto=format&n=NgWyYUIOE6OPGYha&q=85&s=a00b206d98e63e3d31b487dc116dcdf1" alt="lambda-assistant-20251011-084421" width="604" height="407" data-path="images/lambda-assistant-20251011-084421.png" />
    </Frame>
  </Step>

  <Step title="Tell the Assistant about the Lambda you're trying to build">
    Our Lambda functions use Deno behind the scenes, so it will first present you with some helpful syntax tips to get started, which the Assistant is familiar with as well. You can run your function stack beforehand to give the Assistant access to the context of the rest of your logic.

    You can also ask the Assistant to import any NPM packages you need, and it will automatically add the import statement to the top of the function.

    Ask the Assistant to build the Lambda function, and it will generate the code for you.
  </Step>

  <Step title="Review and Iterate">
    Once the Assistant has taken a first pass at your question, you can continue to converse with it to iterate and expand, or correct missteps.
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).