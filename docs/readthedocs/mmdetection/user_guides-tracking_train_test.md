# Learn to train and test

## Train

This section will show how to train existing models on supported datasets.
The following training environments are supported:

- 

CPU

- 

single GPU

- 

single node multiple GPUs

- 

multiple nodes

You can also manage jobs with Slurm.

Important:

- 

You can change the evaluation interval during training by modifying the `train_cfg` as
`train_cfg = dict(val_interval=10)`. That means evaluating the model every 10 epochs.

- 

The default learning rate in all config files is for 8 GPUs.
According to the Linear Scaling Rule [https://arxiv.org/abs/1706.02677],
you need to set the learning rate proportional to the batch size if you use different GPUs or images per GPU,
e.g., `lr=0.01` for 8 GPUs * 1 img/gpu and lr=0.04 for 16 GPUs * 2 imgs/gpu.

- 

During training, log files and checkpoints will be saved to the working directory,
which is specified by CLI argument `--work-dir`. It uses `./work_dirs/CONFIG_NAME` as default.

- 

If you want the mixed precision training, simply specify CLI argument `--amp`.

### 1. Train on CPU

The model is default put on cuda device.
Only if there are no cuda devices, the model will be put on cpu.
So if you want to train the model on CPU, you need to `export CUDA_VISIBLE_DEVICES=-1` to disable GPU visibility first.
More details in MMEngine [https://github.com/open-mmlab/mmengine/blob/ca282aee9e402104b644494ca491f73d93a9544f/mmengine/runner/runner.py#L849-L850].

```
CUDA_VISIBLE_DEVICES=-1 python tools/train.py ${CONFIG_FILE} [optional arguments]

```