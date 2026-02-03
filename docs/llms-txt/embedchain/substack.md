# Source: https://docs.embedchain.ai/components/data-sources/substack.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 📝 Substack

To add any Substack data sources to your app, just add the main base url as the source and set the data\_type to `substack`.

```python  theme={null}
from embedchain import App

app = App()

# source: for any substack just add the root URL
app.add('https://www.lennysnewsletter.com', data_type='substack')
app.query("Who is Brian Chesky?")
# Answer: Brian Chesky is the co-founder and CEO of Airbnb.
```
