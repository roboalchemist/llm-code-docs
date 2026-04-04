# Source: https://www.telerik.com/kendo-react-ui/components/grid/globalization

Title: React Data Grid Globalization - KendoReact

URL Source: https://www.telerik.com/kendo-react-ui/components/grid/globalization

Markdown Content:
New to KendoReact?[Learn about KendoReact Free.](https://www.telerik.com/kendo-react-ui/components/free)

Updated

on Dec 19, 2025

The globalization process combines the translation of component messages with adapting them to specific locales.

For more information on how globalization practices are implemented in KendoReact, refer to the [overview article](https://www.telerik.com/kendo-react-ui/components/intl). For more information on the globalization aspects which are available for each component, refer to the article on [globalization support](https://www.telerik.com/kendo-react-ui/components/intl/globalization-support).

The following example demonstrates how to:

*   Change the date format and month names to Spanish.
*   Localize the built-in Grid messages.
*   Localize the column header messages.

The key points in the implementation of the above examples are as follows:

1.   Change Grid's built-in messages using the [LocalizationProvider](https://www.telerik.com/kendo-react-ui/components/intl/api/localizationproviderprops) component and the [loadMessages](https://www.telerik.com/kendo-react-ui/components/intl/api/loadmessages) function.

Using the `loadMessages` method as follows will assign the texts in the `esMessages` object to the '**es-ES**' language definition.

jsx 
```
loadMessages(esMessages, 'es-ES');
``` 
Having the above, by changing between the `es-ES` and the default `es-EN` languages(the language prop of the LocalizationProvider), we can switch the built-in messages of the Grid.

jsx 
```
<LocalizationProvider language={locale}>
    ...
    </LocalizationProvider>
``` 
2.   Change Grid's data formatting based on a specific country selection using the [IntlProvider](https://www.telerik.com/kendo-react-ui/components/intl/api/intlproviderprops) component and the [load](https://www.telerik.com/kendo-react-ui/components/intl/api/load) function.

Using the `load` function as follows will load the specific formatting for the Spanish language. You can notice that the **numbers**, **currencies**, **caGregorian**, **dateFields** and **timeZoneNames** are imported from file that has `es` in its URL. If we want to import the formatting configurations for French, for example, we need to update the URL from `es` to `fr`.

js 
```
import likelySubtags from 'cldr-core/supplemental/likelySubtags.json';
    import currencyData from 'cldr-core/supplemental/currencyData.json';
    import weekData from 'cldr-core/supplemental/weekData.json';
    import numbers from 'cldr-numbers-full/main/es/numbers.json';
    import currencies from 'cldr-numbers-full/main/es/currencies.json';
    import caGregorian from 'cldr-dates-full/main/es/ca-gregorian.json';
    import dateFields from 'cldr-dates-full/main/es/dateFields.json';
    import timeZoneNames from 'cldr-dates-full/main/es/timeZoneNames.json';

    load(
    likelySubtags,
    currencyData,
    weekData,
    numbers,
    currencies,
    caGregorian,
    dateFields,
    timeZoneNames
    );
``` 

With the import above, by changing the `locale` prop of the `IntlProvider` component, we can switch between the loaded formatting configurations.

jsx

```
<IntlProvider locale={locale === 'es-ES' ? 'es' : 'en'}>
        .............
     </IntlProvider>
```

[Internationalization](https://www.telerik.com/kendo-react-ui/components/grid/globalization#internationalization)
-----------------------------------------------------------------------------------------------------------------

The internationalization process applies specific culture formats to a web application.

For more information, refer to:

*   [KendoReact documentation on internationalization](https://www.telerik.com/kendo-react-ui/components/intl/i18n)
*   [kendo-intl (the base Internationalization package on GitHub)](https://github.com/telerik/kendo-intl)

[Messages](https://www.telerik.com/kendo-react-ui/components/grid/globalization#messages)
-----------------------------------------------------------------------------------------

The Grid supports the localization of its messages by utilizing the [KendoReact Internationalization package](https://www.telerik.com/kendo-react-ui/components/intl/i18n).

The following table lists the built-in message keys and their default values.

| Message Key | Default Value |
| --- | --- |
| **General Grid Messages** |  |
| `grid.gridAriaLabel` | `Table` |
| `grid.noRecords` | `No records available` |
| `grid.selectRow` | `Select Row` |
| `grid.gridRowReorderAriaLabel` | `Drag row` |
| **Pager Messages** |  |
| `grid.pagerInfo` | `{0} - {1} of {2} items` |
| `grid.pagerFirstPage` | `Go to the first page` |
| `grid.pagerPreviousPage` | `Go to the previous page` |
| `grid.pagerNextPage` | `Go to the next page` |
| `grid.pagerLastPage` | `Go to the last page` |
| `grid.pagerPage` | `Page` |
| `grid.pagerOf` | `of` |
| `grid.pagerTotalPages` | `{0}` |
| `grid.pagerItemsPerPage` | `items per page` |
| `grid.pagerPageSizeAriaLabel` | `Page size` |
| **Search Messages** |  |
| `grid.searchPlaceholder` | `Search` |
| `grid.searchboxPlaceholder` | `Search...` |
| **Column Menu Messages** |  |
| `grid.columnMenu` | `Column menu` |
| `grid.columnMenuColumnChooserSelectedItems` | `Selected items` |
| `grid.adaptiveColumnMenuChooserTitle` | `Columns Chooser` |
| `grid.adaptiveColumnMenuChooserSubTitle` | `Selected fields are visible` |
| `grid.filterApplyButton` | `Apply` |
| `grid.filterSubmitButton` | `Filter` |
| `grid.filterResetButton` | `Reset` |
| `grid.filterCheckAll` | `Check All` |
| `grid.filterSelectAll` | `Select All` |
| `grid.filterSelectedItems` | `selected items` |
| `grid.gridAdaptiveColumnMenuFilterTitle` | `Filter by` |
| `grid.adaptiveColumnMenuCheckboxFilterTitle` | `Filter by` |
| **Sorting Messages** |  |
| `grid.sortAscending` | `Sort Ascending` |
| `grid.sortDescending` | `Sort Descending` |
| `grid.sortAriaLabel` | `Sortable` |
| `grid.sortClearButton` | `Clear sorting` |
| `grid.sortApplyButton` | `Done` |
| **Filter Messages** |  |
| `grid.filterTitle` | `Filter` |
| `grid.filterAriaLabel` | `Filter` |
| `grid.filterClearButton` | `Clear` |
| `grid.filterChooseOperator` | `Choose Operator` |
| `grid.filterClearAllButton` | `Clear all filters` |
| **Filter Operators** |  |
| `grid.filterEqOperator` | `Is equal to` |
| `grid.filterNotEqOperator` | `Is not equal to` |
| `grid.filterIsNullOperator` | `Is null` |
| `grid.filterIsNotNullOperator` | `Is not null` |
| `grid.filterIsEmptyOperator` | `Is empty` |
| `grid.filterIsNotEmptyOperator` | `Is not empty` |
| `grid.filterStartsWithOperator` | `Starts with` |
| `grid.filterContainsOperator` | `Contains` |
| `grid.filterNotContainsOperator` | `Does not contain` |
| `grid.filterEndsWithOperator` | `Ends with` |
| `grid.filterGteOperator` | `Is greater than or equal to` |
| `grid.filterGtOperator` | `Is greater than` |
| `grid.filterLteOperator` | `Is less than or equal to` |
| `grid.filterLtOperator` | `Is less than` |
| `grid.filterIsTrue` | `Is true` |
| `grid.filterIsFalse` | `Is false` |
| `grid.filterBooleanAll` | `(All)` |
| `grid.filterAfterOrEqualOperator` | `Is after or equal to` |
| `grid.filterAfterOperator` | `Is after` |
| `grid.filterBeforeOperator` | `Is before` |
| `grid.filterBeforeOrEqualOperator` | `Is before or equal to` |
| `grid.filterAndLogic` | `And` |
| `grid.filterOrLogic` | `Or` |
| **Grouping Messages** |  |
| `grid.groupPanelEmpty` | `Drag a column header and drop it here to group by that column` |
| `grid.groupPanelAriaLabel` | `Group panel` |
| `grid.groupColumn` | `Group Column` |
| `grid.ungroupColumn` | `Ungroup Column` |
| `grid.groupExpand` | `Expand group` |
| `grid.groupCollapse` | `Collapse Group` |
| `grid.groupClearButton` | `Clear grouping` |
| `grid.groupApplyButton` | `Done` |
| **Detail Row Messages** |  |
| `grid.detailExpand` | `Expand detail row` |
| `grid.detailCollapse` | `Collapse detail row` |
| **Toolbar Messages** |  |
| `grid.toolbarSort` | `Sort` |
| `grid.toolbarGroup` | `Group` |
| `grid.toolbarFilter` | `Filter` |
| `grid.toolbarColumnsChooser` | `Columns` |
| `grid.toolbarCheckboxFilter` | `Filter` |
| `grid.adaptiveToolbarSortTitle` | `Sort by` |
| `grid.adaptiveToolbarGroupTitle` | `Group by` |
| **AI Assistant Messages** |  |
| `grid.toolbarAI` | `AI Assistant` |
| `grid.toolbarAIApply` | `Apply` |
| `grid.aIResponseData` | `Operation is successful. Data is: \n` |
| `grid.generatedWithAI` | `Generated with AI` |
| **Edit Dialog Messages** |  |
| `grid.editDialogTitle` | `Edit Dialog` |
| `grid.editDialogSaveButtonTitle` | `Save` |
| `grid.editDialogCancelButtonTitle` | `Cancel` |
| **Export Messages** |  |
| `grid.exportPDF` | `Export PDF` |

[Right-to-Left Support](https://www.telerik.com/kendo-react-ui/components/grid/globalization#right-to-left-support)
-------------------------------------------------------------------------------------------------------------------

The following example demonstrates how to utilize the RTL support for the Grid.

Loading ...

[Suggested Links](https://www.telerik.com/kendo-react-ui/components/grid/globalization#suggested-links)
-------------------------------------------------------------------------------------------------------

*   [React Data Grid](https://www.telerik.com/kendo-react-ui/components/grid)
*   [Globalization](https://www.telerik.com/kendo-react-ui/components/intl)
*   [Internationalization](https://www.telerik.com/kendo-react-ui/components/intl/i18n)
*   [Localization](https://www.telerik.com/kendo-react-ui/components/intl/l10n)
