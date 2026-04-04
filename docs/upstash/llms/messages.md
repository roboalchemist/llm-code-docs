# Source: https://upstash.com/docs/qstash/sdks/ts/examples/messages.md

# Source: https://upstash.com/docs/qstash/sdks/py/examples/messages.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Messages

<Info>
  You can run the async code by importing `AsyncQStash` from `qstash`
  and awaiting the methods.
</Info>

Messages are removed from the database shortly after they're delivered, so you
will not be able to retrieve a message after. This endpoint is intended to be used
for accessing messages that are in the process of being delivered/retried.

#### Retrieve a message

```python  theme={"system"}
from qstash import QStash

client = QStash("<QSTASH-TOKEN>")
msg = client.message.get("<msg-id>")
```

#### Cancel/delete a message

```python  theme={"system"}
from qstash import QStash

client = QStash("<QSTASH-TOKEN>")
client.message.cancel("<msg-id>")
```

#### Cancel messages in bulk

Cancel many messages at once or cancel all messages

```python  theme={"system"}
from qstash import QStash

client = QStash("<QSTASH-TOKEN>")

# cancel more than one message
client.message.cancel_many(["<msg-id-0>", "<msg-id-1>"])

# cancel all messages
client.message.cancel_all()
```
