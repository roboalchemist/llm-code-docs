# Source: https://docs.helicone.ai/integrations/vectordb/logger-sdk.md

# Source: https://docs.helicone.ai/integrations/tools/logger-sdk.md

# Source: https://docs.helicone.ai/integrations/data/logger-sdk.md

# Source: https://docs.helicone.ai/integrations/vectordb/logger-sdk.md

# Source: https://docs.helicone.ai/integrations/tools/logger-sdk.md

# Source: https://docs.helicone.ai/integrations/data/logger-sdk.md

# Source: https://docs.helicone.ai/integrations/vectordb/logger-sdk.md

# Source: https://docs.helicone.ai/integrations/tools/logger-sdk.md

# Source: https://docs.helicone.ai/integrations/data/logger-sdk.md

# Source: https://docs.helicone.ai/integrations/vectordb/logger-sdk.md

# Source: https://docs.helicone.ai/integrations/tools/logger-sdk.md

# Source: https://docs.helicone.ai/integrations/data/logger-sdk.md

# Custom Logs with the Logger SDK

> Log any custom operations using Helicone's Logger SDK for complete observability across your application stack.

export const strings = {
  additionalHeadersForSessions: "Helicone provides additional headers to help you manage and analyze your sessions.",
  azureOpenAIDocs: `To learn more about the differences between OpenAI and AzureOpenAI, review the <a href="https://learn.microsoft.com/en-us/azure/ai-services/openai/overview">documentation here</a>.`,
  chainOfThoughtPromptingCookbookDescription: "Craft effective prompts, ideal for complex responses requiring multi-step problem solving.",
  chatbotCookbookDescription: "This step-by-step guide covers function calling, response formatting and monitoring with Helicone.",
  createHeliconeManualLogger: "Create a new HeliconeManualLogger instance",
  configureWebSocketConnection: "Configure WebSocket connection",
  environmentTrackingCookbookDescription: "Effortlessly track and manage your environments with Helicone across different deployment contexts.",
  exportBaseUrl: tool => `Export your ${tool} base URL`,
  getStartedWithPackage: "To get started, install the @helicone/helpers package",
  generateKey: "Create an account and generate an API key",
  generateKeyInstructions: `Log into <a href="https://www.helicone.ai" target="_blank">Helicone</a> or create an account. Once you have an account, you can generate an <a href="https://helicone.ai/developer" target="_blank">API key here</a>.`,
  generateSessionId: "Generate the unique session ID that will be used to track the session.",
  gettingUserRequestsCookbookDescription: "Retrieve user-specific requests to monitor, debug, and track costs for individual users.",
  githubActionsCookbookDescription: "Automate the monitoring and caching of your LLM calls in your CI pipelines for better deployment processes.",
  groupingCallsWithSessions: "Grouping Calls with Helicone Sessions",
  handleWebSocketEvents: "Handle WebSocket events",
  heliconeLoggerAPIReference: `To learn more about the <code>HeliconeManualLogger</code> API, see the <a href="/getting-started/integration-method/custom" target="_blank">API Reference here</a>.`,
  howToIntegrate: "How to Integrate",
  howToPromptThinkingModelsCookbookDescription: "Best practices to to effectively prompt thinking models like Deepseek and OpenAI o1-o3 for optimal results.",
  howToUseSessions: "To group related API calls and analyze them collectively, you can use Helicone's session tracking features. This is useful for grouping all interactions within a single conversation or user session.",
  includeHeadersInRequests: "Include headers in your requests",
  includeSessionHeaders: "Include the session headers when you make API requests. This way, the session information is attached to each request, allowing Helicone to group and analyze them together.",
  installRequiredDependencies: "Install required dependencies",
  installSDK: tool => `Install ${tool}`,
  logYourRequest: "Log your request",
  modifyBasePath: "Modify the base URL path and set up authentication",
  optional: "Optional",
  relatedGuides: "Related Guides",
  replayLlmSessionsCookbookDescription: "Learn how to replay and modify LLM sessions using Helicone to optimize your AI agents and improve their performance.",
  sessionManagement: "Session Management",
  setApiKey: "Set up your Helicone API key in your .env file",
  setUpToolBaseUrl: tool => `Set up your ${tool} base URL`,
  setUpToolApiKey: tool => `Set up your ${tool} API key as an environment variable`,
  startUsing: tool => `Start using ${tool} with Helicone`,
  useTheSDK: tool => `Use the ${tool} SDK`,
  verifyInHelicone: "Verify your requests in Helicone",
  verifyInHeliconeDesciption: tool => `With the above setup, any calls to ${tool} will automatically be logged and monitored by Helicone. Review them in your <a href="https://www.helicone.ai/dashboard" target="_blank">Helicone dashboard</a>.`,
  whyUseSessions: "By including the session headers in each request, you have more granular control over session tracking. This approach is especially useful if you want to handle sessions dynamically or manage multiple sessions concurrently.",
  viewRequestsInDashboard: "View requests in the Helicone dashboard",
  viewRequestsInDashboardDescription: product => `All your ${product} requests are now visible in your <a href="https://us.helicone.ai/dashboard" target="_blank">Helicone dashboard</a>`,
  modelRegistryDescription: "You can find all 100+ supported models at <a href=\"https://helicone.ai/models\" target=\"_blank\">helicone.ai/models</a>."
};

The Logger SDK allows you to log any custom operation to Helicone - database queries, API calls, ML inference, file processing, or any other operation you want to track.

<Steps>
  <Step title={strings.getStartedWithPackage}>
    <CodeGroup>
      ```bash npm theme={null}
      npm install @helicone/helpers
      ```

      ```bash pip theme={null}
      pip install helicone-helpers
      ```
    </CodeGroup>
  </Step>

  <Step title={strings.setApiKey}>
    <div dangerouslySetInnerHTML={{ __html: strings.generateKeyInstructions }} />

    ```bash  theme={null}
    export HELICONE_API_KEY=<your-helicone-api-key>
    ```
  </Step>

  <Step title={strings.createHeliconeManualLogger}>
    <CodeGroup>
      ```js js theme={null}
      import { HeliconeManualLogger } from "@helicone/helpers";

      const heliconeLogger = new HeliconeManualLogger({
        apiKey: process.env.HELICONE_API_KEY,
        headers: {} // Additional headers sent with the request (optional)
      });
      ```

      ```python python theme={null}
      from helicone_helpers import HeliconeManualLogger

      helicone_logger = HeliconeManualLogger(
        api_key=os.getenv("HELICONE_API_KEY"),
        headers={} # Additional headers sent with the request (optional)
      )
      ```
    </CodeGroup>
  </Step>

  <Step title={strings.logYourRequest}>
    The `logRequest` method takes three parameters:

    1. **Request data**: What you're logging (query, operation name, etc.)
    2. **Operation function**: The actual work being done
    3. **Headers**: Optional custom properties or session tracking

    <CodeGroup>
      ```js js theme={null}
      const result = await heliconeLogger.logRequest(
        // 1. What you're logging
        {
          _type: "data",
          name: "user_query",
          query: "SELECT * FROM users WHERE active = true",
          database: "production"
        },
        // 2. The actual operation
        async (resultRecorder) => {
          const queryResult = await database.query(
            "SELECT * FROM users WHERE active = true"
          );

          // Record the results
          resultRecorder.appendResults({
            _type: "data",
            name: "user_query",
            status: "success",
            data: queryResult.rows,
            count: queryResult.rows.length
          });

          return queryResult;
        },
        // 3. Optional: session tracking or custom properties
        {
          "Helicone-Property-Session": "user-123",
          "Helicone-Property-Environment": "production"
        }
      );
      ```

      ```python python theme={null}
      def database_operation(result_recorder):
        # The actual operation
        query_result = database.execute(
          "SELECT * FROM users WHERE active = true"
        )

        # Record the results
        result_recorder.append_results({
          "_type": "data",
          "name": "user_query",
          "status": "success",
          "data": query_result.fetchall(),
          "count": len(query_result.fetchall())
        })
        return query_result

      result = helicone_logger.log_request(
        # 1. What you're logging
        request={
          "_type": "data",
          "name": "user_query",
          "query": "SELECT * FROM users WHERE active = true",
          "database": "production"
        },
        # 2. The actual operation
        operation=database_operation,
        # 3. Optional: session tracking or custom properties
        additional_headers={
          "Helicone-Property-Session": "user-123",
          "Helicone-Property-Environment": "production"
        }
      )
      ```
    </CodeGroup>
  </Step>

  <Step title={strings.verifyInHelicone}>
    <div dangerouslySetInnerHTML={{ __html: strings.verifyInHeliconeDesciption("any data operation") }} />
  </Step>
</Steps>

## Understanding the Structure

All custom logs follow the same pattern with two parts:

### Request Data

What you're about to do. Must include:

* `_type: "data"` - Identifies this as a custom data log
* `name` - A descriptive name for your operation
* Any custom fields you want to track (query, endpoint, model, etc.)

### Response Data

What happened. Should include:

* `_type: "data"` - Identifies this as a custom data response
* `name` - Same name as the request
* `status` - Success or error state
* Any result data you want to track

## More Examples

### API Call

<CodeGroup>
  ```js js theme={null}
  await heliconeLogger.logRequest(
    {
      _type: "data",
      name: "external_api_call",
      endpoint: "https://api.example.com/users",
      method: "GET"
    },
    async (resultRecorder) => {
      const response = await fetch("https://api.example.com/users?limit=10");
      const data = await response.json();

      resultRecorder.appendResults({
        _type: "data",
        name: "external_api_call",
        status: "success",
        result: data
      });

      return data;
    }
  );
  ```

  ```python python theme={null}
  def api_call_operation(result_recorder):
    response = requests.get("https://api.example.com/users", params={"limit": 10})
    data = response.json()

    result_recorder.append_results({
      "_type": "data",
      "name": "external_api_call",
      "status": "success",
      "result": data
    })
    return data

  api_result = helicone_logger.log_request(
    request={
      "_type": "data",
      "name": "external_api_call",
      "endpoint": "https://api.example.com/users",
      "method": "GET"
    },
    operation=api_call_operation
  )
  ```
</CodeGroup>

### ML Model Inference

<CodeGroup>
  ```js js theme={null}
  await heliconeLogger.logRequest(
    {
      _type: "data",
      name: "ml_inference",
      model: "custom-classifier-v2",
      input_features: { text: "This is a sample text" }
    },
    async (resultRecorder) => {
      const prediction = await customModel.predict({
        text: "This is a sample text",
        threshold: 0.8
      });

      resultRecorder.appendResults({
        _type: "data",
        name: "ml_inference",
        status: "success",
        result: {
          classification: prediction.classification,
          confidence: prediction.confidence
        }
      });

      return prediction;
    }
  );
  ```

  ```python python theme={null}
  def ml_inference_operation(result_recorder):
    prediction = custom_model.predict({
      "text": "This is a sample text",
      "threshold": 0.8
    })

    result_recorder.append_results({
      "_type": "data",
      "name": "ml_inference",
      "status": "success",
      "result": {
        "classification": prediction["classification"],
        "confidence": prediction["confidence"]
      }
    })
    return prediction

  prediction = helicone_logger.log_request(
    request={
      "_type": "data",
      "name": "ml_inference",
      "model": "custom-classifier-v2",
      "input_features": {"text": "This is a sample text"}
    },
    operation=ml_inference_operation
  )
  ```
</CodeGroup>

For more examples, check out our [GitHub examples](https://github.com/Helicone/helicone/tree/main/examples/data).

<div dangerouslySetInnerHTML={{ __html: strings.heliconeLoggerAPIReference }} />

## Related Guides

* [How to use Helicone Sessions](/guides/sessions)
* [How to use Helicone Custom Properties](/guides/custom-properties)
