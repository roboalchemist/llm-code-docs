# Interface: Notification

Represents a notification configuration.

The Notification interface defines the structure of a notification configuration within the Creative Editor SDK. It includes properties for the type, message, duration, onDismiss callback, and action. This interface provides a comprehensive way to define and manage notifications, allowing for flexibility in how they are presented and interacted with by users.

## Properties[#](#properties)

| Property | Type |
| --- | --- |
| `type?` | [`NotificationType`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/notificationtype/) |
| `message` | `string` |
| `duration?` | [`NotificationDuration`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/notificationduration/) |
| `onDismiss?` | () => `void` |
| `action?` | `object` |
| `action.label` | `string` |
| `action.onClick` | (`context`) => `void` |

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/navigationbarcustomactionbutton)