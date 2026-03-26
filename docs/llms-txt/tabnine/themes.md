# Source: https://docs.tabnine.com/main/getting-started/tabnine-cli/features/themes.md

# Themes

Customize the visual appearance of Tabnine CLI with built-in themes.

### Available Themes

Tabnine CLI includes the following built-in themes:

* **Dark themes:**
  * `ANSI`
  * `Atom One`
  * `Ayu`
  * `Default`
  * `Dracula`
  * `GitHub`
* **Light themes:**
  * `ANSI Light`
  * `Ayu Light`
  * `Default Light`
  * `GitHub Light`
  * `Google Code`
  * `Xcode`

**Theme Persistence:** Your theme selection is saved to `.tabnine/agent/settings.json` and persists across sessions.

#### **Custom Themes**

To define custom themes, add a `customThemes` section to your `settings.json` file, located under user, project, or system settings. Each theme is an object with a unique name and associated color keys. For example:

```json
{
  "ui": {
    "customThemes": {
      "MyCustomTheme": {
        "name": "MyCustomTheme",
        "type": "custom",
        "Background": "#181818",
        ...
      }
    }
  }
}
```

**Required properties:**

* `name` (must be a string)
* `type` (must be the string `"custom"`)
* `Background`
* `Foreground`
* `LightBlue`
* `AccentBlue`
* `AccentPurple`
* `AccentCyan`
* `AccentGreen`
* `AccentYellow`
* `AccentRed`
* `Comment`
* `Gray`

**Optional properties**

* `DiffAdded`
* `DiffRemoved`
* `DiffModified`
* `GradientColors`

Use hex codes (e.g., `#FF0000`) or CSS color names (e.g., `coral`, `teal`).

### Changing Themes

You can switch between themes in two ways, either by using the `/theme` command or via `/settings`.

{% tabs %}
{% tab title="/theme" %}
{% stepper %}
{% step %}
**Command**

Type the /theme command. This will open an interactive theme selector.

```bash
/theme
```

{% endstep %}

{% step %}
**Navigate**

Use arrow keys or `J`/`K`.
{% endstep %}

{% step %}
**Preview**

Preview theme in real-time.
{% endstep %}

{% step %}
**Apply**

Press `Enter` to apply.
{% endstep %}
{% endstepper %}
{% endtab %}

{% tab title="/settings" %}
Edit the file at `.tabnine/agent/settings.json`, adjusting the "theme" according to the available themes.

```json
{
  "ui": {
    "theme": "ANSI"
  }
}
```

{% endtab %}
{% endtabs %}

### See Also

* [Commands](https://docs.tabnine.com/main/getting-started/tabnine-cli/features/commands)
* [Settings](https://docs.tabnine.com/main/getting-started/tabnine-cli/features/settings)
