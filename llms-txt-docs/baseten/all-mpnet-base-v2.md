# Source: https://docs.baseten.co/examples/models/microsoft/all-mpnet-base-v2.md

# All MPNet Base V2

> A text embedding model with a context window of 384 tokens and a dimensionality of 768 values.

export const MicrosoftIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M11.49 2H2V11.492H11.492V2H11.49Z" fill="#F25022" />
<path d="M22 2H12.508V11.492H22V2Z" fill="#7FBA00" />
<path d="M11.49 12.508H2V22H11.492V12.508H11.49Z" fill="#00A4EF" />
<path d="M22 12.508H12.508V22H22V12.508Z" fill="#FFB900" />
</svg>} horizontal />;

<MicrosoftIconCard title="Deploy All MPNet Base V2" href="https://app.baseten.co/deploy/all-mpnet-base-v2" />

## Example usage

This model takes a list of strings and returns a list of embeddings, where each embedding is a list of 768 floating-point number representing the semantic text embedding of the associated string.

Strings can be up to 384 tokens in length (approximately 280 words). If the strings are longer, they'll be truncated before being run through the embedding model.

```python  theme={"system"}
import requests
import os

# Replace the empty string with your model id below
model_id = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]

data = {
    "text": ["I want to eat pasta", "I want to eat pizza"],
}

# Call model endpoint
res = requests.post(
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json=data
)

# Print the output of the model
print(res.json())
```

## JSON output

```json  theme={"system"}
[
  [0.2593194842338562, "...", -1.4059709310531616],
  [0.11028853803873062, "...", -0.9492666125297546]
]
```
