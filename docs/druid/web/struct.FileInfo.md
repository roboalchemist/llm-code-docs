druid

# Struct FileInfo

Source

```
pub struct FileInfo {
    pub path: PathBuf,
    pub format: Option<FileSpec>,
}
```

## Fields§

§`path: PathBuf`

The path to the selected file.

On macOS, this is already rewritten to use the extension that the user selected
with the `file format` property.
§`format: Option<FileSpec>`

The selected file format.

If there’re multiple different formats available
this allows understanding the kind of format that the user expects the file
to be written in. Examples could be Blender 2.4 vs Blender 2.6 vs Blender 2.8.
The `path` above will already contain the appropriate extension chosen in the
`format` property, so it is not necessary to mutate `path` any further.

## Implementations§
