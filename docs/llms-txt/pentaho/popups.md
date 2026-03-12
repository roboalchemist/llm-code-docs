# Source: https://docs.pentaho.com/pba-ctools/pentaho-cdf-api/dashboard/popups.md

# Popups

## cdf.dashboard. Popups

Static

A static class containing pre-built error and success popups.

Each exposed popup is an object with a `render` method that can be called to show the popup with some default values for each case.

**AMD Module**

```
require(["cdf/dashboard/Popups"], function(Popups) { /* code goes here */ });
```

\*\*Source:\*\*dashboard/Popups.js, line 22

## Classes

| Name                   | Summary                             |
| ---------------------- | ----------------------------------- |
| notificationsComponent | The Error Notification Popup.       |
| notificationsGrowl     | The Error Notification Growl Popup. |
| okPopup                | The Ok Popup.                       |
