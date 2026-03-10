# Source: https://transloadit.com/docs/robots/file-preview.md

This Robot's purpose is to generate a meaningful preview image for any file, in such a way that the resulting thumbnail highlights the file's content. The goal is not to losslessly present the original media in a smaller way. Instead, it is to maximize the chance of a person recognizing the media at a glance, while being visually pleasing and consistent with other previews. The generation process depends on the file type. For example, the Robot can extract artwork from media files, frames from videos, generate a waveform for audio files, and preview the content of documents and images. The details of all available strategies are provided in the next section.

If no file-specific thumbnail can be generated because the file type is not supported, a generic icon containing the file extension will be generated.

The default parameters ensure that the Robot always generates a preview image with the predefined dimensions and formats, to allow an easy integration into your application's UI. In addition, the generated preview images are optimized by default to reduce their file size while keeping their quality.
