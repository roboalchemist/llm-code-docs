# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/widget/ChecklistFilterCombo.md

# [ChecklistFilterCombo](https://bryntum.com/docs/gantt/api/Grid/widget/ChecklistFilterCombo)

A specialized [Combo](https://bryntum.com/docs/gantt/api/#Core/widget/Combo) box that displays its items as a list of checkboxes with a search field and "remove all" button, used for filtering data in Grid columns.

To customize its contents you can:

* Supply [listItemPillTpl](https://bryntum.com/docs/gantt/api/#Grid/widget/ChecklistFilterCombo#config-listItemPillTpl) to render additional information in a pill alongside search results
* Override [listItemTpl](https://bryntum.com/docs/gantt/api/#Grid/widget/ChecklistFilterCombo#config-listItemTpl) to fully control item rendering
* Configure [showApplyButton](https://bryntum.com/docs/gantt/api/#Grid/widget/ChecklistFilterCombo#config-showApplyButton) to control when `change` events are fired
* Reconfigure built-in widgets by providing override configs in the [picker](https://bryntum.com/docs/gantt/api/#Grid/widget/ChecklistFilterCombo#config-picker) config's `tbar`, `bbar`, and `items`
* Configure the [store](https://bryntum.com/docs/gantt/api/#Grid/widget/ChecklistFilterCombo#config-store) to change sorting of results

* Built-in widgets
    ----------------

The built-in `tbar` widgets are:

Widget ref

Type

Weight

Description

`searchField`

[TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField)

100

Search the list (in tbar)

The built-in `items` widgets are:

Widget ref

Type

Weight

Description

`list`

[List](https://bryntum.com/docs/gantt/api/#Core/widget/List)

100

List of selectable options

The built-in `bbar` buttons are:

Widget ref

Type

Weight

Description

`applyButton`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

100

Apply button, on the bbar, updates field value from list selection

`selectAllButton`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

200

Select All button, on the bbar, selects all list items

`removeAllButton`

[Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button)

300

Remove All button, on the bbar, clears all list selections

Removing a built-in item
------------------------

To remove a built-in widget, specify its `ref` as `null` in the `items`, `tbar.items`, or `bbar.items` config:

```
{
    type : 'checklistfiltercombo',
    bbar : {
        items : {
            selectAllButton : null   // Remove the selectAllButton
        }
    }
}
```

Customizing a built-in widget
-----------------------------

To customize a built-in widget, use its `ref` as the key in the `items` config and specify the configs you want to change (they will merge with the widgets default configs):

```
{
    type : 'checklistfiltercombo',
    tbar : {
        items : {
            searchField : {
                placeholder : 'Search items...'
            }
        }
    }
}
```

Use with the FilterBar feature
------------------------------

To use a ChecklistFilterCombo as the filtering UI for a Grid column when using the [FilterBar](https://bryntum.com/docs/gantt/api/#Grid/feature/FilterBar) feature, specify it using `type` in the `filterField` config inside the column's [filterable](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-filterable) config:

```
{
    text       : 'City',
    field      : 'city',
    filterable : {
        filterField : {
            type     : 'checklistfiltercombo',
            operator : 'isIncludedIn'
            // ...any further ChecklistFilterCombo configs
        }
    }
},
```

Note the use of the 'isIncludedIn' operator on the `filterField` to get the expected "or" behavior.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[listItemPillTpl](https://bryntum.com/docs/gantt/api/Grid/widget/ChecklistFilterCombo#config-listItemPillTpl)
Template to render optional content next to list items.

[showApplyButton](https://bryntum.com/docs/gantt/api/Grid/widget/ChecklistFilterCombo#config-showApplyButton)
When `true`, shows an "Apply" button in place of the "Select All" button, and does not raise `change` events until the Apply button is clicked.

[searchText](https://bryntum.com/docs/gantt/api/Grid/widget/ChecklistFilterCombo#config-searchText)
The text in the search box, which will filter the list to matching records only. See also [filterOperator](https://bryntum.com/docs/gantt/api/#Grid/widget/ChecklistFilterCombo#config-filterOperator).

[value](https://bryntum.com/docs/gantt/api/Grid/widget/ChecklistFilterCombo#config-value)
The initial value of this Combo box. An array of record ids.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isChecklistFilterCombo](https://bryntum.com/docs/gantt/api/Grid/widget/ChecklistFilterCombo#property-isChecklistFilterCombo)
Identifies an object as an instance of [ChecklistFilterCombo](https://bryntum.com/docs/gantt/api/#Grid/widget/ChecklistFilterCombo) class, or subclass thereof.

[isChecklistFilterCombo](https://bryntum.com/docs/gantt/api/Grid/widget/ChecklistFilterCombo#property-isChecklistFilterCombo-static)
Identifies an object as an instance of [ChecklistFilterCombo](https://bryntum.com/docs/gantt/api/#Grid/widget/ChecklistFilterCombo) class, or subclass thereof.

[listItemPillTpl](https://bryntum.com/docs/gantt/api/Grid/widget/ChecklistFilterCombo#property-listItemPillTpl)
Template to render optional content next to list items.

[showApplyButton](https://bryntum.com/docs/gantt/api/Grid/widget/ChecklistFilterCombo#property-showApplyButton)
When `true`, shows an "Apply" button in place of the "Select All" button, and does not raise `change` events until the Apply button is clicked.

[searchText](https://bryntum.com/docs/gantt/api/Grid/widget/ChecklistFilterCombo#property-searchText)
The text in the search box, which will filter the list to matching records only. See also [filterOperator](https://bryntum.com/docs/gantt/api/#Grid/widget/ChecklistFilterCombo#config-filterOperator).
