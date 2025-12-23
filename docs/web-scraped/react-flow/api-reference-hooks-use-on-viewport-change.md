# Source: https://reactflow.dev/api-reference/hooks/use-on-viewport-change

# useOnViewportChange() 

[Source on GitHub ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useOnViewportChange.ts)

The `useOnViewportChange` hook lets you listen for changes to the viewport such as panning and zooming. You can provide a callback for each phase of a viewport change: `onStart`, `onChange`, and `onEnd`.

``` 
import  from 'react';
import  from '@xyflow/react';
 
function ViewportChangeLogger() );
 
  return null;
}
```

## Signature[](#signature) 

**Parameters:**

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-----------------------+
| Name                                                                                                                                                                                                                                                                                                                                              | Type                                           | Default               |
+===================================================================================================================================================================================================================================================================================================================================================+================================================+=======================+
| [](#0onstart)`[0].onStart`   | `OnViewportChange`     |                       |
|                                                                                                                                                                                                                                                                                                                                                   |                                                |                       |
|                                                                                                                                                                                                                                                                                                                                                   | ::: x:mt-2                                     |                       |
|                                                                                                                                                                                                                                                                                                                                                   | Gets called when the viewport starts changing. |                       |
|                                                                                                                                                                                                                                                                                                                                                   | :::                                            |                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-----------------------+
| [](#0onchange)`[0].onChange` | `OnViewportChange`     |                       |
|                                                                                                                                                                                                                                                                                                                                                   |                                                |                       |
|                                                                                                                                                                                                                                                                                                                                                   | ::: x:mt-2                                     |                       |
|                                                                                                                                                                                                                                                                                                                                                   | Gets called when the viewport changes.         |                       |
|                                                                                                                                                                                                                                                                                                                                                   | :::                                            |                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-----------------------+
| [](#0onend)`[0].onEnd`       | `OnViewportChange`     |                       |
|                                                                                                                                                                                                                                                                                                                                                   |                                                |                       |
|                                                                                                                                                                                                                                                                                                                                                   | ::: x:mt-2                                     |                       |
|                                                                                                                                                                                                                                                                                                                                                   | Gets called when the viewport stops changing.  |                       |
|                                                                                                                                                                                                                                                                                                                                                   | :::                                            |                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-----------------------+

**Returns:**

[](#returns)`void`

## Notes[](#notes) 

- This hook can only be used in a component that is a child of a [`<ReactFlowProvider />`](/api-reference/react-flow-provider) or a [`<ReactFlow />`](/api-reference/react-flow) component.