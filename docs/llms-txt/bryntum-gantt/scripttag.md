# Source: https://bryntum.com/products/gantt/docs-llm/guide/Gantt/gettingstarted/scripttag.md

# Loading using `<script>`

## Include script and CSS

To include Bryntum Gantt on your page using a plain old script tag, just include a tag like the following before
including any script that uses the gantt:

```html
<script type="text/javascript" src="path-to-gantt/gantt.umd.js"></script>
```

Also include CSS for the Gantt, FontAwesome (used for the built-in icons) and the theme you want to use on page:

```html
<!-- FontAwesome 6 Free, used for the built-in icons -->
<link rel="stylesheet" type="text/css" href="path-to-gantt/fontawesome/css/fontawesome.css">
<link rel="stylesheet" type="text/css" href="path-to-gantt/fontawesome/css/solid.css">
<!-- Product CSS -->
<link rel="stylesheet" type="text/css" href="path-to-gantt/gantt.css">
<!-- Bryntum theme -->
<link rel="stylesheet" type="text/css" href="path-to-gantt/[theme].css" data-bryntum-theme>
```

## Use it in your code

From your scripts you can access our classes in the global bryntum namespace:

```javascript
var gantt = new bryntum.gantt.Gantt();
```

For a complete example, check out the <a href="../examples/scripttag/" target="_blank">scripttag example</a>.
