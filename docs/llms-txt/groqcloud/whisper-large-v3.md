# Source: https://console.groq.com/docs/model/whisper-large-v3

---
description: Model page for Whisper Large v3: OpenAI&#x27;s most advanced speech recognition model with exceptional accuracy across diverse audio conditions.
title: Whisper Large v3 - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

# Whisper

`whisper-large-v3`

[Try it in Playground](https://console.groq.com/playground?model=whisper-large-v3)

INPUT

Audio

OUTPUT

Text

CAPABILITIES

[Speech to Text](https://console.groq.com/docs/speech-to-text)

![OpenAI logo](https://console.groq.com/_next/image?url=%2Fopenai.webp&w=96&q=75)OpenAI

[Model card](https://huggingface.co/openai/whisper-large-v3)

Whisper Large v3 is OpenAI's most advanced and capable speech recognition model, delivering state-of-the-art accuracy across a wide range of audio conditions and languages. This flagship model excels at handling challenging audio scenarios including background noise, accents, and technical terminology. With its robust architecture and extensive training, it represents the gold standard for automatic speech recognition tasks requiring the highest possible accuracy.

---

### PRICING

Per Hour

$0.111

---

### LIMITS

MAX FILE SIZE

100 MB

---

### QUANTIZATION

This uses Groq's TruePoint Numerics, which reduces precision only in areas that don't affect accuracy, preserving quality while delivering significant speedup over traditional approaches. [Learn more here](https://groq.com/blog/inside-the-lpu-deconstructing-groq-speed).

### [Key Technical Specifications](#key-technical-specifications)

### Model Architecture

Built on OpenAI's transformer-based encoder-decoder architecture with 1550M parameters. The model uses a sophisticated attention mechanism optimized for speech recognition tasks, with specialized training on diverse multilingual audio data. The architecture includes advanced noise robustness and can handle various audio qualities and recording conditions.

### Performance Metrics

Whisper Large v3 sets the benchmark for speech recognition accuracy:

* Short-form transcription: 8.4% WER (industry-leading accuracy)
* Sequential long-form: 10.0% WER
* Chunked long-form: 11.0% WER
* Multilingual support: 99+ languages
* Model size: 1550M parameters

### [Key Model Details](#key-model-details)

* **Model Size**: 1550M parameters
* **Speed**: 189x speed factor
* **Audio Context**: Optimized for 30-second audio segments, with a minimum of 10 seconds per segment
* **Supported Audio**: FLAC, MP3, M4A, MPEG, MPGA, OGG, WAV, or WEBM
* **Language**: 99+ languages supported
* **Usage**: [Groq Speech to Text Documentation](https://console.groq.com/docs/speech-to-text)

### Use Cases

High-Accuracy Transcription

Perfect for applications where transcription accuracy is paramount:
* Legal and medical transcription requiring precision
* Academic research and interview transcription
* Professional content creation and journalism

Multilingual Applications

Ideal for global applications requiring broad language support:
* International conference and meeting transcription
* Multilingual content processing and analysis
* Global customer support and communication tools

Challenging Audio Conditions

Excellent for difficult audio scenarios:
* Noisy environments and poor audio quality
* Multiple speakers and overlapping speech
* Technical terminology and specialized vocabulary

### Best Practices

* Prioritize accuracy: Use this model when transcription precision is more important than speed
* Leverage multilingual capabilities: Take advantage of the model's extensive language support for global applications
* Handle challenging audio: Rely on this model for difficult audio conditions where other models might struggle
* Consider context length: For long-form audio, the model works optimally with 30-second segments
* Use appropriate algorithms: Choose sequential long-form for maximum accuracy, chunked for better speed