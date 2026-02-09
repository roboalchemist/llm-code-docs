# Source: https://braintrust.dev/docs/cookbook/recipes/VoiceAgent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Evaluating a voice agent

<div className="text-sm">[Contributed](https://github.com/braintrustdata/braintrust-cookbook/blob/main/examples/VoiceAgent/voiceagent.ipynb) by [Adrian Barbir](https://www.linkedin.com/in/adrianbarbir/) on 2025-02-13</div>

In this cookbook, we'll walk through how to evaluate an AI voice agent that classifies short customer support messages by language. In a production application, this might be one component of a customer support agent. Our approach uses an LLM and text-to-speech (TTS) to generate synthetic customer calls, and OpenAI's GPT-4o audio model to classify the calls. Finally, we'll use Braintrust to evaluate the performance of the classifier using `ExactMatch` from our [autoevals library](https://github.com/braintrustdata/autoevals).

## Getting started

You’ll need a [Braintrust](https://www.braintrust.dev/signup) account, along with an [OpenAI API key](https://platform.openai.com/). Export your `BRAINTRUST_API_KEY` and `OPENAI_API_KEY` to your environment:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
export BRAINTRUST_API_KEY="YOUR_BRAINTRUST_API_KEY"
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
```

Next, install the required packages:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
pip install braintrust openai autoevals librosa soundfile
```

We’ll import our modules, then wrap the OpenAI client for Braintrust features.

<Callout type="info">
  Best practice is to export your API key as an environment variable. However, to make it easier to follow along with this cookbook, you can also hardcode it into the code below.
</Callout>

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import os
import base64
import tempfile
import random
import soundfile as sf
import librosa
import openai
import string
import nest_asyncio
import numpy as np

from braintrust import EvalAsync, Attachment, current_span, wrap_openai
from autoevals import ExactMatch

# Uncomment to hardcode your API keys
# os.environ["BRAINTRUST_API_KEY"] = "YOUR_BRAINTRUST_API_KEY"
# os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

openai.api_key = os.environ["OPENAI_API_KEY"]

# OpenAI client instance, wrapped for Braintrust.
openai_client = wrap_openai(openai.OpenAI(api_key=openai.api_key))

nest_asyncio.apply()
```

## Generating synthetic support calls

We'll create a function `generate_customer_issue` that asks the LLM to produce one-sentence customer service inquiries in multiple languages, along with a fallback if LLM calls fail. Then, we'll call a TTS endpoint to produce audio from each sentence. We store everything in an array for easy iteration.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
def generate_customer_issue(language):
    """
    Generate a realistic one-sentence customer service inquiry in the specified language.
    If the API call fails, return a fallback string.
    """
    prompt = (
        f"Generate a realistic one-sentence customer service inquiry in {language}. "
        "The sentence should reflect a common customer issue and be in natural language."
    )
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=100,
        )
        return response.choices[0].message.content.strip()
    except Exception:
        fallback_texts = {
            "english": "I can't access my account.",
            "spanish": "No puedo acceder a mi cuenta.",
            "french": "Je n'arrive pas à accéder à mon compte.",
            "german": "Ich kann nicht auf mein Konto zugreifen.",
            "italian": "Non riesco ad accedere al mio account.",
        }
        return fallback_texts.get(language, "I need help.")
```

## Creating evaluation data

We'll generate multiple snippets for each language, each produced by TTS. If TTS fails, we use a dummy silence clip as a fallback.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
def load_eval_data(limit=20):
    """
    Generate synthetic evaluation data simulating customer service calls.
    For each of five languages, generate a customer issue and create TTS audio.
    If the TTS API call fails, print a debug message and use dummy audio data.
    """
    languages = ["english", "spanish", "french", "german", "italian"]
    voices = [
        "alloy",
        "ash",
        "coral",
        "echo",
        "fable",
        "onyx",
        "nova",
        "sage",
        "shimmer",
    ]
    eval_data = []

    examples_per_language = limit // len(languages)
    extra_examples = limit % len(languages)

    for i, lang in enumerate(languages):
        # Distribute any extra examples across the first few languages.
        num_examples = examples_per_language + (1 if i < extra_examples else 0)
        for _ in range(num_examples):
            # Generate the raw text for the TTS call.
            customer_text = generate_customer_issue(lang)
            selected_voice = random.choice(voices)
            tts_file_path = None
            try:
                with tempfile.NamedTemporaryFile(
                    suffix=".mp3", delete=False
                ) as tmp_file:
                    tts_file_path = tmp_file.name

                tts_response = openai.audio.speech.create(
                    model="tts-1",
                    voice=selected_voice,
                    input=customer_text,
                )
                # Use the original streaming call that worked before the asyncio changes.
                tts_response.stream_to_file(tts_file_path)
                audio_array, sampling_rate = librosa.load(tts_file_path, sr=None)
            except Exception as e:
                print(
                    f"TTS generation failed for language '{lang}' with voice '{selected_voice}': {e}"
                )
                print("Using dummy audio data instead.")
                # Create 1 second of silence at 22050 Hz as dummy audio.
                audio_array = np.zeros(22050)
                sampling_rate = 22050
            finally:
                if tts_file_path and os.path.exists(tts_file_path):
                    try:
                        os.remove(tts_file_path)
                    except Exception as cleanup_e:
                        print(f"Error cleaning up temporary file: {cleanup_e}")

            # Append the evaluation case with metadata.
            eval_data.append(
                {
                    "input": {
                        "audio": {"array": audio_array, "sampling_rate": sampling_rate}
                    },
                    "expected": lang,
                    "metadata": {
                        "voice_model": selected_voice,
                        "expected_language": lang,
                        "raw_text": customer_text,
                    },
                }
            )

    return eval_data
```

## Task definition and audio attachment

Below is our core task function, `task_func`, which receives an audio snippet, [attaches the raw audio to Braintrust for logging](/evaluate/run-evaluations#attachments), and prompts an LLM to classify the language. Notice how we create an `Attachment` object and call `current_span().log(input={"audio_attachment": attachment})`. This adds the attachment to your log's trace details, which is helpful if you want to replay or debug your audio data.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
def task_func(example):
    input_data = example.get("input", example)
    audio_info = input_data.get("audio")
    if not audio_info:
        return "ERROR: Missing audio input"

    # Determine the audio source: use an existing file or create one from the array.
    audio_path = audio_info.get("path")
    temp_file_created = False
    if not (audio_path and os.path.exists(audio_path)):
        audio_array = audio_info.get("array")
        sampling_rate = audio_info.get("sampling_rate")
        if audio_array is None or sampling_rate is None:
            return "ERROR: Missing audio data"
        try:
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
                audio_path = tmp_file.name
            sf.write(audio_path, audio_array, sampling_rate)
            temp_file_created = True
        except Exception:
            return "ERROR: Failed to write temporary file"

    # Read and encode the audio file.
    try:
        with open(audio_path, "rb") as af:
            audio_bytes = af.read()
        encoded_audio = base64.b64encode(audio_bytes).decode("utf-8")
    except Exception:
        return "ERROR: Failed to read audio file"

    # Log the audio attachment to Braintrust.
    try:
        attachment = Attachment(
            data=audio_bytes,
            filename="raw_audio.wav",
            content_type="audio/wav",
        )
        current_span().log(input={"audio_attachment": attachment})
    except Exception:
        pass

    # Prepare the payload for language classification.
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": (
                        "Please listen to the following audio clip and determine the language being spoken. "
                        "Return only the language as a single word (e.g., 'english', 'spanish'). "
                        "Do not include any additional text or characters. If you cannot identify the language, return 'unknown'."
                    ),
                },
                {
                    "type": "input_audio",
                    "input_audio": {"data": encoded_audio, "format": "wav"},
                },
            ],
        }
    ]

    try:
        response = openai_client.chat.completions.create(
            model="gpt-4o-audio-preview",
            messages=messages,
        )
        raw_text = response.choices[0].message.content.strip().lower()
        if not raw_text:
            raise ValueError("Empty response from GPT-4o")
        output = raw_text.rstrip(string.punctuation)
    except Exception:
        output = "error"
    finally:
        if temp_file_created:
            try:
                os.remove(audio_path)
            except Exception:
                pass

    # Log additional metadata (expected language and raw text used for TTS) to the current span.
    try:
        current_span().log(
            metadata={
                "expected_language": example.get("expected"),
                "raw_text": example.get("metadata", {}).get("raw_text"),
            }
        )
    except Exception:
        pass

    return output
```

<img src="https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/VoiceAgent/attachment.png?fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=2c5520638aec553dbd79dd45648b8eb6" alt="attachment" data-og-width="2474" width="2474" data-og-height="1540" height="1540" data-path="cookbook/assets/VoiceAgent/attachment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/VoiceAgent/attachment.png?w=280&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=93484163af4f3a817abc9b31781ba58e 280w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/VoiceAgent/attachment.png?w=560&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=d17d0a2ee03e4fd995af24c075c2710d 560w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/VoiceAgent/attachment.png?w=840&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=e893d1a6a73d6b0d444673fe7467be9a 840w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/VoiceAgent/attachment.png?w=1100&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=a7e32c4982a4d860f18140a79a48b4f9 1100w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/VoiceAgent/attachment.png?w=1650&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=5a7a803107195cef35c3826d1efbf301 1650w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/VoiceAgent/attachment.png?w=2500&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=9c10796df4e9b2420cc0f4e36dd964a5 2500w" />

## Running the evaluation

To evaluate our voice agent, we run `EvalAsync` with the `ExactMatch` scoring function. This will compare the agent's predicted language to the expected language, returning 1 if they match and 0 otherwise. After you run the code, you'll be able to analyze the results in the Braintrust UI.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
await EvalAsync(
    "Multilingual Language Classification Eval",
    data=load_eval_data,
    task=task_func,
    scores=[ExactMatch],
    metadata={"model": "gpt-4o-audio-preview"},
    experiment_name="multilingual-language-classification-eval",
)
```

## Analyzing results

In the Braintrust UI, you'll have each audio attachment in its corresponding trace, along with your classification logs and the score. You can refine your prompt or switch to a more advanced model if you notice any incorrect classifications.

In our example, we attached metadata to each eval, giving you more granular insights into the classifier's performance. For example, you can group by `expected_language` and see if a particular language fails more often. These sorts of insights allow you to improve your prompting and overall pipeline.

<img src="https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/VoiceAgent/group.png?fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=48866731dfbaca25028742761d7f7e8b" alt="group-by-language" data-og-width="2968" width="2968" data-og-height="1852" height="1852" data-path="cookbook/assets/VoiceAgent/group.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/VoiceAgent/group.png?w=280&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=e7aa46e6291210b92866190fa1649dcb 280w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/VoiceAgent/group.png?w=560&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=0611301839d5a90f7a9042c05e5f23b9 560w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/VoiceAgent/group.png?w=840&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=497be5fcef607864198699e040ae327f 840w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/VoiceAgent/group.png?w=1100&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=4673d5da7fa3a7dd093a9e9a5f3dcff4 1100w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/VoiceAgent/group.png?w=1650&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=f450fe9fed06284c0d18b24a9dbf3235 1650w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/VoiceAgent/group.png?w=2500&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=4a394851fef07c9b29473203c7bbb95f 2500w" />

## Next steps

As you continue iterating on this voice agent or build more complex AI products, you'll want to customize Braintrust even more for your use case.

You might consider:

* Reading our [blog on evaluating agents](https://braintrust.dev/blog/evaluating-agents)

* Learning to [evaluate prompt chaining agents](/cookbook/recipes/PromptChaining)

* Diving deeper into [LLM classifiers](/cookbook/recipes/PrecisionRecall)
