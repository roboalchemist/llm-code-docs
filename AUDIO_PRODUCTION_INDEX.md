# Audio Production Developer Tools - Quick Index

This index provides quick access to developer-focused audio production tools organized by use case and development domain.

---

## Quick Links by Category

### Plugin Development (VST/AU/AAX)
- **[JUCE](https://juce.com/)** - Most popular C++ plugin framework
  - Cross-platform (Windows, macOS, Linux)
  - Supports VST3, VST2, AU, AUv3, AAX, LV2
  - Includes DSP, GUI, and parameter management

- **[iPlug2](https://github.com/iPlug2/iPlug2)** - Alternative to JUCE
  - Simpler learning curve
  - Free and open-source (BSD license)

- **[VST SDK (Steinberg)](https://www.steinberg.net/developers/)** - Official plugin SDK
  - Usually abstracted through JUCE/iPlug2
  - Industry standard

### Audio File I/O & Manipulation
- **[ffmpeg](https://ffmpeg.org/)** - Universal format converter
  - Supports 100+ audio/video formats
  - Command-line and library (libav)

- **[SoX](http://sox.sourceforge.net/)** - Audio Swiss Army knife
  - Format conversion, effects, editing
  - CLI and library

- **[libsndfile](http://www.mega-nerd.com/libsndfile/)** - Audio file library
  - C library for WAV, FLAC, AU files
  - Low-level format support

### Real-Time Audio I/O
- **[PortAudio](http://www.portaudio.com/)** - Cross-platform audio I/O
  - Low-latency real-time audio
  - Used in standalone applications

- **[GStreamer](https://gstreamer.freedesktop.org/)** - Media processing pipelines
  - Complex audio routing and processing

### Music & Audio Analysis
- **[Librosa](https://librosa.org/)** - Python audio analysis
  - Feature extraction (MFCCs, spectral features)
  - Spectrograms, beat tracking, pitch detection
  - Industry standard for Python

- **[Essentia](https://essentia.upf.edu/)** - Music information retrieval
  - C++ with Python bindings
  - Music tagging, key detection, analysis

- **[Aubio](https://aubio.org/)** - Beat and pitch detection
  - C library with Python bindings
  - Real-time onset detection

### Web Audio
- **[Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)** - Browser standard
  - Synthesis, effects, analysis
  - AudioContext, OscillatorNode, FilterNode, etc.

- **[Tone.js](https://tonejs.org/)** - Web synthesis framework
  - High-level synthesis and sequencing
  - MIDI support, parameter automation

- **[Howler.js](https://howlerjs.com/)** - Web audio playback
  - Lightweight (7KB) playback library
  - Audio sprites, cross-browser support

### Audio Visualization
- **[Three.js](https://threejs.org/)** - 3D graphics
  - WebGL-powered 3D visualizations
  - Audio-reactive particles and effects

- **[p5.js](https://p5js.org/)** - 2D creative coding
  - Beginner-friendly canvas drawing
  - p5.sound library for audio integration

- **[Babylon.js](https://www.babylonjs.com/)** - 3D engine
  - Immersive audio-reactive environments
  - Full scene graph and physics

- **[Matplotlib](https://matplotlib.org/)** (Python) - Static analysis plots
  - Spectrograms, waveforms, frequency plots

- **[Plotly](https://plotly.com/)** (Python) - Interactive charts
  - Web-based audio visualizations

### Audio Programming Languages
- **[SuperCollider](https://github.com/supercollider/supercollider)** - Live coding
  - Text-based synthesis, client-server model
  - ProxySpace for live performance
  - Vast library of unit generators (UGens)

- **[Pure Data (Pd)](https://github.com/pure-data/pure-data)** - Visual patching
  - Free and open-source
  - Large plugin ecosystem
  - Good for learning DSP concepts

- **[Csound](https://csound.com/)** - Synthesis and rendering
  - FFT processing, granular synthesis
  - Score-based composition
  - Offline and real-time modes

- **[ChucK](https://github.com/ccrma/chuck)** - Time-controllable audio
  - Explicit timing control
  - Concurrent on-the-fly synthesis

### Digital Audio Workstations (DAWs)
**Professional/Commercial:**
- **[Reaper](https://www.reaper.fm/)** - Most developer-friendly DAW
  - ReaScript (EEL2, Lua, Python)
  - Lightweight and highly customizable

- **[FL Studio](https://www.image-line.com/)** - Pattern-based production
  - Python scripting API
  - Excellent for beat-making

- **[Ableton Live](https://www.ableton.com/)** - Live performance
  - Max for Live (Python API)
  - Session View for modular composition

- **[Logic Pro](https://www.apple.com/logic-pro/)** - macOS exclusive
  - AppleScript support
  - Extensive stock sounds

**Open-Source:**
- **[Ardour](https://ardour.org/)** - Full-featured DAW
  - VST, AU, CLAP, LV2 plugin support
  - Cross-platform (Linux, macOS, Windows)

- **[LMMS](https://github.com/LMMS/lmms)** - Linux-friendly DAW
  - Multi-track music production
  - Virtual instruments

### Audio Editors
- **[Audacity](https://www.audacityteam.org/)** - Free waveform editor
  - Multi-track recording and editing
  - Wide format support
  - Open-source (GPL)

### Audio Codecs & Libraries
- **[FLAC](https://xiph.org/flac/)** - Lossless codec
  - 30-60% compression, up to 32-bit/192kHz
  - Royalty-free and open-source

- **[libopus](https://opus-codec.org/)** - Modern lossy codec
  - Superior compression to AAC/MP3
  - Streaming and real-time applications

- **[libvorbis](https://xiph.org/vorbis/)** - Patent-free lossy codec
  - Used in OGG containers
  - Gaming and Linux-friendly

- **[libfdk-aac](https://sourceforge.net/projects/opencore-amr/)** - AAC encoder
  - Apple ecosystem and streaming

- **[LAME](https://lame.sourceforge.io/)** - MP3 encoder
  - High-quality MP3 encoding

### Music Identification & Metadata
- **[chromaprint](https://github.com/acoustid/chromaprint)** - Audio fingerprinting
  - Music identification without metadata
  - AcoustID service integration

- **[MusicBrainz API](https://musicbrainz.org/doc/MusicBrainz_API)** - Metadata lookup
  - Artist, album, track information
  - REST API

### Command-Line Tools
- **[ffmpeg](https://ffmpeg.org/)** - Encoding and format conversion
- **[SoX](http://sox.sourceforge.net/)** - Audio editing and effects
- **[MediaInfo](https://mediaarea.net/MediaInfo)** - File analysis
- **[mpv](https://mpv.io/)** - Media player with scripting
- **[liquidsoap](https://www.liquidsoap.info/)** - Audio streaming automation

### Education & Learning
- **[Sonic Pi](https://sonic-pi.net/)** - Music education platform
  - Ruby-based live coding
  - Beginner-friendly

- **[EarSketch](https://earsketch.gatech.edu/)** - Web-based music programming
  - Browser-based education tool
  - JavaScript-based composition

---

## Tools by Developer Skill Level

### Beginner-Friendly
1. **p5.js** - Creative coding with audio
2. **Sonic Pi** - Music education
3. **Web Audio API** - Browser audio basics
4. **Audacity** - Visual waveform editing
5. **Pure Data** - Visual patching basics

### Intermediate
1. **JUCE** - Plugin development
2. **Librosa** - Audio analysis in Python
3. **Tone.js** - Web synthesis
4. **Three.js** - 3D visualization
5. **SuperCollider** - Live coding

### Advanced
1. **VST SDK** - Low-level plugin details
2. **Csound** - Advanced synthesis
3. **ChucK** - Time-domain audio programming
4. **iPlug2** - Custom plugin architecture
5. **STK** - Algorithmic synthesis design

---

## Tools by Development Language

### C++
- JUCE, iPlug2, FFmpeg (libav), Audacity, Ardour, Csound, SuperCollider, Three.js (via Node), libflac, libopus, libvorbis, libsndfile

### C
- FFmpeg, SoX, PortAudio, libsndfile, libflac, libopus, libvorbis, LAME, GStreamer, cmus

### Python
- Librosa, Essentia, pydub, SoundFile, sounddevice, Plotly, Matplotlib, AudioKit, Reaper (ReaScript)

### JavaScript/TypeScript
- Web Audio API, Tone.js, Howler.js, Three.js, p5.js, Babylon.js, audioMotion, ProjectM

### Swift
- AudioKit (iOS/macOS)

### Lua/OCaml
- ReaScript (EEL2/Lua), liquidsoap

### Domain-Specific Languages
- SuperCollider, Csound, ChucK, Pure Data, Max/MSP

---

## Tools by Primary Use Case

### Building Audio Applications
1. JUCE (plugins)
2. PortAudio (I/O)
3. Librosa (analysis)
4. Tone.js (web synthesis)

### Format Conversion & Processing
1. ffmpeg (all formats)
2. SoX (effects + conversion)
3. libav (library interface)

### Music Analysis & Research
1. Librosa (Python standard)
2. Essentia (comprehensive MIR)
3. chromaprint (fingerprinting)
4. MusicBrainz (metadata)

### Real-Time Synthesis
1. SuperCollider (flexible)
2. Pure Data (visual)
3. ChucK (timing control)
4. Csound (offline/real-time)

### Live Performance
1. Reaper (DAW + scripting)
2. Ableton Live (live clips)
3. SuperCollider (live coding)

### Music Education
1. Sonic Pi (beginner)
2. EarSketch (web-based)
3. Pure Data (visual learning)

### Web Audio Applications
1. Web Audio API (standard)
2. Tone.js (high-level)
3. Howler.js (playback)
4. p5.js (creative)

### Visualization
1. Three.js (3D)
2. p5.js (2D)
3. Babylon.js (immersive)
4. Matplotlib (analysis)

---

## Documentation Priority for LLM-Code-Docs

### Tier 1 (Highest Priority)
- JUCE
- FFmpeg
- Web Audio API
- Librosa
- SuperCollider

### Tier 2 (High Priority)
- Pure Data
- SoX
- Reaper
- Audacity
- PortAudio
- Essentia

### Tier 3 (Medium Priority)
- iPlug2
- Three.js
- p5.js
- Tone.js
- Csound
- ChucK

### Tier 4 (Niche/Specialized)
- STK
- AudioKit
- liquidsoap
- Cecilia
- chromaprint

---

## Related Research Topics

1. **Digital Signal Processing (DSP)**
   - Filter design, convolution, spectral analysis
   - Tools: Csound, SuperCollider, STK

2. **Music Information Retrieval (MIR)**
   - Feature extraction, beat tracking, genre classification
   - Tools: Librosa, Essentia, Aubio

3. **Real-Time Audio Processing**
   - Low-latency architecture, buffer management
   - Tools: JUCE, PortAudio, SuperCollider

4. **Audio Codec Design**
   - Lossy/lossless compression, bitrate optimization
   - Codecs: FLAC, Opus, Vorbis, AAC

5. **MIDI and Sequencing**
   - Note events, controller data, timing
   - Integrated in DAWs: Reaper, FL Studio, Ableton

6. **Spatial Audio (3D Audio)**
   - Ambisonics, binaural, HRTF
   - Tools: Web Audio API, Babylon.js

7. **Speech Processing**
   - Voice synthesis, recognition, modification
   - Related to audio analysis tools

---

## File Structure for LLM-Code-Docs

Recommended organization:
```
docs/llms-txt/
├── juce/
├── ffmpeg/
├── librosa/
├── web-audio-api/
├── supercollider/
├── pure-data/
├── sox/
├── reaper/
├── audacity/
├── portaudio/
├── essentia/
├── tone.js/
├── three.js/
├── p5.js/
└── ... (additional tools)
```

---

**Last Updated:** December 31, 2025
**Maintained By:** Research Team
**Status:** Active - Regular updates recommended
