# Source: https://developer.nvidia.com/dcgm.md

1. [Home](/)

NVIDIA DGCM

# NVIDIA DCGM  

NVIDIA Data Center GPU Manager (DCGM) is a suite of tools for managing and monitoring NVIDIA Datacenter GPUs in cluster environments. It includes active health monitoring, comprehensive diagnostics, system alerts, and governance policies including power and clock management. Infrastructure teams can use it standalone and in addition easily integrate it into cluster management tools, resource scheduling, and monitoring products from NVIDIA partners.  
  
DCGM simplifies GPU administration in the data center, improves resource reliability and uptime, automates administrative tasks, and helps drive overall infrastructure efficiency. DCGM supports Linux operating systems on x86\_64, and aarch64 (sbsa) platforms. The installer packages include libraries, binaries, and source examples for using the API (C and Python). In addition, [Go bindings](https://github.com/NVIDIA/go-dcgm) are available via the open-source GitHub repository . Please refer to the documentation for additional details and instructions.  
  
DCGM also integrates into the Kubernetes ecosystem using DCGM-Exporter to provide rich GPU telemetry in containerized environments. DCGM has an open-core architecture - the foundational libraries and building blocks are available as open source on GitHub but at the same time certain blocks such as diagnostics and tests remain proprietary.

[Documentation  
](https://docs.nvidia.com/datacenter/dcgm/latest/index.html &quot;Github Repo&quot;)[DCGM GitHub](https://github.com/NVIDIA/DCGM &quot;Github Repo&quot;)[DCGM-Exporter GitHub  
](https://github.com/NVIDIA/gpu-monitoring-tools &quot;Github Repo&quot;)[DCGM Go Binding  
](https://github.com/NVIDIA/go-dcgm &quot;Github Repo&quot;)

* * *
 
## How NVIDIA DCGM Works?  

NVIDIA Data Center GPU Manager (DCGM) is a powerful tool designed to manage and monitor NVIDIA GPUs in data centers, ensuring optimal performance and reliability. By utilizing DCGM, administrators can easily track the health, performance, and utilization of their GPU resources.  
The process begins with the installation of the DCGM on each server node that houses NVIDIA GPUs. At the core of DCGM is the libdcgm.so library. DCGM can be utilized either by initiating a service through HostEngine, which functions as a wrapper around the library, or by developing a standalone application that directly incorporates the library.  
  
When operated as a service, DCGM offers two interfaces for user interaction: dcgmi and the DCGM Exporter. The dcgmi interface is equipped with commands designed to manage and monitor GPU performance and health, making it an ideal tool for administrators who prefer a command-line approach. In contrast, the DCGM Exporter is tailored for cluster-level monitoring within native Kubernetes environments. It exports GPU metrics and health data for real-time monitoring and alerting, thus providing a comprehensive overview of the GPU cluster&#39;s status.  
  
DCGM also includes active and passive diagnostics for Nvidia hardware. Administrators can access this data through a user-friendly interface or via a command-line tool, enabling them to set up alerts for any irregularities or performance issues. By proactively identifying potential problems and optimizing GPU performance, NVIDIA DCGM plays a crucial role in maintaining the efficiency and reliability of data center operations.

![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/datacenter/dcgm-icon.png)

* * *

## Key Benefits

### GPU Diagnostics and System Validation

Effectively identify failures, performance degradations, power inefficiencies and their root causes.

### GPU Telemetry

Gather rich set of GPU telemetry to explain job behavior, identifying opportunities to drive utilization and efficiencies, and determining root causes of potential application performance issues.

### Active GPU Health Monitoring  

Use low-overhead, non-invasive health monitoring while jobs run without impacting application behavior and performance.

### Integration with Management Ecosystem

Easily deploy a DCGM based monitoring solution in a Kubernetes cluster environment. Out of the box integration with various ISV solutions such as Bright Cluster Manager, IBM Spectrum LSF and open-source tools such as Prometheus, collected.

* * *

## NVIDIA DCGM Resources

### Blog Posts

- [Monitoring GPUs in Kubernetes with DCGM](https://developer.nvidia.com/blog/monitoring-gpus-in-kubernetes-with-dcgm/)
- [Job Statistics with NVIDIA Data Center GPU Manager and Slurm](https://devblogs.nvidia.com/job-statistics-nvidia-data-center-gpu-manager-slurm/)
- [Setting Up GPU Telemetry with NVIDIA Data Center GPU Manager  
](https://devblogs.nvidia.com/gpu-telemetry-nvidia-dcgm/)
- [NVIDIA Data Center GPU Manager Simplifies Cluster Administration](https://devblogs.nvidia.com/nvidia-data-center-gpu-manager-cluster-administration/)

### Documentation

- [DCGM Documentation](https://docs.nvidia.com/datacenter/dcgm)

### Recorded Talks

GTC 2018 Talk:

- GTC 2018 Talk: [GPU Monitoring and Management with NVIDIA Data Center GPU Manager](http://on-demand.gputechconf.com/gtc/2018/presentation/s8505-gpu-monitoring-and-management-with-nvidia-data-center-gpu-manager-dcgm-v2.pdf)

* * *

##   

Get started with NVIDIA DCGM today

[Get Started](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/getting-started.html#)


