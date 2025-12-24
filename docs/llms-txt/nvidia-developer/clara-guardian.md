# Source: https://developer.nvidia.com/clara-guardian.md

  

# NVIDIA Clara Guardian

NVIDIA Clara™ Guardian is an application framework and partner ecosystem that simplifies the development and deployment of smart sensors with multimodal AI, anywhere in a healthcare facility. With a diverse set of pre-trained [models](/ai-models), reference applications, and fleet management solutions, developers can build solutions faster—bringing AI to healthcare facilities and improving patient care.

  

[Get Started](https://catalog.ngc.nvidia.com/orgs/nvidia/collections/clara_guardian)

  
 ![clara software stack](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/nvidia-clara-guardian-stack.svg)  

Clara Guardian’s key components include healthcare pre-trained models for computer vision and speech, training tools, deployment SDKs, and NVIDIA Fleet Command. NVIDIA Fleet Command is a hybrid-cloud platform for securely managing and scaling AI deployments across millions of servers or edge devices at hospitals.

This makes it easy for ecosystem partners to add AI capabilities to common sensors that can monitor crowds for safe social distancing, measure body temperature, detect the absence of protective gear such as masks, or interact remotely with high-risk patients so that everyone in the healthcare facility stays safe and informed.

Applications and services can run on a wide range of hardware, allowing developers to securely deploy anywhere, from the edge to the cloud.

* * *

### Time to Solution

Leverage high-performance, pre-trained [models](/ai-models) to build accurate AI in healthcare.

### Cloud-Native, Edge First

Scale software quickly and deploy applications easily at the edge.

### Secure Management

Securely manage and scale AI deployments across dozens or up to millions of servers or edge devices.

  

* * *
  

## Healthcare-Specific, Pre-Trained Models
  

### Clara Guardian For Speech

Clara Guardian for speech is a healthcare domain specific version of Riva conversational AI capabilities.

- For **automated speech recognition (ASR)**, models perform offline and streaming recognition to automatically add punctuation, output word timestamps, and return top-n transcripts.   
 CitriNet is the recommended new end-to-end convolutional Connectionist Temporal Classification (CTC) based ASR model. CitriNet models take in audio segments and transcribe them to letter,bytepair or word piece sequences.CitriNet has been trained on ASR dataset and ,without any external LM, it reaches Word Error Rate (WER) 6.22% on LibriSpeech test-other, and can run efficiently on a variety of hardware/ GPUs as shown [here](https://docs.nvidia.com/deeplearning/riva/user-guide/docs/asr/asr-performance.html).   
 The Conformer-CTC model is a non-autoregressive variant of the Conformer model for Automatic Speech Recognition that uses CTC loss/decoding instead of Transducer. 
- For **natural language understanding (NLU)**, deep learning models understand context via encoded vectors and provide appropriate outputs for specific language tasks like next-word prediction and text summarization. 
- For **text to speech (TTS)**, a speech synthesis model is based on FastPitchHifiGanE2E. FastPitchHifiGanE2E is an end-to-end, non-autoregressive model that generates audio from text. It combines FastPitch and HiFiGan into one model and is trained jointly in an end-to-end manner.

Speech models (ASR, NLP, and TTS) can be used to capture, process, and respond to common requests that a patient might make when they are in a healthcare setting.

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/clara/images/clara-guadian-speech%402x.jpg)

  

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/clara/images/clara-guadian-computer-vision%402x.jpg)

### Clara Guardian For Computer Vision

Clara Guardian for computer vision is a healthcare domain specific version of DeepStream and Riva computer vision capabilities.

Clara Guardian contains pre-trained models for applications such as gesture recognition, heart rate monitoring, mask detection, and body pose estimation.

- Body pose estimation can be used to detect positions of key joints and facial landmarks in the body (eyes, ears, elbows, shoulders, wrists, hip sides, knees, ankles, nose, neck, etc) to build patient monitoring AI models.
- Gesture recognition models can recognize a set of common gestures (wave, okay, thumbs-up, stop, etc).
- Heart rate estimation can be used to obtain the heart rate of a person just by observing the video stream of a person’s face.

Pre-compiled NVIDIA TensorRT engines are optimized on NVIDIA GPUs.

  

### Secure Management with Fleet Command

NVIDIA Fleet Command is a hybrid-cloud platform for securely and remotely deploying, managing, and scaling AI across dozens or up to millions of servers or edge devices. Instead of spending weeks planning and executing deployments, in minutes, administrators can scale AI to hospitals. With the capability of an entire IT division in a single control plane, administrators can manage the lifecycle of AI applications, update system software over the air, and remotely monitor and access systems.

See how our customers are using it:

https://www.youtube-nocookie.com/embed/48VSHYeGtk4
  
GTC talk for more [technical details](https://www.nvidia.com/en-us/gtc/session-catalog/?tab.catalogtabfields=1600209910618001TWM3&amp;search=%22Cristiana%20Dinea%22&amp;search.language=1594320459782001LCjF)

  

* * *
  

## An End-to-End AI Solution
  

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/clara-guardian-workflow-diagram.png)

Clara Guardian includes GPU-optimized components that can accelerate every stage of your application development.

### Training

- A collection of healthcare-specific, pre-trained computer vision and conversational AI models for a variety of use cases.
- [NVIDIA NeMo](https://github.com/NVIDIA/NeMo) to build conversational AI models for ASR, NLP, and TTS 
- [TAO Toolkit](/tao-toolkit) to create highly accurate computer vision models with zero coding 

### Deployment

- NVIDIA Riva for deploying conversational AI models that fuse vision, speech, and other sensor data
- [NVIDIA DeepStream SDK](/deepstream-sdk) for a multi-platform scalable video analytics framework with Transport Layer Security (TLS) that can deploy on the edge and connect to any cloud

* * *
  

## Testimonials
  

&gt; _“Our AI-powered IOT platform, running on NVIDIA Clara Guardian, is used by leading hospitals, such as Northwestern Medicine, to screen hundreds of thousands of people for elevated temperatures and help front-line providers safely care for patients during the pandemic. Clara Guardian made smart hospitals at the edge possible, enabling our customers to increase staff productivity by over six-fold, saving millions of dollars in staffing costs while improving patient care.”_
&gt; 
&gt; Andrew Gostine, MD, CEO of Whiteboard Coordinator ![Whiteboard](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/clara/images/whiteboard.png)

&gt; _“We have been using NVIDIA GPUs in Ouva solutions from day one. With our new solution, we are aiming to allow nurses to monitor hundreds of patients in real time. The Clara Guardian framework allows us to build a scalable and efficient solution in no time, allowing our team to focus on our core competency—developing algorithms that unlock the potential of remote care.”_
&gt; 
&gt; Dogan Demir, CEO of Ouva ![ouva](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/clara/images/ouva.png)

* * *
  

## Resources
  

**Webinars**
- [Improve Patient Care with Everyday Sensors and Multimodal AI](https://www.nvidia.com/en-us/gtc/session-catalog/?search.industrysegment=option_1559593230294&amp;search=a21257)
- [Cutting Edge AI Tools Aid in Safe Patient Care in Smart Hospital](https://www.nvidia.com/en-us/gtc/session-catalog/?tab.catalogtabfields=1600209910618001TWM3&amp;search=%22Cristiana%20Dinea%22&amp;search.language=1594320459782001LCjF)
- [TensorRT and Triton Deep Dive](https://event.on24.com/eventRegistration/EventLobbyServlet?target=reg30.jsp&amp;referrer=&amp;eventid=2355625&amp;sessionid=1&amp;key=7FEA91B2550844603D8D23097ED564D8&amp;regTag=&amp;sourcepage=register)
- [NVIDIA Pre-trained Vision Models with DeepStream SDK](https://info.nvidia.com/iva-occupancy-webinar-reg-page.html)

**Latest News**
- Learn more about the latest[developer news](https://developer.nvidia.com/blog/?tags=healthcare-and-lifesciences&amp;categories=)
- Learn more about technical deep dive on [Fleet Command](https://www.nvidia.com/FleetCommand/)

**Deep Learning Institute Training**
- [Optimization and Deployment of TensorFlow Models with TensorRT](https://courses.nvidia.com/courses/course-v1:DLI+L-FX-18+V2/about)
- [Fundamentals of Deep Learning for Computer Vision](https://courses.nvidia.com/courses/course-v1:DLI+C-FX-01+V2/about)
- [Getting Started with AI on Jetson Nano](https://courses.nvidia.com/courses/course-v1:DLI+C-RX-02+V1/about)

  

**Intelligent Video Analytics** 
- [NVIDIA DeepStream SDK](/deepstream-sdk) for AI-based multi-sensor processing and video and image understanding
- [TAO Toolkit](/tao-toolkit) to create highly accurate AI models with zero coding

**Speech and NLP**
- [NVIDIA NeMo](https://github.com/NVIDIA/NeMo), an open-source toolkit for building conversational AI models 
- [NVIDIA Riva SDK](/riva) for deploying conversational AI models that fuse vision, speech, and other sensor data 

**Edge Hardware**

Explore the Fleet Command to securely manage and scale AI deployments.

[Learn More](https://www.nvidia.com/en-us/data-center/products/egx-edge-computing/)

_Disclaimer: Clara SDKs and samples are for developmental purposes only and cannot be used directly for clinical procedures._
