# Source: https://docs.embedchain.ai/components/data-sources/youtube-video.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 📺 Youtube Video

## Setup

Make sure you have all the required packages installed before using this data type. You can install them by running the following command in your terminal.

```bash  theme={null}
pip install -U "embedchain[youtube]"
```

## Usage

To add any youtube video to your app, use the data\_type as `youtube_video`. Eg:

```python  theme={null}
from embedchain import App

app = App()
app.add('a_valid_youtube_url_here', data_type='youtube_video')
```
