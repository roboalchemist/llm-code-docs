# Nomic Documentation

Source: https://docs.nomic.ai/platform/embeddings-and-retrieval/guides/using-umap-with-atlas

Uniform Manifold Approximation and Projection (UMAP) is a popular technique for reducing the dimensionality of high-dimensional datasets, making it much easier to visualize your data in two or three dimensions. UMAP stands out because it does a great job of preserving both the local details and the overall structure of your data, which helps you see meaningful patterns and relationships.

In Atlas, UMAP is used to create clear 2D map visualizations of your data, allowing you to quickly spot clusters and patterns. You can upload your own embeddings to Atlas and use UMAP to visualize them, or upload your own text/image data and have Atlas generate embeddings for your UMAP for you.

By default selects a projection algorithm for your data if you don't specify one:

- UMAP is the default for datasets with fewer than 50,000 datapoints.
- Nomic Project, a highly scalable algorithm, is used for datasets with 50,000 or more datapoints.
Here's how to use UMAP with Atlas:

```
from nomic import AtlasDatasetfrom nomic.data_inference import ProjectionOptions# data is a DataFrame or list of dictionariesdataset.add_data(data)atlas_map = dataset.create_index(    indexed_field='text', # name of your field to embed goes here    projection=ProjectionOptions(      model="umap", # specify UMAP as the projection model to use      n_neighbors=20,      min_dist=0.01,      n_epochs=200  ))
```

You can always explicitly choose UMAP as your projection method and customize its parameters, regardless of dataset size.

You specify UMAP parameters as ProjectionOptions when using the create_index method of an AtlasDataset.

```
ProjectionOptions
```

```
create_index
```

```
AtlasDataset
```

Key UMAP parameters you can configure include:

- n_neighbors: Controls how UMAP balances local versus global structure in the data.
```
n_neighbors
```

- min_dist: Controls how tightly UMAP is allowed to pack points together.
```
min_dist
```

- n_epochs: Number of epochs to use for optimization.
```
n_epochs
```

Refer to the UMAP documentation for a detailed explanation of UMAP parameters and the Atlas API Reference for more details on ProjectionOptions.

```
ProjectionOptions
```

Below, we show some examples of using UMAP to visualize text and embedding data.

## Visualizing Text Embeddings​

Your browser does not support the video tag.

This example shows how to visualize a dataset of airline reviews using UMAP. The dataset contains customer reviews of an airline service with ratings and review text.

```
import pandas as pdfrom nomic import AtlasDatasetfrom nomic.data_inference import ProjectionOptions# Load airline reviews datadf = pd.read_csv("https://docs.nomic.ai/singapore_airlines_reviews.csv")# Create an Atlas Datasetdataset = AtlasDataset("airline-reviews")# Add the data to the Atlas Datasetdataset.add_data(df)# Build UMAP from your Atlas datasetatlas_map = dataset.create_index(    indexed_field='text',    projection=ProjectionOptions(      model="umap",      n_neighbors=20,      min_dist=0.01,      n_epochs=200  ))
```

Your atlas_map, once it finishes building, will now be a UMAP visualization of the text embeddings in the dataset.

## Visualizing AI Model Training Dynamics​

This advanced example shows how to visualize the embeddings from a convolutional neural network during training. We'll train the model on the MNIST dataset and track how the embeddings evolve over epochs.

Your browser does not support the video tag.

In this example, the UMAP visualization shows how the model's internal representations of digits evolve over training epochs. As training progresses, you can see the embeddings form clearer clusters corresponding to the different digit classes.

### Downloading MNIST Dataset​

We setup a CNN image classifier for the MNIST dataset of handwritten digits:

```
import torchimport torch.nn as nnimport torch.optim as optimimport torchvisionimport torchvision.transforms as transformsfrom torch.utils.data import DataLoader, Subsetimport numpy as npimport timefrom PIL import Imageimport base64import ioNUM_EPOCHS = 20LEARNING_RATE = 3e-6BATCH_SIZE = 128NUM_VIS_SAMPLES = 2000EMBEDDING_DIM = 128ATLAS_DATASET_NAME = "mnist_training_embeddings"device = torch.device("cuda" if torch.cuda.is_available() else "cpu")print(f"Using device: {device}\n")def tensor_to_html(tensor):    """Helper function to convert image tensors to HTML for rendering in Nomic Atlas"""    # Denormalize the image    img = torch.clamp(tensor.clone().detach().cpu().squeeze(0) * 0.3081 + 0.1307, 0, 1)    img_pil = Image.fromarray((img.numpy() * 255).astype('uint8'), mode='L')    buffered = io.BytesIO()    img_pil.save(buffered, format="PNG")    img_str = base64.b64encode(buffered.getvalue()).decode()    return f'<img src="data:image/png;base64,{img_str}" width="28" height="28">'class MNIST_CNN(nn.Module):    def __init__(self, embedding_dim=128):        super(MNIST_CNN, self).__init__()        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)        self.relu1 = nn.ReLU()        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)        self.relu2 = nn.ReLU()        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)        self.flatten = nn.Flatten()        self.fc1 = nn.Linear(64 * 7 * 7, embedding_dim)        self.relu3 = nn.ReLU()        self.fc2 = nn.Linear(embedding_dim, 10)    def forward(self, x):        x = self.pool1(self.relu1(self.conv1(x)))        x = self.pool2(self.relu2(self.conv2(x)))        x = self.flatten(x)        embeddings = self.relu3(self.fc1(x))        output = self.fc2(embeddings)        return output, embeddingstransform = transforms.Compose([    transforms.ToTensor(),    transforms.Normalize((0.1307,), (0.3081,))])train_dataset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)test_dataset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)persistent_workers_flag = True if device.type not in ['mps', 'cpu'] else Falsenum_workers_val = 2 if persistent_workers_flag else 0train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True, num_workers=num_workers_val, persistent_workers=persistent_workers_flag if num_workers_val > 0 else False)vis_indices = list(range(NUM_VIS_SAMPLES))vis_subset = Subset(test_dataset, vis_indices)test_loader_for_vis = DataLoader(vis_subset, batch_size=BATCH_SIZE, shuffle=False, num_workers=num_workers_val, persistent_workers=persistent_workers_flag if num_workers_val > 0 else False)print(f"Training on {len(train_dataset)} samples, visualizing {NUM_VIS_SAMPLES} test samples per epoch.\n")
```

### Collect Embeddings During Training​

We save embeddings from the last layer at each iteration to track the change in the model's output distribution over the course of training. This is what Atlas is uniquely well suited to visualize.

```
model = MNIST_CNN(embedding_dim=EMBEDDING_DIM).to(device)criterion = nn.CrossEntropyLoss()optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)all_embeddings_list = []all_metadata_list = []all_images_html = []overall_start_time = time.time()for epoch in range(NUM_EPOCHS):    epoch_start_time = time.time()    model.train()    running_loss = 0.0    for batch_idx, (data, target) in enumerate(train_loader):        data, target = data.to(device), target.to(device)        optimizer.zero_grad()        outputs, _ = model(data)        loss = criterion(outputs, target)        loss.backward()        optimizer.step()        running_loss += loss.item()        if (batch_idx + 1) % 200 == 0:            print(f'Epoch [{epoch+1}/{NUM_EPOCHS}], Batch [{batch_idx+1}/{len(train_loader)}], Avg Loss: {running_loss / 200:.4f}')            running_loss = 0.0    print(f"Epoch {epoch+1}/{NUM_EPOCHS} training finished in {time.time() - epoch_start_time:.2f}s.\n")    model.eval()    vis_samples_collected_this_epoch = 0    image_offset_in_vis_subset = 0     with torch.no_grad():        for data, target in test_loader_for_vis:              data, target = data.to(device), target.to(device)              _, embeddings_batch = model(data)              for i in range(embeddings_batch.size(0)):                original_idx_in_subset = image_offset_in_vis_subset + i                 if original_idx_in_subset >= NUM_VIS_SAMPLES:                    continue                all_embeddings_list.append(embeddings_batch[i].cpu().numpy())                                img_html = tensor_to_html(data[i])                all_images_html.append(img_html)                all_metadata_list.append({                    'epoch': epoch,                    'label': f'Digit: {target[i].item()}',                    'vis_sample_idx': original_idx_in_subset,                    'image_html': img_html                })                vis_samples_collected_this_epoch += 1              image_offset_in_vis_subset += embeddings_batch.size(0)              if vis_samples_collected_this_epoch >= NUM_VIS_SAMPLES:                 break    print(f"Collected {vis_samples_collected_this_epoch} embeddings for visualization in epoch {epoch+1}.\n")total_script_time = time.time() - overall_start_timeprint(f"Total training and embedding extraction time: {total_script_time:.2f}s\n")
```

### Upload to Atlas​

We upload the embeddings and metadata to Atlas with UMAP as our projection method.

```
from nomic import AtlasDatasetdataset = AtlasDataset("mnist-training-embeddings")dataset.add_data(data=all_metadata_list, embeddings=np.array(all_embeddings_list))dataset.create_index(projection='umap', topic_model=False)
```

## More Information on UMAP​

Check out the UMAP documentation for more information on UMAP.

### Tips for Effective UMAP Usage​

- Experiment with parameters: n_neighbors and min_dist are the most impactful parameters. Try different values to see how they affect your map.
```
n_neighbors
```

```
min_dist
```

- Data preprocessing: The quality of your UMAP projection can be influenced by the preprocessing steps applied to your embeddings.
- Interpretability: While UMAP is great for visualization, remember that distances in the 2D projection are not always directly interpretable as true distances in the high-dimensional space. Focus on relative positions and clusters.
- Combine with Atlas features: Use Atlas's rich features like vector search in conjunction with your UMAP projection to gain deeper insights.
- Visualizing Text Embeddings
- Visualizing AI Model Training DynamicsDownloading MNIST DatasetCollect Embeddings During TrainingUpload to Atlas
- Downloading MNIST Dataset
- Collect Embeddings During Training
- Upload to Atlas
- More Information on UMAPTips for Effective UMAP Usage
- Tips for Effective UMAP Usage
