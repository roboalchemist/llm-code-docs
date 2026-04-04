# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/column/TreeColumn.md

# [TreeColumn](https://bryntum.com/docs/gantt/api/Grid/column/TreeColumn)

A column that displays a tree structure when using the [Tree](https://bryntum.com/docs/gantt/api/#Grid/feature/Tree) feature.

Default editor is a [TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField).

TreeColumn provides configs to define icons for [expanded](https://bryntum.com/docs/gantt/api/#Grid/column/TreeColumn#config-expandIconCls) / [collapsed](https://bryntum.com/docs/gantt/api/#Grid/column/TreeColumn#config-collapseIconCls) nodes, [expanded folder](https://bryntum.com/docs/gantt/api/#Grid/column/TreeColumn#config-expandedFolderIconCls) / [collapsed folder](https://bryntum.com/docs/gantt/api/#Grid/column/TreeColumn#config-collapsedFolderIconCls) nodes and [leaf](https://bryntum.com/docs/gantt/api/#Grid/column/TreeColumn#config-leafIconCls) nodes.

When the TreeColumn renders its cells, it will look for two special fields [href](https://bryntum.com/docs/gantt/api/#Grid/data/GridRowModel#field-href) and [target](https://bryntum.com/docs/gantt/api/#Grid/data/GridRowModel#field-target). Specifying `href` will produce a link for the TreeNode, and `target` will have the same meaning as in an A tag:

```
{
   id        : 1,
   name      : 'Some external link'
   href      : '//www.website.com",
   target    : '_blank"
}
```

Snippet
-------

```
new TreeGrid({
    appendTo : document.body,

    columns : [
         { type: 'tree', field: 'name' }
    ]
});
```

Cell renderers
--------------

You can affect the contents and styling of cells in this column using a [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/TreeColumn#config-renderer) function.

```
const grid = new Grid({
  columns : [{
      type       : 'tree',
      field      : 'name',
      text       : 'Name',
      renderer({ value, record }) {
        return `${value} (${record.childLevel})`
      }
    }]
});
```

Alternative: tree: true config
------------------------------

Instead of using `type: 'tree'`, you can add tree rendering to any column type by configuring it with `tree: true`:

```
const grid = new TreeGrid({
    columns : [
        // These are equivalent:
        { type: 'tree', field: 'name' },
        { field: 'name', tree: true },

        // Any column type can be a tree column:
        { type: 'resourceInfo', tree: true, field: 'name' },
        { type: 'check', tree: true, field: 'done' }
    ]
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[renderer](https://bryntum.com/docs/gantt/api/Grid/column/TreeColumn#config-renderer)
Renderer function, used to format and style the content displayed in the cell. Return the cell text you want to display. Can also affect other aspects of the cell, such as styling.

As the TreeColumn adds its own cell content to the column, there is a limit to what is supported in the renderer function in comparison with an ordinary [Column renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer). Most notably is that changing \`cellElement\` content can yield unexpected results as it will be updated later in the rendering process.

You can also return a [DomConfig](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#typedef-DomConfig) object describing the markup

```
new Grid({
    columns : [
        {
             type  : 'tree',
             field : 'name'
             text  : 'Name',
             renderer : ({ record }) => {
                 return {
                     class : 'myClass',
                     children : [
                         {
                             tag : 'i',
                             class : 'fa fa-pen'
                         },
                         {
                             tag : 'span',
                             text : record.name
                         }
                     ]
                 };
             }
        }
    ]
});
```

You can modify the row element too from inside a renderer to add custom CSS classes:

```
new Grid({
    columns : [
        {
            type     : 'tree',
            field    : 'name',
            text     : 'Name',
            renderer : ({ record, row }) => {
               // Add special CSS class to new rows that have not yet been saved
              row.cls.newRow = record.isPhantom;

              return record.name;
        }
    ]
});
```

You should never modify any records inside this method.

When using the Bryntum React wrapper, this renderer can also return JSX elements. See [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer) for a JSX example and performance considerations.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTreeColumn](https://bryntum.com/docs/gantt/api/Grid/column/TreeColumn#property-isTreeColumn)
Identifies an object as an instance of [TreeColumn](https://bryntum.com/docs/gantt/api/#Grid/column/TreeColumn) class, or subclass thereof.

[isTreeColumn](https://bryntum.com/docs/gantt/api/Grid/column/TreeColumn#property-isTreeColumn-static)
Identifies an object as an instance of [TreeColumn](https://bryntum.com/docs/gantt/api/#Grid/column/TreeColumn) class, or subclass thereof.

[renderer](https://bryntum.com/docs/gantt/api/Grid/column/TreeColumn#property-renderer)
Renderer function, used to format and style the content displayed in the cell. Return the cell text you want to display. Can also affect other aspects of the cell, such as styling.

As the TreeColumn adds its own cell content to the column, there is a limit to what is supported in the renderer function in comparison with an ordinary [Column renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer). Most notably is that changing \`cellElement\` content can yield unexpected results as it will be updated later in the rendering process.

You can also return a [DomConfig](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#typedef-DomConfig) object describing the markup

```
new Grid({
    columns : [
        {
             type  : 'tree',
             field : 'name'
             text  : 'Name',
             renderer : ({ record }) => {
                 return {
                     class : 'myClass',
                     children : [
                         {
                             tag : 'i',
                             class : 'fa fa-pen'
                         },
                         {
                             tag : 'span',
                             text : record.name
                         }
                     ]
                 };
             }
        }
    ]
});
```

You can modify the row element too from inside a renderer to add custom CSS classes:

```
new Grid({
    columns : [
        {
            type     : 'tree',
            field    : 'name',
            text     : 'Name',
            renderer : ({ record, row }) => {
               // Add special CSS class to new rows that have not yet been saved
              row.cls.newRow = record.isPhantom;

              return record.name;
        }
    ]
});
```

You should never modify any records inside this method.

When using the Bryntum React wrapper, this renderer can also return JSX elements. See [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer) for a JSX example and performance considerations.
