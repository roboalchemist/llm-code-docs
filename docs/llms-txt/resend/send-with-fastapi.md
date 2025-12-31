# Source: https://resend.com/docs/send-with-fastapi.md

# Send emails with FastAPI

> Learn how to send your first email using FastAPI and the Resend Python SDK.

## Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

## 1. Install

Get the Resend Python SDK.

<CodeGroup>
  ```bash Pip theme={null}
  pip install resend
  ```
</CodeGroup>

## 2. Send email using HTML

The easiest way to send an email is by using the `html` parameter.

```py main.py theme={null}
import resend
from typing import Dict
from fastapi import FastAPI

resend.api_key = "re_xxxxxxxxx"

app = FastAPI()

@app.post("/")
def send_mail() -> Dict:
    params: resend.Emails.SendParams = {
        "from": "onboarding@resend.dev",
        "to": ["delivered@resend.dev"],
        "subject": "Hello World",
        "html": "<strong>it works!</strong>",
    }
    email: resend.Email = resend.Emails.send(params)
    return email
```

## 3. Try it yourself

<Card title="FastAPI Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-fastapi-example">
  See the full source code.
</Card>
