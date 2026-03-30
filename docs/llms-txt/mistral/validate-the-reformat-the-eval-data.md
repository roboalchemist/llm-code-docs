# validate the reformat the eval data 
python reformat_data.py ultrachat_chunk_eval.jsonl
```

:::important[ ]
This `reformat_data.py` script is tailored for the UltraChat data and may not be universally applicable to other datasets. Please modify this script and reformat your data accordingly.
:::

After running the script, few cases were removed from the training data. 

```
Skip 3674th sample
Skip 9176th sample
Skip 10559th sample
Skip 13293th sample
Skip 13973th sample
Skip 15219th sample
```

Let’s inspect one of these cases. There are two issues with this use case: 
- one of the assistant messages is an empty string; 
- the last message is not an assistant message. 

<img src="/img/guides/ft1.png" alt="drawing" width="700"/>


### Upload dataset
We can then upload both the training data and evaluation data to the Mistral Client, making them available for use in fine-tuning jobs. 

<Tabs>
  <TabItem value="python" label="python" default>

```python
from mistralai import Mistral


api_key = os.environ["MISTRAL_API_KEY"]

client = Mistral(api_key=api_key)

ultrachat_chunk_train = client.files.upload(file={
    "file_name": "ultrachat_chunk_train.jsonl",
    "content": open("ultrachat_chunk_train.jsonl", "rb"),
})
ultrachat_chunk_eval = client.files.upload(file={
    "file_name": "ultrachat_chunk_eval.jsonl",
    "content": open("ultrachat_chunk_eval.jsonl", "rb"),
})
```
  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript


const apiKey = process.env.MISTRAL_API_KEY;

const client = new MistralClient(apiKey);

const file = fs.readFileSync('ultrachat_chunk_train.jsonl');
const ultrachat_chunk_train = await client.files.create({ file });

const file = fs.readFileSync('ultrachat_chunk_eval.jsonl');
const ultrachat_chunk_eval = await client.files.create({ file });
```
  </TabItem>
  
  <TabItem value="curl" label="curl">

```bash
curl https://api.mistral.ai/v1/files \
  -H "Authorization: Bearer $MISTRAL_API_KEY" \
  -F purpose="fine-tune" \
  -F file="@ultrachat_chunk_train.jsonl"

curl https://api.mistral.ai/v1/files \
  -H "Authorization: Bearer $MISTRAL_API_KEY" \
  -F purpose="fine-tune" \
  -F file="@ultrachat_chunk_eval.jsonl"
```
  </TabItem>

</Tabs>

Example output:

Note that you will need the file IDs for the next steps. 
```
{
    "id": "66f96d02-8b51-4c76-a5ac-a78e28b2584f",
    "object": "file",
    "bytes": 140893645,
    "created_at": 1717164199,
    "filename": "ultrachat_chunk_train.jsonl",
    "purpose": "fine-tune"
}

{
    "id": "84482011-dfe9-4245-9103-d28b6aef30d4",
    "object": "file",
    "bytes": 7247934,
    "created_at": 1717164200,
    "filename": "ultrachat_chunk_eval.jsonl",
    "purpose": "fine-tune"
}
```

### Create a fine-tuning job
Next, we can create a fine-tuning job:

<Tabs>
  <TabItem value="python" label="python" default>

```python