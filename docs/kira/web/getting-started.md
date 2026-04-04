# Source: https://github.com/tesselode/kira

# Kira - Rust Game Audio Engine

## Quick Start

Kira is a backend-agnostic library for expressive game audio in Rust. It provides:

- Tweens for smoothly adjusting sound properties
- A flexible mixer with audio effects (filters, reverb, delay, compression, EQ)
- A clock system for precisely timing audio events
- Spatial audio support for 3D sound positioning

## Installation

Add to `Cargo.toml`:

```toml
[dependencies]
kira = "0.11"
```

## Basic Usage

```rust
use kira::{
    AudioManager, AudioManagerSettings, DefaultBackend,
    sound::static_sound::StaticSoundData,
};

// Create audio manager
let mut manager = AudioManager::<DefaultBackend>::new(
    AudioManagerSettings::default()
)?;

// Load and play a sound
let sound_data = StaticSoundData::from_file("sound.ogg")?;
manager.play(sound_data)?;
```

## Key Features

### Audio Effects
- Low-pass/High-pass/Band-pass Filters
- Reverb/Echo
- Delay
- Compressor
- Distortion
- Parametric Equalizer (EQ)
- Stereo Panning
- Volume Control

### Sound Management
- Static sound playback (fully loaded in memory)
- Streaming sound playback (from files or sources)
- Seamless looping
- Playback rate control
- Volume and panning control

### Timing & Synchronization
- Clock system for beat-synced playback
- Precise timing for audio events
- Musical tempo support

### Spatial Audio
- 3D listener positioning
- Spatial sound source positioning
- Distance-based attenuation

## Platform Support

### Desktop
- Windows (primary)
- macOS (tested)
- Linux (tested)

### WebAssembly
- Limited support
- No file-based static sounds
- No streaming sounds

## Supported Audio Formats

- WAV
- OGG Vorbis
- FLAC
- MP3

## Integration with Game Engines

### Bevy
Use `bevy_kira_audio` plugin for Bevy integration:

```toml
bevy_kira_audio = "0.20"
```

## Architecture

Kira uses a separate audio thread that communicates with the main game thread via command channels. This design:

- Prevents audio glitches from gameplay stutters
- Allows real-time audio parameter adjustments
- Provides thread-safe operations

## Resources

- **Crates.io:** https://crates.io/crates/kira/
- **Docs.rs:** https://docs.rs/kira/latest/kira/
- **GitHub:** https://github.com/tesselode/kira
- **Examples:** https://github.com/tesselode/kira-examples

## License

Dual-licensed under Apache License 2.0 or MIT license.
