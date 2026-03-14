# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/base/CopyPasteBase.md

# [CopyPasteBase](https://bryntum.com/docs/gantt/api/Grid/feature/base/CopyPasteBase)

Base copy-paste functionality for row-based widgets. Not to be used directly.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[copyOnly](https://bryntum.com/docs/gantt/api/Grid/feature/base/CopyPasteBase#config-copyOnly)
If `true` this prevents cutting and pasting. Will default to `true` if [CellEdit](https://bryntum.com/docs/gantt/api/#Grid/feature/CellEdit) feature is disabled. Set to `false` to prevent this behaviour.

[keyMap](https://bryntum.com/docs/gantt/api/Grid/feature/base/CopyPasteBase#config-keyMap)
Default keyMap configuration: Ctrl/Cmd+c to copy, Ctrl/Cmd+x to cut and Ctrl/Cmd+v to paste. These keyboard shortcuts require a selection to be made.

[useNativeClipboard](https://bryntum.com/docs/gantt/api/Grid/feature/base/CopyPasteBase#config-useNativeClipboard)
Set this to `false` to not use native Clipboard API even if it is available

[toCopyString](https://bryntum.com/docs/gantt/api/Grid/feature/base/CopyPasteBase#config-toCopyString)
Provide a function to be able to customize the string value which is copied

```
new Grid({
    features : {
        cellCopyPaste : {
            toCopyString({currentValue, column, record}) {
                if(record.isAvatar){
                    return record.fullName;
                }
                return currentValue;
            }
        }
    }
});
```

Note that this function is only called when copying cell values or copying values from other Bryntum component instances or from native clipboard.

[toPasteValue](https://bryntum.com/docs/gantt/api/Grid/feature/base/CopyPasteBase#config-toPasteValue)
Provide a function to be able to customize the value which will be set onto the record

```
new Grid({
    features : {
        cellCopyPaste : {
            toPasteValue({currentValue, column, record, field}) {
                if(typeof currentValue === 'string'){
                    return currentValue.replace('$', '');
                }
                return currentValue;
            }
        }
    }
});
```

Note that this function is only called when pasting string values, either from CellCopyPaste or copying values from other Bryntum component instances or from native clipboard.

[emptyValueChar](https://bryntum.com/docs/gantt/api/Grid/feature/base/CopyPasteBase#config-emptyValueChar)
If an empty value (null or empty string) is copied or cut, this config will replace that value. This allows for clipboard data to skip columns.

For example, look at these two selections

ROW

0

1

2

3

ROW 1

SEL1

not selected

not selected

SEL2

ROW 2

SEL3

SEL4 (empty)

SEL5 (empty)

SEL6

The clipboardData for `ROW 1` will look like this: `* SEL1\t\t\SEl2\nSEL3\t\t\SEL4`

And `ROW 2` will look like this: `SEL3\t\u{0020}\t\u{0020}\tSEL6`

`ROW 1` will set value `SEL1` at column index 0 and `SEL2` at column index 3. This leaves column index 1 and 2 untouched.

`ROW 2` will set value `SEL3` at column index 0, `u{0020}` at column index 1 and 2, and `SEL`6 at column index 3.

The default `u{0020}` is a blank space.

Note that this only applies when copy-pasting cell values or copying rows from other Bryntum component instances or from native clipboard.

[dateFormat](https://bryntum.com/docs/gantt/api/Grid/feature/base/CopyPasteBase#config-dateFormat)
The format a copied date value should have when converted to a string. To learn more about available formats, check out [DateHelper](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper) docs.

[generateNewName](https://bryntum.com/docs/gantt/api/Grid/feature/base/CopyPasteBase#config-generateNewName)
A method used to generate the name for a copy-pasted record. By defaults appends "- 2", "- 3" as a suffix. Override it to provide your own naming of pasted records.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isCopyPasteBase](https://bryntum.com/docs/gantt/api/Grid/feature/base/CopyPasteBase#property-isCopyPasteBase)
Identifies an object as an instance of [CopyPasteBase](https://bryntum.com/docs/gantt/api/#Grid/feature/base/CopyPasteBase) class, or subclass thereof.

[isCopyPasteBase](https://bryntum.com/docs/gantt/api/Grid/feature/base/CopyPasteBase#property-isCopyPasteBase-static)
Identifies an object as an instance of [CopyPasteBase](https://bryntum.com/docs/gantt/api/#Grid/feature/base/CopyPasteBase) class, or subclass thereof.

[generateNewName](https://bryntum.com/docs/gantt/api/Grid/feature/base/CopyPasteBase#property-generateNewName)
A method used to generate the name for a copy-pasted record. By defaults appends "- 2", "- 3" as a suffix. Override it to provide your own naming of pasted records.

## Functions

Functions are methods available for calling on the class

[cellsToString](https://bryntum.com/docs/gantt/api/Grid/feature/base/CopyPasteBase#function-cellsToString)
Used by CellCopyPaste and RowCopyPaste to generate string representations of grid records

[setFromStringData](https://bryntum.com/docs/gantt/api/Grid/feature/base/CopyPasteBase#function-setFromStringData)
Sets tab and new-line separated string data into records. Used by CellCopyPaste to set values into existing records. Used by RowCopyPaste to create new records from values

[cellSelectorsAs2dArray](https://bryntum.com/docs/gantt/api/Grid/feature/base/CopyPasteBase#function-cellSelectorsAs2dArray)
Converts an array of GridLocation objects to a two-dimensional array where first level is rows and second level is columns. If the array is inconsistent in the number of columns present for each row, the function will return false.

[stringAs2dArray](https://bryntum.com/docs/gantt/api/Grid/feature/base/CopyPasteBase#function-stringAs2dArray)
Converts a new-line- and tab-separated string to a two-dimensional array where first level is rows and second level is columns. If the string is inconsistent in the number of columns present for each row, the function will return false.
