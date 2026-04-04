# Notifications and Dialogs

Display notifications and dialogs to communicate with users during the editing experience using CE.SDK’s UI API.

![Notifications and Dialogs example showing the CE.SDK editor with notification and dialog UI](/docs/cesdk/_astro/browser.hero.B-4Uuw-f_ZEuLiT.webp)

10 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-user-interface-ui-extensions-notifications-and-dialogs-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-user-interface-ui-extensions-notifications-and-dialogs-browser)

Notifications and dialogs are essential for communicating with users during the editing experience. Notifications appear as temporary, non-blocking messages at the edge of the editor for status updates and feedback. Dialogs are modal overlays that interrupt the workflow to present information or collect user decisions. Both are created and controlled through the `cesdk.ui` API.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
class Example implements EditorPlugin {  name = packageJson.name;  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    // Load assets and create scene    await cesdk.addDefaultAssetSources();    await cesdk.addDemoAssetSources({      sceneMode: 'Design',      withUploadAssetSources: true    });
    // Use cesdk convenience method - automatically handles zoom    await cesdk.createDesignScene();
    // Register a notifications dropdown in the navigation bar    cesdk.ui.registerComponent(      'ly.img.notifications.demo.navigationBar',      ({ builder }) => {        // Display a simple notification with a string message        builder.Button('simple-notification', {          label: 'Simple',          onClick: () => {            cesdk.ui.showNotification('Welcome to CE.SDK!');          }        });
        // Display notifications with different types        builder.Button('info-notification', {          label: 'Info',          onClick: () => {            cesdk.ui.showNotification({              message: 'This is an info notification',              type: 'info'            });          }        });
        builder.Button('success-notification', {          label: 'Success',          onClick: () => {            cesdk.ui.showNotification({              message: 'Operation completed successfully',              type: 'success'            });          }        });
        builder.Button('warning-notification', {          label: 'Warning',          onClick: () => {            cesdk.ui.showNotification({              message: 'Please check your input',              type: 'warning'            });          }        });
        builder.Button('error-notification', {          label: 'Error',          onClick: () => {            cesdk.ui.showNotification({              message: 'Something went wrong',              type: 'error'            });          }        });
        // Add an action button to a notification        builder.Button('action-notification', {          label: 'With Action',          onClick: () => {            cesdk.ui.showNotification({              message: 'New template available',              type: 'info',              duration: 'long',              action: {                label: 'View',                onClick: ({ id }) => {                  console.log('Action clicked on notification:', id);                  cesdk.ui.dismissNotification(id);                }              }            });          }        });
        // Create a loading notification that updates to success        builder.Button('loading-notification', {          label: 'Loading → Success',          onClick: () => {            const loadingId = cesdk.ui.showNotification({              message: 'Processing your request...',              type: 'loading',              duration: 'infinite'            });
            // Simulate async operation completing            setTimeout(() => {              cesdk.ui.updateNotification(loadingId, {                type: 'success',                message: 'Processing complete!',                duration: 'medium'              });            }, 2000);          }        });
        // Show a notification that can be dismissed        builder.Button('dismiss-notification', {          label: 'Auto-Dismiss',          onClick: () => {            const notificationId = cesdk.ui.showNotification({              message: 'This will be dismissed in 2 seconds',              type: 'info',              duration: 'infinite'            });
            setTimeout(() => {              cesdk.ui.dismissNotification(notificationId);            }, 2000);          }        });
        // Handle notification dismiss events        builder.Button('ondismiss-notification', {          label: 'With Callback',          onClick: () => {            cesdk.ui.showNotification({              message: 'Dismiss me to see the callback',              type: 'info',              duration: 'long',              onDismiss: () => {                console.log('Notification was dismissed');              }            });          }        });      }    );
    // Register a dialogs dropdown in the navigation bar    cesdk.ui.registerComponent(      'ly.img.dialogs.demo.navigationBar',      ({ builder }) => {        // Display a simple dialog with a string message        builder.Button('simple-dialog', {          label: 'Simple',          onClick: () => {            cesdk.ui.showDialog('This is a simple dialog message');          }        });
        // Show a dialog and close it programmatically        builder.Button('close-dialog', {          label: 'Auto-Close',          onClick: () => {            const dialogId = cesdk.ui.showDialog(              'This dialog will close in 2 seconds'            );            setTimeout(() => {              cesdk.ui.closeDialog(dialogId);            }, 2000);          }        });
        // Display a warning dialog with actions        builder.Button('warning-dialog', {          label: 'Warning',          onClick: () => {            cesdk.ui.showDialog({              type: 'warning',              content: {                title: 'Unsaved Changes',                message:                  'You have unsaved changes. Do you want to save before leaving?'              },              actions: [                {                  label: 'Save',                  color: 'accent',                  onClick: ({ id }) => {                    console.log('Save clicked');                    cesdk.ui.closeDialog(id);                  }                },                {                  label: "Don't Save",                  variant: 'plain',                  onClick: ({ id }) => {                    console.log('Discard clicked');                    cesdk.ui.closeDialog(id);                  }                }              ],              cancel: {                label: 'Cancel',                onClick: ({ id }) => cesdk.ui.closeDialog(id)              }            });          }        });
        // Create a loading dialog with progress indicator        builder.Button('progress-dialog', {          label: 'Progress',          onClick: () => {            const progressDialogId = cesdk.ui.showDialog({              type: 'loading',              content: {                title: 'Exporting',                message: 'Preparing your export...'              },              progress: 'indeterminate',              clickOutsideToClose: false            });
            // Simulate progress updates            let progress = 0;            const progressInterval = setInterval(() => {              progress += 20;              cesdk.ui.updateDialog(progressDialogId, {                progress: { value: progress, max: 100 },                content: {                  title: 'Exporting',                  message: `Processing... ${progress}%`                }              });
              if (progress >= 100) {                clearInterval(progressInterval);                cesdk.ui.updateDialog(progressDialogId, {                  type: 'success',                  content: {                    title: 'Export Complete',                    message: 'Your file has been exported successfully.'                  },                  progress: undefined,                  actions: [                    {                      label: 'Done',                      color: 'accent',                      onClick: ({ id }) => cesdk.ui.closeDialog(id)                    }                  ],                  clickOutsideToClose: true                });              }            }, 500);          }        });
        // Dialog with multi-paragraph content and large size        builder.Button('content-dialog', {          label: 'Large Content',          onClick: () => {            cesdk.ui.showDialog({              type: 'info',              size: 'large',              content: {                title: 'About This Feature',                message: [                  'Notifications and dialogs help communicate with users during the editing workflow.',                  'Use notifications for non-blocking feedback and dialogs for important decisions.'                ]              },              actions: [                {                  label: 'Got It',                  color: 'accent',                  onClick: ({ id }) => cesdk.ui.closeDialog(id)                }              ]            });          }        });
        // Handle dialog close events        builder.Button('onclose-dialog', {          label: 'With Callback',          onClick: () => {            cesdk.ui.showDialog({              type: 'info',              content: 'Close this dialog to see the callback',              onClose: () => {                console.log('Dialog was closed');              }            });          }        });      }    );
    // Add the demo dropdowns to the navigation bar    cesdk.ui.setNavigationBarOrder([      'ly.img.navigationBar.position.left',      'ly.img.navigationBar.position.center',      'ly.img.navigationBar.position.right',      'ly.img.notifications.demo.navigationBar',      'ly.img.dialogs.demo.navigationBar'    ]);  }}
export default Example;
```

## Displaying Notifications[#](#displaying-notifications)

Notifications provide non-blocking feedback without interrupting the user’s workflow. They appear in the lower right corner of the editor and automatically dismiss after a set duration.

### Creating Notifications[#](#creating-notifications)

Use `cesdk.ui.showNotification()` to display a notification. Pass a string for a simple message or a configuration object for full control. The method returns a unique ID for managing the notification.

```
cesdk.ui.showNotification('Welcome to CE.SDK!');
```

### Notification Types[#](#notification-types)

Configure the visual appearance with the `type` property. Available types convey different levels of importance:

*   `info` — General information (default)
*   `success` — Positive confirmations
*   `warning` — Cautions requiring attention
*   `error` — Errors or failures
*   `loading` — Operations in progress with a spinner

```
cesdk.ui.showNotification({  message: 'This is an info notification',  type: 'info'});
```

### Notification Duration[#](#notification-duration)

Control how long notifications remain visible using the `duration` property:

*   `short` — Brief display for quick updates
*   `medium` — Standard duration (default)
*   `long` — Extended display for important messages
*   `infinite` — Persists until dismissed programmatically
*   A number for custom millisecond duration

### Adding Actions to Notifications[#](#adding-actions-to-notifications)

Include an `action` object to add a clickable button. The action’s `onClick` callback receives an object with the notification ID, allowing self-dismissal or other operations.

```
cesdk.ui.showNotification({  message: 'New template available',  type: 'info',  duration: 'long',  action: {    label: 'View',    onClick: ({ id }) => {      console.log('Action clicked on notification:', id);      cesdk.ui.dismissNotification(id);    }  }});
```

### Loading Notifications[#](#loading-notifications)

For operations with unknown completion time, create a loading notification with `infinite` duration. Update or dismiss it when the operation completes.

```
const loadingId = cesdk.ui.showNotification({  message: 'Processing your request...',  type: 'loading',  duration: 'infinite'});
```

### Updating Notifications[#](#updating-notifications)

Modify an existing notification with `cesdk.ui.updateNotification()`. Pass the ID and a partial notification object with updated properties. This is useful for changing a loading notification to a success message when an operation completes.

```
cesdk.ui.updateNotification(loadingId, {  type: 'success',  message: 'Processing complete!',  duration: 'medium'});
```

### Dismissing Notifications[#](#dismissing-notifications)

Use `cesdk.ui.dismissNotification()` with the notification ID to remove it programmatically. This is useful for canceling loading notifications when operations complete or when you need to clear notifications based on user actions.

```
const notificationId = cesdk.ui.showNotification({  message: 'This will be dismissed in 2 seconds',  type: 'info',  duration: 'infinite'});
setTimeout(() => {  cesdk.ui.dismissNotification(notificationId);}, 2000);
```

### Handling Dismiss Callbacks[#](#handling-dismiss-callbacks)

Use the `onDismiss` callback to execute code when a notification is dismissed, whether by timeout, user action, or programmatic dismissal.

```
cesdk.ui.showNotification({  message: 'Dismiss me to see the callback',  type: 'info',  duration: 'long',  onDismiss: () => {    console.log('Notification was dismissed');  }});
```

## Displaying Dialogs[#](#displaying-dialogs)

Dialogs present modal content requiring user attention or decisions. They overlay the editor and block interaction until dismissed.

### Creating Dialogs[#](#creating-dialogs)

Use `cesdk.ui.showDialog()` to display a dialog. Pass a string for a simple message or a configuration object for full control. The method returns a unique ID for managing the dialog.

```
cesdk.ui.showDialog('This is a simple dialog message');
```

### Closing Dialogs[#](#closing-dialogs)

Use `cesdk.ui.closeDialog()` with the dialog ID to close it programmatically.

```
const dialogId = cesdk.ui.showDialog(  'This dialog will close in 2 seconds');setTimeout(() => {  cesdk.ui.closeDialog(dialogId);}, 2000);
```

### Dialog Types and Actions[#](#dialog-types-and-actions)

Configure the visual style with the `type` property. Available types are `regular` (default), `info`, `success`, `warning`, `error`, and `loading`. Add action buttons with the `actions` array and a cancel button with the `cancel` property.

```
cesdk.ui.showDialog({  type: 'warning',  content: {    title: 'Unsaved Changes',    message:      'You have unsaved changes. Do you want to save before leaving?'  },  actions: [    {      label: 'Save',      color: 'accent',      onClick: ({ id }) => {        console.log('Save clicked');        cesdk.ui.closeDialog(id);      }    },    {      label: "Don't Save",      variant: 'plain',      onClick: ({ id }) => {        console.log('Discard clicked');        cesdk.ui.closeDialog(id);      }    }  ],  cancel: {    label: 'Cancel',    onClick: ({ id }) => cesdk.ui.closeDialog(id)  }});
```

Each action object includes:

*   `label` — Button text
*   `variant` — `regular` (default) or `plain` for a text-only button
*   `color` — `accent` for primary actions or `danger` for destructive actions
*   `onClick` — Callback receiving the dialog ID for closing or other operations

### Progress Indicators[#](#progress-indicators)

Display progress in loading dialogs with the `progress` property:

*   `indeterminate` — For unknown duration
*   A number (0-100) — For percentage progress
*   An object with `value` and `max` — For custom progress ranges

```
const progressDialogId = cesdk.ui.showDialog({  type: 'loading',  content: {    title: 'Exporting',    message: 'Preparing your export...'  },  progress: 'indeterminate',  clickOutsideToClose: false});
```

### Updating Dialogs[#](#updating-dialogs)

Modify an existing dialog with `cesdk.ui.updateDialog()`. Pass the ID and a partial dialog object. This is useful for updating progress indicators or changing dialog content during operations.

```
cesdk.ui.updateDialog(progressDialogId, {  progress: { value: progress, max: 100 },  content: {    title: 'Exporting',    message: `Processing... ${progress}%`  }});
```

### Dialog Content[#](#dialog-content)

Set content as a string for simple messages or an object with `title` and `message` properties. The message can be a string or an array of strings for multiple paragraphs. Use the `size` property to control dialog dimensions (`regular` or `large`).

```
cesdk.ui.showDialog({  type: 'info',  size: 'large',  content: {    title: 'About This Feature',    message: [      'Notifications and dialogs help communicate with users during the editing workflow.',      'Use notifications for non-blocking feedback and dialogs for important decisions.'    ]  },  actions: [    {      label: 'Got It',      color: 'accent',      onClick: ({ id }) => cesdk.ui.closeDialog(id)    }  ]});
```

### Handling Close Callbacks[#](#handling-close-callbacks)

Use the `onClose` callback to execute cleanup code when a dialog closes, whether by action, cancel, clicking outside, or programmatic closure.

```
cesdk.ui.showDialog({  type: 'info',  content: 'Close this dialog to see the callback',  onClose: () => {    console.log('Dialog was closed');  }});
```

### Click Outside Behavior[#](#click-outside-behavior)

Control whether clicking outside the dialog closes it with the `clickOutsideToClose` property. It defaults to `true`. Set to `false` for mandatory interactions like loading dialogs.

## Troubleshooting[#](#troubleshooting)

### Notification Not Visible[#](#notification-not-visible)

Verify the notification was created with a valid message string or configuration object. Check that the duration hasn’t expired before you could observe it. Ensure the editor UI is properly initialized before calling notification methods.

### Dialog Not Closing[#](#dialog-not-closing)

Confirm you’re calling `cesdk.ui.closeDialog()` with the correct dialog ID. Check that action callbacks properly close the dialog. If `clickOutsideToClose` is `false`, ensure an action or cancel button is provided.

### Callback Not Firing[#](#callback-not-firing)

Ensure the callback function is properly defined in the notification or dialog configuration. Verify the notification or dialog hasn’t already been dismissed before the callback could fire. Check for JavaScript errors in callback code.

### Progress Not Updating[#](#progress-not-updating)

Confirm you’re using `cesdk.ui.updateDialog()` with the correct dialog ID. Verify the progress value is in the expected format (number, `indeterminate`, or object with `value` and `max`).

## API Reference[#](#api-reference)

| Method | Description |
| --- | --- |
| `cesdk.ui.showNotification()` | Display a non-blocking notification |
| `cesdk.ui.dismissNotification()` | Remove a notification by ID |
| `cesdk.ui.updateNotification()` | Update notification content or properties |
| `cesdk.ui.showDialog()` | Display a modal dialog |
| `cesdk.ui.closeDialog()` | Close a dialog by ID |
| `cesdk.ui.updateDialog()` | Update dialog content or properties |

---



[Source](https:/img.ly/docs/cesdk/vue/user-interface/ui-extensions/customize-behaviour-c09cb2)