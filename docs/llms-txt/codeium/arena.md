# Source: https://docs.windsurf.com/windsurf/cascade/arena.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.windsurf.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Arena Mode

> Run multiple Cascade instances in parallel using arena mode to explore different approaches simultaneously.

Cascade supports **arena mode** to allow you to easily compare responses from different models on the same prompt.

| Mode       | Use Case                                |
| ---------- | --------------------------------------- |
| **Single** | Run Cascade with a single chosen model  |
| **Arena**  | Compare responses from different models |

## Arena Mode

To enter arena mode, click the **arena** button in the model picker and choose your preferred models.

When you select multiple models, Cascade will independently execute your prompt with each model in a separate session. Each model also gets its own [worktree](./worktrees) for isolation.

<Tip>
  If you want to view both conversations at the same time, you can drag the
  Cascade tab into the main editor window to expand the available space.
</Tip>

You can independently continue working in each Cascade conversation, including accepting or rejecting changes or asking follow-up questions.
Since each model has its own [worktree](./worktrees), you can iterate on each response without affecting the others sessions.

### Choosing the better response

When you're ready to commit to a particular approach, you should click the "X is better" button to **discard** other conversations and *converge* all models to continue with your chosen approach.
The next message you send after converging will be sent to all models you have selected, allowing you to continue trying out different approaches.

<Frame>
  <img style={{ maxHeight: "500px" }} src="https://mintcdn.com/codeium/fY08IFDMBkmjud5v/assets/windsurf/cascade/proceed.png?fit=max&auto=format&n=fY08IFDMBkmjud5v&q=85&s=ff6dc05b9d587682e2cb8d0f91077ced" data-og-width="1252" width="1252" data-og-height="260" height="260" data-path="assets/windsurf/cascade/proceed.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/fY08IFDMBkmjud5v/assets/windsurf/cascade/proceed.png?w=280&fit=max&auto=format&n=fY08IFDMBkmjud5v&q=85&s=4f4b16257ea09bbd3949ec7f07e1e315 280w, https://mintcdn.com/codeium/fY08IFDMBkmjud5v/assets/windsurf/cascade/proceed.png?w=560&fit=max&auto=format&n=fY08IFDMBkmjud5v&q=85&s=2fbd6fecd49bdc05ec85cf24701f68fd 560w, https://mintcdn.com/codeium/fY08IFDMBkmjud5v/assets/windsurf/cascade/proceed.png?w=840&fit=max&auto=format&n=fY08IFDMBkmjud5v&q=85&s=c7e7a80578d4b8fc05b01b1fbb1e38a6 840w, https://mintcdn.com/codeium/fY08IFDMBkmjud5v/assets/windsurf/cascade/proceed.png?w=1100&fit=max&auto=format&n=fY08IFDMBkmjud5v&q=85&s=b90ddfc715185d4a6f6167d8334f6804 1100w, https://mintcdn.com/codeium/fY08IFDMBkmjud5v/assets/windsurf/cascade/proceed.png?w=1650&fit=max&auto=format&n=fY08IFDMBkmjud5v&q=85&s=628a25e65020f20c8fd5812efc0a13e3 1650w, https://mintcdn.com/codeium/fY08IFDMBkmjud5v/assets/windsurf/cascade/proceed.png?w=2500&fit=max&auto=format&n=fY08IFDMBkmjud5v&q=85&s=61bc70d1689393b88f8baa057769f848 2500w" />
</Frame>

## Battle Groups

Instead of manually selecting models, you can select one of our curated model groups to have Cascade randomly choose two models to compare. We have two random model groups available:

* **Frontier**: Includes frontier reasoning models like GPT 5.2, Claude Opus/Sonnet 4.5, Gemini 3 Pro, etc., optimized for intelligence.
* **Fast**: Includes fast reasoning models like SWE 1.5, Claude Haiku, etc., optimized for speed.

When you use one of the battle groups, the exact model names are hidden from you until you click the "X is better" button to converge the models. Then, the original model names are revealed and the conversations are reshuffled.

## When To Use Arena Mode

Arena mode is particularly useful when you want to:

* Compare code quality across different models
* Explore different approaches to a hard problem
* Test out a new model without abandoning your standard preference
* Access frontier models at reduced cost by using the battle groups

## Limitations

* Arena mode is only supported for workspaces that have git initialized
* By default, only Git-tracked files are copied into the worktrees created for each model; you can configure a [setup hook](./worktrees#setup-hook) to copy additional files as needed

## Related Features

<CardGroup cols={2}>
  <Card title="Worktrees" icon="code-branch" href="/windsurf/cascade/worktrees">
    Isolate parallel work in separate git worktrees.
  </Card>

  <Card title="Hooks" icon="plug" href="/windsurf/cascade/hooks">
    Automate actions before and after Cascade operations.
  </Card>
</CardGroup>
