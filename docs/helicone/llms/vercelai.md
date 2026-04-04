# Source: https://docs.helicone.ai/getting-started/integration-method/vercelai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Vercel AI SDK Integration

> Integrate Vercel AI SDK with Helicone to monitor, debug, and improve your AI applications.

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
  modelRegistryDescription: "You can find all 100+ supported models at <a href=\"https://helicone.ai/models\" target=\"_blank\">helicone.ai/models</a>.",
  modifyBasePath: "Modify the base URL path",
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
  viewRequestsInDashboard: "View requests in the Helicone dashboard",
  viewRequestsInDashboardDescription: product => `All your ${product} requests are now visible in your <a href="https://us.helicone.ai/dashboard" target="_blank">Helicone dashboard</a>.`,
  whyUseSessions: "By including the session headers in each request, you have more granular control over session tracking. This approach is especially useful if you want to handle sessions dynamically or manage multiple sessions concurrently."
};

<Warning>
  This integration method is maintained but no longer actively developed. For the best experience and latest features, use our new [AI Gateway](/gateway/overview) with unified API access to 100+ models.
</Warning>

## {strings.howToIntegrate}

<Steps>
  <Step title={strings.generateKey}>
    <div dangerouslySetInnerHTML={{ __html: strings.generateKeyInstructions }} />
  </Step>

  <Step title={strings.setApiKey}>
    ```javascript  theme={null}
    HELICONE_API_KEY=<your-helicone-api-key>
    OPENAI_API_KEY=<your-openai-api-key>
    ```
  </Step>

  <Step title={strings.modifyBasePath}>
    <CodeGroup>
      ```javascript OpenAI theme={null}
      import { createOpenAI } from "@ai-sdk/openai";

      const openai = createOpenAI({
        baseURL: "https://oai.helicone.ai/v1",
        headers: {
          "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`,
        },
      });

      // Use openai to make API calls
      const response = streamText({
        model: openai("gpt-4o"),
        prompt: "Hello world",
      });
      ```

      ```javascript Anthropic theme={null}
      import { createAnthropic } from "@ai-sdk/anthropic";

      const anthropic = createAnthropic({
        baseURL: "https://anthropic.helicone.ai/v1",
        headers: {
          "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`,
        },
      });

      // Use openai to make API calls
      const response = streamText({
        model: anthropic("claude-3-5-sonnet-20241022"),
        prompt: "Hello world",
      });
      ```

      ```javascript Groq theme={null}
      import { createOpenAI } from "@ai-sdk/openai";
      import { generateText } from "ai";

      const groq = createOpenAI({
        baseURL: "https://groq.helicone.ai/openai/v1",
        apiKey: process.env.GROQ_API_KEY,
        headers: {
          "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`,
        },
      });

      const response = await generateText({
        model: groq("llama-3.3-70b-versatile"),
        prompt: "Hello world",
      });

      console.log(response);
      ```

      ```javascript Google Gemini theme={null}
      import { createGoogleGenerativeAI } from "@ai-sdk/google";

      const google = createGoogleGenerativeAI({
        apiKey: process.env.GOOGLE_API_KEY,
        baseURL: "https://gateway.helicone.ai/v1beta",
        headers: {
          "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`,
          "Helicone-Target-URL": "https://generativelanguage.googleapis.com",
        },
      });

      // Use Google AI to make API calls
      const response = streamText({
        model: google("gemini-1.5-pro-latest"),
        prompt: "Hello world",
      });
      ```

      ```javascript Google Vertex AI theme={null}
      import { createVertex } from "@ai-sdk/google-vertex";
      import { generateText } from "ai";

      const location = "us-central1";
      const project = process.env.GOOGLE_PROJECT_ID;

      const vertex = createVertex({
        project: project,
        location: location,
        baseURL: `https://gateway.helicone.ai/v1/projects/${project}/locations/${location}/publishers/google/`,
        // You can use any Google auth method: keyFilename, credentials object, ADC, etc.
        googleAuthOptions: {
          keyFilename: process.env.GOOGLE_APPLICATION_CREDENTIALS,
        },
        headers: {
          "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`,
          "Helicone-Target-Url": `https://${location}-aiplatform.googleapis.com`,
        },
      });

      // Use Vertex AI to make API calls
      const response = generateText({
        model: vertex("gemini-1.5-flash"),
        prompt: "Hello world",
      });
      ```

      ```javascript Google Vertex Anthropic theme={null}
      import { createVertexAnthropic } from "@ai-sdk/google-vertex/anthropic";
      import { generateText } from "ai";

      const location = "us-east5";
      const project = process.env.GOOGLE_PROJECT_ID;

      const vertexAnthropic = createVertexAnthropic({
        project: project,
        location: location,
        baseURL: `https://gateway.helicone.ai/v1/projects/${project}/locations/${location}/publishers/anthropic/models/`,
        // You can use any Google auth method: keyFilename, credentials object, ADC, etc.
        googleAuthOptions: {
          keyFilename: process.env.GOOGLE_APPLICATION_CREDENTIALS,
        },
        headers: {
          "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`,
          "Helicone-Target-Url": `https://${location}-aiplatform.googleapis.com`,
        },
      });

      // Use Vertex Anthropic to make API calls
      const response = generateText({
        model: vertexAnthropic("claude-3-5-sonnet@20240620"),
        prompt: "Hello world",
      });
      ```

      ```javascript Azure OpenAI theme={null}
      import { generateText } from "ai";
      import { createAzure } from "@ai-sdk/azure";

      const azure = createAzure({
        resourceName: process.env.AZURE_RESOURCE_NAME, // Your Azure OpenAI resource name (e.g., "your-resource")
        apiKey: process.env.AZURE_API_KEY || "",
        baseURL: "https://oai.helicone.ai/openai/deployments",
        apiVersion: process.env.AZURE_API_VERSION || "2025-01-01-preview",
        headers: {
          "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`,
          "Helicone-OpenAI-Api-Base": process.env.AZURE_API_BASE || "", // Your Azure OpenAI endpoint (e.g., https://your-resource.openai.azure.com/)
        },
      });

      const result = await generateText({
        model: azure(process.env.AZURE_DEPLOYMENT_NAME || "gpt-4o-mini"),
        prompt: "Hello world",
        maxOutputTokens: 100
      });

      console.log(result);
      ```

      ```javascript AWS Bedrock theme={null}
      // Ensure you are using version 2.0.0 or higher of @ai-sdk/amazon-bedrock
      import { createAmazonBedrock } from "@ai-sdk/amazon-bedrock";

      const bedrock = createAmazonBedrock({
        region: process.env.AWS_REGION,
        baseURL: `https://bedrock.helicone.ai/v1/${process.env.AWS_REGION}`,
        accessKeyId: process.env.AWS_ACCESS_KEY_ID,
        secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
        sessionToken: process.env.AWS_SESSION_TOKEN, // Optional: for temporary credentials
        headers: {
          "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`,
          "aws-access-key": process.env.AWS_ACCESS_KEY_ID,
          "aws-secret-key": process.env.AWS_SECRET_ACCESS_KEY,
          "aws-session-token": process.env.AWS_SESSION_TOKEN,
        },
      });

      // Use AWS Bedrock to make API calls
      const response = generateText({
        model: bedrock("anthropic.claude-v2"),
        prompt: "Hello world",
      });
      ```
    </CodeGroup>
  </Step>
</Steps>

## Configuring Helicone Features with Headers

Enable Helicone features through headers, configurable at client initialization or individual request level.

### Configure Client

```javascript {3-6} theme={null}
const openai = createOpenAI({
  baseURL: "https://oai.helicone.ai/v1",
  headers: {
    "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`,
    "Helicone-Cache-Enabled": "true",
  },
});
```

### Generate Text

```javascript {4-9} theme={null}
const response = generateText({
  model: openai("gpt-4o"),
  prompt: "Hello world",
  headers: {
    "Helicone-User-Id": "john@doe.com",
    "Helicone-Session-Id": "uuid",
    "Helicone-Session-Path": "/chat",
    "Helicone-Session-Name": "Chatbot",
  },
});
```

### Stream Text

```javascript {4-9} theme={null}
const response = streamText({
  model: openai("gpt-4o"),
  prompt: "Hello world",
  headers: {
    "Helicone-User-Id": "john@doe.com",
    "Helicone-Session-Id": "uuid",
    "Helicone-Session-Path": "/chat",
    "Helicone-Session-Name": "Chatbot",
  },
});
```

## Using with Existing Custom Base URLs

If you're already using a custom base URL for an OpenAI-compatible vendor, you can proxy your requests through Helicone by setting the `Helicone-Target-URL` header to your existing vendor's endpoint.

### Example with Custom Vendor

```javascript  theme={null}
import { createOpenAI } from "@ai-sdk/openai";

const openai = createOpenAI({
  baseURL: "https://oai.helicone.ai/v1",
  headers: {
    "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`,
    "Helicone-Target-URL": "https://your-vendor-api.com/v1", // Your existing vendor's endpoint
  },
});

// Use openai to make API calls - requests will be proxied to your vendor
const response = streamText({
  model: openai("gpt-4o"),
  prompt: "Hello world",
});
```

### Example with Multiple Vendors

You can also dynamically set the target URL per request:

```javascript  theme={null}
const response = streamText({
  model: openai("gpt-4o"),
  prompt: "Hello world",
  headers: {
    "Helicone-Target-URL": "https://your-vendor-api.com/v1", // Override for this request
  },
});
```

This approach allows you to:

* Keep your existing vendor integrations
* Add Helicone monitoring and features
* Switch between vendors without changing your base URL
* Maintain compatibility with your current setup
