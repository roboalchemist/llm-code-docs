# Source: https://docs.embedchain.ai/components/data-sources/mdx.md

# 📝 Mdx file

To add any `.mdx` file to your app, use the data\_type (first argument to `.add()` method) as `mdx`. Note that this supports support mdx file present on machine, so this should be a file path. Eg:

```python
from embedchain import App

app = App()
app.add('path/to/file.mdx', data_type='mdx')

app.query("What are the docs about?")
```
