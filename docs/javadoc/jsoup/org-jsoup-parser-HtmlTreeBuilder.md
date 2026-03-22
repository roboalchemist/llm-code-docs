Package org.jsoup.parser

# Class HtmlTreeBuilder

java.lang.Object
org.jsoup.parser.HtmlTreeBuilder

---

public class HtmlTreeBuilder
extends Object
HTML Tree Builder; creates a DOM from Tokens.

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final int`
`MaxScopeSearchDepth`

Deprecated.
Not used anymore; configure parser depth via `Parser.setMaxDepth(int)`.

`protected Parser`
`parser`
 

- 

## Constructor Summary

Constructors

Constructor
Description
`HtmlTreeBuilder()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`protected void`
`initialiseParse(Reader input,
 String baseUri,
 Parser parser)`
 
`protected boolean`
`process(org.jsoup.parser.Token token)`
 
`String`
`toString()`
 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Field Details

  - 

### MaxScopeSearchDepth

@Deprecated
public static final int MaxScopeSearchDepth
Deprecated.
Not used anymore; configure parser depth via `Parser.setMaxDepth(int)`. Will be removed in jsoup 1.24.1.

See Also:

    - Constant Field Values

  - 

### parser

protected Parser parser

- 

## Constructor Details

  - 

### HtmlTreeBuilder

public HtmlTreeBuilder()

- 

## Method Details

  - 

### initialiseParse

protected void initialiseParse(Reader input,
 String baseUri,
 Parser parser)

  - 

### process

protected boolean process(org.jsoup.parser.Token token)

  - 

### toString

public String toString()

Overrides:
`toString` in class `Object`