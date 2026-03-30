# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/how-to/customize-context-menu.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/how-to/customize-context-menu.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/how-to/customize-context-menu.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/how-to/customize-context-menu.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/blazor/how-to/customize-context-menu.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/how-to/customize-context-menu.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/how-to/customize-context-menu.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/how-to/customize-context-menu.md

# Context menu customization

## How to customize context menu in Document Editor

Document Editor allows to add custom option in context menu. It can be achieved by using the `addCustomMenu()` method and custom action is defined using the `customContextMenuSelect`.

### Add Custom Option


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<div class="control-section">
    <ejs-documenteditorcontainer id="container" serviceUrl="/api/DocumentEditor/" enableToolbar=true created="onCreated" height="590px"></ejs-documenteditorcontainer>
</div>

<script>
  var documenteditor;
  var container;
  function onCreated() {
      var documenteditorElement = document.getElementById("container");
      container = documenteditorElement.ej2_instances[0];
      documenteditor = container.documentEditor;
      // creating Custom Options
      let menuItems = [
          {
              text: 'Search In Google',
              id: 'search_in_google',
              iconCss: 'e-icons e-de-ctnr-find',
          },
      ];
      // adding Custom Options
      container.documentEditor.contextMenu.addCustomMenu(menuItems, false);
      // custom Options Select Event
      container.documentEditor.customContextMenuSelect = function (args) {
          // custom Options Functionality
          let id = container.documentEditor.element.id;
          switch (args.id) {
              case id + 'search_in_google':
                  // To get the selected content as plain text
                  let searchContent =
                      container.documentEditor.selection.text;
                  if (
                      !container.documentEditor.selection.isEmpty &&
                      /\S/.test(searchContent)
                  ) {
                      window.open('http://google.com/search?q=' + searchContent);
                  }
                  break;
          }
      };
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



### Customize custom option in context menu

Document Editor allows to customize the added custom option and also to hide or show default context menu.

#### Hide default context menu items

Using `addCustomMenu()` method, you can hide the default context menu, by setting second parameter as true.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<div class="control-section">
    <ejs-documenteditorcontainer id="container" serviceUrl="/api/DocumentEditor/" enableToolbar=true created="onCreated" height="590px"></ejs-documenteditorcontainer>
</div>

<script>
  var documenteditor;
  var container;
  function onCreated() {
      var documenteditorElement = document.getElementById("container");
      container = documenteditorElement.ej2_instances[0];
      documenteditor = container.documentEditor;
      // creating Custom Options
      let menuItems = [
          {
              text: 'Search In Google',
              id: 'search_in_google',
              iconCss: 'e-icons e-de-ctnr-find',
          },
      ];
      // The second parameter "true" hide the default context menu
      container.documentEditor.contextMenu.addCustomMenu(menuItems, true);
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


#### Customize added context menu items

The following code shows how to hide or show added custom option in context menu using the `customContextMenuBeforeOpen`.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<div class="control-section">
    <ejs-documenteditorcontainer id="container" serviceUrl="/api/DocumentEditor/" enableToolbar=true created="onCreated" height="590px"></ejs-documenteditorcontainer>
</div>
<script>
  var documenteditor;
  var container;
  function onCreated() {
      var documenteditorElement = document.getElementById("container");
      container = documenteditorElement.ej2_instances[0];
      documenteditor = container.documentEditor;
      // creating Custom Options
      let menuItems = [
          {
              text: 'Search In Google',
              id: 'search_in_google',
              iconCss: 'e-icons e-de-ctnr-find',
          },
      ];
      // adding Custom Options
      container.documentEditor.contextMenu.addCustomMenu(menuItems, false);
      // custom Options Select Event
      container.documentEditor.customContextMenuSelect = function (args) {
          // custom Options Functionality
          let id = container.documentEditor.element.id;
          switch (args.id) {
              case id + 'search_in_google':
                  // To get the selected content as plain text
                  let searchContent =
                      container.documentEditor.selection.text;
                  if (
                      !container.documentEditor.selection.isEmpty &&
                      /\S/.test(searchContent)
                  ) {
                      window.open('http://google.com/search?q=' + searchContent);
                  }
                  break;
          }
      };
      //  custom options hide/show functionality
      container.documentEditor.customContextMenuBeforeOpen = function (args) {
          let search = document.getElementById(args.ids[0]);
          search.style.display = 'none';
          let searchContent = container.documentEditor.selection.text;
          if (!container.documentEditor.selection.isEmpty && /\S/.test(searchContent)) {
              search.style.display = 'block';
          }
      };
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


#### Customize Context Menu with sub-menu items

Document Editor allows you to customize the Context Menu with sub-menu items. It can be achieved by using the `addCustomMenu()` method.

The following code shows how to add a sub items in the custom option in context menu in Document Editor Container.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<div class="control-section">
    <ejs-documenteditorcontainer id="container" serviceUrl="/api/DocumentEditor/" enableToolbar=true created="onCreated" height="590px"></ejs-documenteditorcontainer>
</div>
<script>
  var documenteditor;
  var container;
  function onCreated() {
      var documenteditorElement = document.getElementById("container");
      container = documenteditorElement.ej2_instances[0];
      documenteditor = container.documentEditor;
      // creating Custom Options
      let menuItems = [
          {
            text: 'Form field',
            id: 'form field',
            iconCss: 'e-de-formfield e-icons',
            items: [
                {
                text: 'Text form',
                id: 'Text form',
                iconCss: 'e-icons e-de-textform',
                },
                {
                text: 'Check box',
                id: 'Check box',
                iconCss: 'e-icons e-de-checkbox-form',
                },
                {
                text: 'Drop down',
                id: 'Drop down',
                iconCss: 'e-icons e-de-dropdownform',
                },
            ],
          },
      ];
      // adding Custom Options
      container.documentEditor.contextMenu.addCustomMenu(menuItems, false, true);
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

