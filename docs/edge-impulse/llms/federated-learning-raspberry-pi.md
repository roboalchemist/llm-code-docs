# Source: https://docs.edgeimpulse.com/projects/expert-network/federated-learning-raspberry-pi.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# A Federated Approach to Train and Deploy Machine Learning Models

Created By: Solomon Githu

Public Project Link: [https://studio.edgeimpulse.com/public/279823/latest](https://studio.edgeimpulse.com/public/279823/latest)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img1_cover-image.png?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=07f5cd731bd7d0d3da6e7b9739d25593" width="1600" height="900" data-path=".assets/images/federated-learning/img1_cover-image.png" />
</Frame>

## Introduction

In Machine Learning (ML), we create a model that is trained to do a particular task like object detection, anomaly detection, or prediction. To develop a model, we normally collect data on one computer (possibly in the cloud) and then we train the model on the computer with the centralized data. However, in some situations, using a centralized machine learning model may not be effective or efficient. In some situations, the data may be sensitive, not diverse, or too large for the available internet bandwidth making it unable to be uploaded to the central computer.

Federated Learning enables us to bring the model, to the data. For example, voice recognition and face recognition by Siri and Google Assistant are Federated Learning based solutions. In these cases, we do not want to send our voices or pictures to the cloud for training the model. Federated Learning works by training models locally on the devices using the data on the device. Once a model has been trained, a device uploads the new model updates to a server that aggregates model parameters from various devices and generates a global updated model. This global updated model can then be deployed to the devices for better Machine Learning task performance, and also continuous retraining of the model.

The approach of federated learning normally follows four major processes:

* A central server initializes a global model and its parameters are transferred to clients in each iteration
* Clients update their local model parameters by locally training a model
* The server gets model parameters from clients, aggregates them, and updates the global parameters
* The above steps are repeated until local and global parameters converge

There are several Open-Source Federated Learning frameworks that we can use. However, there are some factors that should be considered before selecting a Federate Learning framework. Some of these factors include:

* The supported Machine Learning frameworks
* Aggregation Algorithms - the most widely supported Federated Learning algorithm is Federated averaging (FedAvg). However, the specific algorithms offered by each framework may vary.
* The supported privacy methods, such as encryption
* The supported devices and operating systems
* Scalability - the complexity of adding your own model or aggregation algorithm

## Demonstration

To demonstrate Federated Learning, I simulated a situation where we want to identify if workers at a construction site are wearing safety equipment (hardhats). At each construction site, we have a surveillance camera that is monitoring the workers. The camera device will be taking an image of a person and determining if it sees a head or a hardhat.

<Frame caption="Head hardhat image">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img2_head-hardhat.png?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=c3e9521c044f204c3ddb48c2be7c4b27" width="1600" height="333" data-path=".assets/images/federated-learning/img2_head-hardhat.png" />
</Frame>

Some of the challenges in this use case are:

* how can we overcome sending sensitive photos of workers to the cloud?
* how can we overcome the need to send a lot of image data to a central server for training a model?
* how to acquire diverse data?

To solve the above challenges, I used [Flower framework](https://flower.dev/) to train a decentralized MobileNetV2 image classification model. Flower is easy to use, flexible, and they have a wide range of quickstart examples to help you get started. I used a Raspberry Pi 4 (with 4GB RAM) and a personal computer as the client devices in the Federated Learning system.

<Frame caption="Client devices">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img3_client-devices.png?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=b6e24662b36fef08ecce36c8714c5a3c" width="1600" height="333" data-path=".assets/images/federated-learning/img3_client-devices.png" />
</Frame>

There are 6 Federated Learning iterations where both the Raspberry Pi and the personal computer individually train a MobileNetV2 model, send updates to the server, and the server aggregates the model parameters. During the client's training process, each client uses a dataset, different from the other, to train the model. This helps us simulate a situation where we have different devices at different locations and therefore the data is different and more diverse.

For my demonstration, I chose the MobileNetV2 architecture since it is a lightweight neural network architecture that is designed to be efficient and fast, with less computation power requirements. In my previous tests, I trained an EfficientNetB0 model and it achieved almost the same performance as the MobileNetV2 model, but at the cost of a significantly longer training and classification time.

When the Federated Learning is complete, the server uses the [Edge Impulse Python SDK](/tools/libraries/sdks/studio/python) to profile the final global model for the Raspberry Pi. This profiling gives us an estimate of the RAM, ROM, and inference time of the model on a target hardware family like the Raspberry Pi. Finally, the new global model will also be uploaded to an Edge Impulse project and this enables us to deploy it to any device that can run it.

<Frame caption="FL server to Edge Impulse">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img4_fl-server-to-edge-impulse.png?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=944bd3beab883eed25a0660ff9c36c23" width="1600" height="667" data-path=".assets/images/federated-learning/img4_fl-server-to-edge-impulse.png" />
</Frame>

## Components and Hardware Configuration

Software components:

* Edge Impulse Studio account
* Python
* Edge Impulse for Linux

Hardware components:

* Personal Computer with Windows or Linux based Operating System
* Raspberry Pi 4 (recommended to use the 4GB RAM version) with Raspberry Pi OS
* Official Raspberry Pi 4 power adapter (recommended)
* Raspberry Pi V2 camera module

## Data Collection Process

I first started by sourcing images with people's heads and people wearing safety hats. I obtained my dataset from this [Public Edge Impulse project](https://studio.edgeimpulse.com/public/34898/latest). The project trains a MobileNetV2 SSD FPN-Lite 320x320 object detection model to identify heads and safety hats on an image. This project is a good demonstration of the classic Machine Learning approach where we train a centralized model with all the data on one computer. To get a better understanding of the project, please feel free to read the [project's write-up here](https://edgeimpulse.com/blog/enhancing-health-and-safety-in-industrial-environments-with-embedded-machine-learning).

The public project has a total of 583 images of people's heads and people wearing safety hats. I then split the images according to this:

* two folders with training and test images for two client devices
* one folder with test images for the server model testing during the Federated Learning
* one folder with test images that we can give to the final global model *after* the Federated Learning

<Frame caption="Dataset folders">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img5_screenshot-dataset-folders.png?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=792e0fe1c8223ecbcf12d8f206174d86" width="524" height="313" data-path=".assets/images/federated-learning/img5_screenshot-dataset-folders.png" />
</Frame>

## Training the Model, the Federated Way

For the Federated Learning pipeline, I created [this GitHub Repository](https://github.com/SolomonGithu/tensorflow_federated_learning_and_edge_impulse_model_deployment/tree/main) that has the dataset and Python scripts for the server and client devices. To follow along as I describe how to run the Federated Learning system, start by cloning the repository on the device that will run as the server. For the client devices, we only need to copy to them the `datasets` folder, `requirements_client.txt` and `client.py`. You \_could\_clone the repository on the client devices, but this will load unnecessary files on them.

First, we need computers for the server and clients.  You can also use the same computer as both a server and client, provided the computer has enough resources to do that. The minimum number of required clients is two for the Federated Learning to start. This minimum number can be modified in the `server.py` code, but remember to also modify the `client.py` code to load datasets for the additional clients.

I decided to use my personal computer as the server and also as one client device. For the other client device, I decided to use a Raspberry Pi 4 with 4GB of RAM.

<Frame caption="A Raspberry Pi 4">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img6_raspberrypi-4-and-v2-camera.jpg?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=292e2817aa4157efb8cf29b0092b4afb" width="1600" height="900" data-path=".assets/images/federated-learning/img6_raspberrypi-4-and-v2-camera.jpg" />
</Frame>

> In my test with Raspberry Pi 3's running as the client devices, they managed to train a model but failed at the model evaluation process. This can be related to the fact that the Raspberry Pi 3 is more resource constrained than the Raspberry Pi 4, with a less powerful CPU and less RAM. Using the `top` command on the Raspberry Pi 3's showed that the CPU and RAM usage were at max capacity during the training process. When it reached the evaluation process, the RAM usage decreased to around 80%, CPU usage dropped to around 40%, but then the Federated Learning framework disconnected the Raspberry Pi 3 client devices. The Raspberry Pi 3's also showed 92% CPU usage and 45% RAM usage when they were connecting as the client devices.

Next, we need to install dependencies on the devices. The difference between the server and client dependencies is that the server computer uses the Edge Impulse Python SDK for profiling and deploying the model. We can install dependencies on the server computer by running the command below on a terminal or a Command Prompt (CMD):

```
pip install -r requirements_server.txt
```

To install the dependencies on the Raspberry Pi 4 running as a client device, we use the command below:

```
pip install -r requirements_client.txt
```

<Frame caption="Installing dependencies">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img7_screenshot-installing-dependencies.png?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=d242e4a5780134bf942acc392085a959" width="1352" height="724" data-path=".assets/images/federated-learning/img7_screenshot-installing-dependencies.png" />
</Frame>

Next, we need to update the `server_address` value in both `server.py` and `client.py` with the IP address of the device running as the server. If you get an error message from `server.py` that says `_ERROR_MESSAGE_PORT_BINDING_FAILED`, change the server's port to another one that is available.

<Frame caption="Server_address variable">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img8_screenshot-server-address-variable.png?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=f7fa3216eb08060996fc9907625c5b65" width="445" height="62" data-path=".assets/images/federated-learning/img8_screenshot-server-address-variable.png" />
</Frame>

Afterwards, we need to get an [API key for an Edge Impulse project](/apis/studio#api-key). To do this, we can create a new project in the Edge Impulse Studio and then copy its API key. We need to paste the API key to the `ei.API_KEY` variable in `server.py`.

<Frame caption="Edge Impulse API keys">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img9_screenshot-ei-api-keys.png?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=43418f7409275575170513e191170433" width="1366" height="768" data-path=".assets/images/federated-learning/img9_screenshot-ei-api-keys.png" />
</Frame>

We can now run the Federated Learning system. I first start the server on my personal computer by running `python server.py`. The server will load the test images, initialize the global model parameters, evaluate the initial model's parameters, and then wait until at least two clients join before starting the Federated Learning.

<Frame caption="Running server.py">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img10_screenshot-server-started.png?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=af41d52a295f5f842eb6f9a1510249c9" width="1366" height="730" data-path=".assets/images/federated-learning/img10_screenshot-server-started.png" />
</Frame>

Next, I start one client on my personal computer by running `python client.py --client_number=1` in a Command Prompt (CMD). When running the client scripts we use the argument `client_number` to enable the script to load different datasets for each client using the two folders with the client's dataset.

<Frame caption="Running client 1">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img11_screenshot-starting-client-1.png?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=25addae7925cbe713f821f55509243c5" width="691" height="279" data-path=".assets/images/federated-learning/img11_screenshot-starting-client-1.png" />
</Frame>

I then start the second client on the Raspberry Pi 4, by running the command `python client.py --client_number=2`.

<Frame caption="Running client 2">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img12_screenshot-starting-client-2.png?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=f014ef797f27c6f526c1b6bef33b3592" width="1366" height="350" data-path=".assets/images/federated-learning/img12_screenshot-starting-client-2.png" />
</Frame>

Once the two clients have connected, the Federated Learning will start. Each client will load a MobileNetV2 model, train the model using the train data, evaluate the model using the test data, and then send model updates to the server. In each Federated Learning iteration, the clients train a model with 20 epochs and a batch size of 8. The sever then aggregates the model's parameters from the updates sent by the clients, and then updates the initial model with the new parameters. This process continues six times, and then the Federated Learning will be completed.

<Frame caption="Clients logs">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img13_screenshot-fl-on-clients.png?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=1d55e987e2991ec8980c7c78992fbba1" width="1362" height="726" data-path=".assets/images/federated-learning/img13_screenshot-fl-on-clients.png" />
</Frame>

<br />

<Frame caption="Server FL logs">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img14_screenshot-fl-on-server.png?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=06a278533d10bd312a0c93f9b07b321f" width="1362" height="736" data-path=".assets/images/federated-learning/img14_screenshot-fl-on-server.png" />
</Frame>

Finally, when the Federated Learning is complete, I added some code on the server script to test the final global model with the test images that were not used during the Federated Learning. In the server's logs, we can see that the global model gives an accuracy of 1.0 in all the Federated Learning iterations. This, however, does not suggest that our model is perfect. Our dataset is still relatively small with only 415 images, equally divided for the two client's training dataset. Also, since this is transfer learning, our head and hardhat images are not very complex objects and the pre-trained model may require a bit of fine-tuning to make it learn the new task.

<Frame caption="Server testing model">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img15_screenshot-server-testing-model.png?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=7a3cfa8b0426033f307bfc6a632a8e69" width="1089" height="177" data-path=".assets/images/federated-learning/img15_screenshot-server-testing-model.png" />
</Frame>

After testing the model, the server script then uses the [Edge Impulse Python SDK](/tools/libraries/sdks/studio/python) to profile the model for the Raspberry Pi. This profiling gives us an estimate of the RAM, ROM, and inference time of our model on the Raspberry Pi. We can see the performance estimates for the Raspberry Pi in the screenshot below. Also, during this profiling, the final global model will be sent to the Edge Impulse project.

<Frame caption="Edge Impulse profiling">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img16_screenshot-ei-profiling.png?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=c3682138910260dfe168f96c79261847" width="1087" height="575" data-path=".assets/images/federated-learning/img16_screenshot-ei-profiling.png" />
</Frame>

## Testing the Global Model

When we go to the Edge Impulse project, we will see "Upload model" under "Impulse design". This is because our final global model was uploaded to the project during profiling.

<Frame caption="Edge Impulse Studio Dashboard">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img17_screenshot-ei-studio-dashboard.png?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=92aae7709418877226e725ab3dca276a" width="1366" height="768" data-path=".assets/images/federated-learning/img17_screenshot-ei-studio-dashboard.png" />
</Frame>

We first need to configure some parameters on the Edge Impulse project. Click "Upload model" and a new interface will open on the right side of the page. Here, we need to select "Image (RGB)" for the model input since our model is using RGB images. Next, for the input scaling query, we select "Pixels ranging 0..255(not normalized)". Afterwards, we select "Classification" for model output since this is an image classification model. Finally, the output labels should be: head, hardhat. Click "Save model" to finish the configuration.

<Frame caption="Upload model Step 2">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img18_screenshot-ei-studio-step-2.png?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=7cc888aa2d67631cbde7b67845e460cb" width="1366" height="768" data-path=".assets/images/federated-learning/img18_screenshot-ei-studio-step-2.png" />
</Frame>

<br />

<Frame caption="Save model successful">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img19_screenshot-ei-studio-step-2-finished.png?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=a94dd9f2e13a1c4af2f3fb89a455b03d" width="1366" height="768" data-path=".assets/images/federated-learning/img19_screenshot-ei-studio-step-2-finished.png" />
</Frame>

Afterwards, we can upload a test image to see if the selections we made are correct. In this test image, we can see that even though person is occupying a relatively small area portion of the image, the model was able to correctly determine that this is a hardhat image.

<Frame caption="Model testing">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img20_screenshot-ei-studio-step-2-model-testing.png?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=55591806a6eeb739ab5e80ceab071977" width="1366" height="768" data-path=".assets/images/federated-learning/img20_screenshot-ei-studio-step-2-model-testing.png" />
</Frame>

Perfect! Now we have a Federated Learning model added to Edge Impulse.

We can use the [Model testing feature](/studio/projects/model-testing) on Edge Impulse to further test our model. Remember we had a fourth dataset folder for test images, that were not used during the Federated Learning system. First click "Data Acquisition", followed by clicking the "Upload data" icon.

<Frame caption="Upload data">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img21_screenshot-data-acquisition-upload-data.png?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=3bbad902b07186114ab21519230f4e5f" width="1366" height="768" data-path=".assets/images/federated-learning/img21_screenshot-data-acquisition-upload-data.png" />
</Frame>

A new interface will open. Here we can first choose "Select a folder" for the upload mode. Click "Choose files" and select the `dataset_test` directory on your computer from where you cloned the GitHub repository to. Next, select "Testing" for the upload category since we have already trained a model and therefore there is no need to have training data. Next, for **Label** we select "Leave data unlabeled". Finally, click "Upload data" and the images will be uploaded to the project. The uploaded images can be seen by going to "Test" in Data acquisition.

<Frame caption="Uploading images">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img22_screenshot-data-acquisition-uploading-images.png?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=2928e7c723fa862d7ec79a473f1020a5" width="1366" height="768" data-path=".assets/images/federated-learning/img22_screenshot-data-acquisition-uploading-images.png" />
</Frame>

<br />

<Frame caption="Test images">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img23_screenshot-data-acquisition-test-images.png?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=1447f8e7e9ffbe6e6740baa7aec01ae0" width="1366" height="768" data-path=".assets/images/federated-learning/img23_screenshot-data-acquisition-test-images.png" />
</Frame>

The last thing to do is to label the images. This label information describes what each image is, head or hardhat. The label information will also be used during the model testing by comparing the models output to the correct class (label). To label the images, first click the kebab menu (three dots menu) next to each item listed in the test data. Next, select "Edit label" and type the name of the class which the image belongs to: head or hardhat. Do this until all images have been labelled.

<Frame caption="Kebab menu">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img24_screenshot-kebab-menu.png?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=a458fa3df55e7a57c19ff512336a4376" width="1366" height="768" data-path=".assets/images/federated-learning/img24_screenshot-kebab-menu.png" />
</Frame>

<br />

<Frame caption="Labeling images">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img25_screenshot-labeling-images.png?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=cd208741d311e48555b9d1ea1c15b146" width="1366" height="768" data-path=".assets/images/federated-learning/img25_screenshot-labeling-images.png" />
</Frame>

Finally, when all the images have been labeled, we can click "Model testing" and afterwards "Classify all". This will test the model on all the test images, determine the model's performance and also create a confusion matrix. From my test, the model achieved an accuracy of 93%. However, for a more robust model, we still need to train the model on more data, and more times. For my demonstration, I chose this result as an acceptable performance.

<Frame caption="Model testing performance">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img26_screenshot-model-testing-performance.png?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=fd727ad669688c021b7159a66c830b6f" width="1366" height="768" data-path=".assets/images/federated-learning/img26_screenshot-model-testing-performance.png" />
</Frame>

## Result

Finally, after training a decentralized model and uploading it to Edge Impulse, one incredible feature that we can benefit from is a seamless deployment of the model on hardware ranging from MCUs, CPUs, and custom AI accelerators. In this case, we can deploy our model to the Raspberry Pi as an [.eim executable](/tools/libraries/sdks/inference/linux#eim-models) that contains the signal processing and ML code, compiled with optimizations for a processor or GPU (e.g. NEON instructions on ARM cores) plus a very simple IPC layer (over a Unix socket).

First, we need to attach the Raspberry Pi camera to the board.

<Frame caption="Raspberry Pi and camera">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img27_raspberrypi-with-camera-connected.jpg?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=41360cfc03d7593e2b0897b99bd725b8" width="563" height="1000" data-path=".assets/images/federated-learning/img27_raspberrypi-with-camera-connected.jpg" />
</Frame>

Next, we need to install Edge Impulse for Linux dependencies on the Raspberry Pi 4. To do this, we can run the commands below on the Raspberry Pi:

```
sudo apt update
curl -sL https://deb.nodesource.com/setup_12.x | sudo bash -
sudo apt install -y gcc g++ make build-essential nodejs sox gstreamer1.0-tools gstreamer1.0-plugins-good gstreamer1.0-plugins-base gstreamer1.0-plugins-base-apps
npm config set user root && sudo npm install edge-impulse-linux -g --unsafe-perm
```

Afterwards, we need to activate the camera interface on the Raspberry Pi 4 for the camera module. We can run the command `sudo raspi-config` and use the cursor keys to select and open Interfacing Options, then select Camera, and follow the prompt to enable the camera. Finally, reboot the Raspberry Pi by running the command `sudo reboot`.

Once rebooted, we can download the final global model from the Edge Impulse project by running the command below. You will be prompted to input your username and password for your Edge Impulse account, followed by a prompt to select the Edge Impulse project.

```
edge-impulse-linux-runner --download modelfile.eim
```

Finally, we can run the executable model locally on the Raspberry Pi by running the command below. This will capture an image using the camera, process the image, give the image to the model, get the model's prediction and present a live stream of the camera feed and inference results. Without having to write code for each step, [Edge Impulse for Linux](/tools/libraries/sdks/inference/linux) bundles all these processes.

```
edge-impulse-linux-runner --model-file modelfile.eim
```

In the command, we pass the name of the downloaded .eim file, `modelfile`.

We can go to the provided URL (Raspberry Pi's IP address at port 4912) and we will see the feed being captured by the camera as well as the model's predictions. At this point I used a 3D printed support to hold the Raspberry Pi camera upright and then projected the test images to the camera.

<Frame caption="Raspberry Pi with camera">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img28_raspberrypi-camera-supported.jpg?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=de2f09156d4114731e755144120e17d6" width="563" height="1000" data-path=".assets/images/federated-learning/img28_raspberrypi-camera-supported.jpg" />
</Frame>

<br />

<Frame caption="Raspberry Pi with camera - side view">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/img29_raspberrypi-camera-supported-side-view.jpg?fit=max&auto=format&n=Ib0i53A0CIAW87u-&q=85&s=2cc2f81e67698f068089b3a2c1319d5d" width="1600" height="900" data-path=".assets/images/federated-learning/img29_raspberrypi-camera-supported-side-view.jpg" />
</Frame>

Below is a demo video of live classification on the Raspberry Pi 4. We can see that the model predicts the correct class for each image.

<Frame caption="Live classification GIF">
  <img src="https://mintcdn.com/edgeimpulse/Ib0i53A0CIAW87u-/.assets/images/federated-learning/gif-inference-on-raspberrypi-4.gif?s=7ec34521fd535d6edb22a2bc25e32d0b" width="1092" height="614" data-path=".assets/images/federated-learning/gif-inference-on-raspberrypi-4.gif" />
</Frame>

## Conclusion

You can access my public Edge Impulse project using this link: [Federated Learning - BYOM image classification model](https://studio.edgeimpulse.com/public/279823/latest).

From the demonstration, we have seen that we can obtain more accurate and generalizable models through Federated Learning, without requiring the data leave the client devices. Federated Learning has a lot of potential. It prevents sending sensitive information like healthcare records, financial records, or similar across the internet. Since the training occurs from multiple data sources, we can also get more diverse data enabling us to come up with more robust models, that perform better at their tasks.

An excellent progression of this demonstration would be to implement the Federated Learning system with a different Machine Learning model framework, and adding more clients and data to the system. Additionally, we can also reinforce the system by implementing automated deployments, whereby a final global model is automatically deployed on edge devices from an Edge Impulse project.


Built with [Mintlify](https://mintlify.com).