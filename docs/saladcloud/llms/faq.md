# Source: https://docs.salad.com/transcription/reference/faq.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Salad Transcription FAQ

*Last Updated: December 05, 2025*

***Does Salad Transcription have a web or app-based mobile experience?***

No, Salad Transcription is an API product. Learn more about our API documentation,
[here](/transcription/tutorials/transcription-quick-start).

***How does SaladCloud determine a transcription hour?***

SaladCloud calculates the number of hours based on the duration of your media, which is measured at the minute level.

Ex. A 12:34-minute video is calculated as (12\*60+34)/3600, which is 0.21 of an hour.

***How would you suggest I use the service if I’m not familiar with how APIs work?***

Check out this [API Reference Page](/transcription/tutorials/transcription-quick-start#api-reference) and follow the
instructions provided. Users can try Transcription services in the
[SaladCloud Portal](https://cloud-support.helpscoutdocs.com/article/425-how-to-try-transcription-services-in-the-salad-portal)
if they are unfamiliar with using an API.

***Does SaladCloud transcribe my media verbatim?***

No, we do not offer verbatim capability. Word repetitions and other small errors are automatically corrected.

***Is there a file size limit for transcription services?***

Salad Transcription supports up to 3GB media files. Media files that are longer than 2.5 hours in duration will need to
be split. If you you require support for larger files, contact our [support team](mailto:cloud@salad.com)

***How long will it take transcribe my file?***

Salad Transcription transcribes, on average, 5x faster than the duration of your media file. We use a sequential
long-form algorithm for transcription, prioritizing transcription accuracy over speed. If diarization and time codes are
enabled, it drops to about 4x faster as multiple passes are required.

***Is Transcription Lite faster?***

Transcription Lite is optimized for speed, processing audio at approximately 40x real-time speed, significantly reducing
turnaround times for transcription-only jobs, but its accuracy and number of features are lower compared to the standard
transcription service.

***How accurate is Salad Transcription?***

Salad Transcription is designed to provide high accuracy, typically achieving over 90% accuracy for clear audio with
normal background noise. For more details check our accuracy [benchmark](/transcription/reference/accuracy-benchmarks).
