# Source: https://docs.asapp.com/generativeagent/configuring/connect-apis.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Your APIs

> Learn how to connect your APIs to GenerativeAgent with API Connections

GenerativeAgent can call your APIs to get data or perform actions through **API Connections**. These connections allow GenerativeAgent to handle complex tasks like looking up account information or booking flights.

Our API Connection tooling lets you transform your existing APIs into LLM-friendly interfaces that GenerativeAgent can use effectively. Unlike other providers that require you to create new simplified APIs specifically for LLM use, ASAPP's approach lets you leverage your current infrastructure without additional development work.

<Note>
  Typically, a developer or other technical user will create API Connections. If you need help, reach out to your ASAPP team.
</Note>

## Understanding API Connections

API Connections are the bridge between your GenerativeAgent and your external APIs. They allow your agent to interact with your existing systems and services, just like a human agent would.

### How API Connections Fit In

GenerativeAgent uses a hierarchical structure to organize its capabilities:

1. **Tasks**: High-level instructions that tell GenerativeAgent what to do. A task can have one or more functions.
2. **Functions**: Tools that help GenerativeAgent complete tasks. A function can point to a single API Connection.
3. **API Connections**: Configurations that enable Functions to interact with your APIs.

<Frame>
  <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/ga-api-connections-flow.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=76687b1c1d193ebe5e4b693f51eaf970" data-og-width="2446" width="2446" data-og-height="839" height="839" data-path="images/generativeagent/connect-apis/ga-api-connections-flow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/ga-api-connections-flow.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=24c2bb158e1ce419e7e7bb797d1c1f36 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/ga-api-connections-flow.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=b395235986ddf6aeaab5f0aff75e83c8 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/ga-api-connections-flow.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=549ab255d67fd15d34db88a499805411 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/ga-api-connections-flow.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=30a2c8349db38491f3510d47238e9246 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/ga-api-connections-flow.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=b95f368dff51563f806f717ccc6e109a 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/ga-api-connections-flow.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=d9955149ff46d3deb5e1253da079d99e 2500w" />
</Frame>

### Core Components

Each API Connection consists of three main parts that work together:

1. **API Source**:
   * Handles the technical details of calling your API
   * Manages authentication and security
   * Configures environment-specific settings (sandbox/production)

2. **Request Interface**:
   * Defines what information GenerativeAgent can send
   * Transforms GenerativeAgent's requests into your API's format
   * Includes testing tools to verify the transformation

3. **Response Interface**:
   * Controls what data GenerativeAgent receives
   * Transforms the API response to a GenerativeAgent friendly format
   * Includes testing tools to verify the transformation

## Create an API Connections

To create an API Connection, you need to:

<Steps>
  <Step title="Access the API Integration Hub">
    1. Navigate to **API Integration Hub** in your dashboard
    2. Select the **API Connections** tab
    3. Click the **Create Connection** button
  </Step>

  <Step title="Select API Source">
    Choose your API source type:

    <Tabs>
      <Tab title="API Spec">
        Every API Connection requires an [OpenAPI specification](https://spec.openapis.org/oas/latest.html) that defines your API endpoints and structure.

        * Choose an existing API spec from your previously uploaded API Specs, or
        * Upload a new OpenAPI specification file

        <Note>
          We support any API that uses JSON for requests and responses.
        </Note>
      </Tab>

      <Tab title="MCP Server">
        Use an MCP (Model Context Protocol) server to connect tools designed for LLM interaction. See [Using MCP Servers](/generativeagent/configuring/connect-apis/mcp-server) for detailed instructions.
      </Tab>
    </Tabs>
  </Step>

  <Step title="Configure Basic Details">
    Provide the essential information for your connection:

    * **Name**: A descriptive name for the API Connection
    * **Description**: Brief explanation of the connection's purpose
    * **Endpoint**: Select the specific API endpoint from your specification

    <Warning>
      We only support endpoints with JSON request and response bodies.
    </Warning>
  </Step>

  <Step title="Configure the API Source">
    After creation, you'll be taken to the API Source configuration page. Here you'll need to:

    1. Set up [authentication methods](#authentication)
    2. Configure [environment settings](#environment-settings)
    3. Define [error handling](#error-handling) rules
    4. Add any required [static headers](#headers)
  </Step>

  <Step title="Set Up Request and Response Interfaces">
    Configure how GenerativeAgent interacts with your API:

    1. Define the [Request Interface](#request-interface):
       * Specify the schema GenerativeAgent will use
       * Create request transformations
       * Test with sample requests
    2. Configure the [Response Interface](#response-interface):
       * Define the response schema
       * Set up response transformations
       * Validate with sample responses
  </Step>

  <Step title="Test and Validate">
    Before finalizing your API Connection:

    1. Run test requests in the sandbox environment
    2. Verify transformations work as expected
    3. Check error handling behavior
  </Step>

  <Step title="Link to Functions">
    Once your API Connection is configured and tested, you can [reference it in a Function](/generativeagent/configuring#step-4-create-functions) to enable GenerativeAgent to use the API.
  </Step>
</Steps>

## Request Interface

The Request Interface defines how GenerativeAgent interacts with your API. It consists of three key components that work together to enable effective API communication.

* [Request Schema](#request-schema): The schema of the data that GenerativeAgent can send to your API.
* [Request Transformation](#request-transformation): The transformation that will apply to the data before sending it to your API.
* [Testing Interface](#request-testing): The interface that allows you to test the request transformation with different inputs.

<Frame>
  <img width="500px" src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/request-interface.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=edebc50f0e4e8454bf5d070dbb3b7949" alt="Request Interface" data-og-width="1229" data-og-height="1120" data-path="images/generativeagent/connect-apis/request-interface.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/request-interface.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=84d3979d3460475b3b675b4de92b7f76 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/request-interface.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=0029a51cf6570e71babd7e32d9c164b5 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/request-interface.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=76693127c16c5329fa37cd17afba16fb 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/request-interface.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=d1833c77a9392dc02fcb771966588cf1 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/request-interface.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=44b5c4949153510cdfd2e5923b57875a 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/request-interface.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=44cc0615053a72f296c7909cc4cb7c81 2500w" />
</Frame>

### Request Schema

The Request Schema specifies the structure of data that GenerativeAgent can send to your API. This schema should be designed for optimal LLM interaction.

<Warning>
  This schema is NOT the schema of the API. This is the schema that the system shows to GenerativeAgent.
</Warning>

**Best Practices for Schema Design**

<AccordionGroup>
  <Accordion title="Simplify Field Names">
    ```json  theme={null}
    // Good - Clear and descriptive
    {
      "type": "object",
      "properties": {
        "customer_name": {
          "type": "string"
        },
        "order_date": {
          "type": "string"
        }
      }
    }

    // Avoid - Cryptic or complex
    {
      "type": "object", 
      "properties": {
        "cust_nm_001": {
          "type": "string"
        },
        "ord_dt_timestamp": {
          "type": "string"
        }
      }
    }
    ```
  </Accordion>

  <Accordion title="Flatten Complex Structures">
    ```json  theme={null}
    // Good - Flat structure
    {
      "type": "object",
      "properties": {
        "shipping_street": {
          "type": "string"
        },
        "shipping_city": {
          "type": "string"
        },
        "shipping_country": {
          "type": "string"
        }
      }
    }

    // Avoid - Deep nesting
    {
      "type": "object",
      "properties": {
        "shipping": {
          "type": "object",
          "properties": {
            "address": {
              "type": "object",
              "properties": {
                "street": {
                  "type": "string"
                },
                "city": {
                  "type": "string"
                },
                "country": {
                  "type": "string"
                }
              }
            }
          }
        }
      }
    }
    ```
  </Accordion>

  <Accordion title="Add Clear Descriptions">
    ```json  theme={null}
    {
      "properties": {
        "order_status": {
          "type": "string",
          "description": "Current status of the order (pending, shipped, delivered)",
          "enum": ["pending", "shipped", "delivered"]
        }
      }
    }
    ```
  </Accordion>

  <Accordion title="Remove Optional Fields">
    * Keep only essential fields that GenerativeAgent needs
    * Set `"additionalProperties": false` to prevent unexpected data
  </Accordion>
</AccordionGroup>

<Note>
  When first created, the Request Schema is a 1-1 mapping to the underlying API spec.
</Note>

### Request Transformation

The Request Transformation converts GenerativeAgent's request into the format your API expects. This is done using [JSONata](https://jsonata.org/) expressions.

<Note>
  When first created, the Request Transformation is a 1-1 mapping to the underlying API spec.
</Note>

<Frame>
  <img width="500px" src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/request-interface.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=edebc50f0e4e8454bf5d070dbb3b7949" alt="Request Interface Configuration" data-og-width="1229" data-og-height="1120" data-path="images/generativeagent/connect-apis/request-interface.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/request-interface.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=84d3979d3460475b3b675b4de92b7f76 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/request-interface.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=0029a51cf6570e71babd7e32d9c164b5 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/request-interface.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=76693127c16c5329fa37cd17afba16fb 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/request-interface.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=d1833c77a9392dc02fcb771966588cf1 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/request-interface.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=44b5c4949153510cdfd2e5923b57875a 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/request-interface.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=44cc0615053a72f296c7909cc4cb7c81 2500w" />
</Frame>

**Common Transformation Patterns**

<AccordionGroup>
  <Accordion title="Basic Field Mapping">
    ```javascript  theme={null}
    {
      "headers": {
        "Content-Type": "application/json"
      },
      "pathParameters": {
        "userId": request.id
      },
      "queryParameters": {
        "include": "details,preferences"
      },
      "body": {
        "name": request.userName,
        "email": request.userEmail
      }
    }
    ```
  </Accordion>

  <Accordion title="Data Formatting">
    ```javascript  theme={null}
    {
      "body": {
        // Convert date to ISO format
        "timestamp": $toMillis(request.date),
        // Uppercase a value
        "region": $uppercase(request.country),
        // Join array values
        "tags": $join(request.categories, ",")
      }
    }
    ```
  </Accordion>

  <Accordion title="Conditional Logic">
    ```javascript  theme={null}
    {
      "body": {
        // Include field only if present
        "optional_field": $exists(request.someField) ? request.someField : undefined,
        // Transform based on condition
        "status": request.isActive = true ? "ACTIVE" : "INACTIVE"
      }
    }
    ```
  </Accordion>
</AccordionGroup>

### Request Testing

Thoroughly test your request transformations to ensure GenerativeAgent can send the correct data to your API.

The API Connection can not be saved until the request transformation has a successful test.

**Testing Best Practices**

<AccordionGroup>
  <Accordion title="Test Various Scenarios">
    ```json  theme={null}
    // Test 1: Minimal valid request
    {
      "customerId": "123",
      "action": "view"
    }

    // Test 2: Full request with all fields
    {
      "customerId": "123",
      "action": "update",
      "data": {
        "name": "John Doe",
        "email": "john@example.com"
      }
    }
    ```
  </Accordion>

  <Accordion title="Validate Error Cases">
    * Test with missing required fields
    * Verify invalid data handling
    * Check boundary conditions
  </Accordion>

  <Accordion title="Use Sandbox Environment">
    By Default, the API Connection testing is local. You can test against actual API endpoints by setting "Run test in" to Sandbox.

    * Test against actual API endpoints
    * Verify complete request flow
    * Check response handling
  </Accordion>
</AccordionGroup>

## Response Interface

The Response Interface determines how GenerativeAgent processes and presents API responses. A well-designed response interface makes it easier for GenerativeAgent to understand and use the API's data effectively.

There are three main components to the response interface:

* [Response Schema](#response-schema): The JSON schema for the data returned to GenerativeAgent from the API.
* [Response Transformation](#response-transformation): A JSONata transformation where the API response is transformed into the response given to GenerativeAgent.
* [Test Response](#response-testing): The testing panel to test the response transformation with different API responses and see the output.

<Frame>
  <img width="500px" src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/response-interface.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=b897266f7d7347e50cb648cece9ef9c2" alt="Response Interface Configuration" data-og-width="1228" data-og-height="1146" data-path="images/generativeagent/connect-apis/response-interface.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/response-interface.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=d47ae894969d4fa9f1a30781e69fdead 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/response-interface.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=29d43c12f7d0868d6f2ee90e494b9830 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/response-interface.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=46d3daae0625abaa083b390982b3e395 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/response-interface.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=837a8f32aec53351d20353421c216657 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/response-interface.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=2d2e4fe0c4ebd0b2f257a03f570fcba6 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/connect-apis/response-interface.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=13611d8010f0bc133985c002184a719a 2500w" />
</Frame>

### Response Schema

The Response Schema defines the structure of data that GenerativeAgent will receive. Focus on creating clear, simple schemas that are optimized for LLM processing.

<Warning>
  The Response Schema is NOT the schema of the underlying API. This is the schema of what the system returns to GenerativeAgent.
</Warning>

**Schema Design Principles**

<AccordionGroup>
  <Accordion title="Focus on Essential Data">
    ```json  theme={null}
    // Good - Only relevant fields
    {
      "orderStatus": "shipped",
      "estimatedDelivery": "2024-03-20",
      "trackingNumber": "1Z999AA1234567890"
    }

    // Avoid - Including unnecessary details
    {
      "orderStatus": "shipped",
      "estimatedDelivery": "2024-03-20",
      "trackingNumber": "1Z999AA1234567890",
      "internalId": "ord_123",
      "systemMetadata": { /* ... */ },
      "auditLog": [ /* ... */ ]
    }
    ```
  </Accordion>

  <Accordion title="Use Clear Data Types">
    ```json  theme={null}
    {
      "type": "object",
      "properties": {
        "temperature": {
          "type": "number",
          "description": "Current temperature in Celsius"
        },
        "isOpen": {
          "type": "boolean",
          "description": "Whether the store is currently open"
        },
        "lastUpdated": {
          "type": "string",
          "format": "date-time",
          "description": "When this information was last updated"
        }
      }
    }
    ```
  </Accordion>

  <Accordion title="Standardize Formats">
    * Use consistent date/time formats
    * Normalize enumerated values
    * Use standard units of measurement
  </Accordion>
</AccordionGroup>

<Note>
  When first created, the Response Schema is a 1-1 mapping to the underlying API spec.
</Note>

### Response Transformation

Transform complex API responses into GenerativeAgent-friendly formats using JSONata. The goal is to simplify and standardize the data.

The Transformation's input is the raw API response. The output is the data that GenerativeAgent will receive and must match the Response Schema.

<Note>
  When first created, the Response Transformation is a 1-1 mapping to the underlying API spec.
</Note>

**Transformation Examples**

<AccordionGroup>
  <Accordion title="Basic Data Mapping">
    ```javascript  theme={null}
    {
      // Extract and rename fields
      "status": clientApiCall.data.orderStatus,
      "items": clientApiCall.data.orderItems.length,
      "total": clientApiCall.data.pricing.total
    }
    ```
  </Accordion>

  <Accordion title="Date and Time Formatting">
    ```javascript  theme={null}
    {
      // Convert ISO timestamp to readable format
      "orderDate": $fromMillis($toMillis(clientApiCall.data.created_at), 
                              "[FNn], [MNn] [D1o], [Y]"),
      
      // Format time in 12-hour clock
      "deliveryTime": $fromMillis($toMillis(clientApiCall.data.delivery_eta), 
                                 "[h]:[m01] [P]")
    }
    ```
  </Accordion>

  <Accordion title="Complex Data Processing">
    ```javascript  theme={null}
    {
      // Calculate order summary
      "orderSummary": {
        "totalItems": $sum(clientApiCall.data.items[*].quantity),
        "uniqueItems": $count(clientApiCall.data.items),
        "hasGiftItems": $exists(clientApiCall.data.items[type="GIFT"])
      },
      
      // Format address components
      "deliveryAddress": $join([
        clientApiCall.data.address.street,
        clientApiCall.data.address.city,
        clientApiCall.data.address.state,
        clientApiCall.data.address.zip
      ], ", ")
    }
    ```
  </Accordion>
</AccordionGroup>

### Response Testing

Thoroughly test your response transformations to ensure GenerativeAgent receives well-formatted, useful data.

The API Connection can not be saved until the response transformation has a successful test.

Use [API Mock Users](/generativeagent/configuring/connect-apis/mock-apis) to save response from your server to use them in the response testing.

**Testing Strategies**

<AccordionGroup>
  <Accordion title="Test Different Response Types">
    Make sure to test with different response types your server may respond with.

    This should include happy paths, varied response types, and error paths.
  </Accordion>

  <Accordion title="Validate Data Formatting">
    * Check date/time formatting
    * Verify numeric calculations
    * Test string manipulations
  </Accordion>

  <Accordion title="Edge Cases">
    * Handle null/undefined values
    * Process empty arrays/objects
    * Manage missing optional fields
  </Accordion>
</AccordionGroup>

## Redaction

You can redact sensitive fields from API Connection Logs and conversation details views. There are two types of redaction, each affecting different parts of the request/response flow:

* **Request/Response Interface**: The data that GenerativeAgent interacts with
* **Raw API Request/Response**: The actual data sent to and received from the underlying API

<Warning>
  Redacting fields does not affect the data that GenerativeAgent can access. GenerativeAgent requires access to the data in order to perform its tasks. Redaction only impacts the views in the UI.
</Warning>

<Tabs>
  <Tab title="Request/Response Interface">
    Redact fields in the request and response that GenerativeAgent uses. This redacts the transformed data that appears in conversations and API Connection Logs.

    To redact request/response interface fields:

    1. Add `x-redact` to the field in the Request Schema or Response Schema
    2. Save the API connection to apply the changes

    <Note>
      Redacting internal fields affects both API Connection Logs and conversations where GenerativeAgent uses the API.
    </Note>
  </Tab>

  <Tab title="Raw API Request/Response">
    Redact fields in the raw API request and response that are sent to and received from the underlying API. This redacts the underlying API data in API Connection Logs only.

    To redact raw API fields:

    1. Navigate to **API Integration Hub** > **API Specs**
    2. Click on the relevant API Spec
    3. Click on the **Parameters** tab
    4. Per endpoint, click the fields you want to redact

    <Note>
      Redacting raw API fields only affects the [API Connection Logs](#api-connection-logs) as the raw API data is not visible to GenerativeAgent.
    </Note>
  </Tab>
</Tabs>

## API Versioning

Every update to an API Connection requires a version change. This is to ensure that no change can be made to an API connection that impacts a live function.

If you make a change to an API connection, the Function that references that API connection will need to be explicitly updated to point to the new version.

## API Connection Logs

We log all requests and responses for API connections. This allows you to see the raw requests and responses, and the transformations that were applied.

Use the logs to debug and understand how API connections are working.

Logs are available in API Integration Hub > API Connection Logs.

## Default API Spec Settings

You can set default information in an API spec. These default settings serve as a template for newly created API connections, copying those settings for all API connections created for that API spec.

You can set the following defaults:

* Headers
* Sandbox Settings:
  * Base URL
  * Authentication Method
* Production Settings:
  * Base URL
  * Authentication Method

You can make further changes to API connections as necessary.

You can also change the defaults and it will not change existing API connections, though the system will use the new defaults on any new connections made with that Spec.

## Examples

Here are some examples of how to configure API connections for different scenarios.

<AccordionGroup>
  <Accordion title="Update Passenger Name (Simple mapping)">
    This example demonstrates configuring an API connection for updating a passenger's name on a flight booking.

    #### API Endpoint

    ```json  theme={null}
    PUT /flight/[flightId]/passenger/[passengerId]
    {
      "name": {
        "first": [Passenger FirstName],
        "last": [Passenger LastName]
      }
    }
    ```

    #### API Response

    ```json  theme={null}
    {
      "id": "pax-12345",
      "flightId": "XZ2468",
      "updatedAt": "2024-10-04T14:30:00Z",
      "passenger": {
        "id": "PSGR-56789",
        "name": {
          "first": "John",
          "last": "Doe"
        },
        "seatAssignment": "14A",
        "checkedIn": true,
        "frequentFlyerNumber": "FF123456"
      },
      "status": "confirmed",
      "specialRequests": ["wheelchair", "vegetarian_meal"],
      "baggage": {
        "checkedBags": 1,
        "carryOn": 1
      }
    }
    ```

    <AccordionGroup>
      <Accordion title="Request Configuration">
        1. Request Schema:

        ```json  theme={null}
        {
          "type": "object",
          "properties": {
            "externalCustomerId": {"type": "string"},
            "passengerFirstName": {"type": "string"},
            "passengerLastName": {"type": "string"},
            "flightId": {"type": "string"}
          },
          "required": ["externalCustomerId", "passengerFirstName", "passengerLastName", "flightId"]
        }
        ```

        2. Request Transformation:

        ```javascript  theme={null}
        {
          "headers": {},
          "pathParameters": {
            "flightId": request.flightId,
            "passengerId": request.externalCustomerId
          },
          "queryParameters": {},
          "body": {
            "name": {
              "first": request.passengerFirstName,
              "last": request.passengerLastName
            }
          }
        }
        ```

        3. Sample Test Request:

        ```json  theme={null}
        {
          "externalCustomerId": "CUST123",
          "passengerFirstName": "Johnson",
          "passengerLastName": "Doe",
          "flightId": "XZ2468"
        }
        ```
      </Accordion>

      <Accordion title="Response Configuration">
        1. Response Schema:

        ```json  theme={null}
        {
          "type": "object",
          "properties": {
            "success": {
              "type": "boolean",
              "description": "Whether the name update was successful"
            }
          },
          "required": ["success"]
        }
        ```

        2. Response Transformation:

        ```javascript  theme={null}
        {
          "success": $exists(clientApiCall.data.id) and 
                     $exists(clientApiCall.data.passenger.name.first) and 
                     $exists(clientApiCall.data.passenger.name.last) and 
                     clientApiCall.data.status = "confirmed"
        }
        ```

        3. Sample Test Response:

        ```json  theme={null}
        {
          "clientApiCall": {
            "data": {
              "id": "pax-12345",
              "flightId": "XZ2468",
              "updatedAt": "2024-10-04T14:30:00Z",
              "passenger": {
                "id": "PSGR-56789",
                "name": {
                  "first": "John",
                  "last": "Doe"
                },
                "seatAssignment": "14A",
                "checkedIn": true,
                "frequentFlyerNumber": "FF123456"
              },
              "status": "confirmed",
              "specialRequests": ["wheelchair", "vegetarian_meal"],
              "baggage": {
                "checkedBags": 1,
                "carryOn": 1
              }
            }
          }
        }
        ```
      </Accordion>
    </AccordionGroup>
  </Accordion>

  <Accordion title="Lookup Flight Status (Complex mapping)">
    This example shows how to simplify a complex flight status API response by removing unnecessary fields and flattening nested structures.

    #### API Endpoint

    ```json  theme={null}
    GET /flights/[flightNumber]/status
    ```

    #### API Response

    ```json  theme={null}
    {
      "flightDetails": {
        "flightNumber": "AA123",
        "route": {
          "origin": {
            "code": "SFO",
            "terminal": "2",
            "gate": "A12",
            "weather": { /* complex weather object */ }
          },
          "destination": {
            "code": "JFK",
            "terminal": "4",
            "gate": "B34",
            "weather": { /* complex weather object */ }
          }
        },
        "schedule": {
          "departure": {
            "scheduled": "2024-03-15T10:30:00Z",
            "estimated": "2024-03-15T10:45:00Z",
            "actual": null
          },
          "arrival": {
            "scheduled": "2024-03-15T19:30:00Z",
            "estimated": "2024-03-15T19:45:00Z",
            "actual": null
          }
        },
        "status": "DELAYED",
        "aircraft": { /* aircraft details */ }
      }
    }
    ```

    <AccordionGroup>
      <Accordion title="Request Configuration">
        1. Request Schema:

        ```json  theme={null}
        {
          "type": "object",
          "properties": {
            "flightNumber": {
              "type": "string",
              "description": "The flight number to look up"
            }
          },
          "required": ["flightNumber"]
        }
        ```

        2. Request Transformation:

        ```javascript  theme={null}
        {
          "headers": {},
          "pathParameters": {
            "flightNumber": request.flightNumber
          },
          "queryParameters": {},
          "body": {}
        }
        ```

        3. Sample Test Request:

        ```json  theme={null}
        {
          "flightNumber": "AA123"
        }
        ```
      </Accordion>

      <Accordion title="Response Configuration">
        1. Response Schema:

        ```json  theme={null}
        {
          "type": "object",
          "properties": {
            "flight_number": { 
              "type": "string",
              "description": "The flight number"
            },
            "flight_status": { 
              "type": "string",
              "description": "Current status of the flight"
            },
            "origin_airport_code": { 
              "type": "string",
              "description": "Three-letter airport code for origin"
            },
            "destination_airport_code": { 
              "type": "string",
              "description": "Three-letter airport code for destination"
            },
            "scheduled_departure_time": { 
              "type": "string",
              "description": "Scheduled departure time"
            },
            "scheduled_arrival_time": { 
              "type": "string",
              "description": "Scheduled arrival time"
            },
            "is_flight_delayed": { 
              "type": "boolean",
              "description": "Whether the flight is delayed"
            }
          }
        }
        ```

        2. Response Transformation:

        ```javascript  theme={null}
        {
          "flight_number": clientApiCall.data.flightDetails.flightNumber,
          "flight_status": clientApiCall.data.flightDetails.status,
          "origin_airport_code": clientApiCall.data.flightDetails.route.origin.code,
          "destination_airport_code": clientApiCall.data.flightDetails.route.destination.code,
          "scheduled_departure_time": clientApiCall.data.flightDetails.schedule.departure.estimated,
          "scheduled_arrival_time": clientApiCall.data.flightDetails.schedule.arrival.estimated,
          "is_flight_delayed": clientApiCall.data.flightDetails.status = "DELAYED"
        }
        ```
      </Accordion>
    </AccordionGroup>
  </Accordion>

  <Accordion title="Appointment Lookup (Date Formatting)">
    This example demonstrates date formatting and complex object transformation for an appointment lookup API.

    #### API Endpoint

    ```json  theme={null}
    GET /appointments/[appointmentId]
    ```

    #### API Response

    ```json  theme={null}
    {
      "id": "apt_123",
      "type": "DENTAL_CLEANING",
      "startTime": "2024-03-15T14:30:00Z",
      "endTime": "2024-03-15T15:30:00Z",
      "provider": "Dr. Sarah Smith",
      "location": "Downtown Medical Center",
      "patient": {
        "id": "pat_456",
        "name": "John Doe",
        "dateOfBirth": "1985-06-15",
        "contactInfo": {
          "email": "john.doe@email.com",
          "phone": "+1-555-0123"
        }
      },
      "status": "confirmed",
      "notes": "Regular cleaning and check-up",
      "insuranceVerified": true,
      "lastUpdated": "2024-03-01T10:15:00Z"
    }
    ```

    <AccordionGroup>
      <Accordion title="Request Configuration">
        1. Request Schema:

        ```json  theme={null}
        {
          "type": "object",
          "properties": {
            "appointmentId": {
              "type": "string",
              "description": "The ID of the appointment to look up"
            }
          },
          "required": ["appointmentId"]
        }
        ```

        2. Request Transformation:

        ```javascript  theme={null}
        {
          "headers": {},
          "pathParameters": {
            "appointmentId": request.appointmentId
          },
          "queryParameters": {},
          "body": {}
        }
        ```

        3. Sample Test Request:

        ```json  theme={null}
        {
          "appointmentId": "apt_123"
        }
        ```
      </Accordion>

      <Accordion title="Response Configuration">
        1. Response Schema:

        ```json  theme={null}
        {
          "type": "object",
          "properties": {
            "appointmentType": { 
              "type": "string",
              "description": "The type of appointment in a readable format"
            },
            "date": { 
              "type": "string",
              "description": "The appointment date in a friendly format"
            },
            "startTime": { 
              "type": "string",
              "description": "The appointment start time in 12-hour format"
            },
            "doctor": { 
              "type": "string",
              "description": "The healthcare provider's name"
            },
            "clinic": { 
              "type": "string",
              "description": "The location where the appointment will take place"
            },
            "status": {
              "type": "string",
              "description": "The current status of the appointment"
            },
            "patientName": {
              "type": "string",
              "description": "The name of the patient"
            }
          },
          "required": ["appointmentType", "date", "startTime", "doctor", "clinic", "status", "patientName"]
        }
        ```

        2. Response Transformation:

        ```javascript  theme={null}
        {
          /* Convert appointment type from UPPER_SNAKE_CASE to readable format */
          "appointmentType": $replace(clientApiCall.data.type, "_", " ") ~> $lowercase(),
          
          /* Format date as "Friday, March 15th, 2024" */
          "date": $fromMillis($toMillis(clientApiCall.data.startTime), "[FNn], [MNn] [D1o], [Y]"),
          
          /* Format start time as "2:30 PM" */
          "startTime": $fromMillis($toMillis(clientApiCall.data.startTime), "[h]:[m01] [P]"),
                      
          /* Map provider and location directly */
          "doctor": clientApiCall.data.provider,
          "clinic": clientApiCall.data.location,
          
          /* Map status and patient name */
          "status": clientApiCall.data.status,
          "patientName": clientApiCall.data.patient.name
        }
        ```

        3. Sample Transformed Response:

        ```json  theme={null}
        {
          "appointmentType": "dental cleaning",
          "date": "Friday, March 15th, 2024",
          "startTime": "2:30 PM",
          "doctor": "Dr. Sarah Smith",
          "clinic": "Downtown Medical Center",
          "status": "confirmed",
          "patientName": "John Doe"
        }
        ```
      </Accordion>
    </AccordionGroup>
  </Accordion>
</AccordionGroup>

## Next Steps

Now that you've configured your API connections, GenerativeAgent can interact with your APIs just like a live agent. Here are some helpful resources for next steps:

<CardGroup>
  <Card title="Previewer" href="/generativeagent/configuring/previewer" />

  <Card title="Integrating GenerativeAgent" href="/generativeagent/integrate" />

  <Card title="Connecting Your Knowledge Base" href="/generativeagent/configuring/connecting-your-knowledge-base" />
</CardGroup>
