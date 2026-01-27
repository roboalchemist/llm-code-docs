# Source: https://clickwrap-developer.ironcladapp.com/docs/adding-a-signature-to-embedded-contract.md

# Adding a Signature to an Embedded Contract

How to add a stylized signature or initials block into a document itself

### Overview

While a checkbox or click is often enough to constitute a legally binding acceptance in most jurisdictions, there are occasions when a stylized signature or initials block on the document itself is the preferred method of acceptance. Keep reading to find out how to configure your HTML contracts to include this acceptance method.

### Requirements

To get started, you'll need to ensure that you have the following:

* Ironclad Clickwrap Site Access ID. More info in the [Authentication](https://clickwrap-developer.ironcladapp.com/docs/authentication-2) page.

## Configuring a Contract

### Using the New Experience

1. Login to the app at [clickwrap.pactsafe.com](https://clickwrap.pactsafe.com).
2. On the templates tab, create a new HTML template or edit an existing one. In either case, you should be redirected to [\<https://clickwrap.pactsafe.com/templates/:id/edit>](https://clickwrap.pactsafe.com/templates/:id/edit)
3. Using the WYSIWYG editor, enter in the following example text:

> Hello \{\{name}},\
> Thank you for your business with \{\{company}}. We are very excited to work with you.\
> Please sign below for our records.\
> Signature: \{\{name}}

4. Next from the `...` overflow menu, select the "Toggle Code View" option.
5. Where previously we had the second `{{name}}` block, replace that line with

```html
<div>Signature: <span style="font-family:cursive">{{name}}<span></div>
```

6. Set the contract to `public` if it is not already (so that it can be loaded into an Embedded Contract Group) and publish the Template.
7. Note the Template Key from the sidebar, as we will use it in the next step. For demo purposes, ours is named `signature-example`.

#### Example Advanced styles:

```html
<span style="font-family: 'Lucida Handwriting', cursive;padding: 0 2px; background-color: #c4f4c4;outline: #00ca88 solid 2px;">
```

#### Example Template Preview (in Ironclad Clickwrap)

<Image alt="App Preview of Dynamic Content.png" align="center" src="https://files.readme.io/db2491c-01_App_Preview_of_Dynamic_Content.png" />

### Add Template to a Clickwrap Group

1. Configure a `scroll` style Clickwrap Group ([Create a Clickwrap Group](https://clickwrap-developer.ironcladapp.com/docs/how-to-add-a-terms-of-use-clickwrap-to-a-sign-up-page#step-2-create-a-clickwrap-group)).
2. Add the Template from above (`signature-example`) to this group.
3. Give the Embedded Group a useful Key. For demo purposes, ours is named `signature-group`.
4. For this demo, on the "Embed" tab, set the "HTML Element ID" to `agreements` and click "Publish".

### Testing the signature block

1. For the ease of testing here, go ahead and use this example to setup your page.

```html
<html>
<head>
<meta charset="UTF-8">
<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css">

<script>
  // Note: this points to production! If you are testing on a demo Site, update this url to vault.demo.pactsafe.io
  (function(w,d,s,c,n,a,b){w['PactSafeObject']=n;w[n]=w[n]||function(){(w[n].q=w[n].q||[]).push(arguments)}, w[n].on=function(){(w[n].e=w[n].e||[]).push(arguments)},w[n].once=function(){(w[n].eo=w[n].eo||[]).push(arguments)},w[n].off=function(){(w[n].o=w[n].o||[]).push(arguments)},w[n].t=1*new Date(); a=d.createElement(s),b=d.getElementsByTagName(s)[0];a.async=1;a.src=c;b.parentNode.insertBefore(a,b) })(window,document,'script','//vault.pactsafe.io/ps.min.js','_ps');

  _ps('create', '<Your Clickwrap Site Access ID>');
  _ps('set', 'signer_id', '<Your Signer ID>');

  var renderData = {
    company: '<Your Company Name>',
    name: ''
  };
  _ps('set', 'dynamic', true);
  _ps('set', 'render_data', renderData);

  var groupKey = 'signature-group';
  _ps('load', groupKey);
  _ps.on('rendered', function(){
    document.getElementById('name-input').addEventListener('change', function(evt) {
      renderData.name = evt.target.value;
      _ps(groupKey + ":retrieveHTML", renderData);
    });
  });
</script>
</head>
<body>
  <div class="container">
    <div class="row">
      <div class="twelve columns">
        <h1>Signature Example</h1>
        <div>
          <label for="name">Name</label>
          <input type="text" name="name" id="name-input" />
        </div>
        <div id="agreements"></div>
      </div>
    </div>
  </div>
</body>
</html>

```

2. Save the file as `signature.html`.

#### Testing the signature block

1. On your browser, render `signature.html`.
2. You should now see something like the following:

<Image align="center" src="https://files.readme.io/bec86ef-01_Rendered_Signature.gif" />