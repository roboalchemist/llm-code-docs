# Source: https://documentation.mailgun.com/docs/mailgun/sdk/python_sdk.md

# Python

a
img

    Official Mailgun Python SDK

## Installation

### pip install

Use the below code to install the Mailgun SDK for Python:


```bash
pip install mailgun-python
```

#### git clone & pip install locally

Use the below code to install it locally by cloning this repository:


```bash
git clone https://github.com/mailgun/mailgun-python
cd mailgun-python
```


```bash
pip install .
```

#### conda & make

Use the below code to install it locally by `conda` and `make` on Unix platforms:


```bash
make install
```

### For development

#### Using conda

on Linux or macOS:


```bash
git clone https://github.com/mailgun/mailgun-python
cd mailgun-python
```

- A basic environment with a minimum number of dependencies:



```bash
make dev
conda activate mailgun
```

- A full dev environment:



```bash
make dev-full
conda activate mailgun-dev
```

### Usage

Here's a simple example of how to send an email.
As always, please consult the repository readme for full details.

#### Send an email

Pass the components of the messages such as To, From, Subject, HTML and text parts, attachments, etc. Mailgun will build a MIME representation of the message and send it. Note: In order to send you must provide one of the following parameters: 'text', 'html', 'amp-html' or 'template'


```python
import os
from pathlib import Path
from mailgun.client import Client

key: str = os.environ["APIKEY"]
domain: str = os.environ["DOMAIN"]
client: Client = Client(auth=("api", key))


def post_message() -> None:
    # Messages
    # POST /<domain>/messages
    data = {
        "from": os.getenv("MESSAGES_FROM", "test@test.com"),
        "to": os.getenv("MESSAGES_TO", "recipient@example.com"),
        "subject": "Hello from python!",
        "text": "Hello world!",
        "o:tag": "Python test",
    }

    req = client.messages.create(data=data, domain=domain)
    print(req.json())
```