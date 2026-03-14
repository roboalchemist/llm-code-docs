druid

# Trait AppDelegate

Source

```
pub trait AppDelegate<T: Data> {
    // Provided methods
    fn event(
        &mut self,
        ctx: &mut DelegateCtx<'_>,
        window_id: WindowId,
        event: Event,
        data: &mut T,
        env: &Env,
    ) -> Option<Event> { ... }
    fn command(
        &mut self,
        ctx: &mut DelegateCtx<'_>,
        target: Target,
        cmd: &Command,
        data: &mut T,
        env: &Env,
    ) -> Handled { ... }
    fn window_added(
        &mut self,
        id: WindowId,
        handle: WindowHandle,
        data: &mut T,
        env: &Env,
        ctx: &mut DelegateCtx<'_>,
    ) { ... }
    fn window_removed(
        &mut self,
        id: WindowId,
        data: &mut T,
        env: &Env,
        ctx: &mut DelegateCtx<'_>,
    ) { ... }
}
```

## Provided Methods§
