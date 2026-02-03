# Source: https://resend.com/docs/send-with-fastapi.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send emails with FastAPI

> Learn how to send your first email using FastAPI and the Resend Python SDK.

## Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

## 1. Install

Get the Resend Python SDK.

<CodeGroup>
  ```bash Pip theme={"theme":{"light":"github-light","dark":"vesper"}}
  pip install resend
  ```
</CodeGroup>

## 2. Send email using HTML

The easiest way to send an email is by using the `html` parameter.

```py main.py theme={"theme":{"light":"github-light","dark":"vesper"}}
import os
from typing import Dict
from fastapi import FastAPI
import resend

resend.api_key = os.environ["RESEND_API_KEY"]

app = FastAPI()

@app.post("/")
def send_mail() -> Dict:
    params: resend.Emails.SendParams = {
        "from": "Acme <onboarding@resend.dev>",
        "to": ["delivered@resend.dev"],
        "subject": "hello world",
        "html": "<strong>it works!</strong>",
    }
    email: resend.Emails.SendResponse = resend.Emails.send(params)
    return email
```

## 3. Try it yourself

<Card title="FastAPI Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-fastapi-example">
  See the full source code.
</Card>
