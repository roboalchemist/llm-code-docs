# SyntaxHighlighter

# SyntaxHighlighter

Inherits:Resource<RefCounted<Object
Inherited By:CodeHighlighter,EditorSyntaxHighlighter
Base class for syntax highlighters. Provides syntax highlighting data to aTextEdit.

## Description

Base class for syntax highlighters. Provides syntax highlighting data to aTextEdit. The associatedTextEditwill call into theSyntaxHighlighteron an as-needed basis.
Note:ASyntaxHighlighterinstance should not be used across multipleTextEditnodes.

## Methods

| void | _clear_highlighting_cache()virtual |
|---|---|
| Dictionary | _get_line_syntax_highlighting(line:int)virtualconst |
| void | _update_cache()virtual |
| void | clear_highlighting_cache() |
| Dictionary | get_line_syntax_highlighting(line:int) |
| TextEdit | get_text_edit()const |
| void | update_cache() |

void
_clear_highlighting_cache()virtual
Dictionary
_get_line_syntax_highlighting(line:int)virtualconst
void
_update_cache()virtual
void
clear_highlighting_cache()
Dictionary
get_line_syntax_highlighting(line:int)
TextEdit
get_text_edit()const
void
update_cache()

## Method Descriptions

void_clear_highlighting_cache()virtual🔗
Virtual method which can be overridden to clear any local caches.
Dictionary_get_line_syntax_highlighting(line:int)virtualconst🔗
Virtual method which can be overridden to return syntax highlighting data.
Seeget_line_syntax_highlighting()for more details.
void_update_cache()virtual🔗
Virtual method which can be overridden to update any local caches.
voidclear_highlighting_cache()🔗
Clears all cached syntax highlighting data.
Then calls overridable method_clear_highlighting_cache().
Dictionaryget_line_syntax_highlighting(line:int)🔗
Returns the syntax highlighting data for the line at indexline. If the line is not cached, calls_get_line_syntax_highlighting()first to calculate the data.
Each entry is a column number containing a nestedDictionary. The column number denotes the start of a region, the region will end if another region is found, or at the end of the line. The nestedDictionarycontains the data for that region. Currently only the key"color"is supported.
Example:Possible return value. This means columns0to4should be red, and columns5to the end of the line should be green:

```
{
    0: {
        "color": Color(1, 0, 0)
    },
    5: {
        "color": Color(0, 1, 0)
    }
}
```

TextEditget_text_edit()const🔗
Returns the associatedTextEditnode.
voidupdate_cache()🔗
Clears then updates theSyntaxHighlightercaches. Override_update_cache()for a callback.
Note:This is called automatically when the associatedTextEditnode, updates its own cache.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
