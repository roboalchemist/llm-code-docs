# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/scrolling-zooming.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/scrolling-zooming.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/scrolling-zooming.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/scrolling-zooming.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/scrolling-zooming.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/scrolling-zooming.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/scrolling-zooming.md

# Scrolling

The Document editor renders the document page by page. You can scroll through the pages by mouse wheel or touch interactions. You can also scroll through the page by using âscrollToPage()â method of document editor instance.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<div id="documenteditor" style="width:100%;height:100%">
    <ejs-documenteditor isReadOnly=false id="container"></ejs-documenteditor>      
</div>
<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        documenteditor = document.getElementById('DocumentEditor').ej2_instances[0];
        documenteditor.resize();
        onLoadDefault();
        documenteditor.scrollToPage(2);
    });

    function onLoadDefault() {
        var defaultDocument = {
            "sections": [
                {
                    "blocks": [
                        {
                            "paragraphFormat": {
                                "styleName": "Normal"
                            },
                            "inlines": [
                                {
                                    "text": "First page"
                                }
                            ]
                        }
                    ],
                    "headersFooters": {},
                },
                {
                    "blocks": [
                        {
                            "paragraphFormat": {
                                "styleName": "Normal"
                            },
                            "inlines": [
                                {
                                    "text": "Second page"
                                }
                            ]
                        }
                    ],
                    "headersFooters": {},
                }
            ],
            "characterFormat": {},
            "paragraphFormat": {},
            "background": {
                "color": "#FFFFFFFF"
            },
            "styles": [
                {
                    "type": "Paragraph",
                    "name": "Normal",
                    "next": "Normal"
                },
                {
                    "type": "Character",
                    "name": "Default Paragraph Font"
                }
            ]
        }
        documenteditor.open(JSON.stringify(defaultDocument));
        documenteditor.focusIn();
    }
</script>
{% endhighlight %}
{% highlight c# tabtitle="Document-editor.cs" %}
public ActionResult Default()
{
    return View();
}
   

{% endhighlight %}
{% endtabs %}


N> Calling this method brings the specified page into view but doesnât move selection. Hence this method will work by default. That is, it works even if selection is not enabled.

In case, if you wish to move the selection to any page in document editor and bring it into view, you can use âgoToPage()â method of selection instance.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<div id="documenteditor" style="width:100%;height:100%">
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableSfdtExport=true id="DocumentEditor"></ejs-documenteditor>
</div>
<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        documenteditor = document.getElementById('DocumentEditor').ej2_instances[0];
        documenteditor.resize();
        onLoadDefaultDocument();
        documenteditor.viewer.selection.goToPage(3);
    });

    function onLoadDefaultDocument() {
        var defaultDocument = {
            "sections": [
                {
                    "blocks": [
                        {
                            "paragraphFormat": {
                                "styleName": "Normal"
                            },
                            "inlines": [
                                {
                                    "text": "First page"
                                }
                            ]
                        }
                    ],
                    "headersFooters": {},
                },
                {
                    "blocks": [
                        {
                            "paragraphFormat": {
                                "styleName": "Normal"
                            },
                            "inlines": [
                                {
                                    "text": "Second page"
                                }
                            ]
                        }
                    ],
                    "headersFooters": {},
                },
                {
                    "blocks": [
                        {
                            "paragraphFormat": {
                                "styleName": "Normal"
                            },
                            "inlines": [
                                {
                                    "text": "Third page"
                                }
                            ]
                        }
                    ],
                    "headersFooters": {},
                }
            ],
            "characterFormat": {},
            "paragraphFormat": {},
            "background": {
                "color": "#FFFFFFFF"
            },
            "styles": [
                {
                    "type": "Paragraph",
                    "name": "Normal",
                    "next": "Normal"
                },
                {
                    "type": "Character",
                    "name": "Default Paragraph Font"
                }
            ]
        };
        documenteditor.open(JSON.stringify(defaultDocument));
        documenteditor.focusIn();
    }

</script>
{% endhighlight %}
{% highlight c# tabtitle="Document-editor.cs" %}
public ActionResult Default()
{
    return View();
}
   

{% endhighlight %}
{% endtabs %}



## Zooming

You can scale the contents in document editor ranging from 10% to 500% of the actual size. You can achieve this using mouse or touch interactions. You can also use âzoomFactorâ property of document editor instance. The value can be specified in a range from 0.1 to 5.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<div id="documenteditor" style="width:100%;height:100%">
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableSfdtExport=true id="DocumentEditor"></ejs-documenteditor>
</div>
<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        documenteditor = document.getElementById('DocumentEditor').ej2_instances[0];
        documenteditor.resize();
        documenteditor.zoomFactor = 3;
    });
</script>
{% endhighlight %}
{% highlight c# tabtitle="Scrolling-zooming.cs" %}
{% endhighlight %}{% endtabs %}


## Page Fit Type

Apart from specifying the zoom factor as value, the Document editor provides option to specify page fit options such as fit to full page or fit to page width. You can set this option using âfitPageâ method of document editor instance.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<div id="documenteditor" style="width:100%;height:100%">
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableSfdtExport=true id="DocumentEditor"></ejs-documenteditor>
</div>
<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        documenteditor = document.getElementById('DocumentEditor').ej2_instances[0];
        documenteditor.resize();
        documenteditor.fitPage('FitPageWidth');
    });
</script>
{% endhighlight %}
{% highlight c# tabtitle="Scrolling-page-fit.cs" %}
{% endhighlight %}{% endtabs %}


## Zoom option using UI


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<div id="documenteditor" style="width:100%;height:100%">
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableSfdtExport=true id="DocumentEditor"></ejs-documenteditor>
</div>
<div id='page-fit-type-div'>
    <label style="margin-top: 6px;margin-right: 2px">Page</label>
    <div id='editablePageNumber' style='border: 1px solid #F1F1F1;display: inline-flex;height: 17px;padding: 0px 4px;'>
        <label id="documenteditor_page_no" style="text-transform:capitalize;white-space:pre;overflow:hidden;user-select:none;cursor:text;height:17px;max-width:150px"></label>
    </div>
    <label style="margin-left:2px;letter-spacing: 1.05px;">of</label>
    <label id='documenteditor_pagecount' style="margin-left:6px;letter-spacing: 1.05px;"></label>
    <ejs-dropdownbutton id="zoom" content="100%" items="ViewBag.zoomList"></ejs-dropdownbutton>
</div>
<script>
    var documenteditor;
    var pageCount;
    var editablePageNumber;
    var editorPageCount;
    var pageNumberLabel;
    var startPage = 1;
    var zoomBtn;
    document.addEventListener('DOMContentLoaded', function () {
        documenteditor = document.getElementById('DocumentEditor').ej2_instances[0];
        pageCount = document.getElementById('documenteditor_pagecount');
        editablePageNumber = document.getElementById('editablePageNumber');
        pageNumberLabel = document.getElementById('documenteditor_page_no');
        documenteditor.resize();
        editablePageNumber.addEventListener('click', updateDocumentEditorPageNumber);
        editablePageNumber.addEventListener('keydown', onKeyDown);
        editablePageNumber.addEventListener('blur', onBlur);
        zoomBtn = document.getElementById('zoom');
        zoomBtn.className = 'e-de-statusbar-zoom';
        var zoom = zoomBtn.ej2_instances[0];
        zoom.select = function (e) {
            onZoom(e);
        };
        updatePageCount();
        updatePageNumber();
        editablePageNumber.addEventListener('click', updateDocumentEditorPageNumber);
        editablePageNumber.addEventListener('keydown', onKeyDown);
        editablePageNumber.addEventListener('blur', onBlur);
        documenteditor.viewChange = function (e) {
            updatePageNumberOnViewChange(e);
        };
        documenteditor.contentChange = function () {
            //Set page count
            updatePageCount();
        };
    });

    function updatePageNumberOnViewChange(args) {
        if (documenteditor.selection
            && documenteditor.selection.startPage >= args.startPage && documenteditor.selection.startPage <= args.endPage) {
            startPage = documenteditor.selection.startPage;
        } else {
            startPage = args.startPage;
        }
        updatePageNumber();
    }
    function onBlur() {
        if (editablePageNumber.textContent === '' || parseInt(editablePageNumber.textContent, 0) > editorPageCount) {
            updatePageNumber();
        }
        editablePageNumber.contentEditable = 'false';
    }
    function onKeyDown(e) {
        if (e.which === 13) {
            e.preventDefault();
            var pageNumber = parseInt(editablePageNumber.textContent, 0);
            if (pageNumber > editorPageCount) {
                updatePageNumber();
            } else {
                if (documenteditor.selection) {
                    documenteditor.selection.goToPage(parseInt(editablePageNumber.textContent, 0));
                } else {
                    documenteditor.scrollToPage(parseInt(editablePageNumber.textContent, 0));
                }
            }
            editablePageNumber.contentEditable = 'false';
            if (editablePageNumber.textContent === '') {
                updatePageNumber();
            }
        }
        if (e.which > 64) {
            e.preventDefault();
        }
    }
    function onZoom(args) {
        setZoomValue(args.item.text);
        updateZoomContent();
    }
    function setZoomValue(text) {
        if (text.match('Fit one page')) {
            documenteditor.fitPage('FitOnePage');
        } else if (text.match('Fit page width')) {
            documenteditor.fitPage('FitPageWidth');
        } else {
            documenteditor.zoomFactor = parseInt(text, 0) / 100;
        }
    }
    function updateZoomContent() {
        zoomBtn.content = Math.round(documenteditor.zoomFactor * 100) + '%';
    }
    function updatePageNumber() {
        pageNumberLabel.textContent = startPage.toString();
    }
    function updatePageCount() {
        editorPageCount = documenteditor.pageCount;
        pageCount.textContent = editorPageCount.toString();
    }
    function updateDocumentEditorPageNumber() {
        var editablePageNumber = document.getElementById('editablePageNumber');
        editablePageNumber.contentEditable = 'true';
        editablePageNumber.focus();
        window.getSelection().selectAllChildren(editablePageNumber);
    }
</script>

<style>
    #DocumentEditor {
        width: 100%;
        height: 100%;
    }

    .e-de-statusbar-zoom {
        float: right;
        text-align: center;
        padding: 2px;
        line-height: 19px;
        margin-top: 1px;
    }
</style>
{% endhighlight %}
{% highlight c# tabtitle="Document-editor.cs" %}
public ActionResult Default()
{
    List<object> zoomItems = new List<object>();
    zoomItems.Add(new { text = "200%" });
    zoomItems.Add(new { text = "175%" });
    zoomItems.Add(new { text = "150%" });
    zoomItems.Add(new { text = "125%" });
    zoomItems.Add(new { text = "100%" });
    zoomItems.Add(new { text = "75%" });
    zoomItems.Add(new { text = "50%" });
    zoomItems.Add(new { text = "25%" });
    zoomItems.Add(new { separator = true });
    zoomItems.Add(new { text = "Fit one page" });
    zoomItems.Add(new { text = "Fit page width" });
    ViewBag.zoomList = zoomItems;

    return View();
}
{% endhighlight %}
{% endtabs %}

