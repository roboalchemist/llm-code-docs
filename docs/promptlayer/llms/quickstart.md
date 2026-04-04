# Source: https://docs.promptlayer.com/quickstart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.promptlayer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart

PromptLayer is your workbench for AI engineering. Version, test, and monitor every prompt and agent with robust evals and tracing. Empower domain experts to iterate alongside engineers in the visual editor.

This tutorial walks you through building an AI application that generates cake recipes. By the end, you'll know how to:

* Create and run prompts in the visual editor
* Track versions with diffs and commit messages
* Switch between LLMs (OpenAI, Anthropic, etc.)
* Deploy to production with release labels
* View logs and debug issues

<Info>
  [Create an account](https://dashboard.promptlayer.com/create-account) to
  follow along.
</Info>

## Creating Your First Prompt

Prompts are the core IP of any AI application. By managing them in PromptLayer instead of hardcoding them, you can edit prompts without deploying code, track every change, and test new versions safely.

From the PromptLayer dashboard, click **New** → **Prompt**.

<Frame>
  <img src="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-creation-access.png?fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=34382dd2de9bd6798c863d02f02e7c37" alt="Creating a new prompt" data-og-width="2880" width="2880" data-og-height="1624" height="1624" data-path="new-quickstart-images/prompt-creation-access.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-creation-access.png?w=280&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=ccfe810f8ebc1f93d512937615607c48 280w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-creation-access.png?w=560&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=e02f9daf6f55431f5a0b1811247a0d5a 560w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-creation-access.png?w=840&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=41142f291dd043683a18d38b3e570f5b 840w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-creation-access.png?w=1100&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=3ef3bc210db3eb24f4e6de657846175f 1100w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-creation-access.png?w=1650&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=c9c087193f006b3bf21c018847603809 1650w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-creation-access.png?w=2500&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=bf1c63681fd838bbc7be453a69d82637 2500w" />
</Frame>

A prompt starts with two messages. The **System** message sets the AI's behavior. The **User** message is what gets sent each time you run it.

<Accordion title="System and User Messages">
  **System message**: Defines the AI's persona, tone, and rules. Think of it as the "instruction manual" that stays constant across all runs. Use it for things like:

  * Setting a persona ("You are a helpful assistant...")
  * Defining output format ("Always respond in JSON...")
  * Establishing guardrails ("Never discuss competitors...")

  **User message**: The input that changes each time the prompt runs. This is where you put the actual request and any input variables. In production, your code will dynamically fill in this message.

  Some prompts also use **Assistant** messages to show example responses, which helps the AI understand the expected format.

  Learn more about [LLM idioms](https://blog.promptlayer.com/llm-idioms/) and why chat formats matter.
</Accordion>

Replace the default content with:

```markdown System theme={null}
You are a Michelin-star pastry chef. Generate cake recipes with:

**Overview**: One paragraph about the cake
**Ingredients**: Bullet points with metric and US measurements  
**Instructions**: Numbered steps with temperatures and timing
**Variations**: Optional frostings or substitutions
```

```markdown User theme={null}
Create a recipe for {{cake_type}} that serves {{serving_size}} people.
```

Notice `{{cake_type}}` and `{{serving_size}}`. These are [input variables](/features/prompt-registry/template-variables)—think of them like mad-libs. When you run the prompt, you'll fill these in with real values.

<Frame>
  <img src="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/variables-explained.png?fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=3b2d6c2203652e7937090e8d9abfcc1a" alt="Input variables in prompt" data-og-width="5760" width="5760" data-og-height="3240" height="3240" data-path="new-quickstart-images/variables-explained.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/variables-explained.png?w=280&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=32f90dd171afae8a1c0cc98b73bf70c3 280w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/variables-explained.png?w=560&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=1b37ea43fd49aa83574af47f4437c884 560w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/variables-explained.png?w=840&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=f4229c335784af573cd9ad3c6357d28a 840w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/variables-explained.png?w=1100&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=6fc536f4ded7261711b10afdef4abced 1100w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/variables-explained.png?w=1650&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=da300421ed5675e9c63faa64850d1041 1650w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/variables-explained.png?w=2500&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=61558999f15365a990c53eb453b34c86 2500w" />
</Frame>

### Running Your Prompt

To test your prompt:

1. Click **Define input variables** in the right panel
2. Set `cake_type` to "Chocolate Cake" and `serving_size` to "8"
3. Click **Run**

<Frame>
  <img src="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/running-in-playground.gif?s=ed164d69a23135b28ff76f7bd8f425ea" alt="Running a prompt in the playground" data-og-width="800" width="800" data-og-height="453" height="453" data-path="new-quickstart-images/running-in-playground.gif" data-optimize="true" data-opv="3" />
</Frame>

Save your prompt by clicking **Save Template**.

<Accordion title="Retrieving Prompts in Your Code">
  Your application fetches prompts from PromptLayer at runtime using the SDK or REST API. This keeps prompts out of your codebase and lets you update them without redeploying. It also means PMs and domain experts can edit prompts directly in the dashboard without waiting for engineering.

  ```python  theme={null}
  from promptlayer import PromptLayer
  client = PromptLayer()

  # Fetch and run a prompt by name
  response = client.run(
      prompt_name="cake-recipe",
      input_variables={"cake_type": "Chocolate", "serving_size": "8"}
  )
  ```

  See [Deployment Strategies](/onboarding-guides/deployment-strategies) for caching strategies.
</Accordion>

## Versioning Your Prompt

PromptLayer tracks every change you make to a prompt. Each save creates a new version with a record of what changed, when, and by whom.

<Accordion title="Prompt Writing Tips">
  * Use headers to structure your prompt (`**Section**:`) - Be specific about
    output format - Include examples when possible PromptLayer supports [Jinja2
    templates](/features/prompt-registry/template-variables#jinja2-templates) for
    more advanced variable logic. For structured outputs, see our guide on [tool
    calling with
    LLMs](https://blog.promptlayer.com/tool-calling-with-llms-how-and-when-to-use-it/).
</Accordion>

### Editing Prompts

To edit a prompt, open it in the editor and make your changes. You can edit any message, add new messages, or change model settings.

Let's try it. Add this line to the end of your System message:

```
Always include a "Baker's Tip" at the end with advice for beginners.
```

Click **Save Template**. Before saving, PromptLayer shows you a diff of exactly what changed: deletions in red, additions in green. Add a commit message like "Added baker's tip requirement" and save.

<Frame>
  <img src="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/bakers-tip.png?fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=3834b0e2794b8d8d3de9ca3a8b01dff4" alt="Saving with diff view" data-og-width="2204" width="2204" data-og-height="1318" height="1318" data-path="new-quickstart-images/bakers-tip.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/bakers-tip.png?w=280&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=ec3ebb7c0d34464ef0ec394e10231a3b 280w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/bakers-tip.png?w=560&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=f14d73fb977cd5fe7f5c06ab7f360d05 560w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/bakers-tip.png?w=840&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=d9e5917e8052f968f28977a52b9f7171 840w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/bakers-tip.png?w=1100&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=c115120f6340dbdc7629206690cb40b3 1100w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/bakers-tip.png?w=1650&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=454b4c699a846c2812c0c970a4cdd047 1650w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/bakers-tip.png?w=2500&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=7132be5024892b2f95022dd75328ee07 2500w" />
</Frame>

Your version history appears in the left panel. You can click any previous version to view it.

<Frame>
  <img src="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-versioning-display.png?fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=28c0e42cbc79f3fc7b2d860d17158384" alt="Version history" data-og-width="2880" width="2880" data-og-height="1624" height="1624" data-path="new-quickstart-images/prompt-versioning-display.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-versioning-display.png?w=280&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=4544a0acf27cb6ed46d01d4cf00b1f79 280w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-versioning-display.png?w=560&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=9b15bced336934a7e86e8a7864f7c44a 560w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-versioning-display.png?w=840&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=14711c3ce32d2409639a53a3b7c8c9d5 840w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-versioning-display.png?w=1100&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=9505088d7f740ccaa6bedc30d7c7449c 1100w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-versioning-display.png?w=1650&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=4259c49bb7d454911bdaa990f5e6630a 1650w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-versioning-display.png?w=2500&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=9b25a2f6a1d3811a703270f99c7e87f4 2500w" />
</Frame>

Hover over a version and click **View Diff** to compare any two versions side by side.

<Frame>
  <img src="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-diffing-display.png?fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=b55cc082d4255b5245e2aa24cde74f58" alt="Comparing versions with diff" data-og-width="2880" width="2880" data-og-height="1624" height="1624" data-path="new-quickstart-images/prompt-diffing-display.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-diffing-display.png?w=280&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=e9c0b5fbb8dda1c0f9f11a2e54cc6be4 280w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-diffing-display.png?w=560&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=af138141925b48418de60a82a400864c 560w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-diffing-display.png?w=840&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=76d88b68c3ee779d353e89464a34c7ee 840w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-diffing-display.png?w=1100&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=b197c3e5fd12b4bdb25ba7fd8b37fce2 1100w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-diffing-display.png?w=1650&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=6ed71e236ddaef80fac201e5607224cb 1650w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-diffing-display.png?w=2500&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=7489d3b6dda969791469f5163ad9504b 2500w" />
</Frame>

### Writing Prompts with AI

Click the magic wand icon to open the AI prompt writer. It can help rewrite or improve your prompts based on your instructions. Try asking it to "add allergy warnings" to the recipe generator.

<Frame>
  <img src="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/ai-prompt-writer-zoomed.png?fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=c064bd7d0af96a73a21845d129cd10a9" alt="AI prompt writer" data-og-width="1430" width="1430" data-og-height="1004" height="1004" data-path="new-quickstart-images/ai-prompt-writer-zoomed.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/ai-prompt-writer-zoomed.png?w=280&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=f4b36aa54ab71e640bff4347bad97dad 280w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/ai-prompt-writer-zoomed.png?w=560&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=010f8e6b15896925508faa960682267c 560w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/ai-prompt-writer-zoomed.png?w=840&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=e4a2f9196534875d16cef2f62b72d6fc 840w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/ai-prompt-writer-zoomed.png?w=1100&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=20d4af959c447720aba6b6a354830e66 1100w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/ai-prompt-writer-zoomed.png?w=1650&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=26e51640abf88284b079194a60b074ec 1650w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/ai-prompt-writer-zoomed.png?w=2500&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=7e19d3fd622ee4d01bd42faa641ab204 2500w" />
</Frame>

### Switching LLMs

PromptLayer is model-agnostic. You can switch between OpenAI, Anthropic, Google, and [other providers](/features/supported-providers) without changing your prompt. Click the model name at the bottom of the editor to switch.

<Frame>
  <img src="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/switching-llms.gif?s=6e61d7126230feb3eb8e72b496772c7c" alt="Switching models" data-og-width="800" width="800" data-og-height="788" height="788" data-path="new-quickstart-images/switching-llms.gif" data-optimize="true" data-opv="3" />
</Frame>

All prompts work across models, including [function calling and tool use](/features/prompt-registry/tool-calling). You can also connect [private models or custom hosts](/features/custom-providers), and build [fine-tuned models](/why-promptlayer/fine-tuning).

<Note>
  Any model with a `base_url` can be added as a [custom
  provider](/features/custom-providers) - including self-hosted models, Azure
  OpenAI, or any OpenAI-compatible API.
</Note>

## Deploying to Prod

Once your prompt is ready, PromptLayer can manage which version goes live. Release labels let you control which version is in production, so you can update prompts without touching code.

For engineers: PromptLayer offers several [deployment strategies](/onboarding-guides/deployment-strategies) including our Python or TypeScript SDKs, webhook-driven caching, fully managed agents, or [self-hosted](/self-hosted) deployments.

### Release Labels

Release labels control which prompt version is live. You can mark versions as "production", "staging", or "testing". Your code fetches the prompt by label, so you can update the live version without changing any code.

<Frame>
  <img src="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/release-labels-close.png?fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=561a862b177c66757b0a9237aeee82cf" alt="Release labels" data-og-width="1002" width="1002" data-og-height="570" height="570" data-path="new-quickstart-images/release-labels-close.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/release-labels-close.png?w=280&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=5e0cfcc5a82e3586555058f813eac35e 280w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/release-labels-close.png?w=560&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=c2224c191e02220087562723a6f854db 560w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/release-labels-close.png?w=840&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=8b2666169840e53e946b91db825c182d 840w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/release-labels-close.png?w=1100&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=838766429e86eccee413d31186d0102a 1100w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/release-labels-close.png?w=1650&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=bc4d3035f57710c9e4d0b2a855219ace 1650w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/release-labels-close.png?w=2500&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=dcee2521da94e1b83ad65cdaa84eaef4 2500w" />
</Frame>

Learn more about [release labels](/features/prompt-registry/release-labels).

### A/B Testing

PromptLayer supports A/B testing prompts in production. Common use cases include:

* Testing a new prompt version on 10% of traffic before full rollout
* Segmenting beta users to receive an experimental prompt based on user metadata

To start an A/B test, assign release labels to different prompt versions and configure traffic splits in the dashboard.

<Frame>
  <img src="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-ab-test-display.png?fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=64f5451d2c9271af619a27dc9dd006d6" alt="A/B testing prompts" data-og-width="1758" width="1758" data-og-height="1238" height="1238" data-path="new-quickstart-images/prompt-ab-test-display.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-ab-test-display.png?w=280&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=183038e2ccaaae93ed2686b23463fde7 280w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-ab-test-display.png?w=560&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=09e1464e642ad2a2b9c1afe575606430 560w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-ab-test-display.png?w=840&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=7f9a7bb156b694caff3e65af235c839e 840w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-ab-test-display.png?w=1100&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=4e05e3e0fb667c792c3b4eb17766006d 1100w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-ab-test-display.png?w=1650&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=1c813a0f15eae3f22bc46f0c3aa8edce 1650w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/prompt-ab-test-display.png?w=2500&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=c85329447c32c0ae415b71b10943a683 2500w" />
</Frame>

Learn more about [A/B testing](/why-promptlayer/ab-releases).

## Building Agents

Agents are multi-step AI workflows. Unlike a single prompt, an agent can chain multiple prompts together, use tools, and make decisions based on intermediate results.

For example, you could extend the cake recipe generator into an agent that:

1. Generates the recipe (using our prompt from earlier)
2. Scales the ingredients for 100 people
3. Calculates the total cost based on current grocery prices

Create an agent by clicking **New** → **Agent**. You can build workflows visually using a drag-and-drop editor. Connect prompts, add conditionals, and loop over data. No code required.

<Frame>
  <img src="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/recipe-agent.png?fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=e562cb9416fe707ab02c6cbfa98cf103" alt="Creating an agent" data-og-width="2616" width="2616" data-og-height="1437" height="1437" data-path="new-quickstart-images/recipe-agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/recipe-agent.png?w=280&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=213f8437a07330242153f3529c52e2e3 280w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/recipe-agent.png?w=560&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=81f316f1efce1213adcfb96c88581494 560w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/recipe-agent.png?w=840&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=b68c619c08acdd20df4fee3f001f880b 840w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/recipe-agent.png?w=1100&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=eecc16accd18614e96f5f13fd6dc2f6e 1100w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/recipe-agent.png?w=1650&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=2cbc5087830f2600a49256e1e2be0940 1650w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/recipe-agent.png?w=2500&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=590cd5248772dd2f3d60d494cc64e1b6 2500w" />
</Frame>

Like prompts, agents are versioned with commit messages and can be retrieved via the SDK.

<Frame>
  <img src="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/agent-version-list.png?fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=5430ddaedf3a493a19332e843980ded0" alt="Agent version history" data-og-width="2130" width="2130" data-og-height="1262" height="1262" data-path="new-quickstart-images/agent-version-list.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/agent-version-list.png?w=280&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=9633fb96603ea8fc2ebb3552e32452ab 280w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/agent-version-list.png?w=560&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=9ff1682bcbdc3ce7cdad92b6c05df50b 560w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/agent-version-list.png?w=840&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=435c23d5669afca083d0b364989b909c 840w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/agent-version-list.png?w=1100&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=f63dddfc35e419f745c3ef12cc55d022 1100w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/agent-version-list.png?w=1650&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=2a92e4d6646688c11a1f3e48338f48fc 1650w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/agent-version-list.png?w=2500&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=4d94c2762bc93c65a912b0e30c22e837 2500w" />
</Frame>

Learn more about [Agents](/why-promptlayer/agents).

## Evaluations

Evals test how well your prompts perform. Common use cases include:

* **LLM-as-judge**: Use AI to score outputs against criteria like tone, accuracy, or formatting
* **Historical backtests**: Compare a new prompt version against real production data
* **Model comparisons**: Test the same prompt across GPT-4, Claude, Gemini, etc.
* **Regression testing**: Automatically run evals when a prompt is updated to catch edge cases
* **Human grading**: Collect feedback from domain experts on prompt quality

<Frame>
  <img src="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/eval-example.png?fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=63490eddfbb69f0aa8ef8bb0a1bca9dd" alt="Evaluation pipeline" data-og-width="2520" width="2520" data-og-height="1174" height="1174" data-path="new-quickstart-images/eval-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/eval-example.png?w=280&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=2ae8a5d09cb313e77ea7adaf9cc47d38 280w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/eval-example.png?w=560&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=fc8ae0e36cd3d64ce95173dc47477652 560w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/eval-example.png?w=840&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=0daef327b5398e578301fd07240dc5e1 840w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/eval-example.png?w=1100&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=ff19d750178ed3cd1edd8156f8f3fe2d 1100w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/eval-example.png?w=1650&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=5e385a69dcb54061877562d06ca58787 1650w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/eval-example.png?w=2500&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=9f11ec664f327fffab7ddace1dd94169 2500w" />
</Frame>

You can build evaluation pipelines visually and connect them to prompts for continuous testing. Learn more about [Evaluations](/features/evaluations/overview).

## Logs and Analytics

Every prompt run is logged with full request and response details. You can attach [metadata](/features/prompt-history/metadata) like user IDs, session IDs, or feature flags to each request, making it easy to debug issues for specific users. [Analytics](/why-promptlayer/analytics) show cost, latency, and usage patterns across your prompts.

<Frame>
  <img src="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/analytics-display.png?fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=0c01273ef5f59de773cf30e9097371a9" alt="Analytics dashboard" data-og-width="2650" width="2650" data-og-height="1482" height="1482" data-path="new-quickstart-images/analytics-display.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/analytics-display.png?w=280&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=0c071d3b5328efe0ebf11dce387de7f0 280w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/analytics-display.png?w=560&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=a1c36772270b10cf2b39ab56e07e0ab9 560w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/analytics-display.png?w=840&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=a8446ba78c15f9434c7c3d83508d8756 840w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/analytics-display.png?w=1100&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=37246ee75fd9bbeee55003558b8c98ac 1100w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/analytics-display.png?w=1650&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=574525411c51aa9261f8577b60e4a285 1650w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/analytics-display.png?w=2500&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=2d269833e47847038c4f5fcd76a7eb20 2500w" />
</Frame>

### Viewing Logs

Click **Logs** in the sidebar to see all requests. You can filter by prompt, [search by content](/why-promptlayer/advanced-search), and debug errors.

<Frame>
  <img src="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/logs-table.png?fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=d95a9fdb55dae6bc3bd7a83016f38ca1" alt="Request logs" data-og-width="1808" width="1808" data-og-height="1052" height="1052" data-path="new-quickstart-images/logs-table.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/logs-table.png?w=280&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=a469d654bd1027f084af76b6efc97563 280w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/logs-table.png?w=560&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=67899f70670e5e791c3b46cbdea69882 560w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/logs-table.png?w=840&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=856ccae1d10d0d47e47ee93cdb30f1db 840w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/logs-table.png?w=1100&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=abef44a6a6b0f779d564115479d19acc 1100w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/logs-table.png?w=1650&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=7582107aa0016f76047e8a853f679863 1650w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/logs-table.png?w=2500&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=6f382c79c86e48009a5198e8b812094a 2500w" />
</Frame>

You can also view logs for a specific prompt by clicking **Analytics & Logs** in the prompt editor.

<Frame>
  <img src="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/logs-by-prompt-display.png?fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=1a3670ead4a4aa2177e524f1bcf458d0" alt="Logs filtered by prompt" data-og-width="2880" width="2880" data-og-height="1556" height="1556" data-path="new-quickstart-images/logs-by-prompt-display.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/logs-by-prompt-display.png?w=280&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=421a6a8dcc1bbe8408c17960e4c64e41 280w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/logs-by-prompt-display.png?w=560&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=bb932cd1da3b53412ff654ec7d14f1b3 560w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/logs-by-prompt-display.png?w=840&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=31229304e7355465c0d7f1a89f2d176f 840w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/logs-by-prompt-display.png?w=1100&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=4662fa31bf1c9680412e6efec6602633 1100w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/logs-by-prompt-display.png?w=1650&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=c8f87340635eec377a726a262c429453 1650w, https://mintcdn.com/promptlayer/Uwb3ZGD7ch34XkjE/new-quickstart-images/logs-by-prompt-display.png?w=2500&fit=max&auto=format&n=Uwb3ZGD7ch34XkjE&q=85&s=edb3ccfea208f805dda2ca98009f2f7c 2500w" />
</Frame>

From the logs table, you can select historical requests and click **Backtest** to run a new prompt version against those inputs and compare results.

### Traces and Spans

For agents, [traces](/running-requests/traces) show each step of the workflow as spans. You can see timing, inputs, and outputs for every step. Traces are OpenTelemetry (OTEL) compatible, so you can integrate with your existing observability stack.

<Frame>
  <img src="https://mintcdn.com/promptlayer/Uqlih28KZOpPNhLj/images/new_traces.gif?s=19696dd0eeaa7a137dde6857a8d7bc71" alt="Trace visualization" data-og-width="800" width="800" data-og-height="542" height="542" data-path="images/new_traces.gif" data-optimize="true" data-opv="3" />
</Frame>

<Tip>
  Continue to [Quickstart Part 2](/quickstart-part-two) to learn about
  evaluations, backtests, and connecting PromptLayer to your code.
</Tip>

You can also watch our [Tutorial Videos](/tutorial-videos) for guided walkthroughs.

### Prompt Management

* [Scalable Prompt Management and Collaboration](https://blog.promptlayer.com/scalable-prompt-management-and-collaboration/) — Best practices for organizing and collaborating on prompts
* [Prompt Management](/why-promptlayer/prompt-management) — Why prompt management matters

### Evaluations

* [Eval Examples](/features/evaluations/examples) — Building RAG chatbots and migrating prompts
* [How to Evaluate LLM Prompts Beyond Simple Use Cases](https://blog.promptlayer.com/how-to-evaluate-llm-prompts-beyond-simple-use-cases/) — Advanced evaluation techniques
* [Production Traffic is the Key to Prompt Engineering](https://blog.promptlayer.com/production-traffic-is-the-key-to-prompt-engineering/) — Using real data to improve prompts

### Migration

* [Migrating Prompts to Open-Source Models](https://blog.promptlayer.com/migrating-prompts-to-open-source-models/) — Switching to Mistral and other open-source LLMs
* [Migration Guide](/migration) — Moving to PromptLayer from other solutions
