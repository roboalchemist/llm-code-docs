# Source: https://docs.warp.dev/terminal/sessions/session-navigation.md

# Session Navigation

## How to access Session navigation

1. Open the Session Navigation palette with the [Command Palette](https://docs.warp.dev/terminal/command-palette), click on **session >\_** or type in "sessions:".
2. Jump to a session by using your mouse or the `UP ↑`/`DOWN ↓` arrow keys and `ENTER`.
3. Refine the session results by searching for sessions by prompt, the currently running command, last run command, and command status (ex: “Running…”, “Completed 10 minutes ago”, “Empty Session”).

{% hint style="info" %}
Sessions are ordered by recency, so the most recently focused sessions show up first. The Session Navigation palette does not have **PS1** support and can only show Warp's native prompt.
{% endhint %}

### CTRL-TAB Behaviour

`CTRL-TAB` shortcut defaults to activate the previous / next [Tabs](https://docs.warp.dev/terminal/windows/tabs). You can configure the shortcut to cycle the most recent session, including any [Split Panes](https://docs.warp.dev/terminal/windows/split-panes), in `Settings > Features > Keys > Ctrl-Tab behavior`

## How Session Navigation Works

{% embed url="<https://www.loom.com/share/2147adc6749c4f4ea5da432eadda7995>" %}
Session Navigation Demo
{% endembed %}
