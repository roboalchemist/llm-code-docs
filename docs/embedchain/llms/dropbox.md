# Source: https://docs.embedchain.ai/components/data-sources/dropbox.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 💾 Dropbox

To load folders or files from your Dropbox account, configure the `data_type` parameter as `dropbox` and specify the path to the desired file or folder, starting from the root directory of your Dropbox account.

For Dropbox access, an **access token** is required. Obtain this token by visiting [Dropbox Developer Apps](https://www.dropbox.com/developers/apps). There, create a new app and generate an access token for it.

Ensure your app has the following settings activated:

* In the Permissions section, enable `files.content.read` and `files.metadata.read`.

## Usage

Install the `dropbox` pypi package:

```bash  theme={null}
pip install dropbox
```

Following is an example of how to use the dropbox loader:

```python  theme={null}
import os
from embedchain import App

os.environ["DROPBOX_ACCESS_TOKEN"] = "sl.xxx"
os.environ["OPENAI_API_KEY"] = "sk-xxx"

app = App()

# any path from the root of your dropbox account, you can leave it "" for the root folder
app.add("/test", data_type="dropbox")

print(app.query("Which two celebrities are mentioned here?"))
# The two celebrities mentioned in the given context are Elon Musk and Jeff Bezos.
```
