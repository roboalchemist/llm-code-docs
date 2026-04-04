# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/RowExpander.md

# [RowExpander](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander)

Enables expanding of Grid rows by either row click or double click, or by adding a separate Grid column which renders a button that expands or collapses the row.

The content of the expanded row body is rendered by providing either a [renderer](https://bryntum.com/docs/gantt/api/#Grid/feature/RowExpander#config-renderer) function to the rowExpander feature config:

```
new Grid({
   features : {
       rowExpander : {
           renderer({record, region, expanderElement}){
               return htmlToBeExpanded;
           }
       }
   }
});
```

Or a [widget](https://bryntum.com/docs/gantt/api/#Grid/feature/RowExpander#config-widget) configuration object:

```
new Grid({
   features : {
       rowExpander : {
           widget : {
               type : 'detailGrid',
           },
           dataField : 'orderDetails'
       }
   }
});
```

Note that if used in a Gantt, the Gantt's \`fixedRowHeight\` must be set to \`false\`.

This feature is **disabled** by default

Expand on click
---------------

Set [triggerEvent](https://bryntum.com/docs/gantt/api/#Grid/feature/RowExpander#config-triggerEvent) to a Grid cell event that should trigger row expanding and collapsing.

```
new Grid({
   features : {
       rowExpander : {
           triggerEvent: 'celldblclick',
           renderer...
       }
   }
});
```

Expander column position
------------------------

The expander column can either be inserted before or after the existing Grid columns. If the Grid has multiple regions the column will be added to the first region.

Adjust expander column position to last in a specific Grid region by setting [columnPosition](https://bryntum.com/docs/gantt/api/#Grid/feature/RowExpander#config-columnPosition) to `last` and configuring the [column](https://bryntum.com/docs/gantt/api/#Grid/feature/RowExpander#config-column) with a region name.

```
new Grid({
   features : {
       rowExpander : {
           column: {
               region: 'last'
           },
           columnPosition: 'last',
           renderer...
       }
   }
});
```

Record update
-------------

If the expander content depends on row record data, the expander can be re-rendered on record update by setting [refreshOnRecordChange](https://bryntum.com/docs/gantt/api/#Grid/feature/RowExpander#config-refreshOnRecordChange) to `true`.

```
new Grid({
   features : {
       rowExpander : {
           refreshOnRecordChange: true,
           renderer...
       }
   }
});
```

Async
-----

When the content of the row expander should be rendered async just see to it that you return a promise.

```
new Grid({
   features : {
       rowExpander : {
           async renderer({record, region, expanderElement}){
               return fetchFromBackendAndRenderData(record);
           }
       }
   }
});
```

Multiple regions
----------------

When the Grid has more than one region, the [renderer](https://bryntum.com/docs/gantt/api/#Grid/feature/RowExpander#config-renderer) function will be called once per region for each expanding row.

```
new Grid({
   features : {
       rowExpander : {
           renderer({ record, region }) {
               if(region === 'locked') {
                   return createRowExpander(record);
               }

               return null;
           }
       }
   }
});
```

If you are using the [widget](https://bryntum.com/docs/gantt/api/#Grid/feature/RowExpander#config-widget) configuration, you can provide a widget configuration object for each region like so:

```
new Grid({
   features : {
       rowExpander : {
           widget : {
               locked : {
                   type : 'detailGrid',
                   // If your widgets uses different data sources, put the
                   // dataField property in the widget configuration object
                   dataField : 'orderDetails'
               },
               normal : {
                   type : 'summaryGrid',
                   dataField : 'sumDetails'
               }
           }
       }
   }
});
```

This live demo has a set of buttons in the locked region and a detail grid in the normal region:

If you want your expanded content to span over all Grid regions, set the [spanRegions](https://bryntum.com/docs/gantt/api/#Grid/feature/RowExpander#config-spanRegions) config to `true`.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[renderer](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#config-renderer)
The implementation of this function is called each time the body of an expanded row is rendered. Either return an HTML string, a [DomConfig](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#typedef-DomConfig) object describing the markup or any Widget configuration object, like a Grid configuration object for example.

You should never modify any records inside this method.

```
new Grid({
   features : {
       rowExpander : {
           renderer({record, region, expanderElement}){
               return htmlToBeExpanded;
           }
       }
   }
});
```

Or return a [DomConfig](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#typedef-DomConfig) object.

```
new Grid({
   features : {
       rowExpander : {
           renderer({record, region, expanderElement}){
               return {
                  tag       : 'form',
                  className : 'expanded-row-form',
                  children  : [
                      {
                          tag        : 'textarea',
                          name       : 'description',
                          className  : 'expanded-textarea'
                      },
                      {
                          tag        : 'button',
                          text       : 'Save',
                          className  : 'expanded-save-button',
                      }
                  ]
               };
           }
       }
   }
});
```

Or return a Widget configuration object. What differs a Widget configuration object from a DomConfig object is the presence of the `type` property and the absence of a `tag` property.

```
new Grid({
   features : {
       rowExpander : {
           async renderer({record, region, expanderElement}){
               const myData = await fetch('myURL');
               return {
                  type : 'grid',
                  autoHeight : true,
                  columns : [
                      ...
                  ],
                  data : myData
               };
           }
       }
   }
});
```

It is also possible to add markup directly to the expanderElement.

```
new Grid({
   features : {
       rowExpander : {
           renderer({record, region, expanderElement}){
               new UIComponent({
                   appendTo: expanderElement,
                   ...
               });
           }
       }
   }
});
```

The renderer function can also be asynchronous.

```
new Grid({
   features : {
       rowExpander : {
           async renderer({record, region, expanderElement}){
               return await awaitAsynchronousOperation();
           }
       }
   }
});
```

Please note that returning a Widget configuration object requires access to the Shadow DOM. If your app lives in a sandboxed environment with restrictions on Shadow DOM manipulation, this is not supported. Known example of such environment is the SalesForce Lightning Web Components running without Lightning Web Security enabled.

[triggerEvent](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#config-triggerEvent)
The name of the Grid event that will toggle expander. Defaults to `null` but can be set to any event such as [cellDblClick](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridElementEvents#event-cellDblClick) or [cellClick](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridElementEvents#event-cellClick).

```
features : {
    rowExpander : {
        triggerEvent : 'cellclick'
    }
}
```

[column](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#config-column)
Provide a column config object to display a button with expand/collapse functionality. Shown by default, set to `null` to not include.

```
new Grid({
   features : {
       rowExpander : {
           column: {
               // Use column config options here
               region: 'last'
           }
       }
   }
});
```

[columnPosition](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#config-columnPosition)
Makes the expand/collapse button column appear either as the first column (default or `first`) or as the last (set to `last`). Note that the column by default will be added to the first region, if the Grid has multiple regions. Use the [column](https://bryntum.com/docs/gantt/api/#Grid/feature/RowExpander#config-column) config to change region.

[refreshOnRecordChange](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#config-refreshOnRecordChange)
If set to `true`, the RowExpander will, on record update, re-render an expanded row by calling the [renderer](https://bryntum.com/docs/gantt/api/#Grid/feature/RowExpander#config-renderer) function or recreate the configured [widget](https://bryntum.com/docs/gantt/api/#Grid/feature/RowExpander#config-widget).

[loadingIndicatorHeight](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#config-loadingIndicatorHeight)
Use this for customizing async [renderer](https://bryntum.com/docs/gantt/api/#Grid/feature/RowExpander#config-renderer) loading indicator height.

[loadingIndicatorText](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#config-loadingIndicatorText)
Use this for customizing async [renderer](https://bryntum.com/docs/gantt/api/#Grid/feature/RowExpander#config-renderer) loading indicator text.

[enableAnimations](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#config-enableAnimations)
Use this to disable expand and collapse animations.

[widget](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#config-widget)
A widget configuration object that will be used to create a widget to render into the row expander body. Can be used instead of providing a [renderer](https://bryntum.com/docs/gantt/api/#Grid/feature/RowExpander#config-renderer).

If the widget needs a store, it can be populated by use of the [dataField](https://bryntum.com/docs/gantt/api/#Grid/feature/RowExpander#config-dataField) config. This will create a store from the expanded record's corresponding `dataField` value, which needs to be an array of objects or a store itself.

```
new Grid({
   features : {
       rowExpander : {
           widget : {
               type : 'detailGrid',
           },
           dataField : 'orderDetails'
       }
   }
});
```

If there is multiple regions, you can configure each region like so:

```
new Grid({
    features : {
        rowExpander : {
            widget : {
                // The region name is the property, and its widget config the value
                left : {
                   type : 'detailGrid',
                   // If your widgets uses different data sources, put the dataField
                   //  property in the widget configuration object
                   dataField : 'orderDetails'
               },
               middle : {
                   type : 'summaryGrid',
                   dataField : 'sumDetails
               },
               // No expander here
               right : null
            }
        }
    }
})
```

Please note that usage of this config requires access to the Shadow DOM. If your app lives in a sandboxed environment with restrictions on Shadow DOM manipulation, this is not supported. Known example of such environment is the SalesForce Lightning Web Components running without Lightning Web Security enabled.

[dataField](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#config-dataField)
Used together with [widget](https://bryntum.com/docs/gantt/api/#Grid/feature/RowExpander#config-widget) to populate the widget's Store from the expanded record's corresponding `dataField` value, which needs to be an array of objects or a store itself.

[autoScroll](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#config-autoScroll)
When expanding a row and the expanded body element is not completely in view, setting this to `true` will automatically scroll the expanded row into view.

[spanRegions](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#config-spanRegions)
When the Grid has multiple regions, setting this config to `true` changes how the expanded content is created and rendered. Instead of calling [renderer](https://bryntum.com/docs/gantt/api/#Grid/feature/RowExpander#config-renderer) once per region (or one [widget](https://bryntum.com/docs/gantt/api/#Grid/feature/RowExpander#config-widget) per region) it will only create one expanded element which will span the full grid width regardless of Grid regions.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isRowExpander](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#property-isRowExpander)
Identifies an object as an instance of [RowExpander](https://bryntum.com/docs/gantt/api/#Grid/feature/RowExpander) class, or subclass thereof.

[isRowExpander](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#property-isRowExpander-static)
Identifies an object as an instance of [RowExpander](https://bryntum.com/docs/gantt/api/#Grid/feature/RowExpander) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[toggleExpand](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#function-toggleExpand)
Toggles expanded state.

[onStoreChange](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#function-onStoreChange)
Listens to changes in the Grid Store. Will remove expand State data on Store removal. If the refreshOnRecordChange config is `true`, it will trigger a re-render of the expander.

[beforeRenderRow](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#function-beforeRenderRow)
Hooks on before row render to render or remove row expander content depending on record state.

[scrollRowIntoView](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#function-scrollRowIntoView)
Scrolls expanded row into view. This function is called after rowManager has finished rendering.

[waitForTransition](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#function-waitForTransition)
Waits for height transition on the provided rows element. Then calls provided function.

[renderExpander](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#function-renderExpander)
Creates expander element for each grid region and calls the renderer, also for each grid region.

[renderRowsWithAnimation](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#function-renderRowsWithAnimation)
Called when grid rows needs to re-render, for example on expand or collapse. Activates animations on grid, and deactivates them when they are completed.

[bufferedRenderer](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#function-bufferedRenderer)
Collects a rendering call for each record, saves them in array and calls the delayed (RAF) rafRenderer function

[internalRender](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#function-internalRender)
Re-renders the grid from the topmost record of those saved in bufferedRenderer

[lockCellHeight](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#function-lockCellHeight)
Called when row is expanded. This function locks all cell's height to current height (before expanding).

[expandRow](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#function-expandRow)
Tells the RowExpander that the provided record should be expanded. If or when the record is rendered into view, the record will be expanded.

Promise will resolve when the row gets expanded. Note that this can be much later than the actual expand call, depending on response times and if current record is in view or not.

[collapseRow](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#function-collapseRow)
Tells the RowExpander that the provided record should be collapsed. If the record is in view, it will be collapsed. If the record is not in view, it will simply not be expanded when rendered into view.

[expand](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#function-expand)
Tells the RowExpander that the provided record should be expanded. If or when the record is rendered into view, the record will be expanded.

Promise will resolve when the row gets expanded. Note that this can be much later than the actual expand call, depending on response times and if current record is in view or not.

[collapse](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#function-collapse)
Tells the RowExpander that the provided record should be collapsed. If the record is in view, it will be collapsed. If the record is not in view, it will simply not be expanded when rendered into view.

[refreshRow](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#function-refreshRow)
Tells the RowExpander that the provided expanded record content should be refreshed. If or when the record is rendered into view, the content will be refreshed.

Promise will resolve when the grid gets refreshed. Note that this does not mean that the provided record content has been re-rendered yet, as it could be scrolled out of view.

[getNavigateableColumn](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#function-getNavigateableColumn)
Get the first column that is not the `checkboxSelectionColumn` and not the expander column.

[handleExpanderBodyKeyboardNavigation](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#function-handleExpanderBodyKeyboardNavigation)
Handles keyboard navigation when focus is within an expander body. Arrow keys navigate out of the body back to the grid rows.

[getExpandedRecord](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#function-getExpandedRecord)
Gets the corresponding expanded record from either a nested widget or an element in the expanded body.

[getExpandedWidgets](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#function-getExpandedWidgets)
Gets the expanded widget(s) for a specified record. The widget(s) will be returned as an object with region names as properties and the widgets as values.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeRowExpand](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#event-beforeRowExpand)
This event fires before row expand is started.

Returning `false` from a listener prevents the RowExpander to expand the row.

Note that this event fires when the RowExpander toggles the row, not when the actual row expander body is rendered. Most of the time this is synchronous, but in the case of a row that is not yet rendered into view by scrolling, it can happen much later.

[beforeRowCollapse](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#event-beforeRowCollapse)
This event fires before row collapse is started.

Returning `false` from a listener prevents the RowExpander to collapse the row.

Note that this event fires when the RowExpander toggles the row, not when the actual row expander body is rendered. Most of the time this is synchronous, but in the case of a row that is not yet rendered into view by scrolling, it can happen much later.

[rowExpand](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#event-rowExpand)
This event fires when a row expand has finished expanding.

Note that this event fires when actual row expander body is rendered, and not necessarily in immediate succession of an expand action. In the case of expanding a row that is not yet rendered into view by scrolling, it can happen much later.

[rowCollapse](https://bryntum.com/docs/gantt/api/Grid/feature/RowExpander#event-rowCollapse)
This event fires when a row has finished collapsing.
