# Source: https://docs.aimlapi.com/api-references/music-models/stability-ai/stable-audio.md

# stable-audio

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `stable-audio`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/stable-audio" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

An advanced audio generation model designed to create high-quality audio tracks from textual prompts.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schemas

{% openapi src="<https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-a46ae5c03898acdb169785f19d65431af80b51a0%2Fstable-audio.json?alt=media>" path="/v2/generate/audio" method="post" %}
[stable-audio.json](https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-a46ae5c03898acdb169785f19d65431af80b51a0%2Fstable-audio.json?alt=media)
{% endopenapi %}

### Retrieve the generated music sample from the server <a href="#retrieve-the-generated-video-from-the-server" id="retrieve-the-generated-video-from-the-server"></a>

After sending a request for music generation, this task is added to the queue. Based on the service's load, the generation can be completed in 50-60 seconds or take a bit more.

{% openapi src="<https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-a98ba4f8d6b3d978115c82a4cdf47c38d17e7902%2FLyria-2-pair.json?alt=media>" path="/v2/generate/audio" method="get" %}
[Lyria-2-pair.json](https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-a98ba4f8d6b3d978115c82a4cdf47c38d17e7902%2FLyria-2-pair.json?alt=media)
{% endopenapi %}
