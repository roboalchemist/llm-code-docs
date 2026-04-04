# Source: https://docs.edgeimpulse.com/knowledge/courses/edge-ai-fundamentals/what-is-edge-computing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is edge computing?

Edge computing is a computer networking strategy where data is processed and stored at the periphery of the network. The "periphery" includes end-user devices and equipment that connects those devices to larger networking infrastructure, such as the internet. For example, laptops, smartphones, IoT devices, routers, and local switches count as edge computing devices.

In the previous article, we [introduced this edge AI series](/knowledge/courses/edge-ai-fundamentals/intro-to-edge-ai). We start the series by examining the advantages and disadvantages of edge computing and how it differs from cloud computing.

<iframe src="https://www.youtube.com/embed/WZQ6kCvOEaE" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

By processing data closer to where the data is generated, we can reduce latency, limit bandwidth usage, improve reliability, and increase data privacy.

## Network architecture overview

Most networking architectures can be divided into the "cloud" and the "edge." Cloud computing consists of applications and services running on remote, internet-connected devices. Edge computing is essentially everything that is not part of the cloud (i.e. in the internet).

<Frame caption="Cloud computing vs. edge computing">
  <img src="https://mintcdn.com/edgeimpulse/yWZVbRGeek_I_Jpe/.assets/images/intro-to-edge-ai-cloud-vs-edge.png?fit=max&auto=format&n=yWZVbRGeek_I_Jpe&q=85&s=18c660c0b26e19495cabdb90d6fc7859" width="960" height="540" data-path=".assets/images/intro-to-edge-ai-cloud-vs-edge.png" />
</Frame>

Typically, local infrastructure IT equipment, such as servers and databases, are not considered either "edge" or "cloud." For our purposes, we will consider them part of the "edge," as running services on this gear often requires on-site customization and maintenance.

In general, data will be created by end-point devices. "End-point devices" or "end devices" refer to physical equipment at the very edge of the network, such as laptops, smartphones, and connected sensors. Sometimes, these end devices have a user interface where a person can interact with various applications, enter data, etc. Other times, the device is embedded into other equipment or offers no user interface. These embedded devices, if connected to the internet or other networks, are referred to as the Internet of Things.

Examples of IoT devices include smart speakers, smart thermostats, doorbell cameras, GPS trackers, and networked pressure sensors in factories used to provide flow metrics and detect anomalies.

> **Note:** a [sensor](https://en.wikipedia.org/wiki/Sensor) is a device that measures a physical property in its environment (such as temperature, pressure, humidity, acceleration, etc.) and converts that measurement into a signal (often an electrical signal) that can be interpreted by a human or computer.

Sometimes, data can be stored and processed on the end device, like saving a local spreadsheet or playing a single-player game. In other cases, you need the power of cloud computing to stream movies, host websites, perform complex data analysis, and so on.

## Cloud computing

You are likely already familiar with many cloud computing services, such as Netflix, Spotify, Salesforce, HubSpot, Dropbox, Google Drive. These services run on powerful, internet-connected servers that you access through a client application, such as a browser.

Most of the time, these services run on top of one of the major cloud computing platforms, like Amazon Web Services, Microsoft Azure, or Google Cloud Platform. Such platforms offer [containerized](https://aws.amazon.com/what-is/containerization/) operating systems that allow you to easily build your application in a modular fashion and scale up production to meet the demand of thousands or millions of users.

The benefits of cloud computing include:

* Large servers offer powerful computing capabilities that can crunch numbers and run complex algorithms quickly
* Remote access to services from any device (as long as you have an internet connection)
* Processing and storage can be scaled on demand
* Physical servers are managed by large companies (e.g. Google, Amazon, Microsoft) so that you do not need to handle the infrastructure and maintenance

## Edge computing

In addition to cloud computing, you also have the option of running services directly on the end devices or on local network servers. Processing such edge data might include running a user application (e.g. word processing document), analyzing sensor data to look for anomalies, identifying faces in a doorbell camera, and hosting an intranet website accessible only to local users.

According to Ericsson, there will be over [7 billion smartphones](https://www.ericsson.com/en/reports-and-papers/mobility-report/mobility-visualizer?f=1\&ft=1\&r=1\&t=8\&s=1\&u=1\&y=2016,2025\&c=1) in the world by 2025. Additionally, the International Data Corporation (IDC) predicts a staggering 41.6 billion IoT devices will be in use by 2025. These devices will produce nearly [80 zettabytes that year](https://www.forbes.com/sites/forbestechcouncil/2023/08/08/innovate-or-perish-the-importance-of-modernizing-data-infrastructure/), which amounts to about 200 million terabytes every day. The sheer amount of raw data is likely to strain existing infrastructure. One way to handle such data is to process locally or on the edge, rather than transmit everything to the cloud.

The network edge can be divided into "near" edge and "far" edge. Near edge equipment consists of on-premises or regional servers and routing equipment controlled by you or your business. Near refers to the physical proximity or relatively low number of router hops it takes for traffic to go from the border of the internet to your equipment. In other words, "near" and "far" are from the perspective of the internet service provider (ISP) or cloud service provider.

Far edge consists of the devices further away from the internet gateway on your network. Examples include user end-devices, such as laptops and smartphones, as well as IoT devices and local networking equipment, such as routers and switches.

The border between the cloud, near edge, and far edge can often be nebulous. In fact, a relatively recent trend includes [fog computing](https://en.wikipedia.org/wiki/Fog_computing), which is a term coined by Cisco in 2012. In fog computing, edge devices (often near edge servers) are used to store and process data, often replicating the functionality of cloud services on the edge.

### Advantages

Edge computing offers a number of benefits:

* **Reduced bandwidth usage** - you no longer need to constantly stream raw data to have it stored, analyzed, or processed by a cloud computing service. Instead, you can simply transmit the results of such processing.
* **Reduced network latency** - network latency is the round-trip time it takes for information to travel to its destination (e.g. a cloud server) and for the response to return to the end-point device. For cloud computing, this can be 100s of milliseconds or more. If processing is performed locally, such latency is often reduced to almost nothing.
* **Improved energy efficiency** - Transmitting data, especially via a wireless connection like WiFi, usually requires more electrical power than processing the data locally.
* **Increased reliability** - Edge computing means that data processing can often be done without an internet connection.
* **Better data privacy** - If raw data is processed directly on an end device without travelling across the network, it becomes harder to access by malicious parties. This means that user data can be made more secure, as there are fewer avenues to access that raw data.

These benefits can easily be remembered with the acronym BLERP: bandwidth, latency, energy usage, reliability, and privacy.

### Disadvantages

While edge computing offers a host of benefits, there are several limitations:

* **Resource constraints** - Most edge devices do not offer the same level of raw computing as most cloud servers. If you need to crunch numbers quickly or run complex algorithms, you might have to rely on cloud computing.
* **Limited remote access** - Services running locally on edge or end devices might not be easily accessed via remote clients. To provide such remote access, you often need to run additional services (such as a web server) and/or configure a [VPN](https://www.cisco.com/c/en/us/products/security/vpn-endpoint-security-clients/what-is-vpn.html) on your local network.
* **Security** - Many IoT devices come from the manufacturer with default login credentials and open ports, making them prime targets for attackers (such as with the infamous [Mirai botnet attack in 2016](https://en.wikipedia.org/wiki/Mirai_\(malware\))). You and your network administrators are responsible for implementing and enforcing up-to-date security plans for all edge devices.
* **Scaling** - Adding more computing power and resources is often easy in cloud computing; you just pay the cloud service provider more money. Scaling your resources for edge computing often requires purchasing and installing additional hardware along with maintaining the infrastructure.

## Examples of edge computing

Anything that runs locally on your computer or smartphone is considered edge computing. That includes word processing, spreadsheets, most programming development environments, and many video games. Some applications require both edge computing and cloud computing elements, such as video conferencing applications (e.g. Zoom). Cloud-based applications that you use in your browser (such as Google Docs or Netflix) require heavy processing on cloud servers as well as some light local processing on your phone or computer.

In addition to user applications, you can also find IoT devices performing local processing of data. Some examples of this include smartwatches monitoring exercise levels, smart speakers waiting for a keyword (such as "Alexa"), and industrial controllers automatically operating machinery based on input sensor values.

One example of edge computing on networking gear is QoS. Your home or office router may monitor web traffic to determine packet priority in a technique known as [quality of service (QoS)](https://en.wikipedia.org/wiki/Quality_of_service). As QoS requires to the router to monitor traffic destinations (and sometimes content) to quickly make such prioritization decisions, edge computing on the router is a natural fit.

## Quiz

Edge computing offers a number of advantages over cloud computing, but it comes with some limitations. You should consider your options carefully before investing in either strategy for your computing needs.

Test your knowledge on edge computing with this quiz:

<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSeueHCAGxu-NgYHL4mF7Z0hYQcEb6FTDAb22Ko1QhcKJU6pww/viewform?embedded=true" className="w-full aspect-square rounded-xl" />


Built with [Mintlify](https://mintlify.com).