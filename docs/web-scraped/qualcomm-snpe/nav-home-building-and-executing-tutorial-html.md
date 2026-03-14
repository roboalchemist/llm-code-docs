# Source: https://docs.qualcomm.com/nav/home/building_and_executing_tutorial.html?product=1601111740010412

Title: Qualcomm AI Runtime (QAIRT) SDK

URL Source: https://docs.qualcomm.com/nav/home/building_and_executing_tutorial.html?product=1601111740010412

Published Time: Wed, 11 Mar 2026 18:04:27 GMT

Markdown Content:
Qualcomm AI Runtime (QAIRT) SDK - Qualcomm Neural Processing SDK for AI Documentation
===============

[](https://www.qualcomm.com/)

Products
========

Applications
============

Developer
=========

Support
=======

Company
=======

Workspace

[Developer](https://www.qualcomm.com/developer)

Qualcomm Neural Processing SDK

*   [Overview](https://www.qualcomm.com/developer/software/neural-processing-sdk-for-ai)
*   [Documentation](https://docs.qualcomm.com/nav/home?product=1601111740010412)
*   [Support](https://www.qualcomm.com/developer/software/neural-processing-sdk-for-ai/support)

[Forums](https://mysupport.qualcomm.com/supportforums/s/topic/0TO4V0000001XL9WAM/iot-ai)

Developer Workspace

Loading...

Bring your ideas to life by saving your favorite products, comparing specifications and sharing with your team to work collaboratively.

0 Projects

Sort

Newest

Newest Oldest Recently updated Least recently updated

Create a Project

You do not have any projects yet. Start building your Workspace.

Documentation

[Qualcomm Neural Processing SDK for AI](https://docs.qualcomm.com/)

Overview QNN

Introduction Overview Setup

Linux Setup Windows Setup

Backend

DSP HTP

Qualcomm Hexagon Plugin Interface QNN HTP Op Package - Common Default Package Ops Usage Examples QNN HTP Optimization Utility Functions Usage Examples HTP Core Headers for Op Packages Implementing Ops QNN HTP Op Package API Revision History Optimization Grammar QNN HTP Op Package - Relu Op Example QNN HTP-FP16 Op Package - Relu Op Example Scheduling and Allocation Allocate Memory for Scratch Buffers Tensors and Memory Layout Writing QNN HTP Op Package General OpPackage Central Migration Guidance Op Package Migration Guide Avoid Low Depth Activations Avoid Low Depth Activations (more examples)Use Space-to-depth Transformation where possible Reducing TCM Requirements for Performance and Functionality Choice of Activation Functions Number of Channels Quantized 16 bit activations (A16) vs FP16 and Activation Fusion: Performance and power differences INT4 encodings for weights Other Performance and Energy Guidelines HTP Yielding HTP VTCM Sharing VTCM Windowing QNN HTP SSR QNN HTP Qmem Graph

HTA LPAI CPU GPU

QNN GPU QnnMem API Tutorial QNN GPU Tuning Mode Tutorial

Saver

Op Packages

 Generating Op Packages

QNN Op Package Code Generation XML OpDef Schema Reference Example XML OpDef Configs QNN Converter Op Package Code Generation

Tools Converters Quantization QAIRT Quantization Specification Tutorials

Tutorial: Converting and executing a CNN or ONNX model with QNN

CNN to QNN for Linux Host

Convert to QNN for Linux Host on Linux / Android / QNX Target

Convert to QNN for Linux Host on CPU Backend Convert to QNN for Linux Host on GPU Backend Convert to QNN for Linux Host on DSP Backend Convert to QNN for Linux Host on HTP Backend Convert to QNN for Linux Host on LPAI Backend

CNN to QNN for Linux Host on Windows Target

ONNX to QNN for Linux Host

Convert to QNN for Linux Host on Linux / Android / QNX Target

Convert to QNN for Linux Host on CPU Backend Convert to QNN for Linux Host on GPU Backend Convert to QNN for Linux Host on DSP Backend Convert to QNN for Linux Host on HTP Backend Convert to QNN for Linux Host on LPAI Backend

CNN to QNN for Linux Host on Windows Target

CNN to QNN for Windows Host

CNN to QNN for Windows Host on Linux Target CNN to QNN for Windows Host on Windows Target

How to Use the Sample App Sample App Tutorial Saver Tutorial: Save execution sequence with Saver and replay on a backend QNN HTP Shared Buffer Tutorial Tutorial: Executing a shallow model using custom op package Migrating from Hexagon-nn

Benchmarking Operations

Supported Operations Op Definition Revision History Backend Specific Revision History

QNN CPU Op Definition Revision History QNN DSP Op Definition Revision History QNN GPU Op Definition Revision History QNN HTA Op Definition Revision History QNN HTP Op Definition Revision History QNN LPAI Op Definition Revision History

Common Terminology Master Definitions Block Op Overview Block Op Usage

Block Ops ONNX Usage Buffer Usage MaskedSoftmax Usage StatefulGru Usage StatefulLstm Usage

Block Op Definitions CPU DSP GPU HTP HTA LPAI

API

Overview Usage Guidelines QNN API Revision History Backend Specific Revision History

CPU Version History DSP Version History GPU Version History HTA Version History HTP Version History LPAI Version History

QNN System API Revision History Supported APIs Supported Capabilities Error codes

Glossary Revision History

SNPE

Overview Setup

Linux Setup Windows Setup

Tutorials and Examples

SNPE Building and Executing Your Model Tutorial

SNPE Building and Executing a Model Tutorial for Linux Host

SNPE Tutorial for Linux Target Device from Linux Host In Summary SNPE Tutorial for Windows Target Device from Linux Host

SNPE Building and Executing Your Model for Windows Host

SNPE Tutorial for Windows Target Device from Windows Host In Summary

Tutorials Setup SNPE1 to SNPE2 Migration Guide Running Nets

Running the Inception v3 Model Running the Inception v3 Model in Windows Running the Word-RNN Model Running the Spoken Digit Recognition Model Running a VGG Model

Code Examples

C++ Tutorial - Build the Sample C Tutorial - Build the Sample C API Guidelines Android Tutorial Windows Tutorial UDO Tutorial UDO DSP tutorial for Quantized DLC UDO DSP tutorial on Windows for Quantized DLC UDO Tutorial With Weights PSNPE Introduction PSNPE C Tutorial PSNPE C++ Tutorial PSNPE Android Tutorial DSP Runtime Environment Network Resizing Input Image Batch Init Caching Windows DSP Library Loading Tutorial Signed PD and Unsigned PD at Runtime

Application Tips

Application Integration Tips Performance Tips Burst Mode on DSP and AIP Logging CPU Fixed Point Mode Windows ARM64X Support Hexagon NPU Runtime Driver (Windows Only)Windows Error Reporting Low Level Perf APIs

Network Models

Supported Network Layers Supported ONNX Ops Quantized vs Non-Quantized Models User-defined Operations

Overview of UDO Defining a UDO Defining a UDO Package Creating a UDO Package Compiling a UDO package Compiling a UDO package for Windows Preparing a model with UDO Running a model with UDO

Model Conversion

TensorFlow Model Conversion Tensorflow Graph Compatibility TFLite Model Conversion PyTorch Model Conversion ONNX Model Conversion Quantizing a Model Offline Graph Caching for DSP Runtime on HTP Qairt Converter Qairt Quantizer Model Tips

Using MobilenetSSD Using DeepLabv3

Input Data and Preprocessing

Input Image Formatting

Benchmarking and Accuracy

Benchmarking

Linting Profile QHAS Profiling

MobilenetSSD Benchmarking Inference Accuracy

Tools Debug Tools

Architecture Checker (Experimental)Accuracy Debugger (Experimental)

API Limitations Revision History References

Genie

Introduction

Conventions Revision History

Tutorials

Setup How to Use Genie Source Code Examples

libGenie.so and Genie.dll genie-t2t-run genie-t2e-run genie-app Gen AI Transformer Model Library

Genie Dialog

Llama 2 7B

QNN HTP

Android

Basic

Yes No

SSD Q1 SPD LADE

Windows

QNN Gen AI Transformer

Linux

Yes

Linux Android

No

Linux Android

Windows

QNN GPU KV Share Dialog

Llama 3 3B

QNN HTP

Android

Eaglet

Eaglet Dialog - LoRA & Draft Switching Eaglet Dialog - LoRA Switching No

Query Cancellation KV$ Rewind Updating the Stop Sequence Token Query Updating the Sampler Parameters Engine Sharing Prefix Quant

Genie Embedding

BGE-Large

QNN HTP QNN Gen AI Transformer

Genie Engine Genie Log Genie Profile Genie Pipeline

GLM-4v facebook/wt19-en-de

Genie Accuracy

Library

Genie C API GeniePipeline

Genie Pipeline JSON Configuration

GenieNode

Genie Node JSON Configuration

GenieDialog

Genie Dialog JSON Configuration

GenieEmbedding

Genie Embedding JSON Configuration

GenieProfile

Genie Profile JSON Configuration

GenieSampler GenieEngine

Genie Engine JSON Configuration

GenieTokenizer GenieAccuracy

Genie Accuracy JSON Configuration

Tools

genie-t2t-run genie-t2e-run genie-app qnn-genai-transformer-composer

TFLite Delegate

Overview Tutorials

Tutorial - Preparing and Executing a Model with TFLite Delegate Tutorial - Using TFLite Delegate With a C/C++ Application Tutorial - Using TFLite Delegate With a Java Application Tutorial - Running Inference Using the Qualcomm® AI Engine Direct Delegate Tutorial - Skip Delegation Ops Using the Qualcomm® AI Engine Direct Delegate Tutorial - Benchmarking the Qualcomm® AI Engine Direct Delegate Tutorial - Running Inference Using Shared Memory Tutorial - Use Mix-Precision Model with Qualcomm® AI Engine Direct Delegate Tutorial - Profile Custom Models using Qualcomm® AI Engine Direct Delegate Tutorial - Use IR Backend by Using the Qualcomm® AI Engine Direct Delegate

Acceleration Support Tools Custom Operator Support Frequently Asked Questions API

C Interface Java Interface External Delegate Options

Qualcomm® AI Engine Direct Backend Library Glossary API Version History Release Notes

Key Documents

Learning Resources

Learning Resources Artificial Intelligence, Machine Learning, Android and the Qualcomm Neural Processing SDK for AI

Types of machine learning Data collection and pre-processing techniques Introduction to the Qualcomm Neural Processing SDK for AI and its components Benchmarking the Qualcomm Neural Processing SDK for AI vs. TensorFlow on Android Bringing up TensorFlow frameworks on the Qualcomm Neural Processing SDK for AI Setting up the project using the Android Studio IDE and required SDKs

Developing Apps with the Qualcomm Neural Processing SDK for AI

Working with Machine Learning Models in the Qualcomm Neural Processing SDK for AI Tuning and Optimizing Machine Learning Models Developing an Android App for Snapdragon Mobile Platforms Streaming Live Frames to a Machine Learning Model with the Qualcomm Neural Processing SDK for AI

Training and Testing Machine Learning Models

Functional Testing of Machine Learning Models Training, Testing and Evaluating Machine Learning Models

Image Segmentation using DeepLab-v3 and Qualcomm Neural Processing SDK for AI

Classification, Object Detection and Image Segmentation DeepLab-v3 using the Qualcomm Neural Processing SDK for AI on Ubuntu DeepLab-v3 using Qualcomm Neural Processing SDK for AI on Android

CNN Architectures

Deep Learning and Convolutional Neural Networks for Computer Vision Computer Vision CNN Architectures Advanced Computer Vision CNN Architectures

Vision-based AI Use Cases

Real-time Facial Detection and Validation Functional Testing of Vision-based ML Applications Facial Keypoint Detection Facial Expression Recognition — Part 1: Solution Pipeline on Ubuntu Facial Expression Recognition — Part 2: Solution Pipeline on Android Performance Analysis Using Benchmarking Tools

Software

SDKs

* * *

[All Documents](https://docs.qualcomm.com/)

[Legal notice](https://docs.qualcomm.com/)

1.   SNPE
2.   Tutorials and Examples
3.   SNPE Building and Executing Your Model Tutorial

SNPE Building and Executing Your Model Tutorial
===============================================

SNPE Building and Executing Your Model Tutorial Qualcomm® AI Runtime (QAIRT) SDKs
===============

SNPE Building and Executing Your Model Tutorial
===============================================

This tutorial will walk you through how to use Qualcomm’s Neural Processing SDK, commonly referred to as the SNPE SDK, to run your AI model on a hardware device’s processing unit of your choice. Ex. Running a Tensorflow model on a GPU.

This tutorial provides an example Tensorflow model (“Inception v3”) to show you the workflow. When applying this to your own model, be sure to consider these key variables which determine how you should use SNPE for your situation:

1.   What model do you want to use?

    1.   How will you download it?

    2.   How will you get the input data?

    3.   How will you format the input data to feed it into your model?

    4.   Do you want to quantize it? (Required for HTP / DSP target device processors)

2.   Which framework is your model using? (Ex. ONNX, PyTorch, Tensorflow, etc.)

3.   What is the OS and architecture of your host machine? (Ex. Linux x86_64)

4.   What is the OS and architecture of your target device? (Ex. Ubuntu Aarch64)

5.   Which processor(s) do you want to use for your AI models? (CPU / GPU / DSP / HTP / AIP)

With those answers, you can adapt this tutorial to work with a model of your choice on your host machine, with any supported target device.

**To start with,** choose the proper instructions below based on which type of host machine you would like to use:

1.   [[Linux Host Machine](https://docs.qualcomm.com/nav/home/building_and_executing_tutorial_linux_host.html?product=1601111740010412)](https://docs.qualcomm.com/)

2.   [[Windows Host Machine](https://docs.qualcomm.com/nav/home/building_and_executing_tutorial_windows_host.html?product=1601111740010412)](https://docs.qualcomm.com/)

Warning

Cross-compiling from a Windows host machine to a Linux target device is not supported.

If you are using a Windows host machine, you can either use [Windows Subsystem Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install) or [dual-boot your machine](https://www.tomshardware.com/software/linux/how-to-dual-boot-linux-and-windows-on-any-pc) with a Linux image ([Ubuntu 22.04 is recommended](https://releases.ubuntu.com/jammy/)) to work with Linux / Android targets. If you use WSL, follow the Linux instructions below.

If you have any issues, please reach out on our [Discord server](https://discord.gg/akBfTuX2bR)!

 Last Published: Mar 03, 2026

[Previous Tutorials and Examples](https://docs.qualcomm.com/)[Next SNPE Building and Executing a Model Tutorial for Linux Host](https://docs.qualcomm.com/)

 Need assistance?: [Contact us](https://www.qualcomm.com/developer/software/neural-processing-sdk-for-ai/support)

May contain U.S. and international export controlled information

Light Dark Auto

[](https://www.qualcomm.com/)

Qualcomm relentlessly innovates to deliver intelligent computing everywhere, helping the world tackle some of its most important challenges. Our leading-edge AI, high performance, low-power computing, and unrivaled connectivity deliver proven solutions that transform major industries. At Qualcomm, we are engineering human progress.

[](https://www.linkedin.com/company/qualcomm/)[](https://x.com/qualcomm)[](https://www.youtube.com/qualcomm)[](http://www.instagram.com/qualcomm/)

Quick links
-----------

*   [Products](https://www.qualcomm.com/products)
*   [Support](https://www.qualcomm.com/support)
*   [Partners](https://www.qualcomm.com/support/partner)
*   [Contact us](https://www.qualcomm.com/support/contact)
*   [Developer](https://www.qualcomm.com/developer)

Company info
------------

*   [About us](https://www.qualcomm.com/company)
*   [Careers](https://www.qualcomm.com/company/careers)
*   [Investors](https://investor.qualcomm.com/)
*   [News & media](https://www.qualcomm.com/news)
*   [Our businesses](https://www.qualcomm.com/our-businesses)
*   [Email Subscriptions](https://assets.qualcomm.com/subscription-center-sign-up.html)

Stay connected
--------------

Get the latest Qualcomm and industry information delivered to your inbox.

[Subscribe](https://assets.qualcomm.com/subscription-center-sign-up.html)[Manage your subscription](https://myaccount.qualcomm.com/profile)

*   [Terms of Use](https://www.qualcomm.com/site/terms-of-use)
*   [Privacy](https://www.qualcomm.com/site/privacy)
*   [Cookie Policy](https://www.qualcomm.com/site/privacy/cookies)
*   [Accessibility Statement](https://www.qualcomm.com/accessibility)
*   [Responsible AI Policy](https://www.qualcomm.com/site/responsible-ai-license)
*   Cookie Settings 

Language: English (US)

### Languages

*   [English ( United States )](https://www.qualcomm.com/)
*   [简体中文 ( China )](http://www.qualcomm.cn/)

© Qualcomm Technologies, Inc. and/or its affiliated companies.

Snapdragon and Qualcomm branded products are products of Qualcomm Technologies, Inc. and/or its subsidiaries. Qualcomm patented technologies are licensed by Qualcomm Incorporated.

Note: Certain services and materials may require you to accept additional terms and conditions before accessing or using those items.

References to "Qualcomm" may mean Qualcomm Incorporated, or subsidiaries or business units within the Qualcomm corporate structure, as applicable.

Qualcomm Incorporated includes our licensing business, QTL, and the vast majority of our patent portfolio. Qualcomm Technologies, Inc., a subsidiary of Qualcomm Incorporated, operates, along with its subsidiaries, substantially all of our engineering, research and development functions, and substantially all of our products and services businesses, including our QCT semiconductor business.

Materials that are as of a specific date, including but not limited to press releases, presentations, blog posts and webcasts, may have been superseded by subsequent events or disclosures.

Nothing in these materials is an offer to sell or license any of the services or materials referenced herein.

[](https://docs.qualcomm.com/ "Scroll To Top")

This website processes personal data through our and third parties’ online tracking technologies, including analytics and advertising cookies. To learn more about how we and our affiliates within the Qualcomm Group may use your personal data and cookies, please review the Privacy Policy published at the bottom of this website and Qualcomm’s [Cookie Policy](https://www.qualcomm.com/site/privacy/cookies). If you don’t want to share your website activities, including browsing behavior, with our third-party partners via these tracking technologies, click on “Cookie Settings" below to update your preferences. You can also update your cookie preferences at any time by clicking the [Do Not Sell or Share My Personal Information](https://docs.qualcomm.com/) link at the bottom of this website.

Cookie Settings

I Understand

![Image 1: Company Logo](https://cdn.cookielaw.org/logos/b0a5f2cc-0b29-4907-89bf-3f6b380a03c8/019b2967-1f59-7929-8629-87bcc32af336/88f57162-c334-444d-87f4-6a565e8edc19/1280px-Qualcomm-Logo.svg.png)

Opt-Out Request Honored

Do Not Sell or Share My Personal Data
-------------------------------------

As described in greater detail in the Privacy Policy at the bottom of this website and Qualcomm’s [Cookie Policy](https://www.qualcomm.com/site/privacy/cookies), we use certain third party advertising and other cookies on this website, which may be considered a “sale” of personal information or “sharing” of personal information for targeted advertising under applicable data privacy laws. To opt out of the sale or sharing of your personal information, please click the “Share or Sale of Personal Information” toggle button below. When you have opted out, the button color will change from blue to grey. We will also honor your opt-out of sale or sharing requests communicated via opt-out preference signals, such as the Global Privacy Control. 

Allow All
### Manage Consent Preferences

#### Strictly Necessary Cookies

Always Active

These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work.

#### Share Or Sale of Personal Information

- [x] Share Or Sale of Personal Information 

As described above, you may exercise your right to opt out of the sale or sharing of personal information by using this toggle button

*   ##### Targeting Cookies

- [x] Switch Label label  
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. If you do not allow these cookies, you will experience less targeted advertising.

*   ##### Performance Cookies

- [x] Switch Label label  
These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.

*   ##### Functional Cookies

- [x] Switch Label label  
These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.

### Cookie List

Clear

*   - [x] checkbox label label 

Apply Cancel

Consent Leg.Interest

- [x] checkbox label label

- [x] checkbox label label

- [x] checkbox label label

Confirm My Choices

[![Image 2: Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)
