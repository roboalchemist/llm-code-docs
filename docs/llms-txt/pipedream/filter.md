# Source: https://pipedream.com/docs/workflows/building-workflows/control-flow/filter.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Filter

### Filter

<Frame>
  <iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/sajgIH3dG58" title="Conditionally run Workflows" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</Frame>

Use the Filter action to quickly stop or continue workflows on certain conditions.

<Frame>
  <img src="https://mintcdn.com/pipedream/nKh6d_6A4aXFb6xD/images/ebe4c539-CleanShot_2022-05-03_at_13.51.17_za1skw.gif?s=cce4659a1e41e5fd3bfacd3f1092e46a" width="800" height="426" data-path="images/ebe4c539-CleanShot_2022-05-03_at_13.51.17_za1skw.gif" />
</Frame>

Add a filter action to your workflow by searching for the **Filter** app in a new step.

The **Filter** app includes several built-in actions: Continue Workflow on Condition, Exit Workflow on Condition and Exit Workflow on Custom Condition.

In each of these actions, the **Value** is the subject of the condition, and the **Condition** is the operand to compare the value against.

For example, to only process orders with a `status = ready`

#### Continue Workflow on Condition

With this action, only when values that *pass* a set condition will the workflow continue to execute steps after this filter.

Built with [Mintlify](https://mintlify.com).
