# Source: https://docs.salad.com/container-engine/how-to-guides/ai-machine-learning/youtube-transcription-pipeline.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Transcribe YouTube Videos

*Last Updated: October 10, 2024*

To collect and transcribe massive videos from YouTube using SaladCloud, the process typically involves three key steps:

Data Collection from YouTube: Gather relevant video URLs from specific channels or based on particular topics, creating
video metadata files. These files include essential details such as video title, URL, duration and codec, etc.

Data Processing on SaladCloud: Input the gathered video URLs into a transcription pipeline, comprising a job queue such
as AWS SQS, accompanied by a job filler that monitors progress and injects jobs regularly, and numerous SaladCloud
nodes, each equipped with dedicated GPUs for transcribing. Additionally, utilize a NoSQL database like AWS DynamoDB to
store job results, while generated assets can be stored in Cloud Storage platforms such as Cloudflare R2.

Validation, Analysis and Delivery: Validate outcomes using both the metadata files and the job results. The videos that
failed to be transcribed can be further analyzed and may be refilled to the pipeline for reprocessing. Then, deliver the
final output, potentially including index files containing YouTube video URLs paired with their corresponding transcript
URLs on Cloudflare. This facilitates easy access to transcribed content for further analysis and utilization.

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/cfef23d-1-1.jpg?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=fdc20e021c6d35fbbbccb1dbef1be839" data-og-width="1073" width="1073" data-og-height="531" height="531" data-path="container-engine/images/cfef23d-1-1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/cfef23d-1-1.jpg?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=63d06046514faadef7f149be4a37360f 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/cfef23d-1-1.jpg?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=300cae208a57056aa1974bf8388d542e 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/cfef23d-1-1.jpg?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=e6265c405da93d706939181e2a3902e2 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/cfef23d-1-1.jpg?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=8a687de3f2187aec938fbf51c835c3ea 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/cfef23d-1-1.jpg?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=548b9255f17b48aeba4b31f995a289ca 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/cfef23d-1-1.jpg?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=82e8c1b7fe3ca17eebb6587611e72f6d 2500w" />

The three steps can either constitute a single end-to-end pipeline or operate as three independent steps, depending on
the specific business requirements.

Transcribing YouTube videos doesn't inherently require pre-downloading and storage of the videos. Simultaneous
downloading and transcribing are feasible. Additionally, if a YouTube video supports an audio codec, efficiency can be
improved by exclusively downloading its audio. This approach not only reduces bandwidth demands but also significantly
saves time, considering that video sizes are typically ten times larger than their corresponding audio files.

By leveraging the solution outlined in the documentation, we've managed to transcribe over 1 million hours of YouTube
videos in just a week. This was made possible by utilizing a resource group of 100 low to mid-end SaladCloud nodes, each
equipped with 2vCPU, 12GB RAM, and a GPU with 8GB or more VRAM.

# STEP 1: Data Collection from YouTube

We need to develop a job generator capable of accepting named channels or playlists, as well as keywords, as input
parameters. This generator will then produce multiple channel metadata files containing detailed information such as
video title, URL, duration, codec, and other relevant data. Additionally, it will create an index file that maps each
channel to its corresponding metadata file, ensuring organized and accessible storage of the collected data.

<img src="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/f647902-2.jpg?fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=94400402509348ee81ca91e61d443c54" data-og-width="827" width="827" data-og-height="383" height="383" data-path="container-engine/images/f647902-2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/f647902-2.jpg?w=280&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=2485c65cf064fba05d937aee9243c54a 280w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/f647902-2.jpg?w=560&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=d5a0fc74f62feff92e72a4008a3d61c3 560w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/f647902-2.jpg?w=840&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=fbcf3495aba0facabcd37ae2804d54f2 840w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/f647902-2.jpg?w=1100&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=82207750a39ba63f32dfbd8ef0c3e63d 1100w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/f647902-2.jpg?w=1650&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=80fb8b5e7153396e2950684b57385846 1650w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/f647902-2.jpg?w=2500&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=a96ee824a65bb29976d1d50d751eee26 2500w" />

The [index file](https://salad-public-transcripts.com/youtube_4m_videos_1.6m_hours_20240322.csv) comprises the following
details for each channel: channel title, ID, URL, playlist number, total video number, total video duration (hour), and
a link to the corresponding metadata file.

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5a72e29-3.jpg?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=3bfa0807b77f4270ca1f8db4652103ce" data-og-width="1053" width="1053" data-og-height="404" height="404" data-path="container-engine/images/5a72e29-3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5a72e29-3.jpg?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=c5f04843000e668e0617fece7dd39453 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5a72e29-3.jpg?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=4ac4e9e5d51705094f430fae84042f90 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5a72e29-3.jpg?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=27ef07ecafd484e2e8790ea2253ce669 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5a72e29-3.jpg?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=0d622d3db26ac24994ce967c444bf54d 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5a72e29-3.jpg?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=9fe45e733944fd0532433aeb9dd431ea 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5a72e29-3.jpg?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=708b3e6d2bac20592e818d9854f2fcd1 2500w" />

A [metadata file](https://salad-public-transcripts.com/datasets/0001.csv) offers extensive details of videos within a
channel, encompassing URL, title, duration (second), codec, and more. Extracting codec information for each video
requires additional operations and time. Hence, we opt to randomly select a subset of videos to collect this
information. Through our testing, we've noted that all YouTube videos encountered thus far support audio codecs.

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/b0cbf46-4.jpg?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=673d9215ad11865f08e87ae0ff9eac9b" data-og-width="902" width="902" data-og-height="404" height="404" data-path="container-engine/images/b0cbf46-4.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/b0cbf46-4.jpg?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=1305fcf4743a3853e84e6a2957bb0695 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/b0cbf46-4.jpg?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=d1c33704206ea3897345a9ba49494dc8 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/b0cbf46-4.jpg?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=469499a68d2f591ab4b1ebbdd16b9743 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/b0cbf46-4.jpg?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=a64e504b4ec8aaf7b67f507b52c43a21 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/b0cbf46-4.jpg?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=7900b1776aa033725f9de81f2ddb4487 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/b0cbf46-4.jpg?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=b2d1d1d60e4610cfb3df2ec58962701c 2500w" />

Downloading video metadata from a channel is time-consuming, ranging from a few minutes to several hours, depending on
the channel's size. Additionally, there are constraints on concurrent access from a single IP address to YouTube.

Through testing, we've implemented and executed the job generator on a standard computer, achieving a collection rate of
approximately 1 million video URLs per day using combined solutions over a single IP address. To exceed this limit or to
further optimize time efficiency, leveraging the global distributed network provided by SaladCloud is recommended.
Building a job generation pipeline over a small pool of SaladCloud nodes distributed across the global Internet can
significantly accelerate the process.

## Build the Job Generator

We can utilize a variety of tools and libraries to construct the job generator:

### [YouTube Data API v3](https://developers.google.com/youtube/v3/getting-started) and [Google API Client Library](https://developers.google.com/youtube/v3/quickstart/python)

This tool offers all the necessary functionalities for interacting with YouTube, such as searching channels, playlists,
and videos based on keywords, retrieving all playlists from a particular channel, and uploading/downloading videos.

To utilize the API, we must possess a Google Account to request an API key and choose a client library, such as Python.
While the API is free to use, each GCP project enabled with the YouTube Data API has a default quota allocation of
10,000 units per day. All API requests, including invalid requests, incur a
[quota cost](https://developers.google.com/youtube/v3/determine_quota_cost).

Now, let's calculate the quota cost for collecting video URLs from a search on a specific keyword:

| Assumption                                                                                                         | Quota Cost | Explanations                                                                                      |
| :----------------------------------------------------------------------------------------------------------------- | :--------- | :------------------------------------------------------------------------------------------------ |
| Search and get 100 channels based on a keyword                                                                     | 200        | Executing a search.list needs 100 units and it can return a maximum of 50 items: 100 x 2          |
| Get 10,000 playlists from the 100 channels, assuming each channel contains 100 playlists                           | 200        | Executing a playlist.list requires 1 unit and it can return a maximum of 50 items: 100 x 1 x 2    |
| Get 2,000,000 video URLs from the 10,000 playlists of the 100 channels, assuming each playlist contains 200 videos | 40,000     | Executing a video.list requires 1 unit and it can return a maximum of 50 items: 100 x 100 x 1 x 4 |

The default quota allocation of 10,000 units per day may prove insufficient if we need to collect numerous video URLs in
a short time frame. We can create several GCP projects with each providing 10,000 units per day, or we could also
complete [an audit](https://developers.google.com/youtube/v3/guides/quota_and_compliance_audits) and request an
additional quota following the process. Here we provide a combined solution by using both YouTube Data API and Pytube.

### [ Pytube](https://pytube.io/en/latest/), a lightweight library for downloading YouTube videos

Pytube bypasses the YouTube Data API by directly scraping the YouTube website, thereby avoiding any quota limits imposed
by the API. However, it does not offer access to the complete range of functionalities available through the YouTube
API. For instance, it lacks the ability to perform searches with diverse request parameters such as location and
relevance language. Nevertheless, Pytube excels at retrieving all video URLs and associated metadata (such as title,
codec, video or audio format, etc.) within a specified playlist, and filtering and downloading streams, the tasks that
would otherwise consume the most significant portion of the quota cost units if executed using the YouTube Data API.

A combined solution enables us to harness the strengths of both tools while alleviating their respective limitations.
Utilizing the YouTube Data API and its Python Client, we can search for channels based on keywords and retrieve all
playlists within each channel. Subsequently, Pytube can be utilized to download all video metadata from these playlists.

It is noteworthy that Pytube does not have a limit on API quota, but it is still constrained by the number of concurrent
accesses from a single IP address imposed by YouTube.

### The reference design for the job generator

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/19b1ccc-5.jpg?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=e26ec179085316d08a8fdad21b5980fa" data-og-width="828" width="828" data-og-height="510" height="510" data-path="container-engine/images/19b1ccc-5.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/19b1ccc-5.jpg?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=c2a1609f814e5a1a2eaf9620b6af406b 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/19b1ccc-5.jpg?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=5983cc443b30e145f828376cfd54ad1b 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/19b1ccc-5.jpg?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=b6010a75296eb19fa4e0aa34ea288a1d 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/19b1ccc-5.jpg?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=c0b2a74fbbb79805ab1a081120be3f5e 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/19b1ccc-5.jpg?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=1ca4ccc617fb3955146fbee4a840b89e 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/19b1ccc-5.jpg?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=5974a2d0c634af1fabb0c7faa8a31b5a 2500w" />

We use a two-tier system for managing our collection: first, we create a metadata file for each channel, containing
comprehensive details of all videos within the channel. Then, we maintain an index file that consolidates all the
collected channels, with each channel linked to its corresponding metadata file.

This helps prevent duplicate channels by checking the index file when processing a new channel. However, there may still
be instances of duplicated videos stemming from different channels or playlists. For example, a playlist within Channel
A might reference a video originally uploaded on Channel B. This scenario requires additional consideration to handle
duplicated videos across various channels or playlists effectively.

Downloading video metadata from a playlist can be I/O-bound and time-consuming, taking from a few minutes to several
hours, especially for playlists with numerous videos. To expedite this process, we employ multiple processes to
concurrently handle the playlists within a channel.

For instance, if a channel contains 100 playlists, we divide and store these playlists into 10 temporary files. Each
file serves as input for a separate process, responsible for downloading video metadata from its designated input file
and saving the results to a corresponding temporary output file. Once all processes have completed their tasks, we merge
the temporary output files into the final metadata file for the channel and update the index file accordingly.

We conducted tests with different numbers of processes. When the number was over 10, the IP address was promptly blocked
by YouTube. Despite this limitation, we managed to collect approximately 1 million video URLs, equivalent to around
300,000 hours of video content, per day using the aforementioned method.

It is important to note that not all collected video URLs remain valid over time as new videos are continuously being
added to the channels and playlists that we have already collected. Some videos may experience changes in permissions,
being publicly accessible today but removed or restricted to membership-only access or accessible only to logged-in
users tomorrow. Additionally, some videos may be static pictures or lengthy monitoring videos without any meaningful
content. Therefore, it's crucial to filter the content and inject the valid URLs into the transcription pipeline.
Moreover, implementing robust mechanisms in the code to handle various exceptions is essential to ensure resilience.

Please refer to the
[example code](https://github.com/SaladTechnologies/yt-1m-hours-transcription-test/blob/main/job_generator.py) for the
job generator implementation.

## Build the job generation pipeline

To further enhance the efficiency of the job generation process, we can divide the job generator into several components
and build a job generation pipeline:

Channel Manager: This component manages the index file and supports operations such as search, creation, and update. It
needs to be publicly accessible and can be implemented using AWS Lambda backed by AWS DynamoDB.

Channel Collector: This component gathers relevant channels based on specific topics. It interacts with the Channel
Manager to verify the existence of a channel and creates a new record if it doesn’t already exist. Once validated, it
sends the channel URL to the job queue, such as AWS SQS, for further processing.

Metadata Downloader: This component runs on a pool of SaladCloud nodes distributed across the global Internet. Each node
retrieves a channel URL from the job queue, gathers all playlists within the channel, and downloads video metadata from
these playlists using the multiprocessing approach. Upon completion, it creates the channel metadata file in Cloudflare,
updates the corresponding record through the Channel Manager, and removes the processed job from the queue.

With this solution, we can effectively harness the global distributed network provided by SaladCloud, significantly
accelerating the job generation process by tens or even hundreds of times.

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/991061d-6.jpg?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=7ffc714202adcebbdc7ba5ce349c390b" data-og-width="941" width="941" data-og-height="504" height="504" data-path="container-engine/images/991061d-6.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/991061d-6.jpg?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=4c52eb2fae49e9b166a785b9244aee1f 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/991061d-6.jpg?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=d3a18aa1b5ce6fc69789b79225fa4799 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/991061d-6.jpg?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=ed83bb588f067ff1692ff09680f5b899 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/991061d-6.jpg?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=9fe56f3dc0d3338f6693250243d693b9 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/991061d-6.jpg?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=61ae6cb34a73c1c23bceaeb678d95151 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/991061d-6.jpg?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=534c78f62d3889d39349163a60fb214b 2500w" />

# STEP 2: Data Processing on SaladCloud

The transcription pipeline consists of:

YouTube and its CDN: YouTube utilizes a Global Content Delivery Network (CDN) to distribute content efficiently. The CDN
edge servers are strategically dispersed across various geographical locations, serving content in close proximity to
users, and enhancing the speed and performance of applications.

GPU Resource Pool and Global Distributed Network: Hundreds of SaladCloud nodes, equipped with dedicated GPUs, are
utilized for tasks such as downloading/uploading, pre-processing/post-processing and transcribing. These nodes assigned
to GPU workloads are positioned within a global, high-speed distributed network infrastructure, and can effectively
align with YouTube’s Global CDN, ensuring optimal system throughput.

Job Queue System: The SaladCloud nodes retrieve jobs via the message queue like AWS SQS, providing the video URLs and
where to store the generated assets (Cloudflare URLs).

Job Filler: It generates jobs based on the index file and metadata files during the STEP 1, monitors the transcription
pipeline process and ensures a consistent supply of tasks by replenishing them regularly.

Cloud Storage: Generated assets stored in Cloudflare R2, which is AWS S3-compatible and incurs zero egress fees.

Job Recording System: Job results, including YouTube video URLs, audio length, processing time, Cloudflare URLs, word
count etc., are stored in NoSQL databases like AWS DynamoDB.

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/49a6736-7.jpg?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=23e087f33fffbc2997fc210379f003b1" data-og-width="847" width="847" data-og-height="519" height="519" data-path="container-engine/images/49a6736-7.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/49a6736-7.jpg?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=b3ff0c012a138c0866aceab538128065 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/49a6736-7.jpg?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=7130c61b65923d9af721353dfb1efc18 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/49a6736-7.jpg?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=bf63fbac97423f54d56889d44bb37b60 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/49a6736-7.jpg?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=957850e8a2d839d8064b1c877915d119 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/49a6736-7.jpg?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=cc268ab66857eea354c31d981ee0b1db 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/49a6736-7.jpg?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=a255516ec0cce7f398f454dc9ceed78c 2500w" />

## Job Filler

The job filler must be versatile in supporting multiple job injection strategies. It should be capable of injecting
millions of hours of video URLs to the job queue instantly and remains idle until the pipeline completes all tasks.
However, a potential issue with this approach arises when certain nodes in the pipeline experience downtime and fail to
process and remove jobs from the queue. Consequently, these jobs may reappear for other nodes to attempt processing,
potentially causing earlier injected jobs to be processed last, which may not be suitable for certain use cases.

Another approach is to continuously monitor the size of the job queue. The job filler will inject new jobs only when
there are nearly no available tasks left in the queue. This method ensures that the pipeline can complete time-sensitive
tasks efficiently. The job filler must maintain high availability, as any failure could potentially cause the pipeline
to run idle, leading to delays in task completion.

Here is an example: Every day, we initially inject a large batch of jobs into the pipeline and monitor progress. When
the queue is nearly empty, we start injecting only a few jobs and aim to keep the number of available jobs in the queue
as low as possible for a period of time. This strategy allows us to prioritize completing older jobs before injecting a
massive influx of new ones.

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6a9c6fc-8.jpg?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=17121372a027adeac8e4e82c815cb3f2" data-og-width="1278" width="1278" data-og-height="573" height="573" data-path="container-engine/images/6a9c6fc-8.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6a9c6fc-8.jpg?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=8e71aed961f36882e387b362d1f944f3 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6a9c6fc-8.jpg?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=3140676f695b8d416b0caae15e8fafa8 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6a9c6fc-8.jpg?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=bc26fbf04377b107eceb2392831f13d5 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6a9c6fc-8.jpg?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=80311e6d9c25cbf561913e6c87dabdab 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6a9c6fc-8.jpg?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=ac6cc42e01fc9b9b92ac356ead98343d 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6a9c6fc-8.jpg?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=2c01d0cb086c9b30c709a162f68e89a3 2500w" />

For time-sensitive tasks, implementing autoscaling is also beneficial. By continually monitoring the job count in the
queue, the job filler dynamically adjusts the number of SaladCloud node groups. This adaptive approach ensures that
specific quantities of tasks can be completed within a predefined time frame while also offering the flexibility to
manage costs efficiently during periods of reduced demand.

### The reference design for the job filler

Job Filter: It filters the original video URLs based on video length and channels, removing unqualified content such as
videos that are too short or too long, purely musical, or in a non-English language, etc. Subsequently, generates a
specified number of hours of tasks from the index file and metadata files, and adds them to the local job queue. The job
filter utilizes a cursor to track progress and generate new tasks after the position of the last generated task, thereby
supporting various job injection strategies.

Job Uploader: Operates on multiple threads to boost throughput; each thread retrieves jobs from the local job queue, and
uses AWS SendMessageBatch to transmit up to 10 jobs simultaneously.

Through testing, the job filler has demonstrated the capability to inject up to 1 million jobs to AWS SQS within a
single hour.

<img src="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/eaf53ec-9.jpg?fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=cdb47ac1936ac2fffa90261809c7523b" data-og-width="882" width="882" data-og-height="460" height="460" data-path="container-engine/images/eaf53ec-9.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/eaf53ec-9.jpg?w=280&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=3b0ea46ecd97fab6086aaece7bb2efc6 280w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/eaf53ec-9.jpg?w=560&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=09b130a3bc6a568b79a3c33a2be29ddb 560w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/eaf53ec-9.jpg?w=840&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=b5726614e4dcd37c7d586deecbe817c1 840w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/eaf53ec-9.jpg?w=1100&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=22ae41497eb853fe6c358a42c20f3084 1100w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/eaf53ec-9.jpg?w=1650&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=5f2805b0afc54369fb1e380ffd39ca30 1650w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/eaf53ec-9.jpg?w=2500&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=f894050b41b1c2ade8fcbb0bd04344a7 2500w" />

Below are the examples of jobs sent from the job filler to the job queue:

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4647030-10.jpg?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=51c2f1ee4922e57b6e0fca4fab0220f4" data-og-width="804" width="804" data-og-height="128" height="128" data-path="container-engine/images/4647030-10.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4647030-10.jpg?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=6ea629a689224e257e727ed62ea34440 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4647030-10.jpg?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=4aa7ecb86e9b803ef93da666c460cc63 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4647030-10.jpg?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=2d775a9edd149b41b9b4344cd5facd6c 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4647030-10.jpg?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=05738403bf82b11dd88ec4ceb4979913 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4647030-10.jpg?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=928d34d592a330356c5e10e5a31a0533 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4647030-10.jpg?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=01791fca317987079aa05543fe03ffee 2500w" />

## Job Queue System Settings

We set the AWS SQS Visibility Timeout to 1 hour. This allows sufficient time for downloading, chunking, buffering, and
processing by most of the nodes in SaladCloud until final results are merged and uploaded to Cloudflare. If a node fails
to process and remove polled jobs within the hour, the jobs become available again for other nodes to process.

Additionally, the AWS SQS Retention Period is set to 2 days. Once the message retention quota is reached, messages are
automatically deleted. This measure prevents jobs from lingering in the queue for an extended period without being
processed for any reason, thereby avoiding wastage of node resources.

## Node Implementation on SaladCloud (using Parakeet TDT 1.1B)

Within each node in the GPU resource pool in SaladCloud, we follow best practices by utilizing two processes: the
Inference Process, dedicated to GPU-based transcription inference; and the Benchmark Worker Process, focused on I/O- and
CPU-bound tasks, such as downloading/uploading, pre-processing, and post-processing.

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/bc5a767-11.jpg?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=2230b05c95492a9cd2bf15c4368a1a7d" data-og-width="878" width="878" data-og-height="481" height="481" data-path="container-engine/images/bc5a767-11.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/bc5a767-11.jpg?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=b071993bf4c11f2c286062bec643eeb9 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/bc5a767-11.jpg?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=7b38ad90e7c8430901e5762e182a8c98 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/bc5a767-11.jpg?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=2b8549e02274226f5f8645faeb63697d 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/bc5a767-11.jpg?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=f9e1b26bf8e2bcd4cce480ac541cdda6 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/bc5a767-11.jpg?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=5deb2859ac210fcc7d4637553c09438b 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/bc5a767-11.jpg?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=b3be72442ce7f882c375cb81b5c1dad5 2500w" />

### Inference Process

The transcription for audio involves resource-intensive operations on both CPU and GPU, including format conversion,
re-sampling, segmentation, transcription and merging. The more CPU operations involved, the lower the GPU utilization
experienced.

While having the capacity to fully leverage the CPU, multiprocessing or multithreading-based concurrent inference over a
single GPU might limit optimal GPU cache utilization and impact performance. This is attributed to each inference
running at its own layer or stage. The multiprocessing approach also consumes more VRAM as every process requires a CUDA
context and loads its own model into GPU VRAM for inference.

Following best practices, we delegate more CPU-bound pre-processing and post-processing tasks to the benchmark worker
process, allowing the inference process to concentrate on GPU operations and run on a single thread. It begins by
loading the model, warming up the GPU, and then listens on a TCP port by running a Python/FastAPI app on a Unicorn
server. Upon receiving a request, it invokes the transcription inference and promptly returns the generated assets.

Batch inference can be employed to enhance performance by effectively leveraging GPU cache and parallel processing
capabilities. However, it requires more VRAM and might delay the return of the result until every single sample in the
input is processed. The choice of using batch inference and determining the optimal batch size depends on model,
dataset, hardware characteristics and use case; and requires experimentation and ongoing performance monitoring.

### Benchmark Worker Process

The benchmark worker process primarily handles various I/O- and CPU-bound tasks, such as downloading/uploading,
pre-processing, and post-processing.

The Global Interpreter Lock (GIL) in Python permits only one thread to execute Python code at a time within a process.
While the GIL can impact the performance of multithreaded applications, certain operations remain unaffected, such as
I/O operations and calling external programs.

To maximize performance with better scalability, we adopt multiple threads to concurrently handle various tasks, with
two queues created to facilitate information exchange among these threads.

| Thread     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| :--------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Downloader | In most cases, we require 3 threads to concurrently pull jobs from the job queue and download audio files from YouTube, and efficiently feed the inference server. It also performs the following pre-processing steps: 1.Removal of bad audio files; 2.Format conversion from Mp4A to MP3; 3.Chunking very long audio into 10-minute clips; 4.Metadata extraction (URL, file/clid ID, length). The pre-processed audio files are stored in a shared folder, and their metadata are added to the transcribing queue simultaneously. To prevent the download of excessive audio files, we enforce a maximum length limit on the transcribing queue. When the queue reaches its capacity, the downloader will sleep for a while. |
| Caller     | It reads metadata from the transcribing queue, and subsequently sends a synchronous request, including the audio filename, to the inference server. Upon receiving the response, it forwards the generated texts along with statistics, and the transcribed audio filename to the reporting queue. The simplicity of the caller is crucial as it directly influences the inference performance.                                                                                                                                                                                                                                                                                                                                |
| Reporter   | The reporter, upon reading the reporting queue, deletes the processed audio files from the shared folder and manages post-processing tasks, including merging results and calculating real-time factor and word count. Eventually, it uploads the generated assets to Cloudflare, reports the job results to AWS DynamoDB and removes the processed jobs from AWS SQS.                                                                                                                                                                                                                                                                                                                                                         |

By running two processes to segregate GPU-bound tasks from I/O and CPU-bound tasks, and fetching and preparing the next
audio clips concurrently and in advance while the current one is still being transcribed, we can eliminate any waiting
period. After one audio clip is completed, the next is immediately ready for transcription. This approach not only
reduces the overall processing time for batch jobs but also leads to even more significant cost savings.

Please refer to the[ example code](https://github.com/SaladTechnologies/yt-1m-hours-transcription-test/tree/main/node)
for the node implementation.

## Optimization of Performance and Throughput

You can define a resource group on SaladCloud that encompasses various GPU types. These resources are distributed across
the global Internet, each with varying bandwidth and latency to specific endpoints. Moreover, the performance of each
node and the number of running replicas within a group may fluctuate over time due to their shared nature.

To optimize node performance and system throughput, consider the following best practices:

Define Initialization Time Threshold: Establish a threshold for initialization time, encompassing tasks such as model
loading and warm-up. If a node's initialization time exceeds this threshold, such as 300 seconds, the code should exit
with a status of 1. SaladCloud will allocate a new node in response, ensuring that nodes are adequately prepared to
execute your application.

Monitor Real-Time Performance: Continuously monitor application performance within a specific time window. If
performance metrics, such as the real-time factor (calculated as audio length divided by processing time, serving as an
efficient measure of transcription performance), fall below a predefined threshold, the code should exit with a status
of 1, prompting reallocation. This practice ensures that nodes remain in an optimal state for application execution. For
example, most nodes can achieve a real-time factor of 80 or higher for long audio; if the real-time factor of a node
falls below 20 during a monitoring period, it should be removed from the resource pool immediately.

Adopt Adaptive Algorithms: Recognize that nodes may vary in GPU types and network performance. High-performance nodes
can handle longer chunks with a large transcription queue (100), whereas low-performance nodes are better suited for
processing shorter chunks with a smaller transcription queue (50). By employing adaptive algorithms, resource
utilization can be optimized, while preventing low-performance nodes from impeding overall progress.

## Single Node Test

Before deploying the application container image on a large scale on SaladCloud, we can build a specialized application
image with JupyterLab and conduct the single-node test across various types of SaladCloud nodes.

With JupyterLab’s terminal, we can log into a container instance running on SaladCloud, gaining OS-level access. This
enables us to conduct various tests and optimize the configurations and parameters of the model and application. These
include:

Measure the time to download the model and then load it into the GPU, including warm-up, to define the appropriate
health check count.

Analyze the VRAM usage variations during the inference process based on long audio lengths and different batch sizes,
and select the best performing or most cost-effective GPU types for the application.

Determine the minimum number of downloader threads and maximum length limit of the transcribing queue to efficiently
feed the inference server.

Identify and handle various possible exceptions during application runtime, etc.

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/78a6585-12.jpg?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=2daeb91872b1a8b640be0ad554912484" data-og-width="842" width="842" data-og-height="441" height="441" data-path="container-engine/images/78a6585-12.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/78a6585-12.jpg?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=056151f085b68603d6e316c9eab036b2 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/78a6585-12.jpg?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=b56ebf2e1c8946828d646ce8555a7614 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/78a6585-12.jpg?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=a698ea18124c2d01aea6f78451358612 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/78a6585-12.jpg?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=e7906a90ad9f9fc2429c4caff81e82ba 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/78a6585-12.jpg?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=5fe63d740778aefea8dd0235247bb308 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/78a6585-12.jpg?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=d3dd4e08f0a00adf2744d2e693c589b2 2500w" />

# STEP 3: Validation, Delivery and Analysis

Job results, which include video URL, audio length, processing time, Cloudflare URL, and word count for each video,
serve multiple purposes.

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4fdaab6-13.jpg?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=7f70a67d3ad86250cd5acd83d74ffd32" data-og-width="969" width="969" data-og-height="488" height="488" data-path="container-engine/images/4fdaab6-13.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4fdaab6-13.jpg?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=5703e2902c7b0a9b8ffb24516b5a706d 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4fdaab6-13.jpg?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=1b52534d7c2ca4feb0500dc3e55fe07b 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4fdaab6-13.jpg?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=e8827e6db91c60a269098c8368ebd60c 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4fdaab6-13.jpg?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=089aefc9ea8983bc6afbb76e7de98054 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4fdaab6-13.jpg?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=d3074d426d117a19159e6e47e1b972a4 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4fdaab6-13.jpg?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=775dec88c17e7150e82982092fa15799 2500w" />

When combined with the index file and metadata files, the job results become instrumental in validating the pipeline
output. They provide crucial information such as processing time, word count and Cloudflare URL for each video, as well
as identify how many and which videos failed to be transcribed. In cases where videos failed to be transcribed, we can
analyze the reasons and may refill them into the transcription pipeline for reprocessing.

Job results also provide the information like how many nodes have been actually allocated and their GPU types, and how
many transcription jobs have been done by each node and each GPU type, and the corresponding real-time factors.
Leveraging this information enables us to identify the best-performing and most cost-effective GPU types for specific
tasks, thereby optimizing our future applications for enhanced efficiency and performance.

The final output comprises index files containing mappings from YouTube URLs to Cloudflare URLs, organized according to
specific channels, topics, and title keywords. These index files adhere to a predefined schema and are intended to serve
as input for subsequent pipelines, facilitating further analysis.

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1316655-14-1.jpg?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=c0e31c259681ff4bb2b981e17c3e0216" data-og-width="948" width="948" data-og-height="509" height="509" data-path="container-engine/images/1316655-14-1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1316655-14-1.jpg?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=cd417ad5e57d3d440a15611e42656157 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1316655-14-1.jpg?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=44662b7bea033b452c04c6ea2bb6b22e 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1316655-14-1.jpg?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=4c814592a164157f7d8d1d0820f8379c 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1316655-14-1.jpg?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=773c544faf47f9dbd60c34420c996aa1 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1316655-14-1.jpg?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=e00a20d40e721cca4ac0018f39f9b561 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1316655-14-1.jpg?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=e14f8f9d221da509f850f98c1c4ed40d 2500w" />

# [Example Code](https://github.com/SaladTechnologies/yt-1m-hours-transcription-test)

| Code                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                |
| :----------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| job\_generator.py                                      | Generates metadata files in the directory "./metadata/" and updates the index file located at "./index.csv" based on named channels and search queries. Creates temporary input and output files in the directory "./temp\_files/” for multiprocessing downloads. The file “topics.csv” contains a list of popular topics. Please ensure that the environment variable GCP\_API\_KEY is set.                               |
| job\_queue\_access.py                                  | Provides the access to the job queue and is imported by Job Filler, Job Cleaner and Job Monitor. Please ensure that the following environment variables are set: AWS\_ID, AWS\_KEY and QUEUE\_URL.                                                                                                                                                                                                                         |
| job\_filler.py                                         | Supports two job injection strategies: one-time injection and send-monitor-replenish. Need access to the index file located at "./index.csv” and metadata files in the directory "./metadata/”. Keep the cursor at the file “./last\_position” to track progress, and send new tasks to the job queue after the position of the last generated task.                                                                       |
| job\_queue\_cleaner.py                                 | Purge the job queue mainly for tests.                                                                                                                                                                                                                                                                                                                                                                                      |
| job\_queue\_monitor.py                                 | Monitor the available jobs in the queue and forecast when the queue will be empty.                                                                                                                                                                                                                                                                                                                                         |
| node/app/api\_parakeet.py, node/bench/benchmark\_1m.py | The inference process and the benchmark worker process.                                                                                                                                                                                                                                                                                                                                                                    |
| node/Dockerfile.parakeet.yt1m                          | The dockerfile to build the image. 10 environment variables are required to run the image: 1.Access the Job Queue System (AWS SQS):AWS\_ID, AWS\_KEY and QUEUE\_URL; 2.Access the Cloud Storage (Cloudflare R2):CLOUDFLARE\_ID, CLOUDFLARE\_KEY and CLOUDFLARE\_URL; 3.Access the Job Reporting System (AWS Lambda to AWS DynamoDB): BENCHMARK\_ID, REPORTING\_API\_URL, REPORTING\_AUTH\_HEADER and REPORTING\_API\_KEY . |
