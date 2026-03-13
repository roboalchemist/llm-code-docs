# sgqlc-codegen Tool

## Generate SGQLC Code

### Downloading schema.json

The schema can be downloaded using `sgqlc.introspection`.

### Generating Schema Types

While one can manually write the schema using `sgqlc.types`, it can
be a daunting task. This can be automated if the `schema.json` is available:

```
sgqlc-codegen schema --docstrings schema.json my_schema.py

```