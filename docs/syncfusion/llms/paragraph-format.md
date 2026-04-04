# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/paragraph-format.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/paragraph-format.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/paragraph-format.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/paragraph-format.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/blazor/paragraph-format.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/paragraph-format.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/paragraph-format.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/paragraph-format.md

# Working with Paragraph Formatting

Document editor supports various paragraph formatting options such as text alignment, indentation, paragraph spacing, and more.

## Indentation

You can modify the left or right indentation of selected paragraphs using the following sample code.

```typescript
documenteditor.selection.paragraphFormat.leftIndent= 24;
documenteditor.selection.paragraphFormat.rightIndent= 24;
```

## Special indentation

You can define special indent for the first line of the paragraph using the following sample code.

```typescript
documenteditor.selection.paragraphFormat.firstLineIndent= 24;
```

## Increase indent

You can increase the left indent of selected paragraphs by a factor of 36 points using the following sample code.

```typescript
documenteditor.editor.increaseIndent()
```

## Decrease indent

You can decrease the left indent of selected paragraphs by a factor of 36 points using the following sample code.

```typescript
documenteditor.editor.decreaseIndent()
```

## Text alignment

You can get or set the text alignment of selected paragraphs using the following sample code.

```typescript
documenteditor.selection.paragraphFormat.textAlignment= 'Center' | 'Left' | 'Right' | 'Justify';
```

You can toggle the text alignment of selected paragraphs by specifying a value using the following sample code.

```typescript
documenteditor.editor.toggleTextAlignment('Center' | 'Left' | 'Right' | 'Justify');
```

## Line spacing and its type

You can define the line spacing and its type for selected paragraphs using the following sample code.

```typescript
// Set line spacing type
documenteditor.selection.paragraphFormat.lineSpacingType='AtLeast';
// Set line spacing value (supports both integer and float)
documenteditor.selection.paragraphFormat.lineSpacing= 6; // Integer value
documenteditor.selection.paragraphFormat.lineSpacing= 6.5; // Float value
```

## Paragraph spacing

You can define the spacing before or after the paragraph by using the following sample code.

```typescript
documenteditor.selection.paragraphFormat.beforeSpacing= 24;
documenteditor.selection.paragraphFormat.afterSpacing= 24;
```

You can also set automatic spacing before and after the paragraph by using the following sample code.

```typescript
documenteditor.selection.paragraphFormat.spaceBeforeAuto = true;
documenteditor.selection.paragraphFormat.spaceAfterAuto = true;
```

N> If auto spacing property is enabled, then value defined in the `beforeSpacing` and `afterSpacing` property will not be considered.

## Pagination properties

You can enable or disable the following pagination properties for the paragraphs in a Word document.

* Widow/Orphan control - whether the first and last lines of the paragraph are to remain on the same page as the rest of the paragraph when paginating the document.
* Keep with next - whether the specified paragraph remains on the same page as the paragraph that follows it while paginating the document.
* Keep lines together - whether all lines in the specified paragraphs remain on the same page while paginating the document.

```typescript
documenteditor.selection.paragraphFormat.widowControl = false;
documenteditor.selection.paragraphFormat.keepWithNext = true;
documenteditor.selection.paragraphFormat.keepLinesTogether = true;
```

## Paragraph Border

You can apply borders to the paragraphs in a Word document. Using borders, decorate the paragraphs to set them apart from other paragraphs in the document.

The following example code illustrates how to apply box border for the selected paragraphs.

```typescript
// left
documenteditor.selection.paragraphFormat.borders.left.lineStyle = 'Single';
documenteditor.selection.paragraphFormat.borders.left.lineWidth = 3;
documenteditor.selection.paragraphFormat.borders.left.color = "#000000";

//right
documenteditor.selection.paragraphFormat.borders.right.lineStyle = 'Single';
documenteditor.selection.paragraphFormat.borders.right.lineWidth = 3;
documenteditor.selection.paragraphFormat.borders.right.color = "#000000";

//top
documenteditor.selection.paragraphFormat.borders.top.lineStyle = 'Single';
documenteditor.selection.paragraphFormat.borders.top.lineWidth = 3;
documenteditor.selection.paragraphFormat.borders.top.color = "#000000";

//bottom
documenteditor.selection.paragraphFormat.borders.bottom.lineStyle = 'Single';
documenteditor.selection.paragraphFormat.borders.bottom.lineWidth = 3;
documenteditor.selection.paragraphFormat.borders.bottom.color = "#000000";

```

N> At present, the Document editor component displays all the border styles as single line. But you can apply any border style and get the proper display in Microsoft Word app when opening the exported Word document.

## Show or Hide Paragraph marks

You can show or hide the hidden formatting symbols like spaces, tab, paragraph marks, and breaks in Document editor component. These marks help identify the start and end of a paragraph and all the hidden formatting symbols in a Word document.

The following example code illustrates how to show or hide paragraph marks.

```typescript
documenteditor.documentEditorSettings.showHiddenMarks = true;
```

## Toolbar with paragraph formatting options


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<div id="toolbar"></div>
<div id="documenteditor" style="width:100%;height:100%" >
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableEditorHistory=true enableSfdtExport=true enableContextMenu=true id="container"></ejs-documenteditor>
</div>

<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        documenteditor = document.getElementById("container").ej2_instances[0];
        documenteditor.resize();
        updateContainerSize();

        function toolbarButtonClick(arg) {
            switch (arg.item.id) {
                case 'AlignLeft':
                    //Toggle the Left alignment for selected or current paragraph
                    documenteditor.editor.toggleTextAlignment('Left');
                    break;
                case 'AlignRight':
                    //Toggle the Right alignment for selected or current paragraph
                    documenteditor.editor.toggleTextAlignment('Right');
                    break;
                case 'AlignCenter':
                    //Toggle the Center alignment for selected or current paragraph
                    documenteditor.editor.toggleTextAlignment('Center');
                    break;
                case 'Justify':
                    //Toggle the Justify alignment for selected or current paragraph
                    documenteditor.editor.toggleTextAlignment('Justify');
                    break;
                case 'IncreaseIndent':
                    //Increase the left indent of selected or current paragraph
                    documenteditor.editor.increaseIndent();
                    break;
                case 'DecreaseIndent':
                    //Decrease the left indent of selected or current paragraph
                    documenteditor.editor.decreaseIndent();
                    break;
                case 'ClearFormat':
                    documenteditor.editor.clearFormatting();
                    break;
                case 'ShowParagraphMark':
                    //Show or hide the hidden characters like spaces, tab, paragraph marks, and breaks.
                    documenteditor.documentEditorSettings.showHiddenMarks = !documenteditor.documentEditorSettings.showHiddenMarks;
                    break;
            }
        }
        //Change the line spacing of selected or current paragraph
        function lineSpacingAction(args) {
            var text = args.item.text;
            switch (text) {
                case 'Single':
                    documenteditor.selection.paragraphFormat.lineSpacing = 1;
                    break;
                case '1.15':
                    documenteditor.selection.paragraphFormat.lineSpacing = 1.15;
                    break;
                case '1.5':
                    documenteditor.selection.paragraphFormat.lineSpacing = 1.5;
                    break;
                case 'Double':
                    documenteditor.selection.paragraphFormat.lineSpacing = 2;
                    break;
            }
            setTimeout(function () {
                documenteditor.focusIn();
            }, 30);
        }
        documenteditor.selectionChange = function () {
            setTimeout(function () {
                onSelectionChange();
            }, 20);
        };
        // Selection change to retrieve formatting
        function onSelectionChange() {
            if (documenteditor.selection) {
                var paragraphFormat = documenteditor.selection.paragraphFormat;
                var toggleBtnId = ['AlignLeft', 'AlignCenter', 'AlignRight', 'Justify', 'ShowParagraphMark'];
                for (var i = 0; i < toggleBtnId.length; i++) {
                    var toggleBtn = document.getElementById(
                        toggleBtnId[i]
                    );
                    toggleBtn.classList.remove('e-btn-toggle');
                }
                if (paragraphFormat.textAlignment === 'Left') {
                    document.getElementById('AlignLeft').classList.add('e-btn-toggle');
                } else if (paragraphFormat.textAlignment === 'Right') {
                    document.getElementById('AlignRight').classList.add('e-btn-toggle');
                } else if (paragraphFormat.textAlignment === 'Center') {
                    document
                        .getElementById('AlignCenter')
                        .classList.add('e-btn-toggle');
                } else {
                    document.getElementById('Justify').classList.add('e-btn-toggle');
                }
                if(documenteditor.documentEditorSettings.showHiddenMarks) {
                    document.getElementById('ShowParagraphMark').classList.add('e-btn-toggle');
                }
                // #endregion
            }
        }
        //Toolbar configuration to add paragraph formatting options
        var toolBar = new ej.navigations.Toolbar({
            clicked: toolbarButtonClick,
            items: [
                {
                    prefixIcon: 'e-de-icon-AlignLeft',
                    tooltipText: 'Align Left',
                    id: 'AlignLeft',
                },
                {
                    prefixIcon: 'e-de-icon-AlignCenter',
                    tooltipText: 'Align Center',
                    id: 'AlignCenter',
                },
                {
                    prefixIcon: 'e-de-icon-AlignRight',
                    tooltipText: 'Align Right',
                    id: 'AlignRight',
                },
                {
                    prefixIcon: 'e-de-icon-Justify',
                    tooltipText: 'Justify',
                    id: 'Justify',
                },
                {
                    prefixIcon: 'e-de-icon-IncreaseIndent',
                    tooltipText: 'Increase Indent',
                    id: 'IncreaseIndent',
                },
                {
                    prefixIcon: 'e-de-icon-DecreaseIndent',
                    tooltipText: 'Decrease Indent',
                    id: 'DecreaseIndent',
                },
                { type: 'Seperator' },
                {
                    id: 'lineSpacing',
                }, {
                    prefixIcon: 'e-de-icon-ClearAll',
                    tooltipText: 'ClearFormatting',
                    id: 'ClearFormat',
                },
                { type: 'Seperator' },
                {
                    prefixIcon: 'e-de-e-paragraph-mark e-icons',
                    tooltipText: 'Show the hidden characters like spaces, tab, paragraph marks, and breaks.(Ctrl + *)',
                    id: 'ShowParagraphMark',
                }
            ],
        });
        toolBar.appendTo('#toolbar');
        var items = [
            {
                text: 'Single',
            },
            {
                text: '1.15',
            },
            {
                text: '1.5',
            },
            {
                text: 'Double',
            },
        ];
        var dropdown = new ejs.splitbuttons.DropDownButton({
            items: items,
            iconCss: 'e-de-icon-LineSpacing',
            select: lineSpacingAction,
        });
        dropdown.appendTo('#lineSpacing');

    });
</script>

<style>
    #container {
        width: 100%;
        height: 100%
    }
</style>
{% endhighlight %}
{% highlight c# tabtitle="Paragraph-format.cs" %}
public ActionResult Default()
{
    return View();
}
   

{% endhighlight %}
{% endtabs %}


## See Also

* [Feature modules](../asp-net-core/feature-module)
* [Paragraph dialog](../asp-net-core/dialog#paragraph-dialog)
* [Keyboard shortcuts](../asp-net-core/keyboard-shortcut)
