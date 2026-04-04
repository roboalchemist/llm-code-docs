# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/angular/how-to/enable-disable-annotation.md

# How to enable and disable the delete button based on annotation selection and unselection events

In the Syncfusion<sup style="font-size:70%">&reg;</sup> PDF viewer, enable and disable the delete button while selecting and unselecting annotations by using the **annotationSelect** and **annotationUnSelect** events.

Here is an example of how you can enable and disable the delete button while selecting and unselecting annotations:

{% tabs %}
{% highlight html tabtitle="Standalone" %}

<ejs-pdfviewer #pdfviewer id='pdfViewer'
    [documentPath]='document'
    [enableToolbar]=false
    [enableNavigationToolbar]=false
    (annotationSelect)="annotationSelect($event)"
    (annotationUnSelect)="annotationUnSelect($event)"
    style="height:640px; display: block">
</ejs-pdfviewer>

{% endhighlight %}
{% highlight html tabtitle="Server-Backed" %}

<ejs-pdfviewer #pdfviewer id='pdfViewer'
    [serviceUrl]='service'
    [documentPath]='document'
    [enableToolbar]=false
    [enableNavigationToolbar]=false
    (annotationSelect)="annotationSelect($event)"
    (annotationUnSelect)="annotationUnSelect($event)"
    style="height:640px; display: block">
</ejs-pdfviewer>

{% endhighlight %}
{% endtabs %}

```html
<ejs-toolbar id='topToolbar' #customToolbar>
    <e-item
        prefixIcon="e-delete-1"
        tooltipText="Delete annotation"
        id ="DeleteButton"
        disabled="true"
        (click)="deleteSelectedAnnotation()">
    </e-items>
</ejs-toolbar>
```

```typescript

public annotationSelect(e:Â any):Â voidÂ {
Â Â Â Â this.customToolbar.items[1].disabledÂ =Â false;
}

public annotationUnSelect(e:Â any):Â voidÂ {
Â Â Â Â this.customToolbar.items[1].disabledÂ =Â true;
}

public deleteSelectedAnnotation():Â voidÂ {
    this.pdfviewerControl.annotation.deleteAnnotation();
Â Â Â Â this.customToolbar.items[1].disabledÂ =Â true;
}

```

Find the sample [how to enable and disable the delete button while selecting and unselecting annotations](https://stackblitz.com/edit/angular-g94gvs-hsrjna?file=app.component.ts).