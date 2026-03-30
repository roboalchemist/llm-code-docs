# Source: https://docs.salad.com/transcription/tutorials/transcription-quick-start.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Transcription API Quickstart

> Get started with Salad Transcription API here. This step by step guide will walk you through setting up your SaladCloud account and running your first Transcription API job.

*Last Updated: November 26, 2024*

## Accounts & Credentials

### Create SaladCloud Account

*To start,* visit [https://portal.salad.com/](https://portal.salad.com/) to log in or create a free account. **New users
receive 5 free audio hours to transcribe at no cost!**

[Watch our quick tutorial](https://www.loom.com/share/6d68372eb4de4600927bc20ad31253f3) on how to use your free credits
effectively.

<img src="https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/create_account.png?fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=506425ff456a3d8c41ffb9ef261b216f" alt="Create SaladCloud Account" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="transcription/images/create_account.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/create_account.png?w=280&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=5d4581e341469efc91bdf1ea1f62d6ba 280w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/create_account.png?w=560&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=1728c8133189bd91eda2eb86227d1167 560w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/create_account.png?w=840&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=cb608f368567bc90a4812607ca33f106 840w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/create_account.png?w=1100&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=8ea180c3da84163edc4b67fe5f323a49 1100w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/create_account.png?w=1650&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=cbd85ea9b6335860ce2ad98719f7ef38 1650w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/create_account.png?w=2500&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=8057860f8dace87872b78a50b948ba9b 2500w" />

### Create SaladCloud Organization

*Next,* create a new organization or select an existing one you'd like to use for transcription. Click on *Switch to
this Organization* for the org you want to use.

<img src="https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/projects.png?fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=895ec38e0297bc3342c7b7fd2ef477d1" alt="Create SaladCloud Organization" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="transcription/images/projects.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/projects.png?w=280&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=dff8040781b48c08dcbeedd3f3f59560 280w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/projects.png?w=560&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=92965f9a0f0787de710683e45bb778e4 560w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/projects.png?w=840&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=910baeff31d3e06707b474b326e77696 840w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/projects.png?w=1100&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=ec5bfe4e03dcafd7037bcdf50acb3d7d 1100w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/projects.png?w=1650&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=2aad6ac85b0d0a669b4bdbaf2220a73c 1650w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/projects.png?w=2500&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=80dd232dddd1c47eba16691a588f3c6b 2500w" />

### Get Transcription API URL

*Then,* click on *Inference Endpoints* in the left-hand nav and open up the Transcription API or Transcription Lite.

<img src="https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/managed_services.png?fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=329e9a6e8a52d8a847645b1d5a9335a8" alt="Access Salad Transcription API" data-og-width="1100" width="1100" data-og-height="618" height="618" data-path="transcription/images/managed_services.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/managed_services.png?w=280&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=93f33349131845dfbb682b73b0414f14 280w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/managed_services.png?w=560&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=6a15030f40cccc3bcab2ec1bdfb98fe5 560w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/managed_services.png?w=840&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=e67c8b9de94b8975754b5834b4767d57 840w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/managed_services.png?w=1100&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=9f8a8c2f5bcefdbd6a3d45427aea4903 1100w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/managed_services.png?w=1650&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=ffa77a60cfc051ec2fd87af09f94b21c 1650w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/managed_services.png?w=2500&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=c49fcc9e8b1ba1d5435f14ecd595ec27 2500w" />

Copy your Transcription API URL

<img src="https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/cc_page.png?fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=6ee48080fbe89b8108b9efadbfdd8201" alt="Copy Transcription API URL" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="transcription/images/cc_page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/cc_page.png?w=280&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=804db46e2000a324e5ccd0463aa6c058 280w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/cc_page.png?w=560&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=cfafdde47b6f689621441c691d31f26f 560w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/cc_page.png?w=840&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=f25dd5d897a55367ea36ad1eddf95c7e 840w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/cc_page.png?w=1100&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=e4a9f7508f28e147eeb054d3b288c229 1100w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/cc_page.png?w=1650&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=e2a53735d1a552fad0f0bee7ffc91628 1650w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/cc_page.png?w=2500&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=5e6245b39d2b532ee3d2dc6016aed942 2500w" />

### Authentication

Copy your SaladCloud API key from your account [here.](https://portal.salad.com/api-key)

<img src="https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/9d9c06f-image.png?fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=05dee5994bfd7a3f654f39ff86079927" alt="Token Instructions" data-og-width="1339" width="1339" data-og-height="394" height="394" data-path="transcription/images/9d9c06f-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/9d9c06f-image.png?w=280&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=39347787f7644d9982065a06beb39587 280w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/9d9c06f-image.png?w=560&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=36ffd538e1d9127beed7e4488005e9cd 560w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/9d9c06f-image.png?w=840&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=95a566fe25a6a0db3160c05cab1de24a 840w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/9d9c06f-image.png?w=1100&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=8242bfbd7e23bb90acf346d303eb2e63 1100w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/9d9c06f-image.png?w=1650&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=0c91c1f51a8be56193012396678e23b3 1650w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/9d9c06f-image.png?w=2500&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=9061c98669d3334efc13d35d0e87c612 2500w" />

## How to Use Transcription APIs

We provide several examples and resources to help you use the API effectively:

* For a **cURL example** and parameter descriptions, refer to
  [Example cURL Post](#example-curl-post-with-salad-transcription-api) on this page.
* For **easy testing** with our API reference, visit the [API Reference](#api-reference).
* For **process automation**, see [Transcription Automation](#transcription-automation).
* For **native Python integration**, check out our
  [official Python SDK](/transcription/how-to-guides/sdk/python-sdk-quick-start). The SDK simplifies file uploads to S4,
  authentication, job polling, and webhook handling, letting you transcribe and manage jobs with just a few lines of
  code.

### Example cURL Post with Salad Transcription API

```bash  theme={null}
curl -X POST https://api.salad.com/api/public/organizations/{my-organization}/inference-endpoints/transcribe/jobs \
   -H "Salad-Api-Key: {your-api-key}" \
   -H "Content-Type: application/json" \
   -d '{
      "input": {
         "url": "https://example.com/path/to/file.mp3",
         "language_code": "en",
         "return_as_file": false,
         "sentence_level_timestamps": "true"
         "word_level_timestamps": false,
         "diarization": false,
         "sentence_diarization": true,
         "multichannel": false,
         "srt": false,
         "translate": "",
         "summarize": 50,
         "llm_translation": "french, german, portuguese",
         "srt_translation": "spanish, Hindi",
         "custom_prompt": "",
         "custom_vocabulary": ""
      },
    "webhook": {your webhook url},
	  "metadata": {
      "my-job-id": 1234
      }
   }'
```

### Example cURL Post with Transcription Lite

```bash  theme={null}
curl -X POST https://api.salad.com/api/public/organizations/{my-organization}/inference-endpoints/transcription-lite/jobs \
   -H "Salad-Api-Key: {your-api-key}" \
   -H "Content-Type: application/json" \
   -d '{
      "input": {
         "url": "https://example.com/path/to/file.mp3",
         "language_code": "en",
         "return_as_file": false,
         "sentence_level_timestamps": "true"
         "word_level_timestamps": false,
         "diarization": false,
         "sentence_diarization": true,
         "srt": false,
         "translate": "to_eng"
      },
    "webhook": {your webhook url},
	  "metadata": {
      "my-job-id": 1234
      }
   }'
```

* Fill in the file link instead of "[https://example.com/path/to/file.mp3](https://example.com/path/to/file.mp3)"

* Optional : replace `{your webhook url}` with webhook url if needed. If not, remove the line.

Webhook is a method that enables application to transmit data to another application immediately upon the occurrence of
an event. Instead of having your application periodically poll for updates, a webhook delivers data to a specified URL
as soon as the event occurs, facilitating instant communication and minimizing latency. In our case transcription result
gets sent to the webhook.

### Example cURL Get Transcript from Salad Transcription API

```bash  theme={null}
curl https://api.salad.com/api/public/organizations/{my-organization}/inference-endpoints/transcribe/jobs/54e84442-3576-45ca-904c-a1d90bc77baf \
   -H "Salad-Api-Key: {your-api-key}"
```

### Example cURL Get Transcript from Transcription Lite

```bash  theme={null}
curl https://api.salad.com/api/public/organizations/{my-organization}/inference-endpoints/transcription-lite/jobs/54e84442-3576-45ca-904c-a1d90bc77baf \
   -H "Salad-Api-Key: {your-api-key}"
```

### Step 1 | Configure Header

Configure you header to include your unique SaladCloud API URL which can be found above as the variable “API URL”. Also
include your unique SaladCloud API key [which can be found here](https://portal.salad.com/api-key) as the variable
“Salad-Api-Key”.

### Step 2 | Set Input Parameters

To find more information about each parameter, please, visit **"Features"** option in the menu on the left.

Update the JSON input parameters to customize your transcription output.

#### url

The url parameter should be a downloadable link to your audio or video file. We recommend using a file service like AWS
S3, Azure Blob Storage, Dropbox, or Google Drive that offers secure, downloadable links. For instructions on how to
generate downloadable links for these services, please refer to
[How to Create Downloadable File Links](/transcription/how-to-guides/cloud-storage/aws-downloadable-file)

Send media in any of these formats.

*Audio:* AIFF, FLAC, M4A, MP3, WAV
*Video:* MKV, MOV, WEBM, WMA, MP4 (most codecs), AVI

#### return\_as\_file

Set to true to receive the transcription output as a downloadable file URL. This is useful for large outputs. Default is
false.

#### language\_code

Transcription is available in 97 languages. We automatically identify the source language. You only need to specify the
"language\_code" if diarization is required. Please note that accuracy varies across languages — some may perform better
than others. For detailed accuracy information, refer to our
[language benchmark results](/transcription/reference/accuracy-benchmarks).

#### sentence\_level\_timestamps

Sentence level timestamps are returned on default. Set to false if not needed.

#### word\_level\_timestamps

Set to "true" for word level timestamps. Set to "false” on default.

#### diarization

Set to *"true"* for speaker separation and identification. If you don't require it, set it to *"false”*.

Diarization requires the `language_code` to be defined. By default, it is set to `"en"` (English).

You can also diarize in *"fr"* (French), *"de"* (German), *"es"* (Spanish), *"it"* (Italian), *"ja"* (Japanese), *"zh"*
(Chinese), *"nl"* (Dutch), *"uk"* (Ukrainian), *"pt"* (Portuguese), *"ar"* (Arabic), *"cs”* (Czech), *"ru"* (Russian),
*"pl"* (Polish), *"hu"* (Hungarian), *"fi"* (Finnish), *"fa"* (Persian), *"el"* (Greek), *"tr"* (Turkish), *"da"*
(Danish), *"he"* (Hebrew), *"vi"* (Vietnamese), *"ko"* (Korean), *"ur"* (Urdu), *"te"* (Telugu), *"hi"* (Hindi), *"ca"*
(Catalan), *"ml"* (Malayalam).

#### sentence\_diarization

Set to `true` to include speaker information at the sentence level. Requires language\_code to be specified. Default is
`false`.

#### multichannel

Set to `true` to enable multichannel transcription. Each channel will be transcribed separately and labeled with
`channel` and `speaker`. Falls back to regular speaker diarization if only one channel is present. Requires
`diarization` for word-level speaker and channel labeling, or `sentence_diarization` for sentence-level speaker and
channel labeling.

#### translate

Set `"translate": "to_eng"` to translate the transcription into English. This replaces the original transcription with
the English translation. All additional parameters may also be used alongside translation.

#### llm\_translation

*(Salad Transcription API only)*

Provide a comma-separated list of target languages to translate the transcription into multiple languages using our LLM
integration. The original transcription will be returned as normal, along with the translations. **Supported
languages:** English, French, German, Italian, Portuguese, Hindi, Spanish, Thai

#### srt

Set to *"true"* to generate a .srt output for caption and subtitles. If you don't require it, set it to *"false"*.

#### srt\_translation

*(Salad Transcription API only)*

Provide a comma-separated list of target languages to translate the generated SRT captions into multiple languages. The
original transcription and SRT content will be returned as normal. **Supported languages:** English, French, German,
Italian, Portuguese, Hindi, Spanish, Thai

#### summarize

*(Salad Transcription API only)*

Set to an integer value representing the maximum number of words for the summary of the transcription.

#### custom\_vocabulary (preview)

*(Salad Transcription API only)*

Provide a comma-separated list of custom words or phrases to improve transcription accuracy for domain-specific terms.

#### custom\_prompt (preview)

*(Salad Transcription API only)*

Provide a custom instruction to perform specific analyses on the transcription using our LLM integration.

#### classification\_labels

#### overall\_classification

*(Salad Transcription API only)*

Use the classification\_labels parameter in conjunction with overall\_classification to classify the entire transcription
into specified categories using an LLM.

#### overall\_sentiment\_analysis

*(Salad Transcription API only)*

Set "overall\_sentiment\_analysis": true to perform sentiment analysis.

### webhook

\*Optional. Webhook is a method that enables application to transmit data to another application immediately when
process is finished. Specify your webhook url to use.

#### my-job-id

\*Optional. If you need an identifier from your system you can the job id as desired.

### Step 3 | Make Post Request

Make your **POST** transcript request. If successful, you will receive a confirmation response that will include the job
*"id"* \*(ex: fb724cc9-d0f7-44a1-86c4-180c7fab975e).

### Step 4 | Make Get Request

Make your GET transcript request. If successful, you will receive a JSON transcript output that will include the inputs
you requested.

##### Example Transcript Output

```json  theme={null}
{
    "id": "fb724cc9-d0f7-44a1-86c4-180c7fab975e",
    "input": {
        "url": "https://example.com/path/to/file.mp3",
        "language_code": "en",
        "word_level_timestamps": true,
        "return_as_file": false,
        "diarization": true,
        "sentence_diarization": true,
        "srt": true,
        "sentence_level_timestamps": true,
        "summarize": 50,
        "llm_translation": "french, german, portuguese",
        "srt_translation": "spanish, Hindi"
    },
    "status": "succeeded",
    "events": [
        {
            "action": "created",
            "time": "2024-10-05T19:22:20.1115308+00:00"
        },
        {
            "action": "started",
            "time": "2024-10-05T21:38:40.1424816+00:00"
        },
        {
            "action": "succeeded",
            "time": "2024-10-05T21:39:49.1000268+00:00"
        }
    ],
    "output": {
        "sentence_level_timestamps": [
            {
                "text": "You know that little voice in your head?",
                "timestamp": [
                    0.0,
                    5.9
                ],
                "start": 0.0,
                "end": 5.9,
                "speaker": "SPEAKER_02"
            },
            ...
            {
                "text": "Because when we change the dialogue, we can change our world.",
                "timestamp": [
                    115.14,
                    121.42
                ],
                "start": 115.14,
                "end": 121.42,
                "speaker": "SPEAKER_02"
            }
        ],
        "word_segments": [
            {
                "word": "You",
                "start": 4.274,
                "end": 4.395,
                "score": 0.89,
                "speaker": "SPEAKER_02"
            },
            {
                "word": "know",
                "start": 4.435,
                "end": 4.555,
                "score": 0.87,
                "speaker": "SPEAKER_02"
            },
            {
                "word": "that",
                "start": 4.576,
                "end": 4.696,
                "score": 0.773,
                "speaker": "SPEAKER_02"
            },
            {
                "word": "little",
                "start": 4.756,
                "end": 4.977,
                "score": 0.833,
                "speaker": "SPEAKER_02"
            },
            {
                "word": "voice",
                "start": 5.037,
                "end": 5.378,
                "score": 0.869,
                "speaker": "SPEAKER_02"
            }
            ...
            {
                "word": "world.",
                "start": 120.938,
                "end": 121.199,
                "score": 0.219,
                "speaker": "SPEAKER_02"
            }
        ],
        "srt_content": "1\n00:00:04,274 --> 00:00:05,880\nYou know that little voice in your head?\n\n2\n00:00:10,506 --> 00:00:13,240\nThe one that tells you to ignore a tasteless joke?\n\n3\n00:00:21,650 --> 00:00:25,920\nThe one that tells you to keep quiet when a client makes a racist comment?\n\n4\n00:00:31,604 --> 00:00:36,197\nThe little voice that tells you you're not smart enough because English isn't your\n\n5\n00:00:36,278 --> 00:00:37,100\nfirst language.\n\n6\n00:00:46,284 --> 00:00:50,138\nOr that it's okay to judge someone for leaving early because they have family\n\n7\n00:00:50,158 --> 00:00:50,660\ncommitments.\n\n8\n00:01:07,800 --> 00:01:11,880\nOr that it's not a big deal when everyone's opinion isn't considered.\n\n9\n00:01:21,129 --> 00:01:23,880\nYou may think you're the only one that hears that voice.\n\n10\n00:01:24,901 --> 00:01:27,659\nBut that voice also speaks to other people.\n\n11\n00:01:28,601 --> 00:01:30,819\nIt says, You're different.\n\n12\n00:01:32,202 --> 00:01:33,177\nYou're an outsider.\n\n13\n00:01:34,843 --> 00:01:35,899\nYou lack commitment.\n\n14\n00:01:37,020 --> 00:01:38,719\nYour opinion doesn't matter.\n\n15\n00:01:39,881 --> 00:01:45,619\nInstead of listening to that little voice, you need to find yours and make it heard.\n\n16\n00:01:51,651 --> 00:01:53,438\nIt's time for all of us to speak up.\n\n17\n00:01:56,143 --> 00:02:01,199\nBecause when we change the dialogue, we can change our world.\n\n",
        "summary": "Silence oppressive voices; amplify your own.",
        "llm_translations": {
            "French": "Connaissez-vous cette petite voix dans votre tête ? \n\nLa voix qui vous dit de ignorer une blague de mauvais goût ?\n\nLa voix qui vous dit de garder le silence quand un client fait un commentaire raciste ?\n\nLa voix qui vous dit que vous ne êtes pas intelligent(e) car l'anglais n'est pas votre langue maternelle ?\n\nOu que c'est normal de juger quelqu'un pour être parti tôt parce qu'il a des engagements familiaux ?\n\nLa voix qui vous dit de ne rien dire quand les autres sont réduits à des stéréotypes ?\n\nOu que ce n'est pas important de prendre en compte toutes les opinions ?\n\nVous pensez peut-être que vous êtes le seul à entendre cette voix. Mais cette voix parle également aux autres.\n\nElle dit : Vous êtes différent(e). Vous êtes un(e) extérieur(e). Vous manquez de détermination. Votre opinion n'a pas d'importance.\n\nAu lieu d'écouter cette petite voice, vous devez trouver la vôtre et faire entendre votre voix. \n\nC'est l'heure pour nous tous de parler. \n\nCar lorsque nous changeons le dialogue, nous pouvons changer notre monde.",
            "German": "Du weißt, diese kleine Stimme in deinem Kopf? Die eine, die dir sagt, ein unfassbarer Witz zu ignorieren? Die eine, die dich auffordert, leise zu sein, wenn jemand einen rassistischen Kommentar abgibt? Die kleine Stimme, die dir sagt, du seist nicht intelligent genug, weil Englisch nicht deine Muttersprache ist. Oder dass es in Ordnung ist, jemanden für früh zu gehen zu verurteilen, weil er Familienverpflichtungen hat. Die eine, die sagt, nichts sagen zu sollen, wenn andere zu Stereotypen reduziert werden. Oder dass das nicht großes Problem ist, wenn nicht alle Meinungen berücksichtigt werden. Du denkst vielleicht, du wärst der Einzige, der diese Stimme hört. Aber diese Stimme spricht auch andere Menschen an. Sie sagt: \"Du bist anders.\" \"Du bist ein Außenseiter.\" \"Du hast keine Verpflichtung.\" \"Deine Meinung zählt nicht.\" Anstatt dieser kleinen Stimme zu lauschen, musst du deine eigene finden und laut werden lassen. Es ist Zeit für uns alle aufzuschreien. Denn wenn wir die Konversation ändern, können wir unsere Welt verändern. Danke.",
            "Portuguese": "Você sabe aquele pequeno voz na sua cabeça? A que diz para ignorar uma piada sem graça? A que diz para ficar calado quando um cliente faz um comentário racista? A pequena voz que diz você não é inteligente o suficiente porque inglês não é a sua língua materna. Ou que está bem julgar alguém por sair cedo porque têm compromissos familiares. A que diz para não dizer nada quando os outros são reduzidos a estereótipos. Ou que não é um grande problema quando nenhuma opinião é considerada. Você pode pensar que você é o único que ouve aquela voz. Mas essa voz também fala com outras pessoas. Diz: Você é diferente. Você é estranho. Você falta de compromisso. Sua opinião não importa. Em vez de ouvir aquele pequeno voz, você precisa encontrar a sua e fazê-la ser ouvida. É hora para todos nós falarmos alto. Porque quando mudamos o diálogo, podemos mudar nosso mundo. Obrigado."
        },
        "srt_translation": {
            "Spanish": "1\n00:00:04,274 --> 00:00:05,880\n¿Sabes esa pequeña voz en tu cabeza?\n\n2\n00:00:10,506 --> 00:00:13,240\nLa que te dice ignorar un chiste de mal gusto?\n\n3\n00:00:21,650 --> 00:00:25,920\nLa que te dice callar cuando alguien hace un comentario racista?\n\n4\n00:00:31,604 --> 00:00:36,197\nEsa voz pequeña que te dice que no eres lo suficientemente inteligente porque el inglés no es tu\n\n5\n00:00:36,278 --> 00:00:37,100\nprimer idioma.\n\n6\n00:00:46,284 --> 00:00:50,138\nO que está bien juzgar a alguien por irse temprano porque tienen compromisos familiares.\n\n7\n00:00:50,158 --> 00:00:50,660\nO que no es un gran problema cuando no se considera la opinión de todos.\n\n8\n00:01:07,800 --> 00:01:11,880\nO que está bien con que nadie tenga la última palabra.\n\n9\n00:01:21,129 --> 00:01:23,880\nPuede parecer que solo tú escuchas esa voz.\n\n10\n00:01:24,901 --> 00:01:27,659\nPero esa voz también habla a otras personas.\n\n11\n00:01:28,601 --> 00:01:30,819\nDice: Eres diferente.\n\n12\n00:01:32,202 --> 00:01:33,177\nEres un forastero.\n\n13\n00:01:34,843 --> 00:01:35,899\nFaltas de compromiso.\n\n14\n00:01:37,020 --> 00:01:38,719\nTu opinión no importa.\n\n15\n00:01:39,881 --> 00:01:45,619\nEn lugar de escuchar esa voz pequeña, necesitas encontrar la tuya y hacer que se escuche.\n\n16\n00:01:51,651 --> 00:01:53,438\nEs hora de que todos hablamos.\n\n17\n00:01:56,143 --> 00:02:01,199\nPorque cuando cambiamos el diálogo, podemos cambiar nuestro mundo.",
        },
        "text": " You know that little voice in your head? The one that tells you to ignore a tasteless joke? The one that tells you to keep quiet when a client makes a racist comment? The little voice that tells you you're not smart enough because English isn't your first language. Or that it's okay to judge someone for leaving early because they have family commitments. The one that tells you not to say anything when others are being reduced to stereotypes. Or that it's not a big deal when everyone's opinion isn't considered. You may think you're the only one that hears that voice. But that voice also speaks to other people. It says, You're different. You're an outsider. You lack commitment. Your opinion doesn't matter. Instead of listening to that little voice, you need to find yours and make it heard. It's time for all of us to speak up. Because when we change the dialogue, we can change our world. Thank you.",
        "duration": 0.04,
        "processing_time": 68.46978211402893
    },
    "create_time": "2024-10-05T19:22:20.1115308+00:00",
    "update_time": "2024-10-05T21:39:49.1000268+00:00"
}
```

**"status"**

If your transcription request is *“pending”*, it has not yet been picked up for processing.

*“created”* the transcription job is now in our queue to be processed.

*“running”* the transcription is processing.

*“failed”* the transcript was not created. We will automatically re-try the transcription process until it fails three
times. If we are unable to transcribe your media, you will get a 200 error with one of the following messages. Send us a
support request at [support@salad.com](https://mailto:support@salad.com/) if this happens.

\*"succeeded" the transcript is ready. If we were not able to pull your url, or there was another issue with the audio
file you will see an "error" in the response and one of the reasons:

\*File size is more than 3GB \*File can not be downloaded or duration is missing. Please check your file and try again.
\*File duration is more than 2.5 hours

## API Reference

Access detailed API specifications and test requests directly by visiting the
[Transcription API Reference page](/reference/transcribe/inference_endpoints/create-an-inference-endpoint-job).

### Step 1: Set Up Authorization

* In the dropdown menu on the left, make sure **"Create a job for Salad Transcription API"** is selected.
* Enter your **Salad API key** and **Organization Name**. Follow instructions above if you do not know where to find
  them.
* Under the **Authorization** section, provide your **Salad API key**.
* Under the **Path** section, specify your organization name.

<img src="https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference1.png?fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=8e2ee1b2a53a69962e3c4eccc249c5cf" alt="Transcription API Reference" data-og-width="1499" width="1499" data-og-height="937" height="937" data-path="transcription/images/TranscriptionAPIReference1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference1.png?w=280&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=17cbf436e18032ede1036113e8ff88ec 280w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference1.png?w=560&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=9d97cb25390e2a869fae3cbbeb16d033 560w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference1.png?w=840&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=b68ff874833c901a0a03d75660997e5d 840w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference1.png?w=1100&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=3c5946fad51b2f3721a283835e1b33e1 1100w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference1.png?w=1650&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=8201dd305d76fc9820cad66140d43157 1650w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference1.png?w=2500&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=cbd4ddfc4eb7ec8ae6e2aeb6301b768e 2500w" />

### Step 2: Configure Input Parameters

* In the **Body** section, specify the input parameters as described in the documentation above.
* Each parameter is explained directly on the reference page to help you customize your request.

<img src="https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference2.png?fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=859a160e9366b99819706074ca3fcdeb" alt="Transcription API Reference 2" data-og-width="1508" width="1508" data-og-height="936" height="936" data-path="transcription/images/TranscriptionAPIReference2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference2.png?w=280&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=934557651d0bad09e6468a36d68b7b67 280w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference2.png?w=560&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=c6ec97f0ca60c13d5ea659af7b768556 560w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference2.png?w=840&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=c0f744b52ad54aff4e3e24e63fbeb2cd 840w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference2.png?w=1100&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=250627957cba7fa0daa75d5f6292179a 1100w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference2.png?w=1650&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=84ad0aefc4fda91ff1c1373f48f1711c 1650w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference2.png?w=2500&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=f13bf89bd7accff9f982f236de001c90 2500w" />

### Step 3: Submit the Request

* Click the **Send** button to submit the request.
* Upon success, you'll receive a response containing a unique `"id"` field. This **Job ID** will be used to retrieve the
  transcription results.

<img src="https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference3.png?fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=acb7b4a701ca1c47a145fb7c6e0fe523" alt="Transcription API Reference 3" data-og-width="684" width="684" data-og-height="744" height="744" data-path="transcription/images/TranscriptionAPIReference3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference3.png?w=280&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=f141e88470320b26fffc314a77843f9c 280w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference3.png?w=560&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=76cfceca03a5fdf7b678e2856ae43fc9 560w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference3.png?w=840&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=cfffc90d5bbc2ed13a35b420f1848af8 840w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference3.png?w=1100&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=094c4febe5d50a73977e4cff8adbb961 1100w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference3.png?w=1650&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=4753bb1c3cb389154568f662feaa505d 1650w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference3.png?w=2500&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=9ffb13a05ac18164b84dd92830c532cc 2500w" />

### Step 4: Retrieve Transcription Results

* In the dropdown menu on the left, select **"Get job for Salad Transcription API"**.
* Under the **Authorization** section, provide your **Salad API key**.
* Under the **Path** section, specify your **organization name** and the **Job ID** you received in Step 3.
* Click **Send** to fetch the transcription results.

<img src="https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference4.png?fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=d38a985d23f8df90cd7903f62065d4f6" alt="Transcription API Reference 4" data-og-width="1574" width="1574" data-og-height="864" height="864" data-path="transcription/images/TranscriptionAPIReference4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference4.png?w=280&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=8b992d2a918ec9834f2a1c40683d6e38 280w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference4.png?w=560&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=f46775a3f974f2fa080f2d372830a5fa 560w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference4.png?w=840&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=1cd79eba0a3c84b9c784951090a9e2a0 840w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference4.png?w=1100&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=f2b26cbf8e2a4855cb58386a00a77426 1100w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference4.png?w=1650&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=1d01ec6c7d31615957dad0188ef41267 1650w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference4.png?w=2500&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=50b3d50e8b70b830f25047f88969bbc3 2500w" />

### Example Response

* The response will include the transcription output, timestamps, and other requested data, depending on the parameters
  you specified.

<img src="https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference5.png?fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=56100350220cc577260830ce665e4c4c" alt="Transcription API Reference 5" data-og-width="645" width="645" data-og-height="745" height="745" data-path="transcription/images/TranscriptionAPIReference5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference5.png?w=280&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=2fdaa123accc2aa5a05659663ec24547 280w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference5.png?w=560&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=e21a654fed5d9f0e9526fc826d3aec15 560w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference5.png?w=840&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=adeb275df160a72dae64c7ca083aec43 840w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference5.png?w=1100&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=5c14ef70876991e1b2fbd4bca7db9194 1100w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference5.png?w=1650&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=46ea572718c03541febfa049989d0e2c 1650w, https://mintcdn.com/salad/MF5npb_t8nHGysAi/transcription/images/TranscriptionAPIReference5.png?w=2500&fit=max&auto=format&n=MF5npb_t8nHGysAi&q=85&s=671c478f039d624e7cbfbf8d14c70153 2500w" />

## Transcription Automation

Webhooks are already available, and you can check the documentation above (under Example cURL Post Transcript). Using
webhooks is a better way to get results as soon as possible. However, if your use case better fits with polling, use the
following code. Make sure you update it as needed:

### Pass 1: Submitting Audio Files for Transcription

This part of the script submits audio files for transcription and collects job IDs. The job IDs are used in the second
pass to check the status and retrieve the results.

```bash  theme={null}
import requests
import json
# Set the organization name, url, and API key
organization_name = "your_organization_name"
url = f"https://api.salad.com/api/public/organizations/{organization_name}/inference-endpoints/transcribe/jobs"
salad_key = "your_salad_key"
language_code = "en"
# Add your audio links here
list_of_audio_files = [
    "audio_url",
    "audio_url",
    "audio_url",
]
# If you want to pull links from a file, you can use the following code
# with open('audio_links.txt', 'r') as f:
#     list_of_audio_files = f.readlines()
# Placeholder for job_ids
list_of_job_ids = []
headers = {
    "Salad-Api-Key": salad_key,
    "Content-Type": "application/json",
    "accept": "application/json",
}
# Pass 1: Submit audio files for transcription
# Loop through the list of audio files and construct body of each request
for audio_file in list_of_audio_files:
    data = {
        "input": {
            "url": audio_file,
            "language_code": language_code,
            "word_level_timestamps": True,
            "diarization": True,
            "srt": True,
        }
    }
    # Send the request
    response = requests.post(url, headers=headers, json=data)
    # Pull job id from response. And save it to a list or a file
    job_id = response.json()["id"]
    list_of_job_ids.append(job_id)
    #save job_ids to a file if needed (uncomment the code below)
    # job_id_str = f'"{job_id}",'
    # # Open a file and write the job_id to it
    # with open('queue_test.txt', 'a') as f:
    #     f.write(job_id_str + '\n')

```

### Pass 2: Checking Job Status and Retrieving Results

This part of the script checks the status of each transcription job periodically and retrieves the results once the
transcription is completed.

```bash  theme={null}
    # Pass 2. Loop though the job_ids and get the results
    # If you use both passes in the same script, just continue.
    # If you use scripts separately you need to set up connection again
    # and initialize the list of job ids :
    # Uncomment the code below if you need to
    # import requests
    # import json
    # Set the organization name, url, and API key
    # organization_name = "your_organization_name"
    # url = f"https://api.salad.com/api/public/organizations/{organization_name}/inference-endpoints/transcribe/jobs"
    # salad_key = "your_salad_key"
    # language_code = "en"
    # headers = {
    #     "Salad-Api-Key": salad_key,
    #     "Content-Type": "application/json",
    #     "accept": "application/json",
    # }
    # Pull list from a file:
    # with open('queue_test.txt', 'r') as f:
    #     list_of_job_ids = f.readlines()
    # or initialize the list manually
    # list_of_job_ids = ["job_id1", "job_id2", "job_id3", "job_id4"]
import time
# Loop though the job_ids and get the results
while len(list_of_job_ids) > 0:
    for job in list_of_job_ids:
        response_url = f"https://api.salad.com/api/public/organizations/salad/inference-endpoints/transcribe/jobs/{job}"
        response = requests.get(response_url, headers=headers)
        if response.json()['status'] == 'running' or response.json()['status'] == 'pending':
          print(f"Job {job} is still {response.json()['status']}, waiting for retry...")
          continue
        elif response.json()['status'] == 'succeeded':

            #save the response to a file
            with open(f'result_{job}.json', 'w', encoding='utf-8') as f:
                json.dump(response.json(), f, ensure_ascii=False)
            #remove the job_id from the list
            list_of_job_ids.remove(job)
        else:
            print(f"Job {job} failed, waiting for retry...")
            # wait for 30 seconds and retry
            time.sleep(30)
            continue

```
