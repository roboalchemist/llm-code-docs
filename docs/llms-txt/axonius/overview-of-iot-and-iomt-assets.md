# Source: https://docs.axonius.com/docs/overview-of-iot-and-iomt-assets.md

# Overview of IoT and IoMT Assets

The **Internet of Things (IoT)** and **Internet of Medical Things (IoMT)** represent the convergence of digital and physical assets, significantly expanding the enterprise attack surface beyond conventional IT.

IoT encompasses network-connected devices used for general business operations, such as security cameras, smart building controls, and industrial sensors (Operational Technology - OT).

IoMT, specifically within healthcare, includes clinical equipment like infusion pumps, patient monitors, and imaging systems.

In the context of Axonius, these devices are uniquely challenging because they are often unmanaged, unpatchable, and communicate via non-standard protocols. The platform addresses this by aggregating data through specialized discovery tools, including the **Axonius Network Inspector** physical device and software adapter, to establish verified inventories for distinct cyber-physical asset classes, including IoT/OT and IoMT devices. This unified visibility is essential for mapping the total risk exposure and enabling segmentation and policy enforcement actions on devices that cannot support traditional security agents.

<Callout icon="📘" theme="info">
  Note

  For information about the **Axonius Network Inspector** physical device and software adapter, see [Axonius Network Inspector Deployment](https://docs.axonius.com/axonius-help-docs/docs/network-inspector-deployment) and [Axonius Network Inspector adapter](https://docs.axonius.com/axonius-help-docs/docs/axonius-network-inspector).
</Callout>

## Managing IoT/OT Devices

Managing general IoT and OT environments prioritizes system availability and operational safety. OT hardware, such as Programmable Logic Controllers (PLCs), is designed for extended lifecycles and is highly sensitive to disruption; aggressive network activity or unexpected restarts can halt production or critical infrastructure functions. Effective security requires passive discovery methods to maintain system uptime.

The Axonius platform provides the contextual data necessary to inventory devices running unsupported software and trigger policy actions (like network isolation) that reduce risk without compromising the functional integrity of the OT environment.

## Securing IoMT Devices

Securing IoMT assets is uniquely constrained by patient safety requirements and strict regulatory compliance. Medical devices often contain Protected Health Information (PHI) and are governed by rigorous change control processes that prohibit rapid software updates. Security actions must, therefore, be clinically non-disruptive.

The Axonius platform provides deep data correlation by integrating clinical context (device criticality, location) with vulnerability data. This enables biomedical engineering and security teams to apply risk mitigation strategies, such as micro-segmentation or virtual patching, that preserve essential device functionality and maintain continuous patient care.