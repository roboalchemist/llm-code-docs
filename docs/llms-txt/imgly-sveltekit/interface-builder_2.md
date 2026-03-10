# Interface: Builder

Interface for all available builder. Depending on the context different implementation might be used. A “Button” in the canvas menu might render different component than a button in the topbar or a panel.

## Properties[#](#properties)

| Property | Type |
| --- | --- |
| `Menu` | (`id`, `options`) => `void` |
| `Popover` | (`id`, `options`) => `void` |
| `ButtonRow` | (`id`, `options`) => `void` |
| `MediaPreview` | (`id`, `options`) => `void` |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/themefn)