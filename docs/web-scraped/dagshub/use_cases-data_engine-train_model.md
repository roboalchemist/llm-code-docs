# Source: https://dagshub.com/docs/use_cases/data_engine/train_model/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/use_cases/data_engine/train_model.md "Edit this page")

# Training a model with your dataset[¶](#training-a-model-with-your-dataset "Permanent link")

Now that you created new datasets, the next step will be to train and improve your model with it. Data Engine supports the **PyTorch** and **TensorFlow** frameworks out of the box to easily create data loaders and datasets for your model training.

## Working with Dataloaders[¶](#working-with-dataloaders "Permanent link")

Data Engineâ€™s DataLoaders extend the following classes:

- `torch.utils.data.DataLoader` for PyTorch
- `tf.keras.utils.Sequence` for TensorFlow
- `datasets.arrow_dataset.Dataset` for HuggingFace Datasets

Info

For HuggingFace Datasets, the paths of the downloaded datapoints are passed, and can be used with `cast_column()` for conversions to a format required by your framework of choice.

For each [`QueryResult`](https://dagshub.com/docs/client/reference/data_engine/query_result.html#module-dagshub.data_engine.model.query_result), we can get a native dataset for PyTorch, TensorFlow or HuggingFace, which you can use to train your model.

### Creating a Dataloader[¶](#creating-a-dataloader "Permanent link")

The easiest way to get a dataloader from your enriched dataset is to use the following function:

PyTorchTensorFlowHuggingFace

Info

For more information on how to best utilize HuggingFace datasets, check out [HuggingFaces\' documentation](https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Dataset.cast_column).

For PyTorch and TensorFlow, Data Engine automatically guesses the data type from the path (thereâ€™s built-in support for images, audio, video, and numeric formats), and converts each file to a tensor you can use for training.

By default, files are downloaded from your project only as requested, so you donâ€™t download anything you donâ€™t use. This allows you to start training immediately without needing to first download the entire dataset.

However, all these things are customizable. Below is a full explanation of the dataloader functionality.

### Full Dataloader Functionality[¶](#full-dataloader-functionality "Permanent link")

Given the above `query_res` object, you can convert it to a dataloader with the following options:

PyTorchTensorFlow

- `flavor`**:** supports `torch` or `tensorflow`. Choose the one you need depending on your training framework.

- `metadata_columns`: To support extensible multimodal data use cases with varying model I/O as well as getting labels into your dataloader, we added the `metadata_columns` argument. Select which columns you would like to extract from the metadata by specifying a list of metadata column names to `metadata_columns` as strings. The dataloaders will return a list of all the tensorized columns.

- `strategy`**:** dataloaders stream data from the cloud remote in order to facilitate training. There are multiple ways of doing this, and the best strategy usually depends on the compute at hand as well as the scenario within which you are using the dataloaders. You can choose from the following inputs:
  - `'lazy'`: Downloads as indices are requested. Intended for compute or storage hardware, where having your entire dataset at hand is not possible.
  - `'background'`: As itâ€™s name suggests â€" download data in the background while continuing to let you work in your IDE. If an item is requested that isn\'t already downloaded, that item will be prioritized and downloaded immediately. This is the ideal for interactive work, or when the time it takes to train on a batch is much longer than the time it take to download one.
  - `'preload'`: Downloads all the data before finishing the function and returning the dataloader object. This is best when training on batches is much faster than downloading them, or when avoiding dataloader delays is critical (GPU clusters where jobs have strict timeouts).

- `tensorizers`: Most data isnâ€™t stored as tensors, and must be converted into tensor format for training. Since objects can be of a different type (file paths, annotations, numbers, etc.) you can let Data Engine guess how best to convert each data and metadata column to tensor format, or provide a list of custom functions that get the column value and convert it to the appropriate tensor. This can help in cases where you need to do custom processing, for example normalizing an image, before inputting it into your model. The supported options:

  - `'auto'` - in this case the data types of the columns will be automatically declared and tensorized, by checking the file extension to see if there is a match.

  ::::: 
  ::: tabbed-labels
  PyTorchTensorFlow
  :::

  ::: tabbed-content
  :::
  :::::

  - `'image'|'audio'|'video'`- You can provide a single string if all the datatypes within columns are the same â€" for example in an image-to-image task, you can just send in a string and it will use the same tensorizer for all cases:

  ::::: 
  ::: tabbed-labels
  PyTorchTensorFlow
  :::

  ::: tabbed-content
  :::
  :::::

  For multi-modal data, such as image to video, you can provide a list of datatype strings â€" each type will be sequentially parsed with column:

  ::::: 
  ::: tabbed-labels
  PyTorchTensorFlow
  :::

  ::: tabbed-content
  :::
  :::::

  You can also provide a single function that takes as input each field, and can merged and converted to any desired format:

  ::::: 
  ::: tabbed-labels
  PyTorchTensorFlow
  :::

  ::: tabbed-content
  :::
  :::::

  - Data Engine also supports custom tensor conversion functions. You can supply a list of functions, each with signature `filepath: str â†’ <torch.Tensor>|<tf.Tensor>` depending on your framework of choice. The actual output type specification is not enforced, which means if you have a model that takes as input a dictionary from a single column within your dataset, you can write a tensorizer to do just that, and it wonâ€™t complain. For example, if we want to normalize our images in an image-to-image task we can use the following code:

    ::: highlight
        def image_norm(file: str) -> torch.Tensor:
            img_tensor = torchvision.io.read_image(file).type(torch.float)
            img_tensor = (img_tensor - torch.min(img_tensor)) / (torch.max(img_tensor) - torch.min(img_tensor))
            return img_tensor

        dl = query_res.all().as_ml_dataloader(flavor='torch', metadata_columns=["label_path"], batch_size=4,
                                              tensorizers=[image_norm, image_norm])
    :::
  - `**kwargs`: Use [Torch documentation](https://pytorch.org/docs/stable/index.html) or [TensorFlow documentation](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Sequence) for additional keyword arguments you can supply to the data loader.

List of tensorizers

Note: In all cases where you supply a list of tensorizers, the number of items in that list should be one more than the number of items in the `metadata_columns` list. The first tensorizer will always be applied to the input data path.

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).