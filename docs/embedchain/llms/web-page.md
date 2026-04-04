# Source: https://docs.embedchain.ai/components/data-sources/web-page.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 🌐 HTML Web page

To add any web page, use the data\_type as `web_page`. Eg:

```python  theme={null}
from embedchain import App

app = App()

app.add('a_valid_web_page_url', data_type='web_page')
```
