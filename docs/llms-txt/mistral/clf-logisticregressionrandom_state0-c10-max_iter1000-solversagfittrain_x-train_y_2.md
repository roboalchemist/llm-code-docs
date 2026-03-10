# clf = LogisticRegression(random_state=0, C=1.0, max_iter=1000, solver='sag').fit(train_x, train_y)

print(f"Precision: {100*np.mean(clf.predict(test_x) == test_y.to_list()):.2f}%")
```

Output
```
Precision: 86.25%
```

## Clustering
What if we don't have disease labels? One approach to gain insights from the data is through clustering. Clustering is an unsupervised machine learning technique that groups similar data points together based on their similarity with respect to certain features. In the context of text embeddings, we can use the distance between each embedding as a measure of similarity, and group together data points with embeddings that are close to each other in the high-dimensional space.

Since we already know there are 24 clusters, let's use the K-means clustering with 24 clusters. Then we can inspect a few examples and verify whether the examples in a single cluster are similar to one another. For example, take a look at the first three rows of cluster 23. We can see that they look very similar in terms of symptoms.

```python
from sklearn.cluster import KMeans

model = KMeans(n_clusters=24, max_iter=1000)
model.fit(df['embeddings'].to_list())
df["cluster"] = model.labels_
print(*df[df.cluster==23].text.head(3), sep='\n\n')
```

Output:
```
I have been feeling extremely tired and weak, and I've also been coughing a lot with difficulty breathing. My fever is very high, and I'm producing a lot of mucus when I cough.
I've got a cough that won't go away, and I'm exhausted. I've been coughing up thick mucous and my fever is also pretty high.
I have a persistent cough and have been feeling quite fatigued. My fever is through the roof, and I'm having trouble breathing. When I cough, I also cough up a lot of mucous.
```

## Retrieval
Our embedding model excels in retrieval tasks, as it is trained with retrieval in mind. Embeddings are also incredibly helpful in implementing retrieval-augmented generation (RAG) systems, which use retrieved relevant information from a knowledge base to generate responses. At a high-level, we embed a knowledge base, whether it is a local directory, text files, or internal wikis, into text embeddings and store them in a vector database. Then, based on the user's query, we retrieve the most similar embeddings, which represent the relevant information from the knowledge base. Finally, we feed these relevant embeddings to a large language model to generate a response that is tailored to the user's query and context. If you are interested in learning more about how RAG systems work and how to implement a basic RAG, check out our [previous guide](/guides/rag) on this topic.


[Classifier Factory]
Source: https://docs.mistral.ai/docs/capabilities/finetuning/classifier-factory

In various domains and enterprises, classification models play a crucial role in enhancing efficiency, improving user experience, and ensuring compliance. These models serve diverse purposes, including but not limited to:
- **Moderation**: Classification models are essential for moderating services and classifying unwanted content. For instance, our [moderation service](../../guardrailing/#moderation-api) helps in identifying and filtering inappropriate or harmful content in real-time, ensuring a safe and respectful environment for users.
- **Intent Detection**: These models help in understanding user intent and behavior. By analyzing user interactions, they can predict the user's next actions or needs, enabling personalized recommendations and improved customer support.
- **Sentiment Analysis**: Emotion and sentiment detection models analyze text data to determine the emotional tone behind words. This is particularly useful in social media monitoring, customer feedback analysis, and market research, where understanding public sentiment can drive strategic decisions.
- **Data Clustering**: Classification models can group similar data points together, aiding in data organization and pattern recognition. This is beneficial in market segmentation, where businesses can identify distinct customer groups for targeted marketing campaigns.
- **Fraud Detection**: In the financial sector, classification models help in identifying fraudulent transactions by analyzing patterns and anomalies in transaction data. This ensures the security and integrity of financial systems.
- **Spam Filtering**: Email services use classification models to filter out spam emails, ensuring that users receive only relevant and safe communications.
- **Recommendation Systems**: Classification models power recommendation engines by categorizing user preferences and suggesting relevant products, movies, or content based on past behavior and preferences.

By leveraging classification models, organizations can make data-driven decisions, improve operational efficiency, and deliver better products and services to their customers.

For this reason, we designed a friendly and easy way to make your own classifiers. Leveraging our small but highly efficient models and training methods, the Classifier Factory is both available directly in [la plateforme](https://console.mistral.ai/build/finetuned-models) and our API.

## Dataset Format

Data must be stored in JSON Lines (`.jsonl`) files, which allow storing multiple JSON objects, each on a new line.

We provide two endpoints:
- `v1/classifications`: To classify raw text.
- `v1/chat/classifications`: To classify chats and multi-turn interactions.

There are 2 main kinds of classification models:
- Single Target
- Multi-Target

### 1. Single Target

For single label classification, data must have the label name and the value for that corresponding label. Example:

<Tabs groupId="classification-type">
  <TabItem value="v1/classifications" label="v1/classifications" default>

```json
{
    "text": "I love this product!",
    "labels": {
        "sentiment": "positive" // positive/neutral/negative
    }
}
```

For multiple labels, you can provide a list.

```json
{
    "text": "I love this product!",
    "labels": {
        "sentiment": ["positive","neutral"]
    }
}
```

  </TabItem>

  <TabItem value="v1/chat/classifications" label="v1/chat/classifications">

```json
{
    "messages": [{"role": "user", "content": "I love this product!"}],
    "labels": {
        "sentiment": "positive" // positive/neutral/negative
    }
}
```

For multiple labels, you can provide a list.

```json
{
    "messages": [{"role": "user", "content": "I love this product!"}],
    "labels": {
        "sentiment": ["positive","neutral"]
    }
}
```

  </TabItem>

</Tabs>


When using the result model, you will be able to retrieve the scores for the corresponding label and value.

Note that the files must be in JSONL format, meaning every JSON object must be flattened into a single line, and each JSON object is on a new line.
<details>

<summary><b>Raw `.jsonl` file example.</b></summary>

```json
{"text": "I love this product!", "labels": {"sentiment": "positive"}}
{"text": "The game was amazing.", "labels": {"sentiment": "positive"}}
{"text": "The new policy is controversial.", "labels": {"sentiment": "neutral"}}
{"text": "I don't like the new design.", "labels": {"sentiment": "negative"}}
{"text": "The team won the championship.", "labels": {"sentiment": "positive"}}
{"text": "The economy is in a bad shape.", "labels": {"sentiment": "negative"}}
...
```

</details>

- Label data must be a dictionary with the label name as the key and the label value as the value.

### 2. Multi-Target

You can also have multiple targets and not only a single one. This is useful if you want to classify different aspects of the same content independently. Example:

<Tabs groupId="classification-type">
  <TabItem value="v1/classifications" label="v1/classifications" default>

```json
{
    "text": "I love this product!",
    "labels": {
        "sentiment": "positive", // positive/neutral/negative
        "is-english": "yes" // yes/no, boolean
    }
}
```

  </TabItem>

  <TabItem value="v1/chat/classifications" label="v1/chat/classifications">

```json
{
    "messages": [{"role": "user", "content": "I love this product!"}],
    "labels": {
        "sentiment": "positive", // positive/neutral/negative
        "is-english": "yes" // yes/no, boolean
    }
}
```

  </TabItem>

</Tabs>

- Each target is independent of each other, meaning the scores for each label will also be independent.

## Upload a file
Once you have the data file with the right format, you can upload the data file to the Mistral Client, making them available for use in fine-tuning jobs.

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python
from mistralai import Mistral


api_key = os.environ["MISTRAL_API_KEY"]

client = Mistral(api_key=api_key)

training_data = client.files.upload(
    file={
        "file_name": "training_file.jsonl",
        "content": open("training_file.jsonl", "rb"),
    }
)

validation_data = client.files.upload(
    file={
        "file_name": "validation_file.jsonl",
        "content": open("validation_file.jsonl", "rb"),
    }
)
```
  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript


const apiKey = process.env.MISTRAL_API_KEY;

const client = new Mistral({apiKey: apiKey});

const training_file = fs.readFileSync('training_file.jsonl');
const training_data = await client.files.upload({
    file: {
        fileName: "training_file.jsonl",
        content: training_file,
    }
});

const validation_file = fs.readFileSync('validation_file.jsonl');
const validation_data = await client.files.upload({
    file: {
        fileName: "validation_file.jsonl",
        content: validation_file,
    }
});
```
  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl https://api.mistral.ai/v1/files \
  -H "Authorization: Bearer $MISTRAL_API_KEY" \
  -F purpose="fine-tune" \
  -F file="@training_file.jsonl"

curl https://api.mistral.ai/v1/files \
  -H "Authorization: Bearer $MISTRAL_API_KEY" \
  -F purpose="fine-tune" \
  -F file="@validation_file.jsonl"
```

  </TabItem>

</Tabs>

## Create a fine-tuning job
The next step is to create a fine-tuning job.
- model: the specific model you would like to fine-tune. The choice is `ministral-3b-latest`.
- training_files: a collection of training file IDs, which can consist of a single file or multiple files.
- validation_files: a collection of validation file IDs, which can consist of a single file or multiple files.
- hyperparameters: two adjustable hyperparameters, "training_steps" and "learning_rate", that users can modify.
- auto_start:
    - `auto_start=True`: Your job will be launched immediately after validation.
    - `auto_start=False` (default): You can manually start the training after validation by sending a POST request to `/fine_tuning/jobs/<uuid>/start`.
- integrations: external integrations we support such as Weights and Biases for metrics tracking during training.

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python