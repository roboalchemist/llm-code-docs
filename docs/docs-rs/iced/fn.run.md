iced
# Function run 
Source 

```
pub fn run<State, Message, Theme, Renderer>(
    update: impl UpdateFn<State, Message> + 'static,
    view: impl for<'a> ViewFn<'a, State, Message, Theme, Renderer> + 'static,
) -> Resultwhere
    State: Default + 'static,
    Message: Send + MaybeDebug + MaybeClone + 'static,
    Theme: Base + 'static,
    Renderer: Renderer + 'static,
```