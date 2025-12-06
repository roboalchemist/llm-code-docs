# Nomic Documentation

Source: https://docs.nomic.ai/platform/embeddings-and-retrieval/guides/improve-ai-model-performance-with-embedding-visualization-and-evaluation

In this guide, we'll walk through how to visualize embedding model decision boundaries to improve AI model accuracy using Nomic Atlas. Embedding visualizations help engineers debug models, detect overlapping clusters, and refine vector search performance.

By using Nomic Atlas's interactive embedding visualizations, AI engineers can:

- Quickly diagnose model failures
- Optimize embedding separability for improved performance
- Debug vector search, clustering, and classification models
## Why Visualizing Embedding Decision Boundaries Matters​

Embeddings encode data into high-dimensional spaces for use in AI applications such as NLP, recommendation systems, and search engines.
However, when embeddings are poorly formed, models struggle to separate concepts correctly, leading to misclassification and poor model performance.

With Atlas, engineers can explore embeddings in an interactive space and detect:

- Cluster overlap causing poor classification performance
- Misclassified points that require dataset adjustments
- Feature drift in embeddings over different training iterations
## Setup​

To run the code in this guide, make sure you have the required libraries installed to your python environment:

- pip
- uv
```
pip install nomic numpy torch torchvision pytorch-lightning
```

```
uv add nomic numpy torch torchvision pytorch-lightning
```

Then, login to nomic with your Nomic API key. If you don't have a Nomic API key you can create one here.

```
nomic
```

- Terminal
- Python
```
nomic login nk-...
```

```
import nomicnomic.login("nk-...")
```

## Create Your Embeddings Data Map​

To demonstrate how to create a map of embeddings, we will train a neural network to generate embeddings and upload the generated data to Atlas.

### Train Model​

Let's train a simple neural network on the MNIST dataset and visualize its embedding space to understand how it makes decisions. We'll use a minimal Multi-Layer Perceptron (MLP) that takes 28x28 pixel images as input and outputs 10-dimensional embeddings - one dimension for each digit class (0-9).

First, let's set up our imports and initialize our data:

```
import osimport torchfrom pytorch_lightning import LightningModule, Trainerfrom pytorch_lightning.callbacks.progress import TQDMProgressBarfrom torch.nn import functional as Ffrom torch.utils.data import DataLoader, random_splitfrom torchvision import transformsfrom torchvision.datasets import MNISTfrom nomic import AtlasDatasetimport numpy as npPATH_DATASETS = os.environ.get("PATH_DATASETS", ".")BATCH_SIZE = 256torch.manual_seed(0)# Init DataLoader from MNIST Datasettrain_ds = MNIST(PATH_DATASETS, train=True, download=True, transform=transforms.ToTensor())test_ds = MNIST(PATH_DATASETS, train=False, download=True, transform=transforms.ToTensor())train_loader = DataLoader(train_ds, batch_size=BATCH_SIZE)test_loader = DataLoader(test_ds, batch_size=BATCH_SIZE)
```

Next, we'll define our model. This is a simple two-layer network that will learn to classify MNIST digits:

```
class MNISTModel(LightningModule):    def __init__(self):        super().__init__()        self.l1 = torch.nn.Linear(28 * 28, 10)        self.l2 = torch.nn.Linear(10, 10)    def forward(self, x):        return torch.relu(self.l2(torch.relu(self.l1(x.view(x.size(0), -1)))))    def training_step(self, batch, batch_nb):        x, y = batch        logits = self(x)        loss = F.cross_entropy(logits, y)        return loss    def configure_optimizers(self):        return torch.optim.Adam(self.parameters(), lr=0.02)
```

Now let's train the model:

```
mnist_model = MNISTModel()trainer = Trainer(accelerator="auto",max_epochs=15,)trainer.fit(mnist_model, train_dataloaders=train_loader, val_dataloaders=test_loader)mnist_model.eval()
```

### Generate Embeddings and Metadata​

After training, we'll use the model's final layer outputs as our embeddings. These 10-dimensional vectors represent how the model "sees" each digit:

We prepare a list of embeddings for each image as well as a list of metadata for each image: this way, we can examine this data together in Atlas.

```
all_embeddings = []all_data = []for batch_idx, batch in enumerate(test_loader):    x, y = batch        # Get model embeddings (last layer logits) and predictions    logits = mnist_model(x)    embeddings = logits.detach().numpy()    predictions = torch.argmax(logits, dim=1).detach().numpy()        # get image links for each image (already hosted)    image_links = [f'https://s3.amazonaws.com/static.nomic.ai/mnist/eval/{label}/{batch_idx*BATCH_SIZE+idx}.jpg'                       for idx, label in enumerate(y)]        # prepare metadata for each image    batch_data = [{'label': str(int(label)), 'prediction': str(int(prediction)), 'image': image, 'id': f'{batch_idx*BATCH_SIZE+idx}'}     for idx, (label, image, prediction) in enumerate(zip(y.tolist(), image_links, predictions))]        all_embeddings.append(embeddings)    all_data.extend(batch_data)
```

### Upload to Atlas​

Now we create an AtlasDataset for our embeddings, add our emebddings array and metadata, and create a data map.

```
dataset = AtlasDataset(    'mnist-model-embeddings',    description='Embeddings of an MNIST model',)dataset.add_data(embeddings=np.concatenate(all_embeddings), data=all_data)data_map = dataset.create_index()
```

## View Embeddings in Atlas​

Once the map is finished building, when you view your map in Atlas, you'll see that the embeddings form 10 distinct clusters - one for each digit class.

### Visualizing Decision Boundary Overlap​

Pay special attention to the areas where clusters overlap. These regions represent digits that the model finds ambiguous or difficult to classify correctly.

For example, the map reveals a boundary between the '4' and '9' clusters, highlighting the model's difficulty in distinguishing between these two digits due to their similar shapes.

Examining these overlapping regions is incredibly valuable for model improvement as they highlight which digit pairs are most commonly confused, what types of writing styles cause classification uncertainty, and where additional training data or model capacity might be needed.

Key Indicators of Embedding Quality:

- ✅ Tight, well-separated clusters suggest strong feature learning
- ⚠️ Overlapping clusters indicate classification uncertainty
- ❌ Sparse, unstructured embeddings may signal poor feature extraction
## Conclusion​

Embedding visualizations help AI teams gain deeper insights into feature learning—beyond traditional accuracy metrics.

Try this tutorial with your own embeddings using the Nomic Atlas Python SDK

- Why Visualizing Embedding Decision Boundaries Matters
- Setup
- Create Your Embeddings Data MapTrain ModelGenerate Embeddings and MetadataUpload to Atlas
- Train Model
- Generate Embeddings and Metadata
- Upload to Atlas
- View Embeddings in AtlasVisualizing Decision Boundary Overlap
- Visualizing Decision Boundary Overlap
- Conclusion
