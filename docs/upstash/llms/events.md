# Source: https://upstash.com/docs/workflow/howto/events.md

# Source: https://upstash.com/docs/qstash/sdks/py/examples/events.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Events

<Info>
  You can run the async code by importing `AsyncQStash` from `qstash`
  and awaiting the methods.
</Info>

#### Get all events with pagination using cursor

Since there can be a large number of events, they are paginated.
You can go through the results using the `cursor`.

```python  theme={"system"}
from qstash import QStash

client = QStash("<QSTASH-TOKEN>")

all_events = []
cursor = None
while True:
    res = client.event.list(cursor=cursor)
    all_events.extend(res.events)
    cursor = res.cursor
    if cursor is None:
        break
```
