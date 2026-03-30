# Interface: UserInterfaceNavigation

Interface representing the navigation in the user interface.

*   `position`: Optional position of the navigation.
*   `title`: Optional title for the navigation.
*   `action`: Optional object containing actions for the navigation.

## Extends[#](#extends)

*   [`UserInterfaceElement`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/userinterfaceelement/)

## Properties[#](#properties)

| Property | Type | Description | Inherited from |
| --- | --- | --- | --- |
| `show?` | `boolean` | \- | [`UserInterfaceElement`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/userinterfaceelement/).[`show`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/userinterfaceelement/) |
| `position?` | [`NavigationPosition`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/userinterfaceelements/enumerations/navigationposition/) | \- | \- |
| `title?` | `string` | \- | \- |
| ~`action?`~ | `object` | **Deprecated** Use the Order API to configure the actions instead. | \- |
| `action.close?` |  | `boolean` | [`UserInterfaceElement`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/userinterfaceelement/) |
| `action.back?` |  | `boolean` | [`UserInterfaceElement`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/userinterfaceelement/) |
| `action.save?` |  | `boolean` | [`UserInterfaceElement`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/userinterfaceelement/) |
| `action.export?` |  | `boolean` | [`UserInterfaceExportAction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/userinterfaceexportaction/) |
| `action.share?` |  | `boolean` | [`UserInterfaceElement`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/userinterfaceelement/) |
| `action.load?` |  | `boolean` | [`UserInterfaceElement`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/userinterfaceelement/) |
| `action.download?` |  | `boolean` | [`UserInterfaceElement`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/userinterfaceelement/) |
| `action.custom?` | [`UserInterfaceCustomAction`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/userinterfacecustomaction/)\[\] | **Deprecated** Use the Order API to configure the actions instead. | \- |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/userinterfaceelements/interfaces/userinterfaceinspectorblocktext)