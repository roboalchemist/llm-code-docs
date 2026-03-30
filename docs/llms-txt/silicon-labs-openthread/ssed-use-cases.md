# Source: https://docs.silabs.com/openthread/3.0.0/openthread-sleepy-devices/ssed-use-cases.md

# SSED Use Cases

- In dense network settings, SSEDs can reduce over-the-air radio traffic by avoiding frequent data polling.
- SSEDs are also useful in settings with sparse data traffic patterns that require high responsiveness from the sleepy devices.

When comparing viability of SEDs and SSEDs, note that SSEDs may have lower power consumption in a direct comparison only in settings that ensure tight CSL accuracy and uncertainty. With worse uncertainty deviations, or in settings with high interference, any power savings sought by reducing time spent in data polling traffic will be compromised by power spent on larger receive windows. Referring to the following figure, the goal should be to minimize receive windows on the SSEDs when there is no data, while still supporting the application use case.

![Comparison of SED and SSED Power Consumption](/openthread-sleepy-devices/0.2/images/sld415-image2.png)