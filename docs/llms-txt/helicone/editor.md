# Source: https://docs.helicone.ai/features/prompts-legacy/editor.md

# Editor

> Design, version, and manage your prompts collaboratively, then [effortlessly deploy them across your app](/features/prompts/generate).

<Warning>
  **This version of prompts is deprecated.** It will remain available for existing users until August 20th, 2025.
</Warning>

## Build and Deploy Production-Ready Prompts

The Helicone Prompt Editor enables you to:

* Design prompts collaboratively in a UI
* Create templates with variables and track real production inputs
* Connect to any major AI provider (Anthropic, OpenAI, Google, Meta, DeepSeek and more)

<Frame>
  <video width="100%" autoPlay loop muted playsInline>
    <source src="https://marketing-assets-helicone.s3.us-west-2.amazonaws.com/prompts1_2.mp4" type="video/mp4" />

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/helicone/static/features/prompts/feature1.png" alt="Prompt building interface" />
  </video>
</Frame>

## Version Control for Your Prompts

Take full control of your prompt versions:

* Track versions automatically in code or manually in UI
* Switch, promote, or rollback versions instantly
* Deploy any version using just the prompt ID

<Frame>
  <video width="100%" autoPlay loop muted playsInline>
    <source src="https://marketing-assets-helicone.s3.us-west-2.amazonaws.com/prompts2_2.mp4" type="video/mp4" />

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/helicone/static/features/prompts/feature2.png" alt="Version control interface" />
  </video>
</Frame>

## Prompt Editor Copilot

Write prompts faster and more efficiently:

* Get auto-complete and smart suggestions
* Add variables (⌘E) and XML delimiters (⌘J) with quick shortcuts
* Perform any edits you describe with natural language (⌘K)

<Frame>
  <video width="100%" autoPlay loop muted playsInline>
    <source src="https://marketing-assets-helicone.s3.us-west-2.amazonaws.com/prompts3_2.mp4" type="video/mp4" />

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/helicone/static/features/prompts/feature3.png" alt="Prompt testing interface" />
  </video>
</Frame>

## Real-Time Testing

Test and refine your prompts instantly:

* Edit and run prompts side-by-side with instant feedback
* Experiment with different models, messages, temperatures, and parameters

<Frame>
  <video width="100%" autoPlay loop muted playsInline>
    <source src="https://marketing-assets-helicone.s3.us-west-2.amazonaws.com/prompts4_2.mp4" type="video/mp4" />

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/helicone/static/features/prompts/feature4.png" alt="Prompt testing interface" />
  </video>
</Frame>

## Auto-Improve (Beta)

We're excited to launch Auto-Improve, an intelligent prompt optimization tool that helps you write more effective LLM prompts. While traditional prompt engineering requires extensive trial and error, Auto-Improve analyzes your prompts and suggests improvements instantly.

### How it Works

1. Click the Auto-Improve button in the Helicone Prompt Editor
2. Our AI analyzes each sentence of your prompt to understand:
   * The semantic interpretation
   * Your instructional intent
   * Potential areas for enhancement
3. Get a new suggested optimized version of your prompt

<Frame>
  <img src="https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/prompts/auto-improve.webp?fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=124e56b9ceb7ca006b21df6d2d61c1ee" alt="Auto-Improve feature interface" data-og-width="2588" width="2588" data-og-height="1686" height="1686" data-path="images/prompts/auto-improve.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/prompts/auto-improve.webp?w=280&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=20f0066fac9c69a47bf994e819813801 280w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/prompts/auto-improve.webp?w=560&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=60327f7b264b7f43724a802144da4842 560w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/prompts/auto-improve.webp?w=840&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=0034a510623c9f5b42c04e993e89d5be 840w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/prompts/auto-improve.webp?w=1100&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=7e1611fd2532407b4d3bd1ba99ad9437 1100w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/prompts/auto-improve.webp?w=1650&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=6dca9de15f9fd868f89b507404b92e88 1650w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/prompts/auto-improve.webp?w=2500&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=a01068eba24a8ce0de24a5aada2ca6c6 2500w" />
</Frame>

### Key Benefits

* **Semantic Analysis**: Goes beyond simple text improvements by understanding the purpose behind each instruction
* **Maintains Intent**: Preserves your original goals while enhancing how they're communicated
* **Time Saving**: Skip hours of prompt iteration and testing
* **Learning Tool**: Understand what makes an effective prompt by comparing your original with the improved version

## Using Prompts in Your Code

<Warning>
  **API Migration Notice:** We are actively working on a new Router project that
  will include an updated Generate API. While the previous [Generate API
  (legacy)](/features/prompts/generate) is still functional (see the notice on
  that page for deprecation timelines), here's a temporary way to import and use
  your UI-managed prompts directly in your code in the meantime:
</Warning>

### For OpenAI users or Azure

```tsx  theme={null}
const openai = new OpenAI({
  baseURL: "https://generate.helicone.ai/v1",
  defaultHeaders: {
    "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`,
    OPENAI_API_KEY: process.env.OPENAI_API_KEY,

    // For Azure users
    AZURE_API_KEY: process.env.AZURE_API_KEY,
    AZURE_REGION: process.env.AZURE_REGION,
    AZURE_PROJECT: process.env.AZURE_PROJECT,
    AZURE_LOCATION: process.env.AZURE_LOCATION,
  },
});

const response = await openai.chat.completions.create({
  inputs: {
    number: "world",
  },
  promptId: "helicone-test",
} as any);
```

### Using API to pull down the compiled prompt templates

##### Step 1: Get the compile the prompt template

Bash exmaple

```bash  theme={null}
curl --request POST \
  --url https://api.helicone.ai/v1/prompt/helicone-test/compile \
  --header "Content-Type: application/json" \
  --header "authorization: $HELICONE_API_KEY" \
  --data '{
  "filter": "all",
  "includeExperimentVersions": false,
  "inputs": {
    "number": "10"
  }
}'
```

Javascript example with openai

```tsx  theme={null}
const promptTemplate = await fetch(
  "https://api.helicone.ai/v1/prompt/helicone-test/compile",
  {
    method: "POST",
    headers: {
      authorization: "sk-helicone-n4vqkhi-gg6exli-teictoi-aw7azyy",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      filter: "all",
      includeExperimentVersions: false,
      inputs: { number: "10" }, // place all of your inputs here
    }),
  }
).then((res) => res.json() as any);

const example = (await openai.chat.completions.create({
  ...(promptTemplate.data.prompt_compiled as any),
  stream: false, // or true
})) as any;
```
