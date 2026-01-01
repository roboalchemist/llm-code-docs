# Source: https://docs.rs/kira/latest/kira/

# Kira API Reference

## Overview

Kira is a backend-agnostic library to create expressive audio for games. It provides:

- **Tweens** for smoothly adjusting properties of sounds
- **Flexible mixer** for applying effects to audio
- **Clock system** for precisely timing audio events
- **Spatial audio** support for 3D sound positioning

## Core Modules

### backend
Communication between Kira and a low-level audio API. Handles different audio backends (CPAL, etc.).

### manager
The `AudioManager` is the main entry point for Kira. It manages:
- Playing sounds
- Creating and managing mixer tracks
- Creating and managing clocks
- Managing audio resources

**Key Type:** `AudioManager<B: Backend>`

### sound
Defines sound data and playback types:
- `StaticSoundData` - Audio loaded entirely in memory
- `StreamingSoundData` - Audio streamed from disk or other sources

### track
Mixer tracks for organizing and applying effects to audio:
- `TrackBuilder` - Builder for creating tracks
- `Track` - Handle to a mixer track
- Effects: Filter, Reverb, Delay, Compressor, Distortion, EQ, etc.

### effect
Audio effects that can be applied to tracks:
- `FilterEffect` - Low-pass, high-pass, band-pass filters
- `ReverbEffect` - Reverb/echo effects
- `DelayEffect` - Delay line effect
- `CompressorEffect` - Dynamic range compression
- `DistortionEffect` - Distortion effect
- `EQEffect` - Parametric equalizer
- `PanningControl` - Stereo panning
- `VolumeControl` - Volume control

### clock
Precise timing system for synchronizing audio events:
- `Clock` - Timing source for scheduling audio events
- `ClockSpeed` - How fast the clock ticks (e.g., TicksPerMinute)

### modulator
Modulators for dynamically adjusting audio parameters:
- `Modulator` trait for custom implementations
- Built-in modulators for common use cases

### parameter
Parameter types for controlling sound and effect properties:
- `Tweens` for smooth parameter transitions
- `Ramp` for linear transitions

### listener
Types for spatial audio listeners:
- `Listener` - Position and orientation in 3D space
- Defines the perspective for spatial audio calculations

### command
Helpers for sending commands from the gameplay thread to the audio thread.

## Main Types

### AudioManager

```rust
use kira::{AudioManager, AudioManagerSettings, DefaultBackend};

let mut manager = AudioManager::<DefaultBackend>::new(
    AudioManagerSettings::default()
)?;
```

Methods:
- `play(sound_data)` - Play a sound immediately
- `add_sub_track(builder)` - Create a mixer sub-track
- `add_clock(speed)` - Create a new clock
- `listener()` - Get/set spatial audio listener

### StaticSoundData

```rust
use kira::sound::static_sound::StaticSoundData;

let sound_data = StaticSoundData::from_file("sound.ogg")?;
let sound = manager.play(sound_data)?;
```

Properties:
- `volume` - Initial volume in decibels
- `playback_rate` - Speed of playback
- `panning` - Stereo panning
- `loop_region` - Looping configuration
- `output_destination` - Which track to play on

### StreamingSoundData

For streaming audio from files or other sources:

```rust
use kira::sound::streaming::StreamingSoundData;

let sound_data = StreamingSoundData::from_file("music.ogg")?;
```

### Tween

Smooth transitions for parameter changes:

```rust
use kira::Tween;
use std::time::Duration;

sound.set_playback_rate(
    2.0,
    Tween {
        duration: Duration::from_secs(3),
        easing: kira::tween::Easing::Linear,
        ..Default::default()
    },
);
```

### Track

Mixer tracks for organizing and applying effects:

```rust
use kira::track::TrackBuilder;
use kira::track::effect::filter::FilterBuilder;

let track = manager.add_sub_track({
    let mut builder = TrackBuilder::new();
    builder.add_effect(FilterBuilder::new().cutoff(1000.0));
    builder
})?;
```

### Clock

For timing audio events with musical precision:

```rust
use kira::clock::ClockSpeed;

let mut clock = manager.add_clock(ClockSpeed::TicksPerMinute(120.0))?;
let sound_data = StaticSoundData::from_file("sound.ogg")?
    .start_time(clock.time() + 2);
clock.start()?;
```

## Common Patterns

### Playing a Sound

```rust
use kira::{
    AudioManager, AudioManagerSettings, DefaultBackend,
    sound::static_sound::StaticSoundData,
};

let mut manager = AudioManager::<DefaultBackend>::new(
    AudioManagerSettings::default()
)?;
let sound_data = StaticSoundData::from_file("sound.ogg")?;
manager.play(sound_data)?;
```

### Applying Effects to a Track

```rust
use kira::track::{TrackBuilder, effect::filter::FilterBuilder};

let track = manager.add_sub_track({
    let mut builder = TrackBuilder::new();
    builder.add_effect(FilterBuilder::new().cutoff(1000.0));
    builder
})?;

let sound_data = StaticSoundData::from_file("sound.ogg")?
    .output_destination(&track);
manager.play(sound_data)?;
```

### Beat-Synced Playback

```rust
use kira::clock::ClockSpeed;

let mut clock = manager.add_clock(ClockSpeed::TicksPerMinute(120.0))?;

// Play sound 2 beats from now
let sound_data = StaticSoundData::from_file("sound.ogg")?
    .start_time(clock.time() + 2);
manager.play(sound_data)?;

clock.start()?;
```

### Tweening Parameters

```rust
use std::time::Duration;
use kira::Tween;

let mut sound = manager.play(sound_data)?;

// Gradually change playback rate
sound.set_playback_rate(
    2.0,
    Tween {
        duration: Duration::from_secs(3),
        ..Default::default()
    },
);
```

## Audio File Format Support

Kira uses the Symphonia library for audio decoding. The following formats are supported (with corresponding features):

- **WAV** - `wav` feature
- **OGG Vorbis** - `ogg` feature
- **FLAC** - `flac` feature
- **MP3** - `mp3` feature
- **AAC** - requires `symphonia` with `aac` feature

Default enabled features provide WAV, OGG, FLAC, and MP3 support.

## Platform Support

### Desktop Platforms
- Windows (primary)
- macOS (tested)
- Linux (tested)

### WASM
Limited WASM support with restrictions:
- Static sounds cannot be loaded from files
- Streaming sounds are not supported (heavy thread usage)

## Error Handling

Kira operations return `Result` types that can fail:

```rust
use kira::error::KiraError;

match manager.play(sound_data) {
    Ok(sound) => { /* use sound */ }
    Err(KiraError::AudioManager(err)) => { /* handle error */ }
    Err(e) => { /* handle other error */ }
}
```

## Integration with Bevy

For Bevy game engine integration, use the `bevy_kira_audio` plugin:

```toml
bevy_kira_audio = "0.20"
```

See: https://docs.rs/bevy_kira_audio/

## Cargo Features

- `cpal` - CPAL audio backend support
- `symphonia` - Enable Symphonia audio decoding (default)
- `mp3`, `ogg`, `flac`, `wav` - Audio format support (bundled with symphonia feature)

## Resources

- **Crates.io:** https://crates.io/crates/kira/
- **Docs.rs:** https://docs.rs/kira/latest/kira/
- **GitHub:** https://github.com/tesselode/kira
- **Examples:** https://github.com/tesselode/kira-examples
- **Bevy Integration:** https://docs.rs/bevy_kira_audio/

## License

Licensed under either of:
- Apache License, Version 2.0
- MIT license

at your option.
