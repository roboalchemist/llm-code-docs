# Source: https://docs.argil.ai/resources/captions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.argil.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Captions

Captions are a crucial part of a video - among other topics, it allows viewers to watch them on mobile without sound or understand the video better.

/

### Adding captions from a script

<Tip>
  Make sure to enable "Auto-captions" on the script page before generating the preview to avoid generating them later
</Tip>

<Steps>
  <Step title="Toggle the captions in the right sidebar" />

  <Step title="Pick style, size and position">
    Click on the "CC" icon to open the styling page and pick your preferences.
  </Step>

  <Step title="Preview the results">
    Preview the results by clicking play and make sure the results work well
  </Step>
</Steps>

### Editing captions for Audio-to-video

If you uploaded an audio instead of typing a script, we use a different way to generate captions <u>since we don't have an original text to pull from</u>. As such, this method contains more error.

<Steps>
  <Step title="Preview the captions to see if there are typos" />

  <Step title="Click on the audio segment that has inaccurate captions" />

  <Step title="Click on the word you wish to fix, correct it, then save" />
</Steps>

### Frequently asked questions

<AccordionGroup>
  <Accordion title="How do I fix a typo in captions?" defaultOpen="false">
    If the captions are not working, you're probably using a video input and our algorithm got the transcript wrong - just click "edit text" on the right segment, change the incorrect words, save, then re-generate captions.
  </Accordion>

  <Accordion title="Do captions work in any language?" defaultOpen="false">
    Yes, captions work in any language
  </Accordion>
</AccordionGroup>
