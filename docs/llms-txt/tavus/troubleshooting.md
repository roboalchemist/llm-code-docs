# Source: https://docs.tavus.io/sections/troubleshooting.md

# Troubleshooting

> Find solutions to common problems and get back on track quickly with our troubleshooting guides.

## General

<AccordionGroup>
  <Accordion title="Training Video and Audio File Size Limit">
    If you see an error about file size, it means your training video or audio file is larger than the 750 MB limit.

    Tavus supports training videos and audio files **up to 750 MB**. This limit helps maintain a balance between quality and processing speed.
    <Note>Tavus requires the **H.264 codec** for all uploads.</Note>
    To reduce file size:

    * **Compress the file** using video compression tools.
    * **Lower the resolution** — 1080p is usually enough.
    * **Trim any extra content** to shorten the video.
    * **Reduce the frame rate** to around 30 fps.
  </Accordion>
</AccordionGroup>

## Conversational Video Interface (CVI)

<AccordionGroup>
  <Accordion title="Replica Responding to Background Noise">
    If the replica starts responding to background sounds, such as people talking nearby, it may be due to the absence of noise filtering.

    To resolve this, enable noise cancellation using Daily’s `updateInputSettings()` method. For example:

    ```js  theme={null}
    callFrame.updateInputSettings({
      audio: {
        processor: {
          type: 'noise-cancellation',
        },
      },
    });
    ```

    <Note>
      Learn more in the <a href="https://docs.daily.co/reference/daily-js/instance-methods/update-input-settings#audio-processor" target="_blank">Daily SDK documentation</a>.
    </Note>
  </Accordion>

  <Accordion title="Replica Is Not Joining the Conversation">
    This is a rare issue caused by an internal server problem. When it happens, our team is automatically notified and works to resolve it as quickly as possible.

    You can check the system status at <a href="https://status.tavus.io/" target="_blank">status.tavus.io</a>. We recommend checking periodically for updates if you encounter this error.
  </Accordion>
</AccordionGroup>

## Replica

<AccordionGroup>
  <Accordion title="Personal Replica Creation Failed">
    This error usually means your training video is missing the required consent statement or the statement wasn’t clearly spoken.

    To generate a digital replica using the Phoenix model, your video must include this line at the beginning, spoken clearly:

    > "I, \[FULL NAME], am currently speaking and give consent to Tavus to create an AI clone of me by using the audio and video samples I provide. I understand that this AI clone can be used to create videos that look and sound like me."

    Make sure to replace **\[FULL NAME]** with your actual name. The consent must be easy to hear and can be spoken in any supported language. You can view the <a href="/sections/conversational-video-interface/language-support" target="_blank">list of supported languages here</a>.

    If your video didn’t include this, re-record it with the consent statement at the beginning, then submit a new request through the <a href="https://platform.tavus.io/" target="_blank">Developer Portal</a> or <a href="/api-reference/phoenix-replica-model/create-replica" target="_blank">API</a>.
  </Accordion>

  <Accordion title="Poor Replica Quality">
    If your replica’s lip movements are noticeably out of sync, it may be due to issues with the training video format. Even if the video appears clean, AI-generated content or videos that don't follow the expected structure can affect training quality.

    Common causes:

    * The video **does not follow the required recording format**, which includes:
      * **1 minute of talking**
      * **1 minute of silence**
    * **Lips do not fully close** during the talking segment, which limits the model's ability to learn realistic lip movements.

    To improve your replica:

    * Record a new video following the correct structure (one minute of talking followed by one minute of silence).
    * Speak naturally, allowing full lip movement including closures.
    * Avoid using AI-generated videos for training.

    For more details, see the <a href="/sections/replica/replica-training" target="_blank">Replica Training Guide</a>.
  </Accordion>
</AccordionGroup>

## Video Generation

<AccordionGroup>
  <Accordion title="Poor Video Generation Quality">
    If your video looks unnatural or has repeated gestures, it may be due to the script length. Videos over **5 minutes** can lead to **reduced movement variety** and a **less natural feel**.

    To improve quality:

    1. **Keep videos short** – under 5 minutes is ideal.
    2. **Break long scripts** into smaller, focused segments.
    3. **Tighten the script** – remove filler and keep pacing steady.
    4. **Use multiple replicas** for variety in longer content.
    5. **Review and revise** – check for repetition and adjust as needed.
  </Accordion>
</AccordionGroup>

<Danger>
  If the issue persists after following the troubleshooting guide above, please don’t hesitate to [contact our support team](mailto:support@tavus.io) for further assistance.
</Danger>
