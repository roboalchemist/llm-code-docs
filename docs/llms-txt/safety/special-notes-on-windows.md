# Source: https://docs.safetycli.com/safety-docs/support/support/special-notes-on-windows.md

# Special Notes on Windows

### Setting the PYTHONENCODING Variable

In some Windows environments, Safety CLI will return an error when performing scans on files or directories that include special or accented characters, e.g. é, è, à, ç, et al.&#x20;

This issue occurs because the `PYTHONIOENCODING` variable is empty or not set to `utf-8`.

If you are using the Windows CMD, you can set the variable in the following way:

```
set PYTHONIOENCODING=utf-8
safety scan --output screen > results.txt
```

This set command updates the value per terminal session; if you want to do it permanently, you must add `PYTHONIOENCODING` with the value `utf-8` to your environment variables on Windows.&#x20;
