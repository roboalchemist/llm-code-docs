# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-protect/how-to/pausing-or-resuming-a-stage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Pausing Or Resuming A Stage

> When you're using the Galileo Protect product, once you've created a project and a stage, you can pause and resume the stage.

This feature is useful when you want to temporarily stop the rulesets from being triggered without deleting them. Pausing and resuming a stage can be done for both central and local stages.

To pause a stage, you can use the following code snippet:

```py  theme={null}
import galileo_protect as gp
gp.pause_stage(project_id="<project_id>", stage_id="<stage_id>")
```

To resume a stage, you can use the following code snippet:

```py  theme={null}
import galileo_protect as gp
gp.resume_stage(project_id="<project_id>", stage_id="<stage_id>")
```
