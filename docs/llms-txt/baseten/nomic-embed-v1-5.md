# Source: https://docs.baseten.co/examples/models/nomic/nomic-embed-v1-5.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Nomic Embed v1.5

> SOTA text embedding model with variable dimensionality — outperforms OpenAI text-embedding-ada-002 and text-embedding-3-small models.

export const NomicIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<g clip-path="url(#clip0_603_2944)">
<path d="M2.96725 16.2278V3.5H3.69541V20.4705H2.96725L0.782782 7.74262V20.4705H0.0546265V3.5H0.782782L2.96725 16.2278Z" fill="black" />
<path d="M7.40443 19.7326C7.60164 19.7326 7.76851 19.6635 7.90504 19.5251C8.05673 19.3867 8.13259 19.21 8.13259 18.9948V4.97569C8.13259 4.77586 8.05673 4.60677 7.90504 4.46842C7.76851 4.31471 7.60164 4.23785 7.40443 4.23785C7.19205 4.23785 7.0176 4.31471 6.88107 4.46842C6.74454 4.60677 6.67628 4.77586 6.67628 4.97569V18.9948C6.67628 19.21 6.74454 19.3867 6.88107 19.5251C7.0176 19.6635 7.19205 19.7326 7.40443 19.7326ZM7.40443 20.4705C6.99485 20.4705 6.64594 20.3321 6.3577 20.0554C6.08465 19.7633 5.94812 19.4099 5.94812 18.9948V4.97569C5.94812 4.57603 6.08465 4.23016 6.3577 3.9381C6.64594 3.64603 6.99485 3.5 7.40443 3.5C7.79885 3.5 8.14017 3.64603 8.4284 3.9381C8.71663 4.23016 8.86074 4.57603 8.86074 4.97569V18.9948C8.86074 19.4099 8.71663 19.7633 8.4284 20.0554C8.14017 20.3321 7.79885 20.4705 7.40443 20.4705Z" fill="black" />
<path d="M15.3003 3.5H16.0285V20.4705H15.3003V6.45139L13.48 13.8299L11.6596 6.45139V20.4705H10.9314V3.5H11.6596L13.48 10.8785L15.3003 3.5Z" fill="black" />
<path d="M18.1902 20.4705V3.5H18.9184V20.4705H18.1902Z" fill="black" />
<path d="M22.5365 20.4705C22.1268 20.4705 21.7779 20.3321 21.4897 20.0554C21.2166 19.7633 21.0802 19.4099 21.0802 18.9948V4.97569C21.0802 4.57603 21.2166 4.23016 21.4897 3.9381C21.7779 3.64603 22.1268 3.5 22.5365 3.5C22.9308 3.5 23.2722 3.64603 23.5604 3.9381C23.8487 4.23016 23.9928 4.57603 23.9928 4.97569V6.45139H23.2646V4.97569C23.2646 4.77586 23.1887 4.60677 23.037 4.46842C22.9004 4.31471 22.7336 4.23785 22.5365 4.23785C22.3241 4.23785 22.1496 4.31471 22.013 4.46842C21.8765 4.60677 21.8083 4.77586 21.8083 4.97569V18.9948C21.8083 19.21 21.8765 19.3867 22.013 19.5251C22.1496 19.6635 22.3241 19.7326 22.5365 19.7326C22.7336 19.7326 22.9004 19.6635 23.037 19.5251C23.1887 19.3867 23.2646 19.21 23.2646 18.9948V17.5191H23.9928V18.9948C23.9928 19.4099 23.8487 19.7633 23.5604 20.0554C23.2722 20.3321 22.9308 20.4705 22.5365 20.4705Z" fill="black" />
</g>
<defs>
<clipPath id="clip0_603_2944">
<rect width="24" height="17" fill="white" transform="translate(0 3.5)" />
</clipPath>
</defs>
</svg>} horizontal />;

<NomicIconCard title="Deploy Nomic Embed v1.5" href="https://app.baseten.co/deploy/nomic_embed_v1_5?_gl=1*dnaf1c*_gcl_au*MTYzMTk5MDI1OS4xNzM2NjM4OTMw" />

## Example usage

Nomic Embed v1.5 is a state of the art text embedding model with two special features:

* You can choose whether to optimize the embeddings for retrieval, search, clustering, or classification.
* You can trade off between cost and accuracy by choosing your own dimensionality thanks to Matryoshka Representation Learning.

Nomic Embed v1.5 takes the following parameters:

* `texts` the strings to embed.
* `task_type` the task to optimize the embedding for. Can be `search_document` (default), `search_query`, `clustering`, or `classification`.
* `dimensionality` the size of each output vector, any integer between `64` and `768` (default).

This code sample demonstrates embedding a set of sentences for retrieval with a dimensionality of 512.

```python  theme={"system"}
import requests
import os

# Replace the empty string with your model id below
model_id = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]

data = {
    "texts": ["I want to eat pasta", "I want to eat pizza"],
    "task_type": "search_document",
    "dimensionality": 512
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
  [-0.03811980411410332, "...", -0.023593541234731674],
  [-0.042617011815309525, "...", -0.0191882885992527]
]
```
