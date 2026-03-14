# Source: https://docs.ivy.app/widgets/inputs/color-input.md

# ColorInput

*Select colors visually with an intuitive color picker [interface](../../01_Onboarding/02_Concepts/02_Views.md) that returns values suitable for [styling](../../01_Onboarding/02_Concepts/02_Views.md) and [theming](../../01_Onboarding/02_Concepts/12_Theming.md) applications.*

The `ColorInput` [widget](../../01_Onboarding/02_Concepts/03_Widgets.md) provides a color picker interface for selecting color values. It allows users to visually choose colors and returns the selected color in a format suitable for use in styles and [themes](../../01_Onboarding/02_Concepts/12_Theming.md).

## Basic Usage

Here's a simple example of a `ColorInput` that updates a [state](../../03_Hooks/02_Core/03_UseState.md) with the selected color:

```csharp
public class ColorDemo : ViewBase
{
    public override object? Build()
    {    
        var colorState = UseState("#ff0000");
        return colorState.ToColorInput();
    }   
}
```

### Using the Non-Generic Constructor

For convenience, you can create a `ColorInput` without specifying the generic type, which defaults to `string`:

```csharp
// Using the non-generic constructor (defaults to string)
var colorInput = new ColorInput();

// With placeholder
var colorInputWithPlaceholder = new ColorInput("Choose a color");

// With all options
var colorInputFull = new ColorInput(
    placeholder: "Select your favorite color",
    disabled: false,
    variant: ColorInputVariants.TextAndPicker
);
```

## Variants

`ColorInput` has four variants:

| Variant | Description |
|---------|-------------|
| `ColorInputVariants.Text` | Text input for entering hex codes manually |
| `ColorInputVariants.Picker` | Color picker only |
| `ColorInputVariants.TextAndPicker` | Text input with color picker (default) |
| `ColorInputVariants.Swatch` | Grid of predefined colors from `Colors` enum |

The following code shows all variants in action:

```csharp
public class ColorVariantsDemo : ViewBase
{
    public override object? Build()
    {    
        var colorState = UseState("red");
        return Layout.Grid().Columns(2).ColumnWidths(Size.Units(30), null)
            | Text.P("Just Text").Small() | colorState.ToColorInput().Variant(ColorInputVariants.Text)
            | Text.P("Just Picker").Small() | colorState.ToColorInput().Variant(ColorInputVariants.Picker)
            | Text.P("Text and Picker").Small() | colorState.ToColorInput().Variant(ColorInputVariants.TextAndPicker)
            | Text.P("Swatch").Small() | colorState.ToColorInput().Variant(ColorInputVariants.Swatch);
    }   
}
```

### Swatch Variant

The `Swatch` variant displays a grid of predefined colors from the `Colors` enum. This is useful when you want users to select from a specific set of theme-aware colors rather than arbitrary hex values.

```csharp
public class ColorSwatchDemo : ViewBase
{
    public override object? Build()
    {    
        var colorState = UseState(Colors.Blue);
        return Layout.Vertical()
            | colorState.ToColorInput().Variant(ColorInputVariants.Swatch)
            | Text.P($"Selected: {colorState.Value}");
    }   
}
```

## Event Handling

ColorInput can handle change events using the `onChange` parameter.
The following demo shows how the `Picker` variant can be used with a code
block so that

```csharp
public class ColorChangedDemo : ViewBase
{

    public override object? Build()
    {    
        var colorState = UseState("#ff0000");
        var colorName = UseState(colorState.Value);
        var onChangeHandler = (Event<IInput<string>, string> e) =>
        {
            colorName.Set(e.Value);
            colorState.Set(e.Value);
        };
        return Layout.Vertical() 
                | H3("Hex Color Picker")
                | (Layout.Horizontal()
                | new ColorInput<string>
                       (colorState.Value, onChangeHandler)
                      .Variant(ColorInputVariants.Picker) 
                | new CodeBlock(colorName.Value)
                    .ShowCopyButton()
                    .ShowBorder());
    }    
}    
```

## Styling

`ColorInput` can be customized with various styling options, such as setting a placeholder or disabling the input.

```csharp
public class ColorStylingDemo : ViewBase
{
    public override object? Build()
    {
        var colorState = UseState("#ff0000");
        return Layout.Grid().Columns(2).ColumnWidths(Size.Units(30), null)
            | Text.P("Disabled").Small() | colorState.ToColorInput().Disabled()
            | Text.P("Invalid").Small() | colorState.ToColorInput().Invalid("Invalid color value");
    }
}
```


## API

[View Source: ColorInput.cs](https://github.com/Ivy-Interactive/Ivy-Framework/blob/main/src/Ivy/Widgets/Inputs/ColorInput.cs)

### Constructors

| Signature |
|-----------|
| `new ColorInput(IAnyState state, string placeholder = null, bool disabled = false, ColorInputVariants variant = ColorInputVariants.TextAndPicker)` |
| `new ColorInput(string value, Func<Event<IInput<string>, string>, ValueTask> onChange, string placeholder = null, bool disabled = false, ColorInputVariants variant = ColorInputVariants.TextAndPicker)` |
| `new ColorInput(string value, Action<Event<IInput<string>, string>> onChange, string placeholder = null, bool disabled = false, ColorInputVariants variant = ColorInputVariants.TextAndPicker)` |
| `new ColorInput(string placeholder = null, bool disabled = false, ColorInputVariants variant = ColorInputVariants.TextAndPicker)` |
| `ToColorInput(IAnyState state, string placeholder = null, bool disabled = false, ColorInputVariants? variant = null)` |


### Supported Types

| Group | Type | Nullable |
|-------|------|----------|
| Text | `string` | - |
| Enum | `Colors` | `Colors?` |


### Properties

| Name | Type | Setters |
|------|------|---------|
| `Disabled` | `bool` | `Disabled` |
| `Foreground` | `bool?` | `Foreground` |
| `Height` | `Size` | - |
| `Invalid` | `string` | `Invalid` |
| `Nullable` | `bool` | `Nullable` |
| `Placeholder` | `string` | `Placeholder` |
| `Scale` | `Scale?` | - |
| `Value` | `string` | `Value` |
| `Variant` | `ColorInputVariants` | `Variant` |
| `Visible` | `bool` | - |
| `Width` | `Size` | - |


### Events

| Name | Type | Handlers |
|------|------|----------|
| `OnBlur` | `EventHandler<Event<IAnyInput>>` | `OnBlur` |
| `OnChange` | `EventHandler<Event<IInput<string>, string>>` | - |




## Examples


### ColorPicker control can be used in a developer tool setting that generates CSS blocks.

```csharp
public class CSSColorDemo : ViewBase
{
    public override object? Build()
    {
        var color = UseState("#333333");
        var bgColor = UseState("#F5F5F5");
        var border = UseState("#CCCCCC");
        var template = """
                     .my-element {
                            color: [COLOR];
                            background-color: [BG_COLOR];
                            border: 1px solid [BORDER];
                      }
        """;
        var genCode = UseState("");
        genCode.Set(template.Replace("[COLOR]",color.Value)
                            .Replace("[BG_COLOR]",bgColor.Value)
                            .Replace("[BORDER]",border.Value));
        return Layout.Vertical()
                | H3("CSS Block Generator")
                | (Layout.Horizontal()
                   | Text.InlineCode("color")
                         .Width(35)
                   | color.ToColorInput()
                          .Variant(ColorInputVariants.Picker))
                | (Layout.Horizontal()
                   | Text.InlineCode("background-color")
                         .Width(35)
                   | bgColor.ToColorInput()
                          .Variant(ColorInputVariants.Picker))
                | (Layout.Horizontal()
                   | Text.InlineCode("border")
                         .Width(35)
                   | border.ToColorInput()
                          .Variant(ColorInputVariants.Picker))
                   | new CodeBlock(genCode.Value)
                         .Language(Languages.Css)
                         .ShowCopyButton();
    }
}
```