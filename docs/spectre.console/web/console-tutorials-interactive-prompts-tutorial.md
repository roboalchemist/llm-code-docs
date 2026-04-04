# Source: https://spectreconsole.net/console/tutorials/interactive-prompts-tutorial

Title: Spectre.Console Documentation - Asking User Questions

URL Source: https://spectreconsole.net/console/tutorials/interactive-prompts-tutorial

Markdown Content:
In this tutorial, we'll build a pizza ordering system that collects user input. By the end, you'll know how to ask for text, let users choose from lists, and confirm their selections.

Caution

Prompts are not thread safe. Using them together with other interactive components such as progress displays, status displays, or other prompts is not supported.

1.   1
**Ask for the Customer's Name**

Let's start by asking for the customer's name. The `Ask<string>()` method displays a prompt and waits for input:

```
var name = AnsiConsole.Ask<string>("What's your [green]name[/]?");
AnsiConsole.MarkupLine($"Welcome, [blue]{name}[/]!");
``` 
Run the code:

```
dotnet run
``` 
"What's your name?" appears with a cursor waiting for input. Type your name and press Enter. The program then greets you by name.

See how we used `[green]` markup in the prompt? You can style your prompts just like any other Spectre.Console output.

You've captured your first user input.

2.   2
**Choose a Pizza Size**

Now let's let the user pick from a list of options. A `SelectionPrompt` shows an interactive menu where users navigate with arrow keys:

```
var size = AnsiConsole.Prompt(
    new SelectionPrompt<string>()
        .Title("What [green]size pizza[/] would you like?")
        .AddChoices("Small", "Medium", "Large", "Extra Large"));
  
AnsiConsole.MarkupLine($"You selected: [yellow]{size}[/]");
``` 
Run it:

```
dotnet run
``` 
A list of pizza sizes appears with one highlighted. Use the up/down arrow keys to move between options, then press Enter to select.

The prompt handles all the keyboard interaction - no need to parse input or validate choices. Spectre.Console takes care of it.

An interactive menu with just a few lines of code.

3.   3
**Select Your Toppings**

What if the user wants to pick multiple items? That's where `MultiSelectionPrompt` comes in. Users can toggle items with the spacebar and confirm with Enter:

```
var toppings = AnsiConsole.Prompt(
    new MultiSelectionPrompt<string>()
        .Title("What [green]toppings[/] would you like?")
        .NotRequired()
        .InstructionsText("[grey](Press [blue]<space>[/] to toggle, [green]<enter>[/] to confirm)[/]")
        .AddChoices("Pepperoni", "Mushrooms", "Sausage",
                    "Onions", "Green Peppers", "Black Olives",
                    "Extra Cheese", "Bacon", "Pineapple"));
  
if (toppings.Count == 0)
{
    AnsiConsole.MarkupLine("A plain cheese pizza - classic choice!");
}
else
{
    AnsiConsole.MarkupLine($"Toppings: [yellow]{string.Join(", ", toppings)}[/]");
}
``` 
Run it:

```
dotnet run
``` 
A list of toppings appears with checkboxes. Press Space to select or deselect items, use arrow keys to navigate, and press Enter when you're done.

The `NotRequired()` call allows zero items to be selected (for a plain cheese pizza). Without it, at least one selection would be required.

Your users can now make multiple selections.

4.   4
**Confirm the Order**

Before placing the order, let's ask for confirmation. The `Confirm()` method presents a simple yes/no question:

```
var confirmed = AnsiConsole.Confirm("Place this order?");
  
if (confirmed)
{
    AnsiConsole.MarkupLine("[green]Order placed![/]");
}
else
{
    AnsiConsole.MarkupLine("[yellow]Order cancelled.[/]");
}
``` 
Run it:

```
dotnet run
``` 
"Place this order? [y/n]" appears with options to type `y` or `n`. The method returns `true` for yes and `false` for no.

The `[y/n]` hint is automatically added - Spectre.Console handles common UX patterns for you.

Now you can get confirmation before important actions.

5.   5
**Complete Pizza Order**

Let's put it all together into a complete ordering flow with a styled order summary:

```
AnsiConsole.MarkupLine("[bold yellow]Welcome to Spectre Pizza![/]");
AnsiConsole.WriteLine();
  
// Ask for name
var name = AnsiConsole.Ask<string>("What's your [green]name[/]?");
  
// Choose size
var size = AnsiConsole.Prompt(
    new SelectionPrompt<string>()
        .Title("What [green]size pizza[/] would you like?")
        .AddChoices("Small", "Medium", "Large", "Extra Large"));
  
// Select toppings
var toppings = AnsiConsole.Prompt(
    new MultiSelectionPrompt<string>()
        .Title("What [green]toppings[/] would you like?")
        .NotRequired()
        .InstructionsText("[grey](Press [blue]<space>[/] to toggle, [green]<enter>[/] to confirm)[/]")
        .AddChoices("Pepperoni", "Mushrooms", "Sausage",
            "Onions", "Green Peppers", "Black Olives",
            "Extra Cheese", "Bacon", "Pineapple"));
  
// Show order summary
AnsiConsole.WriteLine();
var panel = new Panel(
        new Rows(
            new Markup($"[bold]Customer:[/] {name}"),
            new Markup($"[bold]Size:[/]     {size}"),
            new Markup($"[bold]Toppings:[/] {(toppings.Count > 0 ? string.Join(", ", toppings) : "Plain cheese")}")))
    .Header("[yellow]Order Summary[/]")
    .Border(BoxBorder.Rounded);
AnsiConsole.Write(panel);
AnsiConsole.WriteLine();
  
// Confirm order
if (AnsiConsole.Confirm("Place this order?"))
{
    AnsiConsole.MarkupLine($"[green]Order placed! Thanks, {name}![/]");
}
else
{
    AnsiConsole.MarkupLine("[yellow]Order cancelled.[/]");
}
``` 
Run the complete application:

```
dotnet run
``` 
The full ordering experience unfolds: enter your name, pick a size, select toppings, review the summary in a styled panel, and confirm your order.

We used a `Panel` to display the order summary - combining prompts with other Spectre.Console widgets creates polished, professional interfaces.

A complete interactive ordering flow.

You've created a pizza ordering system that demonstrates all the core prompting features. Your application asks for text input, presents single-choice and multiple-choice menus, displays a styled summary, and confirms the order before processing.

Use these prompts in configuration wizards, CLI tools, installation scripts, and anywhere you need user input.
