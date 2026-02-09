# Source: https://docs.embedchain.ai/components/data-sources/beehiiv.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 🐝 Beehiiv

To add any Beehiiv data sources to your app, just add the base url as the source and set the data\_type to `beehiiv`.

```python  theme={null}
from embedchain import App

app = App()

# source: just add the base url and set the data_type to 'beehiiv'
app.add('https://aibreakfast.beehiiv.com', data_type='beehiiv')
app.query("How much is OpenAI paying developers?")
# Answer: OpenAI is aggressively recruiting Google's top AI researchers with offers ranging between $5 to $10 million annually, primarily in stock options.
```
