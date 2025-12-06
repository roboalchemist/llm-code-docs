# Nomic Documentation

Source: https://docs.nomic.ai/platform/embeddings-and-retrieval/guides/building-image-classifiers-with-atlas

In this cookbook guide, we'll show you how to use Nomic Atlas Semantic Search to build a classifier from an image dataset.

## Why This Cookbook Guide Matters​

Building classifiers with Nomic Atlas does not involve training a model. You just upload a dataset to Atlas and make sure Atlas can find your intended text/image concept in that dataset!

## Cookbook Outline​

In this cookbook guide, you will see how Atlas (using our Nomic Embed models) already gives you what you need to build a high performing image classifier, calibrate against your own data, and use it with the Nomic Python API.

Simple Classifiers: Cats vs Dogs

We will make a classifier for dogs using this dataset of cats and dogs from HuggingFace and demonstrate that it can effectively pick out dogs from the CIFAR-10 dataset

Advanced Classifiers: Detecting Semantics In Images

We will use the Imagenette dataset as a source of images to build a classifier that can detect images of a more complicated semantic concept: a tiny white ball. This will give us a reusable binary classifier that we can adapt to detect this concept in future unseen images.

```
a tiny white ball
```

## Getting Started​

### Prerequisites​

Before we begin, make sure you have:

- Python (3.6 or higher) installed on your machine.
- Nomic API key to access Nomic Atlas.
### Install Required Libraries​

```
pip install nomic dataset numpy tqdm datasets pillow scikit-learn
```

## Simple Classifiers: Cats & Dogs​

The models Nomic Embed Text and Nomic Embed Vision were trained to be aligned.

With zero training, processing text with Nomic Embed Text and processing images with Nomic Embed Vision gives us a way to find entites inside images that we describe with language. Nomic Embed makes it easy to detect a simple concept like a dog in images, because the Nomic Embed latent space is already well-trained on dogs both in text as well as in images.

```
dog
```

### Store Data In Atlas​

We download image datasets from HuggingFace and store them in Atlas.

Here we will use a dataset of pictures of cats and dogs.

```
from datasets import load_datasetfrom nomic import AtlasDatasetdataset = load_dataset("Bingsu/Cat_and_Dog")label_map = {0: "cat", 1: "dog"}data = [{"animal" : label_map[x]} for x in dataset['train']['labels']]atlas_dataset = AtlasDataset("cats-and-dogs")atlas_dataset.add_data(    blobs=dataset['train']['image'],    data=data)atlas_map = atlas_dataset.create_index()
```

Your map will take a few minutes to build. You can view it in your Atlas Dashboard.

### Building a Classifier​

Once your map has built successfully, open the vector search modal in the top left corner of the Atlas dashboard and search for dog to see the images that match the query.

```
dog
```

Your browser does not support the video tag.

#### Determine classifier threshold​

This threshold represents the similarity between the text query and the image embeddings.

We can see that it is easy to manually zero in on the threshold 0.0564 to separate the cats from the dogs.

```
0.0564
```

#### Using embeddings for custom classifiers in Python​

Let's walk through how to build a classifier using the Atlas dataset we created above.

We will define the predict method of an ImageClassifierFromTextQuery to measure the similarity between images and a reference text query with embeddings. When we embed the text query, we use Nomic Embed with the task_type set to search_query.

```
predict
```

```
ImageClassifierFromTextQuery
```

```
task_type
```

```
search_query
```

predict accepts a list of images (paths to images on your machine or PIL.Images) and gets the image embeddings using Nomic Embed Vision, and calculates the similarity between the embeddings for the images and the embedding for the string self.text_emb that the classifier was initialzied with.
The way we calculate similarity is using the function np.dot. If the similarity is greater than the threshold, the classifier will return True, otherwise it will return False.

```
predict
```

```
PIL.Image
```

```
self.text_emb
```

```
np.dot
```

```
True
```

```
False
```

```
import numpy as npfrom PIL import Imagefrom typing import List, Unionclass ImageClassifierFromTextQuery:    """A classifier that returns True when images are similar to particular text query    This is determined by the embedding similarity score between the image and the text query    If this similarity score is above the provided threshold, return True. Otherwise, return False.    """    def __init__(self, text_query: str, threshold: float):        self.threshold = threshold        text_emb = embed.text([text_query], task_type="search_query", model="nomic-embed-text-v1.5")["embeddings"]        self.text_emb: np.ndarray = np.array(text_emb)            def predict(self, image: List[Union[str, Image.Image]]) -> List[bool]:        """Predicts whether the input images are similar to self.text_emb        """        image_emb = embed.image(image)["embeddings"]        image_emb = np.array(image_emb)        similarity = np.dot(self.text_emb, image_emb.T)        return np.squeeze(similarity > self.threshold).tolist()
```

To create a dog_detector, we will pass in the text query dog and the threshold 0.0564 we found using Atlas in the step above.

```
dog_detector
```

```
dog
```

```
0.0564
```

```
dog_detector = ImageClassifierFromTextQuery("dog", .0564)
```

#### Testing the Classifier​

Let's test the classifier on the cats & dogs to make sure it can distinguish them.

We make predictions with dog_detector by passing in the images from the test split of the datatset

```
dog_detector
```

```
test
```

We compute the dog_labels by selecting the images with label 1 (since the dataset has the label scheme: 0 cat 1 dog)

```
dog_labels
```

```
1
```

- Python
- Output
```
print(f"Loading cats / dogs dataset")catsdogs = load_dataset("Bingsu/Cat_and_Dog")print("Predicting")dog_predictions = dog_detector.predict(catsdogs['test']['image'])dog_labels = [x == 1 for x in catsdogs['test']['labels']]print("Precision", np.round(precision_score(dog_labels, dog_predictions), 2))print("Recall", np.round(recall_score(dog_labels, dog_predictions), 2))print("F1", np.round(f1_score(dog_labels, dog_predictions), 2))
```

```
Loading cats / dogs datasetPredictingPrecision 0.99Recall 0.67F1 0.8
```

This classifier does a decent job with zero training. However, note that a precision of 0.99 and recall of 0.67 indicates that we could probably change our threshold to achieve a lower precision and higher recall with further adjustment. Let's try a lower threshold of 0.0544:

```
0.0544
```

- Python
- Output
```
dog_detector_with_lower_threshold = ImageClassifierFromTextQuery("dog", .0544)print("Predicting")dog_predictions_with_lower_threshold = dog_detector_with_lower_threshold.predict(catsdogs['test']['image'])print("Precision", np.round(precision_score(dog_labels, dog_predictions_with_lower_threshold), 2))print("Recall", np.round(recall_score(dog_labels, dog_predictions_with_lower_threshold), 2))print("F1", np.round(f1_score(dog_labels, dog_predictions_with_lower_threshold), 2))
```

```
PredictingPrecision 0.98Recall 0.74F1 0.84
```

This improved the recall of our model by 7% on this test dataset!

#### Generalizing To New Data​

Let's see how well the classifier can detect dogs from CIFAR-10. The dog_labels for this dataset are selected with the label 5 (since the dataset has the label scheme: 0 airplane 1 automobile 2 bird 3 cat 4 deer 5 dog 6 frog 7 horse 8 ship 9 truck)

```
dog_labels
```

```
5
```

We will also build a third dog detector with a higher threshold of 0.0584. Even though the previous dataset benefitted from a lower threshold, a new distribution of images could appear to Nomic Embed Vision and may require adjusting our threshold for improved performance.

```
0.0584
```

- Python
- Output
```
dog_detector_with_higher_threshold = ImageClassifierFromTextQuery("dog", .0584)print("Loading CIFAR dataset")cifar = load_dataset("uoft-cs/cifar10")dog_labels = [x == 5 for x in cifar['test']['label']]for detector, threshold in zip(    [dog_detector_with_lower_threshold, dog_detector, dog_detector_with_higher_threshold],    [0.0544, 0.0564, 0.0584]):    print("Predicting with threshold", threshold)    predictions = detector.predict(cifar['test']['img'])    print("Precision", np.round(precision_score(dog_labels, predictions), 2))    print("Recall", np.round(recall_score(dog_labels, predictions), 2))    print("F1", np.round(f1_score(dog_labels, predictions), 2))
```

```
Loading CIFAR datasetPredicting with threshold 0.0544Precision 0.49Recall 0.94F1 0.64Predicting with threshold 0.0564Precision 0.56Recall 0.92F1 0.7Predicting with threshold 0.0584Precision 0.63Recall 0.89F1 0.74
```

So we can see the higher threshold of 0.0584 does better at detecting dogs in CIFAR-10, and we could likely improve the model still with further experimentation!

```
0.0584
```

## Advanced Classifiers: Detecting Semantics In Images​

Imagine you would like to build a binary classifier to distinguish whether there's a tiny white ball in the image or not. With Atlas, this is just as easy as the process we followed above.

```
a tiny white ball
```

### Store Data In Atlas​

We load the Imagenette dataset from Hugging Face and store it in Atlas.

```
from nomic import AtlasDatasetfrom datasets import load_datasetfrom tqdm import tqdmid2label = {   "0": "tench",   "1": "English springer",   "2": "cassette player",   "3": "chain saw",   "4": "church",   "5": "French horn",   "6": "garbage truck",   "7": "gas pump",   "8": "golf ball",   "9": "parachute"}dataset = load_dataset('frgfm/imagenette', '160px')['train']images = dataset["image"]labels = dataset["label"]metadata = [{"label": id2label[str(label)]} for label in tqdm(labels, desc="Creating metadata")]dataset_identifier = "imagenette10k" # to create the dataset in the organization connected to your Nomic API key# dataset_identifier = "<ORG_NAME>/imagenette10k" # to create the dataset in other organizations you are a member ofatlas_dataset = AtlasDataset(    dataset_identifier,     description='10k 160px Imagenette images')atlas_dataset.add_data(    blobs=images,    data=metadata)atlas_map = atlas_dataset.create_index(    topic_model={"build_topic_model": False})
```

### Building a Classifier​

As above, open the vector search modal in the Atlas dashboard and search for a tiny white ball to see the images that match the query.

```
a tiny white ball
```

#### Determine classifier threshold​

Drag the slider to the right to see the images that are most similar to the query.

We see that for a threshold of 0.058, most of the images are golf balls!
The higher the number the more similar the image is to the text query.

```
0.058
```

#### Using embeddings for custom classifiers in Python​

We use the same ImageClassifierFromTextQuery defined above to build our classifier in Python:

```
ImageClassifierFromTextQuery
```

```
classifier = ImageClassifierFromTextQuery(text_query="a tiny white ball", threshold=0.058)
```

#### Testing the Classifier​

Let's test the classifer on some data. First, let's check that the classifier works as expected on the Imagenette dataset.

We will use these 5 test images:

- Python
- Output
```
print(f"Loading dataset")dataset = load_dataset('frgfm/imagenette', '160px')['train']# first three should return True, last two should return Falseids = [7450, 6828, 7464, 2343, 3356]images = [dataset[i]["image"] for i in ids]print(f"Predicting")predicitions = classifier.predict(images)assert predicitions == [True, True, True, False, False], f"Predictions should be [True, True, True, False, False], got {predicitions=}"for i, pred in enumerate(predicitions):    print(f"Prediction for image {ids[i]}: {pred}")
```

```
Building classifierLoading datasetPredictingPrediction for image 7450: TruePrediction for image 6828: TruePrediction for image 7464: TruePrediction for image 2343: FalsePrediction for image 3356: False
```

We see that the classifier correctly predicts images with high similarity to the text query as True and images with low similarity as False as shown in the Nomic Atlas interface.

```
True
```

```
False
```

#### Generalizing To New Data​

Now, let's test the classifier on a new dataset. We will use the Sports Classification dataset to classify images of baseball, cricket, and hockey.

```
sport_dataset = load_dataset('nihaludeen/sports_classification', split="train")sport_images = sport_dataset["image"]predictions = classifier.predict(sport_images)
```

You should see the classifier return True for images that contain a tiny white ball like this:

```
True
```

and false for other images that do not contain a tiny white ball like this:

## Conclusion​

In this cookbook, we showed you how to use Nomic Atlas to build an image classifier leveraging the power of multimodal semantic search.
Using Atlas, we were able to visualize the decision boundary of the text query across our image dataset and find an appropriate threshold for our classifier.
From there, we showed you how you can expand your classifier to any new image dataset you have.

To run the full script, you can find it on our github.

- Why This Cookbook Guide Matters
- Cookbook Outline
- Getting StartedPrerequisitesInstall Required Libraries
- Prerequisites
- Install Required Libraries
- Simple Classifiers: Cats & DogsStore Data In AtlasBuilding a Classifier
- Store Data In Atlas
- Building a Classifier
- Advanced Classifiers: Detecting Semantics In ImagesStore Data In AtlasBuilding a Classifier
- Store Data In Atlas
- Building a Classifier
- Conclusion
