# Source: https://firebase.google.com/docs/ai-logic/input-file-requirements.md.txt

<br />

When calling theGemini APIfrom your app using aFirebase AI LogicSDK, you can prompt theGeminimodel to generate text based on a multimodal input, like images, video, and audio, and documents (like PDFs).

You need to use supported file types, specify a supported MIME type, and make sure that your files and multimodal requests meet the requirements and follow best practices.

This page is specific to using a`GenerativeModel`and describes the following:

- [Options for providing files in your request.](https://firebase.google.com/docs/ai-logic/input-file-requirements#options-for-input-files)

- Details about the supported MIME types, best practices, and limitations for the following file inputs:  
  [Images](https://firebase.google.com/docs/ai-logic/input-file-requirements#images)\|[Video](https://firebase.google.com/docs/ai-logic/input-file-requirements#video)\|[Audio](https://firebase.google.com/docs/ai-logic/input-file-requirements#audio)\|[Documents (like PDFs)](https://firebase.google.com/docs/ai-logic/input-file-requirements#documents).

## Options for providing files in multimodal requests

|---------------------------------------------------------------------------------------------------------------------------|
| *Select your Gemini API provider to view provider-specific content on this page* Gemini Developer APIVertex AI Gemini API |

In each multimodal request, you must always provide the following:

- The file's`mimeType`. See each input file's supported MIME types in the applicable section of this page.

- The file. You can either[provide the file as inline data](https://firebase.google.com/docs/ai-logic/input-file-requirements#provide-file-as-inline-data)or[provide the file using its URL](https://firebase.google.com/docs/ai-logic/input-file-requirements#provide-file-using-url).

The size and number of files that you can provide in the request is dictated by the input file type, how you provide the file, and the model used (for details, see each input file type's section on this page).

### **Option 1**: Provide the file as inline data

Note the following about files provided as inline data:

- Only small files can be sent as inline data because the*total request size limit*is 20 MB.

- The file is encoded to base64 in transit (which increases the file size).

For an example showing how to include a file as inline data, see[Generate text from text-and-file (multimodal) input](https://firebase.google.com/docs/ai-logic/generate-text#base64). Note that the SDKs for Android and Apple platforms can handle inline images in requests without the need to specify the MIME type.[Learn more.](https://firebase.google.com/docs/ai-logic/faq-and-troubleshooting#inline-img-sdk-handling)
| **Important:** **The total request size limit is 20 MB.** To send large files, consider using theVertex AIGemini APIbecause it supports including files in multimodal requests usingCloud StorageURLs (which allows for larger file sizes to be sent).

### **Option 2**: Provide the file using a URL

Here are the acceptable types of URLs when using theGemini Developer API:

- **YouTube video URL** : The YouTube video must be[public or unlisted](https://support.google.com/youtube/answer/157177).

  You can specify one YouTube video URL per request.

<br />

*** ** * ** ***

## **Images**: Requirements, best practices, and limitations

### Images: Requirements

In this section, learn about the supported MIME types and limits per request for images.

#### Supported MIME types

Geminimultimodal models support the following image MIME types:

- PNG -`image/png`
- JPEG -`image/jpeg`
- WebP -`image/webp`

<br />

#### Limits per request

<br />

There isn't a specific limit to the number of pixels in an image. However, larger images are scaled down and padded to fit a maximum resolution of 3072 x 3072 while preserving their original aspect ratio.

Maximum files per request: 3,000 image files

<br />

### Images: Tokenization

<br />

Here's how tokens are calculated for images:

- If both dimensions of an image are less than or equal to 384 pixels, then 258 tokens are used.
- If one dimension of an image is greater than 384 pixels, then the image is cropped into tiles. Each tile size defaults to the smallest dimension (width or height) divided by 1.5. If necessary, each tile is adjusted so that it's not smaller than 256 pixels and not greater than 768 pixels. Each tile is then resized to 768x768 and uses 258 tokens.

<br />

### Images: Best practices

<br />

When using images, use the following best practices and information for the best results:

- If you want to detect text in an image, use prompts with a single image to produce better results than prompts with multiple images.
- If your prompt contains a single image, place the image before the text prompt in your request.
- If your prompt contains multiple images, and you want to refer to them later in your prompt or have the model refer to them in the model response, it can help to give each image an index before the image. Use`a``b``c`or`image 1``image 2``image 3`for your index. The following is an example of using indexed images in a prompt:  

  ```
  image 1 
  image 2 
  image 3 

  Write a blogpost about my day using image 1 and image 2. Then, give me ideas
  for tomorrow based on image 3.
  ```
- Use images with higher resolution; they yield better results.
- Include a few examples in the prompt.
- Rotate images to their proper orientation before adding them to the prompt.
- Avoid blurry images.

<br />

### Images: Limitations

<br />

WhileGeminimultimodal models are powerful in many multimodal use cases, it's important to understand the limitations of the models:

- **Content moderation**: The models refuse to provide answers on images that violate our safety policies.
- **Spatial reasoning**: The models aren't precise at locating text or objects in images. They might only return the approximated counts of objects.
- **Medical uses**: The models aren't suitable for interpreting medical images (for example, x-rays and CT scans) or providing medical advice.
- **People recognition**: The models aren't meant to be used to identify people who aren't celebrities in images.
- **Accuracy**: The models might hallucinate or make mistakes when interpreting low-quality, rotated, or extremely low-resolution images. The models might also hallucinate when interpreting handwritten text in images documents.

<br />

<br />

*** ** * ** ***

## **Video**: Requirements, best practices, and limitations

### Video: Requirements

In this section, learn about the supported MIME types and limits per request for video.

#### Supported MIME types

Geminimultimodal models support the following video MIME types:

- FLV -`video/x-flv`
- MOV -`video/quicktime`
- MPEG -`video/mpeg`
- MPEGPS -`video/mpegps`
- MPG -`video/mpg`
- MP4 -`video/mp4`
- WEBM -`video/webm`
- WMV -`video/wmv`
- 3GPP -`video/3gpp`

<br />

#### Limits per request

<br />

Maximum files per request: 10 video files

<br />

### Video: Tokenization

<br />

Here's how tokens are calculated for video:

- The audio track is encoded with video frames. The audio track is also broken down into1-second trunksthat each accounts for 32 tokens. The video frame and audio tokens are interleaved together with their timestamps. The timestamps are represented as 5 tokens.
- For videos that are sampled at or below1 frame per second (fps), the timestamps for the first hour of video are represented as 5 tokens per video frame. The remaining timestamps are represented as 7 tokens per video frame.
- For videos that are sampled above1 frame per second (fps), the timestamps for the first hour of video are represented as 9 tokens per video frame. The remaining timestamps are represented as 11 tokens per video frame.

<br />

### Video: Best practices

<br />

When using video, use the following best practices and information for the best results:

- If your prompt contains a single video, place the video before the text prompt.
- If you require timestamp localization in a video with audio, ask the model to generate timestamps that follow the format as described in "Timestamp format".

<br />

### Video: Limitations

<br />

WhileGeminimultimodal models are powerful in many multimodal use cases, it's important to understand the limitations of the models:

- **Content moderation**: The models refuse to provide answers on videos that violate our safety policies.
- **Non-speech sound recognition**: The models that support audio might make mistakes recognizing sound that's not speech.

<br />

<br />

*** ** * ** ***

## **Audio**: Requirements and limitations

### Audio: Requirements

In this section, learn about the supported MIME types and limits per request for audio.

#### Supported MIME types

Geminimultimodal models support the following audio MIME types:

- AAC -`audio/aac`
- FLAC -`audio/flac`
- MP3 -`audio/mp3`
- MPA -`audio/m4a`
- MPEG -`audio/mpeg`
- MPGA -`audio/mpga`
- MP4 -`audio/mp4`
- OPUS -`audio/opus`
- PCM -`audio/pcm`
- WAV -`audio/wav`
- WEBM -`audio/webm`

<br />

#### Limits per request

<br />

Maximum files per request: 1 audio file

<br />

<br />

### Audio: Limitations

<br />

WhileGeminimultimodal models are powerful in many multimodal use cases, it's important to understand the limitations of the models:

- **Non-speech sound recognition**: The models that support audio might make mistakes recognizing sound that's not speech.
- **Audio-only timestamps** : To accurately generate timestamps for audio-only files, you must configure the`audio_timestamp`parameter in`generation_config`.

<br />

<br />

*** ** * ** ***

## **Documents (like PDFs)**: Requirements, best practices, and limitations

### Documents: Requirements

In this section, learn about the supported MIME types and limits per request for documents (like PDFs).

#### Supported MIME types

Geminimultimodal models support the following document MIME types:

- PDF -`application/pdf`
- Text -`text/plain`

<br />

#### Limits per request

<br />

PDFs are treated as images, so a single page of a PDF is treated as one image. The number of pages allowed in a prompt is limited to the number of images theGeminimultimodal models can support.

- Maximum files per request: 3,000 files
- Maximum pages per file: 1,000 pages per file
- Maximum size per file: 50 MB per file

<br />

### Documents: Tokenization

<br />

**PDF tokenization**

PDFs are treated as images, so each page of a PDF is tokenized in the same way as an image.

Also, the cost for PDFs follows[Geminiimage pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing#gemini-models). For example, if you include a two-page PDF in aGeminiAPI call, you incur an input fee of processing two images.

<br />

### Documents: Best practices

<br />

When using PDFs, use the following best practices and information for the best results:

- If your prompt contains a single PDF, place the PDF before the text prompt in your request.
- If you have a long document, consider splitting it into multiple PDFs to process it.
- Use PDFs created with text rendered as text instead of using text in scanned images. This format ensures text is machine-readable so that it's easier for the model to edit, search, and manipulate compared to scanned image PDFs. This practice provides optimal results when working with text-heavy documents like contracts.

<br />

### Documents: Limitations

<br />

WhileGeminimultimodal models are powerful in many multimodal use cases, it's important to understand the limitations of the models:

- **Spatial reasoning**: The models aren't precise at locating text or objects in PDFs. They might only return the approximated counts of objects.
- **Accuracy**: The models might hallucinate when interpreting handwritten text in PDF documents.

<br />