# Magenta Music Models

**Source:** https://magenta.tensorflow.org/

Complete guide to music generation models in Google Magenta.

## MusicVAE

**Variational Autoencoder for Music Generation**

MusicVAE is a neural network model that learns a continuous, learnable representation of musical sequences. It enables both generation of new music and smooth interpolation between melodies.

### Architecture
- Encoder-decoder variational autoencoder (VAE)
- Learns a latent space of musical sequences
- Trained on MIDI data
- Supports various music representations

### Capabilities
- **Generation** - Create new melodies from random latent vectors
- **Interpolation** - Smooth morphing between two melodies
- **Reconstruction** - Reconstruct input sequences
- **Multi-track** - Generate multiple instrument parts simultaneously

### Models Available
- **Melody** - Single melody line generation
- **Drums** - Drum pattern generation
- **Multitrack** - Multiple simultaneous instruments
- **Bass + Drums** - Drum and bass accompaniment

### Example Usage (Python)

```python
from magenta.models import music_vae
from magenta.music import note_seq

# Initialize model
vae = music_vae.MusicVAE()
vae.load_checkpoint(checkpoint_path)

# Generate from random vector
z = np.random.normal(size=16)  # Latent vector
generated_sequence = vae.decode(z)

# Interpolate between two sequences
seq1 = ...  # First melody
seq2 = ...  # Second melody
encoded1 = vae.encode(seq1)
encoded2 = vae.encode(seq2)

# Create smooth interpolation
num_steps = 10
interpolated = []
for i in range(num_steps):
    t = i / (num_steps - 1)
    z = encoded1 * (1 - t) + encoded2 * t
    interpolated.append(vae.decode(z))
```

### Checkpoints

Pre-trained checkpoints available at: `goo.gl/magenta/musicvae-colab`

Includes configurations for:
- 2-bar melodies
- 16-bar melodies
- Drum patterns
- Multitrack music

## MelodyRNN

**Recurrent Neural Network for Melody Generation**

MelodyRNN uses LSTM recurrent neural networks to generate melodies conditioned on musical history.

### Configurations

#### Basic RNN
- Simple LSTM without attention
- Generates melodies based on previous notes
- Fastest inference

#### Attention RNN
- LSTM with attention mechanism
- Attends to full sequence history
- Better long-range dependencies
- Better melodic coherence

#### LookBack RNN
- Attention mechanism over previous N steps
- Efficient attention with fixed lookback window
- Balance between Basic and Attention RNN

### Temperature Parameter

Controls randomness in generation:
- **Low (0.5-0.7)** - More conservative, safer choices
- **Medium (1.0)** - Natural randomness
- **High (1.5+)** - More creative, chaotic output

### Training

```bash
# Create dataset from MIDI files
melody_rnn_create_dataset \
  --config=attention_rnn \
  --input_dir=/path/to/midi/files \
  --output_file=output.tfrecord \
  --eval_split=0.1

# Train model
melody_rnn_train \
  --config=attention_rnn \
  --run_dir=/path/to/run \
  --sequence_example_file=output.tfrecord \
  --hparams="batch_size=32"

# Generate melodies
melody_rnn_generate \
  --config=attention_rnn \
  --checkpoint=/path/to/checkpoint \
  --output_dir=/tmp/melody_rnn_output \
  --temperature=1.0 \
  --num_outputs=10
```

## DrumsRNN

**Recurrent Neural Network for Drum Pattern Generation**

Generates drum patterns given an optional backing track. Models polyphonic drum interactions.

### Features
- Multi-instrument drum support
- Learns drum pattern timing and dynamics
- Can condition on tempo and style
- Pre-trained models for various genres

### Example Patterns

```python
from magenta.models import drums_rnn
from magenta.music import note_seq

# Generate drum pattern
drums_model = drums_rnn.DrumsRNN()
drums_model.load_checkpoint(checkpoint)

# With backing track
backing_track = note_seq.NoteSequence(...)
drums = drums_model.generate(
    backing_track=backing_track,
    temperature=1.0,
    length=16  # 16 quarter notes
)
```

## Performance RNN

**Piano Performance Modeling**

Models piano performance characteristics including:
- Note timing (velocity, when notes are struck)
- Sustain pedal usage
- Expressive variations

### Capabilities
- Generate expressive piano performances
- Model rubato and dynamics
- Learn performance style from examples
- Condition generation on melodies

## Music Transformer

**Transformer-Based Long-Form Music Generation**

Uses transformer architecture for generating longer, more structured musical pieces.

### Advantages Over RNN
- Better long-range dependencies
- More coherent large-scale structure
- Attention mechanisms capture harmonic relationships
- Can generate pieces 4-5 minutes long

### Features
- Self-attention over full sequence
- Positional encodings for temporal relationships
- Generates multi-track compositions
- Better maintains harmonic structure

## Polyphony RNN

**Polyphonic Music Generation**

Generates multi-voice, multi-instrument compositions with proper voice leading and harmony.

### Architecture
- LSTM with polyphonic encoding
- Handles up to 16 simultaneous notes
- Learns harmonic relationships
- Models voice independence

## Improv RNN

**Interactive Improvisation Model**

Generates musical continuations given initial musical ideas. Useful for:
- AI-assisted composition
- Interactive music creation
- Real-time musical response

### Interactive Generation

```python
from magenta.models import improv_rnn

model = improv_rnn.ImprovRNN()
model.load_checkpoint(checkpoint)

# Prime with initial melody
primer = note_seq.NoteSequence(...)

# Generate continuation
continuation = model.generate(
    primer=primer,
    temperature=1.0,
    length=32
)

# Combine
complete = note_seq.combine_sequences([primer, continuation])
```

## NSynth (Neural Synth)

**WaveNet-Based Audio Synthesis**

Neural network approach to synthesizing audio from learned instrument timbres.

### Features
- Learn timbral characteristics from audio samples
- Generate novel sounds by interpolating in timbre space
- Supports pitch transposition
- Real-time synthesis capability

### Architecture
- WaveNet vocoder
- Learned embeddings for instruments/timbres
- Autoregressive audio generation
- Trained on diverse instrument samples

## GANSynth

**Generative Adversarial Network for Audio Synthesis**

GAN-based approach to audio synthesis with improved phase coherence compared to WaveNet.

### Advantages
- Better phase coherence (fewer artifacts)
- Cleaner, more natural sounding audio
- Faster generation than WaveNet
- Better perceptual quality

### Architecture
- Generator network for audio synthesis
- Discriminator for quality assessment
- Progressive training for stability
- Learned timbre/instrument embeddings

## Onsets and Frames Transcription

**Automatic Music Transcription**

Converts audio recordings to MIDI notation using deep learning.

### Features
- Note onset detection
- Frame-level note probability estimation
- Automatic velocity estimation
- Multi-instrument capable

### Usage

```bash
# Transcribe audio to MIDI
onsets_frames_transcription_transcribe \
  --checkpoint=/path/to/checkpoint \
  --input_audio=/path/to/audio.wav \
  --output_midi=/tmp/output.mid
```

## Model Training Guidelines

### Data Preparation

1. **MIDI Files**
   - Collect high-quality MIDI in your domain
   - Remove overly long or short sequences
   - Clean up timing and velocity data
   - Split into train/validation/test

2. **Audio Files**
   - Resample to consistent rate (16kHz typical)
   - Normalize volume levels
   - Segment into training windows
   - Align with MIDI when needed

### Hyperparameters

Common settings:
- **Batch size** - 32-128 depending on GPU memory
- **Learning rate** - 0.001-0.01 (Adam optimizer)
- **Embedding size** - 128-512 dimensions
- **RNN units** - 256-1024 for LSTM
- **Dropout** - 0.2-0.5 for regularization

### Evaluation Metrics

- **Perplexity** - How surprising the model finds test data
- **Accuracy** - For classification tasks
- **BLEU** - Sequence similarity to ground truth
- **Human listening tests** - Essential for music quality

## Pre-trained Checkpoints

All models provide pre-trained checkpoints:

```python
import os
checkpoint_dir = os.path.join(
    os.path.expanduser('~'),
    'magenta-checkpoints'
)
# Checkpoints automatically downloaded on first use
```

## Performance Considerations

### Inference Speed

Approximate generation times per 16 notes (4 seconds of music):
- **RNN models** - 50-200ms CPU, 10-50ms GPU
- **Transformer** - 100-500ms CPU, 20-100ms GPU
- **Audio synthesis** - 1-5 seconds per 4-second clip

### Memory Requirements

Model sizes:
- **RNN models** - 50-200MB
- **Transformer** - 200-500MB
- **Audio synthesis** - 300-1000MB

### Optimization

- Use GPU for real-time generation
- Batch generation for multiple samples
- Cache model checkpoints locally
- Use smaller models for resource-constrained environments

## Community Models

Community members have trained models on:
- Different musical genres
- Cultural music traditions
- Specific instruments
- Custom datasets

Check the Magenta discussion forum and GitHub issues for community contributions.
