# Source: https://upstash.com/docs/redis/sdks/ts/commands/generic/keys.md

# Source: https://upstash.com/docs/redis/sdks/py/commands/generic/keys.md

# Source: https://upstash.com/docs/qstash/sdks/py/examples/keys.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Keys

<Info>
  You can run the async code by importing `AsyncQStash` from `qstash`
  and awaiting the methods.
</Info>

#### Retrieve your signing Keys

```python  theme={"system"}
from qstash import QStash

client = QStash("<QSTASH-TOKEN>")
signing_key = client.signing_key.get()

print(signing_key.current, signing_key.next)
```

#### Rotate your signing Keys

```python  theme={"system"}
from qstash import QStash

client = QStash("<QSTASH-TOKEN>")
new_signing_key = client.signing_key.rotate()

print(new_signing_key.current, new_signing_key.next)
```
