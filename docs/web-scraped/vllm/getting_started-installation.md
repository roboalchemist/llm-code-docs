# Source: https://docs.vllm.ai/en/stable/getting_started/installation/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/getting_started/installation/README.md "Edit this page")

# Installation[¶](#installation "Permanent link")

vLLM supports the following hardware platforms:

-   [GPU](gpu/)
    -   [NVIDIA CUDA](gpu/#nvidia-cuda)
    -   [AMD ROCm](gpu/#amd-rocm)
    -   [Intel XPU](gpu/#intel-xpu)
-   [CPU](cpu/)
    -   [Intel/AMD x86](cpu/#intelamd-x86)
    -   [ARM AArch64](cpu/#arm-aarch64)
    -   [Apple silicon](cpu/#apple-silicon)
    -   [IBM Z (S390X)](cpu/#ibm-z-s390x)

## Hardware Plugins[¶](#hardware-plugins "Permanent link")

The backends below live **outside** the main `vllm` repository and follow the [Hardware-Pluggable RFC](../../design/plugin_system/).

  Accelerator                   PyPI / package             Repository
  ----------------------------- -------------------------- -------------------------------------------------
  Google TPU                    `tpu-inference`            <https://github.com/vllm-project/tpu-inference>
  Ascend NPU                    `vllm-ascend`              <https://github.com/vllm-project/vllm-ascend>
  Intel Gaudi (HPU)             N/A, install from source   <https://github.com/vllm-project/vllm-gaudi>
  MetaX MACA GPU                N/A, install from source   <https://github.com/MetaX-MACA/vLLM-metax>
  Rebellions ATOM / REBEL NPU   `vllm-rbln`                <https://github.com/rebellions-sw/vllm-rbln>
  IBM Spyre AIU                 `vllm-spyre`               <https://github.com/vllm-project/vllm-spyre>
  Cambricon MLU                 `vllm-mlu`                 <https://github.com/Cambricon/vllm-mlu>
  Baidu Kunlun XPU              N/A, install from source   <https://github.com/baidu/vLLM-Kunlun>

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [December 11, 2025] ]