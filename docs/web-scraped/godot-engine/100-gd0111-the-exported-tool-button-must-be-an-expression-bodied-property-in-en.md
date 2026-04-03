# GD0111: The exported tool button must be an expression-bodied property in English

# GD0111: The exported tool button must be an expression-bodied property

|  |  |
|---|---|
| Rule ID | GD0111 |
| Category | Usage |
| Fix is breaking or non-breaking | Non-breaking |
| Enabled by default | Yes |

Rule ID
GD0111
Category
Usage
Fix is breaking or non-breaking
Non-breaking
Enabled by default

## Cause

A property is annotated with the[ExportToolButton]attribute but it's not
anexpression-bodied property.

## Rule description

When reloading the .NET assembly, Godot will attempt to serialize exported
members to preserve their values. A field or a property with a backing field
that stores aCallablemay prevent the unloading of the assembly.
An expression-bodied property doesn't have a backing field and won't store
theCallable, so Godot won't attempt to serialize it, which should result
in the successful reloading of the .NET assembly.

```
[ExportToolButton("Click me!")]
public Callable ValidClickMeButton => Callable.From(ClickMe);

// Invalid because the Callable will be stored in the property's backing field.
[ExportToolButton("Click me!")]
public Callable InvalidClickMeButton { get; } = Callable.From(ClickMe);
```

## How to fix violations

To fix a violation of this rule, replace the property implementation with anexpression-bodied property.

## When to suppress warnings

Do not suppress a warning from this rule.Callableinstances may prevent
the .NET assembly from unloading.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
