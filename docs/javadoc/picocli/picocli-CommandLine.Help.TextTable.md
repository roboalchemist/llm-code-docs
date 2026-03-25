JavaScript is disabled on your browser.





Skip navigation links






- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help







- Prev Class

- Next Class





- Frames

- No Frames





- All Classes









- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method





- Detail: 

- Field | 

- Constr | 

- Method









picocli

## Class CommandLine.Help.TextTable






- java.lang.Object

- 



  - picocli.CommandLine.Help.TextTable









- 

Enclosing class:
CommandLine.Help


---




```
public static class CommandLine.Help.TextTable
extends Object
```


Responsible for spacing out `CommandLine.Help.Ansi.Text` values according to the `CommandLine.Help.Column` definitions the table was
 created with. Columns have a width, indentation, and an overflow policy that decides what to do if a value is
 longer than the column's width.








- 




  - 



### Nested Class Summary


Nested Classes 

Modifier and Type
Class and Description


`static class `
`CommandLine.Help.TextTable.Cell`
Helper class to index positions in a `Help.TextTable`.










  - 



### Field Summary


Fields 

Modifier and Type
Field and Description


`protected List<CommandLine.Help.Ansi.Text>`
`columnValues`
The `char[]` slots of the `TextTable` to copy text values into.



`int`
`indentWrappedLines`
By default, indent wrapped lines by 2 spaces.










  - 



### Constructor Summary


Constructors 

Modifier
Constructor and Description


`protected `
`TextTable(CommandLine.Help.Ansi ansi,
         CommandLine.Help.Column[] columns)`
Deprecated. 
use `picocli.CommandLine.Help.TextTable#TextTable(picocli.CommandLine.Help.ColorScheme, picocli.CommandLine.Help.Column[])`  instead




`protected `
`TextTable(CommandLine.Help.ColorScheme colorScheme,
         CommandLine.Help.Column[] columns)` 









  - 



### Method Summary


All Methods Static Methods Instance Methods Concrete Methods Deprecated Methods 

Modifier and Type
Method and Description


`void`
`addEmptyRow()`
Adds the required `char[]` slots for a new row to the `columnValues` field.



`void`
`addRowValues(CommandLine.Help.Ansi.Text... values)`
Adds a new empty row, then calls `putValue` for each of the specified values, adding more empty rows
 if the return value indicates that the value spanned multiple columns or was wrapped to multiple rows.



`void`
`addRowValues(String... values)`
Delegates to `addRowValues(CommandLine.Help.Ansi.Text...)`, after ensuring
 that multi-line values are layed out in the correct row and column.



`CommandLine.Help.Ansi.Text`
`cellAt(int row,
      int col)`
Deprecated. 
use `textAt(int, int)` instead




`CommandLine.Help.Column[]`
`columns()`
The column definitions of this table.



`static CommandLine.Help.TextTable`
`forColumns(CommandLine.Help.Ansi ansi,
          CommandLine.Help.Column... columns)`
Deprecated. 
use `forColumns(CommandLine.Help.ColorScheme, CommandLine.Help.Column...)` instead




`static CommandLine.Help.TextTable`
`forColumns(CommandLine.Help.ColorScheme colorScheme,
          CommandLine.Help.Column... columns)`
Constructs a `TextTable` with the specified columns.



`static CommandLine.Help.TextTable`
`forColumnWidths(CommandLine.Help.Ansi ansi,
               int... columnWidths)`
Deprecated. 
use `forColumns(CommandLine.Help.ColorScheme, CommandLine.Help.Column...)` instead




`static CommandLine.Help.TextTable`
`forColumnWidths(CommandLine.Help.ColorScheme colorScheme,
               int... columnWidths)`
Constructs a new TextTable with columns with the specified width, all SPANning  multiple columns on
 overflow except the last column which WRAPS to the next row.



`static CommandLine.Help.TextTable`
`forDefaultColumns(CommandLine.Help.Ansi ansi,
                 int usageHelpWidth)`
Deprecated. 
use `forDefaultColumns(CommandLine.Help.Ansi, int, int)` instead




`static CommandLine.Help.TextTable`
`forDefaultColumns(CommandLine.Help.Ansi ansi,
                 int longOptionsColumnWidth,
                 int usageHelpWidth)`
Deprecated. 
use `forDefaultColumns(CommandLine.Help.ColorScheme, int, int)` instead




`static CommandLine.Help.TextTable`
`forDefaultColumns(CommandLine.Help.ColorScheme colorScheme,
                 int longOptionsColumnWidth,
                 int usageHelpWidth)`
Constructs a TextTable with five columns as follows:
 
 required option/parameter marker (width: 2, indent: 0, TRUNCATE on overflow)
 short option name (width: 2, indent: 0, TRUNCATE on overflow)
 comma separator (width: 1, indent: 0, TRUNCATE on overflow)
 long option name(s) (width: 24, indent: 1, SPAN multiple columns on overflow)
 description line(s) (width: 51, indent: 1, WRAP to next row on overflow)
 



`boolean`
`isAdjustLineBreaksForWideCJKCharacters()` 


`CommandLine.Help.TextTable.Cell`
`putValue(int row,
        int col,
        CommandLine.Help.Ansi.Text value)`
Writes the specified value into the cell at the specified row and column and returns the last row and
 column written to.



`int`
`rowCount()`
Returns the current number of rows of this `TextTable`.



`CommandLine.Help.TextTable`
`setAdjustLineBreaksForWideCJKCharacters(boolean adjustLineBreaksForWideCJKCharacters)` 


`CommandLine.Help.Ansi.Text`
`textAt(int row,
      int col)`
Returns the `Text` slot at the specified row and column to write a text value into.



`String`
`toString()` 


`StringBuilder`
`toString(StringBuilder text)`
Copies the text representation that we built up from the options into the specified StringBuilder.






    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`













- 




  - 



### Field Detail







    - 

#### columnValues


```
protected final List<CommandLine.Help.Ansi.Text> columnValues
```

The `char[]` slots of the `TextTable` to copy text values into.









    - 

#### indentWrappedLines


```
public int indentWrappedLines
```

By default, indent wrapped lines by 2 spaces.










  - 



### Constructor Detail







    - 

#### TextTable


```
@Deprecated
protected TextTable(CommandLine.Help.Ansi ansi,
                                 CommandLine.Help.Column[] columns)
```

Deprecated. use `picocli.CommandLine.Help.TextTable#TextTable(picocli.CommandLine.Help.ColorScheme, picocli.CommandLine.Help.Column[])`  instead









    - 

#### TextTable


```
protected TextTable(CommandLine.Help.ColorScheme colorScheme,
                    CommandLine.Help.Column[] columns)
```











  - 



### Method Detail







    - 

#### forDefaultColumns


```
@Deprecated
public static CommandLine.Help.TextTable forDefaultColumns(CommandLine.Help.Ansi ansi,
                                                                        int usageHelpWidth)
```

Deprecated. use `forDefaultColumns(CommandLine.Help.Ansi, int, int)` instead
Constructs a TextTable with five columns as follows:
 

 
      - required option/parameter marker (width: 2, indent: 0, TRUNCATE on overflow)
 
      - short option name (width: 2, indent: 0, TRUNCATE on overflow)
 
      - comma separator (width: 1, indent: 0, TRUNCATE on overflow)
 
      - long option name(s) (width: 24, indent: 1, SPAN multiple columns on overflow)
 
      - description line(s) (width: 51, indent: 1, WRAP to next row on overflow)
 


Parameters:
`ansi` - whether to emit ANSI escape codes or not
`usageHelpWidth` - the total width of the columns combined










    - 

#### forDefaultColumns


```
@Deprecated
public static CommandLine.Help.TextTable forDefaultColumns(CommandLine.Help.Ansi ansi,
                                                                        int longOptionsColumnWidth,
                                                                        int usageHelpWidth)
```

Deprecated. use `forDefaultColumns(CommandLine.Help.ColorScheme, int, int)` instead
Constructs a TextTable with five columns as follows:
 

 
      - required option/parameter marker (width: 2, indent: 0, TRUNCATE on overflow)
 
      - short option name (width: 2, indent: 0, TRUNCATE on overflow)
 
      - comma separator (width: 1, indent: 0, TRUNCATE on overflow)
 
      - long option name(s) (width: 24, indent: 1, SPAN multiple columns on overflow)
 
      - description line(s) (width: 51, indent: 1, WRAP to next row on overflow)
 


Parameters:
`ansi` - whether to emit ANSI escape codes or not
`longOptionsColumnWidth` - the width of the long options column
`usageHelpWidth` - the total width of the columns combined










    - 

#### forDefaultColumns


```
public static CommandLine.Help.TextTable forDefaultColumns(CommandLine.Help.ColorScheme colorScheme,
                                                           int longOptionsColumnWidth,
                                                           int usageHelpWidth)
```

Constructs a TextTable with five columns as follows:
 

 
      - required option/parameter marker (width: 2, indent: 0, TRUNCATE on overflow)
 
      - short option name (width: 2, indent: 0, TRUNCATE on overflow)
 
      - comma separator (width: 1, indent: 0, TRUNCATE on overflow)
 
      - long option name(s) (width: 24, indent: 1, SPAN multiple columns on overflow)
 
      - description line(s) (width: 51, indent: 1, WRAP to next row on overflow)
 


Parameters:
`colorScheme` - the styles and ANSI mode to use for embedded markup
`longOptionsColumnWidth` - the width of the long options column
`usageHelpWidth` - the total width of the columns combined
Since:
4.2










    - 

#### forColumnWidths


```
@Deprecated
public static CommandLine.Help.TextTable forColumnWidths(CommandLine.Help.Ansi ansi,
                                                                      int... columnWidths)
```

Deprecated. use `forColumns(CommandLine.Help.ColorScheme, CommandLine.Help.Column...)` instead
Constructs a new TextTable with columns with the specified width, all SPANning  multiple columns on
 overflow except the last column which WRAPS to the next row.

Parameters:
`ansi` - whether to emit ANSI escape codes or not
`columnWidths` - the width of each table column (all columns have zero indent)










    - 

#### forColumnWidths


```
public static CommandLine.Help.TextTable forColumnWidths(CommandLine.Help.ColorScheme colorScheme,
                                                         int... columnWidths)
```

Constructs a new TextTable with columns with the specified width, all SPANning  multiple columns on
 overflow except the last column which WRAPS to the next row.

Parameters:
`colorScheme` - the styles and ANSI mode to use for embedded markup
`columnWidths` - the width of each table column (all columns have zero indent)
Since:
4.2










    - 

#### forColumns


```
@Deprecated
public static CommandLine.Help.TextTable forColumns(CommandLine.Help.Ansi ansi,
                                                                 CommandLine.Help.Column... columns)
```

Deprecated. use `forColumns(CommandLine.Help.ColorScheme, CommandLine.Help.Column...)` instead
Constructs a `TextTable` with the specified columns.

Parameters:
`ansi` - whether to emit ANSI escape codes or not
`columns` - columns to construct this TextTable with










    - 

#### forColumns


```
public static CommandLine.Help.TextTable forColumns(CommandLine.Help.ColorScheme colorScheme,
                                                    CommandLine.Help.Column... columns)
```

Constructs a `TextTable` with the specified columns.

Parameters:
`colorScheme` - the styles and ANSI mode to use for embedded markup
`columns` - columns to construct this TextTable with
Since:
4.2










    - 

#### isAdjustLineBreaksForWideCJKCharacters


```
public boolean isAdjustLineBreaksForWideCJKCharacters()
```


Since:
4.0
See Also:
`CommandLine.Model.UsageMessageSpec.adjustLineBreaksForWideCJKCharacters()`










    - 

#### setAdjustLineBreaksForWideCJKCharacters


```
public CommandLine.Help.TextTable setAdjustLineBreaksForWideCJKCharacters(boolean adjustLineBreaksForWideCJKCharacters)
```


Since:
4.0
See Also:
`CommandLine.Model.UsageMessageSpec.adjustLineBreaksForWideCJKCharacters(boolean)`










    - 

#### columns


```
public CommandLine.Help.Column[] columns()
```

The column definitions of this table.









    - 

#### textAt


```
public CommandLine.Help.Ansi.Text textAt(int row,
                                         int col)
```

Returns the `Text` slot at the specified row and column to write a text value into.

Parameters:
`row` - the row of the cell whose Text to return
`col` - the column of the cell whose Text to return
Returns:
the Text object at the specified row and column
Since:
2.0










    - 

#### cellAt


```
@Deprecated
public CommandLine.Help.Ansi.Text cellAt(int row,
                                                      int col)
```

Deprecated. use `textAt(int, int)` instead
Returns the `Text` slot at the specified row and column to write a text value into.

Parameters:
`row` - the row of the cell whose Text to return
`col` - the column of the cell whose Text to return
Returns:
the Text object at the specified row and column










    - 

#### rowCount


```
public int rowCount()
```

Returns the current number of rows of this `TextTable`.

Returns:
the current number of rows in this TextTable










    - 

#### addEmptyRow


```
public void addEmptyRow()
```

Adds the required `char[]` slots for a new row to the `columnValues` field.









    - 

#### addRowValues


```
public void addRowValues(String... values)
```

Delegates to `addRowValues(CommandLine.Help.Ansi.Text...)`, after ensuring
 that multi-line values are layed out in the correct row and column.

Parameters:
`values` - the text values to display in each column of the current row










    - 

#### addRowValues


```
public void addRowValues(CommandLine.Help.Ansi.Text... values)
```

Adds a new empty row, then calls `putValue` for each of the specified values, adding more empty rows
 if the return value indicates that the value spanned multiple columns or was wrapped to multiple rows.

Parameters:
`values` - the values to write into a new row in this TextTable
Throws:
`IllegalArgumentException` - if the number of values exceeds the number of Columns in this table










    - 

#### putValue


```
public CommandLine.Help.TextTable.Cell putValue(int row,
                                                int col,
                                                CommandLine.Help.Ansi.Text value)
```

Writes the specified value into the cell at the specified row and column and returns the last row and
 column written to. Depending on the Column's `Overflow` policy, the value may span
 multiple columns or wrap to multiple rows when larger than the column width.

Parameters:
`row` - the target row in the table
`col` - the target column in the table to write to
`value` - the value to write
Returns:
a Cell indicating the position in the table that was last written to (since 2.0)
Throws:
`IllegalArgumentException` - if the specified row exceeds the table's row count
Since:
2.0 (previous versions returned a `java.awt.Point` object)










    - 

#### toString


```
public StringBuilder toString(StringBuilder text)
```

Copies the text representation that we built up from the options into the specified StringBuilder.

Parameters:
`text` - the StringBuilder to write into
Returns:
the specified StringBuilder object (to allow method chaining and a more fluid API)










    - 

#### toString


```
public String toString()
```


Overrides:
`toString` in class `Object`

















Skip navigation links






- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help







- Prev Class

- Next Class





- Frames

- No Frames





- All Classes









- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method





- Detail: 

- Field | 

- Constr | 

- Method