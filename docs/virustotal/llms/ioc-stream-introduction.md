# Source: https://virustotal.readme.io/reference/ioc-stream-introduction.md

# IoC Stream

VirusTotal IoC Stream is an evolution to the previous Hunting's Livehunt but opening the flux to other origins that allows you to curate your own custom feeds based on your interests. This service sinks all the IoC matches in a single place to expose them following a common interface to make the IoC Stream actionable.

The IoC stream supports multiple filters and orders to filter your matches by their origin, entity type (file, domain, url, IP address), etc. You can find the complete reference [here](https://virustotal.readme.io/reference/get-objects-from-the-ioc-stream)

## Notification origins

> 📘
>
> More origins coming soon, keep tuned!

### Threats

Allows you to hook onto the stream of different threats (threat actors, malware, software toolkit, IoC collections) and get notified whenever one of them has a new IoC associated.

### Hunting

Allows you to hook onto the stream of files submitted to VirusTotal and get notified whenever one of them matches a certain [YARA](http://virustotal.github.io/yara/) rule.