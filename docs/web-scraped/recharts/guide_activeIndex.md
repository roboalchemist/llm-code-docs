# Source: https://recharts.github.io/en-US/guide/activeIndex/

# Active Index

Recharts 2.x used to have a prop named `activeIndex` that was setting which item the user was interacting with. In version 3.0, this prop has been removed.

## Why?

Trouble is that this prop was already set internally - by Tooltip component. Things behaved weird when both the activeIndex and Tooltip were set. Unpredictable!

## What should I do instead?

[Tooltip](/en-US/api/Tooltip/) component is controlling user interaction with the chart. Use Tooltip!

Tooltip has several props that allow you to control the interaction in detail:

- `defaultIndex`: Sets the initial index of the item that is highlighted when the chart is rendered, before any user interactions
- `active`: If true, the tooltip remains active even when the user interaction has completed (for example, when user hovers over a different item)
- `content`: This prop decides what content is displayed in the tooltip. You can turn off the rendering completely by passing `content=`.
- `cursor`: Is what renders in the plot area, to draw attention to the item that is being interacted with. You can turn it off by passing `cursor=`.

## Example 1: PieChart with default index

The example below shows how to use the `defaultIndex` prop to set the initial item that is highlighted when the chart is rendered.

Also see [GitHub issue #5999 for discussion.![Link opens in new tab](data:image/svg+xml,%3c!--%20SVG%20Icon:%20Open%20in%20New%20Window%20/%20External%20Link%20-%20This%20SVG%20is%20designed%20to%20be%20placed%20next%20to%20a%20link.%20-%20The%20color%20will%20be%20inherited%20from%20the%20parent%20text%20element's%20color%20(e.g.,%20the%20link's%20color)%20because%20%60stroke%60%20is%20set%20to%20'currentColor'.%20--%3e%3csvg%20xmlns='http://www.w3.org/2000/svg'%20width='16'%20height='16'%20viewBox='0%200%2032%2024'%20fill='none'%20stroke='currentColor'%20stroke-width='2.5'%20stroke-linecap='round'%20stroke-linejoin='round'%20style='display:%20inline-block;%20vertical-align:%20middle;%20margin-left:%204px;'%20%3e%3cpath%20d='M18%2013v6a2%202%200%200%201-2%202H5a2%202%200%200%201-2-2V8a2%202%200%200%201%202-2h6'/%3e%3cpolyline%20points='15%203%2021%203%2021%209'/%3e%3cline%20x1='10'%20y1='14'%20x2='21'%20y2='3'/%3e%3c/svg%3e)](https://github.com/recharts/recharts/issues/5999)

Source codeHook inspector

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0icmVjaGFydHMtc3VyZmFjZSIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiB2aWV3Ym94PSIwIDAgMTYgMTYiPjx0aXRsZT48L3RpdGxlPjxkZXNjPjwvZGVzYz48cGF0aCBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLXRleHQtY29sb3IpIiBzdHJva2Utd2lkdGg9IjEiIHdpZHRoPSIxMCIgaGVpZ2h0PSIxMCIgeD0iMSIgeT0iMSIgcmFkaXVzPSIyIiBjbGFzcz0icmVjaGFydHMtcmVjdGFuZ2xlIiBkPSJNIDEsMwogICAgICAgICAgICBBIDIsMiwwLDAsMSwzLDEKICAgICAgICAgICAgTCA5LDEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTEsMwogICAgICAgICAgICBMIDExLDkKICAgICAgICAgICAgQSAyLDIsMCwwLDEsOSwxMQogICAgICAgICAgICBMIDMsMTEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMSw5IFoiIHN0eWxlPSJzdHJva2UtZGFzaGFycmF5OjBweCAxcHgiIC8+PHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS10ZXh0LWNvbG9yKSIgc3Ryb2tlLXdpZHRoPSIxIiB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIHg9IjUiIHk9IjUiIHJhZGl1cz0iMiIgY2xhc3M9InJlY2hhcnRzLXJlY3RhbmdsZSIgZD0iTSA1LDcKICAgICAgICAgICAgQSAyLDIsMCwwLDEsNyw1CiAgICAgICAgICAgIEwgMTMsNQogICAgICAgICAgICBBIDIsMiwwLDAsMSwxNSw3CiAgICAgICAgICAgIEwgMTUsMTMKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTMsMTUKICAgICAgICAgICAgTCA3LDE1CiAgICAgICAgICAgIEEgMiwyLDAsMCwxLDUsMTMgWiIgc3R5bGU9InN0cm9rZS1kYXNoYXJyYXk6MHB4IDFweCIgLz48L3N2Zz4=)Copy to clipboard

Edit

Open in StackBlitz

[View this example in Storybook![Link opens in new tab](data:image/svg+xml,%3c!--%20SVG%20Icon:%20Open%20in%20New%20Window%20/%20External%20Link%20-%20This%20SVG%20is%20designed%20to%20be%20placed%20next%20to%20a%20link.%20-%20The%20color%20will%20be%20inherited%20from%20the%20parent%20text%20element's%20color%20(e.g.,%20the%20link's%20color)%20because%20%60stroke%60%20is%20set%20to%20'currentColor'.%20--%3e%3csvg%20xmlns='http://www.w3.org/2000/svg'%20width='16'%20height='16'%20viewBox='0%200%2032%2024'%20fill='none'%20stroke='currentColor'%20stroke-width='2.5'%20stroke-linecap='round'%20stroke-linejoin='round'%20style='display:%20inline-block;%20vertical-align:%20middle;%20margin-left:%204px;'%20%3e%3cpath%20d='M18%2013v6a2%202%200%200%201-2%202H5a2%202%200%200%201-2-2V8a2%202%200%200%201%202-2h6'/%3e%3cpolyline%20points='15%203%2021%203%2021%209'/%3e%3cline%20x1='10'%20y1='14'%20x2='21'%20y2='3'/%3e%3c/svg%3e)](https://main--63da8268a0da9970db6992aa.chromatic.com/?path=/story/api-chart-piechart--simple)

## Example 2: BarChart with clickable items and hidden tooltip

The example below shows how to use the `trigger` prop to highlight the item that is being clicked, and how to hide the tooltip by passing `content=` and `cursor=`.

Also see [GitHub issue #6047 for discussion.![Link opens in new tab](data:image/svg+xml,%3c!--%20SVG%20Icon:%20Open%20in%20New%20Window%20/%20External%20Link%20-%20This%20SVG%20is%20designed%20to%20be%20placed%20next%20to%20a%20link.%20-%20The%20color%20will%20be%20inherited%20from%20the%20parent%20text%20element's%20color%20(e.g.,%20the%20link's%20color)%20because%20%60stroke%60%20is%20set%20to%20'currentColor'.%20--%3e%3csvg%20xmlns='http://www.w3.org/2000/svg'%20width='16'%20height='16'%20viewBox='0%200%2032%2024'%20fill='none'%20stroke='currentColor'%20stroke-width='2.5'%20stroke-linecap='round'%20stroke-linejoin='round'%20style='display:%20inline-block;%20vertical-align:%20middle;%20margin-left:%204px;'%20%3e%3cpath%20d='M18%2013v6a2%202%200%200%201-2%202H5a2%202%200%200%201-2-2V8a2%202%200%200%201%202-2h6'/%3e%3cpolyline%20points='15%203%2021%203%2021%209'/%3e%3cline%20x1='10'%20y1='14'%20x2='21'%20y2='3'/%3e%3c/svg%3e)](https://github.com/recharts/recharts/issues/6047)

Source codeHook inspector

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0icmVjaGFydHMtc3VyZmFjZSIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiB2aWV3Ym94PSIwIDAgMTYgMTYiPjx0aXRsZT48L3RpdGxlPjxkZXNjPjwvZGVzYz48cGF0aCBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLXRleHQtY29sb3IpIiBzdHJva2Utd2lkdGg9IjEiIHdpZHRoPSIxMCIgaGVpZ2h0PSIxMCIgeD0iMSIgeT0iMSIgcmFkaXVzPSIyIiBjbGFzcz0icmVjaGFydHMtcmVjdGFuZ2xlIiBkPSJNIDEsMwogICAgICAgICAgICBBIDIsMiwwLDAsMSwzLDEKICAgICAgICAgICAgTCA5LDEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTEsMwogICAgICAgICAgICBMIDExLDkKICAgICAgICAgICAgQSAyLDIsMCwwLDEsOSwxMQogICAgICAgICAgICBMIDMsMTEKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMSw5IFoiIHN0eWxlPSJzdHJva2UtZGFzaGFycmF5OjBweCAxcHgiIC8+PHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJ2YXIoLS10ZXh0LWNvbG9yKSIgc3Ryb2tlLXdpZHRoPSIxIiB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIHg9IjUiIHk9IjUiIHJhZGl1cz0iMiIgY2xhc3M9InJlY2hhcnRzLXJlY3RhbmdsZSIgZD0iTSA1LDcKICAgICAgICAgICAgQSAyLDIsMCwwLDEsNyw1CiAgICAgICAgICAgIEwgMTMsNQogICAgICAgICAgICBBIDIsMiwwLDAsMSwxNSw3CiAgICAgICAgICAgIEwgMTUsMTMKICAgICAgICAgICAgQSAyLDIsMCwwLDEsMTMsMTUKICAgICAgICAgICAgTCA3LDE1CiAgICAgICAgICAgIEEgMiwyLDAsMCwxLDUsMTMgWiIgc3R5bGU9InN0cm9rZS1kYXNoYXJyYXk6MHB4IDFweCIgLz48L3N2Zz4=)Copy to clipboard

Edit

Open in StackBlitz