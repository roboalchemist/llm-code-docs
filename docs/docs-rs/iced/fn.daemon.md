iced
# Function daemon 
Source 

```
pub fn daemon<State, Message, Theme, Renderer>(
    boot: impl BootFn<State, Message>,
    update: impl UpdateFn<State, Message>,
    view: impl for<'a> ViewFn<'a, State, Message, Theme, Renderer>,
) -> Daemon<impl Program<State = State, Message = Message, Theme = Theme>>where
    State: 'static,
    Message: Send + 'static,
    Theme: Base,
    Renderer: Renderer,
```