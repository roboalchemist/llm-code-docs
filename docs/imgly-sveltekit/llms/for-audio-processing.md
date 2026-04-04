# For Audio Processing

Export audio from pages, video blocks, audio blocks, and tracks to WAV or MP4 format for external processing, transcription, or analysis.

![Audio Export example showing audio export interface in CE.SDK](/docs/cesdk/_astro/browser.hero.C6YSnavl_WQpHH.webp)

8 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-export-audio-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-export-audio-browser)

The `exportAudio` API allows you to extract audio from any block that contains audio content. This is particularly useful when integrating with external audio processing services like speech-to-text transcription, audio enhancement, or music analysis platforms.

Audio can be exported from multiple block types:

*   **Page blocks** - Export the complete mixed audio timeline
*   **Video blocks** - Extract audio tracks from videos
*   **Audio blocks** - Export standalone audio content
*   **Track blocks** - Export audio from specific timeline tracks

## Export Audio[#](#export-audio)

Export audio from any block using the `exportAudio` API:

```
const page = cesdk.engine.scene.getCurrentPage();
const audioBlob = await cesdk.engine.block.exportAudio(page, {  mimeType: 'audio/wav',  sampleRate: 48000,  numberOfChannels: 2});
```

### Export Options[#](#export-options)

Configure your audio export with these options:

*   **`mimeType`** - `'audio/wav'` (uncompressed) or `'audio/mp4'` (compressed AAC)
*   **`sampleRate`** - Audio quality in Hz (default: 48000)
*   **`numberOfChannels`** - 1 for mono or 2 for stereo
*   **`timeOffset`** - Start time in seconds (default: 0)
*   **`duration`** - Length to export in seconds (0 = entire duration)
*   **`onProgress`** - Callback function receiving `(rendered, encoded, total)` for progress tracking

## Find Audio Sources[#](#find-audio-sources)

To find blocks with audio in your scene:

```
// Find audio blocksconst audioBlocks = cesdk.engine.block.findByType('audio');
// Find video blocks with audioconst videoFills = cesdk.engine.block.findByType('//ly.img.ubq/fill/video');const videosWithAudio = videoFills.filter(block => {  try {    return cesdk.engine.block.getAudioInfoFromVideo(block).length > 0;  } catch {    return false;  }});
```

## Working with Multi-Track Video Audio[#](#working-with-multi-track-video-audio)

Videos can contain multiple audio tracks (e.g., different languages). CE.SDK provides APIs to inspect and extract specific tracks.

### Check audio track count[#](#check-audio-track-count)

```
const videoFillId = cesdk.engine.block.findByType('//ly.img.ubq/fill/video')[0];
const trackCount = cesdk.engine.block.getAudioTrackCountFromVideo(videoFillId);console.log(`Video has ${trackCount} audio track(s)`);
```

### Get track information[#](#get-track-information)

```
const audioTracks = cesdk.engine.block.getAudioInfoFromVideo(videoFillId);
audioTracks.forEach((track, index) => {  console.log(`Track ${index}:`, {    channels: track.channels,      // 1=mono, 2=stereo    sampleRate: track.sampleRate,  // Sample rate in Hz    language: track.language,      // e.g., "en", "es"    label: track.label             // Track description  });});
```

### Extract a specific track[#](#extract-a-specific-track)

```
// Create audio block from track 0 (first track)const audioBlockId = cesdk.engine.block.createAudioFromVideo(videoFillId, 0);
// Export just this track's audioconst trackAudioBlob = await cesdk.engine.block.exportAudio(audioBlockId, {  mimeType: 'audio/wav'});
```

### Extract all tracks[#](#extract-all-tracks)

```
// Create audio blocks for all tracksconst audioBlockIds = cesdk.engine.block.createAudiosFromVideo(videoFillId);
// Export each trackfor (let i = 0; i < audioBlockIds.length; i++) {  const trackBlob = await cesdk.engine.block.exportAudio(audioBlockIds[i]);  console.log(`Track ${i}: ${trackBlob.size} bytes`);}
```

## Complete Workflow: Audio to Captions[#](#complete-workflow-audio-to-captions)

A common workflow is to export audio, send it to a transcription service, and use the returned captions in your scene.

### Step 1: Export Audio[#](#step-1-export-audio)

```
const page = cesdk.engine.scene.getCurrentPage();
const audioBlob = await cesdk.engine.block.exportAudio(page, {  mimeType: 'audio/wav',  sampleRate: 48000,  numberOfChannels: 2});
```

### Step 2: Send to Transcription Service[#](#step-2-send-to-transcription-service)

Send the audio to a service that returns SubRip (SRT) format captions:

```
async function transcribeAudio(audioBlob) {  const formData = new FormData();  formData.append('audio', audioBlob, 'audio.wav');  formData.append('format', 'srt');
  const response = await fetch('https://api.transcription-service.com/transcribe', {    method: 'POST',    headers: {      'Authorization': 'Bearer YOUR_API_KEY'    },    body: formData  });
  // Returns SRT format text  return await response.text();}
const srtContent = await transcribeAudio(audioBlob);
```

### Step 3: Import Captions from SRT[#](#step-3-import-captions-from-srt)

Use the built-in API to create caption blocks from the SRT response:

```
// Create a file from the SRT textconst srtFile = new File([srtContent], 'captions.srt', {  type: 'application/x-subrip'});
// Create object URL and import captionsconst uri = URL.createObjectURL(srtFile);const captions = await cesdk.engine.block.createCaptionsFromURI(uri);URL.revokeObjectURL(uri);
// Add captions to pageconst page = cesdk.engine.scene.getCurrentPage();const captionTrack = cesdk.engine.block.create('//ly.img.ubq/captionTrack');
captions.forEach(caption => {  cesdk.engine.block.appendChild(captionTrack, caption);});
cesdk.engine.block.appendChild(page, captionTrack);
// Center the first caption as a reference pointcesdk.engine.block.alignHorizontally([captions[0]], 'Center');cesdk.engine.block.alignVertically([captions[0]], 'Center');
```

### Other Processing Services[#](#other-processing-services)

Audio export also supports these workflows:

*   **Audio enhancement** - Noise removal, normalization
*   **Music analysis** - Tempo, key, beat detection
*   **Language detection** - Identify spoken language
*   **Speaker diarization** - Identify who spoke when

## Next Steps[#](#next-steps)

Now that you understand audio export, explore related audio and video features:

*   [Add Captions](sveltekit/edit-video/add-captions-f67565/) - Learn how to create and sync caption blocks with audio content
*   [Control Audio and Video](sveltekit/create-video/control-daba54/) - Master time offset, duration, and playback controls for audio blocks
*   [Trim Video Clips](sveltekit/edit-video/trim-4f688b/) - Apply the same trim concepts to isolate audio segments

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/variables/mimetype)