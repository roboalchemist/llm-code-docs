# Source: https://docs.embedchain.ai/components/data-sources/qna.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# ❓💬 Question and answer pair

QnA pair is a local data type. To supply your own QnA pair, use the data\_type as `qna_pair` and enter a tuple. Eg:

```python  theme={null}
from embedchain import App

app = App()

app.add(("Question", "Answer"), data_type="qna_pair")
```
