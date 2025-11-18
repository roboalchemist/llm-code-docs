# Source: https://docs.asapp.com/autotranscribe/product-guide.md

# AutoTranscribe Product Guide

> Learn more about the use of AutoTranscribe and its features

## Getting Started

This page provides an overview of the features and functionalities in AutoTranscribe.

After AutoTranscribe is integrated into your applications, you can use all of the configured features.

### Transcription Outputs

AutoTranscribe returns transcriptions as a sequence of utterances with start and end timestamps in response to an audio stream from a single speaker.

As the agent and customer speak, ASAPP's automated speech recognition (ASR) model transcribes their audio streams and returns completed utterances based on the natural pauses from each speaker. The expected latency between when ASAPP receives audio for a completed utterance and provides a transcription of that same utterance is 200-600ms.

<Note>
  Perceived latency will also be influenced by any network delay sending audio to ASAPP and receiving transcription messages in return.
</Note>

Smart Formatting is enabled by default, producing utterances with punctuation and capitalization already applied. Any spoken forms of utterances are also automatically converted to written forms (e.g. 'twenty two' shown as '22').

<Frame>
  <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e9807381-de3a-ed49-9c99-79421640a28c.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=a4027cc20c096001e829865f789b8289" data-og-width="994" width="994" data-og-height="376" height="376" data-path="image/uuid-e9807381-de3a-ed49-9c99-79421640a28c.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e9807381-de3a-ed49-9c99-79421640a28c.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=ea14f21a715c24f22423fe9c94e48f4b 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e9807381-de3a-ed49-9c99-79421640a28c.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=d5805d19b5f9b553937772e36637faa1 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e9807381-de3a-ed49-9c99-79421640a28c.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=05e2f895931d69fe9efc7d5878a1d3d0 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e9807381-de3a-ed49-9c99-79421640a28c.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=3159343db516b5a812420556190f8936 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e9807381-de3a-ed49-9c99-79421640a28c.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=a5ff73e227d42a2831bf10911978e37b 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e9807381-de3a-ed49-9c99-79421640a28c.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=7c517118326e9ba33a64e6a12e86f93b 2500w" />
</Frame>

### Redaction

AutoTranscribe can immediately redact audio for sensitive information, returning utterances with sensitive information denoted in hashmarks.

ASAPP applies default redaction policies to prevent exposure of sensitive combinations of numerical digits. To configure redaction rules for your implementation, consult your ASAPP account contact.

Visit the [Data Redaction](/security/data-redaction) section to learn more.

<Frame>
  <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-5e163ec2-b3c0-533c-710b-d784dbf42203.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=8d2c8ef4b05cff3909dc2b49b3524e9f" data-og-width="1866" width="1866" data-og-height="711" height="711" data-path="image/uuid-5e163ec2-b3c0-533c-710b-d784dbf42203.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-5e163ec2-b3c0-533c-710b-d784dbf42203.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=cf70ed840c672ea89ae889fb532d882a 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-5e163ec2-b3c0-533c-710b-d784dbf42203.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=a9792f4c7738719dec062af14a8d5fac 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-5e163ec2-b3c0-533c-710b-d784dbf42203.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=14d27c283b95b0436dfcb306cc29b297 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-5e163ec2-b3c0-533c-710b-d784dbf42203.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=1f784845d5a0ed6b19e140cfa825a7b7 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-5e163ec2-b3c0-533c-710b-d784dbf42203.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=367fa920ce10fdbdb9e48a4ed7334f52 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-5e163ec2-b3c0-533c-710b-d784dbf42203.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=8209386d706de757ede3e8710f31c21b 2500w" />
</Frame>

<note>
  Redaction is enabled by default. Smart Formatting must also be enabled (it is by default) in order for redaction to function.
</note>

## Customization

### Transcriptions

ASAPP customizes transcription models for each implementation of AutoTranscribe to ensure domain-specific context and terminology is well incorporated prior to launch.

Consult your ASAPP account contact if the required historical call audio files are not available ahead of implementing AutoTranscribe.

<table class="informaltable frame-void rules-rows">
  <tbody>
    <tr>
      <td class="td"><p><strong>Option</strong></p></td>
      <td class="td"><p><strong>Description</strong></p></td>
      <td class="td"><p><strong>Requirements</strong></p></td>
    </tr>

    <tr>
      <td class="td"><p>Baseline</p></td>
      <td class="td"><p>ASAPP’s general-purpose transcription capability, trained with no audio from relevant historical calls</p></td>
      <td class="td"><p>none</p></td>
    </tr>

    <tr>
      <td class="td"><p>Customized</p></td>
      <td class="td"><p>A custom-trained transcription model to incorporate domain-specific terminology likely to be encountered during implementation</p></td>

      <td class="td">
        <p>For English custom models, a minimum 100 hours of representative historical call audio between customers and agents</p>
        <p>For Spanish custom models, a minimum of 200 hours.</p>
      </td>
    </tr>
  </tbody>
</table>

<Note>
  When supplying recorded audio to ASAPP for AutoTranscribe model training prior to implementation, send uncompressed `.WAV` media files with speaker-separated channels.

  Recordings for training and real-time streams should have both the same sample rate (8000 samples/sec) and audio encoding (16-bit PCM).
</Note>

Visit [Transmitting Data to SFTP](/reporting/send-sftp) for instructions on how to send historical call audio files to ASAPP.

### Vocabulary

In addition to training on historical transcripts, AutoTranscribe accepts explicitly defined custom vocabulary for terms that are specific to your implementation.

AutoTranscribe also boosts detection for these terms by accepting what the term may ordinarily sound like, so that it can be recognized and outputted with the correct spelling.

Common examples of custom vocabulary include:

* Branded products, services and offers
* Commonly used acronyms or abbreviations
* Important corporate addresses

Custom vocabulary is sent to ASAPP for each audio transcription session, and can be consistent for all transcription requests or adjusted for different use cases (different brands, skills/queues, geographies, etc.)

<Note>
  Session-specific custom vocabulary is only available for AutoTranscribe implementations via WebSocket API.

  For Media Gateway implementations, transcription models can also be trained with custom vocabulary through an alternative mechanism. Reach out to your ASAPP account team for more information.
</Note>

## Use Cases

### For Live Agent Assistance

**Challenge**

Organizations are exploring technologies to assist agents in real-time by surfacing customer-specific offers, troubleshooting process flows, topical knowledge articles, relevant customer profile attributes and more. Agents have access to most (if not all) of this content already, but a great assistive technology makes content actionable by finding the right time to bring the right item to the forefront. To do this well, these technologies need to know both what's been said and what is being said in the moment with very low latency.

Many of these technologies face agent adoption and click-through challenges for two reported reasons:

1. Recommended content often doesn't fit the conversation, which may mean the underlying transcription isn't an accurate representation of the real conversation
2. Recommended content doesn't arrive soon enough for them to use it, which may mean the latency between the audio and outputted transcript is too high

**Using AutoTranscribe**

AutoTranscribe is built to be the call transcript input data source for models that power assistive technologies for customer interactions.

Because AutoTranscribe is specifically designed for customer service interactions and trained on implementation-specific historical data, the word error rate (WER) for domain and company-specific language is reduced substantially rather than being the subject of incorrect transcriptions that lead models astray.

To illustrate this point, consider a sample of 10,000 hours of transcribed audio from a typical contact center. A speech-to-text service only needs to recognize 241 of the most frequently used words to get 80% accuracy; those are largely words like "the", "you", "to", "what", and so on.

To get to 90% accuracy, the system needs to correctly transcribe the next 324 most frequently used words, and even more for every additional percent. These are often words that are unique to your business---the words that really matter.

<Tip>
  Read more here about [why small increases in transcription accuracy matter.](https://www.asapp.com/blog/why-a-little-increase-in-transcription-accuracy-is-such-a-big-deal/)
</Tip>

To ensure these high-accuracy transcript inputs reach models quickly enough to make timely recommendations, the expected time from audio received to transcription of that same utterance is 200-600 ms (excluding effects of network delay, as noted in *Transcription Outputs*).

### For Insights and Compliance

**Challenge**

For many organizations, lack of accuracy and coverage of speech-to-text technologies prevent them from effectively employing transcripts for insights, quality management and compliance use cases. Transcripts that fall short of accurately representing conversations compromise the usability of insights and leave too much room for ambiguity for quality managers and compliance teams.

Transcription technologies that aren't accurate enough for many use cases also tend to be employed only for a minority share of total call volume because the outputs aren't useful enough to pay for full coverage. As a result, quality and compliance teams must rely on audio recordings since most calls don't get transcribed.

**Using AutoTranscribe**

AutoTranscribe is specifically designed to maximize domain-specific accuracy for call center conversations. It is trained on past conversations before being deployed and continues to improve early in the implementation as it encounters conversations at scale.

For non real-time use cases, AutoTranscribe also supports processing batches of call audio at an interval that suits the use case.

Teams can query AutoTranscribe outputs in time-stamped utterance tables for data science and targeted compliance use cases or load customer and agent utterances into quality management systems for managers to review in messaging-style user interfaces.

### AI Services That Enhance AutoTranscribe

<Frame>
  <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-597c4697-359d-b13e-8532-9b2119d3381d.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=e15f17e7467349a953d5de50b1a6deba" data-og-width="2002" width="2002" data-og-height="669" height="669" data-path="image/uuid-597c4697-359d-b13e-8532-9b2119d3381d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-597c4697-359d-b13e-8532-9b2119d3381d.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=83b1175647b735ab613d63d404023943 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-597c4697-359d-b13e-8532-9b2119d3381d.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=8894af02ee5ec88b5d28c05d4e2c5f0f 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-597c4697-359d-b13e-8532-9b2119d3381d.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=00832e5efa5a70c81708c39fae1b8711 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-597c4697-359d-b13e-8532-9b2119d3381d.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=737555976e74a97d853a82a19027faed 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-597c4697-359d-b13e-8532-9b2119d3381d.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=6a565b9d628512b097143ef27e37ba60 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-597c4697-359d-b13e-8532-9b2119d3381d.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=6267bcd225d2f1331bbcf41ff4193e65 2500w" />
</Frame>

Once accurate call transcripts are generated, automatic summarization of those customer interactions becomes possible.

ASAPP AutoSummary is a recommended pairing with AutoTranscribe, generating analytics-ready structured summaries and readable paragraph summaries that save agents the distraction of needing to write and submit disposition notes on every call.

<CardGroup>
  <Card title="AutoSummary" href="/autosummary"> Head to AutoSummary Overview to learn more.</Card>
  <Card title="AutoSummary on ASAPP.com" href="https://www.asapp.com/products/ai-services/autosummary"> Learn more about AutoSummary on ASAPP.com </Card>
</CardGroup>

<note>
  AutoSummary currently supports English-language conversations only.
</note>
