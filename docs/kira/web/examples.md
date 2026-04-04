# Source: https://github.com/tesselode/kira-examples

# Kira Examples

## Basic Examples

### Playing a Sound

The simplest example: load and play a sound file.

```rust
use kira::{
    AudioManager, AudioManagerSettings, DefaultBackend,
    sound::static_sound::StaticSoundData,
};

let mut manager = AudioManager::<DefaultBackend>::new(
    AudioManagerSettings::default()
)?;

let sound_data = StaticSoundData::from_file("sound.ogg")?;
let mut sound = manager.play(sound_data)?;
```

### Playing Multiple Sounds Simultaneously

Kira efficiently handles playing the same sound multiple times:

```rust
use kira::{
    AudioManager, AudioManagerSettings, DefaultBackend,
    sound::static_sound::StaticSoundData,
};

let mut manager = AudioManager::<DefaultBackend>::new(
    AudioManagerSettings::default()
)?;

let sound_data = StaticSoundData::from_file("sound.ogg")?;

// Cloning sound_data is cheap and doesn't use extra memory
manager.play(sound_data.clone())?;
// After a couple seconds...
manager.play(sound_data.clone())?;
```

## Advanced Examples

### Tweening Parameters

Smoothly adjust sound properties over time:

```rust
use std::time::Duration;
use kira::{
    AudioManager, AudioManagerSettings, DefaultBackend,
    sound::static_sound::StaticSoundData,
    Tween,
};

let mut manager = AudioManager::<DefaultBackend>::new(
    AudioManagerSettings::default()
)?;

let sound_data = StaticSoundData::from_file("sound.ogg")?;
let mut sound = manager.play(sound_data)?;

// Gradually speed up over 3 seconds
sound.set_playback_rate(
    2.0,
    Tween {
        duration: Duration::from_secs(3),
        ..Default::default()
    },
);
```

### Using Mixer Effects

Apply audio effects to tracks:

```rust
use kira::{
    AudioManager, AudioManagerSettings, DefaultBackend,
    sound::static_sound::StaticSoundData,
    track::TrackBuilder,
    track::effect::filter::FilterBuilder,
};

let mut manager = AudioManager::<DefaultBackend>::new(
    AudioManagerSettings::default()
)?;

// Create a track with a low-pass filter
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

Time sounds to musical beats using clocks:

```rust
use kira::{
    AudioManager, AudioManagerSettings, DefaultBackend,
    sound::static_sound::StaticSoundData,
    clock::ClockSpeed,
};

const TEMPO: f64 = 120.0;

let mut manager = AudioManager::<DefaultBackend>::new(
    AudioManagerSettings::default()
)?;

// Create a clock that ticks 120 times per minute (one beat per tick)
let mut clock = manager.add_clock(ClockSpeed::TicksPerMinute(TEMPO))?;

// Schedule sounds to play at specific beats
let sound_data_1 = StaticSoundData::from_file("sound1.ogg")?
    .start_time(clock.time() + 2); // Play 2 beats from now
manager.play(sound_data_1)?;

let sound_data_2 = StaticSoundData::from_file("sound2.ogg")?
    .start_time(clock.time() + 4); // Play 4 beats from now
manager.play(sound_data_2)?;

clock.start()?;
```

### Seamless Loops

Create seamless looping sounds:

```rust
use kira::sound::static_sound::{StaticSoundData, StaticSoundSettings};

let sound_data = StaticSoundData::from_file("loop.ogg")?;
let settings = StaticSoundSettings::default()
    .loop_region(0.0..); // Loop from start to end

// Play the looping sound
manager.play(sound_data.with_settings(settings))?;
```

### Metronome

Create a simple metronome using clocks:

```rust
use kira::{
    AudioManager, AudioManagerSettings, DefaultBackend,
    sound::static_sound::StaticSoundData,
    clock::ClockSpeed,
};

const TEMPO: f64 = 120.0;

let mut manager = AudioManager::<DefaultBackend>::new(
    AudioManagerSettings::default()
)?;

let beep_sound = StaticSoundData::from_file("beep.ogg")?;
let mut clock = manager.add_clock(ClockSpeed::TicksPerMinute(TEMPO))?;

// Play a beep on each beat
loop {
    manager.play(beep_sound.clone())?;
    std::thread::sleep(std::time::Duration::from_millis(500));
}
```

## Effect Examples

### Low-Pass Filter

Apply a low-pass filter to muffle audio:

```rust
use kira::track::effect::filter::FilterBuilder;

let filter = FilterBuilder::new()
    .cutoff(1000.0) // Cutoff frequency in Hz
    .resonance(1.0);
```

### Reverb

Add reverb/echo to audio:

```rust
use kira::track::effect::reverb::ReverbBuilder;

let reverb = ReverbBuilder::new()
    .room_size(0.5)
    .damping(0.5);
```

### Delay

Create a delay effect:

```rust
use kira::track::effect::delay::DelayBuilder;
use std::time::Duration;

let delay = DelayBuilder::new()
    .time(Duration::from_millis(500));
```

### Compressor

Compress dynamic range:

```rust
use kira::track::effect::compressor::CompressorBuilder;
use std::time::Duration;

let compressor = CompressorBuilder::new()
    .threshold(0.0)
    .ratio(4.0)
    .attack_time(Duration::from_millis(10))
    .release_time(Duration::from_millis(100));
```

## Resource Links

- **GitHub Repository:** https://github.com/tesselode/kira
- **Examples Repository:** https://github.com/tesselode/kira-examples
- **Crates.io:** https://crates.io/crates/kira/
- **Docs.rs:** https://docs.rs/kira/latest/kira/
