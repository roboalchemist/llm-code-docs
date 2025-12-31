# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-protect/how-to/editing-centralized-stages.md

# Editing Centralized Stages

> Edit centralized stages in Galileo Protect with this guide, ensuring accurate ruleset updates and maintaining effective AI monitoring across applications.

<Info>The following only applies to [centralized stages](/galileo/gen-ai-studio-products/galileo-protect/concepts/stage).</Info>

Once you've created and registered a [centralized stage](/galileo/gen-ai-studio-products/galileo-protect/concepts/stage#different-types-of-stages) you can continue updating your stage configuration. Your changes will immediately be reflected in any further invocations.

To update a stage, you can call `gp.update_stage()`:

```py
import galileo_protect as gp

gp.update_stage(project_id="<project_id>", # Alternatively, use project_name
                stage_id="<stage_id>", # Alternatively, use stage_name
                prioritized_rulesets=[
    {
        "rules": [
            {
                "metric": "pii",
                "operator": "contains",
                "target_value": "ssn",
            },
        ],
        "action": {
            "type": "OVERRIDE",
            "choices": [
                "Personal Identifiable Information detected in the model output. Sorry, I cannot answer that question."
            ],
        },
    },
])
```

Your changes will immediately be reflected. Any subsequent calls to `gp.invoke()` will use the updated `prioritized_rulesets.`
