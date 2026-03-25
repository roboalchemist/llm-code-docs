# Source: https://docs.wandb.ai/models/integrations/yolov5.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# YOLOv5

> Use the built-in W&B integration in YOLOv5 for experiment tracking, model versioning, and prediction visualization.

export const ColabLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="colab-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M14.25.18l.9.2.73.26.59.3.45.32.34.34.25.34.16.33.1.3.04.26.02.2-.01.13V8.5l-.05.63-.13.55-.21.46-.26.38-.3.31-.33.25-.35.19-.35.14-.33.1-.3.07-.26.04-.21.02H8.77l-.69.05-.59.14-.5.22-.41.27-.33.32-.27.35-.2.36-.15.37-.1.35-.07.32-.04.27-.02.21v3.06H3.17l-.21-.03-.28-.07-.32-.12-.35-.18-.36-.26-.36-.36-.35-.46-.32-.59-.28-.73-.21-.88-.14-1.05-.05-1.23.06-1.22.16-1.04.24-.87.32-.71.36-.57.4-.44.42-.33.42-.24.4-.16.36-.1.32-.05.24-.01h.16l.06.01h8.16v-.83H6.18l-.01-2.75-.02-.37.05-.34.11-.31.17-.28.25-.26.31-.23.38-.2.44-.18.51-.15.58-.12.64-.1.71-.06.77-.04.84-.02 1.27.05zm-6.3 1.98l-.23.33-.08.41.08.41.23.34.33.22.41.09.41-.09.33-.22.23-.34.08-.41-.08-.41-.23-.33-.33-.22-.41-.09-.41.09zm13.09 3.95l.28.06.32.12.35.18.36.27.36.35.35.47.32.59.28.73.21.88.14 1.04.05 1.23-.06 1.23-.16 1.04-.24.86-.32.71-.36.57-.4.45-.42.33-.42.24-.4.16-.36.09-.32.05-.24.02-.16-.01h-8.22v.82h5.84l.01 2.76.02.36-.05.34-.11.31-.17.29-.25.25-.31.24-.38.2-.44.17-.51.15-.58.13-.64.09-.71.07-.77.04-.84.01-1.27-.04-1.07-.14-.9-.2-.73-.25-.59-.3-.45-.33-.34-.34-.25-.34-.16-.33-.1-.3-.04-.25-.02-.2.01-.13v-5.34l.05-.64.13-.54.21-.46.26-.38.3-.32.33-.24.35-.2.35-.14.33-.1.3-.06.26-.04.21-.02.13-.01h5.84l.69-.05.59-.14.5-.21.41-.28.33-.32.27-.35.2-.36.15-.36.1-.35.07-.32.04-.28.02-.21V6.07h2.09l.14.01.21.03zm-6.47 14.25l-.23.33-.08.41.08.41.23.33.33.23.41.08.41-.08.33-.23.23-.33.08-.41-.08-.41-.23-.33-.33-.23-.41-.08-.41.08z" />
    </svg>
    Try in Colab
  </a>;

<ColabLink url="https://colab.research.google.com/github/wandb/examples/blob/master/colabs/yolo/Train_and_Debug_YOLOv5_Models_with_Weights_%26_Biases_.ipynb" />

[Ultralytics' YOLOv5](https://www.ultralytics.com/yolo) ("You Only Look Once") model family enables real-time object detection with convolutional neural networks without all the agonizing pain.

[W\&B](https://wandb.com) is directly integrated into YOLOv5, providing experiment metric tracking, model and dataset versioning, rich model prediction visualization, and more. **It's as easy as running a single `pip install` before you run your YOLO experiments.**

<Note>
  All W\&B logging features are compatible with data-parallel multi-GPU training, such as with [PyTorch DDP](https://pytorch.org/tutorials/intermediate/ddp_tutorial.html).
</Note>

## Track core experiments

Simply by installing `wandb`, you'll activate the built-in W\&B [logging features](/models/track/log/): system metrics, model metrics, and media logged to interactive [Dashboards](/models/track/workspaces/).

```python  theme={null}
pip install wandb
git clone https://github.com/ultralytics/yolov5.git
python yolov5/train.py  # train a small network on a small dataset
```

Just follow the links printed to the standard out by wandb.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/w-lBKSCruauC3-2f/images/integrations/yolov5_experiment_tracking.png?fit=max&auto=format&n=w-lBKSCruauC3-2f&q=85&s=174e65b51a49e649eb802ffddaf8a5d0" alt="All these charts and more." width="2424" height="2954" data-path="images/integrations/yolov5_experiment_tracking.png" />
</Frame>

## Customize the integration

By passing a few simple command line arguments to YOLO, you can take advantage of even more W\&B features.

* If you pass a number to `--save_period`, W\&B saves a [model version](/models/registry/) at the end of every `save_period` epochs. The model version includes the model weights and tags the best-performing model in the validation set.
* Turning on the `--upload_dataset` flag will also upload the dataset for data versioning.
* Passing a number to `--bbox_interval` will turn on [data visualization](../). At the end of every `bbox_interval` epochs, the outputs of the model on the validation set will be uploaded to W\&B.

<Tabs>
  <Tab title="Model Versioning Only">
    ```python  theme={null}
    python yolov5/train.py --epochs 20 --save_period 1
    ```
  </Tab>

  <Tab title="Model Versioning and Data Visualization">
    ```python  theme={null}
    python yolov5/train.py --epochs 20 --save_period 1 \
      --upload_dataset --bbox_interval 1
    ```
  </Tab>
</Tabs>

<Note>
  Every W\&B account comes with 100 GB of free storage for datasets and models.
</Note>

Here's what that looks like.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/w-lBKSCruauC3-2f/images/integrations/yolov5_model_versioning.png?fit=max&auto=format&n=w-lBKSCruauC3-2f&q=85&s=3a25b11f41892c377508bc0fb6969485" alt="Model versioning" width="852" height="328" data-path="images/integrations/yolov5_model_versioning.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/w-lBKSCruauC3-2f/images/integrations/yolov5_data_visualization.png?fit=max&auto=format&n=w-lBKSCruauC3-2f&q=85&s=c3985f3851ac8af2ddac95561e8e5715" alt="Data visualization" width="1277" height="736" data-path="images/integrations/yolov5_data_visualization.png" />
</Frame>

<Note>
  With data and model versioning, you can resume paused or crashed experiments from any device, no setup necessary. Check out [the Colab ](https://wandb.me/yolo-colab) for details.
</Note>
