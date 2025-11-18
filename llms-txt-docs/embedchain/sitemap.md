# Source: https://docs.embedchain.ai/components/data-sources/sitemap.md

# 🗺️ Sitemap

Add all web pages from an xml-sitemap. Filters non-text files. Use the data\_type as `sitemap`. Eg:

```python
from embedchain import App

app = App()

app.add('https://example.com/sitemap.xml', data_type='sitemap')
```
