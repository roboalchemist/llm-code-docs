# Source: https://docs.axonius.com/docs/incident-response.md

# Incident Response

**Accelerate Incident Response**

<HTMLBlock>
  {`
  <iframe src="https://fast.wistia.net/embed/iframe/lgk4wu2kux?web_component=true&amp;seo=false&amp;videoFoam=false" frameborder="0" allowfullscreen="true" allow="autoplay; fullscreen" title="Incident Response Video" style="display:flex;margin-right:auto;width:640px;height:360px;" width="640" height="360" allowtransparency="true" scrolling="no" class="wistia_embed" name="wistia_embed" dataalign="left" datadisplay="flex"></iframe>
  `}
</HTMLBlock>

## **Introduction**

Incident Response is an organization’s processes and associated technologies for detecting and responding to cyberthreats, security breaches, or cyberattacks. A formal incident response plan using Axonius enables IR teams to get a broader view of the threat being addressed and the ability to dive deeper into individual assets that have been impacted.

**Audience:** SOC, Incident Response Team

**Difficulty:** Intermediate to Advanced

**Execution Time:** 1 week, ongoing refinement

**Duration of Use Case:** Perpetual

**Value:** Helps organizations streamline investigations, minimize the impact of a breach, and maintain business continuity.

**What is this use case?**

Every organization needs an Incident Response plan so there is no time wasted gathering data for analysis, and the impact of the incident is minimized. Axonius can provide the IR teams with information from security tool coverage (confirming what systems may be at heightened risk), user activity, and other data points of interest (like what devices have encryption enabled).

**Use Case in Action:**

Axonius has templates for both Device and User Incident Response, and they are a great start in developing a comprehensive collection of IR dashboards and charts:

* Endpoint Protection (EPP, XDE, EDR)
* VA Tools
* IAM

**Why is it Relevant?**

The key to Incident Response is responding to an incident as quickly and efficiently as possible. Finding pertinent information regarding a Device or User improves the chances of containing the incident and promptly remediating it before any further harm is done. Working with the IR team to develop charts and dashboards will help to achieve this goal.

## Visibility

**How do I visually explain this use case?**

For Incident Response, the **Asset Profile Dashboard** allows you to create investigative dashboards focused on a specific asset of any given asset type. Additionally, the Asset Graph helps you explore relationships between assets. Together, these tools provide a visual foundation for conducting the research necessary for detection, containment, investigation, remediation, and recovery.

**Recommended Visualizations**

Below are some visualizations that give us pertinent information regarding the asset being investigated quickly and efficiently by creating an IR dashboard within Dashboard Overview.

* **Device Users** – Who was last on this device? Are they associated with any other devices?![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUcYki6KOwhinTsQY_4UjO5COLDP56Zr0i6CupmMNtcBd2fnId0QiYkh39R9GAD97xEoxZpFCmEe2D0EMkZdkcUtxNTLiI3Wjn4uv4YGby0kjPEYT-9UX9V_znNlAlRGX62tWa33iNm4lYp_4Xi8FFQc6dbXgyPKNekAk-FOqbrJDsWoEXuMa0U=nw?key=VSK9xfPGmpy2Wl9lO_CfWw)
* **OS Status** – What OS, version, EOS, EOL?![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUebxilEPdpglN6la34-Kn2bAIkUFK0TexYllUlxZd7oe-2rQSBhdWU05dVkYOV8BTzRBAzauDP_kjuAyC9UkO4xBzoDDAGbeDHHiM8tcpf196eu4gGY0E5UWOMRm6GHRnNL48FNvBgXPIviP-ZxGKAEjbZt_RNYgFTKaeCs-I0Lz0pnkVnO5w=nw?key=VSK9xfPGmpy2Wl9lO_CfWw)
* **IR Team Data** – Data points the IR team wants to quickly see![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUeU8yrtc-G8VeOVb_rSGbjPcleDiZNoh2AzIiGkF0ovQY-mwkSH34P4cmR-FqfuAJkpH5noPik2YXtc4Go-huQn9L-XhK7el0v-1WZkMAA0_8STkMfqpyIgCX-x_61zQ5o4utAsN05ZOl6ToKXzW2F110luVQ-wZBYXI4MbyJPfN49osl8q43s=nw?key=VSK9xfPGmpy2Wl9lO_CfWw)

### Asset Investigation

View changes over a period of time through the use of Asset Investigation. This view can either be accessed for a single Asset, via its profile page, or for all assets through Asset Investigation on the side menu.

* What ports are open and when were they discovered?
* When were new users first seen on the device?
* Were any applications recently installed or updated?![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUeCVSNYfByWzkBcEZNyqbpV3kUQeLAjZWP88f9sNsfdWoVWGO-WPz8FSlH5U3d07ydVACrbaic0E-Oo-xRO6W-wCkmYHvzHlwOspE9eGfBNuxzbEC-Jd7tOrvTc5hZSUH6-h7eTwsmzACwErDCVpsHIp_NNukrL6yTUqUq-1mhfpJ4pD0o-qtQ=nw?key=VSK9xfPGmpy2Wl9lO_CfWw)

### Asset Graph

Explore the asset's relationship to all other Asset types known to Axonius.

<Image align="center" border={false} width="543px" src="https://lh7-rt.googleusercontent.com/slidesz/AGV_vUfiHRMCFVrQ0lUGq9ye3He4nLLNKZF1aKIxMFKhSKnMZsJms44OCZazdV5pYwO4rxz6WddVp5QY1rPYWb7DKqIcbuc5zg8lX3iowDXCcFx44iw5NSoOziiC1-YMgznrnlyFadaqqnBErLYL71qhZgbdjZn8VV4yjnv1YevponugrJlhR1fkuNc=nw?key=VSK9xfPGmpy2Wl9lO_CfWw" height="auto" />

Further expand your search to identify associated Users and Devices that may need to be investigated.

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-RJUJ3IKM.png" />

The graphics can be used as part of an incident postmortem. View the asset profile from within the Asset Graph.

<Image align="center" border={false} width="689px" src="https://lh7-rt.googleusercontent.com/slidesz/AGV_vUffiMhsF8_vIz1k8vkYNdHn3PwToHB8avLPAqdi8DcgVPIzhpHVKihQRb1kBrO0d29eY-CkF_705T-4VdaErzsGW89xyETIxZoXXXH28OGr1D6q7jUyP301l3ieKvaGlFblE77MCElFfLp-2vYZqjUWL8hHhzZnqJKCwEgqMD2I4TRIINmBQA=nw?key=VSK9xfPGmpy2Wl9lO_CfWw" height="auto" />

## Actionability

**How do I automate this use case?**

Execute Enforcement Center Actions to automate different tasks in response to the incident. Automations can be configured in advance and used on demand.