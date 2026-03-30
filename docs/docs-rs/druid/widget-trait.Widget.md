druid::widget

# Trait Widget

Source

```
pub trait Widget<T> {
    // Required methods
    fn event(
        &mut self,
        ctx: &mut EventCtx<'_, '_>,
        event: &Event,
        data: &mut T,
        env: &Env,
    );
    fn lifecycle(
        &mut self,
        ctx: &mut LifeCycleCtx<'_, '_>,
        event: &LifeCycle,
        data: &T,
        env: &Env,
    );
    fn update(
        &mut self,
        ctx: &mut UpdateCtx<'_, '_>,
        old_data: &T,
        data: &T,
        env: &Env,
    );
    fn layout(
        &mut self,
        ctx: &mut LayoutCtx<'_, '_>,
        bc: &BoxConstraints,
        data: &T,
        env: &Env,
    ) -> Size;
    fn paint(&mut self, ctx: &mut PaintCtx<'_, '_, '_>, data: &T, env: &Env);

    // Provided method
    fn compute_max_intrinsic(
        &mut self,
        axis: Axis,
        ctx: &mut LayoutCtx<'_, '_>,
        bc: &BoxConstraints,
        data: &T,
        env: &Env,
    ) -> f64 { ... }
}
```

## Required Methods§
