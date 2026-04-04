# Source: https://developer.nvidia.com/cuda-gdb.md

# CUDA-GDB

When developing massively parallel applications on the GPU, you need a debugger capable of handling thousands of threads running simultaneously on each GPU in the system.  CUDA-GDB delivers a seamless debugging experience that allows you to debug both the CPU and GPU portions of your application simultaneously.

If you already use GDB to debug your CPU application then getting started with CUDA-GDB involves learning just a few additional debugger commands. Just like GDB, CUDA-GDB provides a console-based debugging interface you can use from the command line on your local system or any remote system on which you have Telnet or SSH access. If you prefer debugging with a GUI frontend, CUDA-GDB also supports integration with [DDD](https://www.gnu.org/software/ddd), [EMACS](https://www.gnu.org/software/emacs), [Nsight Eclipse Edition](/nsight-eclipse-edition) or the new [Nsight Visual Studio Code Edition](/nsight-visual-studio-code-edition)

Note that [NVIDIA® CUDA Toolkit 11.0](https://developer.nvidia.com/cuda-toolkit) (and later) no longer supports development or running applications on macOS. While there are no tools which use macOS as a target environment, NVIDIA made the [macOS host version of cuda-gdb available up to CUDA 12.4](/nvidia-cuda-toolkit-12_4_0-developer-tools-mac-hosts). However, the macOS host versions were dropped as of CUDA 12.5.

|   | [![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuda/images/buttons/production_download.png)](/cuda-downloads) |   | [![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuda/images/buttons/cuda_prerelease_learnmore_button.png)](/cuda-toolkit) |   | [![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/tools/MacHosts/cuda_gdb_debugAPI_UD_preview.png)](/nvidia-cuda-toolkit-cuda-gdb-developer-preview) |   |

### CUDA-GDB Feature Set Overview

CUDA-GDB supports debugging of both 32 and 64-bit CUDA C/C++ applications. It provides full control over the execution of the CUDA application including breakpoints and single-stepping. You can examine variables, read/write memory and registers and inspect the GPU state when the application is suspended. Third party developers can leverage CUDA-GDB powerful features directly, see **CUDA Samples,** which can be downloaded with the latest [CUDA Toolkit .](/cuda-downloads)

| 

![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuda/images/toolsscreenshots/cuda-gdb-screenshot-1.png &quot;Click to zoom/shrink&quot;)  
 (Click to zoom)

 | 

**CUDA-GDB on Linux**  
\&gt; Debug CUDA C and C++ applications directly on the GPU  
\&gt; Simultaneously debug on the CPU and more GPUs  
\&gt; Debug at either high-level C/C++ source or low-level GPU assembly  
\&gt; Use conditional breakpoints to identify and correct errors in CUDA code  
\&gt; Identify memory access violations  
\&gt; Automatically break on every kernel launch  
\&gt; Use the autostep mode to detect errors more precisely  
\&gt; Debug multiple applications simultaneously using multiple sessions  
\&gt; Selectively assert in CUDA code  
\&gt; Dynamic Parallelism Support  
\&gt; Inlined Subroutine Support  
\&gt; Run [CUDA-MEMCHECK](/cuda-memcheck) in integrated mode to detect precise exceptions.

 |
| ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuda/images/toolsscreenshots/cuda-gdb-screenshot-2.png &quot;Click to zoom/shrink&quot;)  
 (Click to zoom) | 

\&gt; Kernel launch stack information  
\&gt; Single-GPU debugging  
\&gt; Long-running kernel debugging  
\&gt; Remote debugging for x86 and ARM

 |

Developers should be sure to check out NVIDIA Nsight for integrated debugging and profiling. [Nsight Eclipse Edition](/nsight-eclipse-edition) and [Nsight Visual Studio Code Edition](/nsight-visual-studio-code-edition) for Linux support, and [Nsight Visual Studio Edition](/nvidia-nsight-visual-studio-edition) for Windows.

### CUDA Debugging on Clusters

NVIDIA partners with the following vendors to provide cluster-class debugging solutions for CUDA applications:

| [![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuda/images/product_logos/ddt340.png)](/allinea-ddt) | [![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuda/images/product_logos/RogueWave_Logo_RGB.png)](/totalview-debugger) |

#### [CUDA-GDB Documentation](https://docs.nvidia.com/cuda/cuda-gdb/index.html)

### Questions on CUDA Tools

If you encounter difficulty with any of the CUDA Tools or have more questions please contact the NVIDIA tools team at [cudatools@nvidia.com](mailto:cudatools@nvidia.com) .


