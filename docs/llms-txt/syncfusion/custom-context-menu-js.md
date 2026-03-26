# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/javascript-es5/how-to/custom-context-menu-js.md

# Customize the context menu in JavaScript PDF Viewer

The PDF Viewer supports adding custom options to the context menu using the [addCustomMenu()](https://ej2.syncfusion.com/documentation/api/pdfviewer#addcustommenu) method. Define actions for custom items with the [customContextMenuSelect()](https://ej2.syncfusion.com/documentation/api/pdfviewer#customcontextMenuselect) method.

### Add a custom option

The following example adds custom options to the context menu.

```js
var pdfviewer = new ej.pdfviewer.PdfViewer({
    documentPath: 'https://cdn.syncfusion.com/content/pdf/pdf-succinctly.pdf',
    resourceUrl:'https://cdn.syncfusion.com/ej2/31.2.2/dist/ej2-pdfviewer-lib'
});
ej.pdfviewer.PdfViewer.Inject(ej.pdfviewer.TextSelection, ej.pdfviewer.TextSearch, ej.pdfviewer.Print, ej.pdfviewer.Navigation, ej.pdfviewer.Toolbar, ej.pdfviewer.Magnification, ej.pdfviewer.Annotation, ej.pdfviewer.FormDesigner, ej.pdfviewer.FormFields,ej.pdfviewer.PageOrganizer);

var menuItems = [
    {
        text: 'Search In Google',
        id: 'search_in_google',
        iconCss: 'e-icons e-search'
    },
    {
        text: 'Lock Annotation',
        iconCss: 'e-icons e-lock',
        id: 'lock_annotation'
    },
    {
        text: 'Unlock Annotation',
        iconCss: 'e-icons e-unlock',
        id: 'unlock_annotation'
    },
    {
        text: 'Lock Form Field',
        iconCss: 'e-icons e-lock',
        id: 'read_only_true'
    },
    {
        text: 'UnLock Form Field',
        iconCss: 'e-icons e-unlock',
        id: 'read_only_false'
    },
];

pdfviewer.appendTo('#PdfViewer');

pdfviewer.documentLoad = function (args) {
    pdfviewer.addCustomMenu(menuItems, false, false);
}
```

### Customize the default vs custom menu

Toggle the display of the default context menu. When the addCustomMenu parameter is `true`, the default menu is hidden; when `false`, default menu items are displayed alongside custom items.

```js
var pdfviewer = new ej.pdfviewer.PdfViewer({
    documentPath: 'https://cdn.syncfusion.com/content/pdf/pdf-succinctly.pdf',
    resourceUrl:'https://cdn.syncfusion.com/ej2/31.2.2/dist/ej2-pdfviewer-lib'
});
ej.pdfviewer.PdfViewer.Inject(ej.pdfviewer.TextSelection, ej.pdfviewer.TextSearch, ej.pdfviewer.Print, ej.pdfviewer.Navigation, ej.pdfviewer.Toolbar, ej.pdfviewer.Magnification, ej.pdfviewer.Annotation, ej.pdfviewer.FormDesigner, ej.pdfviewer.FormFields,ej.pdfviewer.PageOrganizer);

var menuItems = [
    {
        text: 'Search In Google',
        id: 'search_in_google',
        iconCss: 'e-icons e-search'
    },
    {
        text: 'Lock Annotation',
        iconCss: 'e-icons e-lock',
        id: 'lock_annotation'
    },
    {
        text: 'Unlock Annotation',
        iconCss: 'e-icons e-unlock',
        id: 'unlock_annotation'
    },
    {
        text: 'Lock Form Field',
        iconCss: 'e-icons e-lock',
        id: 'read_only_true'
    },
    {
        text: 'UnLock Form Field',
        iconCss: 'e-icons e-unlock',
        id: 'read_only_false'
    },
];

pdfviewer.appendTo('#PdfViewer');

pdfviewer.documentLoad = function (args) {
    pdfviewer.addCustomMenu(menuItems, true);
}
```

#### Show or hide custom items before opening

Use [customContextMenuBeforeOpen()](https://ej2.syncfusion.com/documentation/api/pdfviewer#customcontextmenubeforeopen) to hide or show custom options dynamically.

```js
var pdfviewer = new ej.pdfviewer.PdfViewer({
    documentPath: 'https://cdn.syncfusion.com/content/pdf/pdf-succinctly.pdf',
    resourceUrl:'https://cdn.syncfusion.com/ej2/31.2.2/dist/ej2-pdfviewer-lib'
});
ej.pdfviewer.PdfViewer.Inject(ej.pdfviewer.TextSelection, ej.pdfviewer.TextSearch, ej.pdfviewer.Print, ej.pdfviewer.Navigation, ej.pdfviewer.Toolbar, ej.pdfviewer.Magnification, ej.pdfviewer.Annotation, ej.pdfviewer.FormDesigner, ej.pdfviewer.FormFields,ej.pdfviewer.PageOrganizer);

var menuItems = [
    {
        text: 'Search In Google',
        id: 'search_in_google',
        iconCss: 'e-icons e-search'
    },
    {
        text: 'Lock Annotation',
        iconCss: 'e-icons e-lock',
        id: 'lock_annotation'
    },
    {
        text: 'Unlock Annotation',
        iconCss: 'e-icons e-unlock',
        id: 'unlock_annotation'
    },
    {
        text: 'Lock Form Field',
        iconCss: 'e-icons e-lock',
        id: 'read_only_true'
    },
    {
        text: 'UnLock Form Field',
        iconCss: 'e-icons e-unlock',
        id: 'read_only_false'
    },
];

pdfviewer.appendTo('#PdfViewer');

pdfviewer.documentLoad = function (args) {
    pdfviewer.addCustomMenu(menuItems, false, false);
}

pdfviewer.customContextMenuSelect = function (args) {
    switch (args.id) {
        case 'search_in_google':
            for (var i = 0; i < pdfviewer.textSelectionModule.selectionRangeArray.length; i++) {
                var content = pdfviewer.textSelectionModule.selectionRangeArray[i].textContent;
                if ((pdfviewer.textSelectionModule.isTextSelection) && (/\S/.test(content))) {
                    window.open('http://google.com/search?q=' + content);
                }
            }
            break;
        case 'lock_annotation':
            lockAnnotations(args);
            break;
        case 'unlock_annotation':
            unlockAnnotations(args);
            break;
        case 'read_only_true':
            setReadOnlyTrue(args);
            break;
        case 'read_only_false':
            setReadOnlyFalse(args);
            break;
        case 'formfield properties':
            break;
        default:
            break;
    }
};

pdfviewer.customContextMenuBeforeOpen = function (args) {
    for (var i = 0; i < args.ids.length; i++) {
        var search = document.getElementById(args.ids[i]);
        if (search) {
            search.style.display = 'none';
            if (args.ids[i] === 'search_in_google' && (pdfviewer.textSelectionModule) && pdfviewer.textSelectionModule.isTextSelection) {
                search.style.display = 'block';
            } else if (args.ids[i] === "lock_annotation" || args.ids[i] === "unlock_annotation") {
                var isLockOption = args.ids[i] === "lock_annotation";
                for (var j = 0; j < pdfviewer.selectedItems.annotations.length; j++) {
                    var selectedAnnotation = pdfviewer.selectedItems.annotations[j];
                    if (selectedAnnotation && selectedAnnotation.annotationSettings) {
                        var shouldDisplay = (isLockOption && !selectedAnnotation.annotationSettings.isLock) ||
                            (!isLockOption && selectedAnnotation.annotationSettings.isLock);
                        search.style.display = shouldDisplay ? 'block' : 'none';
                    }
                }
            } else if ((args.ids[i] === "read_only_true" || args.ids[i] === "read_only_false") && pdfviewer.selectedItems.formFields.length !== 0) {
                var isReadOnlyOption = args.ids[i] === "read_only_true";
                for (var k = 0; k < pdfviewer.selectedItems.formFields.length; k++) {
                    var selectedFormFields = pdfviewer.selectedItems.formFields[k];
                    if (selectedFormFields) {
                        var selectedFormField = pdfviewer.selectedItems.formFields[k].isReadonly;
                        var displayMenu = (isReadOnlyOption && !selectedFormField) || (!isReadOnlyOption && selectedFormField);
                        search.style.display = displayMenu ? 'block' : 'none';
                    }
                }
            } else if (args.ids[i] === 'formfield properties' && pdfviewer.selectedItems.formFields.length !== 0) {
                search.style.display = 'block';
            }
        }
    }
};

function lockAnnotations(args) {
    for (var i = 0; i < pdfviewer.annotationCollection.length; i++) {
        if (pdfviewer.annotationCollection[i].uniqueKey === pdfviewer.selectedItems.annotations[0].id) {
            pdfviewer.annotationCollection[i].annotationSettings.isLock = true;
            pdfviewer.annotationCollection[i].isCommentLock = true;
            pdfviewer.annotation.editAnnotation(pdfviewer.annotationCollection[i]);
        }
        args.cancel = false;
    }
}

function unlockAnnotations(args) {
    for (var i = 0; i < pdfviewer.annotationCollection.length; i++) {
        if (pdfviewer.annotationCollection[i].uniqueKey === pdfviewer.selectedItems.annotations[0].id) {
            pdfviewer.annotationCollection[i].annotationSettings.isLock = false;
            pdfviewer.annotationCollection[i].isCommentLock = false;
            pdfviewer.annotation.editAnnotation(pdfviewer.annotationCollection[i]);
        }
        args.cancel = false;
    }
}

function setReadOnlyTrue(args) {
    var selectedFormFields = pdfviewer.selectedItems.formFields;
    for (var i = 0; i < selectedFormFields.length; i++) {
        var selectFormFields = selectedFormFields[i];
        if (selectFormFields) {
            pdfviewer.formDesignerModule.updateFormField(selectFormFields, {
                isReadOnly: true,
            });
        }
        args.cancel = false;
    }
}

function setReadOnlyFalse(args) {
    var selectedFormFields = pdfviewer.selectedItems.formFields;
    for (var i = 0; i < selectedFormFields.length; i++) {
        var selectFormFields = selectedFormFields[i];
        if (selectFormFields) {
            pdfviewer.formDesignerModule.updateFormField(selectFormFields, {
                isReadOnly: false,
            });
        }
        args.cancel = false;
    }
}
```

The following is the output of the custom context menu with customization.

{% tabs %}
{% highlight ts tabtitle="index.js" %}
var pdfviewer = new ej.pdfviewer.PdfViewer({
    documentPath: 'https://cdn.syncfusion.com/content/pdf/pdf-succinctly.pdf',
    resourceUrl:'https://cdn.syncfusion.com/ej2/25.1.35/dist/ej2-pdfviewer-lib'
});
ej.pdfviewer.PdfViewer.Inject(ej.pdfviewer.TextSelection, ej.pdfviewer.TextSearch, ej.pdfviewer.Print, ej.pdfviewer.Navigation, ej.pdfviewer.Toolbar,
                              ej.pdfviewer.Magnification, ej.pdfviewer.Annotation, ej.pdfviewer.FormDesigner, ej.pdfviewer.FormFields, ej.pdfviewer.PageOrganizer);

var menuItems = [
    {
        text: 'Search In Google',
        id: 'search_in_google',
        iconCss: 'e-icons e-search'
    },
    {
        text: 'Lock Annotation',
        iconCss: 'e-icons e-lock',
        id: 'lock_annotation'
    },
    {
        text: 'Unlock Annotation',
        iconCss: 'e-icons e-unlock',
        id: 'unlock_annotation'
    },
    {
        text: 'Lock Form Field',
        iconCss: 'e-icons e-lock',
        id: 'read_only_true'
    },
    {
        text: 'UnLock Form Field',
        iconCss: 'e-icons e-unlock',
        id: 'read_only_false'
    },
];

pdfviewer.appendTo('#PdfViewer');

pdfviewer.documentLoad = function (args) {
    pdfviewer.addCustomMenu(menuItems, false, false);
}

pdfviewer.customContextMenuSelect = function (args) {
    switch (args.id) {
        case 'search_in_google':
            for (var i = 0; i < pdfviewer.textSelectionModule.selectionRangeArray.length; i++) {
                var content = pdfviewer.textSelectionModule.selectionRangeArray[i].textContent;
                if ((pdfviewer.textSelectionModule.isTextSelection) && (/\S/.test(content))) {
                    window.open('http://google.com/search?q=' + content);
                }
            }
            break;
        case 'lock_annotation':
            lockAnnotations(args);
            break;
        case 'unlock_annotation':
            unlockAnnotations(args);
            break;
        case 'read_only_true':
            setReadOnlyTrue(args);
            break;
        case 'read_only_false':
            setReadOnlyFalse(args);
            break;
        case 'formfield properties':
            break;
        default:
            break;
    }
};

pdfviewer.customContextMenuBeforeOpen = function (args) {
    for (var i = 0; i < args.ids.length; i++) {
        var search = document.getElementById(args.ids[i]);
        if (search) {
            search.style.display = 'none';
            if (args.ids[i] === 'search_in_google' && (pdfviewer.textSelectionModule) && pdfviewer.textSelectionModule.isTextSelection) {
                search.style.display = 'block';
            } else if (args.ids[i] === "lock_annotation" || args.ids[i] === "unlock_annotation") {
                var isLockOption = args.ids[i] === "lock_annotation";
                for (var j = 0; j < pdfviewer.selectedItems.annotations.length; j++) {
                    var selectedAnnotation = pdfviewer.selectedItems.annotations[j];
                    if (selectedAnnotation && selectedAnnotation.annotationSettings) {
                        var shouldDisplay = (isLockOption && !selectedAnnotation.annotationSettings.isLock) ||
                            (!isLockOption && selectedAnnotation.annotationSettings.isLock);
                        search.style.display = shouldDisplay ? 'block' : 'none';
                    }
                }
            } else if ((args.ids[i] === "read_only_true" || args.ids[i] === "read_only_false") && pdfviewer.selectedItems.formFields.length !== 0) {
                var isReadOnlyOption = args.ids[i] === "read_only_true";
                for (var k = 0; k < pdfviewer.selectedItems.formFields.length; k++) {
                    var selectedFormFields = pdfviewer.selectedItems.formFields[k];
                    if (selectedFormFields) {
                        var selectedFormField = pdfviewer.selectedItems.formFields[k].isReadonly;
                        var displayMenu = (isReadOnlyOption && !selectedFormField) || (!isReadOnlyOption && selectedFormField);
                        search.style.display = displayMenu ? 'block' : 'none';
                    }
                }
            } else if (args.ids[i] === 'formfield properties' && pdfviewer.selectedItems.formFields.length !== 0) {
                search.style.display = 'block';
            }
        }
    }
};

function lockAnnotations(args) {
    for (var i = 0; i < pdfviewer.annotationCollection.length; i++) {
        if (pdfviewer.annotationCollection[i].uniqueKey === pdfviewer.selectedItems.annotations[0].id) {
            pdfviewer.annotationCollection[i].annotationSettings.isLock = true;
            pdfviewer.annotationCollection[i].isCommentLock = true;
            pdfviewer.annotation.editAnnotation(pdfviewer.annotationCollection[i]);
        }
        args.cancel = false;
    }
}

function unlockAnnotations(args) {
    for (var i = 0; i < pdfviewer.annotationCollection.length; i++) {
        if (pdfviewer.annotationCollection[i].uniqueKey === pdfviewer.selectedItems.annotations[0].id) {
            pdfviewer.annotationCollection[i].annotationSettings.isLock = false;
            pdfviewer.annotationCollection[i].isCommentLock = false;
            pdfviewer.annotation.editAnnotation(pdfviewer.annotationCollection[i]);
        }
        args.cancel = false;
    }
}

function setReadOnlyTrue(args) {
    var selectedFormFields = pdfviewer.selectedItems.formFields;
    for (var i = 0; i < selectedFormFields.length; i++) {
        var selectFormFields = selectedFormFields[i];
        if (selectFormFields) {
            pdfviewer.formDesignerModule.updateFormField(selectFormFields, {
                isReadOnly: true,
            });
        }
        args.cancel = false;
    }
}

function setReadOnlyFalse(args) {
    var selectedFormFields = pdfviewer.selectedItems.formFields;
    for (var i = 0; i < selectedFormFields.length; i++) {
        var selectFormFields = selectedFormFields[i];
        if (selectFormFields) {
            pdfviewer.formDesignerModule.updateFormField(selectFormFields, {
                isReadOnly: false,
            });
        }
        args.cancel = false;
    }
}

var defaultCheckBoxObj = new ej.buttons.CheckBox({
    change: contextmenuHelper,
    label: "Hide Default Context Menu"
});
defaultCheckBoxObj.appendTo('#hide');

var positionCheckBoxObj = new ej.buttons.CheckBox({
    change: contextmenuHelper,
    label: "Add Custom option at bottom"
    
});
positionCheckBoxObj.appendTo('#toolbar');

function contextmenuHelper(args) {
    pdfviewer.addCustomMenu(menuItems, defaultCheckBoxObj.checked, positionCheckBoxObj.checked);
}
{% endhighlight %}
{% highlight html tabtitle="index.html" %}
<!DOCTYPE html><html lang="en"><head>
    <title>EJ2 PDF Viewer</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Typescript PDF Viewer Control">
    <meta name="author" content="Syncfusion">
    <link href="index.css" rel="stylesheet">
    <link href="https://cdn.syncfusion.com/ej2/25.1.35/ej2-base/styles/material.css" rel="stylesheet">    
    <link href="https://cdn.syncfusion.com/ej2/25.1.35/ej2-pdfviewer/styles/material.css" rel="stylesheet">
    <link href="https://cdn.syncfusion.com/ej2/25.1.35/ej2-buttons/styles/material.css" rel="stylesheet">
    <link href="https://cdn.syncfusion.com/ej2/25.1.35/ej2-popups/styles/material.css" rel="stylesheet">
    <link href="https://cdn.syncfusion.com/ej2/25.1.35/ej2-navigations/styles/material.css" rel="stylesheet">
    <link href="https://cdn.syncfusion.com/ej2/25.1.35/ej2-dropdowns/styles/material.css" rel="stylesheet">
    <link href="https://cdn.syncfusion.com/ej2/25.1.35/ej2-lists/styles/material.css" rel="stylesheet">
    <link href="https://cdn.syncfusion.com/ej2/25.1.35/ej2-inputs/styles/material.css" rel="stylesheet">    
    <link href="https://cdn.syncfusion.com/ej2/25.1.35/ej2-splitbuttons/styles/material.css" rel="stylesheet">
    <link href="https://cdn.syncfusion.com/ej2/25.1.35/ej2-notifications/styles/material.css" rel="stylesheet">
    
    <!-- Essential JS 2 PDF Viewer's script --> 
    <script src="https://cdn.syncfusion.com/ej2/25.1.35/dist/ej2.min.js" type="text/javascript"></script>
    
</head>
<body>
    
    <div id="container">
        <div>
            <input type="checkbox" id="hide">
        </div>
        <div> 
            <input type="checkbox" id="toolbar">
        </div>
        <div id="PdfViewer" style="height:500px;width:100%;"></div>        
    </div>


<script>
var ele = document.getElementById('container');
if(ele) {
  ele.style.visibility = "visible";
}   
</script>
<script src="index.js" type="text/javascript"></script>
</body></html>
{% endhighlight %}
{% endtabs %}

N> To set up the server-backed PDF Viewer, add the following `serviceUrl` in the `index.ts` file:

`pdfviewer.serviceUrl = 'https://document.syncfusion.com/web-services/pdf-viewer/api/pdfviewer';`



[Custom context menu sample on GitHub](https://github.com/SyncfusionExamples/javascript-pdf-viewer-examples/tree/master/How%20to/Custom%20Context%20Menu)