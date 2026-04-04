# Source: https://docs.asapp.com/generativeagent/configuring/connect-apis/code-api-connections.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Code API Connections

> Create custom API connections using JavaScript code

Code-based API connections allow you to create custom integrations with any external API using JavaScript. This enables you to support any authentication flow or API structure that your external systems require.

You will implement a function that takes a request as input and returns the response that GenerativeAgent will receive. This allows you to transform data, handle complex authentication flows, and integrate with any external system.

## Before You Begin

Before you begin, you will need:

* An ASAPP Dashboard account with Edit permissions for Code based API Connections.

  <Note>
    Your Admin should be able to enable this for you. Reach out to your ASAPP account team if you need help.
  </Note>
* A basic understanding of JavaScript.

## Using Code Based API Connections

<Steps>
  <Step title="Create initial Code API Connection">
    1. Navigate to **API Integration HUB** > **API Connections**
    2. Click **Create Connection**
    3. Select **Code-based API Connection** from the dropdown
    4. Enter a **Name** and optional **Description**.
    5. Click **Create connection**

    This creates a new, unimplemented API connection. You will be dropped into the **Settings** tab.

    <Frame>
            <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/create-code-api.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=79caaccbbe699934b2cf1502acebd9ee" alt="Create Code API Connection" data-og-width="2032" width="2032" data-og-height="918" height="918" data-path="images/generativeagent/connect-apis/create-code-api.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/create-code-api.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=94d4c0b158d7f3ddda82fb5bbca864b3 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/create-code-api.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=c85b0285d2f7288a381e36e024a3be78 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/create-code-api.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=e285f7ca15031c84e6cbbf6a03b7646e 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/create-code-api.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=bcb44349979c69e0209a6fb62783bb23 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/create-code-api.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=8a704314dd2b4fddca6e9ff38a77e8ac 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/create-code-api.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=7b9f04b238330d118ea2e40686669ced 2500w" />
    </Frame>
  </Step>

  <Step title="Set Up Allowed Domains">
    Code-based API connections restrict access to an explicit whitelist of domains as a security measure. You need to add each domain that your code will reach out to.

    1. In the **Basic Settings** tab, specify allowed domains for any API calls your code needs to make
    2. Click **Add Domain** and enter URLs (e.g., `api.example.com`)
    3. Wildcards (`*`) are supported for subdomains
    4. Your code only calls URLs specified in the allowed domains using `asappUtilities.callAPI(url, apiRequest)`

    <Frame>
            <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/allowed-domains.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=76c6a9226c70a4f1f5b383e90c520717" alt="Allowed Domains" data-og-width="1220" width="1220" data-og-height="543" height="543" data-path="images/generativeagent/connect-apis/allowed-domains.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/allowed-domains.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=8af127edd2c03c637f3d720ad877362f 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/allowed-domains.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=f4d19989a5d05c6fef1085480a9d3c84 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/allowed-domains.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=010523dec10325e1c0e9f7745411f9b3 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/allowed-domains.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=90706b96e27cb1858d203e6a1f83943b 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/allowed-domains.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=31250426a5c5cee98d54d1e039a402f3 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/allowed-domains.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=30faf3c86c75bac2764b71759f7b5145 2500w" />
    </Frame>
  </Step>

  <Step title="Manage Environment Variables">
    Store and manage environment variables to be used in your code. This is often used to store data that will change between environments, such as URLs for the API call you will be making.

    <Note>
      Environment variables support storing **Secret** values which the system encrypts when stored in the database. However, for API credentials and authentication data, we strongly recommend using **Authentication Methods** instead, as they provide better security and easier management.
    </Note>

    1. In the **Environment Variables** settings tab, add any variables your code needs.
    2. Specify the value for Sandbox and Production environments.
    3. Use the **Secret** checkbox to store encrypted environment variables (for configuration data, not API credentials)
    4. Access environment variables in your code using `asappUtilities.getEnvVariable("VARIABLE_NAME")`

    <Frame>
            <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/env-variables.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=dff3f6ee0dc276448e4bc15bea70dc67" alt="Environment Variables" data-og-width="1835" width="1835" data-og-height="327" height="327" data-path="images/generativeagent/connect-apis/env-variables.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/env-variables.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=c5ef02b92d06d6911f7be8d93d6912ed 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/env-variables.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=89ea91f25e1ebc678160c92d63c5d53b 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/env-variables.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=a7177e515bf0ceacab14efb00d84f123 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/env-variables.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=2920fdd29fd5dee2be9a72830be42ac5 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/env-variables.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=65a40c06c11d564489f8838cf867b4ae 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/env-variables.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=f389d6b4a9c540df852cf444a7319f0b 2500w" />
    </Frame>
  </Step>

  <Step title="Add Authentication Methods">
    If your API connection requires authentication, add authentication methods to your API connection.

    1. Navigate to **Settings** → **Authentication Methods**
    2. For each environment, click **Add Authentication** to add a new authentication method.
    3. Create a new [authentication method](/generativeagent/configuring/connect-apis/authentication-methods) or select an existing one.

    <Frame>
            <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/add-authentication-methods.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=242b68b3a5357052d7f418565e47680c" alt="Add Authentication Method" data-og-width="1801" width="1801" data-og-height="636" height="636" data-path="images/generativeagent/connect-apis/add-authentication-methods.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/add-authentication-methods.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=4175dc64a69127d396b14e4498378c60 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/add-authentication-methods.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=a94e58f1126c28f8d1b59b3f72cf66dd 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/add-authentication-methods.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=a69831d8992547c33095c84d47e27e17 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/add-authentication-methods.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=eb4b2e43e6f2dc6c90227cae7e43e55a 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/add-authentication-methods.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=166980dadaefa39918890c9af04201f8 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/add-authentication-methods.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=96f4849b5206412947560f50d1ed3f2d 2500w" />
    </Frame>
  </Step>

  <Step title="Define Request and Response Schemas">
    You need to define the structure of data that your API connection will receive and return:

    1. **Request Schema** (`schemas/request.json`) - Define the request schema that your function will receive
    2. **Response Schema** (`schemas/response.json`) - Define the response schema that your function will return

    See the [Request Schema](#request-schema) and [Response Schema](#response-schema) sections below for detailed information on how to structure these schemas.
  </Step>

  <Step title="Implement Your Function">
    Implement the `handleRequest(request)` function in `src/index.js` that takes the request object and returns the response object.

    See the [Implementing the Handle Function](#implementing-the-handle-function) section below for detailed information on how to implement your function.
  </Step>

  <Step title="Test Your Code">
    As you write code, test it to ensure it works as expected:

    1. In the **Run** panel, define an example request that matches your `request.json` schema
    2. Select which environment to run: **Sandbox** or **Production**
    3. Click **Run**
    4. Review the results in the left panel

    You can not publish your code until you have successfully tested it.
  </Step>

  <Step title="Save and Deploy">
    Once you have successfully tested your API connection:

    1. Publish the API connection. This will save your code and make it available as a new version.

       <Note>
         The system does not provide separate Save vs Publish functionality. You must directly publish any changes to your code.
       </Note>
    2. It will now be available for use in your GenerativeAgent tasks and functions. If you have an existing function that uses this API connection, you will need to update it to use the new version.
    3. Test the integration end-to-end to ensure it works as expected
  </Step>
</Steps>

## Request Schema

The request schema (`schemas/request.json`) defines the structure of data that your function will receive. This JSON schema is both the request schema that your function will receive and the parameters shown to GenerativeAgent.

Add the variables you want as input. Ensure the name and description of each variable is easy for GenerativeAgent to understand.

<Tip>
  GenerativeAgent works better with flat JSON object as an input with a reduced number of properties. The more complex the input, the harder it is for GenerativeAgent to understand the request.
</Tip>

<Note>
  By default, the request schema is empty.
</Note>

```json  theme={null}
{
  "additionalProperties": false,
  "type": "object"
}
```

### Example Request Schema

This example takes a last name and confirmation code as input for an airline rebooking function.

```json  theme={null}
{
  "type": "object",
  "properties": {
    "last_name": {
      "type": "string",
      "description": "The last name of the user"
    },
    "confirmation_code": {
      "type": "string",
      "description": "The flight confirmation code from the user"
    }
  },
  "required": ["last_name", "confirmation_code"]
}
```

## Response Schema

The response schema (`schemas/response.json`) defines the structure of data that your function must return. This is the response that GenerativeAgent receives.

Add the variables you want as output. Ensure the name and description of each variable is easy for GenerativeAgent to understand.

<Tip>
  GenerativeAgent can read complex JSON objects more effectively than on request. However, if you are seeing issues with GenerativeAgent not understanding the response, try reducing the number of properties in the response.
</Tip>

<Note>
  By default, the response schema is empty.
</Note>

```json  theme={null}
{
  "additionalProperties": false,
  "type": "object"
}
```

### Example Response Schema

```json  theme={null}
{
  "type": "object",
  "properties": {
    "response": {
      "type": "string",
      "description": "Human-readable response message"
    },
    "data": {
      "type": "array",
      "description": "Array of search results",
      "items": {
        "type": "object",
        "properties": {
          "id": { "type": "string" },
          "title": { "type": "string" },
          "description": { "type": "string" }
        }
      }
    },
    "metadata": {
      "type": "object",
      "description": "Additional metadata about the response",
      "properties": {
        "totalResults": { "type": "number" },
        "query": { "type": "string" }
      }
    }
  },
  "required": ["response"]
}
```

## Implementing the Handle Function

The `handleRequest(request)` function in `src/index.js` is the core of your API connection. This function takes the request object and returns the response object.

When first created, your function looks like this:

```javascript  theme={null}
export async function handleRequest(request) {
  /* 
    Implement this function to handle the request. Return the result or throw an error.
    
    > Success case
    return {
      "response": "Your response text",
      "data": {},
      "metadata": {}
    };
    
    > Failure case (throw an error)
    throw new asappUtilities.APIConnectionError({
      customErrorCode: "SOME_ERROR",  // Codes make it easier to specify logic to GenerativeAgent around error handling
      errorMessage: "Error message", // This is the human readable error message
      error: [Optionally pass along error object]
    });
  */
  throw new asappUtilities.APIConnectionError({
    customErrorCode: "NOT_IMPLEMENTED"
  });
}
```

Replace the `NOT_IMPLEMENTED` error with your own implementation for the API connection.

### Function Parameters

The `request` parameter contains the data defined in your request schema.

### Return Value

Your function should return an object that matches your response schema.

### Error Handling

We expose [`several error classes in the asappUtilities`](#asapp-utilities-errors) library. Always use one of these error classes for error handling to ensure proper error propagation to ASAPP:

```javascript  theme={null}
try {
  // Your API logic here
  return {
    response: "Success message",
    data: resultData,
    metadata: {}
  };
} catch (error) {
  throw new asappUtilities.APIConnectionError({
    customErrorCode: "API_ERROR",
    errorMessage: "API call failed",
    error: error
  });
}
```

## ASAPP Utilities

ASAPP Utilities is a library designed for integration of Code Driven API Connections. It provides tools for writing secure and efficient code.

### Making API Calls

The library provides a secure way to make API calls to allowed domains with the `callAPI` function. This function uses fetch under the hood and follows fetch's interface.

This is the only way to make external HTTP API calls from your code.

```javascript  theme={null}
const response = await asappUtilities.callAPI(`${asappUtilities.getEnvVariable("API_URL")}/data`, {
  method: "GET",
  headers: {
    "Content-Type": "application/json"
  },
  authMethods: {
    prod: "Production API Auth",
    sandbox: "Sandbox API Auth"
  }
});

if (response.status === 200) { // Status codes must be check, non 2XX don't raise errors.
  const data = await response.json();
  console.log("Data received:", data);
} else {
  throw new asappUtilities.APIConnectionError({
    customErrorCode: `API_HTTP_STATUS_ERROR`,
    errorMessage: `API call failed with HTTP status ${response.status}: ${response.statusText}`
  });
}
```

### Environment Variables

Access environment variables configured during setup. Use environment variables for configuration data like API URLs. Do not use environment variables for sensitive credentials.

<Note>
  For API credentials and authentication data, use [Authentication Methods](#using-authentication-methods).
</Note>

```javascript  theme={null}
const apiUrl = asappUtilities.getEnvVariable("API_URL");
console.log(`Using API URL: ${apiUrl}`);
```

### ASAPP Utilities Errors

In order to properly propagate errors to ASAPP, you must throw an `asappUtilities` error:

<AccordionGroup>
  <Accordion title="asappUtilities.APIConnectionError">
    This is a generic error that can be used to catch any error that occurs in your code.

    ```javascript  theme={null}
    try {
      // Your business logic here
      const result = await processUserData(request.userId);
      if (!result) {
        throw new asappUtilities.APIConnectionError({
          customErrorCode: "USER_NOT_FOUND",
          errorMessage: "User data could not be retrieved"
        });
      }
      return result;
    } catch (error) {
      throw new asappUtilities.APIConnectionError({
        customErrorCode: "PROCESSING_ERROR",
        errorMessage: "An error occurred while processing the request",
        error: error
      });
    }
    ```
  </Accordion>

  <Accordion title="asappUtilities.ClientAuthenticationError">
    This is an error that is thrown when a client authentication error occurs.

    Raising this error will cause GenerativeAgent to send an [authentication\_required event](/generativeagent/integrate/handling-events#user-authentication-required) to the client.

    ```javascript  theme={null}
    const response = await asappUtilities.callAPI(url, request);
    if (response.status === 401) {
      throw new asappUtilities.ClientAuthenticationError({
        customErrorCode: "TOKEN_EXPIRED",
        errorMessage: "Token expired and user needs to re-authenticate"
      });
    }
    ```
  </Accordion>
</AccordionGroup>

### Context Data

When you execute an API Connection, the ASAPP system may provide context data available to you in the `context` object.

```javascript  theme={null}
const contextData = asappUtilities.getContextData();
console.log(`Current ASAPP conversation ID: ${contextData.asapp.conversationId}`);
```

<Accordion title="Available Context Data">
  This is the context data that is available to you in the `context` object. Access it using dot notation.

  ```json  theme={null}
  {
    "externalCustomerId": "1234567890", // The external customer ID for the customer
    "asapp": {
      "externalConversationId": "1234567890", // The external conversation ID for the conversation
      "conversationId": "1234567890" // The ASAPP generated ID for the conversation
    }
  }
  ```
</Accordion>

### Fetch Authentication Method Data

To use authentication methods for an API call, provide them as part of the request to `asappUtilities.callAPI()`.

There may be times you want to pull out data from the authentication method, such grabbing claims from a JWT token. You can access the authentication methods you've configured in your code using the `asappUtilities.getAuthMethod()` function.

```javascript  theme={null}
const authMethodResults = asappUtilities.getAuthMethod({
  prod: "prod-auth-method-1",
  sandbox: "sandbox-auth-method-2",
});

// returns array of type {  headers: Record<string, string>; authResultContext?: object; ttlSeconds?:number;}
console.log(`Current authMethodResults: ${authMethodResults}`);
```

## Using Authentication Methods

<Warning>
  **Best Practice**: Always use authentication methods instead of storing API keys in environment variables. Authentication methods provide better security, easier management, and support for complex authentication flows like OAuth, JWT, and custom token management.
</Warning>

If your API connection requires authentication, first you must add the authentcation method in **Settings** > **Authentication Methods**. Then, when making API calls with `asappUtilities.callAPI()`, specify which authentication method to use by name for each environment:

```javascript  theme={null}
const response = await asappUtilities.callAPI(
  "https://api.example.com/data",
  {
    method: "GET",
    headers: {
      "Content-Type": "application/json"
    },
    authMethods: {
      prod: "Your Production Auth Method Name",
      sandbox: "Your Sandbox Auth Method Name",
    },
  }
);
```

The `authMethods` object maps environment names to the exact names of your configured authentication methods. ASAPP automatically applies the appropriate authentication (e.g. tokens, api keys, etc.) to the headers based on the method you've configured for each environment.

**Important**: The authentication method names in your code must exactly match the names you gave them when creating the authentication methods in the **Settings** → **Authentication Methods** section.

## Running your code

While developing your code-based API connection, you can test it by running it in the **Run** panel. This will allow you to test your code without having to publish it. Any `console.log` statements will be displayed in the **Run** panel.

To specify the data that will be passed to your function when running, in the right hand run panel, you need to specify:

* The **Request** object that will be passed to your function. This must match the `request.json` schema.
* The **Context** object that will be passed to your function.
* The **Auth** object that will be passed to your function. This is only used if the authentication method you are using uses [client authentication data](/generativeagent/configuring/connect-apis/authentication-methods#client-authentication-data).

Additionally, you can specify the **Environment** to run your code in in the Environment dropdown.

<Frame>
    <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/run-env-dropdown.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=41207ea038ddc0d811ed6088aa2c60e5" alt="Run Code" data-og-width="1801" width="1801" data-og-height="463" height="463" data-path="images/generativeagent/connect-apis/run-env-dropdown.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/run-env-dropdown.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=4d7b13f3aaaa56c0808afb14e2286e10 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/run-env-dropdown.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=a1dfc94e66be25e424218cbe54b54780 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/run-env-dropdown.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=ab50347e475b2eff0210d8c6a5df83e2 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/run-env-dropdown.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=c8693f1250d56f8ade75333f5dc7444f 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/run-env-dropdown.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=5d5f21749ebde95b46aed8ec767ccf15 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/run-env-dropdown.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=03a692c6e593696cc18df56ae3e13140 2500w" />
</Frame>

## Examples

### Simple API Call

```javascript  theme={null}
export async function handleRequest(request) {
  const { query, context } = request;
  
  try {
    const response = await asappUtilities.callAPI(
      `https://api.example.com/search?q=${encodeURIComponent(query)}`,
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json"
        },
        authMethods: {
          prod: "Production API Auth",
          sandbox: "Sandbox API Auth"
        }
      }
    );
    
    if (!response.ok) {
      throw new Error("API call failed");
    }
    
    const data = await response.json();
    
    return {
      response: `Found ${data.results.length} results for "${query}"`,
      data: data.results,
      metadata: {
        totalResults: data.total,
        query: query
      }
    };
  } catch (error) {
    throw new asappUtilities.APIConnectionError({
      customErrorCode: "API_ERROR",
      error: error
    });
  }
}
```

### Using JWT Claims from Authentication

```javascript  theme={null}
export async function handleRequest(request) {
  const { query, context } = request;
  
  try {
    // Get authentication method results to access JWT token
    const authMethodResults = asappUtilities.getAuthMethod({
      prod: "Production JWT Auth",
      sandbox: "Sandbox JWT Auth"
    });
    
    // Extract user ID from JWT token (assuming it's in the Authorization header)
    let userId = null;
    if (authMethodResults && authMethodResults.length > 0) {
      const authHeaders = authMethodResults[0].headers;
      const authHeader = authHeaders['Authorization'] || authHeaders['authorization'];
      
      if (authHeader && authHeader.startsWith('Bearer ')) {
        const token = authHeader.substring(7);
        // Decode JWT payload (this is a simplified example - in practice, you'd want proper JWT validation)
        try {
          const payload = JSON.parse(atob(token.split('.')[1]));
          userId = payload.user_id || payload.sub;
        } catch (e) {
          console.log('Could not decode JWT token');
        }
      }
    }
    
    // Build API URL with user ID if available
    let apiUrl = `https://api.example.com/data?customer=${context.externalCustomerId}`;
    if (userId) {
      apiUrl += `&user=${encodeURIComponent(userId)}`;
    }
    
    const response = await asappUtilities.callAPI(
      apiUrl,
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json"
        },
        authMethods: {
          prod: "Production JWT Auth",
          sandbox: "Sandbox JWT Auth"
        }
      }
    );
    
    const data = await response.json();
    
    return {
      response: `Customer data retrieved successfully${userId ? ` for user ${userId}` : ''}`,
      data: data,
      metadata: {
        customerId: context.externalCustomerId,
        userId: userId
      }
    };
  } catch (error) {
    throw new asappUtilities.APIConnectionError({
      customErrorCode: "AUTH_ERROR",
      error: error
    });
  }
}
```

## Additional Libraries

Currently, code-based API connections support the core ASAPP Utilities library and do not allow the use of third-party libraries e.g., using `require()` or `import` statements.

If you require additional third-party libraries or tools for your integration, reach out to your ASAPP account team to discuss your specific needs.
