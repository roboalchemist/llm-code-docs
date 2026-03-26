# Source: https://docs.tabnine.com/main/getting-started/tabnine-cli/features/model-selection.md

# Model Selection

Choose which AI model powers your Tabnine CLI interactions.

### Opening the Model Dialogue

```
/model
```

This opens an interactive dialog showing available models.

### Available Models

Tabnine CLI uses the same models as detailed in the [models](https://docs.tabnine.com/main/welcome/readme/ai-models) section

### Changing Models

Via `/model` Command:

{% stepper %}
{% step %}
**Open the model dialog**

Run:

```
/model
```

This opens the interactive model selection dialog.
{% endstep %}

{% step %}
**Navigate**

Use the arrow keys or `J` / `K` to move through available models.
{% endstep %}

{% step %}
**Select**

Press `Enter` to select the highlighted model.
{% endstep %}

{% step %}
**Immediate effect**

Model changes take effect immediately after selection.
{% endstep %}
{% endstepper %}

### Model Information

View current model:

```
/about
```

or check the footer (shown if enabled in settings).

#### Token Limits

Tabnine CLI automatically manages token limits based on the selected model.

View token usage:

```
/stats
```

### Fallback Behavior

If your selected model is unavailable, Tabnine CLI may:

1. Prompt you to select another model
2. Automatically fall back to a default model (depending on settings)

### Model Persistence

Your model selection is saved and persists across sessions in `.tabnine/agent/settings.json`.

### See Also

* [Commands: /model](https://docs.tabnine.com/main/getting-started/tabnine-cli/commands#model)
* [Commands: /stats](https://docs.tabnine.com/main/getting-started/tabnine-cli/commands#stats)
* [Settings](https://docs.tabnine.com/main/getting-started/tabnine-cli/features/settings)
