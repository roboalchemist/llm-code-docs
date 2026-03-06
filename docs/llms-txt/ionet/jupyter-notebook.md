# Source: https://io.net/docs/guides/clouds/jupyter-notebook.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Train a PyTorch Model on Fashion MNIST: Jupyter Notebook

> This document describes how to run a job on your cluster that distributes the training workload across multiple workers using Ray's distributed computing capabilities. This allows for parallelizing the training process and potentially reducing the overall training time. In the instructions below, we run Train a PyTorch Model on Fashion MNIST job using Jupyter Notebook.

For more information about Jupyter Notebook, see their [documentation](https://docs.jupyter.org/en/latest/).

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/j2Idm_VOJAM" title="Easy Model Training with Ray Cluster  on IO Cloud" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

## Table of Contents

* [Steps to run a test job in Jupyter Notebook](https://docs.io.net/docs/jupyter-notebook#steps-to-run-a-test-job-in-jupyter-notebook)
* [Congratulations on Successfully Training Your First Model](https://docs.io.net/docs/jupyter-notebook#congratulations-on-successfully-training-your-first-model)
* [Troubleshooting Model Training](https://docs.io.net/docs/jupyter-notebook#troubleshooting-model-training)

## Steps to run a test job in Jupyter Notebook:

1. After your cluster deployment is complete, go to **View Cluster**.

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8cca6a4-deployed.png?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=f744cc1e0221c4be71a8d77f68a82738" alt="" className="mx-auto" style={{ width:"66%" }} data-og-width="1098" width="1098" data-og-height="284" height="284" data-path="images/docs/8cca6a4-deployed.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8cca6a4-deployed.png?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=4291a330a46131cfb5b627b671925316 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8cca6a4-deployed.png?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=74558b238bc8083e03e88c6d908db95e 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8cca6a4-deployed.png?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=376e4c2d6e365a934d824a0ce7534f46 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8cca6a4-deployed.png?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=c1108349f755bcf25a7f4c8150a915fd 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8cca6a4-deployed.png?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=3712c28484f36de10e7bcdff23d38818 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8cca6a4-deployed.png?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=cce59523af3794f117e8d5864034b24e 2500w" />
   </Frame>
2. On the cluster detail page, copy the **IDE Password** and click **Jupyter Notebook**.

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d5cb98d636f8405c7ca7d68c3874193ace1d25659639d19a69334f81474f0da7-traininmodel1.jpg?fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=913b90b4b20bafdec5ec069beefdfc18" alt="" className="mx-auto" style={{ width:"68%" }} data-og-width="1235" width="1235" data-og-height="438" height="438" data-path="images/docs/d5cb98d636f8405c7ca7d68c3874193ace1d25659639d19a69334f81474f0da7-traininmodel1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d5cb98d636f8405c7ca7d68c3874193ace1d25659639d19a69334f81474f0da7-traininmodel1.jpg?w=280&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=3fadc3ac80d5b446d635b96da3eed87d 280w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d5cb98d636f8405c7ca7d68c3874193ace1d25659639d19a69334f81474f0da7-traininmodel1.jpg?w=560&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=656868ac3d7b6d663c10cc7c895a22d1 560w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d5cb98d636f8405c7ca7d68c3874193ace1d25659639d19a69334f81474f0da7-traininmodel1.jpg?w=840&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=85adb46ad023405208e61cd8826ff284 840w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d5cb98d636f8405c7ca7d68c3874193ace1d25659639d19a69334f81474f0da7-traininmodel1.jpg?w=1100&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=7062ed3531a822aa07c6d3769064ff4b 1100w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d5cb98d636f8405c7ca7d68c3874193ace1d25659639d19a69334f81474f0da7-traininmodel1.jpg?w=1650&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=5b455f46bb164b054951580fffbd2076 1650w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d5cb98d636f8405c7ca7d68c3874193ace1d25659639d19a69334f81474f0da7-traininmodel1.jpg?w=2500&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=9d56a1a8182ba3c48df3939cad19da26 2500w" />
   </Frame>
3. Enter your **IDE Password** you copied in the **Jupyter** password field.

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a07a40fb534a97f28398effc7d6cdf577779ca3f1f3e7d9739e2e0c001eae8a3-traininmodel8.jpg?fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=d2d20bf3b87e8aa20ca98491715c89d9" alt="" className="mx-auto" style={{ width:"55%" }} data-og-width="734" width="734" data-og-height="398" height="398" data-path="images/docs/a07a40fb534a97f28398effc7d6cdf577779ca3f1f3e7d9739e2e0c001eae8a3-traininmodel8.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a07a40fb534a97f28398effc7d6cdf577779ca3f1f3e7d9739e2e0c001eae8a3-traininmodel8.jpg?w=280&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=09b0c844f56a122c2dbc9903cec96b44 280w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a07a40fb534a97f28398effc7d6cdf577779ca3f1f3e7d9739e2e0c001eae8a3-traininmodel8.jpg?w=560&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=9c9e8572d15e2247325f05253b64159e 560w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a07a40fb534a97f28398effc7d6cdf577779ca3f1f3e7d9739e2e0c001eae8a3-traininmodel8.jpg?w=840&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=fdbaef88c7f620e3623946e3b783bca1 840w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a07a40fb534a97f28398effc7d6cdf577779ca3f1f3e7d9739e2e0c001eae8a3-traininmodel8.jpg?w=1100&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=3faf8f18af642464b9dab55be693cd58 1100w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a07a40fb534a97f28398effc7d6cdf577779ca3f1f3e7d9739e2e0c001eae8a3-traininmodel8.jpg?w=1650&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=2fbad7fdcf3203a31181b831d43ddec8 1650w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a07a40fb534a97f28398effc7d6cdf577779ca3f1f3e7d9739e2e0c001eae8a3-traininmodel8.jpg?w=2500&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=c35b6f4805d1afa8cc11fe88fa0a1e43 2500w" />
   </Frame>
4. Click **File** to create a new Python Notebook.

   <Frame>
       <img src="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/27734160a29b3143229bee1f734a58f10457efe4e4cbcb9eeed9ff6b3d5e3fe6-traininmodel2.jpg?fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=5d77cf3921c87bade0bf8e2ad759d684" alt="" data-og-width="1568" width="1568" data-og-height="944" height="944" data-path="images/docs/27734160a29b3143229bee1f734a58f10457efe4e4cbcb9eeed9ff6b3d5e3fe6-traininmodel2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/27734160a29b3143229bee1f734a58f10457efe4e4cbcb9eeed9ff6b3d5e3fe6-traininmodel2.jpg?w=280&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=c29860007b124c03cb17406873f59be6 280w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/27734160a29b3143229bee1f734a58f10457efe4e4cbcb9eeed9ff6b3d5e3fe6-traininmodel2.jpg?w=560&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=ffff57059654cddc124dfb81dcfe83b8 560w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/27734160a29b3143229bee1f734a58f10457efe4e4cbcb9eeed9ff6b3d5e3fe6-traininmodel2.jpg?w=840&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=80bc13c963ffa7421c120f1826233087 840w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/27734160a29b3143229bee1f734a58f10457efe4e4cbcb9eeed9ff6b3d5e3fe6-traininmodel2.jpg?w=1100&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=c497294c8686fc0e1c98bd008f11614a 1100w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/27734160a29b3143229bee1f734a58f10457efe4e4cbcb9eeed9ff6b3d5e3fe6-traininmodel2.jpg?w=1650&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=cb10fe9125b7dc49066841f935e3f550 1650w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/27734160a29b3143229bee1f734a58f10457efe4e4cbcb9eeed9ff6b3d5e3fe6-traininmodel2.jpg?w=2500&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=a6f677e8d076399fcb9b33ec5b0d80ef 2500w" />
   </Frame>
5. In the **New** dropdown, select **Notebook**. It launches a new tab.

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3a9f10c224d4053617584b26f3d9f17d35d600c2209a1eecd95a7de7ea04b93c-traininmodel3.jpg?fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=f80cba2da319f467ee3b21ab3ffca872" alt="" className="mx-auto" style={{ width:"67%" }} data-og-width="1020" width="1020" data-og-height="652" height="652" data-path="images/docs/3a9f10c224d4053617584b26f3d9f17d35d600c2209a1eecd95a7de7ea04b93c-traininmodel3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3a9f10c224d4053617584b26f3d9f17d35d600c2209a1eecd95a7de7ea04b93c-traininmodel3.jpg?w=280&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=b6c4c6cf326b1c0393896aef49b4af5e 280w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3a9f10c224d4053617584b26f3d9f17d35d600c2209a1eecd95a7de7ea04b93c-traininmodel3.jpg?w=560&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=358d96dac5d0520f5a8738e484807b5e 560w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3a9f10c224d4053617584b26f3d9f17d35d600c2209a1eecd95a7de7ea04b93c-traininmodel3.jpg?w=840&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=1be99d1205868b1d7bb9f32431d61034 840w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3a9f10c224d4053617584b26f3d9f17d35d600c2209a1eecd95a7de7ea04b93c-traininmodel3.jpg?w=1100&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=3569dc6c9f937f2a2d1027cfc8f1692b 1100w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3a9f10c224d4053617584b26f3d9f17d35d600c2209a1eecd95a7de7ea04b93c-traininmodel3.jpg?w=1650&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=50a43adff384fb92184ed074d9ec3587 1650w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/3a9f10c224d4053617584b26f3d9f17d35d600c2209a1eecd95a7de7ea04b93c-traininmodel3.jpg?w=2500&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=5981bdcd48d943d53baa61f6a5c46dab 2500w" />
   </Frame>
6. A new notebook will open in a new browser tab with a prompt to select a kernel. Choose **Python 3** for this example, then click **Select**.

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f15613067182fa62c950dc70e8c4de5827fdbf5aadc48726028d68ee226d4913-traininmodel6.jpg?fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=bd66f966c437c5653b7472c42b932ac0" alt="" className="mx-auto" style={{ width:"71%" }} data-og-width="872" width="872" data-og-height="368" height="368" data-path="images/docs/f15613067182fa62c950dc70e8c4de5827fdbf5aadc48726028d68ee226d4913-traininmodel6.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f15613067182fa62c950dc70e8c4de5827fdbf5aadc48726028d68ee226d4913-traininmodel6.jpg?w=280&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=3b63a6edc419dc2cb09b2a33024c1ebb 280w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f15613067182fa62c950dc70e8c4de5827fdbf5aadc48726028d68ee226d4913-traininmodel6.jpg?w=560&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=fa859e6ebc42e7ec437990109ac47d1a 560w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f15613067182fa62c950dc70e8c4de5827fdbf5aadc48726028d68ee226d4913-traininmodel6.jpg?w=840&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=2aa2027b12a4b2d0995959f16e0c3d40 840w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f15613067182fa62c950dc70e8c4de5827fdbf5aadc48726028d68ee226d4913-traininmodel6.jpg?w=1100&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=d83e5334ad34f77e4417cc7a0c8cb2dd 1100w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f15613067182fa62c950dc70e8c4de5827fdbf5aadc48726028d68ee226d4913-traininmodel6.jpg?w=1650&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=d320b474f14d3547ad4d5f972e5cf09b 1650w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f15613067182fa62c950dc70e8c4de5827fdbf5aadc48726028d68ee226d4913-traininmodel6.jpg?w=2500&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=bab95d794e5dae842de15cfce1f02757 2500w" />
   </Frame>
7. Enter the code sample below into a cell and click **Run**.

   <CodeGroup>
     ```python Python theme={null}
     import os
     from typing import Dict

     import torch
     from filelock import FileLock
     from torch import nn
     from torch.utils.data import DataLoader
     from torchvision import datasets, transforms
     from torchvision.transforms import Normalize, ToTensor
     from tqdm import tqdm

     import ray.train
     from ray.train import ScalingConfig
     from ray.train.torch import TorchTrainer

     def get_dataloaders(batch_size):
         transform = transforms.Compose([ToTensor(), Normalize((0.5,), (0.5,))])

         with FileLock(os.path.expanduser("~/data.lock")):
             training_data = datasets.FashionMNIST(
                 root="~/data",
                 train=True,
                 download=True,
                 transform=transform,
             )

             test_data = datasets.FashionMNIST(
                 root="~/data",
                 train=False,
                 download=True,
                 transform=transform,
             )

         train_dataloader = DataLoader(training_data, batch_size=batch_size, shuffle=True)
         test_dataloader = DataLoader(test_data, batch_size=batch_size)

         return train_dataloader, test_dataloader

     class NeuralNetwork(nn.Module):
         def __init__(self):
             super(NeuralNetwork, self).__init__()
             self.flatten = nn.Flatten()
             self.linear_relu_stack = nn.Sequential(
                 nn.Linear(28 * 28, 512),
                 nn.ReLU(),
                 nn.Dropout(0.25),
                 nn.Linear(512, 512),
                 nn.ReLU(),
                 nn.Dropout(0.25),
                 nn.Linear(512, 10),
                 nn.ReLU(),
             )

         def forward(self, x):
             x = self.flatten(x)
             logits = self.linear_relu_stack(x)
             return logits

     def train_func_per_worker(config: Dict):
         lr = config["lr"]
         epochs = config["epochs"]
         batch_size = config["batch_size_per_worker"]

         train_dataloader, test_dataloader = get_dataloaders(batch_size=batch_size)

         train_dataloader = ray.train.torch.prepare_data_loader(train_dataloader)
         test_dataloader = ray.train.torch.prepare_data_loader(test_dataloader)

         model = NeuralNetwork()

         model = ray.train.torch.prepare_model(model)

         loss_fn = nn.CrossEntropyLoss()
         optimizer = torch.optim.SGD(model.parameters(), lr=lr, momentum=0.9)

         # Model training loop
         for epoch in range(epochs):
             if ray.train.get_context().get_world_size() > 1:
                 train_dataloader.sampler.set_epoch(epoch)

             model.train()
             for X, y in tqdm(train_dataloader, desc=f"Train Epoch {epoch}"):
                 pred = model(X)
                 loss = loss_fn(pred, y)

                 optimizer.zero_grad()
                 loss.backward()
                 optimizer.step()

             model.eval()
             test_loss, num_correct, num_total = 0, 0, 0
             with torch.no_grad():
                 for X, y in tqdm(test_dataloader, desc=f"Test Epoch {epoch}"):
                     pred = model(X)
                     loss = loss_fn(pred, y)

                     test_loss += loss.item()
                     num_total += y.shape[0]
                     num_correct += (pred.argmax(1) == y).sum().item()

             test_loss /= len(test_dataloader)
             accuracy = num_correct / num_total

             ray.train.report(metrics={"loss": test_loss, "accuracy": accuracy})

     def train_fashion_mnist(num_workers=2, use_gpu=False):
         global_batch_size = 32

         train_config = {
             "lr": 1e-3,
             "epochs": 10,
             "batch_size_per_worker": global_batch_size // num_workers,
         }

         # Configure computation resources
         scaling_config = ScalingConfig(num_workers=num_workers, use_gpu=use_gpu)

         # Initialize a Ray TorchTrainer
         trainer = TorchTrainer(
             train_loop_per_worker=train_func_per_worker,
             train_loop_config=train_config,
             scaling_config=scaling_config,
         )

         result = trainer.fit()
         print(f"Training result: {result}")
     ```
   </CodeGroup>

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8b19d23cdbe0ff6004e93cbbe9089d0d13f816020a9cc1cad041e17ec157c028-traininmodel5.jpg?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=01cb96bdecd4553c43da892948c5b500" alt="" className="mx-auto" style={{ width:"77%" }} data-og-width="1790" width="1790" data-og-height="490" height="490" data-path="images/docs/8b19d23cdbe0ff6004e93cbbe9089d0d13f816020a9cc1cad041e17ec157c028-traininmodel5.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8b19d23cdbe0ff6004e93cbbe9089d0d13f816020a9cc1cad041e17ec157c028-traininmodel5.jpg?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=c62ce8f3bbbd20e74a9f8b8105a494f8 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8b19d23cdbe0ff6004e93cbbe9089d0d13f816020a9cc1cad041e17ec157c028-traininmodel5.jpg?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=c1453890dbaceb6aa0acb7e4803fe054 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8b19d23cdbe0ff6004e93cbbe9089d0d13f816020a9cc1cad041e17ec157c028-traininmodel5.jpg?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=d507de5c7f9386e01d3237e503387721 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8b19d23cdbe0ff6004e93cbbe9089d0d13f816020a9cc1cad041e17ec157c028-traininmodel5.jpg?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=9eeb86d5b791168281f3ef8c2648e64e 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8b19d23cdbe0ff6004e93cbbe9089d0d13f816020a9cc1cad041e17ec157c028-traininmodel5.jpg?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=de8f781dfa7b61d375b506b69bc3a9d1 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8b19d23cdbe0ff6004e93cbbe9089d0d13f816020a9cc1cad041e17ec157c028-traininmodel5.jpg?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=7229883e821068335f570a48a5b9af57 2500w" />
   </Frame>
8. Enter the **Python command** below in a new cell to run the training model script. Then click **Run**.

   <CodeGroup>
     ```python python theme={null}
     train_fashion_mnist(num_workers=2, use_gpu=True)
     ```
   </CodeGroup>

   <Info>
     Note, by default, 2 CPUs and a GPU are set for this command. Make sure that your hardware has enough CPU and GPU available, increase or reduce the allocation if needed.
   </Info>

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/bc3157cc357f4fae0cb040e768fce9b6666bf761ccb4ee9395816bac85dad552-traininmodel11.jpg?fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=b7ef45eddfb5dcc2325f5e9c133c7f1e" alt="" className="mx-auto" style={{ width:"75%" }} data-og-width="1110" width="1110" data-og-height="390" height="390" data-path="images/docs/bc3157cc357f4fae0cb040e768fce9b6666bf761ccb4ee9395816bac85dad552-traininmodel11.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/bc3157cc357f4fae0cb040e768fce9b6666bf761ccb4ee9395816bac85dad552-traininmodel11.jpg?w=280&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=76c88a68d9117fda20d0e6e5d8fa6eff 280w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/bc3157cc357f4fae0cb040e768fce9b6666bf761ccb4ee9395816bac85dad552-traininmodel11.jpg?w=560&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=41237fb9822b866bc30e9b170ca73de0 560w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/bc3157cc357f4fae0cb040e768fce9b6666bf761ccb4ee9395816bac85dad552-traininmodel11.jpg?w=840&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=000c2ca127dc6e0587d7bc41e2535e0d 840w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/bc3157cc357f4fae0cb040e768fce9b6666bf761ccb4ee9395816bac85dad552-traininmodel11.jpg?w=1100&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=18e2704ff623ee618d00eb4a4e271897 1100w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/bc3157cc357f4fae0cb040e768fce9b6666bf761ccb4ee9395816bac85dad552-traininmodel11.jpg?w=1650&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=d4b7e73d68ffd0e451140590dc681656 1650w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/bc3157cc357f4fae0cb040e768fce9b6666bf761ccb4ee9395816bac85dad552-traininmodel11.jpg?w=2500&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=a32dceec2e1bc4351db737d4330a6796 2500w" />
   </Frame>
9. If you scroll to the bottom of the output, you will see the training result.

   <CodeGroup>
     ```python python theme={null}
     Training result: Result(
       metrics={'loss': 0.3572742183404133, 'accuracy': 0.8728},
       path='/home/ray/ray_results/TorchTrainer_2024-05-17_18-55-55/TorchTrainer_c3725_00000_0_2024-05-17_18-55-55',
       filesystem='local',
       checkpoint=None
     )
     ```
   </CodeGroup>

## Congratulations on Successfully Training Your First Model

You can now track your model's progress using the **Ray Dashboard.** The dashboard provides detailed insights into your cluster, including **cluster utilization, status, autoscaler activity, resource states**, and more.

1. Return to your cluster. On the cluster detail page, copy the **IDE Password** and click **Ray Dashboard**.

   <Frame>
       <img src="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/73bbddca679bf39b2af899a2083e4f157cdeb9b9210f98d20606ef5e071dfa9b-traininmodel9.jpg?fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=fc491cd18ba90af9c2a38b12c1c18ff6" alt="" data-og-width="1621" width="1621" data-og-height="516" height="516" data-path="images/docs/73bbddca679bf39b2af899a2083e4f157cdeb9b9210f98d20606ef5e071dfa9b-traininmodel9.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/73bbddca679bf39b2af899a2083e4f157cdeb9b9210f98d20606ef5e071dfa9b-traininmodel9.jpg?w=280&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=7d2cf5c08ae02affa6e8c8a1e13e517d 280w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/73bbddca679bf39b2af899a2083e4f157cdeb9b9210f98d20606ef5e071dfa9b-traininmodel9.jpg?w=560&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=64716a9dc6433d40760b70a35e2a25b7 560w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/73bbddca679bf39b2af899a2083e4f157cdeb9b9210f98d20606ef5e071dfa9b-traininmodel9.jpg?w=840&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=8d0893ccdd7a7c67e3bdf97cd61b4546 840w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/73bbddca679bf39b2af899a2083e4f157cdeb9b9210f98d20606ef5e071dfa9b-traininmodel9.jpg?w=1100&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=a89278edffbab52e231c0206f268bd40 1100w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/73bbddca679bf39b2af899a2083e4f157cdeb9b9210f98d20606ef5e071dfa9b-traininmodel9.jpg?w=1650&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=e29bd145a695e34d5e8a73392b998e75 1650w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/73bbddca679bf39b2af899a2083e4f157cdeb9b9210f98d20606ef5e071dfa9b-traininmodel9.jpg?w=2500&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=ff8087c38087ba2ec3c7dc6148997255 2500w" />
   </Frame>
2. In the password field, enter your password. Click **View All Jobs**. Here, you can see that your job is running.

   <Frame>
       <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8fdf7fd52bfcbcb6d0387a183eebbc7f18aed5b2eb01451a2c7ad9114aa53210-traininmodel7.jpg?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=211ca3e91b61f3d086bc5a6042c9bd61" alt="" data-og-width="1023" width="1023" data-og-height="251" height="251" data-path="images/docs/8fdf7fd52bfcbcb6d0387a183eebbc7f18aed5b2eb01451a2c7ad9114aa53210-traininmodel7.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8fdf7fd52bfcbcb6d0387a183eebbc7f18aed5b2eb01451a2c7ad9114aa53210-traininmodel7.jpg?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=281d4aad2c8142462ba8091a6d726724 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8fdf7fd52bfcbcb6d0387a183eebbc7f18aed5b2eb01451a2c7ad9114aa53210-traininmodel7.jpg?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=eb688526af0e7ebc15ee8e6cd444e6be 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8fdf7fd52bfcbcb6d0387a183eebbc7f18aed5b2eb01451a2c7ad9114aa53210-traininmodel7.jpg?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=c08f00a4336317873f7026728926d83e 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8fdf7fd52bfcbcb6d0387a183eebbc7f18aed5b2eb01451a2c7ad9114aa53210-traininmodel7.jpg?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=d0cd6500946f9a40905e7955b7157b53 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8fdf7fd52bfcbcb6d0387a183eebbc7f18aed5b2eb01451a2c7ad9114aa53210-traininmodel7.jpg?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=26cb6287155996e9ccf241e6a342c77b 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8fdf7fd52bfcbcb6d0387a183eebbc7f18aed5b2eb01451a2c7ad9114aa53210-traininmodel7.jpg?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=11a17d32f7aadeb6e46edf741f6d10d5 2500w" />
   </Frame>
3. You can also check this in io.net by going to **Clusters** > **select your cluster** > click an **IO Worker** > **Jobs**.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/249f44a-job_detail_2.png?fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=e99794130e22b52e9f35b8a8a7346280" alt="" className="mx-auto" style={{ width:"49%" }} data-og-width="806" width="806" data-og-height="1126" height="1126" data-path="images/docs/249f44a-job_detail_2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/249f44a-job_detail_2.png?w=280&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=61211331e6243c721757cfb298da8d78 280w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/249f44a-job_detail_2.png?w=560&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=10a2a5a5d0f87836cac52bce49df96fd 560w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/249f44a-job_detail_2.png?w=840&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=50af5de66e276d38f5af1e4b51ead187 840w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/249f44a-job_detail_2.png?w=1100&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=358dd3a8117c61aa7198a63c8d2b99a1 1100w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/249f44a-job_detail_2.png?w=1650&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=39bcc66f74f9e5a4f61f5046a187563e 1650w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/249f44a-job_detail_2.png?w=2500&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=5407bd4768f06ba24f9a08114199cab0 2500w" />
</Frame>

## Troubleshooting Model Training

1. If you see an error after running the example code that matches the one below:

   <CodeGroup>
     ```python python theme={null}
     2025-05-15 01:39:02,503	INFO util.py:154 -- Outdated packages:
       ipywidgets==7.7.2 found, needs ipywidgets>=8
     Run `pip install -U ipywidgets`, then restart the notebook server for rich notebook output.
     2025-05-15 01:39:03,181	INFO util.py:154 -- Outdated packages:
       ipywidgets==7.7.2 found, needs ipywidgets>=8
     Run `pip install -U ipywidgets`, then restart the notebook server for rich notebook output.
     2025-05-15 01:39:03,219	INFO util.py:154 -- Outdated packages:
       ipywidgets==7.7.2 found, needs ipywidgets>=8
     Run `pip install -U ipywidgets`, then restart the notebook server for rich notebook output.
     ```
   </CodeGroup>
2. Copy the update command for outdated packages, paste it into a new cell, and click the Run button to install the updates:

   <CodeGroup>
     ```python python theme={null}
     pip install -U ipywidgets
     ```
   </CodeGroup>
3. In the toolbar, click **Kernel** and select **Restart the kernel** from the dropdown. This updates the packages.

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d3ed96a94ffd83313a95cd28c0deb9b6cf498022b9d7d239d401b2cf99f001df-traininmodel4.jpg?fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=c6ea6bdd9b58e0236389ff1add1b4d0c" alt="" className="mx-auto" style={{ width:"67%" }} data-og-width="1172" width="1172" data-og-height="558" height="558" data-path="images/docs/d3ed96a94ffd83313a95cd28c0deb9b6cf498022b9d7d239d401b2cf99f001df-traininmodel4.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d3ed96a94ffd83313a95cd28c0deb9b6cf498022b9d7d239d401b2cf99f001df-traininmodel4.jpg?w=280&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=3c2af8b20d6a6ef470c3b47bd105b665 280w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d3ed96a94ffd83313a95cd28c0deb9b6cf498022b9d7d239d401b2cf99f001df-traininmodel4.jpg?w=560&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=b930af5a448965be1f7abfb0c80e551d 560w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d3ed96a94ffd83313a95cd28c0deb9b6cf498022b9d7d239d401b2cf99f001df-traininmodel4.jpg?w=840&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=0d5dc68e2026916639d2cd8c2d825743 840w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d3ed96a94ffd83313a95cd28c0deb9b6cf498022b9d7d239d401b2cf99f001df-traininmodel4.jpg?w=1100&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=476f6cce6ce4f1f5bb31e1555b797f59 1100w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d3ed96a94ffd83313a95cd28c0deb9b6cf498022b9d7d239d401b2cf99f001df-traininmodel4.jpg?w=1650&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=41b8ccb4b9dc872d0ddcd4434a874be0 1650w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d3ed96a94ffd83313a95cd28c0deb9b6cf498022b9d7d239d401b2cf99f001df-traininmodel4.jpg?w=2500&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=c392763ad3329f10746dad3bf0fe0c23 2500w" />
   </Frame>
4. Then paste the command again and run it to execute the script.
