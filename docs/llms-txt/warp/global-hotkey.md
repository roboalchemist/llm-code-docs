# Source: https://docs.warp.dev/terminal/windows/global-hotkey.md

# Global Hotkey

{% hint style="info" %}
On macOS, [system keyboard shortcuts](https://support.apple.com/en-us/HT201236) like `CMD-ESC`, `CMD-BACKTICK`, `CMD-TAB`, `CMD-PERIOD`, and `CMD-TILDE` need to be [unbound](https://support.apple.com/guide/mac-help/keyboard-shortcuts-mchlp2262/mac) before you can use them in Warp.
{% endhint %}

{% hint style="warning" %}
On Linux, the Global Hotkey may not work for some X11 window managers that do not implement [Extended Window Manager Hints](https://en.wikipedia.org/wiki/Extended_Window_Manager_Hints). Some examples include: [sowm](https://github.com/dylanaraps/sowm), [catwm](https://github.com/pyknite/catwm), [Fvwm](https://www.fvwm.org/), [dwm](https://dwm.suckless.org/), [2bWM](https://github.com/venam/2bwm), [monsterwm](https://github.com/c00kiemon5ter/monsterwm), [TinyWM](https://github.com/mackstann/tinywm), [x11fs](https://github.com/sdhand/x11fs), [XMonad](https://xmonad.org/)
{% endhint %}

## How to access it

### Dedicated Window

Dedicated Window allows you to customize the windows' pinned position and its width and height ratio relative to your active screen size (also known as Quake Mode).

1. Open `Settings > Features > Keys` and select "Dedicated hotkey window" from the Global Hotkey dropdown to enable the feature.
2. Configure the keybinding, the windows position, screen, and relative size or uncheck "Autohides on the loss of keyboard focus" which will cause the dedicated Hotkey Window to stay on top when triggered regardless of mouse or keyboard focus.

{% hint style="warning" %}
On Linux and Windows, Warp does not support the "Autohides on the loss of keyboard focus" feature.
{% endhint %}

### Show/Hide All Windows

Show/Hide All Windows allows you to configure a shortcut to show/hide all Warp windows.

1. Open `Settings > Features > Keys` and select "Show/hide all windows" from the Global Hotkey dropdown to enable the feature.
2. Configure your preferred keybinding.

{% hint style="warning" %}
On Linux, hidden windows may not appear in your `ALT-TAB` window switcher menu. Furthermore, the ordering of windows beyond the top window may change after toggling.
{% endhint %}

## How it works

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-048acf9fd85b0fa2129bb90a1b3d8a2d1f911f5b%2FDedicated%20Window.gif?alt=media&#x26;token=39195b3a-16c6-44e5-b2e2-f4bb84677c30" alt=""><figcaption><p>Global Hotkey - Dedicated Window Demo</p></figcaption></figure>

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-af6164e0085e8fa8f3d2ff3602178e4c9343332c%2FShow-Hide%20All%20Windows.gif?alt=media&#x26;token=e292ad67-f087-4b0b-a779-f5266be40a45" alt=""><figcaption><p>Global Hotkey - Show/Hide All Windows Demo</p></figcaption></figure>

## Troubleshooting Hotkey Dedicated Window

Review platform-specific instructions for troubleshooting the global hotkey below

{% tabs %}
{% tab title="macOS" %}
If the keybinding doesn't work, check under `System Preferences > Security & Privacy > Accessibility` and tick the checkbox to grant Warp access.
{% endtab %}

{% tab title="Windows" %}
On Windows, there are no known issues with Global Hotkey Dedicated Window. If you find an issue, please [send feedback](https://docs.warp.dev/support-and-billing/sending-us-feedback) to let us know.
{% endtab %}

{% tab title="Linux" %}
The hotkey window may appear on the incorrect monitor under certain window sizes. For example, with GNOME, if the hotkey window is supposed to show on a monitor having the taskbar (GNOME Panel), and the window height is 100%, causing an overlap, the hotkey window may fallback to showing on an external monitor if you have one. Try working around this by setting a window height to a lesser percentage, e.g. 90%.
{% endtab %}
{% endtabs %}
