# Source: https://docs.wiremock.io/simulating-faults.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Simulating Faults

> Responding with network and HTTP faults

Real-world APIs and the networks used to communicate with them can fail in ways that can destabilise your application,
and are hard to test.

WireMock Cloud supports responding to requests with four different fault types:

* Server closes connection before response sent
* Corrupt data sent, then connection closed
* OK response sent, followed by corrupt data and connection close
* Peer connection reset - `SO_LINGER` is set to 0 causing a non-graceful TCP connection termination.

These are configured per stub, so it is possible to respond to specific requests with a fault.

## Usage

Faults are configured when creating or editing a stub by selecting the Fault tab in the response and choosing the fault type:

<img src="https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/fault-response.png?fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=f35340456d874f3ed5c306f0650d7151" title="Fault response" data-og-width="424" width="424" data-og-height="244" height="244" data-path="images/screenshots/fault-response.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/fault-response.png?w=280&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=54a62d81923e81b5ccd798d9bb3018a3 280w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/fault-response.png?w=560&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=62aaeabb4f694507817ec337f1b7990d 560w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/fault-response.png?w=840&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=725f79a30b3b256b814d88ca999b0061 840w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/fault-response.png?w=1100&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=53b905b2437d4f4774972745ba3e4afa 1100w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/fault-response.png?w=1650&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=51fdcf13583259ad2935411290c8cc14 1650w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/fault-response.png?w=2500&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=fdeef635984aed0f6b9d530ddc15f452 2500w" />
