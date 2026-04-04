# Source: https://docs.embedchain.ai/api-reference/app/reset.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 🔄 reset

`reset()` method allows you to wipe the data from your RAG application and start from scratch.

## Usage

```python  theme={null}
from embedchain import App

app = App()
app.add("https://www.forbes.com/profile/elon-musk")

# Reset the app
app.reset()
```
