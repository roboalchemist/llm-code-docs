iocraft
# Trait Component 
Source 

```
pub trait Component:
    Any
    + Send
    + Sync
    + Unpin {
    type Props<'a>: Props
       where Self: 'a;

    // Required method
    fn new(props: &Self::Props<'_>) -> Self;

    // Provided methods
    fn update(
        &mut self,
        _props: &mut Self::Props<'_>,
        _hooks: Hooks<'_, '_>,
        _updater: &mut ComponentUpdater<'_, '_, '_>,
    ) { ... }
    fn draw(&mut self, _drawer: &mut ComponentDrawer<'_>) { ... }
    fn poll_change(self: Pin<&mut Self>, _cx: &mut Context<'_>) -> Poll<()> { ... }
}
```

## Required Associated Types§