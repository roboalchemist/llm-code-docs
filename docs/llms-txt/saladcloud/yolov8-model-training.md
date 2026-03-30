# Source: https://docs.salad.com/container-engine/tutorials/computer-vision/yolov8-model-training.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Training a custom YOLOv8 model

> In this blog, we showcase training three distinct custom YOLOv8 models on SaladCloud within an hour for just $1.

*Last Updated: October 10, 2024*

### Introduction: Training a Custom YOLO Model for Logo Detection\*\*

In the realm of AI and machine learning, the power of customization cannot be overstated. Our previous article covered
deploying a pre-trained YOLOv8 model using SaladCloud's infrastructure. During that journey we did real-time object
tracking and analysis. In the landscape of AI and machine learning, the ability to train custom models for specific
tasks opens up a world of possibilities. And now, we're taking a step further: training a custom YOLO (You Only Look
Once) model using SaladCloud .

Running inference with pre-trained models, as we've previously seen, can be relatively less dependent on computational
resources. However, when it comes to training custom models that changes significantly. Training is much more
GPU-intensive, time-consuming, and often pretty expensive. This is particularly true for deep learning models used in
object detection, where numerous parameters are fine-tuned over extensive datasets. The process involves repeatedly
processing large amounts of data, making heavy use of GPU resources for extended periods. This intensity not only
extends the training duration but also adds to the overall cost, especially in cloud-based environments.

Acknowledging these challenges, our current project aims to train several YOLO models using different base models. We
will be focusing on three critical aspects:

1. **Processing Times**: We will monitor the duration taken by each model to train, providing insights into the
   efficiency of different YOLO configurations.
2. **Cost Analysis**: Given that training is a resource-heavy task, understanding the financial implications is crucial.
   We will compare the costs of training each model on SaladCloud's platform, offering a clear perspective on the
   budgetary requirements for such tasks.
3. **Model Accuracy**: The ultimate test of any model is its performance. We will evaluate the accuracy of each trained
   model, understanding how the training complexity translates into detection precision.

**Dataset: The Foundation of Our Model**

In our particular example we will use the ["Flickr Logos 27" dataset](http://image.ntua.gr/iva/datasets/flickr_logos/),
but we will make sure that using any other dataset is easy and straightforward. In the end of our project we want to
have a model that will be able to detect particular logos in videos and pictures.

High-level overview of "Flickr Logos 27" dataset:

It comprises 810 images spread across 27 logo classes. All images are annotated with bounding boxes.

Brands included in the dataset: Adidas, Apple, Google, Coca Cola, Ferrari and others.

**Preparing for YOLOv8: Structuring the Dataset**

In order to train a YOLOv8 model our dataset needs to be in a format that the model can understand and learn from
effectively.

We need to organize our training and validation images and labels like this:

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/8a17a88-Screenshot_2023-11-26_144806.png?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=ab14f4f51884d021dc6cd5f4d696d642" data-og-width="389" width="389" data-og-height="178" height="178" data-path="container-engine/images/8a17a88-Screenshot_2023-11-26_144806.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/8a17a88-Screenshot_2023-11-26_144806.png?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=5fbcaf8733e1db6536367d4afd26a8b4 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/8a17a88-Screenshot_2023-11-26_144806.png?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=ae1fe62ae40aaa588d444b94ba67f097 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/8a17a88-Screenshot_2023-11-26_144806.png?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=1a7685122e0888e382ec631909df017a 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/8a17a88-Screenshot_2023-11-26_144806.png?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=730cb72d40fc144ff5ed3cd88d6e9260 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/8a17a88-Screenshot_2023-11-26_144806.png?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=4a60609ac9f399eefcf3801bf1a945b6 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/8a17a88-Screenshot_2023-11-26_144806.png?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=95d926e1b31df97ab930892ad3f04874 2500w" />

We also need a dataset YAML to define paths to the images and the class names:

```java yaml theme={null}
path: /app/training/training # Dataset root path
test: images/test
train: images/train
val: images/val

names:
  0: Adidas
  1: Apple
  ...
```

Each image in our dataset will be accompanied by a `.txt` file in YOLO format, detailing the objects present. These
annotations are crucial, as they provide the model with the necessary information about the location and class of each
logo in an image:

```java txt theme={null}
9 0.498 0.491 0.982 0.927
```

Preparing data is said to be 90% of success in Data Science, so make sure your dataset has the right format. Every
dataset is very specific, so we will not go too deep in the dataset we used. We had to shuffle the files a little and
create a yaml file based on our data. Scripts that we used to do that are in the
[git repo](https://github.com/SaladTechnologies/yolov8-training-on-salad).

Since we want to make our process as easy and persistent as possible we will copy our training data into azure file
share with the following directory structure where “training“ is the name of the fileshare:

```java txt theme={null}
training/{dataset_name}/images/

training/{dataset_name}/labels/

training/{dataset_name}/yolo8.yaml
```

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/093038e-Screenshot_2023-11-26_155043.png?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=c04d45c9cc682601b32a06c07f63e555" data-og-width="569" width="569" data-og-height="167" height="167" data-path="container-engine/images/093038e-Screenshot_2023-11-26_155043.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/093038e-Screenshot_2023-11-26_155043.png?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=ba0ad457dc4873dd6bbed306815c026b 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/093038e-Screenshot_2023-11-26_155043.png?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=b2437b4175c0af07430f7e93530a8238 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/093038e-Screenshot_2023-11-26_155043.png?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=c0d3285128ee0626260dc82b65b47bdf 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/093038e-Screenshot_2023-11-26_155043.png?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=981f0bc98bad21fe14cf1131cf3d35b1 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/093038e-Screenshot_2023-11-26_155043.png?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=9d40b0e6c7ffe3b4746abcc82127ecd2 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/093038e-Screenshot_2023-11-26_155043.png?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=845e91ae87cbf71a5a58db51f66d26d1 2500w" />

Solution Architecture:

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/b6dfaeb-Training_Architecture.drawio.png?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=73becf5241e785042bacd19b8181c143" data-og-width="691" width="691" data-og-height="325" height="325" data-path="container-engine/images/b6dfaeb-Training_Architecture.drawio.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/b6dfaeb-Training_Architecture.drawio.png?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=c3b6fce8923fa2bb2cd80ac9b947a657 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/b6dfaeb-Training_Architecture.drawio.png?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=c6735a9736c31967cd42f31bbd139aae 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/b6dfaeb-Training_Architecture.drawio.png?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=c22b31d48ca2c4edd16dd0e7cf080c32 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/b6dfaeb-Training_Architecture.drawio.png?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=f1aba65e60264d66be4258afe819d4d0 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/b6dfaeb-Training_Architecture.drawio.png?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=0a22cc1ac291ff102697a69131df838b 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/b6dfaeb-Training_Architecture.drawio.png?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=e8f0fd39760fec0d83e706a50a008853 2500w" />

**Training Different YOLOv8 Models**

In our project we train 3 variants of the YOLOv8 model:

1. **YOLOv8 Nano (n)**
2. **YOLOv8 Small (s)**
3. **YOLOv8 Medium (m)**

Each model offers different performance and complexity trade-offs, making them suitable for various use cases.

**Hyperparameter Considerations**

Training models requires careful selection of hyperparameters. Here are the choices we’ve made for our training:

* **Epochs**: We will train each model for 50 epochs.
* **Batch Size**: To ensure consistency and fairness in our comparison, all models will be trained with a batch size
  of 8.
* **Image Resolution**: We will go with the default resolution of 640
* **Workers** : 1

**Sample Training Command with YOLOv8 Nano**

Here's how you can initiate training using the YOLOv8 model with Python:

```python  theme={null}
from ultralytics import YOLO
# Load the YOLOv8 Nano model
model = YOLO('yolov8n.pt')
# Start the training process
results = model.train( data='yolo8.yaml', imgsz=640, epochs=10, batch=8, name='yolov8n_custom' )
```

**Explanation of Command Line Arguments**

* **model**: This specifies the YOLO model to be used. In our example, we use `yolov8n.pt`, which refers to the YOLOv8
  Nano model.
* **imgsz (Image Size)**: Defines the resolution of the input images for training. The default value is 640, but this
  can be adjusted based on the dataset and GPU capabilities.
* **data**: The path to the YAML file containing the dataset configuration. This file includes paths to training,
  validation, and test image directories, and the class names.
* **epochs**: This determines the number of complete passes through the training dataset. We've set it to 10 for our
  example, but this can vary based on the size of your dataset and the desired level of model convergence.
* **batch (Batch Size)**: Indicates the number of training samples to work through before updating the internal model
  parameters. The value depends on the available GPU memory; a higher batch size generally requires more memory.
* **name**: The name assigned to the training run. This is useful for organizing and identifying results, especially
  when conducting multiple experiments.

We will replace all the values with arguments so that we can easily switch them during deployment to Salad.

We will also run the validation command in order to check our model performance:

```python  theme={null}
model.val()
```

### Resuming Interrupted Trainings

In the world of deep learning, resuming training from a saved state is a crucial feature. This feature is particularly
beneficial when training is unexpectedly interrupted or when you wish to continue refining a model with additional data
or more training epochs.

YOLO simplifies the process of resuming training. When resuming, the model not only reloads the weights from the last
saved checkpoint but also restores the optimizer state, learning rate scheduler, and the current epoch number. This
seamless integration ensures that training can continue precisely from where it was paused.

To resume training you simply need to use the `resume` argument within the training method and provide the path to the
`.pt` file containing the partially trained model weights. We will slightly modify the code checking if the intermediate
weight is available and start from where it stopped:

```python  theme={null}
last_model_path = f"runs/detect/{output_model_name}/weights/last.pt"
if os.path.isfile(last_model_path):
    model = YOLO(last_model_path)
    model.train(resume=True)
```

Keep in mind that checkpoints in Ultralytics YOLO are automatically saved at the end of every epoch, or at a fixed
interval if the `save_period` argument is used. Therefore, to successfully resume a training session, you need to have
at least one completed epoch.

### Creating a Persistent Training Environment with SaladCloud and Azure File Shares

To ensure a smooth and uninterrupted training process on Salad, especially when dealing with containerized environments,
it's crucial to have a persistent storage solution. Azure File Shares provide an ideal way to maintain and access
training data and model weights across different container sessions. In our setup, we utilize two Azure File Shares:
`runs` and `training`.

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/7ba7f70-Screenshot_2023-11-26_165430.png?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=f3b9358a2ddad6cf81881e2e3c4a3a1e" data-og-width="478" width="478" data-og-height="95" height="95" data-path="container-engine/images/7ba7f70-Screenshot_2023-11-26_165430.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/7ba7f70-Screenshot_2023-11-26_165430.png?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=366d108f94aad3be0f496537b2ac0e53 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/7ba7f70-Screenshot_2023-11-26_165430.png?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=7e983a5e389030ebf46fdfc572a7c6c6 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/7ba7f70-Screenshot_2023-11-26_165430.png?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=130526f7fd9e5ba4e0b69ca7661f090a 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/7ba7f70-Screenshot_2023-11-26_165430.png?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=256b597d8b6c0920f0dea38767272b57 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/7ba7f70-Screenshot_2023-11-26_165430.png?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=3e22b1d339bfce449d861cbf3408bd79 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/7ba7f70-Screenshot_2023-11-26_165430.png?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=7e00f0dda85b5c07b3c3b5eb3d1739b6 2500w" />

**Directory Structure and Data Management**

* **Training Directory**: Within the `training` file share, we have a sub-directory named `{dataset_name}`. This
  organization allows us to switch between different datasets efficiently, facilitating the training of various models
  without hassle.
* **Synchronizing Data**: To manage and synchronize our training data and weights, we'll employ a bash script as the
  entry point for our `train.py`. This script will automate several crucial tasks, ensuring our training process is both
  efficient and consistent.

**Process workflow**

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/529d48a-workflow.drawio.png?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=a956571b7ce291bf94e52da5ba78f116" data-og-width="512" width="512" data-og-height="491" height="491" data-path="container-engine/images/529d48a-workflow.drawio.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/529d48a-workflow.drawio.png?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=0c7207762a5156e6b3e987f2c8c3a3ee 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/529d48a-workflow.drawio.png?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=f38c62ea1d497fd359227abbd4a2ecbd 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/529d48a-workflow.drawio.png?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=3a3d512c7f4167635b01510311d940ae 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/529d48a-workflow.drawio.png?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=9afbedfe0c81608339e4e8540fb3b70f 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/529d48a-workflow.drawio.png?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=eb439f61c1529602df19522fe6c5e262 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/529d48a-workflow.drawio.png?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=28acaf9d3c5b5834c98e38e6978e3607 2500w" />

**Functionality of the Bash Script**

1. **Download Training Data**: The script will pull all necessary training data, including images, labels, and the
   YOLOv8 YAML configuration file, into our container.
2. **Retrieve Weights from Previous Runs**: It will download weights from previous training runs to the container,
   ensuring continuity.
3. **Handle Training Process**:
   * The script initiates the `train.py`.
   * If a `runs` folder with the same model output name exists, the training resumes. Otherwise, it starts a new
     training session with the base model.
4. **Regular Sync to Azure**: Every minute, the script will copy the contents of the `runs` folder from the container to
   Azure File Share, maintaining a backup and allowing for process continuity.
5. **Monitoring Training Completion**:
   * Upon the completion of `train.py`, a `done.txt` file is created.
   * The script continuously checks for this file and, once detected, terminates the process.

## Training Results:

To ensure a fair and uniform comparison across different YOLOv8 model trainings, we pick a consistent set of hardware
and training parameters. We chose the RTX 4080 (16 GB) GPU for all our experiments, priced at a very low rate of \$0.28
per hour. Additionally, each training was conducted over 50 epochs, with a batch size of 8, and an image resolution
of 640.

#### YOLOv8 Nano Model Training: Efficiency and Speed

The first model in our comparative study is the YOLOv8 Nano, renowned for its compact yet powerful architecture. With
3.2 million parameters, it is the smallest model in the YOLOv8 family, yet capable of real-time performance, even on
CPU-based systems.

**Duration of Training**: Training session for the YOLOv8 Nano model was completed in just about 10 minutes. Which gets
us to about 5 cents for training a model.

**Training results**: once our model is trained we can find all the weight along with training and validation results in
our Azure storage. We will first check the confusion matrix:

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6f5a5e3-confusion_matrix_normalized.png?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=b34788f89b8a6d14ad0a941189d86abd" data-og-width="3000" width="3000" data-og-height="2250" height="2250" data-path="container-engine/images/6f5a5e3-confusion_matrix_normalized.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6f5a5e3-confusion_matrix_normalized.png?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=2c56e7fb4d37fc6714ee6d47a2136393 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6f5a5e3-confusion_matrix_normalized.png?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=d318bc7429aaa1b8b73acd5cbfb8831e 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6f5a5e3-confusion_matrix_normalized.png?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=dbd6a4c9151a78024e8d02e3b092ff6e 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6f5a5e3-confusion_matrix_normalized.png?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=3e19d8c72da261f912a73b1136c3fb72 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6f5a5e3-confusion_matrix_normalized.png?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=bc2945fb8f7456ff890bb2c58b15131f 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6f5a5e3-confusion_matrix_normalized.png?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=129617afc0271443248ff4cb637b2265 2500w" />

We can see that some of the labels are being detected pretty good, but a few are positively detected in less than half
of the scenarios.

<img src="https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/d5c6c5c-results.png?fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=eefc2d80364a61f918eac5ac3a6cb8aa" data-og-width="2400" width="2400" data-og-height="1200" height="1200" data-path="container-engine/images/d5c6c5c-results.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/d5c6c5c-results.png?w=280&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=1bf992fd2ff5459f0528594deff52fe8 280w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/d5c6c5c-results.png?w=560&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=4688f08fdcc391fa2567543a653645c2 560w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/d5c6c5c-results.png?w=840&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=e1f3a229bc218149569d9c723b5b0d49 840w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/d5c6c5c-results.png?w=1100&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=6a04a2f25e1180a749d0493a84cf1716 1100w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/d5c6c5c-results.png?w=1650&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=ceef1e77e086dcae4da7f7617fb7f8d3 1650w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/d5c6c5c-results.png?w=2500&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=1de26b4d2e5b3ebfd2116614b8ece8cb 2500w" />

Here we can see what the labels on a picture are and what we predicted with our trained model:

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/16f170b-val_batch0_labels.jpg?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=2d5b5d80251bcc88fbad49ec22762d49" data-og-width="1920" width="1920" data-og-height="1192" height="1192" data-path="container-engine/images/16f170b-val_batch0_labels.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/16f170b-val_batch0_labels.jpg?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=c031e3fdfc19a210cbe41575727aac4b 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/16f170b-val_batch0_labels.jpg?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=5a93bd48b2cd0f573cf3c6cf79b6c9b1 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/16f170b-val_batch0_labels.jpg?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=fb2314e7ba153f61d89a88576644f796 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/16f170b-val_batch0_labels.jpg?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=9018e2d00d63c3b31cfdbb6ddbc08ff6 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/16f170b-val_batch0_labels.jpg?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=c7fab6d85c8a5312639ef3c7314e4fa4 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/16f170b-val_batch0_labels.jpg?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=6cb6e1b64cf58a9855a6b4ac05ef9cbc 2500w" />

<img src="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e29a1f3-val_batch0_pred.jpg?fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=598e20a17110e698d04b68fb1358d6ab" data-og-width="1920" width="1920" data-og-height="1192" height="1192" data-path="container-engine/images/e29a1f3-val_batch0_pred.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e29a1f3-val_batch0_pred.jpg?w=280&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=99fc8d643abdf0a38ae093ff8be54843 280w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e29a1f3-val_batch0_pred.jpg?w=560&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=2252bc7512fb8df26939c30ebf178f17 560w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e29a1f3-val_batch0_pred.jpg?w=840&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=73ecbd74c908500264aabf599917f382 840w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e29a1f3-val_batch0_pred.jpg?w=1100&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=27b27707bf30da9d241da9b743ebafca 1100w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e29a1f3-val_batch0_pred.jpg?w=1650&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=f35c40fd4ff0ad089bfbcf96e52600b4 1650w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/e29a1f3-val_batch0_pred.jpg?w=2500&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=ea9968fdc28b73f0448b959f44c9ac43 2500w" />

#### YOLOv8 Small Model Training:

**Duration of Training**: Training session for the YOLOv8 Small model was completed in about 15 minutes. **Trainings
Results**:

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/69e0885-confusion_matrix_normalized_1.png?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=cbcc90844754c686ac40c9795dc8b844" data-og-width="3000" width="3000" data-og-height="2250" height="2250" data-path="container-engine/images/69e0885-confusion_matrix_normalized_1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/69e0885-confusion_matrix_normalized_1.png?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=acc954b2cd8f61e96392230b66d46e7f 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/69e0885-confusion_matrix_normalized_1.png?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=306d085f07ad142cd5ad496ffa491c03 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/69e0885-confusion_matrix_normalized_1.png?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=620f37659a8072bc15030302685c8346 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/69e0885-confusion_matrix_normalized_1.png?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=1d17ec5c7949478e98d08706224d1a2e 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/69e0885-confusion_matrix_normalized_1.png?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=731078c4ccdc30b5e38df317bbc11026 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/69e0885-confusion_matrix_normalized_1.png?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=a93f8a0df5fb52f2bd7e7c646b16d526 2500w" />

We can see that the model performs better

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/7caac82-results.png?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=d3f0a7e9547a30367c56bec360088e0e" data-og-width="2400" width="2400" data-og-height="1200" height="1200" data-path="container-engine/images/7caac82-results.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/7caac82-results.png?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=568f2d9ffd26a7e0e14e8b8ffaa7e647 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/7caac82-results.png?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=a12a4e99ad6d5fa099cd7e3f385887d5 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/7caac82-results.png?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=232d41a0d48fb8565eb8fae523487c9a 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/7caac82-results.png?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=d946bdd0145055f8264128152d73bf60 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/7caac82-results.png?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=256225d6f7a2310183d298f32b1e07ae 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/7caac82-results.png?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=819d3c4be83644b1afa788adb860b998 2500w" />

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4ebc600-val_batch0_pred.jpg?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=86935e93a49753d207a9ef7ac7c9a65a" data-og-width="1920" width="1920" data-og-height="1192" height="1192" data-path="container-engine/images/4ebc600-val_batch0_pred.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4ebc600-val_batch0_pred.jpg?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=34d8bf0a61740351acef1803383c437b 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4ebc600-val_batch0_pred.jpg?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=82c8dd4e90d69c84ea9eb0df348decb7 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4ebc600-val_batch0_pred.jpg?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=81964899dc90cfafcf0a2a649be67c1c 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4ebc600-val_batch0_pred.jpg?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=cdce533a16ddcc819ea7fd0bc4d48a2d 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4ebc600-val_batch0_pred.jpg?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=c04d94340b743d90443bbfd94e041b0c 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4ebc600-val_batch0_pred.jpg?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=27167eab28075106b0986513d2f75ba5 2500w" />

#### YOLOv8 Medium Model Training:

**Duration of Training**: Training session for the YOLOv8 Medium model was completed in about 40 minutes.

This time we stopped our process and allocated it to the other machine to check if it can start from the last weights we
have and it worked successfully.

**Trainings Results**:

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1402547-confusion_matrix_normalized.png?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=c08d629dbde6e77347bef8e0db600559" data-og-width="3000" width="3000" data-og-height="2250" height="2250" data-path="container-engine/images/1402547-confusion_matrix_normalized.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1402547-confusion_matrix_normalized.png?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=30b337c7ad7de2c6f015c988f8c1d995 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1402547-confusion_matrix_normalized.png?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=0c45f7b2f9bbc3a2a7ce6e8ae7041eb8 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1402547-confusion_matrix_normalized.png?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=2f992043629c5d496cb35225d93971cc 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1402547-confusion_matrix_normalized.png?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=7cee4dfde6e11ad39109b2a3752c5bec 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1402547-confusion_matrix_normalized.png?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=5970c3f62ff08108ccc98d02771401c8 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1402547-confusion_matrix_normalized.png?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=2f99c32f297d3322c67436b339a43d1d 2500w" />

<img src="https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/d8d25f3-results.png?fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=7cd047a0e84bfcdf5d81592cb0ce82ca" data-og-width="2400" width="2400" data-og-height="1200" height="1200" data-path="container-engine/images/d8d25f3-results.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/d8d25f3-results.png?w=280&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=7976fe3b3e59ac879e54fdd91e61f9cd 280w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/d8d25f3-results.png?w=560&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=f1e27fb519bcc82924a30f30bc2b4f4e 560w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/d8d25f3-results.png?w=840&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=d30afab083731f6119340a8c71c84eaa 840w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/d8d25f3-results.png?w=1100&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=80d690b227a3023d98b2b2888340e509 1100w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/d8d25f3-results.png?w=1650&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=371d6df5d1588f939ec8563402e8b07a 1650w, https://mintcdn.com/salad/Q-b7u7-avMFxB0Ze/container-engine/images/d8d25f3-results.png?w=2500&fit=max&auto=format&n=Q-b7u7-avMFxB0Ze&q=85&s=120a8fe5c2a2629c64e1741049907e30 2500w" />

<img src="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/ef883c8-val_batch0_pred.jpg?fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=6dfca67cbd22e7cab8f63b728ea7e823" data-og-width="1920" width="1920" data-og-height="1192" height="1192" data-path="container-engine/images/ef883c8-val_batch0_pred.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/ef883c8-val_batch0_pred.jpg?w=280&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=d3ddf29113abaea461e47a23fd5565a4 280w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/ef883c8-val_batch0_pred.jpg?w=560&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=a7d986a8571eb3bc8e19d3f3c16101f1 560w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/ef883c8-val_batch0_pred.jpg?w=840&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=186dab5af73943bf60d8384a4b4ce3df 840w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/ef883c8-val_batch0_pred.jpg?w=1100&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=6e20632d83fc1102023d261310e53125 1100w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/ef883c8-val_batch0_pred.jpg?w=1650&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=849058df4d533bcfb94c8d4987568cd6 1650w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/ef883c8-val_batch0_pred.jpg?w=2500&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=8c27a2ba8dc9520553f96a5c866ebd4e 2500w" />

We can see that bigger models give us better results.

## Using custom model in the real life:

We will now upload the medium model into our inference code and run it on a Coca-Cola video. To do that we just need to
specify the model path in our script. Check out our previous article and step by step guide on how to deploy an
inference using Salad

```python  theme={null}
# Load the model
model = YOLO("yolob8m-custom.pt")
results = model.track(image, persist=True)
```

Let’s check the results:

<img src="https://mintlify.s3.us-west-1.amazonaws.com/salad/container-engine/images/bd1dfb4-2023-11-29-16-00-34.gif" />

As a result we can see that we not only can use our custom trained model on images, but even on videos adding tracking
possibilities.

### Conclusion: Streamlined Training and Deployment of YOLOv8 Models on SaladCloud

In a concise and cost-effective operation, we successfully trained three YOLOv8 models of varying sizes on a custom
dataset and put the medium model to the test in real-world scenario. Attaining these training results in approximately
40 minutes and at a cost of only about a quarter of a dollar on SaladCloud highlights the efficiency and
cost-effectiveness of advanced model training using SaladCloud's environment. Training custom computer vision models has
never been that accessible.
