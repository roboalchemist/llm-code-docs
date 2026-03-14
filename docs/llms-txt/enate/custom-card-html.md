# Source: https://docs.enate.net/enate-help/integrations/enate-integrations/custom-card-content/custom-card-html.md

# Custom Card HTML

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWjcOexbZ7WYX5vQcly%2F-MWjdFnW92AL7rLHX10j%2Fimage.png?alt=media\&token=23b432a5-28ae-4d6c-9aa5-e95076a670f1)

The HTML section is where you can build your UI. We recommend visiting following articles in the Angular.io help files first to learn about how templates work.

* [Template Syntax](https://angular.io/guide/template-syntax)
* [Interpolation](https://angular.io/guide/interpolation)
* [Template Statements](https://angular.io/guide/template-statements)
* [Property Binding](https://angular.io/guide/property-binding)
* [Attribute Binding](https://angular.io/guide/attribute-binding)
* [Event Binding](https://angular.io/guide/event-binding)
* [Two-Way Binding](https://angular.io/guide/two-way-binding)

### Custom Card Directives - View & Update Data Fields <a href="#custom-card-directives-view-and-update-data-fields" id="custom-card-directives-view-and-update-data-fields"></a>

We have created a few directives for different data type fields which allow you to see and update the data field value. Please note that this directive is compatible with the 'disable state', meaning that if a work item is not editable then such fields will be in read-only mode and the user will not be able to update data field values.

1\. For Boolean Fields

```
<en8-checkbox 
    [(ngModel)]="Packet.DataFields.model"
    [Option]="option">
</en8-checkbox>
```

2\. Date & Time Fields

```
<en8-date-time 
    [dateOnly]="boolean" 
    [(ngModel)]="Packet.DataFields.model" 
    [Option]="option">
</en8-date-time>
```

3\. Email Address Fields

```
<en8-email-address 
    [(ngModel)]="Packet.DataFields.model"
    [Option] "option">
</en8-email-address>
```

4\. List Field

```
<en8-list
    [(ngModel)]="packet.datafields.model"
    [options]="options">
</en8-list>
```

5\. Long Text Fields

```
<en8-long-text
    [(ngModel)]="Packet.DataFields.model"
    [Option]="option">
</en8-long-text>
```

6\. Number Fields

```
<en8-number-input
    [step]="stepAmount"
    [(ngModel)]="Packet.DataFields.model"
    [Option]="option">
</en8-number-input>
```

7\. Text Fields

```
<en8-short-text 
    [(ngModel)]="Packet.DataFields.model" 
    [Option]="option">
</en8-short-text>
```

### Sample HTML Code <a href="#sample-html-code" id="sample-html-code"></a>

Here are a couple of examples of HTML code you can write within a Custom Card

1\. Add Input control for text field with basic HTML input control:

```
<div class="form-group">
   <label>
      {{Option?.Card.DataFieldsSchema.model?.Name}}
   </label>
   <input
      [(ngModel)]="Packet.DataFields.model" />
</div>
```

2\. Add Input control for text field with directive control:

```
<div class="form-group">
   <label>
       {{Option?.Card.DataFieldsSchema.model?.Name}}
   </label>
   <en8-short-text 
       [(ngModel)]="Packet.DataFields.model" 
       [Option]="option">
   </en8-short-text>
 </div>

```

Twitter-bootstrap version 4.x.x is being used as as a base CSS, so you can use any component class in your HTML elements and CSS will be applied at runtime. For more information about this, please go to <https://getbootstrap.com/docs/4.6/getting-started/introduction/>
