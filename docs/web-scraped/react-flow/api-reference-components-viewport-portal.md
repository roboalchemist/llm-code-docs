# Source: https://reactflow.dev/api-reference/components/viewport-portal

# \<ViewportPortal /\> 

[Source on GitHub ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/xyflow/xyflow/blob/main/packages/react/src/components/ViewportPortal/index.tsx)

`<ViewportPortal />` component can be used to add components to the same viewport of the flow where nodes and edges are rendered. This is useful when you want to render your own components that adhere to the same coordinate system as the nodes & edges and are also affected by zooming and panning

``` 
import React from 'react';
import  from '@xyflow/react';
 
export default function () }
      >
        This div is positioned at [100, 100] on the flow.
      </div>
    </ViewportPortal>
  );
}
```

## Props[](#props) 

  Name                                                                                                                                                                                                                                                                                                                  Type                                                                                                                                                                                                                                                                                                                                                        Default
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------
  [](#children)`children`   [`ReactNode`](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/d7e13a7c7789d54cf8d601352517189e82baf502/types/react/index.d.ts#L264)