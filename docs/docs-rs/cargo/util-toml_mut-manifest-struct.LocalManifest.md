cargo::util::toml_mut::manifest

# Struct LocalManifest

Source

```
pub struct LocalManifest {
    pub path: PathBuf,
    pub manifest: Manifest,
    pub raw: String,
    pub embedded: Option<Embedded>,
}
```

## Fields§

§`path: PathBuf`

Path to the manifest.
§`manifest: Manifest`

Manifest contents.
§`raw: String`

The raw, unparsed package file
§`embedded: Option<Embedded>`

Edit location for an embedded manifest, if relevant

## Implementations§
