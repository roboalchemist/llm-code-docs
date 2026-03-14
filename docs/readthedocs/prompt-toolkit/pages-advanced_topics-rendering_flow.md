# The rendering flow

Understanding the rendering flow is important for understanding how
`Container` and
`UIControl` objects interact. We will demonstrate
it by explaining the flow around a
`BufferControl`.

Note

A `BufferControl` is a
`UIControl` for displaying the content of a
`Buffer`. A buffer is the object that holds
any editable region of text. Like all controls, it has to be wrapped into a
`Window`.