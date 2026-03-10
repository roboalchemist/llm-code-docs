# Interface: Dialog

Represents a dialog configuration.

The Dialog interface defines the structure of a dialog configuration within the Creative Editor SDK. It includes properties for the type, size, content, progress, actions, cancel action, onClose callback, and whether clicking outside the dialog should close it. This interface provides a comprehensive way to define and manage dialogs, allowing for flexibility in how they are presented and interacted with by users.

## Properties[#](#properties)

| Property | Type |
| --- | --- |
| `type?` | [`DialogType`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/dialogtype/) |
| `size?` | [`DialogSize`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/dialogsize/) |
| `content` | [`DialogContent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/dialogcontent/) |
| `progress?` | [`DialogProgress`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/dialogprogress/) |
| `actions?` |  |
| `cancel?` | [`DialogAction`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/dialogaction/) |
| `onClose?` | () => `void` |
| `clickOutsideToClose?` | `boolean` |

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/componentpayload)