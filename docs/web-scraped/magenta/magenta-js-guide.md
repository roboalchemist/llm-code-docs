# Magenta.js Guide

**Source:** https://magenta.tensorflow.org/js-announce

Magenta.js is a JavaScript library suite for generating music and art with Magenta models. Built on TensorFlow.js, it runs directly in the browser with WebGL acceleration.

## Overview

Magenta.js provides a simple API for:
- Music generation with pre-trained models
- Image and drawing generation
- Real-time synthesis
- Interactive music creation
- Browser-based creative applications

## Installation

### Via npm

```bash
npm install @magenta/music @magenta/image
```

### Via CDN (Browser)

```html
<script src="https://cdn.jsdelivr.net/npm/@magenta/music@1.4.0/dist/magenta.js"></script>
```

## Core Modules

### @magenta/music

The main music generation library including:

- MusicVAE
- MelodyRNN
- DrumsRNN
- ImprovRNN
- PerformanceRNN
- MusicRNN (base class)
- Utility functions

### @magenta/image

For generative images:

- Sketch-RNN
- PGAN (Progressive GAN)
- Other image models

## Basic Concepts

### Model Loading

Models are loaded from checkpoints (weights and configuration files):

```javascript
const checkpoint = 'https://storage.googleapis.com/magenta-js/checkpoints/music_vae/...';
const model = new mm.MusicVAE(checkpoint);
await model.initialize();
```

### Note Sequences

Music is represented as note sequences - arrays of note events:

```javascript
{
  notes: [
    {
      pitch: 60,           // MIDI note number
      startTime: 0,        // In quarter notes
      endTime: 1,
      velocity: 100        // 0-127, optional
    },
    // ... more notes
  ],
  totalQuantizedSteps: 16,
  quantizationInfo: {
    stepsPerQuarter: 4
  }
}
```

### MIDI Conversion

Convert between sequences and MIDI:

```javascript
// Sequence to MIDI
const midiData = mm.sequenceProtoToMidi(noteSequence);

// Download MIDI
const link = document.createElement('a');
link.href = URL.createObjectURL(new Blob([midiData], {type: 'audio/midi'}));
link.download = 'generated.mid';
link.click();

// Load MIDI
const file = document.getElementById('midi-input').files[0];
const arrayBuffer = await file.arrayBuffer();
const sequence = mm.midiToSequenceProto(arrayBuffer);
```

## MusicVAE

Variational Autoencoder for music generation.

### Basic Generation

```javascript
const checkpoint = 'https://storage.googleapis.com/magenta-js/checkpoints/music_vae/mel_2bar_big';
const model = new mm.MusicVAE(checkpoint);
await model.initialize();

// Generate single sequence
const samples = await model.sample(1);
const sequence = samples[0];
```

### Interpolation

```javascript
// Encode two melodies
const melody1 = mm.midiToSequenceProto(midi1);
const melody2 = mm.midiToSequenceProto(midi2);

const z1 = await model.encode([melody1]);
const z2 = await model.encode([melody2]);

// Interpolate between them
const numSteps = 10;
const interpolated = [];

for (let i = 0; i < numSteps; i++) {
  const t = i / (numSteps - 1);

  // Linear interpolation in latent space
  const z = [];
  for (let j = 0; j < z1[0].length; j++) {
    z[j] = z1[0][j] * (1 - t) + z2[0][j] * t;
  }

  const decoded = await model.decode([z]);
  interpolated.push(decoded[0]);
}
```

### Available Checkpoints

Music VAE has multiple checkpoints for different:
- **Duration** - 2-bar, 4-bar, 16-bar
- **Content** - Melodies, drums, multitrack
- **Style** - Genre-specific models
- **Size** - Smaller/larger variants for speed/quality tradeoff

```javascript
// Melody VAE (2-bar)
'https://storage.googleapis.com/magenta-js/checkpoints/music_vae/mel_2bar_big'

// Drums VAE
'https://storage.googleapis.com/magenta-js/checkpoints/music_vae/drums_2bar_small'

// Multitrack VAE
'https://storage.googleapis.com/magenta-js/checkpoints/music_vae/multitrack'
```

## MelodyRNN

Recurrent neural network for melody generation.

### Configuration

```javascript
// Attention RNN config
const config = {
  type: 'attn',
  temperature: 1.2
};

// Generate melody conditioned on primer
const primer = mm.midiToSequenceProto(primerMidi);
const generated = await mm.generate(
  config,
  mm.rnnEncoder,
  primer,
  32  // length
);
```

### Temperature Control

```javascript
// Conservative generation (higher note probability)
const conservative = await model.continueSequence(
  primer,
  32,
  0.5  // low temperature
);

// Creative generation (more random)
const creative = await model.continueSequence(
  primer,
  32,
  1.5  // high temperature
);
```

## DrumsRNN

Drum pattern generation.

### Basic Usage

```javascript
const config = {
  type: 'drums',
  temperature: 1.0
};

// Generate drums
const drums = await mm.generate(
  config,
  mm.rnnEncoder,
  null,  // no primer
  16     // 16 steps (1 bar)
);
```

### Constrain with Backing Track

```javascript
const backingTrack = mm.midiToSequenceProto(backingMidi);

// Generate drums that fit with backing track
const drums = await mm.conditionedGenerate(
  config,
  mm.rnnEncoder,
  backingTrack,
  16
);
```

## Sketch-RNN

For drawing and image generation.

### Loading Model

```javascript
const checkpoint = 'https://storage.googleapis.com/magenta-js/checkpoints/sketch_rnn/cat';
const model = new mm.SketchRNN(checkpoint);
await model.initialize();
```

### Generating Sketches

```javascript
// Generate random sketch
const sketch = await model.sample();

// Sketch is array of points:
// [{x, y, penDown}, ...]
```

## Audio Playback

### Using Tone.js

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/tone/14.8.49/Tone.js"></script>
```

```javascript
const synth = new Tone.Synth({
  oscillator: { type: 'square' },
  envelope: {
    attack: 0.005,
    decay: 0.1,
    sustain: 0.3,
    release: 0.1
  }
}).toDestination();

// Play sequence
const sequence = samples[0];
let currentTime = 0;

sequence.notes.forEach(note => {
  const noteStr = Tone.Frequency(note.pitch, 'midi').toNote();
  const duration = note.endTime - note.startTime;

  synth.triggerAttackRelease(
    noteStr,
    duration + 's',
    '+' + note.startTime + 'm'
  );
});

await Tone.start();
```

### MIDI Output

Use Web MIDI API to send to hardware:

```javascript
// Request MIDI access
const midiAccess = await navigator.requestMIDIAccess();
const outputs = Array.from(midiAccess.outputs.values());

// Send notes
const output = outputs[0];
const noteOnMsg = [0x90, 60, 100];  // Note on, pitch 60, velocity 100
output.send(noteOnMsg, performance.now());
```

## Building Interactive Applications

### Complete Music Creation App

```javascript
const mm = window.mm;

async function initializeApp() {
  // Load models
  const vae = new mm.MusicVAE(
    'https://storage.googleapis.com/magenta-js/checkpoints/music_vae/mel_2bar_big'
  );
  await vae.initialize();

  const drums = new mm.MusicVAE(
    'https://storage.googleapis.com/magenta-js/checkpoints/music_vae/drums_2bar_small'
  );
  await drums.initialize();

  // UI Elements
  document.getElementById('generate').addEventListener('click', async () => {
    // Generate melody
    const melodies = await vae.sample(1);
    const melody = melodies[0];

    // Generate drums
    const drumPatterns = await drums.sample(1);
    const drumPattern = drumPatterns[0];

    // Combine
    const combined = mm.sequences.concatenate([melody, drumPattern]);

    // Convert to MIDI and play
    const midiData = mm.sequenceProtoToMidi(combined);
    playSoundFromMidi(midiData);
  });

  document.getElementById('download').addEventListener('click', () => {
    const midiData = mm.sequenceProtoToMidi(lastSequence);
    downloadMidi(midiData, 'generated.mid');
  });
}

function playSoundFromMidi(midiData) {
  // Use Web Audio API or Tone.js
  // ...
}

function downloadMidi(data, filename) {
  const blob = new Blob([data], {type: 'audio/midi'});
  const link = document.createElement('a');
  link.href = URL.createObjectURL(blob);
  link.download = filename;
  link.click();
}

// Start when page loads
document.addEventListener('DOMContentLoaded', initializeApp);
```

## Utility Functions

### Sequence Manipulation

```javascript
// Combine sequences
const combined = mm.sequences.concatenate([seq1, seq2]);

// Shift pitch
const shifted = mm.sequences.shiftSequence(sequence, 5);  // Up 5 semitones

// Quantize
const quantized = mm.sequences.quantizeSequence(sequence, 4);

// Trim to length
const trimmed = mm.sequences.trimSequence(sequence, 0, 16);

// Clone
const clone = JSON.parse(JSON.stringify(sequence));
```

### Validation

```javascript
// Check if sequence is valid
if (!mm.sequences.isAbsoluteQuantizedSequence(sequence)) {
  console.log('Invalid sequence');
}

// Get sequence length
const length = mm.sequences.getSequenceLength(sequence);
```

## Performance Optimization

### Model Caching

```javascript
// Cache models for reuse
const modelCache = {};

async function getModel(checkpoint) {
  if (!modelCache[checkpoint]) {
    const model = new mm.MusicVAE(checkpoint);
    await model.initialize();
    modelCache[checkpoint] = model;
  }
  return modelCache[checkpoint];
}
```

### Batch Generation

```javascript
// Generate multiple samples efficiently
const vae = await getModel(checkpoint);
const samples = await vae.sample(10);  // Generate 10 at once
```

### Worker Threads

```javascript
// Use Web Workers for heavy computation
const worker = new Worker('magenta-worker.js');

worker.postMessage({
  command: 'generate',
  checkpoint: checkpointUrl,
  count: 5
});

worker.onmessage = (event) => {
  const sequences = event.data;
  // Process results
};
```

## Troubleshooting

### Model Loading Issues

```javascript
// Check if model loaded successfully
try {
  await model.initialize();
  console.log('Model loaded');
} catch (e) {
  console.error('Model loading failed:', e);
}
```

### Browser Compatibility

- Requires WebGL for GPU acceleration
- Falls back to CPU if WebGL unavailable
- Tested on Chrome, Firefox, Safari, Edge
- Mobile browsers supported (iOS Safari, Chrome Android)

### Memory Management

```javascript
// Dispose of models when done
model.dispose();

// Clear GPU memory
tf.disposeVariables();
```

## Examples and Demos

Official examples available at:
- **GitHub Repository** - https://github.com/magenta/magenta-js
- **Demo Gallery** - https://magenta.tensorflow.org/demos/web/
- **Interactive Examples** - Browser-based applications

## API Reference

### MusicVAE Methods

- `initialize()` - Load model weights
- `sample(numSamples)` - Generate random sequences
- `encode(sequences)` - Encode to latent space
- `decode(z)` - Decode from latent vectors
- `interpolate(sequences, steps)` - Interpolate between sequences

### MelodyRNN Methods

- `continueSequence(primer, length, temperature)` - Generate continuation
- `sample(length, temperature)` - Generate from scratch

### Utility Namespaces

- `mm.sequences` - Sequence manipulation
- `mm.performance` - Performance modeling
- `mm.chords` - Chord recognition and generation
- `mm.drums` - Drum-specific utilities

## Additional Resources

- **Official Documentation** - https://github.com/magenta/magenta-js
- **API Docs** - https://magenta.github.io/magenta-js/
- **GitHub Issues** - Report bugs and request features
- **Discussion Forum** - Community support and examples
