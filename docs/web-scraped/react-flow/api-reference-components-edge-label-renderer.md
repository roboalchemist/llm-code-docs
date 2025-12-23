# Source: https://reactflow.dev/api-reference/components/edge-label-renderer

# \<EdgeLabelRenderer /\> 

[Source on GitHub ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/xyflow/xyflow/blob/main/packages/react/src/components/EdgeLabelRenderer/index.tsx)

Edges are SVG-based. If you want to render more complex labels you can use the `<EdgeLabelRenderer />` component to access a div based renderer. This component is a portal that renders the label in a `<div />` that is positioned on top of the edges. You can see an example usage of the component in the [edge label renderer](/examples/edges/edge-label-renderer) example.

``` 
import React from 'react';
import  from '@xyflow/react';
 
const CustomEdge = () =>  path= />
      <EdgeLabelRenderer>
        <div
          style=px,$px)`,
            background: '#ffcc00',
            padding: 10,
            borderRadius: 5,
            fontSize: 12,
            fontWeight: 700,
          }}
          className="nodrag nopan"
        >
          
        </div>
      </EdgeLabelRenderer>
    </>
  );
};
 
export default CustomEdge;
```

## Props[](#props) 

  Name                                                                                                                                                                                                                                                                                                                  Type                                                                                                                                                                                                                                                                                                                                                        Default
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------
  [](#children)`children`   [`ReactNode`](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/d7e13a7c7789d54cf8d601352517189e82baf502/types/react/index.d.ts#L264)   

## Notes[](#notes) 

- The `<EdgeLabelRenderer />` has no pointer events by default. If you want to add mouse interactions you need to set the style `pointerEvents: 'all'` and add the `nopan` class on the label or the element you want to interact with.