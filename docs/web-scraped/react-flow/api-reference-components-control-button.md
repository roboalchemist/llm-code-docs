# Source: https://reactflow.dev/api-reference/components/control-button

# \<ControlButton /\> 

[Source on GitHub ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/xyflow/xyflow/blob/main/packages/react/src/additional-components/Controls/ControlButton.tsx)

You can add buttons to the control panel by using the `<ControlButton />` component and pass it as a child to the [`<Controls />`](/api-reference/components/controls) component.

``` 
import  from '@radix-ui/react-icons'
import  from '@xyflow/react'
 
export default function Flow()  edges=>
      <Controls>
        <ControlButton onClick=>
          <MagicWand />
        </ControlButton>
      </Controls>
    </ReactFlow>
  )
}
```

## Props[](#props) 

The `<ControlButton />` component accepts any prop valid on a HTML `<button />` element.

  Name                                                                                                                                                                                                                                                                                                               Type                                                                Default
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------- ---------
  [](#props)`...props`   `ButtonHTMLAttributes<HTMLButtonElement>`