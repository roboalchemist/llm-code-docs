# Source: https://braintrust.dev/docs/cookbook/recipes/Lovable.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Evaluating and iterating on AI apps with Lovable

<div className="text-sm">[Contributed](https://github.com/braintrustdata/braintrust-cookbook/blob/main/examples/Lovable/Lovable.ipynb) by [Mengying Li](https://www.linkedin.com/in/mengyingli/) on 2025-12-08</div>

[Lovable](https://lovable.dev/) is a no-code platform that helps non-technical builders create real applications with AI features. After building your app with Lovable, the next step is connecting it to Braintrust so you can see what the AI is doing and iterate confidently. This cookbook guides you through adding Braintrust observability and evaluations to your Lovable app, which runs on Supabase Edge Functions with Deno.

By the end of this cookbook, you'll learn how to:

* Add Braintrust logging to a Lovable app running on Supabase Edge + Deno
* Configure the Braintrust SDK to send traces for observability
* Run evals to inspect AI behavior including prompts, tool calls, and responses
* Set up remote evals to test changes in your Lovable AI features before deploying

## Getting started

To get started, make sure you have:

* A Lovable account with an existing app
* A [Braintrust account](https://www.braintrust.dev/signup) and [API key](https://www.braintrust.dev/app/settings?subroute=api-keys)
* Access to your Lovable app's Edge Functions

## Add your API key to Lovable

From your Lovable chat interface:

1. Select the cloud icon to access secrets management
2. Add a new secret named `BRAINTRUST_API_KEY`
3. Paste your Braintrust API key as the value
4. Save the secret
   <img src="https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/secrets-2.png?fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=197b26620ed7c77d14adf0d07527a20d" alt="Secrets UI screenshot 2" data-og-width="2190" width="2190" data-og-height="1446" height="1446" data-path="cookbook/assets/Lovable/secrets-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/secrets-2.png?w=280&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=9eac392f35bc223f795885900bbb1f5f 280w, https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/secrets-2.png?w=560&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=994e334f3fa40524cbf27706727fb1a5 560w, https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/secrets-2.png?w=840&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=404787dfc5f1bd0a0de7dc00690cf971 840w, https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/secrets-2.png?w=1100&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=f4c465b890747ebba9f96dd00e81daa0 1100w, https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/secrets-2.png?w=1650&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=3b4130e3a5f3cdeb6bdd15629ac31f42 1650w, https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/secrets-2.png?w=2500&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=ee1276b5c0c695104d6b672afb5e5ea8 2500w" />

## Configure logging in your Edge Function

Ask Lovable to configure Braintrust logging by pasting this prompt into the Lovable chat:

```
Add Braintrust logging to [project name]'s Edge Function following this pattern:

1. Import the Braintrust SDK at the top of the Edge Function file.
2. Initialize the logger in the request handler using env var BRAINTRUST_API_KEY, with projectName set to your Braintrust project. Use asyncFlush: false to send logs immediately.
3. Create a root span named `request` and child spans for each major step (e.g., `ai_call`, `processing`).
   - Wrap main logic with `braintrust.traced(..., { name: "request" })`.
   - Create child spans with `rootSpan.startSpan("step_name")` and always `await span.end()` in `finally`.
   - Log input and output at each span for detailed tracing.
   - Provide a safe fallback path if the logger is unavailable.
4. Log inputs with clear fields (e.g., userPrompt, systemPrompt in metadata, not nested in messages).
5. Log outputs with both preview and full response.
6. If you later handle images, log full base64 data URLs: `data:image/[type];base64,[data]`.
7. Handle all errors and end spans in finally blocks.
8. Use or adapt this template:
import { serve } from "https://deno.land/std@0.168.0/http/server.ts";

// Import Braintrust SDK
let braintrust: any = null;
try {
  braintrust = await import("https://esm.sh/braintrust@0.4.8");
} catch (e) {
  // Braintrust not available, continue without logging
}

const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
};

serve(async (req) => {
  if (req.method === "OPTIONS") {
    return new Response(null, { headers: corsHeaders });
  }

  try {
    // Initialize logger
    const BRAINTRUST_API_KEY = Deno.env.get("BRAINTRUST_API_KEY");
    const logger = braintrust && BRAINTRUST_API_KEY
      ? braintrust.initLogger({
        projectName: "YOUR_PROJECT_NAME", // Replace with your project name
        apiKey: BRAINTRUST_API_KEY,
        asyncFlush: false,
      })
      : null;

    // Process request with or without Braintrust
    if (logger) {
      return await braintrust.traced(async (rootSpan: any) => {
        try {
          const body = await req.json();

          // Log input at root span
          await rootSpan?.log({ input: body });

          // ============================================
          // CHILD SPAN EXAMPLE
          // ============================================
          const childSpan = rootSpan.startSpan("example_step");
          let stepResult;
          try {
            // ← Add your logic here
            // Example: stepResult = await yourFunction(body);
            stepResult = body; // Placeholder - replace with your actual logic

            await childSpan?.log({
              input: body,
              output: stepResult
            });
          } finally {
            await childSpan?.end();
          }

          // Add more child spans as needed...

          // Log output at root span
          const finalResult = stepResult; // ← Replace with your actual result
          await rootSpan?.log({ output: finalResult });
          await rootSpan?.end();

          return new Response(JSON.stringify(finalResult), {
            headers: { ...corsHeaders, "Content-Type": "application/json" },
          });
        } catch (error: any) {
          await rootSpan?.log({ error: error?.message });
          await rootSpan?.end();
          throw error;
        }
      }, { name: "request" });
    } else {
      // Fallback without Braintrust
      const body = await req.json();
      // ← Add your logic here (same as above, just without spans)
      // Example: const result = await yourFunction(body);
      const result = body; // Placeholder - replace with your actual logic
      return new Response(JSON.stringify(result), {
        headers: { ...corsHeaders, "Content-Type": "application/json" },
      });
    }
  } catch (error: any) {
    return new Response(JSON.stringify({ error: error?.message }), {
      status: 500,
      headers: corsHeaders,
    });
  }
});
```

## View logs

After implementing the logging, run your AI feature end-to-end. Start with text-only if you prefer, and you can add image flows later.

<img src="https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/verify-logs-1.png?fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=7b2b9997c9406ada4fb83a3839055cce" alt="Run flow" data-og-width="2934" width="2934" data-og-height="1458" height="1458" data-path="cookbook/assets/Lovable/verify-logs-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/verify-logs-1.png?w=280&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=5148301c9c14a4670214cdddc9f24867 280w, https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/verify-logs-1.png?w=560&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=847215fe519e9c9bd3957112447fe0f4 560w, https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/verify-logs-1.png?w=840&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=697445272592b1939aa1163bc7fd0e3d 840w, https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/verify-logs-1.png?w=1100&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=46f199b1afda18bc7069b52ab595a119 1100w, https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/verify-logs-1.png?w=1650&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=c40f480c143693aa7ba283fda87f49b3 1650w, https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/verify-logs-1.png?w=2500&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=d30cdc9c02550e83492c0f1b43ee04ef 2500w" />

Navigate to your Braintrust project and select the **Logs** tab to view traces. Confirm that the traces are streaming in real time. The `ai_gateway_call` child span will show system and user prompts.

<img src="https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/verify-logs-2.png?fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=86a1829bb174fdb399a341d9ee16ac89" alt="Logs tab" data-og-width="1724" width="1724" data-og-height="1134" height="1134" data-path="cookbook/assets/Lovable/verify-logs-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/verify-logs-2.png?w=280&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=bcce799fe41864914dcb4d2fa1d3c1e9 280w, https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/verify-logs-2.png?w=560&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=7a66a58d56f87c21a21535cd5a401497 560w, https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/verify-logs-2.png?w=840&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=448dcd0f04991b5e09495d0988d73d95 840w, https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/verify-logs-2.png?w=1100&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=0ff469ec739c036202c3e6e92db2bc43 1100w, https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/verify-logs-2.png?w=1650&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=870d8e12920d0dc64b2ad9220957ae90 1650w, https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/verify-logs-2.png?w=2500&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=8d2664cc7686feb041b28b05be5e89ff 2500w" />

Each trace will include detailed information about:

* Request inputs and outputs
* AI model interactions with prompts
* Processing steps with latency
* Complete request/response payloads

## Running eval experiments

Once logging is live, you can run evals to compare prompt or agent changes and score results:

1. Create a playground directly from Logs
2. Ask Braintrust's AI assistant to add custom scorers
3. Experiment with different models and prompts
4. Compare results side-by-side

## Running remote evals

You can use remote evals to tweak prompts or tool calls locally, then test your cloud function as if it were deployed.

1. Ask Lovable for the exact Supabase Edge Function URL and substitute it below
2. Run a local dev server
3. Expose it via Cloudflare Tunnel
4. Register the tunnel URL in Braintrust

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { Eval } from "braintrust";
import { z } from "zod";

export default Eval("My Function Remote Eval", {
  task: async (input, { parameters }) => {
    const functionUrl = parameters?.functionUrl || input?.functionUrl;
    const systemPrompt =
      parameters?.systemPrompt || input?.systemPrompt || "You are a helpful assistant.";
    const userPrompt = parameters?.userPrompt || input?.userPrompt;

    if (!functionUrl) throw new Error("Missing functionUrl");

    const resp = await fetch(functionUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(input || {}),
    });

    if (!resp.ok) throw new Error(`Function error ${resp.status}: ${await resp.text()}`);

    return await resp.json();
  },

  scores: [],

  parameters: {
    functionUrl: z.string().describe("Supabase Edge Function URL").default("https://your-project.supabase.co/functions/v1/your-function"),
  },
});
```

To run the remote eval, start the dev server and tunnel:

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
npx braintrust eval my-function-eval.js --dev --dev-host 0.0.0.0 --dev-port 8400
npx cloudflared tunnel --url http://localhost:8400
```

Then, register the tunnel URL. You can do this from a playground or your project configuration.

Add the tunnel URL (for example, `https://xyz-abc-123.trycloudflare.com`):

<img src="https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/remote-eval-2.png?fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=acc461b08677c52ed05d48777ab26a7c" alt="Remote eval screenshot 2" data-og-width="2976" width="2976" data-og-height="1470" height="1470" data-path="cookbook/assets/Lovable/remote-eval-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/remote-eval-2.png?w=280&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=459f9147157ed1974097a0a404dc2a68 280w, https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/remote-eval-2.png?w=560&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=fe44cf3c5a90fef237f905f6d5e1bd3f 560w, https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/remote-eval-2.png?w=840&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=f44b2e90882520a1ad00591ddae1d8f7 840w, https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/remote-eval-2.png?w=1100&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=9af6092b7cbc6d2ac9ad0dc9db4b324c 1100w, https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/remote-eval-2.png?w=1650&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=8f5977f5748b02f95376591211d317cb 1650w, https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/remote-eval-2.png?w=2500&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=b1793a3a71829f135f712f8cde3fdd07 2500w" />

And run your remote eval:

<img src="https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/remote-eval-1.png?fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=c8a79adeca5c55c8e457575279c714a3" alt="Remote eval screenshot 2" data-og-width="2982" width="2982" data-og-height="1482" height="1482" data-path="cookbook/assets/Lovable/remote-eval-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/remote-eval-1.png?w=280&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=8ed51113c6b066bf5f7b24ec3ec9b0e4 280w, https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/remote-eval-1.png?w=560&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=fddd1d1bfa99e11588c5f4c74fec28d4 560w, https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/remote-eval-1.png?w=840&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=239c8a1282e9bfab2a06f2e287de9f4b 840w, https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/remote-eval-1.png?w=1100&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=a1554053e0e920bec2167fd9053af019 1100w, https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/remote-eval-1.png?w=1650&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=3365a5e33dadc290a0872881ce2ac33a 1650w, https://mintcdn.com/braintrust/NceB9kpAppzjNjlh/cookbook/assets/Lovable/remote-eval-1.png?w=2500&fit=max&auto=format&n=NceB9kpAppzjNjlh&q=85&s=3934f275a8240b18c2ccad527fe73157 2500w" />
Each time you'd like to run a remote eval, make sure you have the dev server running, Cloudflare Tunnel active, and Braintrust configured with the current tunnel URL.

## Troubleshooting

You can ask Lovable to help you troubleshoot in the chat window.

### Traces not showing up

* Verify secret name in Supabase matches your code
* Ensure Braintrust `projectName` is exact
* Look for "\[Braintrust]" console messages
* Ensure every span calls `await span.end()`

### Images not displaying

* Log full base64 data URLs
* Keep payloads under \~10 MB per trace
* Use format: `data:image/png;base64,...`
* Don't log booleans — include the actual data

### Errors in logs

* Verify SDK import succeeded
* Check that API key is valid
* Ensure `asyncFlush: false` is set
* Confirm outbound network access is allowed from Supabase Edge

## Next steps

Now that you have a Lovable app with full observability and evaluation capabilities, you can:

* Create [custom scorers](/evaluate/write-scorers) to evaluate AI quality against specific criteria
* Build [evaluation datasets](/annotate/datasets) from production logs to continuously improve your app
* Use the [playground](/evaluate/playgrounds) to experiment with prompts before deploying changes
* Add more AI features to your Lovable app with confidence in their quality
