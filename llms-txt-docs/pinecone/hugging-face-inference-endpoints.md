# Source: https://docs.pinecone.io/integrations/hugging-face-inference-endpoints.md

# Hugging Face Inference Endpoints

> Using Hugging Face Inference Endpoints and Pinecone to generate and index high-quality vector embeddings

export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

Hugging Face Inference Endpoints offers a secure production solution to easily deploy any Hugging Face Transformers, Sentence-Transformers and Diffusion models from the Hub on dedicated and autoscaling infrastructure managed by Hugging Face.

Coupled with Pinecone, you can use Hugging Face to generate and index high-quality vector embeddings with ease.

<PrimarySecondaryCTA secondaryHref={"#setup-guide"} secondaryLabel={"View setup guide"} />

## Setup guide

Hugging Face Inference Endpoints allows access to straightforward model inference. Coupled with Pinecone we can generate and index high-quality vector embeddings with ease.

Let's get started by initializing an Inference Endpoint for generating vector embeddings.

### Create an endpoint

We start by heading over to the [Hugging Face Inference Endpoints homepage](https://ui.endpoints.huggingface.co/endpoints) and signing up for an account if needed. After, we should find ourselves on this page:

<img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-0.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=193e39d5e65bb87b3b1b1b0d429180b6" alt="endpoints 0" data-og-width="1622" width="1622" data-og-height="936" height="936" data-path="images/hf-endpoints-0.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-0.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=a93797264f78198d1dee10c2a1fe820a 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-0.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=8f4799ed2133a717e22e78aa2cf0f245 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-0.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=7afce26d262b3f4a30933214e6274ca0 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-0.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=d3e1e36538d3684c13b371cb1f2ede96 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-0.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=02472896f27429a4f7655faf8abb1c3f 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-0.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=df1732e3534af7e1ffb4e55dc6b33245 2500w" />

We click on **Create new endpoint**, choose a model repository (eg name of the model), endpoint name (this can be anything), and select a cloud environment. Before moving on it is *very important* that we set the **Task** to **Sentence Embeddings** (found within the *Advanced configuration* settings).

<img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-1.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=322d411596affb620805d391d824c863" alt="endpoints 1" data-og-width="1622" width="1622" data-og-height="1196" height="1196" data-path="images/hf-endpoints-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-1.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=094ffc9c6babf9f1fa1060d214063d5d 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-1.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=3a794a6a789b7a2082b2147f1d79cc57 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-1.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=0556363ec9cb927bc76433c4f7525072 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-1.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=2191bb241e7042f790baac1d5323b18d 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-1.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=3f1f41f28c98a2c1944d15802cc3ea01 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-1.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=7ab0e0991b83c12202d8986e8182a292 2500w" />

<img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-2.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=db8b7952c2d42d939b6764cb39f62a7d" alt="endpoints 2" data-og-width="1548" width="1548" data-og-height="354" height="354" data-path="images/hf-endpoints-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-2.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=8b8ddd85cddf0b44fdfb12c5d828e200 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-2.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=3cf09f91cc295046fd8cdeef7f95f617 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-2.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=59fed1c0984ab4fcdb9ed8cd0a14512d 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-2.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=67b3dfd3362eecf6dd0cacaa5988ed8c 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-2.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=aa7577163d22caa6dd4032a926acd9f4 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-2.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=d9ce21fa370f79c7d5acd8a9651aa3e7 2500w" />

Other important options include the *Instance Type*, by default this uses CPU which is cheaper but also slower. For faster processing we need a GPU instance. And finally, we set our privacy setting near the end of the page.

After setting our options we can click **Create Endpoint** at the bottom of the page. This action should take use to the next page where we will see the current status of our endpoint.

<img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-3.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=925a8437da312a756edf0a1bdbac16e0" alt="endpoints 3" data-og-width="1548" width="1548" data-og-height="112" height="112" data-path="images/hf-endpoints-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-3.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=a08a7a0a590037b0f959fd94f5563006 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-3.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=bd7b7970fbd20dae84dc2116dd6647f5 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-3.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=6202139573fbda7e1b2cbe71c0ddd7a9 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-3.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=2542fa57778a6a81d564e1e39bf5ba6f 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-3.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=3ff523c988657e3dbdfcc8bc374a374d 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-3.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=37ba16c888d5f1dfc1c0ad60480ae57e 2500w" />

Once the status has moved from **Building** to **Running** (this can take some time), we're ready to begin creating embeddings with it.

## Create embeddings

Each endpoint is given an **Endpoint URL**, it can be found on the endpoint **Overview** page. We need to assign this endpoint URL to the `endpoint_url` variable.

<img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-4.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=af3da5b0476bec94258c3cc711fd8b47" alt="endpoints 4" data-og-width="1404" width="1404" data-og-height="222" height="222" data-path="images/hf-endpoints-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-4.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=26b6d9ed0620c27e4982f99b6427f3df 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-4.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=281c535c7fe5e8fa90f1cb267fd922a6 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-4.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=0a037b4ca662219475cacc73d1243262 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-4.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=7df385446234a0f87c199b3748fe6f0b 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-4.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=eda7a0dd9a7424ab38a6eeb49c5256af 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-4.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=2bc2d005700830aa2660cfd6afa723a4 2500w" />

```Python Python theme={null}
endpoint = "<ENDPOINT_URL>"
```

We will also need the organization API token, we find this via the organization settings on Hugging Face (`https://huggingface.co/organizations/<ORG_NAME>/settings/profile`). This is assigned to the `api_org` variable.

<img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-5.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=41b16cbb97439082bbd4a4c7e76c662d" alt="endpoints 5" data-og-width="2230" width="2230" data-og-height="1120" height="1120" data-path="images/hf-endpoints-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-5.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=81ba23ffdce70a192ee85f22d4cb525f 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-5.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=be1170a4cc6f68a9ec56252dfcff73b0 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-5.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=e64873c28eb2937436cde6d91a33990a 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-5.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=40ccf67ba795afd1a2b3d1ca7ec39efe 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-5.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=1d9f9593f03a500ae85698d07e86c5cf 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/hf-endpoints-5.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=e154eaafeb63a69100d2a73e55edd2ce 2500w" />

```Python Python theme={null}
api_org = "<API_ORG_TOKEN>"
```

Now we're ready to create embeddings via Inference Endpoints. Let's start with a toy example.

```Python Python theme={null}
import requests

# add the api org token to the headers
headers = {
    'Authorization': f'Bearer {api_org}'
}
# we add sentences to embed like so
json_data = {"inputs": ["a happy dog", "a sad dog"]}
# make the request
res = requests.post(
    endpoint,
    headers=headers,
    json=json_data
)
```

We should see a `200` response.

```Python Python theme={null}
res
```

```
<Response [200]>
```

Inside the response we should find two embeddings...

```Python Python theme={null}
len(res.json()['embeddings'])
```

```
2
```

We can also see the dimensionality of our embeddings like so:

```Python Python theme={null}
dim = len(res.json()['embeddings'][0])
dim
```

```
768
```

We will need more than two items to search through, so let's download a larger dataset. For this we will use Hugging Face datasets.

```Python Python theme={null}
from datasets import load_dataset

snli = load_dataset("snli", split='train')
snli
```

```
Downloading: 100%|██████████| 1.93k/1.93k [00:00<00:00, 992kB/s]
Downloading: 100%|██████████| 1.26M/1.26M [00:00<00:00, 31.2MB/s]
Downloading: 100%|██████████| 65.9M/65.9M [00:01<00:00, 57.9MB/s]
Downloading: 100%|██████████| 1.26M/1.26M [00:00<00:00, 43.6MB/s]

Dataset({
    features: ['premise', 'hypothesis', 'label'],
    num_rows: 550152
})
```

SNLI contains 550K sentence pairs, many of these include duplicate items so we will take just one set of these (the *hypothesis*) and deduplicate them.

```Python  theme={null}
passages = list(set(snli['hypothesis']))
len(passages)
```

```
480042
```

We will drop to 50K sentences so that the example is quick to run, if you have time, feel free to keep the full 480K.

```Python Python theme={null}
passages = passages[:50_000]
```

## Create a Pinecone index

With our endpoint and dataset ready, all that we're missing is a vector database. For this, we need to initialize our connection to Pinecone, this requires a [free API key](https://app.pinecone.io/).

```Python Python theme={null}
import pinecone

# initialize connection to pinecone (get API key at app.pinecone.io)
pinecone.init(api_key="YOUR_API_KEY", environment="YOUR_ENVIRONMENT")

```

Now we create a new index called `'hf-endpoints'`, the name isn't important *but* the `dimension` must align to our endpoint model output dimensionality (we found this in `dim` above) and the model metric (typically `cosine` is okay, but not for all models).

```Python Python theme={null}
index_name = 'hf-endpoints'

# check if the hf-endpoints index exists
if index_name not in pinecone.list_indexes():
    # create the index if it does not exist
    pinecone.create_index(
        index_name,
        dimension=dim,
        metric="cosine"
    )

# connect to hf-endpoints index we created
index = pinecone.Index(index_name)
```

## Create and index embeddings

Now we have all of our components ready; endpoints, dataset, and Pinecone. Let's go ahead and create our dataset embeddings and index them within Pinecone.

```Python Python theme={null}
from tqdm.auto import tqdm

# we will use batches of 64
batch_size = 64

for i in tqdm(range(0, len(passages), batch_size)):
    # find end of batch
    i_end = min(i+batch_size, len(passages))
    # extract batch
    batch = passages[i:i_end]
    # generate embeddings for batch via endpoints
    res = requests.post(
        endpoint,
        headers=headers,
        json={"inputs": batch}
    )
    emb = res.json()['embeddings']
    # get metadata (just the original text)
    meta = [{'text': text} for text in batch]
    # create IDs
    ids = [str(x) for x in range(i, i_end)]
    # add all to upsert list
    to_upsert = list(zip(ids, emb, meta))
    # upsert/insert these records to pinecone
    _ = index.upsert(vectors=to_upsert)

# check that we have all vectors in index
index.describe_index_stats()
```

```
100%|██████████| 782/782 [11:02<00:00,  1.18it/s]

{'dimension': 768,
 'index_fullness': 0.1,
 'namespaces': {'': {'vector_count': 50000}},
 'total_vector_count': 50000}
```

With everything indexed we can begin querying. We will take a few examples from the *premise* column of the dataset.

```Python Python theme={null}
query = snli['premise'][0]
print(f"Query: {query}")
# encode with HF endpoints
res = requests.post(endpoint, headers=headers, json={"inputs": query})
xq = res.json()['embeddings']
# query and return top 5
xc = index.query(xq, top_k=5, include_metadata=True)
# iterate through results and print text
print("Answers:")
for match in xc['matches']:
    print(match['metadata']['text'])
```

```
Query: A person on a horse jumps over a broken down airplane.
Answers:
The horse jumps over a toy airplane.
a lady rides a horse over a plane shaped obstacle
A person getting onto a horse.
person rides horse
A woman riding a horse jumps over a bar.
```

These look good, let's try a couple more examples.

```Python Python theme={null}
query = snli['premise'][100]
print(f"Query: {query}")
# encode with HF endpoints
res = requests.post(endpoint, headers=headers, json={"inputs": query})
xq = res.json()['embeddings']
# query and return top 5
xc = index.query(xq, top_k=5, include_metadata=True)
# iterate through results and print text
print("Answers:")
for match in xc['matches']:
    print(match['metadata']['text'])
```

```
Query: A woman is walking across the street eating a banana, while a man is following with his briefcase.
Answers:
A woman eats a banana and walks across a street, and there is a man trailing behind her.
A woman eats a banana split.
A woman is carrying two small watermelons and a purse while walking down the street.
The woman walked across the street.
A woman walking on the street with a monkey on her back.
```

And one more...

```Python Python theme={null}
query = snli['premise'][200]
print(f"Query: {query}")
# encode with HF endpoints
res = requests.post(endpoint, headers=headers, json={"inputs": query})
xq = res.json()['embeddings']
# query and return top 5
xc = index.query(xq, top_k=5, include_metadata=True)
# iterate through results and print text
print("Answers:")
for match in xc['matches']:
    print(match['metadata']['text'])
```

```
Query: People on bicycles waiting at an intersection.
Answers:
A pair of people on bikes are waiting at a stoplight.
Bike riders wait to cross the street.
people on bicycles
Group of bike riders stopped in the street.
There are bicycles outside.
```

All of these results look excellent. If you are not planning on running your endpoint and vector DB beyond this tutorial, you can shut down both.

## Clean up

Shut down the endpoint by navigating to the Inference Endpoints **Overview** page and selecting **Delete endpoint**. Delete the Pinecone index with:

```Python Python theme={null}
pinecone.delete_index(index_name)
```

<Note>Once the index is deleted, you cannot use it again.</Note>
