cursive::view
# Trait ViewWrapper 
Source 

```
pub trait ViewWrapper:
    Send
    + Sync
    + 'static {
    type V: View + ?Sized;

    // Required methods
    fn with_view<F, R>(&self, f: F) -> Option<R>
       where F: FnOnce(&Self::V) -> R;
    fn with_view_mut<F, R>(&mut self, f: F) -> Option<R>
       where F: FnOnce(&mut Self::V) -> R;

    // Provided methods
    fn into_inner(self) -> Result<Self::V, Self>
       where Self: Sized,
             Self::V: Sized { ... }
    fn wrap_draw(&self, printer: &Printer<'_, '_>) { ... }
    fn wrap_required_size(&mut self, req: XY<usize>) -> XY<usize> { ... }
    fn wrap_on_event(&mut self, ch: Event) -> EventResult { ... }
    fn wrap_layout(&mut self, size: XY<usize>) { ... }
    fn wrap_take_focus(
        &mut self,
        source: Direction,
    ) -> Result<EventResult, CannotFocus> { ... }
    fn wrap_call_on_any(
        &mut self,
        selector: &Selector<'_>,
        callback: &mut dyn FnMut(&mut (dyn View + 'static)),
    ) { ... }
    fn wrap_focus_view(
        &mut self,
        selector: &Selector<'_>,
    ) -> Result<EventResult, ViewNotFound> { ... }
    fn wrap_needs_relayout(&self) -> bool { ... }
    fn wrap_important_area(&self, size: XY<usize>) -> Rect { ... }
}
```

## Required Associated Types§