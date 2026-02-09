# Source: https://docs.asapp.com/generativeagent/configuring/connect-apis/mock-apis.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Mock API Users

> Learn how to mock APIs for testing and development.

While you are building your API Connection, you can use Mock Data to test the API Connection and ensure your transformations are working as expected. This Mock data saves as a Mock User where you can group mock responses for a given scenario.

<Note>
  The system only uses the Mock Data when testing the API Connection. Use [Test Users](/generativeagent/configuring/tasks-and-functions/test-users) to test and simulate Tasks and Function responses.
</Note>

## Mock Users

A mock user is a collection of mock responses that simulate how your server may respond. Each endpoint in use by an API Connection can have a mock response defined. By default, the mock user will return the [default mock data](/generativeagent/configuring/connect-apis#api-source) defined in the API Connection's API Source.

To Create a Mock User:

<Steps>
  <Step title="Navigate to API Integration Hub > API Mock Users">
    Access the API Mock Users section from the API Integration Hub.
  </Step>

  <Step title="Click 'Create User'">
    Select the 'Create User' button to start creating a new mock user.
  </Step>

  <Step title="Specify the User Details">
    Provide the following information:

    * Name of the User
    * Description of the User
  </Step>

  <Step title="Define Mock Responses">
    The newly created mock user will have a default mock response for each endpoint in the API Connection.

    You can check "Override Default Mock response" and specify a new mock response.

    Make sure to save the mock user to apply the changes.
  </Step>
</Steps>

## Using Mock Users

You can use Mock Users to test your transformations. From within the Response interface, you can select the mock user to use in the "Test Response" panel.

<Frame>
  <img width="500px" src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/mock-user-selection.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=48a0c9b12199cfcbf44c44a419fcc445" alt="Mock User Selection" data-og-width="701" data-og-height="706" data-path="images/generativeagent/connect-apis/mock-user-selection.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/mock-user-selection.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=f85fc0590c05f6b96de0eea42c6a9d40 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/mock-user-selection.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=87fb6d1a17c88ca003818b2054e41517 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/mock-user-selection.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=4f8b3c94d364151d17598d62861135b4 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/mock-user-selection.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=19cf034762c4779c507bce35fa7847d9 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/mock-user-selection.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=c0c8adac4bae9749603bd4451e04fef2 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/mock-user-selection.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=bd91599cd39728910470aee89c332b27 2500w" />
</Frame>

This allows you to save common responses from your server in sets of Mock users. As you iterate on your API Connection, you can test your transformation using the same mock responses.

## Next Steps

<CardGroup>
  <Card title="Test Users" icon="user-check" href="/generativeagent/configuring/tasks-and-functions/test-users">
    Learn how to use test users to simulate and validate task and function responses
  </Card>

  <Card title="Connect APIs" icon="plug" href="/generativeagent/configuring/connect-apis">
    Understand how to connect and configure external APIs with your application
  </Card>

  <Card title="Authentication Methods" icon="key" href="/generativeagent/configuring/connect-apis/authentication-methods">
    Learn how to authenticate your API connections
  </Card>

  <Card title="Integration Guide" icon="code-merge" href="/generativeagent/integrate">
    Step-by-step guide to integrate APIs with your GenerativeAgent implementation
  </Card>
</CardGroup>
