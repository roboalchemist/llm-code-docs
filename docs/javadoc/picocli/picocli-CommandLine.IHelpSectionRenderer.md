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

## Interface CommandLine.IHelpSectionRenderer







- 

Enclosing class:
CommandLine


---




```
public static interface CommandLine.IHelpSectionRenderer
```

Renders a section of the usage help message. The usage help message can be customized:
 use the `CommandLine.setHelpSectionKeys(List)` and `CommandLine.setHelpSectionMap(Map)` to change the order of sections,
 delete standard sections, add custom sections or replace the renderer of a standard sections with a custom one.
 


 This gives complete freedom on how a usage help message section is rendered, but it also means that the section renderer
 is responsible for all aspects of rendering the section, including layout and emitting ANSI escape codes.
 The `CommandLine.Help.TextTable` and `CommandLine.Help.Ansi.Text` classes, and the `CommandLine.Help.Ansi.string(String)` and `CommandLine.Help.Ansi.text(String)` methods may be useful.
 

Since:
3.9
See Also:
`CommandLine.Model.UsageMessageSpec`









- 




  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description


`String`
`render(CommandLine.Help help)`
Renders a section of the usage help, like header heading, header, synopsis heading,
 synopsis, description heading, description, etc.














- 




  - 



### Method Detail







    - 

#### render


```
String render(CommandLine.Help help)
```

Renders a section of the usage help, like header heading, header, synopsis heading,
 synopsis, description heading, description, etc.

Parameters:
`help` - the `Help` instance for which to render a section
Returns:
the text for this section; may contain ANSI escape codes
Since:
3.9

















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