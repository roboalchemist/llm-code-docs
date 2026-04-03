# Source: https://docs.gradsflow.com/en/latest/examples/nbs/01-ImageClassification/

---
description: An open-source AutoML Library based on PyTorch
title: GradsFlow - Auto Image Classification
---

* API References
* [ Tuner](https://docs.gradsflow.com/en/gradsflow/tuner)
* AutoTasks
* [ Data](https://docs.gradsflow.com/en/gradsflow/data)
* [ Callbacks](https://docs.gradsflow.com/en/gradsflow/callbacks)
* [ Core](https://docs.gradsflow.com/en/gradsflow/core)
* [ utility](https://docs.gradsflow.com/en/gradsflow/utils.md)
* [ Release Notes](https://docs.gradsflow.com/en/CHANGELOG/)

[ ](https://github.com/gradsflow/gradsflow/edit/master/docs/examples/nbs/01-ImageClassification.ipynb "Edit this page") 

# Auto Image Classification

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gradsflow/gradsflow/blob/main/examples/nbs/01-ImageClassification.ipynb) 

First, install gradsflow

`pip install git+https://github.com/gradsflow/gradsflow@main`

In \[ \]:

Copied! 

import os
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

import os import sys import warnings from pathlib import Path warnings.filterwarnings("ignore")

In \[ \]:

Copied! 

import torchvision
from torch.utils.data import DataLoader
from torchvision import transforms as T

from gradsflow import AutoImageClassifier
from gradsflow.data.common import random_split_dataset

import torchvision from torch.utils.data import DataLoader from torchvision import transforms as T from gradsflow import AutoImageClassifier from gradsflow.data.common import random\_split\_dataset

Let's use `CalTech101` dataset provided by `torchvision`

In \[ \]:

Copied! 

# Replace dataloaders with your custom dataset and you are all set to train your model
image_size = (64, 64)
batch_size = 4

to_rgb = lambda x: x.convert("RGB")

augs = T.Compose([to_rgb, T.AutoAugment(), T.Resize(image_size), T.ToTensor()])
data = torchvision.datasets.Caltech101("~/", download=True, transform=augs)

\# Replace dataloaders with your custom dataset and you are all set to train your model image\_size = (64, 64) batch\_size = 4 to\_rgb = lambda x: x.convert("RGB") augs = T.Compose(\[to\_rgb, T.AutoAugment(), T.Resize(image\_size), T.ToTensor()\]) data = torchvision.datasets.Caltech101("\~/", download=True, transform=augs)

Files already downloaded and verified

In \[ \]:

Copied! 

train_data, val_data = random_split_dataset(data, 0.01)
train_dl = DataLoader(train_data, batch_size=batch_size)
val_dl = DataLoader(val_data, batch_size=batch_size)
num_classes = len(data.categories)

train\_data, val\_data = random\_split\_dataset(data, 0.01) train\_dl = DataLoader(train\_data, batch\_size=batch\_size) val\_dl = DataLoader(val\_data, batch\_size=batch\_size) num\_classes = len(data.categories)

If you want to run Gradsflow on a remote server then first setup [ray cluster](https://docs.ray.io/en/master/cluster/index.html) and initialize ray with the remote address.

In \[ \]:

Copied! 

# ray.init(address="REMOTE_IP_ADDR")
# ray.init(local_mode=True)

\# ray.init(address="REMOTE\_IP\_ADDR") # ray.init(local\_mode=True)

To train an image classifier create an object of `AutoImageClassifier` and provide number of trials and timeout.

In \[ \]:

Copied! 

model = AutoImageClassifier(
    train_dataloader=train_dl,
    val_dataloader=val_dl,
    num_classes=num_classes,
    max_epochs=2,
    optimization_metric="train_loss",
    n_trials=4,
)
print("AutoImageClassifier initialised!")

model = AutoImageClassifier( train\_dataloader=train\_dl, val\_dataloader=val\_dl, num\_classes=num\_classes, max\_epochs=2, optimization\_metric="train\_loss", n\_trials=4, ) print("AutoImageClassifier initialised!")

AutoImageClassifier initialised!

In \[ \]:

Copied! 

analysis = model.hp_tune()
print("completed!")

analysis = model.hp\_tune() print("completed!")

2022-01-09 14:50:33,186	WARNING function_runner.py:563 -- Function checkpointing is disabled. This may result in unexpected behavior when using checkpointing features or certain schedulers. To enable, set the train function arguments to be `func(config, checkpoint_dir=None)`.

\== Status ==  
Current time: 2022-01-09 14:50:33 (running for 00:00:00.12)  
Memory usage on this node: 10.0/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 PENDING)  

| Trial name                            | status  | loc | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | --- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | PENDING |     | ssl\_resnet18 | 0.00333062 | adam      |
  
  
(pid=2443) /Users/aniket/miniconda3/envs/am/lib/python3.9/site-packages/gradsflow/utility/common.py:124: UserWarning: to_item didn't convert any value.
(pid=2443)   warnings.warn("to_item didn't convert any value.")

\== Status ==  
Current time: 2022-01-09 14:50:38 (running for 00:00:05.24)  
Memory usage on this node: 10.0/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 1.0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 RUNNING)  

| Trial name                            | status  | loc            | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | -------------- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | RUNNING | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      |
  
  
\== Status ==  
Current time: 2022-01-09 14:50:43 (running for 00:00:10.26)  
Memory usage on this node: 10.0/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 1.0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 RUNNING)  

| Trial name                            | status  | loc            | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | -------------- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | RUNNING | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      |
  
  
\== Status ==  
Current time: 2022-01-09 14:50:48 (running for 00:00:15.27)  
Memory usage on this node: 9.9/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 1.0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 RUNNING)  

| Trial name                            | status  | loc            | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | -------------- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | RUNNING | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      |
  
  
\== Status ==  
Current time: 2022-01-09 14:50:53 (running for 00:00:20.29)  
Memory usage on this node: 9.9/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 1.0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 RUNNING)  

| Trial name                            | status  | loc            | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | -------------- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | RUNNING | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      |
  
  
\== Status ==  
Current time: 2022-01-09 14:50:58 (running for 00:00:25.31)  
Memory usage on this node: 9.9/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 1.0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 RUNNING)  

| Trial name                            | status  | loc            | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | -------------- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | RUNNING | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      |
  
  
\== Status ==  
Current time: 2022-01-09 14:51:03 (running for 00:00:30.32)  
Memory usage on this node: 9.9/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 1.0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 RUNNING)  

| Trial name                            | status  | loc            | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | -------------- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | RUNNING | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      |
  
  
\== Status ==  
Current time: 2022-01-09 14:51:08 (running for 00:00:35.34)  
Memory usage on this node: 9.9/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 1.0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 RUNNING)  

| Trial name                            | status  | loc            | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | -------------- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | RUNNING | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      |
  
  
\== Status ==  
Current time: 2022-01-09 14:51:13 (running for 00:00:40.36)  
Memory usage on this node: 9.9/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 1.0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 RUNNING)  

| Trial name                            | status  | loc            | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | -------------- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | RUNNING | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      |
  
  
\== Status ==  
Current time: 2022-01-09 14:51:18 (running for 00:00:45.38)  
Memory usage on this node: 9.9/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 1.0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 RUNNING)  

| Trial name                            | status  | loc            | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | -------------- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | RUNNING | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      |
  
  
\== Status ==  
Current time: 2022-01-09 14:51:23 (running for 00:00:50.40)  
Memory usage on this node: 9.9/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 1.0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 RUNNING)  

| Trial name                            | status  | loc            | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | -------------- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | RUNNING | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      |
  
  
\== Status ==  
Current time: 2022-01-09 14:51:28 (running for 00:00:55.41)  
Memory usage on this node: 9.9/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 1.0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 RUNNING)  

| Trial name                            | status  | loc            | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | -------------- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | RUNNING | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      |
  
  
\== Status ==  
Current time: 2022-01-09 14:51:33 (running for 00:01:00.43)  
Memory usage on this node: 10.0/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 1.0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 RUNNING)  

| Trial name                            | status  | loc            | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | -------------- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | RUNNING | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      |
  
  
\== Status ==  
Current time: 2022-01-09 14:51:38 (running for 00:01:05.45)  
Memory usage on this node: 10.1/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 1.0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 RUNNING)  

| Trial name                            | status  | loc            | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | -------------- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | RUNNING | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      |
  
  
\== Status ==  
Current time: 2022-01-09 14:51:43 (running for 00:01:10.47)  
Memory usage on this node: 10.1/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 1.0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 RUNNING)  

| Trial name                            | status  | loc            | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | -------------- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | RUNNING | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      |
  
  
\== Status ==  
Current time: 2022-01-09 14:51:48 (running for 00:01:15.48)  
Memory usage on this node: 10.1/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 1.0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 RUNNING)  

| Trial name                            | status  | loc            | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | -------------- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | RUNNING | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      |
  
  
\== Status ==  
Current time: 2022-01-09 14:51:53 (running for 00:01:20.50)  
Memory usage on this node: 10.1/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 1.0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 RUNNING)  

| Trial name                            | status  | loc            | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | -------------- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | RUNNING | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      |
  
  
\== Status ==  
Current time: 2022-01-09 14:51:58 (running for 00:01:25.52)  
Memory usage on this node: 10.0/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 1.0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 RUNNING)  

| Trial name                            | status  | loc            | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | -------------- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | RUNNING | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      |
  
  
\== Status ==  
Current time: 2022-01-09 14:52:03 (running for 00:01:30.54)  
Memory usage on this node: 10.0/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 1.0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 RUNNING)  

| Trial name                            | status  | loc            | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | -------------- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | RUNNING | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      |
  
  
\== Status ==  
Current time: 2022-01-09 14:52:08 (running for 00:01:35.56)  
Memory usage on this node: 10.0/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 1.0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 RUNNING)  

| Trial name                            | status  | loc            | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | -------------- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | RUNNING | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      |
  
  
\== Status ==  
Current time: 2022-01-09 14:52:13 (running for 00:01:40.58)  
Memory usage on this node: 9.9/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 1.0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 RUNNING)  

| Trial name                            | status  | loc            | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | -------------- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | RUNNING | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      |
  
  
\== Status ==  
Current time: 2022-01-09 14:52:18 (running for 00:01:45.60)  
Memory usage on this node: 9.9/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 1.0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 RUNNING)  

| Trial name                            | status  | loc            | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | -------------- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | RUNNING | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      |
  
  
\== Status ==  
Current time: 2022-01-09 14:52:23 (running for 00:01:50.62)  
Memory usage on this node: 10.1/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 1.0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 RUNNING)  

| Trial name                            | status  | loc            | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | -------------- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | RUNNING | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      |
  
  
\== Status ==  
Current time: 2022-01-09 14:52:28 (running for 00:01:55.63)  
Memory usage on this node: 10.1/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 1.0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 RUNNING)  

| Trial name                            | status  | loc            | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | -------------- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | RUNNING | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      |
  
  
\== Status ==  
Current time: 2022-01-09 14:52:33 (running for 00:02:00.66)  
Memory usage on this node: 10.1/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 1.0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 RUNNING)  

| Trial name                            | status  | loc            | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | -------------- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | RUNNING | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      |
  
  
\== Status ==  
Current time: 2022-01-09 14:52:38 (running for 00:02:05.68)  
Memory usage on this node: 10.1/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 1.0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 RUNNING)  

| Trial name                            | status  | loc            | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | -------------- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | RUNNING | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      |
  
  
\== Status ==  
Current time: 2022-01-09 14:52:43 (running for 00:02:10.69)  
Memory usage on this node: 10.1/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 1.0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 RUNNING)  

| Trial name                            | status  | loc            | backbone      | lr         | optimizer |
| ------------------------------------- | ------- | -------------- | ------------- | ---------- | --------- |
| optimization\_objective\_657f0\_00000 | RUNNING | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      |
  
  
Result for optimization_objective_657f0_00000:
  date: 2022-01-09_14-52-48
  done: false
  experiment_id: f14d18631a8942e392e8b69780f61d85
  hostname: Anikets-Turing-Machine.local
  iterations_since_restore: 1
  node_ip: 127.0.0.1
  pid: 2443
  should_checkpoint: true
  time_since_restore: 132.34348511695862
  time_this_iter_s: 132.34348511695862
  time_total_s: 132.34348511695862
  timestamp: 1641720168
  timesteps_since_restore: 0
  train_accuracy: 0.005975634484635094
  train_loss: 5.911113500595093
  training_iteration: 1
  trial_id: 657f0_00000
  val_accuracy: 0.0
  val_loss: 137.33717279238851
  
Result for optimization_objective_657f0_00000:
  date: 2022-01-09_14-52-48
  done: true
  experiment_id: f14d18631a8942e392e8b69780f61d85
  experiment_tag: 0_backbone=ssl_resnet18,lr=0.0033306,optimizer=adam
  hostname: Anikets-Turing-Machine.local
  iterations_since_restore: 2
  node_ip: 127.0.0.1
  pid: 2443
  should_checkpoint: true
  time_since_restore: 132.47166109085083
  time_this_iter_s: 0.12817597389221191
  time_total_s: 132.47166109085083
  timestamp: 1641720168
  timesteps_since_restore: 0
  train_accuracy: 0.005975634484635094
  train_loss: 5.911113500595093
  training_iteration: 2
  trial_id: 657f0_00000
  val_accuracy: 0.0
  val_loss: 137.33717279238851
  
\== Status ==  
Current time: 2022-01-09 14:52:48 (running for 00:02:15.07)  
Memory usage on this node: 10.0/16.0 GiB  
Using FIFO scheduling algorithm.  
Resources requested: 0/8 CPUs, 0/0 GPUs, 0.0/4.28 GiB heap, 0.0/2.14 GiB objects  
Current best trial: 657f0\_00000 with train\_loss=5.911113500595093 and parameters={'backbone': 'ssl\_resnet18', 'lr': 0.0033306242909976825, 'optimizer': 'adam'}  
Result logdir: /Users/aniket/ray\_results/optimization\_objective\_2022-01-09\_14-50-33  
Number of trials: 1/1 (1 TERMINATED)  

| Trial name                            | status     | loc            | backbone      | lr         | optimizer | iter | total time (s) | val\_loss | train\_loss | train\_accuracy |
| ------------------------------------- | ---------- | -------------- | ------------- | ---------- | --------- | ---- | -------------- | --------- | ----------- | --------------- |
| optimization\_objective\_657f0\_00000 | TERMINATED | 127.0.0.1:2443 | ssl\_resnet18 | 0.00333062 | adam      | 2    | 132.472        | 137.337   | 5.91111     | 0.00597563      |
  
  
2022-01-09 14:52:48,404	INFO tune.py:630 -- Total run time: 135.22 seconds (135.06 seconds for the tuning loop).

completed!

In \[ \]:

Copied! 

# ray.shutdown()

\# ray.shutdown()

---

 Last update:May 18, 2022 