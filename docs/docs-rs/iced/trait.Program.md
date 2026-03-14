iced
# Trait Program 
Source 

```
pub trait Program: Sized {
    type State;
    type Message: Send + 'static;
    type Theme: Base;
    type Renderer: Renderer;
    type Executor: Executor;

    // Required methods
    fn name() -> &'static str;
    fn settings(&self) -> Settings;
    fn window(&self) -> Option<Settings>;
    fn boot(&self) -> (Self::State, Task<Self::Message>);
    fn update(
        &self,
        state: &mut Self::State,
        message: Self::Message,
    ) -> Task<Self::Message>;
    fn view<'a>(
        &self,
        state: &'a Self::State,
        window: Id,
    ) -> Element<'a, Self::Message, Self::Theme, Self::Renderer>;

    // Provided methods
    fn title(&self, _state: &Self::State, _window: Id) -> String { ... }
    fn subscription(&self, _state: &Self::State) -> Subscription<Self::Message> { ... }
    fn theme(&self, _state: &Self::State, _window: Id) -> Option<Self::Theme> { ... }
    fn style(&self, _state: &Self::State, theme: &Self::Theme) -> Style { ... }
    fn scale_factor(&self, _state: &Self::State, _window: Id) -> f32 { ... }
    fn presets(&self) -> &[Preset<Self::State, Self::Message>] { ... }
}
```

## Required Associated Types§