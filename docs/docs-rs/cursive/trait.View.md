cursive
# Trait View 
Source 

```
pub trait View:
    Any
    + AnyView
    + Send
    + Sync {
    // Required method
    fn draw(&self, printer: &Printer<'_, '_>);

    // Provided methods
    fn layout(&mut self, _: XY<usize>) { ... }
    fn needs_relayout(&self) -> bool { ... }
    fn required_size(&mut self, constraint: XY<usize>) -> XY<usize> { ... }
    fn on_event(&mut self, _: Event) -> EventResult { ... }
    fn call_on_any(
        &mut self,
        _: &Selector<'_>,
        _: &mut dyn FnMut(&mut (dyn View + 'static)),
    ) { ... }
    fn focus_view(
        &mut self,
        _: &Selector<'_>,
    ) -> Result<EventResult, ViewNotFound> { ... }
    fn take_focus(
        &mut self,
        source: Direction,
    ) -> Result<EventResult, CannotFocus> { ... }
    fn important_area(&self, view_size: XY<usize>) -> Rect { ... }
    fn type_name(&self) -> &'static str { ... }
}
```

## Required Methods§