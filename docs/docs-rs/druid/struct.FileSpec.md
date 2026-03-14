druid

# Struct FileSpec

Source

```
pub struct FileSpec {
    pub name: &'static str,
    pub extensions: &'static [&'static str],
}
```

## Fields§

§`name: &'static str`

A human readable name, describing this filetype.

This is used in the Windows file dialog, where the user can select
from a dropdown the type of file they would like to choose.

This should not include the file extensions; they will be added automatically.
For instance, if we are describing Word documents, the name would be “Word Document”,
and the displayed string would be “Word Document (*.doc)”.
§`extensions: &'static [&'static str]`

The file extensions used by this file type.

This should not include the leading ‘.’.

## Implementations§
