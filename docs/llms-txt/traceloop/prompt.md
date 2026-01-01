# Source: https://www.traceloop.com/docs/playgrounds/columns/prompt.md

# Prompt Column

> Execute LLM prompts with full model configuration

### Prompt

A Prompt column allows you to define a custom prompt and run it directly on your Playground data.
You can compose prompts with messages (system, user, assistant or developer), insert playground variables, and configure which model to use.
Each row in your playground will be passed through the prompt, and the model’s response will be stored in the column.

<Info>
  Prompt columns make it easy to test different prompts against real data, compare model outputs side by side.
</Info>

<img className="block dark:hidden" src="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-column-light.png?fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=88046857909c4eb3be8500a4aafed854" style={{maxWidth: '400'}} data-og-width="2680" width="2680" data-og-height="1510" height="1510" data-path="img/playground/play-prompt-column-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-column-light.png?w=280&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=eefb57c6d6320da2471dd0b2665526a0 280w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-column-light.png?w=560&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=6d98da9ea23b9cc3e175b83faa18d1f9 560w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-column-light.png?w=840&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=c8e2c25b84eb8c1e9c7f4eb0bda3f5e6 840w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-column-light.png?w=1100&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=b0c3aff36d4741574037e49b77655dc9 1100w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-column-light.png?w=1650&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=ece809297f252bf8cd6eed9f8a920138 1650w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-column-light.png?w=2500&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=6ba62615ea71742ee9ba64a976454972 2500w" />

<img className="hidden dark:block" src="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-column-dark.png?fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=37290df1e71a2ac357db3e3f38322246" style={{maxWidth: '400'}} data-og-width="2700" width="2700" data-og-height="1544" height="1544" data-path="img/playground/play-prompt-column-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-column-dark.png?w=280&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=768af2c6526dfc3ddf133ac6676380a0 280w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-column-dark.png?w=560&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=c5cbf0a52e9fa08ec346c36db60bbb93 560w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-column-dark.png?w=840&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=c2334a9e63ae3f29b2abe3722d2ab304 840w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-column-dark.png?w=1100&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=b8f664472600d4ba7b8db21a54803937 1100w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-column-dark.png?w=1650&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=3a9d8da709aaaee8a440780de7749091 1650w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-column-dark.png?w=2500&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=71f654b811e46979f7fbe10b21e9c641 2500w" />

## Prompt Writing

Write your prompt messages by selecting a specific role—System, User, Assistant, or Developer.

You can insert variables into the prompt using curly brackets (e.g., `{{variable_name}}`) or by adding column valuable with the top right `+` button in the message box. These variables can then be mapped to existing column data, allowing your prompt to dynamically adapt to the playground

<img className="block dark:hidden" src="https://mintcdn.com/enrolla/fi54H1qiXGQeGMJV/img/playground/play-prompt-write-light.png?fit=max&auto=format&n=fi54H1qiXGQeGMJV&q=85&s=2b06d83d25704bc9cede4c42e9915535" style={{maxWidth: '400'}} data-og-width="1576" width="1576" data-og-height="1368" height="1368" data-path="img/playground/play-prompt-write-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/fi54H1qiXGQeGMJV/img/playground/play-prompt-write-light.png?w=280&fit=max&auto=format&n=fi54H1qiXGQeGMJV&q=85&s=155b8edcdd898db061087fd2726af90b 280w, https://mintcdn.com/enrolla/fi54H1qiXGQeGMJV/img/playground/play-prompt-write-light.png?w=560&fit=max&auto=format&n=fi54H1qiXGQeGMJV&q=85&s=f508b436d19b135628ac51843c1fc075 560w, https://mintcdn.com/enrolla/fi54H1qiXGQeGMJV/img/playground/play-prompt-write-light.png?w=840&fit=max&auto=format&n=fi54H1qiXGQeGMJV&q=85&s=bb0ec529462a5e591bc4866f8a24f9c1 840w, https://mintcdn.com/enrolla/fi54H1qiXGQeGMJV/img/playground/play-prompt-write-light.png?w=1100&fit=max&auto=format&n=fi54H1qiXGQeGMJV&q=85&s=0acc0e65ff40391ce469ae0766664d6b 1100w, https://mintcdn.com/enrolla/fi54H1qiXGQeGMJV/img/playground/play-prompt-write-light.png?w=1650&fit=max&auto=format&n=fi54H1qiXGQeGMJV&q=85&s=5ab0f93fa6d6f8cfcf834c2f90c7e7c0 1650w, https://mintcdn.com/enrolla/fi54H1qiXGQeGMJV/img/playground/play-prompt-write-light.png?w=2500&fit=max&auto=format&n=fi54H1qiXGQeGMJV&q=85&s=a3348b4f5e89532b323f32f859ab21ed 2500w" />

<img className="hidden dark:block" src="https://mintcdn.com/enrolla/fi54H1qiXGQeGMJV/img/playground/play-prompt-write-dark.png?fit=max&auto=format&n=fi54H1qiXGQeGMJV&q=85&s=c71f537426522461848a63ecd32915c8" style={{maxWidth: '400'}} data-og-width="1576" width="1576" data-og-height="1368" height="1368" data-path="img/playground/play-prompt-write-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/fi54H1qiXGQeGMJV/img/playground/play-prompt-write-dark.png?w=280&fit=max&auto=format&n=fi54H1qiXGQeGMJV&q=85&s=d52b472e6cfdcc1bc98fe6e789f1cf3c 280w, https://mintcdn.com/enrolla/fi54H1qiXGQeGMJV/img/playground/play-prompt-write-dark.png?w=560&fit=max&auto=format&n=fi54H1qiXGQeGMJV&q=85&s=cd2743812dc2b5400157a174de7fcfc3 560w, https://mintcdn.com/enrolla/fi54H1qiXGQeGMJV/img/playground/play-prompt-write-dark.png?w=840&fit=max&auto=format&n=fi54H1qiXGQeGMJV&q=85&s=2bd49513845561fee707150220e807d1 840w, https://mintcdn.com/enrolla/fi54H1qiXGQeGMJV/img/playground/play-prompt-write-dark.png?w=1100&fit=max&auto=format&n=fi54H1qiXGQeGMJV&q=85&s=41e1f43753a21c31e5380afcbf66f54a 1100w, https://mintcdn.com/enrolla/fi54H1qiXGQeGMJV/img/playground/play-prompt-write-dark.png?w=1650&fit=max&auto=format&n=fi54H1qiXGQeGMJV&q=85&s=96fbf5c08a8c5d221b55e61413300c12 1650w, https://mintcdn.com/enrolla/fi54H1qiXGQeGMJV/img/playground/play-prompt-write-dark.png?w=2500&fit=max&auto=format&n=fi54H1qiXGQeGMJV&q=85&s=cb41facdfe4115eda07c3a689b70cd36 2500w" />

## Configuration Options

### Model Selection

You can connect to a wide range of LLM providers and models. Common choices include OpenAI (GPT-4o, GPT-4o-mini), Anthropic (Claude-3.5-Sonnet, Claude-3-Opus), and Google (Gemini-2.5 family).
Other providers such as Groq and DeepSeek may also be supported, and additional integrations will continue to be added over time.

### Structured Output

Structured output can be enabled for models that support it. You can define a schema in several ways:

* **JSON Editor** - Write a JSON structure directly in the editor
* **Visual Editor** - Add parameters interactively, specifying their names and types
* **Generate Schema** - Use the "Generate schema" button on the top right to automatically create a schema based on your written prompt

<img className="block dark:hidden" src="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-structure-output-light.png?fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=f058893831f04ac7a12a5954e59aa8bb" style={{maxWidth: '600px'}} data-og-width="1064" width="1064" data-og-height="658" height="658" data-path="img/playground/play-prompt-structure-output-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-structure-output-light.png?w=280&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=4218fdd45a85b4ac0e103c782a1c621b 280w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-structure-output-light.png?w=560&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=750934d1e3c583f00211fea405fe4e99 560w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-structure-output-light.png?w=840&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=37de6f4786cfae52d16d8d11049d6dc1 840w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-structure-output-light.png?w=1100&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=f600e5afb0e577f791ada174ccddcc86 1100w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-structure-output-light.png?w=1650&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=16b005b83df2545c2f70044c4e2ce071 1650w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-structure-output-light.png?w=2500&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=b4e9606c87513c0cb42dcd03ab246de0 2500w" />

<img className="hidden dark:block" src="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-structure-output-dark.png?fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=8d17fd484c50a99e721a92f8840adadf" style={{maxWidth: '600px'}} data-og-width="1030" width="1030" data-og-height="620" height="620" data-path="img/playground/play-prompt-structure-output-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-structure-output-dark.png?w=280&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=ebb3ea7fb39034f8dc88004a60598909 280w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-structure-output-dark.png?w=560&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=37b133d040bac8226329b7b887f3776b 560w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-structure-output-dark.png?w=840&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=c95bf5088bf898b09ab87388759d9594 840w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-structure-output-dark.png?w=1100&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=c89a7f3be7e65e63f9230eb9508bb05a 1100w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-structure-output-dark.png?w=1650&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=4edb9c48f9dd4f9e56784ba9b342bc12 1650w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/playground/play-prompt-structure-output-dark.png?w=2500&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=0caaf0f9d32c01a8057dd40b985c650c 2500w" />

## Tools

Tools let you extend prompts by allowing the model to call custom functions with structured arguments. Instead of plain text, the model can return a validated tool-call object that follows your schema.

To create a tool, give it a name and description so the model knows when to use it. Then define its parameters with a name, description, type (string, number, boolean, etc.), and whether they are required.

### Advanced Settings

Fine-tune model behavior options:

* **Temperature** (0.0-1.0): Control randomness and creativity
* **Max Tokens**: Limit model output length (1-8000+ depending on model)
* **Top P**: Nucleus sampling parameter (0.0-1.0)
* **Frequency Penalty**: Reduce repetition (0.0 to 1.0)
* **Presence Penalty**: Encourage topic diversity (0.0 to 1.0)
* **Logprobs**: When enabled, returns the probability scores for generated tokens
* **Thinking Budget** (512-24576): Sets the number of tokens the model can use for internal reasoning before producing the final output
  A higher budget allows more complex reasoning but increases cost and runtime
* **Exclude Reasoning from Response**: If enabled, the model hides its internal reasoning steps and only outputs the final response

## Prompt Execution

A prompt can be executed across all cells in a column or on a specific cell.

Prompt outputs can be mapped to different columns by clicking a cell and selecting the mapping icon, or by double-clicking the cell


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://www.traceloop.com/docs/llms.txt