# Source: https://docs.warp.dev/terminal/sessions/session-restoration.md

# Session Restoration

## What is it

Session restoration allows you to quickly pick up where you left off in your previous terminal session.

## How to access Session Restoration

* Session Restoration comes enabled by default in Warp.

{% hint style="info" %}
On Linux, opening windows at a specific position is not supported in Wayland.
{% endhint %}

* You can disable Session Restoration by going to `Settings > Features`, then toggling off `Restore windows, tabs, and panes on startup`.

{% hint style="warning" %}
Toggling off Session Restoration will not clear the [SQLite database](#session-restoration-database); however, Warp will stop recording new output.
{% endhint %}

## How Session Restoration works

![Session Restoration Demo](https://4009768362-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FPsjNxoJ0NFCXW6rRdHH3%2Fuploads%2Fgit-blob-eea5d549c432c9c124c175120bc2b901b1add9fb%2Fsessions-block_restoration.gif?alt=media)

#### Session Restoration database

Warp saves the data from your previous session's windows, tabs, and panes to a SQLite database on your computer, and every time you quit the app, this data is overwritten by your latest session. You can open the database directly and inspect its full contents like so:

{% tabs %}
{% tab title="macOS" %}

```bash
sqlite3 "$HOME/Library/Group Containers/2BBY89MBSN.dev.warp/Library/Application Support/dev.warp.Warp-Stable/warp.sqlite"
```

{% endtab %}

{% tab title="Windows" %}

```powershell
sqlite3 $env:LOCALAPPDATA\warp\Warp\data\warp.sqlite
```

{% endtab %}

{% tab title="Linux" %}

```bash
sqlite3 "${XDG_STATE_HOME:-$HOME/.local/state}/warp-terminal/warp.sqlite"
```

{% endtab %}
{% endtabs %}

**How to clear the Session Restoration database**

Sometimes, you may want to prevent a sensitive Block from being saved on your computer, or you may want to clear blocks from a machine entirely.

{% hint style="info" %}
This interferes with the running session's ability to save content and may require you close Warp before running the database removal commands.
{% endhint %}

{% hint style="danger" %}
The following guidance is destructive and will delete any sessions and block history.
{% endhint %}

There are two ways to do this:

{% tabs %}
{% tab title="macOS" %}

* Clear the blocks from your running Warp session with `CMD-K`.
* Delete the SQLite file entirely with the following command:

```bash
rm -f "$HOME/Library/Group Containers/2BBY89MBSN.dev.warp/Library/Application Support/dev.warp.Warp-Stable/warp.sqlite"
```

{% endtab %}

{% tab title="Windows" %}

* Clear the blocks from your running Warp session with `CTRL-SHIFT-K`.
* Delete the SQLite file entirely with the following command:

```powershell
Remove-Item -Force $env:LOCALAPPDATA\warp\Warp\data\warp.sqlite
```

{% endtab %}

{% tab title="Linux" %}

* Clear the blocks from your running Warp session with `CTRL-SHIFT-K`.
* Delete the SQLite file entirely with the following command:

```bash
rm -f "${XDG_STATE_HOME:-$HOME/.local/state}/warp-terminal/warp.sqlite"
```

{% endtab %}
{% endtabs %}
