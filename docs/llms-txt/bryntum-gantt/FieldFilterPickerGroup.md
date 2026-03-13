# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/FieldFilterPickerGroup.md

# [FieldFilterPickerGroup](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup)

A set of [FieldFilterPicker](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPicker)s, representing an array of [CollectionFilter](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter)s. The filters are provided to the picker as an array of filter configuration objects.

When [store](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPickerGroup#config-store) is provided in the configuration, the picker group will read filters from the store and monitor for filter changes, and reflect any changes. It is possible to synchronize multiple [FieldFilterPickerGroup](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPickerGroup)s by configuring them with the same store.

Does not support modifying filters defined as custom functions.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[filters](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#config-filters)
Array of [CollectionFilter](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter) configuration objects. One [FieldFilterPicker](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPicker) will be created for each object in the array.

When [store](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPickerGroup#config-store) is provided, any filters in the store will be automatically added and do not need to be provided explicitly.

Example:

```
filters: [{
    // Filter properties should exist among field names configured
    // via `fields` or `store`
    property: 'age',
    operator: '<',
    value: 30
},{
    property: 'title',
    operator: 'startsWith',
    value: 'Director'
}]
```

[fields](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#config-fields)
Dictionary of [FieldOption](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPicker#typedef-FieldOption) representing the fields against which filters can be defined, keyed by field name.

If filtering a [Grid](https://bryntum.com/docs/gantt/api/#Grid/view/Grid), consider using [GridFieldFilterPicker](https://bryntum.com/docs/gantt/api/#Grid/widget/GridFieldFilterPicker), which can be configured with an existing [Grid](https://bryntum.com/docs/gantt/api/#Grid/view/Grid) instead of, or in combination with, defining fields manually.

Example:

```
fields: {
    // Allow filters to be defined against the 'age' and 'role' fields in our data
    age  : { text: 'Age', type: 'number' },
    role : { text: 'Role', type: 'string' }
}
```

[disabled](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#config-disabled)
Whether the picker group is disabled.

[readOnly](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#config-readOnly)
Whether the picker group is read-only.

Example: fields: \[ { name: 'age', type: 'number' }, { name: 'title', type: 'string' } \]

[store](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#config-store)
The [Store](https://bryntum.com/docs/gantt/api/#Core/data/Store) whose records will be filtered. The store's [modelClass](https://bryntum.com/docs/gantt/api/#Core/data/Store#property-modelClass) will be used to determine field types.

This store will be kept in sync with the filters defined in the picker group, and new filters added to the store via other means will appear in this filter group when they are able to be modified by it. (Some types of filters, like arbitrary filter functions, cannot be managed through this widget.)

As a corollary, multiple `FieldFilterPickerGroup`s configured with the same store will stay in sync, showing the same filters as the store's filters change.

[limitToProperty](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#config-limitToProperty)
When `limitToProperty` is set to the name of an available field (as specified either explicitly in [fields](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPickerGroup#config-fields) or implicitly in the [store](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPickerGroup#config-store)'s model), it has the following effects:

* the picker group will only show filters defined on the specified property
* it will automatically set the `property` to the specified property for all newly added filters where the property is not already set
* the property selector is made read-only

[valueFieldCls](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#config-valueFieldCls)
Optional CSS class to apply to the value field(s).

[showAddFilterButton](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#config-showAddFilterButton)
Show a button at the bottom of the group that adds a new, blank filter to the group.

[canDeleteFilter](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#config-canDeleteFilter)
Optional predicate that returns whether a given filter can be deleted. When `canDeleteFilter` is provided, it will be called for each filter and will not show the delete button for those for which the function returns `false`.

[getFieldFilterPickerConfig](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#config-getFieldFilterPickerConfig)
Optional function that returns [FieldFilterPicker](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPicker) configuration properties for a given filter. When `getFieldFilterPickerConfig` is provided, it will be called for each filter and the returned object will be merged with the configuration properties for the individual [FieldFilterPicker](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPicker) representing that filter.

The supplied function should accept a single argument, the [CollectionFilter](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter) whose picker is being created.

[canManageFilter](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#config-canManageFilter)
Optional predicate that returns whether a given filter can be managed by this widget. When `canManageFilter` is provided, it will be used to decide whether to display filters found in the configured [store](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPickerGroup#config-store).

[addFilterButtonText](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#config-addFilterButtonText)
Sets the text displayed in the 'add filter' button if one is present.

[triggerChangeOnInput](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#config-triggerChangeOnInput)
Whether to raise [change](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPickerGroup#event-change) events as the user types into a value field. If `false`, [change](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPickerGroup#event-change) events will be raised only when the value input field's own `change` event occurs, for example on field blur.

[allowedFieldNames](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#config-allowedFieldNames)
Optional array of field names that are allowed as selectable properties for filters. This should be a subset of the field names found in the [store](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPickerGroup#config-store). When supplied, only the named fields will be shown in the property selector combo.

[operators](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#config-operators)
When specified, overrides the built-in list of available operators. See [operators](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPicker#config-operators).

[dateFormat](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#config-dateFormat)
The date format string used to display dates when using the 'is one of' / 'is not one of' operators with a date field. Defaults to the current locale's `FieldFilterPicker.dateFormat` value.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isFieldFilterPickerGroup](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#property-isFieldFilterPickerGroup)
Identifies an object as an instance of [FieldFilterPickerGroup](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPickerGroup) class, or subclass thereof.

[isFieldFilterPickerGroup](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#property-isFieldFilterPickerGroup-static)
Identifies an object as an instance of [FieldFilterPickerGroup](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPickerGroup) class, or subclass thereof.

[addFilterButtonDefaultText](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#property-addFilterButtonDefaultText)

[items](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#property-items)

[value](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#property-value)
Returns the array of filter configuration objects currently represented by this picker group.

## Functions

Functions are methods available for calling on the class

[appendFiltersFromStore](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#function-appendFiltersFromStore)
Find any filters the store has that we don't know about yet, and add to our list

[canManage](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#function-canManage)

[getFilterPickerConfig](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#function-getFilterPickerConfig)
Get the configuration object for one child FieldFilterPicker.

[getFieldsFromStore](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#function-getFieldsFromStore)
Get store fields as [FieldOption](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPicker#typedef-FieldOption)s in a dictionary keyed by name.

[getFilterPicker](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#function-getFilterPicker)
Return the [FieldFilterPicker](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPicker) for the filter at the specified index.

[addFilter](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#function-addFilter)
Appends a filter at the bottom of the list.

[appendFilter](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#function-appendFilter)

[removeFilterAt](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#function-removeFilterAt)
Remove the filter at the given index.

[updateStoreFilter](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#function-updateStoreFilter)
Trigger a store re-filter after filters have been silently modified.

[activateAll](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#function-activateAll)
Sets all current filters to enabled and checks their checkboxes.

[deactivateAll](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#function-deactivateAll)
Sets all current filters to disabled and clears their checkboxes.

[setAllActiveStatus](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#function-setAllActiveStatus)

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeAddFilter](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#event-beforeAddFilter)
Fires before a new filter is added to the picker group (and its store, if configured and the filter is valid). Return `false` from the event handler to prevent the filter being added.

[change](https://bryntum.com/docs/gantt/api/Core/widget/FieldFilterPickerGroup#event-change)
Fires when any filter in the group is added, removed, or modified.
