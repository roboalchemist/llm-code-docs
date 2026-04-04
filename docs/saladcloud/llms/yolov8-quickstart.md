# Source: https://docs.salad.com/container-engine/tutorials/computer-vision/yolov8-quickstart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# YOLOv8 QuickStart Guide

*Last Updated: October 10, 2024*

## **Introduction**

Object detection has significantly evolved from its early days. Early systems struggled with shape differentiation, but
modern algorithms like YOLOv8 now pinpoint and track objects with impressive accuracy and speed.

YOLOv8 excels in processing live feeds, identifying and classifying objects efficiently. It provides real-time object
detection without requiring extensive model training from users.

Deploying YOLOv8 on SaladCloud is practical and efficient. SaladCloud's infrastructure makes YOLOv8 accessible, allowing
users to deploy advanced object detection systems without heavy hardware investment. Whether you're a developer or a
business, YOLOv8 on SaladCloud offers a scalable solution.

## **Deployment**

To deploy YOLO on Salad, you have several options:

**Option 1: Use our prebuilt container:**

* Create your account on [portal](https://portal.salad.com/) and set up your organization.
* Under container groups click “Deploy a Container Group“:

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/72bde49-image-20231110-194241.png?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=8ae0f9cf5ebb292cfad7d1d3dce3b95d" data-og-width="1224" width="1224" data-og-height="436" height="436" data-path="container-engine/images/72bde49-image-20231110-194241.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/72bde49-image-20231110-194241.png?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=bf245f36324bd8838729438112b04adb 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/72bde49-image-20231110-194241.png?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=6d5d594f9a4cc1d7798b4a8105194d2f 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/72bde49-image-20231110-194241.png?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=72074a0ae6b99c94fa145667266b005e 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/72bde49-image-20231110-194241.png?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=2dba43fb57da8b28a590e0b45a2f53e5 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/72bde49-image-20231110-194241.png?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=9b4dfcd9deda56e397dc6dd36521c395 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/72bde49-image-20231110-194241.png?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=b967c9370e2bbdc34ea2821e3772e5f2 2500w" />

**Configure Container Group:**

1. Create a **unique name** for your Container group
2. Click “edit” next to **Image source**. Under image name paste our open source image link:
   saladtechnologies/yolov8-api:2.0.0 and click save
3. **Replica count**: Choose the number of replicas you need
4. **Choose compute resources**, including CPU, RAM, and GPU allocation.
5. **Optional Settings:**

* Enable health check probes, external logging, and environment variables as needed.
* For our solution, enable networking under **Container Gateway** by clicking “Edit,” checking “Enable Container
  Gateway,” and **setting the port to 80**.
* Optionally, enable Authentication for an extra layer of security. If enabled, you'll need to provide your personal
  token with API calls. Your token can be found here: [SaladCloud Portal](https://portal.salad.com/api-key)

6. Check “AutoStart container group once image is pulled” and hit “Deploy.”

**Option 2: Build your own image using our git repo.**

If you want to make some changes to the way the application works you can use our git repo as a base code:

1. Fork our Git repo: [SaladTechnologies/yolov8-on-salad](https://github.com/SaladTechnologies/yolov8-on-salad)
2. Make changes to the code. Example: To use your custom model save the model in “inference“ folder:

<img src="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolo_repo.png?fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=de9b48b2820b28c7c9f75715c4161db9" data-og-width="357" width="357" data-og-height="170" height="170" data-path="container-engine/images/yolo_repo.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolo_repo.png?w=280&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=01f4594ba41f3404011e2dde07033cab 280w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolo_repo.png?w=560&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=d9bb978aee46c570dcc1274fd6612183 560w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolo_repo.png?w=840&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=a9c17aac091d6bd62e53242ee16836a1 840w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolo_repo.png?w=1100&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=f4411851c6584407a022a497e6f396b4 1100w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolo_repo.png?w=1650&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=4920baeaf5066afafa218d59bd74c41f 1650w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/yolo_repo.png?w=2500&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=7c793ad197a933538dae42f72fcc198f 2500w" />

Replace model path in your fast.py file : model = YOLO("yolov8n.pt") with model = YOLO("path/to/your/model.pt") 3. Build
and deploy your image. Example Dockerfile is located in “Api” folder The repo also contains code for multithreading and
batch processing, as well as a Bicep file for Azure resources deployment. Azure is provided as an example. 4. Follow
steps from deployment option 1 above

**Option 3: Create your custom solution using our step-by-step guides.** We’ve created a detailed guide on how to set up
our solution, including all the parameters used. You can find it here:
[Deployment Guide](/container-engine/tutorials/computer-vision/yolov8-deployment-tutorial).
