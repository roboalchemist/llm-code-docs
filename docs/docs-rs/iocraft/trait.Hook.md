iocraft
# Trait Hook 
Source 

```
pub trait Hook: Unpin + Send {
    // Provided methods
    fn poll_change(self: Pin<&mut Self>, _cx: &mut Context<'_>) -> Poll<()> { ... }
    fn pre_component_update(
        &mut self,
        _updater: &mut ComponentUpdater<'_, '_, '_>,
    ) { ... }
    fn post_component_update(
        &mut self,
        _updater: &mut ComponentUpdater<'_, '_, '_>,
    ) { ... }
    fn pre_component_draw(&mut self, _drawer: &mut ComponentDrawer<'_>) { ... }
    fn post_component_draw(&mut self, _drawer: &mut ComponentDrawer<'_>) { ... }
}
```

## Provided Methods§