# Source: https://docs.embedchain.ai/components/data-sources/youtube-channel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 📽️ Youtube Channel

## Setup

Make sure you have all the required packages installed before using this data type. You can install them by running the following command in your terminal.

```bash  theme={null}
pip install -U "embedchain[youtube]"
```

## Usage

To add all the videos from a youtube channel to your app, use the data\_type as `youtube_channel`.

```python  theme={null}
from embedchain import App

app = App()
app.add("@channel_name", data_type="youtube_channel")
```
