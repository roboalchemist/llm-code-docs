# Source: https://docs.syncfusion.com/windowsforms/commandbar/faq/why-is-it-not-possible-to-add-a-commandbarcontroller-to-a-form-containing-xp-menus-and-toolbars.md

# Why is it not possible to add a CommandBarController to a form containing XP Menus and ToolBars?

The CommandBars Framework should be used only with the standard .NET Menus/ToolBars and not with the Essential Tools XP Menus. This is because the XP Menus designer infrastructure will freeze the .NET environment.

![Menu with command bar](Frequently-Asked-Questions-Images/Getting-Started_img8.jpeg)

But it is possible to add a CommandBar to a form containing XP Menus through code as shown in the sample screenshot.