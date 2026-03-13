# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/customElements/GridTag.md

# [GridTag](https://bryntum.com/docs/gantt/api/Grid/customElements/GridTag)

Import this file to be able to use the tag <bryntum-grid> to create a grid.

This is more of a proof of concept than a ready to use class. Example:

```
<bryntum-grid>
  <column data-field="name">Name</column>
  <column data-field="city">City</column>
  <column data-field="food">Food</column>
  <data data-id="1" data-name="Daniel" data-city="Stockholm" data-food="Hamburgers"></data>
  <data data-id="2" data-name="Steve" data-city="Lund" data-food="Pasta"></data>
  <data data-id="3" data-name="Sergei" data-city="St Petersburg" data-food="Pizza"></data>
</bryntum-grid>
```

To get styling correct, supply the path to the theme you want to use and to the folder that holds Font Awesome:

```
<bryntum-grid stylesheet="resources/grid.stockholm.css" fa-path="resources/fonts">
</bryntum-grid>
```

Any entries in the tags dataset (attributes starting with `data-`) will be applied as configs of the Grid:

```
<bryntum-grid data-row-height="100">
</bryntum-grid>
```

NOTE: Remember to call [destroy](https://bryntum.com/docs/gantt/api/#Grid/customElements/GridTag#function-destroy) before removing this web component from the DOM to avoid memory leaks.
