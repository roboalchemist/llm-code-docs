# Source: https://ag-grid.com/react-data-grid/component-filter/

Title: React Grid: Filter Component | AG Grid

URL Source: https://ag-grid.com/react-data-grid/component-filter/

Markdown Content:
[![Image 1: React Custom Filter Components thumbnail](https://img.youtube.com/vi/98JVaTcoexc/0.jpg)](https://www.youtube.com/watch?v=98JVaTcoexc)

The example below shows a custom filter on the `Athlete` column with "fuzzy" matching.

Implementing a Filter Component [Copy Link](https://ag-grid.com/react-data-grid/component-filter/#implementing-a-filter-component)
----------------------------------------------------------------------------------------------------------------------------------

To configure custom filters, first enable the grid option `enableFilterHandlers`.

If you do not enable the grid option `enableFilterHandlers`, it is still possible to use custom filters, however this will involve embedding your filter logic into the custom component, and is not recommended. See [Legacy Filter Component](https://ag-grid.com/react-data-grid/component-filter-legacy/).

Implementing a custom filter requires two parts:

*   The custom filter component which will be displayed to the user.
*   The the logic to run the filter.

Custom filter components are controlled components, which receive a filter model as part of the props, and pass model updates back to the grid via the `onModelChange` callback.

A filter model of `null` means that no filter is applied (the filter displays as inactive). Note that the filter is applied immediately when `onModelChange` is called. This behaviour can be changed by [Using Buttons](https://ag-grid.com/react-data-grid/component-filter/#using-buttons).

```
export default ({ model, onModelChange, getValue }) => {
    return (
        <div>
            <input
                type="text"
                value={model || ''}
                onChange={({ target: { value }}) => onModelChange(value === '' ? null : value)}
            />
        </div>
    );
}
```

Custom Filter Parameters [Copy Link](https://ag-grid.com/react-data-grid/component-filter/#custom-filter-parameters)
--------------------------------------------------------------------------------------------------------------------

### Filter Props [Copy Link](https://ag-grid.com/react-data-grid/component-filter/#filter-props)

The following props are passed to the custom filter components (`CustomFilterDisplayProps` interface). If custom props are provided via the `colDef.filterParams` property, these will be additionally added to the props object, overriding items of the same name if a name clash exists.

TModel | null

The current applied filter model for the component.
FilterDisplayState<TModel, TState>

The current state to display in the component.
Function

Callback that should be called every time the model in the component changes. `additionalEventAttributes` If provided, will be passed to the filter changed event
Function

If using the filter with apply buttons, callback that should be called every time the unapplied model in the component changes.
Function

Can be called to manually apply any of the filter actions that would be done via buttons. `additionalEventAttributes` If provided, will be passed to the filter changed event `event` If the action was via the keyboard, provide the event here for correct focus handling.
Function

Callback that can be optionally called every time the filter UI changes. The grid will respond with emitting a FilterUiChangedEvent. Apart from emitting the event, the grid takes no further action. The callback takes one optional parameter which, if included, will get merged to the FilterUiChangedEvent object.
get Handler

[Copy Link](https://ag-grid.com/react-data-grid/component-filter/#reference-CustomFilterDisplayProps-getHandler)

Function

Get the filter handler instance. If using a `SimpleColumnFilter`, the handler is is a wrapper object containing the provided `doesFilterPass` callback.
FilterDisplaySource

FilterDisplaySource
any

If this refresh was as a result of the filter triggering an update with additional event attributes, these will be set here
column

[Copy Link](https://ag-grid.com/react-data-grid/component-filter/#reference-CustomFilterDisplayProps-column)

[Column](https://ag-grid.com/react-data-grid/column-object/)

The column this filter is for.
[ColDef](https://ag-grid.com/react-data-grid/column-properties/)

The column definition for the column.
Function

Get the cell value for the given row node and column, which can be the column ID, definition, or `Column` object. If no column is provided, the column this filter is on will be used.
Function

A function callback, call with a node to be told whether the node passes all filters except the current filter. This is useful if you want to only present to the user values that this filter can filter given the status of the other filters. The set filter uses this to remove from the list, items that are no longer available due to the state of other filters (like Excel type filtering).
[GridApi](https://ag-grid.com/react-data-grid/grid-api/)

The grid api.
[TContext](https://ag-grid.com/react-data-grid/typescript-generics/#context-tcontext)

Application context as set on `gridOptions.context`.

### Filter Callbacks [Copy Link](https://ag-grid.com/react-data-grid/component-filter/#filter-callbacks)

The following callbacks can be passed to the `useGridFilterDisplay` hook (`CustomFilterDisplayCallbacks` interface). All the callbacks are optional. The hook only needs to be used if callbacks are provided.

Function

Optional: A hook to perform any necessary operation just after the GUI for this component has been rendered on the screen. If a parent popup is closed and reopened (e.g. for filters), this method is called each time the component is shown. This is useful for any logic that requires attachment before executing, such as putting focus on a particular DOM element.
Function

Optional: A hook to perform any necessary operation just after the GUI for this component has been removed from the screen. If a parent popup is opened and closed (e.g. for filters), this method is called each time the component is hidden. This is useful for any logic to reset the UI state back to the model before the component is reopened.
Function

Optional: Gets called when new rows are inserted into the grid. If the filter needs to change its state after rows are loaded, it can do it here. For example the set filters uses this to update the list of available values to select from (e.g. 'Ireland', 'UK' etc for Country filter). To get the list of available values from within this method from the Client Side Row Model, use `gridApi.forEachLeafNode(callback)`.
Function

Optional: Called whenever any filter is changed.

Filter Logic [Copy Link](https://ag-grid.com/react-data-grid/component-filter/#filter-logic)
--------------------------------------------------------------------------------------------

The logic to run the filter can be provided in one of two ways:

*   As a `doesFilterPass` callback for simple filter cases.
*   As a filter handler object for more complex filter cases.

The logic is passed via the `filter` property along with the custom component as a `ColumnFilter` object.

component

[Copy Link](https://ag-grid.com/react-data-grid/component-filter/#reference-ColumnFilter-component)

any

Filter component to use for this column.

*    Set to the name of a provided filter: `agNumberColumnFilter`, `agBigIntColumnFilter`, `agTextColumnFilter`, `agDateColumnFilter`, `agMultiColumnFilter`, `agSetColumnFilter`. 
*    Set to a custom filter `FilterDisplay`
does Filter Pass

[Copy Link](https://ag-grid.com/react-data-grid/component-filter/#reference-ColumnFilter-doesFilterPass)

Function

Contains the logic for executing the filter. If the filter is active, will be called for each row in the grid to see if it passes. If any filter fails, then the row will be excluded from the final set. Not required if providing a `handler`, or if not using Client-Side Row Model.
handler

[Copy Link](https://ag-grid.com/react-data-grid/component-filter/#reference-ColumnFilter-handler)

string | CreateFilterHandlerFunc<TData, TValue, TContext, TModel, TCustomParams>

Returns a handler which contains the logic for executing the filter. Allows for more complex filter cases than `doesFilterPass`. Not required if providing `doesFilterPass` (but will take precedence), or if not using Client-Side Row Model.

The filter logic is only used with the [Client-Side Row Model](https://ag-grid.com/react-data-grid/row-models/). If being used exclusively with other row models, it does not need to be provided as the filtering logic is performed on the server. If a handler is provided, it will still be instantiated, but `doesFilterPass` will not be called.

### doesFilterPass Callback [Copy Link](https://ag-grid.com/react-data-grid/component-filter/#doesfilterpass-callback)

```
const [columnDefs, setColumnDefs] = useState([
    {
        field: 'year',
        filter: {
            component: YearFilter, // custom filter component
            doesFilterPass: (params) => {
                // evaluate filter for row here
                return model === params.handlerParams.getValue(params.node);
            },
        },
    }
]);

<AgGridReact columnDefs={columnDefs} />
```

The callback `doesFilterPass(params)` will be called for each row when filtering is performed (and the filter is active), and takes the following as a parameter:

TModel

TModel
handler Params

[Copy Link](https://ag-grid.com/react-data-grid/component-filter/#reference-DoesFilterPassParams-handlerParams)

FilterHandlerBaseParams<TData, TContext, TModel, TCustomParams>

Utility params that would be passed to the handler, including `getValue` which provides access to the cell values.
[IRowNode](https://ag-grid.com/react-data-grid/row-object/)

The row node in question.
[TData](https://ag-grid.com/react-data-grid/typescript-generics/#row-data-tdata)

The data part of the row node in question.

### Filter Handler [Copy Link](https://ag-grid.com/react-data-grid/component-filter/#filter-handler)

```
const [columnDefs, setColumnDefs] = useState([
    {
        field: 'year',
        filter: {
            component: YearFilter, // custom filter component
            handler: (params) => ({
                doesFilterPass: (params) => {
                    // evaluate filter for row here
                    return passes;
                },
                // other handler methods
            }),
        },
    }
]);

<AgGridReact columnDefs={columnDefs} />
```

The filter handler function should return a `FilterHandler` which will be created when the filter is active. The `doesFilterPass` method on the evaluator will be called for each row when filtering is performed (and the filter is active).

The filter handler is useful for when the filter model needs parsing to allow for fast comparison of values. The handler is passed the latest filter model via the `init` / `refresh` methods, which can then process the model before `doesFilterPass` is called.

init

[Copy Link](https://ag-grid.com/react-data-grid/component-filter/#reference-FilterHandler-init)

Function

Optional: Called once when the handler is created.
refresh

[Copy Link](https://ag-grid.com/react-data-grid/component-filter/#reference-FilterHandler-refresh)

Function

Optional: Called every time the handler is updated, e.g. when the model changes.
does Filter Pass

[Copy Link](https://ag-grid.com/react-data-grid/component-filter/#reference-FilterHandler-doesFilterPass)

Function

The grid will ask each active filter, in turn, whether each row in the grid passes. If any filter fails, then the row will be excluded from the final set.
get Model As String

[Copy Link](https://ag-grid.com/react-data-grid/component-filter/#reference-FilterHandler-getModelAsString)

Function

Optional: Used by AG Grid when rendering floating filters and there isn't a floating filter associated for this filter, this will happen if you create a custom filter and NOT a custom floating filter.
process Model To Apply

[Copy Link](https://ag-grid.com/react-data-grid/component-filter/#reference-FilterHandler-processModelToApply)

Function

Optional: When using an apply button with the filter, this method will be called before the apply happens, The returned model will be applied, allowing for any validation or updates to be performed.
destroy

[Copy Link](https://ag-grid.com/react-data-grid/component-filter/#reference-FilterHandler-destroy)

Function

Optional: Gets called once by grid when the component is being removed; if your component needs to do any cleanup, do it here
on New Rows Loaded

[Copy Link](https://ag-grid.com/react-data-grid/component-filter/#reference-FilterHandler-onNewRowsLoaded)

Function

Optional: Gets called when new rows are inserted into the grid. If the filter needs to change its state after rows are loaded, it can do it here. For example the set filters uses this to update the list of available values to select from (e.g. 'Ireland', 'UK' etc for Country filter). To get the list of available values from within this method from the Client Side Row Model, use `gridApi.forEachLeafNode(callback)`.
on Any Filter Changed

[Copy Link](https://ag-grid.com/react-data-grid/component-filter/#reference-FilterHandler-onAnyFilterChanged)

Function

Optional: Called whenever any filter is changed.

It is also possible to define filter handlers in the `filterHandlers` grid option, and then refer to them by the string key in the column definition.

filter Handlers

[Copy Link](https://ag-grid.com/react-data-grid/component-filter/#reference-filter-filterHandlers)

FilterHandlers

[Initial](https://ag-grid.com/react-data-grid/grid-interface/#initial-grid-options)

A map of filter handler key to filter handler function. Allows for filter handler keys to be used in `colDef.filter.handler`.

Using Buttons [Copy Link](https://ag-grid.com/react-data-grid/component-filter/#using-buttons)
----------------------------------------------------------------------------------------------

It is possible to use the [Filter Buttons](https://ag-grid.com/react-data-grid/filter-applying/) for grid-provided filters with custom filter components.

The example above demonstrates using filters with buttons via the same custom filter component:

*   The **Year Default** column does not use buttons.
*   The **Year Apply** column uses the apply button, and additionally closes the filter popup on apply.
*   The **Year Reset** column uses the reset button, which will set the filter back to the default model and apply it.

The buttons are configured by passing additional parameters to the filter (interface `FilterWrapperParams`).

FilterAction[]

Specifies the buttons to be shown in the filter, in the order they should be displayed in. The options are:

*   `'apply'`: If the Apply button is present, the filter is only applied after the user hits the Apply button. 
*   `'clear'`: The Clear button will clear the (form) details of the filter without removing any active filters on the column. 
*   `'reset'`: The Reset button will clear the details of the filter and any active filters on that column. 
*   `'cancel'`: The Cancel button will discard any changes that have been made to the filter in the UI, restoring the applied model.
boolean

default: false

When this is set to `true`, the following will happen after clicking a filter button:

*    Apply closes popup. 
*    Reset closes popup if Apply button is present. 
*    Cancel closes popup.

When the buttons are pressed, the custom filter `state` parameter will be updated via the `refresh(params)` method, with `state.model` being the model that should be displayed in the filter.

With the `Apply` button present, the filter component no longer needs to call `onModelChange(model)` as the grid will apply the model when the button is clicked (although it can still be called if the component wants to apply a model in some other way). Instead, the filter component will call `onStateChange({ model })` with the model that is currently displayed in the filter component. This is the model that the grid will apply when the button is clicked. If the filter is being used without buttons, it can also call `onAction('apply')` to apply the model set via the state.

Associating Floating Filter [Copy Link](https://ag-grid.com/react-data-grid/component-filter/#associating-floating-filter)
--------------------------------------------------------------------------------------------------------------------------

If you create your own filter you have two options to get floating filters working for that filter:

1.   You can create your own [Custom Floating Filter](https://ag-grid.com/react-data-grid/component-floating-filter/).
2.   You can implement the `getModelAsString()` method on your filter evaluator. If you implement this method and don't provide a custom floating filter, AG Grid will automatically provide a read-only version of a floating filter. See [Custom Filter And Read-Only Floating Filter](https://ag-grid.com/react-data-grid/component-floating-filter/#example-custom-filter-and-read-only-floating-filter).

If you don't provide either of these two options for your custom filter, the display area for the floating filter will be empty.

Sometimes you will need to create custom components for your filters that also contain popup elements. This is the case for Date Filter as it pops up a Date Picker. If the library you use anchors the popup element outside of the parent filter, then when you click on it the grid will think you clicked outside of the filter and hence close the column menu.

There are two ways you can get fix this problem:

*   Add a mouse click listener to your floating element and set it to `preventDefault()`. This way, the click event will not bubble up to the grid. This is the best solution, but you can only do this if you are writing the component yourself.
*   Add the `ag-custom-component-popup` CSS class to your floating element. An example of this usage can be found here: [Custom Date Component](https://ag-grid.com/react-data-grid/filter-date/#custom-selection-component)

Using Custom Filters with Grid-Provided Filter Logic [Copy Link](https://ag-grid.com/react-data-grid/component-filter/#using-custom-filters-with-grid-provided-filter-logic)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It is possible to use the grid-provided filter logic with custom filter components.

```
const [columnDefs, setColumnDefs] = useState([
    {
        field: 'year',
        filter: {
            component: YearFilter, // custom filter component
            handler: 'agNumberColumnFilterHandler', // grid-provided Number Filter handler
        },
    }
]);

<AgGridReact columnDefs={columnDefs} />
```

The grid-provided handlers are:

*   `'agTextColumnFilterHandler'` - [Text Filter](https://ag-grid.com/react-data-grid/filter-text/) handler.
*   `'agNumberColumnFilterHandler'` - [Number Filter](https://ag-grid.com/react-data-grid/filter-number/) handler.
*   `'agBigIntColumnFilterHandler'` - [BigInt Filter](https://ag-grid.com/react-data-grid/filter-bigint/) handler.
*   `'agDateColumnFilterHandler'` - [Date Filter](https://ag-grid.com/react-data-grid/filter-date/) handler.

The example below demonstrates using the Number Filter handler with a custom filter component:

Accessing the Component Instance [Copy Link](https://ag-grid.com/react-data-grid/component-filter/#accessing-the-component-instance)
------------------------------------------------------------------------------------------------------------------------------------

AG Grid allows you to get a reference to the filter component instances via `api.getColumnFilterInstance(colKey)`. This returns a wrapper component that matches the provided grid filter components that implement `FilterDisplay`. To get the React custom filter component, the helper function `getInstance` can be used with this. As React components are created asynchronously, it is necessary to use a callback for both methods.

Similarly, you can get a reference to the filter handler via `api.getColumnFilterHandler(colKey)`.

```
// let's assume a React component as follows
export default forwardRef((props, ref) => {
    useImperativeHandle(ref, () => {
        return {
            ... // required filter methods

            // put a custom method on the filter
            myMethod() {
                // does something
            }
        }
    });

    ... // rest of component
}

// later in your app, if you want to execute myMethod()...
laterOnInYourApplicationSomewhere() {
    // get reference to the AG Grid Filter component on name column
    api.getColumnFilterInstance('name').then(filterInstance => {
        getInstance(filterInstance, comp => {
            if (comp != null) {
                comp.myMethod();
            }
        });
    });
}
```

The example below illustrates how a custom filter component can be accessed and methods on it invoked. If you click on the `Invoke Filter Instance Method` button, it will invoke the instance `componentMethod`, which logs to the developer console.

Console logs from the example shown here...
