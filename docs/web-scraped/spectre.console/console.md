# Source: https://spectreconsole.net/console

Title: Spectre.Console Documentation - Spectre.Console Documentation

URL Source: https://spectreconsole.net/console

Markdown Content:
Create beautiful, cross-platform console applications with Spectre.Console.

Start Here
----------

Get Spectre.Console running in seconds:

```
dotnet add package Spectre.Console
```

Then try this quick example that demonstrates styled text, a table, and a status spinner:

```
// Styled text with markup
AnsiConsole.MarkupLine("[bold blue]Welcome[/] to [green]Spectre.Console[/]!");
  
// A simple table
var table = new Table()
    .AddColumn("Feature")
    .AddColumn("Description")
    .AddRow("[green]Markup[/]", "Rich text with colors and styles")
    .AddRow("[blue]Tables[/]", "Structured data display")
    .AddRow("[yellow]Progress[/]", "Spinners and progress bars");
AnsiConsole.Write(table);
  
// Status spinner for work
AnsiConsole.Status()
    .Start("Processing...", ctx =>
    {
        Thread.Sleep(2500);
    });
  
AnsiConsole.MarkupLine("[green]Done![/]");
```

Your application should look something like this:

![Image 1: Screencast of Spectre.Console in action](https://spectreconsole.net/assets/quickstart.svg)

* * *

Explore the Documentation
-------------------------

Whether you're just getting started or looking to master advanced features, we've organized everything to help you find what you need. Start with the tutorials to build a solid foundation, then dive into specific topics as your projects grow.

Tutorials
---------

*   [Building a Rich Console App](https://spectreconsole.net/console/tutorials/getting-started-building-rich-console-app) - A beginner-friendly tutorial that walks through creating a simple console application using Spectre.Console
*   [Asking User Questions](https://spectreconsole.net/console/tutorials/interactive-prompts-tutorial) - Learn to ask the user simple questions and use their answers
*   [Showing Status and Spinners](https://spectreconsole.net/console/tutorials/status-spinners-tutorial) - Display animated spinners while operations are running
*   [Showing Progress Bars](https://spectreconsole.net/console/tutorials/progress-bars-tutorial) - A beginner-friendly tutorial that walks through creating animated progress bars to track long-running operations
*   [Creating a Custom IRenderable](https://spectreconsole.net/console/tutorials/creating-custom-renderables-tutorial) - Build a reusable Pill widget by implementing the IRenderable interface

How-To Guides
-------------

*   [Prompt for User Input](https://spectreconsole.net/console/how-to/prompting-for-user-input) - Collect input from users with text prompts, confirmations, and selection menus
*   [Display Tabular Data](https://spectreconsole.net/console/how-to/displaying-tabular-data) - Display structured data in tables with borders, alignment, and styling
*   [Show Progress Bars](https://spectreconsole.net/console/how-to/showing-progress-bars) - Display progress bars for long-running operations with percentage completion
*   [Show Activity Status](https://spectreconsole.net/console/how-to/showing-activity-status) - Display a spinner for operations without measurable progress
*   [Escape Markup](https://spectreconsole.net/console/how-to/escaping-markup) - Safely display user input, array indexers, and JSON without markup parsing errors
*   [Write Exceptions](https://spectreconsole.net/console/how-to/writing-exceptions) - Display formatted exception details with stack traces, colors, and clickable links
*   [Display Hierarchical Data](https://spectreconsole.net/console/how-to/displaying-hierarchical-data) - Visualize nested structures using tree views with customizable styling
*   [Organize Layout](https://spectreconsole.net/console/how-to/organizing-layout-with-panels-and-grids) - Arrange content using panels, columns, grids, and alignment
*   [Update Content Live](https://spectreconsole.net/console/how-to/live-rendering-and-dynamic-updates) - Update console output in-place without scrolling
*   [Run Tasks with a Spinner](https://spectreconsole.net/console/how-to/running-tasks-with-async-spinner) - Show a spinner animation while awaiting async operations
*   [Draw Charts](https://spectreconsole.net/console/how-to/drawing-charts-and-diagrams) - Visualize data with bar charts, breakdown charts, and calendars
*   [Test Console Output](https://spectreconsole.net/console/how-to/testing-console-output) - Write unit tests for console applications using TestConsole
*   [Create Custom Renderables](https://spectreconsole.net/console/how-to/creating-custom-renderables) - Build your own widgets by implementing IRenderable
*   [Write ANSI](https://spectreconsole.net/console/how-to/writing-ansi) - How to write ANSI/VT sequences and markup without the Spectre.Console library

Widgets
-------

*   [Text Widget](https://spectreconsole.net/console/widgets/text) - Render styled text with precise control over formatting and overflow
*   [Markup Widget](https://spectreconsole.net/console/widgets/markup) - Render styled text using an inline markup syntax
*   [Panel Widget](https://spectreconsole.net/console/widgets/panel) - Create bordered boxes around content with customizable headers, padding, and styles
*   [TextPath Widget](https://spectreconsole.net/console/widgets/text-path) - Display file paths with intelligent truncation and component styling
*   [Table Widget](https://spectreconsole.net/console/widgets/table) - Display tabular data with customizable columns, rows, borders, and styling
*   [Tree Widget](https://spectreconsole.net/console/widgets/tree) - Display hierarchical data structures with expandable tree views
*   [Columns Widget](https://spectreconsole.net/console/widgets/columns) - Display content side-by-side in columns with automatic width distribution
*   [Rule Widget](https://spectreconsole.net/console/widgets/rule) - Create horizontal dividers and section separators with optional titles
*   [Grid Widget](https://spectreconsole.net/console/widgets/grid) - Arrange content in rows and columns without visible borders for flexible layouts
*   [Rows Widget](https://spectreconsole.net/console/widgets/rows) - Stack multiple renderables vertically with consistent spacing
*   [Layout Widget](https://spectreconsole.net/console/widgets/layout) - Create complex multi-section layouts with the flexible Layout widget
*   [Padder Widget](https://spectreconsole.net/console/widgets/padder) - Add padding around any renderable content
*   [Align Widget](https://spectreconsole.net/console/widgets/align) - Control horizontal and vertical alignment of content
*   [FigletText Widget](https://spectreconsole.net/console/widgets/figlet) - Create large ASCII art text banners using FIGlet fonts
*   [BarChart Widget](https://spectreconsole.net/console/widgets/bar-chart) - Display data as horizontal bars with labels, values, and colors
*   [BreakdownChart Widget](https://spectreconsole.net/console/widgets/breakdown-chart) - Display proportional data as a colored bar chart with optional legend
*   [Calendar Widget](https://spectreconsole.net/console/widgets/calendar) - Display monthly calendars with highlighted dates and events
*   [JsonText Widget](https://spectreconsole.net/console/widgets/json) - Render JSON data with syntax highlighting and customizable colors
*   [Canvas Widget](https://spectreconsole.net/console/widgets/canvas) - Draw pixel-level graphics and patterns in the console
*   [CanvasImage Widget](https://spectreconsole.net/console/widgets/canvas-image) - Display image files in the console using pixel-based rendering

Prompts
-------

*   [TextPrompt](https://spectreconsole.net/console/prompts/text-prompt) - Prompt users for text input with validation and default values
*   [SelectionPrompt](https://spectreconsole.net/console/prompts/selection-prompt) - Let users select a single option from a list with keyboard navigation
*   [MultiSelectionPrompt](https://spectreconsole.net/console/prompts/multi-selection-prompt) - Allow users to select multiple options from a list

Live Rendering
--------------

*   [Progress Display](https://spectreconsole.net/console/live/progress) - Show progress bars and task status for long-running operations
*   [Status Display](https://spectreconsole.net/console/live/status) - Show animated status indicators with spinners for ongoing operations
*   [Live Display](https://spectreconsole.net/console/live/live-display) - Update and refresh any renderable content dynamically in real-time

Explanation
-----------

*   [Understanding Spectre.Console's Rendering Model](https://spectreconsole.net/console/explanation/understanding-rendering-model) - An in-depth explanation of how Spectre.Console renders text and widgets to the terminal

Reference
---------

*   [Color Reference](https://spectreconsole.net/console/reference/color-reference) - A comprehensive reference of color usage in Spectre.Console
*   [Markup Reference](https://spectreconsole.net/console/reference/markup-reference) - Complete reference for Spectre.Console's inline markup syntax including tags, colors, styles, links, and escaping
*   [Box Border Reference](https://spectreconsole.net/console/reference/box-border-reference) - A complete reference of all box border styles available in Spectre.Console
*   [Text Style Reference](https://spectreconsole.net/console/reference/text-style-reference) - A comprehensive reference of text styles and decoration options in Spectre.Console
*   [Capabilities Reference](https://spectreconsole.net/console/reference/capabilities-reference) - Complete reference for terminal capabilities, environment variables, and CI detection in Spectre.Console
*   [Table Border Reference](https://spectreconsole.net/console/reference/table-border-reference) - A complete reference of all table border styles available in Spectre.Console
*   [Spinner Styles Reference](https://spectreconsole.net/console/reference/spinner-reference) - A reference of built-in spinner animations available for the Status and Spinner APIs
*   [Tree Guide Reference](https://spectreconsole.net/console/reference/tree-guide-reference) - A complete reference of all tree guide styles available in Spectre.Console
*   [Emoji Reference](https://spectreconsole.net/console/reference/emoji-reference) - A list of all emoji shortcodes supported by Spectre.Console's Markup
