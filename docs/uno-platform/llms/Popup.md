# Source: https://raw.githubusercontent.com/unoplatform/uno/refs/heads/master/doc/articles/controls/Popup.md

---
uid: Uno.Controls.Popup
---

# Popup

## Customizing light-dismiss overlay

If you want to show a dimmed overlay underneath the popup, set the `Popup.LightDismissOverlayMode` property to `On`.

If you wish to customize the overlay color, add the following to your top-level `App.Resources`:

```xml
<SolidColorBrush x:Key="PopupLightDismissOverlayBackground"
                 Color="Red" />
```
