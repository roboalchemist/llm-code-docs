# Source: https://docs.edgeimpulse.com/knowledge/courses/edge-ai-fundamentals/how-to-choose-an-edge-ai-device.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to choose an edge AI device

Choosing a device for edge AI can be tricky, as the plethora of computing devices available is daunting. We consider popular edge AI use cases, such as time-series classification and object detection, along with other design constraints to offer a helpful guide for choosing the best hardware.

In the previous section, we [defined edge AI](/knowledge/courses/edge-ai-fundamentals/what-is-edge-ai). In this article, we examine popular edge AI use cases and offer some guidance on choosing the best hardware for an edge AI project.

<iframe src="https://www.youtube.com/embed/okXhTCuIgrs" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

## Design considerations

Your problem or project requires careful consideration along with the various design constraints for choosing the right hardware. Let us begin by looking at the various use cases and constraints.

### Is edge AI the right approach?

Before looking at hardware, you should consider if edge AI is the right approach for your particular problem. In many cases, a traditional rules-based approach with classical algorithms may be enough to tackle the issue.

For example, if you are creating an anomaly detection system based on vibration sensor data, perhaps a [fast Fourier transform (FFT)](https://en.wikipedia.org/wiki/Fast_Fourier_transform) to give you the various frequency components is sufficient. You could set a simple threshold to see if the machine in question is vibrating at a particular frequency. This approach usually requires enough domain knowledge around your particular problem to identify which data is important and how to analyze it.

### Use cases

While the idea behind edge AI is to run any AI algorithm on edge devices, the compute limitations of edge devices restricts most edge AI to a few popular use cases at this time. As hardware and AI technology improves, possible use cases will continue to expand.

Often, edge AI works on data collected from [sensors](https://en.wikipedia.org/wiki/Sensor), which are devices that detect and react to their physical environment. In most cases, we work with electrical sensors that convert measurable environmental factors into electrical signals. Examples of such sensors include digital thermometers (temperature), accelerometers (acceleration and vibration), current sensors (electrical current), microphones (audio), and cameras (images).

* **Time-series sensor data** - Classify occurrences (e.g. sleep patterns) or identify anomalies (e.g. arrhythmia, mechanical equipment failure) from sensor data patterns over time. These time-series data often have relatively slow sample rates, ranging from less than 1 sample per second (1 Hz) to around 1000 Hz.
* **Audio** - Identify wake words, classify sounds (e.g. animals, machinery), or identify anomalies (e.g. mechanical failure). Audio is a form of time-series data, but it usually requires a higher sample rate, often in the 10 kHz to 40 kHz range.
* **Image classification** - Identify if an image contains a particular object, animal, or person. Such processing requires a camera for the sensor. Resolution can be low (e.g. 96x96 pixels) to very high (e.g. 15360x8640 pixels). Response time can be slow, such as 1 frame per second (fps), to very fast (e.g. 60+ fps).
* **Object detection** - Detect one or more target objects, animals, or people in an image, and determine the relative position of each target object in the image. Object detection requires more complex models than image classification. Cameras are also used, and detection can be performed on low to high resolution images. Response times can vary depending on your particular needs.

<Frame caption="Example of object detection">
  <img src="https://mintcdn.com/edgeimpulse/C0SzOGcUNl7GskyL/.assets/images/how-to-choose-an-edge-ai-device-object-detection.png?fit=max&auto=format&n=C0SzOGcUNl7GskyL&q=85&s=721a7bceccedb57a3693134e53d75719" width="406" height="406" data-path=".assets/images/how-to-choose-an-edge-ai-device-object-detection.png" />
</Frame>

*Example of object detection identifying a dog, ball, and toy*

See if your particular project is close to one of the use cases listed above. If not, then you may need to dig into the technical details about the problem's domain, possible machine learning (ML) approaches, and ML model compute requirements.

### Design constraints

Whether you are building an edge AI device for sale or buying off-the-shelf (OTS) components to solve a business need, you should consider your environmental and use constraints.

* **Interfaces** - Does your device connect to sensors? Will it need a connection to the internet (e.g. WiFi) or a smartphone (e.g. Bluetooth)? Does it need to have a user interface (screen, buttons, etc.), or can it be embedded in another device without human interaction?
* **Power constraints** - If the device is battery-powered, how long does it need to operate on a single charge? Even if the device can be plugged into the wall, optimizing for energy savings means you can save money on electricity usage.
* **Form factor** - Do you have the space for a large, powerful server? If not, can you mount a small box containing your device somewhere? Alternatively, is the device wearable, or does it need to conform to some unique shape?
* **Operating environment** - Most electronics work best in a climate-controlled environment, free from moisture and debris. Can you place your device in climate-controlled room like a server room or office? If not, does your device need to be hardened for a specific operating environment, like the outdoors, vehicle, or in space?
* **Code portability** - If you are designing an edge AI application, you should weigh your available options for code portability. Code optimized for a particular piece of hardware can often execute faster and with less energy usage. However, optimized code can often be difficult to port to different hardware and may require unique expertise and extra time to develop. Portable code, on the other hand, usually requires some overhead in the form of an operating system, but it is often easier to run on different hardware (i.e. port to a different device).

### Off the shelf (OTS) versus do it yourself (DIY)

You have the option of buying any or all parts of an edge AI solution from a third-party provider. OTS usually involves a higher unit price, as vendors have overhead and profit margins built in. However, purchasing the device, software, or framework likely means faster setup and time-to-market. Additionally, some of the support/maintenance needs can be passed on to the vendor.

If you are developing or selling an electrical device, OTS options often include compliance testing, such as [UL](https://en.wikipedia.org/wiki/UL_\(safety_organization\)), [FCC](https://en.wikipedia.org/wiki/Federal_Communications_Commission), and [CE](https://en.wikipedia.org/wiki/CE_marking). Such testing can be expensive and time-consuming, but they are almost always necessary for selling devices in a given country.

On the other hand, developing the device or solution yourself requires more up-front time and costs in engineering, programming, and compliance testing. However, the device can be customized and optimized for particular use cases and environments. You also gain economies of scale if you plan to manufacture and sell hundreds or thousands of devices.

The following chart summarizes the tradeoffs between OTS and DIY.

| Buy (OTS)           | Build (DIY)                           |
| ------------------- | ------------------------------------- |
| Time efficiency     | More engineering effort               |
| Ease of use         | Customization                         |
| Higher unit cost    | Potential hidden costs                |
| Third-party support | Independence from third-party vendors |

## Choosing hardware

Once you have an idea of your problem scope and design constraints, you can choose the appropriate hardware. Most edge AI is performed by one of the following hardware categories:

* **Low-end microcontroller** - A microcontroller (also known as a microcontroller unit or MCU) is a self-contained central processing unit (CPU) and memory on a single chip, much like a tiny, low-power computer. Low-end microcontrollers are often optimized for a single or few tasks with a focus on collecting sensor data or communicating with other devices. Such MCUs usually have little or no user interface, as they are intended to be embedded in other equipment. Examples include controllers for microwave ovens, fitness trackers, TV remote controls, IoT sensors, modern thermostats, and smart lights.
* **High-end microcontroller** - High-end MCUs offer more powerful CPUs, more memory, and more peripherals (built-in WiFi, sensors, etc.) than their low-end counterparts. You can find high-end microcontrollers in vehicle engine control units (ECUs), infotainment systems in cars, industrial robotics, smart watches, networking equipment (e.g. routers), and medical imaging systems (e.g. MRI, X-ray).You can read more about microcontrollers [here](https://en.wikipedia.org/wiki/Microcontroller).
* **Microprocessor unit (MPU)** - An MPU is a CPU (often more than one CPU core) packaged on a single chip for general purpose computing. MPUs can be found in laptops, tablets, and smartphones. Unlike MCUs, they require external memory (e.g. RAM, hard drive) to function. They are almost always more powerful than MCUs and capable of crunching numbers at a faster rate. However, they also generally require more energy to function versus MCUs. You can read more about microprocessors [here](https://en.wikipedia.org/wiki/Microprocessor).
* **Graphics processing unit (GPU)** - Graphics processing units were originally designed to render complex 2D and 3D graphics to a computer screen. They are sold either as coprocessors on the same motherboard as an MPU (known as *integrated graphics*) or as a separate graphics card that can be plugged into a motherboard. In both cases, they require another processor (usually an MPU) to handle the general computing needs. Because graphics are generally created using parallel matrix operations, GPUs have also seen success performing similar matrix operations for activities like cryptocurrency mining and machine learning. [NVIDIA](https://www.nvidia.com/) is the most popular GPU maker. You can read more about GPUs [here](https://en.wikipedia.org/wiki/Graphics_processing_unit).
* **Neural processing unit (NPU)** - NPUs are special-purpose AI accelerator chips designed to perform neural network calculations quickly and efficiently. Like GPUs, they almost always require a coprocessor in the form of an MCU or MPU to handle the general purpose computing needs. NPUs range from tiny coprocessors in the same chip as an MCU to powerful, card-based options that can be plugged into a motherboard. The Google [Tensor Processing Unit (TPU)](https://en.wikipedia.org/wiki/Tensor_Processing_Unit) is one example of an NPU. You can read more about AI accelerators and NPUs [here](https://en.wikipedia.org/wiki/AI_accelerator).

The boundary between low- and high-end microcontrollers is not clearly defined. However, we try to differentiate them here to demonstrate that your choice of hardware can affect your ability to execute different edge AI tasks.

<Frame caption="Which hardware works best for which edge AI task">
  <img src="https://mintcdn.com/edgeimpulse/C0SzOGcUNl7GskyL/.assets/images/how-to-choose-an-edge-ai-device-chart.png?fit=max&auto=format&n=C0SzOGcUNl7GskyL&q=85&s=5583597d3ea218b1cf6eee3d1cb3ef47" width="960" height="540" data-path=".assets/images/how-to-choose-an-edge-ai-device-chart.png" />
</Frame>

The above chart makes general suggestions for which class of hardware is best suited for each edge AI task. Not all AI tasks are included, as some are better suited for cloud AI, and AI is an evolving field where such needs are constantly changing.

## Hardware combinations

As noted, many of the processor types are not intended to operate alone. For example, GPUs are optimized for a particular type of operation (e.g. matrix math) and need to be paired with another processor (e.g. MPU) for general purpose computing needs. In some cases, you can create processor-specific modules, such as GPUs and NPUs on cards that easily slot into many personal computer (PC) motherboards.

In some cases, you may come across single-chip solutions that contain multiple processors and various peripherals. For example, a chip might contain a high-end MCU for general processing, a specialized radio MCU for handling WiFi traffic, a low-end MCU for managing power systems, random-access memory (RAM), and a specialized NPU for tackling AI tasks. This type of chip is often marketed as a [system on a chip (SOC)](https://en.wikipedia.org/wiki/System_on_a_chip).

<Frame caption="Example of system on a chip (SOC)">
  <img src="https://mintcdn.com/edgeimpulse/C0SzOGcUNl7GskyL/.assets/images/how-to-choose-an-edge-ai-device-soc.png?fit=max&auto=format&n=C0SzOGcUNl7GskyL&q=85&s=d5b2a626578f93eb3c6dce598dda93f6" width="460" height="460" data-path=".assets/images/how-to-choose-an-edge-ai-device-soc.png" />
</Frame>

## Conclusion

Asking the right questions when creating the scope of your edge AI project is crucial for choosing the right hardware to meet your needs. In many cases, you can simply purchase an off-the-shelf solution, such as buying a doorbell camera, person counting security camera, smart speaker, etc. If your project requires customization, optimization, economies of scale, or a specific operating environment, you may need to develop your own edge AI solution.

Understanding the use case and computing needs for the model can help direct your purchasing or development decisions when it comes to choosing hardware.

## Quiz

Test your knowledge on choosing edge AI hardware with the following quiz:

<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSeUxMq_ZbF82TG61TwbIxyECoFwGXk3wsOuwK2WydD9XTEhsA/viewform?embedded=true" className="w-full aspect-square rounded-xl" />


Built with [Mintlify](https://mintlify.com).