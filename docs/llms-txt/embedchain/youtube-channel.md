# Source: https://docs.embedchain.ai/components/data-sources/youtube-channel.md

# 📽️ Youtube Channel

## Setup

Make sure you have all the required packages installed before using this data type. You can install them by running the following command in your terminal.

```bash
pip install -U "embedchain[youtube]"
```

## Usage

To add all the videos from a youtube channel to your app, use the data\_type as `youtube_channel`.

```python
from embedchain import App

app = App()
app.add("@channel_name", data_type="youtube_channel")
```
