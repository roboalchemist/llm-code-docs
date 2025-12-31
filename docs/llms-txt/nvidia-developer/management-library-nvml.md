# Source: https://developer.nvidia.com/management-library-nvml.md

# NVIDIA Management Library (NVML)

The NVIDIA Management Library (NVML) is a C-based programmatic interface for monitoring and managing various states within [Data Center GPUs](https://www.nvidia.com/en-us/data-center/). It is intended to be a platform for building 3rd party applications, and is also the underlying library for the NVIDIA-supported [nvidia-smi tool](https://docs.nvidia.com/deploy/nvidia-smi/index.html). NVML is thread-safe so it is safe to make simultaneous NVML calls from multiple threads.

### Query-able states includes:

- Identification: Various dynamic and static information is reported, including board serial numbers, PCI device ids, VBIOS/Inforom version numbers and product names. 
- GPU utilization: Current utilization rates are reported for both the compute resources of the GPU and the memory interface.
- ECC error counts: Both correctable single bit and detectable double bit errors are reported. Error counts are provided for both the current boot cycle and for the lifetime of the GPU.
- Temperature and fan speed: The current core GPU temperature is reported, along with fan speeds for non-passive products.
- Power management: For supported products, the current board power draw and power limits are reported.
- Active compute process: The list of active processes running on the GPU is reported, along with the corresponding process name/id and allocated GPU memory.
- Clocks and PState: Max and current clock rates are reported for several important clock domains, as well as the current GPU performance state.

### Modifiable state includes:

- ECC mode: Enable and disable ECC.
- ECC reset: Clear single and double bit ECC error counts.
- Compute mode: Control whether compute processes can run on the GPU and whether they run exclusively or concurrently with other compute processes.
- Persistence mode: Control whether the NVIDIA driver stays loaded when no active clients are connected to the GPU.

The NVIDIA Management Library can be downloaded as part of the [NVIDIA GPU Driver](https://www.nvidia.com/en-us/drivers/) for Linux and Windows.

### Additional References

- [NVML API Reference](https://docs.nvidia.com/deploy/nvml-api/index.html)
- [NVML Python Bindings](https://pypi.org/project/nvidia-ml-py/)


