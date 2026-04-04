# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/user-defined-java-class/general-user-defined-java-class/class-and-code-fragments.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/user-defined-java-class/general-user-defined-java-class/class-and-code-fragments.md

# Class and code fragments

![Class and code fragments panel](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-8a2313297fe99308bb38417840987d5a22d82121%2FPDITransStep_UserDefinedJavaClass_ClassesAndCodeFragments.png?alt=media)

You can navigate through your defined classes along with related code snippets and fields through the **Classes and Code Fragments** panel. You can right-click on any item in this tree to either **Delete**, **Rename**, or **Show Sample**.

## Classes

The **Classes** folder indicates what classes have corresponding code block tabs in the **Class Code** panel.

## Code Snippits

The **Code Snippits** folder shows the internal PDI code related to the User Defined Java Class step. These snippits are shown as reference for the code of your class.

## Input Fields

The **Input fields** folder contains any input fields you define in your code. While working with your defined code, you will be handling input and output fields. Many ways exist for handling input fields. For example, to start, examine the following description of an input row:

```java
RowMetaInterface inputRowMeta = getInputRowMeta();
```

The **inputRowMeta** object contains the metadata of the input row. It includes all the fields, their data types, lengths, names, format masks, and more. You can use this object to look up input fields. For example, if you want to look for a field called customer, you would use the following code:

```java
ValueMetaInterface customer = inputRowMeta.searchValueMeta("year");
```

Because looking up field names can be slow if you need to do it for every row that passes through a transformation, you could look up field names in advance in a first block of code, as shown in the following example:

```java
if (first) {
 yearIndex = getInputRowMeta().indexOfValue(getParameter("YEAR"));
 if (yearIndex<0) {
   throw new KettleException("Year field not found in the input row, check parameter 'YEAR'\!");
 }
}
```

To get the Integer value contained in the year field, you can then use the following construct:

```java
Object[] r = getRow();
...
Long year = inputRowMeta().getInteger(r, yearIndex);
```

To make this process easier, you can use a shortcut in the following form:

```java
Long year = get(Fields.In, "year").getInteger(r);
```

This method also takes into account the index-based optimization mentioned above.

**Note:** The Java data types that you get from previous steps always corresponds to the PDI data type as described on the [PDI Rows Of Data](https://wiki.pentaho.com/display/EAI/PDI+Rows+Of+Data) page.

## Info Fields

The **Info fields** folder contains any information fields you define in your code. These fields will not appear in the **Classes and Code Fragments** panel until they are defined in your code. If no information fields are defined in your code, nothing will show in this folder.

## Output Fields

You can define all the new fields you want to use as the output of the step in the **Fields** tab. Setting fields in this tab will automatically calculate the layout of the output row metadata and store it in `data.outputRowMeta`, which enables you to create the output row.

In cases where the step writes as many (or as few) rows as it reads, you can resize the row you get on input, as shown in the following example code:

```java
Object[] outputRowData = RowDataUtil.resizeArray(r, data.outputRowMeta.size());
```

or in the following example code:

```java
Object[] outputRowData = createOutputRow(r, data.outputRowMeta.size());
```

If you are copying the rows, create separate copies to prevent subsequent steps from modifying the same Object\[] copy many times at once, as shown in the following example:

```java
Object[] outputRowData = RowDataUtil.createResizedCopy(r, data.outputRowMeta.size());
```

As with accessing input fields, output fields can be addressed through the index in the output row, as shown in the following example:

```java
outputRowData[getInputRowMeta().size()] = easterDate(year.intValue());
```

or using the shortcut that is shown in the following example:

```java
get(Fields.Out, "easter").setValue(r, easterDate(year.intValue());
```

The Java data types that you pass to subsequent steps always need to correspond to the PDI data type as described on the [PDI Rows Of Data](https://wiki.pentaho.com/display/EAI/PDI+Rows+Of+Data) page.
