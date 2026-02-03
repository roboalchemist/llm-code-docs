# Source: https://docs.embedchain.ai/components/data-sources/mdx.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 📝 Mdx file

To add any `.mdx` file to your app, use the data\_type (first argument to `.add()` method) as `mdx`. Note that this supports support mdx file present on machine, so this should be a file path. Eg:

```python  theme={null}
from embedchain import App

app = App()
app.add('path/to/file.mdx', data_type='mdx')

app.query("What are the docs about?")
```
