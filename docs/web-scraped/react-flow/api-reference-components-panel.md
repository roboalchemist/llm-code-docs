# Source: https://reactflow.dev/api-reference/components/panel

# \<Panel /\> 

[Source on GitHub ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/xyflow/xyflow/blob/main/packages/react/src/components/Panel/index.tsx)

The `<Panel />` component helps you position content above the viewport. It is used internally by the [`<MiniMap />`](/api-reference/components/minimap) and [`<Controls />`](/api-reference/components/controls) components.

``` 
import  from '@xyflow/react';
 
export default function Flow()  fitView>
      <Panel position="top-left">top-left</Panel>
      <Panel position="top-center">top-center</Panel>
      <Panel position="top-right">top-right</Panel>
      <Panel position="bottom-left">bottom-left</Panel>
      <Panel position="bottom-center">bottom-center</Panel>
      <Panel position="bottom-right">bottom-right</Panel>
      <Panel position="center-left">center-left</Panel>
      <Panel position="center-right">center-right</Panel>
    </ReactFlow>
  );
}
```

## Props[](#props) 

For TypeScript users, the props type for the `<Panel />` component is exported as `PanelProps`. Additionally, the `<Panel />` component accepts all props of the HTML `<div />` element.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Name                                                                                                                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                | Default                                                                     |
+==============================================================================================================================================================================================================================================================================================================================================+=====================================================================================================================================================================================================================================+=============================================================================+
| [](#position)`position` | [`PanelPosition`](/api-reference/types/panel-position) | `"top-left"` |
|                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                     |                                                                             |
|                                                                                                                                                                                                                                                                                                                                              | ::: x:mt-2                                                                                                                                                                                                                          |                                                                             |
|                                                                                                                                                                                                                                                                                                                                              | The position of the panel.                                                                                                                                                                                                          |                                                                             |
|                                                                                                                                                                                                                                                                                                                                              | :::                                                                                                                                                                                                                                 |                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| [](#props)`...props`                             | `DetailedHTMLProps<HTMLAttributes<HTMLDivElement>, HTMLDivElement>`                                                                                                                                         |                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+