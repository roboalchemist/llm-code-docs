# Source: https://spectreconsole.net/console/tutorials/creating-custom-renderables-tutorial

Title: Spectre.Console Documentation - Creating a Custom IRenderable

URL Source: https://spectreconsole.net/console/tutorials/creating-custom-renderables-tutorial

Markdown Content:
Spectre.Console Documentation - Creating a Custom IRenderable
===============

[Spectre.Console](https://spectreconsole.net/)

[Home](https://spectreconsole.net/)[Console](https://spectreconsole.net/console)[CLI](https://spectreconsole.net/cli)[Blog](https://spectreconsole.net/blog)[GitHub](https://github.com/spectreconsole)[Discord](https://discord.gg/DxqCxpmA2K)

 Search 

[Home](https://spectreconsole.net/)[Console](https://spectreconsole.net/console)[CLI](https://spectreconsole.net/cli)[Blog](https://spectreconsole.net/blog)

[GitHub](https://github.com/spectreconsole)[Discord](https://discord.gg/DxqCxpmA2K)

*   Tutorials 
    *   [Building a Rich Console App](https://spectreconsole.net/console/tutorials/getting-started-building-rich-console-app)
    *   [Asking User Questions](https://spectreconsole.net/console/tutorials/interactive-prompts-tutorial)
    *   [Showing Status and Spinners](https://spectreconsole.net/console/tutorials/status-spinners-tutorial)
    *   [Showing Progress Bars](https://spectreconsole.net/console/tutorials/progress-bars-tutorial)
    *   [Creating a Custom IRenderable](https://spectreconsole.net/console/tutorials/creating-custom-renderables-tutorial)

*   How-To 
    *   [Prompt for User Input](https://spectreconsole.net/console/how-to/prompting-for-user-input)
    *   [Display Tabular Data](https://spectreconsole.net/console/how-to/displaying-tabular-data)
    *   [Show Progress Bars](https://spectreconsole.net/console/how-to/showing-progress-bars)
    *   [Show Activity Status](https://spectreconsole.net/console/how-to/showing-activity-status)
    *   [Escape Markup](https://spectreconsole.net/console/how-to/escaping-markup)
    *   [Write Exceptions](https://spectreconsole.net/console/how-to/writing-exceptions)
    *   [Display Hierarchical Data](https://spectreconsole.net/console/how-to/displaying-hierarchical-data)
    *   [Organize Layout](https://spectreconsole.net/console/how-to/organizing-layout-with-panels-and-grids)
    *   [Update Content Live](https://spectreconsole.net/console/how-to/live-rendering-and-dynamic-updates)
    *   [Run Tasks with a Spinner](https://spectreconsole.net/console/how-to/running-tasks-with-async-spinner)
    *   [Draw Charts](https://spectreconsole.net/console/how-to/drawing-charts-and-diagrams)
    *   [Test Console Output](https://spectreconsole.net/console/how-to/testing-console-output)
    *   [Create Custom Renderables](https://spectreconsole.net/console/how-to/creating-custom-renderables)
    *   [Write ANSI](https://spectreconsole.net/console/how-to/writing-ansi)

*   Widgets 
    *   [Text Widget](https://spectreconsole.net/console/widgets/text)
    *   [Markup Widget](https://spectreconsole.net/console/widgets/markup)
    *   [TextPath Widget](https://spectreconsole.net/console/widgets/text-path)
    *   [Panel Widget](https://spectreconsole.net/console/widgets/panel)
    *   [Table Widget](https://spectreconsole.net/console/widgets/table)
    *   [Tree Widget](https://spectreconsole.net/console/widgets/tree)
    *   [Columns Widget](https://spectreconsole.net/console/widgets/columns)
    *   [Rule Widget](https://spectreconsole.net/console/widgets/rule)
    *   [Grid Widget](https://spectreconsole.net/console/widgets/grid)
    *   [Rows Widget](https://spectreconsole.net/console/widgets/rows)
    *   [Layout Widget](https://spectreconsole.net/console/widgets/layout)
    *   [Padder Widget](https://spectreconsole.net/console/widgets/padder)
    *   [Align Widget](https://spectreconsole.net/console/widgets/align)
    *   [FigletText Widget](https://spectreconsole.net/console/widgets/figlet)
    *   [BarChart Widget](https://spectreconsole.net/console/widgets/bar-chart)
    *   [BreakdownChart Widget](https://spectreconsole.net/console/widgets/breakdown-chart)
    *   [Calendar Widget](https://spectreconsole.net/console/widgets/calendar)
    *   [JsonText Widget](https://spectreconsole.net/console/widgets/json)
    *   [Canvas Widget](https://spectreconsole.net/console/widgets/canvas)
    *   [CanvasImage Widget](https://spectreconsole.net/console/widgets/canvas-image)

*   Live 
    *   [Progress Display](https://spectreconsole.net/console/live/progress)
    *   [Status Display](https://spectreconsole.net/console/live/status)
    *   [Live Display](https://spectreconsole.net/console/live/live-display)

*   Prompts 
    *   [TextPrompt](https://spectreconsole.net/console/prompts/text-prompt)
    *   [SelectionPrompt](https://spectreconsole.net/console/prompts/selection-prompt)
    *   [MultiSelectionPrompt](https://spectreconsole.net/console/prompts/multi-selection-prompt)

*   Explanation 
    *   [Understanding Spectre.Console's Rendering Model](https://spectreconsole.net/console/explanation/understanding-rendering-model)

*   Reference 
    *   [Color Reference](https://spectreconsole.net/console/reference/color-reference)
    *   [Markup Reference](https://spectreconsole.net/console/reference/markup-reference)
    *   [Box Border Reference](https://spectreconsole.net/console/reference/box-border-reference)
    *   [Text Style Reference](https://spectreconsole.net/console/reference/text-style-reference)
    *   [Capabilities Reference](https://spectreconsole.net/console/reference/capabilities-reference)
    *   [Table Border Reference](https://spectreconsole.net/console/reference/table-border-reference)
    *   [Tree Guide Reference](https://spectreconsole.net/console/reference/tree-guide-reference)
    *   [Spinner Styles Reference](https://spectreconsole.net/console/reference/spinner-reference)
    *   [Emoji Reference](https://spectreconsole.net/console/reference/emoji-reference)

*   Tutorials 
    *   [Building a Rich Console App](https://spectreconsole.net/console/tutorials/getting-started-building-rich-console-app)
    *   [Asking User Questions](https://spectreconsole.net/console/tutorials/interactive-prompts-tutorial)
    *   [Showing Status and Spinners](https://spectreconsole.net/console/tutorials/status-spinners-tutorial)
    *   [Showing Progress Bars](https://spectreconsole.net/console/tutorials/progress-bars-tutorial)
    *   [Creating a Custom IRenderable](https://spectreconsole.net/console/tutorials/creating-custom-renderables-tutorial)

*   How-To 
    *   [Prompt for User Input](https://spectreconsole.net/console/how-to/prompting-for-user-input)
    *   [Display Tabular Data](https://spectreconsole.net/console/how-to/displaying-tabular-data)
    *   [Show Progress Bars](https://spectreconsole.net/console/how-to/showing-progress-bars)
    *   [Show Activity Status](https://spectreconsole.net/console/how-to/showing-activity-status)
    *   [Escape Markup](https://spectreconsole.net/console/how-to/escaping-markup)
    *   [Write Exceptions](https://spectreconsole.net/console/how-to/writing-exceptions)
    *   [Display Hierarchical Data](https://spectreconsole.net/console/how-to/displaying-hierarchical-data)
    *   [Organize Layout](https://spectreconsole.net/console/how-to/organizing-layout-with-panels-and-grids)
    *   [Update Content Live](https://spectreconsole.net/console/how-to/live-rendering-and-dynamic-updates)
    *   [Run Tasks with a Spinner](https://spectreconsole.net/console/how-to/running-tasks-with-async-spinner)
    *   [Draw Charts](https://spectreconsole.net/console/how-to/drawing-charts-and-diagrams)
    *   [Test Console Output](https://spectreconsole.net/console/how-to/testing-console-output)
    *   [Create Custom Renderables](https://spectreconsole.net/console/how-to/creating-custom-renderables)
    *   [Write ANSI](https://spectreconsole.net/console/how-to/writing-ansi)

*   Widgets 
    *   [Text Widget](https://spectreconsole.net/console/widgets/text)
    *   [Markup Widget](https://spectreconsole.net/console/widgets/markup)
    *   [TextPath Widget](https://spectreconsole.net/console/widgets/text-path)
    *   [Panel Widget](https://spectreconsole.net/console/widgets/panel)
    *   [Table Widget](https://spectreconsole.net/console/widgets/table)
    *   [Tree Widget](https://spectreconsole.net/console/widgets/tree)
    *   [Columns Widget](https://spectreconsole.net/console/widgets/columns)
    *   [Rule Widget](https://spectreconsole.net/console/widgets/rule)
    *   [Grid Widget](https://spectreconsole.net/console/widgets/grid)
    *   [Rows Widget](https://spectreconsole.net/console/widgets/rows)
    *   [Layout Widget](https://spectreconsole.net/console/widgets/layout)
    *   [Padder Widget](https://spectreconsole.net/console/widgets/padder)
    *   [Align Widget](https://spectreconsole.net/console/widgets/align)
    *   [FigletText Widget](https://spectreconsole.net/console/widgets/figlet)
    *   [BarChart Widget](https://spectreconsole.net/console/widgets/bar-chart)
    *   [BreakdownChart Widget](https://spectreconsole.net/console/widgets/breakdown-chart)
    *   [Calendar Widget](https://spectreconsole.net/console/widgets/calendar)
    *   [JsonText Widget](https://spectreconsole.net/console/widgets/json)
    *   [Canvas Widget](https://spectreconsole.net/console/widgets/canvas)
    *   [CanvasImage Widget](https://spectreconsole.net/console/widgets/canvas-image)

*   Live 
    *   [Progress Display](https://spectreconsole.net/console/live/progress)
    *   [Status Display](https://spectreconsole.net/console/live/status)
    *   [Live Display](https://spectreconsole.net/console/live/live-display)

*   Prompts 
    *   [TextPrompt](https://spectreconsole.net/console/prompts/text-prompt)
    *   [SelectionPrompt](https://spectreconsole.net/console/prompts/selection-prompt)
    *   [MultiSelectionPrompt](https://spectreconsole.net/console/prompts/multi-selection-prompt)

*   Explanation 
    *   [Understanding Spectre.Console's Rendering Model](https://spectreconsole.net/console/explanation/understanding-rendering-model)

*   Reference 
    *   [Color Reference](https://spectreconsole.net/console/reference/color-reference)
    *   [Markup Reference](https://spectreconsole.net/console/reference/markup-reference)
    *   [Box Border Reference](https://spectreconsole.net/console/reference/box-border-reference)
    *   [Text Style Reference](https://spectreconsole.net/console/reference/text-style-reference)
    *   [Capabilities Reference](https://spectreconsole.net/console/reference/capabilities-reference)
    *   [Table Border Reference](https://spectreconsole.net/console/reference/table-border-reference)
    *   [Tree Guide Reference](https://spectreconsole.net/console/reference/tree-guide-reference)
    *   [Spinner Styles Reference](https://spectreconsole.net/console/reference/spinner-reference)
    *   [Emoji Reference](https://spectreconsole.net/console/reference/emoji-reference)

Creating a Custom IRenderable
=============================

Build a reusable Pill widget by implementing the IRenderable interface

In this tutorial, we'll build a Pill widget from scratch. By the end, we'll have a reusable component that displays styled labels with rounded end caps - and gracefully falls back on terminals without Unicode support.

What We're Building
-------------------

Here's the output we're creating:

![Image 1: Colored pill widgets showing Success, Warning, Error, and Info labels](https://spectreconsole.net/assets/creating-custom-renderables-tutorial.svg)

Prerequisites
-------------

*   .NET 6.0 or later
*   Completion of the [Building a Rich Console App](https://spectreconsole.net/console/tutorials/getting-started-building-rich-console-app) tutorial
*   Basic understanding of C# interfaces

1.   1
**Create the Pill Class**

Let's start by defining a `PillType` enum and creating a class that implements `IRenderable`. This interface requires two methods: `Measure()` to report size constraints and `Render()` to produce output.

```
public enum PillType
{
    Success,
    Warning,
    Error,
    Info,
}
  
public sealed class Pill : IRenderable
{
    private readonly string _text;
    private readonly Style _style;
  
    /// <summary>
    /// Creates a new pill with the specified text and type.
    /// </summary>
    /// <param name="text">The text to display inside the pill.</param>
    /// <param name="type">The pill type which determines its color scheme.</param>
    public Pill(string text, PillType type)
    {
        _text = text;
        _style = GetStyleForType(type);
    }
  
    private static Style GetStyleForType(PillType type) => type switch
    {
        PillType.Success => new Style(Color.White, Color.Green),
        PillType.Warning => new Style(Color.Black, Color.Yellow),
        PillType.Error => new Style(Color.White, Color.Red),
        PillType.Info => new Style(Color.White, Color.Blue),
        _ => new Style(Color.White, Color.Grey),
    };
  
    /// <summary>
    /// Measures the pill's width in console cells.
    /// </summary>
    public Measurement Measure(RenderOptions options, int maxWidth)
    {
        // todo
    }
  
    /// <summary>
    /// Renders the pill as a sequence of styled segments.
    /// </summary>
    public IEnumerable<Segment> Render(RenderOptions options, int maxWidth)
    {
        // todo
    }
}
```   
The `PillType` enum defines four semantic variants with predefined color schemes. The `Pill` class maps these types to styles internally, making it easy to create consistent status indicators.

Our widget skeleton is ready.

2.   2
**Implement Measure**

The `Measure()` method tells Spectre.Console how wide our pill needs to be. Containers like `Table` and `Panel` call this before rendering to calculate layouts.

```
public Measurement Measure(RenderOptions options, int maxWidth)
{
    // Width = text + 2 padding spaces + 2 cap characters
    var width = _text.Length + 4;
    return new Measurement(width, width);
}
```   
Our pill width is the text length plus 4 characters: two for padding spaces and two for the rounded cap characters. We return the same value for both minimum and maximum since our pill has a fixed width.

The measurement calculation is complete.

3.   3
**Implement Render**

The `Render()` method produces the actual output as `Segment` objects. Each segment contains text and an optional style.

```
public IEnumerable<Segment> Render(RenderOptions options, int maxWidth)
{
    // Use rounded half-circles if Unicode is supported, otherwise spaces
    const string LeftCap = "\uE0B6";
    const string RightCap = "\uE0B4";
  
    var inverseStyle = new Style(_style.Background);
  
    if (options.Capabilities.Unicode)
    {
        yield return new Segment(LeftCap, inverseStyle);
        yield return new Segment($" {_text} ", _style);
        yield return new Segment(RightCap, inverseStyle);
    }
    else
    {
        yield return new Segment($"  {_text}  ", _style);
    }
  
}
```   
We yield three segments: the left cap, the padded text, and the right cap. The `yield return` pattern lets Spectre.Console process segments efficiently without creating intermediate collections.

Notice the Unicode detection: `options.Capabilities.Unicode` tells us whether the terminal supports Unicode characters. We use `U+E0B4` and `U+E0B5` for nice rounded caps, falling back to spaces on limited terminals.

Our pill now renders with style.

4.   4
**Complete Pill Widget**

Let's put it all together with our final showcase:

```
var table = new Table()
    .Border(TableBorder.Rounded)
    .AddColumn("Status")
    .AddColumn("Message");
  
table.AddRow(new Pill("Success", PillType.Success), new Text("All systems operational"));
table.AddRow(new Pill("Warning", PillType.Warning), new Text("High memory usage detected"));
table.AddRow(new Pill("Error", PillType.Error), new Text("Database connection failed"));
table.AddRow(new Pill("Info", PillType.Info), new Text("Scheduled maintenance at 2:00 AM"));
  
console.Write(table);
```   
Run the code:

```
dotnet run
```   
Four pills appear in a row: Success (green), Warning (yellow), Error (red), and Info (blue). Each pill renders with rounded Unicode caps, proper padding, and distinct colors.

Our custom IRenderable is complete.

Congratulations!
----------------

You've built a custom `IRenderable` from scratch. Your Pill widget measures its own width, renders styled segments, detects terminal capabilities, and displays beautifully colored labels with rounded caps.

Apply this pattern to create any custom widget: badges, progress indicators, sparklines, or domain-specific visualizations. The `IRenderable` interface is the foundation of every Spectre.Console widget.

Next Steps
----------

*   [Understanding Spectre.Console's Rendering Model](https://spectreconsole.net/console/explanation/understanding-rendering-model) - Deep dive into how rendering works
*   [Create Custom Renderables](https://spectreconsole.net/console/how-to/creating-custom-renderables) - Quick reference for custom renderables
*   [Panel Widget](https://spectreconsole.net/console/widgets/panel) - See how containers use `Measure()` and `Render()`
*   [Capabilities Reference](https://spectreconsole.net/console/reference/capabilities-reference) - All detectable terminal capabilities

### On this page
