# Source: https://apple.github.io/coremltools/source/coremltools.optimize.html

# Optimizers[](#optimizers "Link to this heading")

To deploy models on devices such as the iPhone, you often need to optimize the models to use less storage space, reduce power consumption, and reduce latency during inference. For an overview, see Optimizing Models Post-Training ([Compressing ML Program Weights](https://coremltools.readme.io/docs/compressing-ml-program-weights) and [Compressing Neural Network Weights](https://coremltools.readme.io/docs/quantization)).

## PyTorch[](#pytorch "Link to this heading")

Compression for PyTorch models:

- [Palettization](coremltools.optimize.torch.palettization.html)
- [Pruning](coremltools.optimize.torch.pruning.html)
- [Quantization](coremltools.optimize.torch.quantization.html)
- [Examples](coremltools.optimize.torch.examples.html)

## Core ML[](#core-ml "Link to this heading")

Compression for Core ML models:

- [Palettization](coremltools.optimize.coreml.palettization.html)
- [Pruning](coremltools.optimize.coreml.pruning.html)
- [Quantization](coremltools.optimize.coreml.quantization.html)
- [Utilities](coremltools.optimize.coreml.utilities.html)