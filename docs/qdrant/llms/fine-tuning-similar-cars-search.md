# Fine Tuning Similar Cars Search

Yusuf Sarıgöz

·

June 28, 2022

![Fine Tuning Similar Cars Search](https://qdrant.tech/articles_data/cars-recognition/preview/title.jpg)

Supervised classification is one of the most widely used training objectives in machine learning,
but not every task can be defined as such. For example,

1. Your classes may change quickly —e.g., new classes may be added over time,
2. You may not have samples from every possible category,
3. It may be impossible to enumerate all the possible classes during the training time,
4. You may have an essentially different task, e.g., search or retrieval.

All such problems may be efficiently solved with similarity learning.

N.B.: If you are new to the similarity learning concept, checkout the [awesome-metric-learning](https://github.com/qdrant/awesome-metric-learning) repo for great resources and use case examples.

However, similarity learning comes with its own difficulties such as:

1. Need for larger batch sizes usually,
2. More sophisticated loss functions,
3. Changing architectures between training and inference.

Quaterion is a fine tuning framework built to tackle such problems in similarity learning.
It uses [PyTorch Lightning](https://www.pytorchlightning.ai/)
as a backend, which is advertized with the motto, “spend more time on research, less on engineering.”
This is also true for Quaterion, and it includes:

1. Trainable and servable model classes,
2. Annotated built-in loss functions, and a wrapper over [pytorch-metric-learning](https://kevinmusgrave.github.io/pytorch-metric-learning/) when you need even more,
3. Sample, dataset and data loader classes to make it easier to work with similarity learning data,
4. A caching mechanism for faster iterations and less memory footprint.

## [Anchor](https://qdrant.tech/articles/cars-recognition/\#a-closer-look-at-quaterion) A closer look at Quaterion

Let’s break down some important modules:

- `TrainableModel`: A subclass of `pl.LightNingModule` that has additional hook methods such as `configure_encoders`, `configure_head`, `configure_metrics` and others
to define objects needed for training and evaluation —see below to learn more on these.
- `SimilarityModel`: An inference-only export method to boost code transfer and lower dependencies during the inference time.
In fact, Quaterion is composed of two packages:
1. `quaterion_models`: package that you need for inference.
2. `quaterion`: package that defines objects needed for training and also depends on `quaterion_models`.
- `Encoder` and `EncoderHead`: Two objects that form a `SimilarityModel`.
In most of the cases, you may use a frozen pretrained encoder, e.g., ResNets from `torchvision`, or language modelling
models from `transformers`, with a trainable `EncoderHead` stacked on top of it.
`quaterion_models` offers several ready-to-use `EncoderHead` implementations,
but you may also create your own by subclassing a parent class or easily listing PyTorch modules in a `SequentialHead`.

Quaterion has other objects such as distance functions, evaluation metrics, evaluators, convenient dataset and data loader classes, but these are mostly self-explanatory.
Thus, they will not be explained in detail in this article for brevity.
However, you can always go check out the [documentation](https://quaterion.qdrant.tech/) to learn more about them.

The focus of this tutorial is a step-by-step solution to a similarity learning problem with Quaterion.
This will also help us better understand how the abovementioned objects fit together in a real project.
Let’s start walking through some of the important parts of the code.

If you are looking for the complete source code instead, you can find it under the [examples](https://github.com/qdrant/quaterion/tree/master/examples/cars)
directory in the Quaterion repo.

## [Anchor](https://qdrant.tech/articles/cars-recognition/\#dataset) Dataset

In this tutorial, we will use the [Stanford Cars](https://pytorch.org/vision/main/generated/torchvision.datasets.StanfordCars.html)
dataset.

![Stanford Cars Dataset](https://storage.googleapis.com/quaterion/docs/class_montage.jpg)

Stanford Cars Dataset

It has 16185 images of cars from 196 classes,
and it is split into training and testing subsets with almost a 50-50% split.
To make things even more interesting, however, we will first merge training and testing subsets,
then we will split it into two again in such a way that the half of the 196 classes will be put into the training set and the other half will be in the testing set.
This will let us test our model with samples from novel classes that it has never seen in the training phase,
which is what supervised classification cannot achieve but similarity learning can.

In the following code borrowed from [`data.py`](https://github.com/qdrant/quaterion/blob/master/examples/cars/data.py):

- `get_datasets()` function performs the splitting task described above.
- `get_dataloaders()` function creates `GroupSimilarityDataLoader` instances from training and testing datasets.
- Datasets are regular PyTorch datasets that emit `SimilarityGroupSample` instances.

N.B.: Currently, Quaterion has two data types to represent samples in a dataset. To learn more about `SimilarityPairSample`, check out the [NLP tutorial](https://quaterion.qdrant.tech/tutorials/nlp_tutorial.html)

```python
import numpy as np
import os
import tqdm
from torch.utils.data import Dataset, Subset
from torchvision import datasets, transforms
from typing import Callable
from pytorch_lightning import seed_everything

from quaterion.dataset import (
    GroupSimilarityDataLoader,
    SimilarityGroupSample,
)