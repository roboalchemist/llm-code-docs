# Source: https://upstash.com/docs/qstash/sdks/ts/examples/receiver.md

# Source: https://upstash.com/docs/qstash/sdks/py/examples/receiver.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Receiver

When receiving a message from QStash, you should [verify the signature](/qstash/howto/signature).
The QStash Python SDK provides a helper function for this.

```python  theme={"system"}
from qstash import Receiver

receiver = Receiver(
    current_signing_key="YOUR_CURRENT_SIGNING_KEY",
    next_signing_key="YOUR_NEXT_SIGNING_KEY",
)

# ... in your request handler

signature, body = req.headers["Upstash-Signature"], req.body

receiver.verify(
    body=body,
    signature=signature,
    url="YOUR-SITE-URL",
)
```
