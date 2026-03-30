# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/track-changes.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/track-changes.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/track-changes.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/track-changes.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/blazor/track-changes.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/track-changes.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/track-changes.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/track-changes.md

# Track Changes in Document Editor Component

Track Changes allows you to keep a record of changes or edits made to a document. You can then choose to accept or reject the modifications. It is a useful tool for managing changes made by several reviewers to the same document. If track changes option is enabled, all editing operations are preserved as revisions in Document Editor.

## Enable track changes in Document Editor

The following example demonstrates how to enable track changes.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}

<ejs-documenteditorcontainer id="container" serviceUrl="/api/DocumentEditor/" enableToolbar=true enableTrackChanges=true created="onCreated" height="590px"></ejs-documenteditorcontainer>

{% endhighlight %}
{% highlight c# tabtitle="Track-changes-only.cs" %}
 public ActionResult Default()
    {
        return View();
    }
   

{% endhighlight %}
{% endtabs %}


>Track changes are document level settings. When opening a document, if the document does not have track changes enabled, then enableTrackChanges will be disabled even if we set enableTrackChanges = true in the initial rendering. If you want to enable track changes for all the documents, then we recommend enabling track changes during the document change event. The following example demonstrates how to enable Track changes for the all the Document while Opening.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-documenteditorcontainer id="container"  documentChange="onDocumentChange" enableToolbar=true serviceUrl="/api/DocumentEditor/" height="590px"></ejs-documenteditorcontainer>
<script>
    function onDocumentChange() {
        var container = document.getElementById("container").ej2_instances[0];
        if(container !== null){
           container.documentEditor.enableTrackChanges= true;
        }
    }
</script>

{% endhighlight %}
{% highlight c# tabtitle="Track-changes-default.cs" %}
 public ActionResult Default()
    {
        return View();
    }
   

{% endhighlight %}
{% endtabs %}


## Show/Hide Revisions Pane
 
The Show/Hide Revisions Pane feature in the Document Editor allows users to toggle the visibility of the revisions pane, providing flexibility in managing tracked changes within the document.
 
The following example code illustrates how to show/hide the revisions pane.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-documenteditorcontainer id="container" serviceUrl="/api/DocumentEditor/" enableToolbar=true    enableTrackChanges=true height="590px"></ejs-documenteditorcontainer>

<script>
    var documenteditor;
    var container;
    var documenteditorElement = document.getElementById("container");
    container = documenteditorElement.ej2_instances[0];
    container.documentEditor.showRevisions = true; // To show revisions pane
    container.documentEditor.showRevisions = false; // To hide revisions pane
</script>

{% endhighlight %}
{% highlight c# tabtitle="Track-changes-only.cs" %}
 public ActionResult Default()
    {
        return View();
    }
   

{% endhighlight %}
{% endtabs %}


## Get all tracked revisions

The following example demonstrate how to get all tracked revision from current document.

```typescript
/**
 * Get revisions from the current document
 */
var revisions  = container.documentEditor.revisions;
```

## Accept or Reject all changes programmatically

The following example demonstrates how to accept/reject all changes.

```typescript
/**
 * Get revisions from the current document
 */
var revisions = container.documentEditor.revisions;

/**
 * Accept all tracked changes
 */
revisions.acceptAll();

/**
 * Reject all tracked changes
 */
revisions.rejectAll();
```

## Accept or reject a specific revision

The following example demonstrates how to accept/reject specific revision in the Document Editor.

```typescript
/**
 * Get revisions from the current document
 */
var revisions  = container.documentEditor.revisions;
/**
 * Accept specific changes
 */
revisions.get(0).accept();
/**
 * Reject specific changes
 */
revisions.get(1).reject();
```

## Navigate between the tracked changes

The following example demonstrates how to navigate tracked revision programmatically.

```typescript
/**
 * Navigate to next tracked change from the current selection.
 */
container.documentEditor.selection.navigateNextRevision();

/**
 * Navigate to previous tracked change from the current selection.
 */
container.documentEditor.selection.navigatePreviousRevision();
```

## Filtering changes based on user

In DocumentEditor, we have built-in review panel in which we have provided support for filtering changes based on the user.

![Track changes](images/track-changes.png)

## Custom metadata along with author

The Document Editor provides options to customize revisions using `revisionSettings`. The `customData` property allows you to attach additional metadata to tracked revisions in the Word Processor. This metadata can represent roles, tags, or any custom identifier for the revision. To display this metadata along with the author name in the Track Changes pane, you must enable the `showCustomDataWithAuthor` property.

The following example code illustrates how to enable and update custom metadata for track changes revisions.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-documenteditorcontainer id="container" documentEditorSettings="settings"  height="590px" enableTrackChanges=true></ejs-documenteditorcontainer>
<script>
    var settings = { revisionSettings: { customData: 'Developer', showCustomDataWithAuthor: true} };
</script>

{% endhighlight %}
{% highlight c# tabtitle="Track-changes-only.cs" %}
 public ActionResult Default()
    {
        return View();
    }
   

{% endhighlight %}
{% endtabs %}

The Track Changes pane will display the author name along with the custom metadata, as shown in the screenshot below.

![Custom metadata along with author](images/track-changes-customData.png)

>Note:
* When you export the document as SFDT, the customData value is stored in the revision collection. When you reopen the SFDT, the custom data is automatically restored and displayed in the Track Changes pane.
* Other than SFDT export (e.g. DOCX and other), the customData is not preserved, as it is specific to the Document Editor component.

## Protect the document in track changes only mode

Document Editor provides support for protecting the document with `RevisionsOnly` protection. In this protection, all the users are allowed to view the document and do their corrections, but they cannot accept or reject any tracked changes in the document. Later, the author can view their corrections and accept or reject the changes.

Document editor provides an option to protect and unprotect document using `enforceProtection` and `stopProtection` API.

The following example code illustrates how to enforce and stop protection in Document editor container.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}

<ejs-documenteditorcontainer id="container" serviceUrl="/api/DocumentEditor/" enableToolbar=true enableTrackChanges=true created="onCreated" height="590px"></ejs-documenteditorcontainer>


<script>
    var documenteditor;
    var container;
    function onCreated() {
        var documenteditorElement = document.getElementById('container');
        container = documenteditorElement.ej2_instances[0];
        documenteditor = container.documentEditor;
        container.documentEditor.editor.enforceProtection('123', 'RevisionsOnly');
        //stop the document protection
        container.documentEditor.editor.stopProtection('123');
    }
</script>
{% endhighlight %}
{% highlight c# tabtitle="Track-changes-only.cs" %}
 public ActionResult Default()
    {
        return View();
    }
   

{% endhighlight %}
{% endtabs %}


Tracked changes only protection can be enabled in UI by using [Restrict Editing pane](https://ej2.syncfusion.com/aspnetcore/documentation/document-editor/document-management#restrict-editing-pane)

![Enable track changes only protection](images/tracked-changes.png)

N> In enforce Protection method, first parameter denotes password and second parameter denotes protection type. Possible values of protection type are `NoProtection |ReadOnly |FormFieldsOnly |CommentsOnly |RevisionsOnly`. In stop protection method, parameter denotes the password.
