# Source: https://docs.embedchain.ai/components/data-sources/xml.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 🧾 XML file

### XML file

To add any xml file, use the data\_type as `xml`. Eg:

```python  theme={null}
from embedchain import App

app = App()

app.add('content/data.xml')
```

Note: Only the text content of the xml file will be added to the app. The tags will be ignored.
