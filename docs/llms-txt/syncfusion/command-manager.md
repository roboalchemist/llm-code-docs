# Source: https://docs.syncfusion.com/wpf/diagram/commands/command-manager.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/blazor/command-manager.md

# Command Manager in Blazor SfPdfViewer Component

The PDF viewer provides support to map or bind command execution with a desired combination of key gestures.

The [PdfViewerCommandManager](https://help.syncfusion.com/cr/blazor/Syncfusion.Blazor.SfPdfViewer.PdfViewerCommandManager.html) provides support to define custom commands. These custom commands are executed when the specified key gesture is recognized.

## Command Execution
To execute custom commands, simply provide a list of keyboard shortcuts along with the corresponding actions. These actions will be triggered when the specified keyboard shortcuts are pressed.

* [Commands](https://help.syncfusion.com/cr/blazor/Syncfusion.Blazor.SfPdfViewer.KeyboardCommand.html): Defines the collection of custom keyboard shortcuts and the action names to execute in the PDF Viewer.

* [CommandExecuted](https://help.syncfusion.com/cr/blazor/Syncfusion.Blazor.SfPdfViewer.CommandExecutedEventArgs.html): Raised when a registered keyboard shortcut is detected; handle this event to perform the action.

## How to create custom command: 
Create custom keyboard commands by specifying an action name and the corresponding key gesture for the PDF Viewer.

* [ActionName](https://help.syncfusion.com/cr/blazor/Syncfusion.Blazor.SfPdfViewer.CommandExecutedEventArgs.html#Syncfusion_Blazor_SfPdfViewer_CommandExecutedEventArgs_ActionName): Specifies the name of the action to execute when the keyboard shortcut is pressed (for example, FitToWidth, FitToPage). The action name must correspond to a recognized PDF Viewer action.

* [Gesture](https://help.syncfusion.com/cr/blazor/Syncfusion.Blazor.SfPdfViewer.KeyGesture.html): Specifies the combination of [keys](https://help.syncfusion.com/cr/blazor/Syncfusion.Blazor.SfPdfViewer.KeyGesture.html#Syncfusion_Blazor_SfPdfViewer_KeyGesture_Key) and [modifiers](https://help.syncfusion.com/cr/blazor/Syncfusion.Blazor.SfPdfViewer.KeyGesture.html#Syncfusion_Blazor_SfPdfViewer_KeyGesture_Modifiers), including Control, Shift, Alt or Meta key that are utilized within the PDF viewer. On macOS, Meta maps to the Command key.

The following example registers two custom keyboard commands (FitToWidth and FitToPage) and handles them in CommandExecuted. The example uses SfPdfViewer2; use the component that matches the project version.

```cshtml

@using Syncfusion.Blazor.SfPdfViewer

<SfPdfViewer2 Height="100%"
              Width="100%"
              @ref="@pdfViewer"
              DocumentPath="@DocumentPath">
    <PdfViewerEvents CommandExecuted="@CommandExecute"></PdfViewerEvents>
    <PdfViewerCommandManager Commands="@command" ></PdfViewerCommandManager>                
</SfPdfViewer2>

@code {
    // Reference to the Pdf viewer 
    SfPdfViewer2 pdfViewer;
    public string DocumentPath { get; set; } = "wwwroot/Data/PDF_Succinctly.pdf";

â¯ â¯ /// <summary> 
â¯ â¯ /// Defines the list of custom commands 
â¯ â¯ /// </summary> 

â¯ â¯ public List<KeyboardCommand> command = new List<KeyboardCommand>() 
â¯ â¯ { 
â¯ â¯ â¯ â¯ new KeyboardCommand() 
â¯ â¯ â¯ â¯ { 
â¯ â¯ â¯ â¯ â¯ â¯ ActionName = "FitToWidth", 
â¯ â¯ â¯ â¯ â¯ â¯ Gesture = new KeyGesture() { Key = PdfKeys.W, Modifiers = PdfModifierKeys.Shift } 
â¯ â¯ â¯ â¯ }, 
â¯ â¯ â¯ â¯ new KeyboardCommand() 
â¯ â¯ â¯ â¯ { 
â¯ â¯ â¯ â¯ â¯ â¯ ActionName = "FitToPage", 
â¯ â¯ â¯ â¯ â¯ â¯ Gesture = new KeyGesture() { Key = PdfKeys.P, Modifiers = PdfModifierKeys.Alt } 
        } 
â¯ â¯ }; 

â¯ â¯ /// <summary> 
â¯ â¯ /// Custom command execution. 
â¯ â¯ /// </summary> 

â¯ â¯ public void CommandExecute(CommandExecutedEventArgs args) 
â¯ â¯ { 
â¯ â¯ â¯ â¯ if(args.Modifiers == PdfModifierKeys.Shiftâ¯&& args.Key == PdfKeys.W) 
â¯ â¯ â¯ â¯ { 
â¯ â¯ â¯ â¯ â¯ â¯ pdfViewer.FitToWidthAsync(); 
â¯ â¯ â¯ â¯ } 
â¯ â¯ â¯ â¯ else if (args.Modifiers == PdfModifierKeys.Alt && args.Key == PdfKeys.P) 
â¯ â¯ â¯ â¯ { 
â¯ â¯ â¯ â¯ â¯ â¯ pdfViewer.FitToPageAsync(); 
â¯ â¯ â¯ â¯ }  
â¯ â¯ } 
} 

```

[View sample in GitHub](https://github.com/SyncfusionExamples/blazor-pdf-viewer-examples/tree/master/Keyboard%20accessibility/Command%20Manager)

## See also

* [Keyboard Accessibility in Syncfusion<sup style="font-size:70%">&reg;</sup> Blazor PDF Viewer](./accessibility)
