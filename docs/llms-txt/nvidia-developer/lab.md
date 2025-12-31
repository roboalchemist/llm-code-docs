# Source: https://developer.nvidia.com/isaac/lab.md

1. [Home](/)

[Isaac](https://developer.nvidia.com/isaac)

Isaac Lab  

# NVIDIA Isaac Lab

NVIDIA Isaac™ Lab is an open-source, unified framework for [robot learning](https://www.nvidia.com/en-us/glossary/robot-learning/) designed to help train robot policies.   
  
It’s built on [NVIDIA Isaac Sim™](https://developer.nvidia.com/isaac/sim), delivering high-fidelity physics simulation using [NVIDIA PhysX®](https://developer.nvidia.com/physx-sdk) and physically based rendering with NVIDIA RTX™. This bridges the gap between high-fidelity simulation and perception-based robot training, helping developers and researchers build more robots, more efficiently.

[Download Now from GitHub  
](https://github.com/isaac-sim/IsaacLab &quot;Download on GitHub&quot;)[Documentation  
](https://isaac-sim.github.io/IsaacLab/main/index.html &quot;Documentation&quot;)

* * *

## How Isaac Lab Works

Isaac Lab’s modular architecture and NVIDIA GPU-based parallelization make it ideal for building robot policies that cover a wide range of embodiments, including [humanoid robots](https://www.nvidia.com/en-us/glossary/humanoid-robot/), manipulators, and autonomous mobile robots (AMRs).   
  
This gives you a comprehensive framework for robot learning, covering everything from environment setup to policy training. It supports both [imitation](https://www.nvidia.com/en-us/glossary/imitation-learning/) and [reinforcement learning](https://www.nvidia.com/en-us/glossary/reinforcement-learning/) methods. Plus, you can further customize and extend its capabilities with a variety of physics engines, such as PhysX, [NVIDIA Warp](https://developer.nvidia.com/warp-python), and MuJoCo.    
  
Isaac Lab is also the foundational robot learning framework of the [NVIDIA Isaac GR00T platform](https://developer.nvidia.com/isaac/gr00t).

![Isaac Lab’s comprehensive platform for robot learning and robot policy building](https://developer.download.nvidia.com/images/isaac/lab/how-nvidia-isaac-lab-works.jpg)

## Introductory Resources

### 
### A Simulation Framework for Multi-Modal Robot Learning

See how Isaac Lab’s combination of advanced simulation capabilities and data-center scale execution will help unlock breakthroughs in [robotics research](https://www.nvidia.com/en-us/research/robotics/).

[Read Whitepaper](https://research.nvidia.com/publication/2025-09_isaac-lab-gpu-accelerated-simulation-framework-multi-modal-robot-learning)

### Next-Generation Open-Source Physics Simulation Engine

Built on Warp and [OpenUSD](https://developer.nvidia.com/usd), Newton is optimized for advancing robot learning and development and compatible with learning frameworks such as MuJoCo Playground or Isaac Lab.

[Read Blog](https://developer.nvidia.com/blog/train-a-quadruped-locomotion-policy-and-simulate-cloth-manipulation-with-nvidia-isaac-lab-and-newton/)

### Isaac Lab Courses

Explore the fundamentals of robot learning and Isaac Lab, a powerful tool for developing robotic applications.

[Take the Introductory Course](https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-OV-36+V1)

### Isaac Lab Office Hours

Stay informed with our [recurring office hours](https://addevent.com/calendar/ae483892) that cover in-depth topics with experts answering questions about Isaac Lab.

[Watch the Livestreams  
](https://www.youtube.com/@NVIDIAOmniverse/streams)

* * *

## Key Features

### Flexible Robot Learning 

Customize workflows with robot training environments, tasks, learning techniques, and the ability to integrate custom libraries (e.g., skrl, RLLib, rl\_games, and more).

### Reduced Sim-to-Real Gap 

The GPU-accelerated PhysX version provides accurate, high-fidelity physics simulations. This include support for deformables that allows for more realistic modeling of robot interactions with the environment.

### Unified Representation

Discover easy customization and addition of new environments, robots, and sensors with OpenUSD through Isaac Lab’s modular design. 

* * *

## Get Started With Isaac Lab

 ![](https://developer.download.nvidia.com/images/icons/m48-coding-256px-blk.png)
### Download

Get started with the latest version of Isaac Lab by following the installation guides on GitHub.

[Installation Guide (GitHub)](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/index.html#local-installation)[Documentation](https://isaac-sim.github.io/IsaacLab/)

### Tutorials

Access the step-by-step guide to help understand and use various features of the framework.

[Developer Guide](https://github.com/isaac-sim/IsaacLab/discussions)

 ![](https://developer.download.nvidia.com/icons/m48-speech-recognition.svg)
### Start Your Learning Path

Explore advanced concepts in robot learning, gain practical skills, and learn how you can streamline your development processes with Isaac Lab.

[Learn More](https://www.nvidia.com/en-us/learn/learning-path/robotics/)

* * *

#### Newton, the Next-Generation Open-Source Physics Simulation Engine

Newton is an open-source, GPU-accelerated, and extensible physics engine, co-developed by Google DeepMind and Disney Research, and [managed by the Linux Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-contribution-of-newton-by-disney-research-google-deepmind-and-nvidia-to-accelerate-open-robot-learning). Built on NVIDIA Warp and OpenUSD, Newton is optimized for robotics and compatible with learning frameworks such as MuJoCo Playground or Isaac Lab. [Newton Beta](https://github.com/newton-physics) is now available to use.

[Get Started on Newton](https://developer.nvidia.com/newton-physics)

![Newton Physics Engine logo](https://developer.download.nvidia.com/images/isaac/newton-ari.jpg)

* * *

## Starter Kits

View more tutorials and how-to guides in the [documentation](https://isaac-sim.github.io/IsaacLab/main/source/tutorials/index.html).

### Accelerate Robot Learning  

Choose from reinforcement learning and imitation learning to train AI robots. Easily bring your custom libraries and use the direct agent-environment or hierarchical-manager development workflows.

- 

[Read Use Case: Robot Learning](https://www.nvidia.com/en-us/use-cases/robot-learning/?)

- 

[Isaac GR00T-Mimic Blueprint for Synthetic Manipulation Motion Generation](https://github.com/NVIDIA-Omniverse-blueprints/synthetic-manipulation-motion-generation)

- 

[Physical AI Dataset](https://huggingface.co/collections/nvidia/physicalai-67c643edbb024053dcbcd6d8)

### Enable Perception in the Loop  

Tiled rendering reduces rendering time by consolidating input from multiple cameras into a single large image. With a streamlined API for handling vision data, the rendered output directly serves as observational data for simulation learning.

- 

[Read Guide: Tiled Rendering](https://isaac-sim.github.io/IsaacLab/main/source/overview/sensors/camera.html#tiled-rendering)

### Scale With Multi-GPU and Multi-Node Training  

Scale up training of cross-embodied models for complex reinforcement learning environments across multiple GPUs and nodes. Deploy locally and on the cloud (AWS, GCP, Azure, and Alibaba Cloud) by integrating with NVIDIA OSMO.

- 

[Read Guide: Multi-GPU and Multi-Node Rendering](https://isaac-sim.github.io/IsaacLab/main/source/features/multi_gpu.html)

### Accurate High-Fidelity Physics Simulation and Rendering in Omniverse  

Tap into the latest GPU-accelerated PhysX version through Isaac Lab, including support for deformables, ensuring quick and accurate physics simulations augmented by domain randomizations.

- 

[Read Guide: Mastering Omniverse for Robotics](https://isaac-sim.github.io/IsaacLab/main/source/how-to/master_omniverse.html#)

* * *

### RTX PRO Server—the Best Platform for Industrial and Physical AI

NVIDIA RTX PRO Server accelerates every industrial digitalization, robot simulation, and synthetic data generation workload.

[Learn More](https://www.nvidia.com/en-us/data-center/rtx-pro-6000-blackwell-server-edition/)

* * *

## Isaac Lab Learning Library

Research 

A GPU Accelerated Simulation Framework For Multi-Modal Robot Learning

**NVIDIA Isaac Lab**  
  
We present Isaac Lab, the natural successor to Isaac Gym, which extends the paradigm of GPU-native robotics simulation into the era of large-scale multi-modal learning.

Tech Blog 

Streamline Robot Learning with Whole-Body Control and Enhanced Teleoperation in NVIDIA Isaac Lab 2.3

**NVIDIA Isaac Lab**  
  
The latest version of Isaac Lab 2.3, in early developer preview, improves humanoid robot capabilities with advanced whole-body control, enhanced imitation learning, and better locomotion.

Tech Blog 

Quadruped Robot Locomotion and Multiphysics Simulation Using Newton in NVIDIA Isaac Lab

**NVIDIA Isaac Lab**  
  
Walks through how to train a quadruped robot to move from one point to another and how to set up a multiphysics simulation with an industrial manipulator to fold clothes. This tutorial uses Newton within NVIDIA Isaac Lab.

* * *

## Ecosystem

Our industry partners and collaborators are integrating NVIDIA Isaac Lab and accelerated computing into their platforms and solutions.

[![ NVIDIA industry partner - 1X](https://developer.download.nvidia.com/images/isaac/lab/logo-1x.png)](https://www.1x.tech/)

 ![NVIDIA industry partner - AgiBot](https://developer.download.nvidia.com/images/logos/agibot-logo.svg)

[![NVIDIA industry partner - Agility](https://developer.download.nvidia.com/images/isaac/lab/logo-agility-robotics.png)](https://agilityrobotics.com/)

 ![NVIDIA industry partner - Boston Dynamics](https://developer.download.nvidia.com/images/isaac/lab/logo-boston-dynamics.png)

 ![NVIDIA industry partner - Field AI](https://developer.download.nvidia.com/images/isaac/lab/logo-field-ai.png)

 ![NVIDIA industry partner - Fourier](https://developer.download.nvidia.com/images/isaac/lab/logo-fourier.png)

 ![NVIDIA industry partner - Galbot](https://developer.download.nvidia.com/images/isaac/lab/logo-galbot.png)

 ![NVIDIA industry partner - General Robotics](https://developer.download.nvidia.com/images/logos/general-robotics-logo.svg)

 ![](https://developer.download.nvidia.com/images/isaac/lab/logo-mentee-robotics.png)

 ![NVIDIA industry partner - RAI Institute](https://developer.download.nvidia.com/images/logos/rai-logo.svg)

[![ NVIDIA industry partner - Skild AI](https://developer.download.nvidia.com/images/isaac/lab/logo-skild-ai.png)](https://www.skild.ai/)

 ![NVIDIA industry partner - UCR](https://developer.download.nvidia.com/images/isaac/lab/logo-ucr.svg)

 ![NVIDIA industry partner - X-Humanoid](https://developer.download.nvidia.com/images/logos/x-humanoid-logo.svg)

* * *

## More Resources  

 ![Decorative image representing forums](https://developer.download.nvidia.com/images/omniverse/m48-people-group.svg)
### Explore the Community  

 ![](https://developer.download.nvidia.com/images/isaac/m48-certification-ribbon-2-256px-blk.png)
### Get Training and Certification  

 ![](https://developer.download.nvidia.com/images/isaac/m48-ai-startup-256px-blk.png)
### Join the Program for Startups  

* * *

## Latest Isaac Lab News

## Get started with NVIDIA Isaac Lab today.

[Download Now](https://github.com/isaac-sim/IsaacLab &quot;Download Now&quot;)[Documentation](https://isaac-sim.github.io/IsaacLab/ &quot;Documentation&quot;)

## FAQs

The Isaac Lab framework is open-sourced under the [BSD-3-Clause license](https://opensource.org/licenses/BSD-3-Clause).

Isaac Sim is a comprehensive robotics simulation platform built on NVIDIA Omniverse™ that provides high-fidelity simulation with advanced physics and photorealistic rendering. It focuses on synthetic data generation (SDG) and testing and validation (SIL/HIL), and is a reference template for custom robotics simulators.   
  
In contrast, Isaac Lab is a lightweight, open-source framework built on top of Isaac Sim, specifically optimized for robot learning workflows and designed to simplify common tasks in robotics research like reinforcement learning, imitation learning, and motion planning.

If you’re an existing NVIDIA Isaac Gym (predecessor of Isaac Lab) user, we recommend migrating to Isaac Lab to ensure you have access to the latest advancements in robot learning and a powerful development environment to accelerate your robot training efforts. Check out the [migration guide](https://isaac-sim.github.io/IsaacLab/main/source/migration/migrating_from_isaacgymenvs.html) from Isaac Gym environments to Isaac Lab.

Yes, Isaac Lab and MuJoCo are complementary. MuJoCo&#39;s ease of use and lightweight design allow for rapid prototyping and deployment of policies and Isaac Lab can complement it when you want to create more complex scenes, scaling massively parallel environments with GPUs and high-fidelity sensor simulations with RTX rendering. NVIDIA and MuJoCo are actively exploring advancing technical collaborations, stay tuned for future announcements.


