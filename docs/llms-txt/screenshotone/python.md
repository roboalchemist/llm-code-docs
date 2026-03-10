# Source: https://screenshotone.com/docs/code-examples/python/

# Python SDK and Code Examples

import Alert from "@/components/Alert.astro";

<Alert>
    If you have any questions, please, reach out at `support@screenshotone.com`.
</Alert>

### Installation

Run the next command to install the Python SDK to take screenshots:

```shell
pip install screenshotone
```

### Usage

Don't forget to [sign up](https://dash.screenshotone.com/sign-up) to get access and secret keys.

Generate a screenshot URL without executing the request. Or download the screenshot. It is up to you:

```python
import shutil
from screenshotone import Client, TakeOptions

# create API client
client = Client('<your access key>', '<your secret key>')

# set up options
options = (TakeOptions.url('https://screenshotone.com')
    .format("png")
    .viewport_width(1024)
    .viewport_height(768)
    .block_cookie_banners(True)
    .block_chats(True))

# generate the screenshot URL and share it with a user
url = client.generate_take_url(options)
# expected output: https://api.screenshotone.com/take?url=https%3A%2F%2Fscreenshotone.com&viewport_width=1024&viewport_height=768&block_cookie_banners=True&block_chats=True&access_key=<your access key>&signature=6afc9417a523788580fa01a9f668ea82c78a9d2b41441d2a696010bf2743170f

# or render a screenshot and download the image as stream
image = client.take(options)

# store the screenshot the example.png file
with open('example.png', 'wb') as result_file:
    shutil.copyfileobj(image, result_file)
```

Check out [other SDKs and code examples](/docs/code-examples/).