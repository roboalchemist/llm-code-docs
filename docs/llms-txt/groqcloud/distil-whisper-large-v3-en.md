# Source: https://console.groq.com/docs/model/distil-whisper-large-v3-en

---
description: Model page for Distil-Whisper Large v3: High-performance speech recognition model that&#x27;s 6.3x faster than Whisper Large v3 with comparable accuracy.
title: Distil-Whisper Large v3 - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

Loading model information...

### [Key Technical Specifications](#key-technical-specifications)

### Model Architecture

Built on the encoder-decoder transformer architecture inherited from Whisper, with optimized decoder layers for enhanced inference speed. The model uses knowledge distillation from Whisper Large v3, reducing decoder layers while maintaining the full encoder. This architecture enables the model to process audio 6.3x faster than the original while preserving transcription quality.

### Performance Metrics

Distil-Whisper Large v3 delivers exceptional performance across different transcription scenarios:

* Short-form transcription: 9.7% WER (vs 8.4% for Large v3)
* Sequential long-form: 10.8% WER (vs 10.0% for Large v3)
* Chunked long-form: 10.9% WER (vs 11.0% for Large v3)
* Speed improvement: 6.3x faster than Whisper Large v3
* Model size: 756M parameters (vs 1550M for Large v3)

### [Key Model Details](#key-model-details)

* **Model Size**: 756M parameters
* **Speed**: 250x speed factor
* **Audio Context**: Optimized for 30-second audio segments, with a minimum of 10 seconds per segment
* **Supported Audio**: FLAC, MP3, M4A, MPEG, MPGA, OGG, WAV, or WEBM
* **Language**: English only
* **Usage**: [Groq Speech to Text Documentation](https://console.groq.com/docs/speech-to-text)

### Use Cases

Real-Time Transcription

Perfect for applications requiring immediate speech-to-text conversion:
* Live meeting transcription and note-taking
* Real-time subtitling for broadcasts and streaming
* Voice-controlled applications and interfaces

Content Processing

Ideal for processing large volumes of audio content:
* Podcast and video transcription at scale
* Audio content indexing and search
* Automated captioning for accessibility

Interactive Applications

Excellent for user-facing speech recognition features:
* Voice assistants and chatbots
* Dictation and voice input systems
* Language learning and pronunciation tools

### Best Practices

* Optimize audio quality: Use clear, high-quality audio (16kHz sampling rate recommended) for best transcription accuracy
* Choose appropriate algorithm: Use sequential long-form for accuracy-critical applications, chunked for speed-critical single files
* Leverage batching: Process multiple audio files together to maximize throughput efficiency
* Consider context length: For long-form audio, the model works optimally with 30-second segments
* Use timestamps: Enable timestamp output for applications requiring precise timing information