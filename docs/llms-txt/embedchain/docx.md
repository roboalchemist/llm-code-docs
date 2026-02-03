# Source: https://docs.embedchain.ai/components/data-sources/docx.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 📄 Docx file

### Docx file

To add any doc/docx file, use the data\_type as `docx`. `docx` allows remote urls and conventional file paths. Eg:

```python  theme={null}
from embedchain import App

app = App()
app.add('https://example.com/content/intro.docx', data_type="docx")
# Or add file using the local file path on your system
# app.add('content/intro.docx', data_type="docx")

app.query("Summarize the docx data?")
```
