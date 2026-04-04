# Amphion: Audio, Music, and Speech Generation Toolkit

**Source:** https://github.com/open-mmlab/Amphion

## Overview

Amphion (/æmˈfaɪən/) is an open-source deep learning toolkit for audio, music, and speech generation research and development. It is designed to support reproducible research and help junior researchers and engineers get started in the field of audio, music, and speech generation. The toolkit offers unique visualizations of classic models and architectures, providing invaluable educational resources for understanding neural audio processing.

## Purpose

The North-Star objective of Amphion is to offer a platform for studying the conversion of any inputs into audio. It is designed to support multiple individual generation tasks with a unified framework and pipeline.

## Supported Tasks

Amphion provides comprehensive support for the following audio generation tasks:

- **TTS (Text-to-Speech)** - Supported
  - Convert text to natural-sounding speech
  - Multiple supported architectures with state-of-the-art performance

- **SVC (Singing Voice Conversion)** - Supported
  - Convert singing voice from one speaker/style to another
  - Multiple acoustic decoder implementations

- **VC (Voice Conversion)** - Supported
  - Zero-shot and few-shot voice conversion
  - Controllable timbre and style conversion

- **AC (Accent Conversion)** - Supported
  - Convert accents in speech while preserving content
  - Zero-shot capability for style conversion

- **TTA (Text-to-Audio)** - Supported
  - Generate audio from textual descriptions
  - Latent diffusion model architecture

- **SVS (Singing Voice Synthesis)** - In Development
  - Convert text directly to singing voice

- **TTM (Text-to-Music)** - In Development
  - Generate music from textual descriptions

## Key Features

### TTS: Text-to-Speech

Amphion achieves state-of-the-art performance on TTS systems with multiple supported architectures:

- **FastSpeech2**: Non-autoregressive architecture using feed-forward Transformer blocks
- **VITS**: End-to-end architecture with conditional VAE and adversarial learning
- **VALL-E**: Zero-shot TTS using neural codec language model with discrete codes
- **NaturalSpeech2**: Architecture using latent diffusion models for natural-sounding voices
- **Jets**: End-to-end model jointly training FastSpeech2 and HiFi-GAN with alignment
- **MaskGCT**: Fully non-autoregressive architecture eliminating explicit alignment requirements
- **Vevo-TTS**: Zero-shot TTS with controllable timbre and style

### Voice Conversion & Imitation

- **Vevo**: Zero-shot voice imitation framework with controllable timbre and style
  - Vevo-Timbre: Style-preserved voice conversion
  - Vevo-Voice: Style-converted voice conversion

- **FACodec**: Decomposes speech into subspaces for content, prosody, and timbre
  - Achieves zero-shot voice conversion

- **Noro**: Noise-robust zero-shot voice conversion system
  - Handles noisy reference speeches
  - Dual-branch reference encoding

### Singing Voice Conversion

Amphion implements multiple speaker-agnostic feature representations:

- **Content Features**: From WeNet, Whisper, and ContentVec pretrained models
- **Prosody Features**: F0 and energy extraction
- **Acoustic Decoders**:
  - Diffusion-based: DiffWaveNetSVC, DiffComoSVC (Consistency Model)
  - Transformer-based: TransformerSVC (encoder-only, non-autoregressive)
  - VAE/Flow-based: VitsSVC (VITS-like architecture)

### Text-to-Audio Generation

- Latent diffusion model architecture
- Two-stage training: VAE (AutoencoderKL) and conditional diffusion (AudioLDM)
- Similar to AudioLDM, Make-an-Audio, and AUDIT frameworks

### Neural Audio Codecs

- **DualCodec**: Low-frame-rate (12.5Hz or 25Hz) codec with SSL features
- **FACodec**: Speech decomposition for content, prosody, and timbre

### Vocoders

Amphion supports multiple neural vocoder architectures:

- **GAN-based**: MelGAN, HiFi-GAN, NSF-HiFiGAN, BigVGAN, APNet
- **Flow-based**: WaveGlow
- **Diffusion-based**: Diffwave
- **Auto-regressive**: WaveNet, WaveRNN
- **Multi-Scale Constant-Q Transform Discriminator**: Enhancement for GAN vocoders (ICASSP 2024)

### Evaluation Metrics

Comprehensive objective evaluation capabilities:

- **F0 Modeling**: F0 Pearson Coefficients, Periodicity RMSE, Voiced/Unvoiced F1 Score
- **Energy Modeling**: Energy RMSE, Energy Pearson Coefficients
- **Intelligibility**: Character/Word Error Rate (via Whisper)
- **Spectrogram Distortion**: FAD, MCD, Multi-Resolution STFT Distance, PESQ, STOI
- **Speaker Similarity**: Cosine similarity (RawNet3, Resemblyzer, WeSpeaker, WavLM)

### Datasets

Amphion provides unified data preprocessing for open-source datasets:

- AudioCaps, LibriTTS, LJSpeech, M4Singer, Opencpop, OpenSinger, SVCC, VCTK
- **Emilia Dataset**: Exclusive support for in-the-wild speech data
  - 101k+ hours of multilingual speech data
  - Latest Emilia-Large: 200,000+ hours (Emilia + Emilia-YODAS)
- **Emilia-Pipe**: Preprocessing pipeline for in-the-wild speech data

### Visualization Tools

- **SingVisio**: Interactive visualization tool for diffusion models in singing voice conversion
  - Educational resource for understanding model internals
  - Facilitates understandable research

## Latest Releases

### Amphion v0.2 (January 2025)
- Comprehensive technical report covering 2024 updates
- Emilia-Large dataset (200k+ hours)
- Enhanced multilingual support
- Multiple new model releases

### Recent Model Releases
- **DualCodec** (May 2025): Low-frame-rate neural audio codec
- **Vevo1.5** (April 2025): Unified speech and singing voice generation
- **Metis** (February 2025): Foundation model for unified speech generation
- **MaskGCT** (October 2024): State-of-the-art non-autoregressive TTS
- **Vevo** (December 2024): Zero-shot voice imitation framework

## Pre-trained Models

Amphion provides pre-trained models available on:
- HuggingFace: https://huggingface.co/amphion
- ModelScope: https://modelscope.cn/organization/amphion
- OpenXLab: https://openxlab.org.cn/usercenter/Amphion

All models are released under the MIT License for both research and commercial use.

## Community & Resources

- **GitHub**: https://github.com/open-mmlab/Amphion
- **Discord**: Join the community at https://discord.com/invite/drhW7ajqAG
- **Paper**: https://arxiv.org/abs/2312.09911
- **Website**: https://amphion.dev
- **HuggingFace Demos**: Interactive demos available for multiple models

## License

Amphion is released under the MIT License, allowing free use for both research and commercial applications.
