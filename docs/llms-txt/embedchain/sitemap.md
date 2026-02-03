# Source: https://docs.embedchain.ai/components/data-sources/sitemap.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 🗺️ Sitemap

Add all web pages from an xml-sitemap. Filters non-text files. Use the data\_type as `sitemap`. Eg:

```python  theme={null}
from embedchain import App

app = App()

app.add('https://example.com/sitemap.xml', data_type='sitemap')
```
