# Source: https://reactflow.dev/api-reference/types/viewport

# Viewport 

[Source on GitHub ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://github.com/xyflow/xyflow/blob/main/packages/system/src/types/general.ts/#L149-L153)

Internally, React Flow maintains a coordinate system that is independent of the rest of the page. The `Viewport` type tells you where in that system your flow is currently being display at and how zoomed in or out it is.

## Fields[](#fields) 

  Name                                                                                                                                                                                                                                                                                                          Type                               Default
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------- ---------
  [](#x)`x`         `number`   
  [](#y)`y`         `number`   
  [](#zoom)`zoom`   `number`   

## Notes[](#notes) 

- A `Transform` has the same properties as the viewport, but they represent different things. Make sure you don't get them muddled up or things will start to look weird!