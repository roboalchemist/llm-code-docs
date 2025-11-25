# Source: https://docs.comfy.org/installation/system_requirements.md

# System Requirements

> This guide introduces some system requirements for ComfyUI, including hardware and software requirements

In this guide, we will introduce the system requirements for installing ComfyUI. Due to frequent updates of ComfyUI, this document may not be updated in a timely manner. Please refer to the relevant instructions in [ComfyUI](https://github.com/comfyanonymous/ComfyUI).

Regardless of which version of ComfyUI you use, it runs in a separate Python environment.

### System Requirements

Currently, we support the following operating systems:

* Windows
* Linux
* macOS (supports Apple Silicon, such as the M series)

You can refer to the following sections to learn about the installation methods for different systems and versions of ComfyUI. In the installation of different versions, we have simply described the system requirements.

<AccordionGroup>
  <Accordion title="ComfyUI Desktop">
    ComfyUI Desktop currently supports standalone installation for **Windows and MacOS (ARM)**, currently in Beta

    * Code is open source on [Github](https://github.com/Comfy-Org/desktop)

    <Tip>
      Because Desktop is always built based on the **stable release**, so the latest updates may take some time to experience for Desktop, if you want to always experience the latest version, please use the portable version or manual installation
    </Tip>

    You can choose the appropriate installation for your system and hardware below

    <Tabs>
      <Tab title="Windows">
        <Card title="ComfyUI Desktop (Windows) Installation Guide" icon="link" href="/installation/desktop/windows">
          Suitable for **Windows** version with **Nvidia** GPU
        </Card>
      </Tab>

      <Tab title="MacOS(Apple Silicon)">
        <Card title="ComfyUI Desktop (MacOS) Installation Guide" icon="link" href="/installation/desktop/macos">
          Suitable for MacOS with **Apple Silicon**
        </Card>
      </Tab>

      <Tab title="Linux">
        <Note>ComfyUI Desktop **currently has no Linux prebuilds**, please visit the [Manual Installation](/installation/manual_install) section to install ComfyUI</Note>
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="ComfyUI Portable (Windows)">
    Portable version is a ComfyUI version that integrates an independent embedded Python environment, using the portable version you can experience the latest features, currently only supports **Windows** system

    <Card title="ComfyUI Portable (Windows) Installation Guide" icon="link" href="/installation/comfyui_portable_windows">
      Supports **Windows** ComfyUI version running on **Nvidia GPUs** or **CPU-only**, always use the latest commits and completely portable.
    </Card>
  </Accordion>

  <Accordion title="Manual Installation">
    <Card title="ComfyUI Manual Installation Guide" icon="link" href="/installation/manual_install">
      Supports all system types and GPU types (Nvidia, AMD, Intel, Apple Silicon, Ascend NPU, Cambricon MLU)
    </Card>
  </Accordion>
</AccordionGroup>

### Python Version

* Recommended Python 3.12
* Supports Python 3.13 (some custom nodes may not be compatible)

### Supported Hardware

* NVIDIA GPU
* AMD GPU
* Intel GPU (includes Arc series, supports IPEX)
* Apple Silicon (M1/M2)
* Ascend NPU
* Cambricon MLU
* CPU (can use the --cpu parameter, slower)

Please refer to the [ComfyUI Windows and Linux manual installation section](https://github.com/comfyanonymous/ComfyUI?tab=readme-ov-file#manual-install-windows-linux) for detailed installation steps.

<Note>
  The stable version of PyTorch 2.7 now supports the Blackwell architecture (CUDA 12.8), and the core and desktop versions of ComfyUI have adopted this version.
</Note>

### Dependencies

* Install PyTorch
* Install all dependencies in the requirements.txt of ComfyUI

<Card title="Manual Installation" icon="book" href="/installation/manual_install">
  Please refer to the manual installation section for detailed installation steps.
</Card>
