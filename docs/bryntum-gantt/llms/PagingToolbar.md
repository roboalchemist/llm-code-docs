# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/PagingToolbar.md

# [PagingToolbar](https://bryntum.com/docs/gantt/api/Core/widget/PagingToolbar)

A special Toolbar class, which, when attached to a [Store](https://bryntum.com/docs/gantt/api/#Core/data/Store), which has been configured to be [paged](https://bryntum.com/docs/gantt/api/#Core/data/Store#property-isPaged), controls the loading of that store to page through the data set.

```
new Grid({
     bbar : {
         type  : 'pagingtoolbar'
     }
});
```

### Default toolbar items

The toolbar provides some default buttons and other items as described below:

Reference

Weight

Description

`firstPageButton`

100

Go to first page

`previousPageButton`

110

Go to previous page

`pageNumber`

120

TextCurrent page number

`pageCount`

130

Label showing number of pages

`nextPageButton`

140

Go to next page

`lastPageButton`

150

Go to last page

`reloadButton`

160

Reload data

`dataSummary`

170

Summary text

### Customizing the toolbar items

The toolbar items can be customized, existing items can be changed or removed, and new items can be added. This is handled using the [items](https://bryntum.com/docs/gantt/api/#Core/widget/PagingToolbar#config-items) config.

Adding additional buttons or widgets to the paging toolbar can be done like so:

```
bbar : {
    type  : 'pagingtoolbar',
    items : {
        click : {
            type : 'button',
            text : 'Click me',
            weight : 175 // Add after last item
        }
    }
}
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[store](https://bryntum.com/docs/gantt/api/Core/widget/PagingToolbar#config-store)
The [Store](https://bryntum.com/docs/gantt/api/#Core/data/Store) that this PagingToolbar is to control. If set to a string value, that string value should represent the property name of the Store's reference on this toolbar's parent component. By default, the toolbar will control the Store found at the parent components 'store' property.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isPagingToolbar](https://bryntum.com/docs/gantt/api/Core/widget/PagingToolbar#property-isPagingToolbar)
Identifies an object as an instance of [PagingToolbar](https://bryntum.com/docs/gantt/api/#Core/widget/PagingToolbar) class, or subclass thereof.

[isPagingToolbar](https://bryntum.com/docs/gantt/api/Core/widget/PagingToolbar#property-isPagingToolbar-static)
Identifies an object as an instance of [PagingToolbar](https://bryntum.com/docs/gantt/api/#Core/widget/PagingToolbar) class, or subclass thereof.
