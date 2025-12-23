# Source: https://reactflow.dev/api-reference/hooks/use-viewport

# useViewport() 

[Source on GitHub ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/xyflow/xyflow/blob/main/packages/react/src/hooks/useViewport.ts)

The `useViewport` hook is a convenient way to read the current state of the [`Viewport`](/api-reference/types/viewport) in a component. Components that use this hook will re-render **whenever the viewport changes**.

``` 
import  from '@xyflow/react';
 
export default function ViewportDisplay()  = useViewport();
 
  return (
    <div>
      <p>
        The viewport is currently at (, ) and zoomed to .
      </p>
    </div>
  );
}
```

## Signature[](#signature) 

**Parameters:**

This function does not accept any parameters.

**Returns:**

The current viewport.

  Name                                                                                                                                                                                                                                                                                                          Type
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------
  [](#x)`x`         `number`
  [](#y)`y`         `number`
  [](#zoom)`zoom`   `number`

## Notes[](#notes) 

- This hook can only be used in a component that is a child of a [`<ReactFlowProvider />`](/api-reference/react-flow-provider) or a [`<ReactFlow />`](/api-reference/react-flow) component.