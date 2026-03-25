# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/ChipView.md

# [ChipView](https://bryntum.com/docs/gantt/api/Core/widget/ChipView)

Displays an inline series of Chips which may be navigated to, selected and deleted. You can provide a [closeHandler](https://bryntum.com/docs/gantt/api/#Core/widget/ChipView#config-closeHandler) to decide what should happen when a chip is closed. If not provided, by default the record representing the chip is removed from the store.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[multiSelect](https://bryntum.com/docs/gantt/api/Core/widget/ChipView#config-multiSelect)
Configure as `true` to allow multi select and allow clicking and key navigation to select multiple chips.

[closable](https://bryntum.com/docs/gantt/api/Core/widget/ChipView#config-closable)
Configure as `true` to display a clickable close icon after the [itemTpl](https://bryntum.com/docs/gantt/api/#Core/widget/List#config-itemTpl). When tapped, the configured [closeHandler](https://bryntum.com/docs/gantt/api/#Core/widget/ChipView#config-closeHandler) is called passing the associated record.

Chips may also be selected using the `LEFT` and `RIGHT` arrows (And the `Shift` key to do multiple, contiguous selection). Pressing the `DELETE` or `BACKSPACE` key passes the selected records to the [closeHandler](https://bryntum.com/docs/gantt/api/#Core/widget/ChipView#config-closeHandler) (if not provided, the record representing the chip is removed from the store).

[iconTpl](https://bryntum.com/docs/gantt/api/Core/widget/ChipView#config-iconTpl)
A template function, which, when passed a record, returns the markup which encapsulates a chip's icon to be placed before the [itemTpl](https://bryntum.com/docs/gantt/api/#Core/widget/List#config-itemTpl).

[closeHandler](https://bryntum.com/docs/gantt/api/Core/widget/ChipView#config-closeHandler)
If [closable](https://bryntum.com/docs/gantt/api/#Core/widget/ChipView#config-closable) is `true`, this is the name of a callback function to handle what the "close" action means. If not provided, the record representing the chip is removed from the store.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isChipView](https://bryntum.com/docs/gantt/api/Core/widget/ChipView#property-isChipView)
Identifies an object as an instance of [ChipView](https://bryntum.com/docs/gantt/api/#Core/widget/ChipView) class, or subclass thereof.

[isChipView](https://bryntum.com/docs/gantt/api/Core/widget/ChipView#property-isChipView-static)
Identifies an object as an instance of [ChipView](https://bryntum.com/docs/gantt/api/#Core/widget/ChipView) class, or subclass thereof.
