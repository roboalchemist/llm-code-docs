# Source: https://virustotal.readme.io/docs/difference-public-private.md

# What is the difference between the public API and the private API?

# Use cases

* **Public API** -  Non-commercial, or academic use.
* **Private API** - Commercial or Government use is allowed.

# Request Rate

* **Public API** - 4 interactions per minute.
* **Private API** - Custom.

# Additional Information

* **Public API** - Basic.
* **Private API** - File and URL information provided by tools integrated in VirusTotal (PEinfo, PEiD, ExifTool, packers, sandbox links, sigcheck, etc.).

# Sandbox data

* **Public API** - None.
* **Private API** - Behavioral execution information, on files types supported by our sandboxes.

# Goodware Info

* **Public API** - None.
* **Private API** - We provide signals whether a given hash is goodware or not, products in which the file is found.

# Search API

* **Public API** - Only query by hash
* **Private API** -Example searches:
  * "give me all samples that are detected with the following signature",
  * "give me all samples that are detected by more than 10 engines"
  * "give me all samples that contain a given PE section with the following hash", etc.
  * queries can be combined to build complex requests.

# Notifications

* **Public API** - None.
* **Private API** - [YARA](https://plusvic.github.io/yara/) notifications on the samples received at VirusTotal.  (Note:  This requires VirusTotal Intelligence service).

# Price

* **Public API** - None.
* **Private API** - Paid, pricing depends on usage. [Contact us](https://www.virustotal.com/gui/contact-us/premium-services) tell us about your use case, and usage estimates for a quote.

# Terms of service

* **Public API** - [Standard Terms of Service](https://docs.virustotal.com/docs/terms-of-service/)
* **Private API** - Premium services agreement.

Service Level Agreement (SLA)

* **Public API** - None
* **Private API** - 99% uptime guarantee, details in premium services agreement.