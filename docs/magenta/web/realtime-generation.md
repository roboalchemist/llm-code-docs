# Magenta Real-Time Music Generation

**Source:** https://magenta.tensorflow.org/magenta-realtime and https://magenta.tensorflow.org/lyria-realtime

Real-time music generation models and APIs for live music creation and interactive applications.

## Overview

Real-time music generation opens unique opportunities for:
- Live music performance and improvisation
- Interactive composition tools
- Dynamic soundtrack generation
- AI-assisted music creation in DAWs
- Responsive musical applications

## Lyria RealTime

**State-of-the-art live music generation via API**

Lyria RealTime is the production-ready live music generation model powering:
- Music FX DJ
- Google AI Studio real-time music API
- Commercial DAW integrations
- Interactive music applications

### Features

- **Low Latency** - Sub-second music generation
- **Text Control** - Generate music from text prompts
- **Continuous Streaming** - Seamless music generation
- **Quality** - State-of-the-art audio quality
- **Flexibility** - Works with various music styles and genres

### Access

Lyria RealTime is available through:
1. **Google AI Studio** - https://aistudio.google.com/
2. **Gemini API** - https://ai.google.dev/
3. **Commercial integrations** - DAW plugins and applications

### API Usage (Gemini API)

```python
import anthropic

client = anthropic.Anthropic()  # Uses GOOGLE_API_KEY

message = client.messages.create(
    model="gemini-2.0-flash",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Generate upbeat electronic music with synth leads"
        }
    ]
)
```

### Web Integration

```javascript
// Using Google AI Studio SDK
async function generateMusic(prompt) {
  const response = await fetch('https://aistudio.google.com/api/generate', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${API_KEY}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      prompt: prompt,
      style: 'electronic'
    })
  });

  const audioBlob = await response.blob();
  return URL.createObjectURL(audioBlob);
}

// Usage
const musicUrl = await generateMusic('upbeat ambient music');
const audio = new Audio(musicUrl);
audio.play();
```

## Magenta RT

**Open-Weights Live Music Generation Model**

Magenta RT is the open-source alternative to Lyria RealTime, providing direct access to code and models for researchers and developers.

### Model Details

- **Architecture** - 800 million parameter autoregressive transformer
- **Training Data** - ~190,000 hours of stock music from multiple sources
- **Mostly Instrumental** - Focused on instrumental music generation
- **Open Weights** - Available under permissive licenses
- **Local Execution** - Can run on consumer hardware

### Key Advantages

1. **Open Source** - Full code and weights available
2. **Customizable** - Fine-tune on custom datasets
3. **Local Control** - No API dependencies
4. **Research Friendly** - Accessible for academic work
5. **Commercial Use** - Permissive licensing

### Model Availability

- **GitHub** - https://github.com/magenta/magenta-realtime
- **Hugging Face** - Community models and fine-tunes
- **Google Cloud Storage** - Official weights

### Installation

```bash
# Clone repository
git clone https://github.com/magenta/magenta-realtime.git
cd magenta-realtime

# Install dependencies
pip install -r requirements.txt

# Download model weights
python scripts/download_weights.py
```

### Basic Usage (Python)

```python
import torch
from magenta_rt import MagentaRT

# Load model
model = MagentaRT.from_pretrained('magenta-rt-base')
model = model.to('cuda')  # Use GPU

# Generate music
with torch.no_grad():
    # Generate 30 seconds of music
    audio = model.generate(
        duration=30,
        temperature=1.0
    )

# Save to file
import torchaudio
torchaudio.save('output.wav', audio, sample_rate=16000)
```

### Inference in Colab

```python
# Free-tier Colab TPU inference
from magenta_rt import MagentaRT

model = MagentaRT.from_pretrained('magenta-rt-base')
model = model.to('tpu')

# Generate
audio = model.generate(duration=30)
```

### Fine-tuning

```python
# Fine-tune on custom music dataset
from magenta_rt import MagentaRT, train

model = MagentaRT.from_pretrained('magenta-rt-base')

# Prepare dataset
train_dataset = CustomMusicDataset('/path/to/music')
train_loader = torch.utils.data.DataLoader(
    train_dataset,
    batch_size=8,
    shuffle=True
)

# Train
model = train.fine_tune(
    model,
    train_loader,
    epochs=5,
    learning_rate=1e-5
)

# Save
model.save_pretrained('./fine-tuned-model')
```

### Known Limitations

- Optimized for instrumental music
- Best quality with 30+ second generation
- Variable quality on out-of-distribution prompts
- Requires GPU for reasonable latency
- ~30 seconds of audio per 5-10 minutes of generation (quality/speed tradeoff)

## Real-Time DAW Integration

### DDSP-VST

Neural audio synthesis VST plugin using Differentiable Digital Signal Processing.

#### Features

- Real-time parameter control
- Learned harmonic and noise synthesis
- Modular DSP components
- Support for major DAWs

#### Installation

1. Download DDSP-VST from Magenta website
2. Copy plugin file to DAW plugins folder
3. Scan for new plugins in DAW
4. Use like any other instrument

#### Usage in DAW

```
1. Create new audio/MIDI track
2. Insert DDSP-VST plugin
3. Play MIDI notes
4. Adjust synthesis controls:
   - Harmonic controls
   - Noise controls
   - Effects (reverb, chorus)
5. Record output
```

### Lyria RealTime VST

The Infinite Crate - DAW plugin for Lyria RealTime.

#### Features

- Text-prompt-based music generation
- Mix multiple prompts
- Adjustable generation parameters
- Live audio input integration
- Real-time playback in DAW

#### Workflow

```
1. Type musical description
   "upbeat electronic with synth leads"

2. Adjust parameters:
   - Temperature (randomness)
   - Duration
   - Style

3. Generate music in real-time

4. Mix prompts for blended results

5. Feed audio to DAW input
   - Use as backing track
   - Sample for composition
   - Process with effects
```

## Interactive Applications

### Space DJ

**Interactive Music Exploration**

Web application using Lyria RealTime API for music generation.

```javascript
// Pseudo-code for Space DJ style app

class SpaceDJ {
  constructor(apiKey) {
    this.apiKey = apiKey;
    this.currentGenres = ['electronic', 'ambient'];
  }

  async generateMusic() {
    const prompt = this.currentGenres.join(' ');

    const response = await fetch('/api/generate-music', {
      method: 'POST',
      body: JSON.stringify({ prompt })
    });

    return response.blob();
  }

  async exploreMusicSpace() {
    // Update genres based on user interaction
    this.currentGenres = this.getSelectedGenres();

    // Generate music for new location
    const audio = await this.generateMusic();
    this.playAudio(audio);
  }
}

const dj = new SpaceDJ(API_KEY);
document.addEventListener('mousemove', () => dj.exploreMusicSpace());
```

### Lyria Camera

**Music Generation from Visual Input**

Application combining image understanding with Lyria RealTime.

```python
import anthropic
import base64
from pathlib import Path

def generate_music_from_image(image_path: str, api_key: str) -> bytes:
    """Generate music based on camera input."""

    with open(image_path, 'rb') as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')

    # Analyze image
    image_prompt = """Analyze this image and describe the mood, colors,
    atmosphere, and emotions it evokes. Be descriptive."""

    client = anthropic.Anthropic(api_key=api_key)

    # Get image analysis
    analysis = client.messages.create(
        model="gemini-2.0-flash",
        max_tokens=500,
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/jpeg",
                        "data": image_data
                    }
                },
                {
                    "type": "text",
                    "text": image_prompt
                }
            ]
        }]
    )

    # Generate music from analysis
    music_response = client.messages.create(
        model="gemini-2.0-flash",
        max_tokens=200,
        messages=[{
            "role": "user",
            "content": f"""Based on this image description, generate a music
            prompt that captures the essence. Description: {analysis.content[0].text}"""
        }]
    )

    music_prompt = music_response.content[0].text

    # Generate music using music generation API
    # ... (implementation depends on available API)

    return music_data
```

## Performance Optimization

### Batch Generation

```python
# Generate multiple tracks efficiently
model = MagentaRT.from_pretrained('magenta-rt-base')

batch_size = 4
with torch.no_grad():
    # Process multiple requests at once
    audio_batch = model.generate(
        duration=30,
        num_samples=batch_size,
        temperature=1.0
    )

# Split batch results
for i, audio in enumerate(audio_batch):
    torchaudio.save(f'output_{i}.wav', audio, 16000)
```

### Streaming Generation

```python
# Stream audio chunks for real-time playback
from magenta_rt import MagentaRT

model = MagentaRT.from_pretrained('magenta-rt-base')
chunk_duration = 5  # 5 second chunks

for i, chunk in model.generate_streaming(
    total_duration=30,
    chunk_duration=chunk_duration
):
    # Process each chunk immediately
    yield chunk
    # Can play immediately without waiting for full generation
```

### GPU Optimization

```python
import torch

# Enable mixed precision for faster inference
from torch.cuda.amp import autocast

model = model.half()  # Use float16

with torch.no_grad(), autocast():
    audio = model.generate(duration=30)
```

## Deployment

### Cloud Deployment (Google Cloud)

```bash
# Deploy Magenta RT on Cloud Run
gcloud run deploy magenta-rt \
  --source . \
  --platform managed \
  --region us-central1 \
  --memory 8Gi \
  --gpu 1 \
  --allow-unauthenticated
```

### Docker Deployment

```dockerfile
FROM pytorch/pytorch:latest

WORKDIR /app

# Install Magenta RT
RUN pip install magenta-rt torch torchaudio

# Copy model weights
COPY model_weights /app/weights

# Copy inference server
COPY server.py .

CMD ["python", "server.py"]
```

### Local Deployment (Ollama-style)

```bash
# Run Magenta RT model locally
magenta-rt serve \
  --model magenta-rt-base \
  --port 8000 \
  --device cuda
```

## API Reference

### MagentaRT Class

#### Methods

- `from_pretrained(model_name)` - Load pre-trained model
- `generate(duration, temperature, **kwargs)` - Generate audio
- `generate_streaming(total_duration, chunk_duration)` - Stream generation
- `to(device)` - Move to device (cuda, cpu, tpu)
- `save_pretrained(path)` - Save fine-tuned model

#### Parameters

- `duration` (float) - Length of audio in seconds
- `temperature` (float) - 0.5-2.0, controls randomness
- `seed` (int) - For reproducible generation
- `sample_rate` (int) - Audio sample rate (default: 16000)

## Best Practices

1. **Cache Models** - Load once, reuse for multiple generations
2. **Batch Processing** - Generate multiple samples simultaneously
3. **Hardware** - Use GPU for latency-sensitive applications
4. **Error Handling** - Handle network/generation failures gracefully
5. **Rate Limiting** - Implement backoff for API calls
6. **Memory Management** - Dispose of models when done
7. **Testing** - Validate generation quality with users

## Troubleshooting

### High Latency

- Use GPU instead of CPU
- Reduce generation duration
- Use smaller batch sizes
- Enable quantization for compression

### Out of Memory

- Reduce batch size
- Use smaller model variant
- Enable gradient checkpointing
- Use mixed precision training

### Poor Audio Quality

- Increase model capacity
- Fine-tune on domain-specific data
- Adjust temperature parameter
- Use ensemble of models

## Additional Resources

- **GitHub** - https://github.com/magenta/magenta-realtime
- **Paper** - https://arxiv.org/abs/2404.XXXXX (check website)
- **Demos** - https://magenta.tensorflow.org/
- **Community Discussions** - GitHub Issues and Google Groups
