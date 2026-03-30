iocraft::components
# Struct ButtonProps 
Source 

```
#[non_exhaustive]pub struct ButtonProps<'a> {
    pub children: Vec<AnyElement<'a>>,
    pub handler: HandlerMut<'static, ()>,
    pub has_focus: bool,
}
```

## Fields (Non-exhaustive)§
§`children: Vec<AnyElement<'a>>`

The children of the component. Exactly one child is expected.
§`handler: HandlerMut<'static, ()>`

The handler to invoke when the button is triggered.

The button can be triggered two ways:

- By clicking on it with the mouse while in fullscreen mode.

- By pressing the Enter or Space key while `has_focus` is `true`.

§`has_focus: bool`

True if the button has focus and should process keyboard input.

## Trait Implementations§