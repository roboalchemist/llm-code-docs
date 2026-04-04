# Source: https://docs.aws.amazon.com/iot-expresslink/archive/v0.5/programmersguide/llms.txt

# ExpressLink Programmer's Guide

> Provides detailed information about ExpressLink modules that are connectivity modules connected via serial interface (initially UART based) that use an abstracted Application Programming Interface (API) to connect any host application to AWS IoT Core and its services.

## [AWS IoT ExpressLink programmer's guide v0.5](https://docs.aws.amazon.com/iot-expresslink/archive/v0.5/programmersguide/elpg.html)

- [1 Overview](https://docs.aws.amazon.com/iot-expresslink/archive/v0.5/programmersguide/elpg-overview.html): This document defines the Application Programming Interface (API) that all AWS IoT ExpressLink compliant connectivity modules are required to implement to connect any host processor to the AWS cloud.
- [2 Run states](https://docs.aws.amazon.com/iot-expresslink/archive/v0.5/programmersguide/elpg-run-states.html): Although an ExpressLink module operates as a state machine that moves through a number of internal states (see figure 1 for a partial representation), its user interface is designed to abstract these details entirely.
- [3 ExpressLink commands](https://docs.aws.amazon.com/iot-expresslink/archive/v0.5/programmersguide/elpg-commands.html): These commands are sent to and from the UART.
- [4 Messaging](https://docs.aws.amazon.com/iot-expresslink/archive/v0.5/programmersguide/elpg-messaging.html)
- [5 Configuration Dictionary](https://docs.aws.amazon.com/iot-expresslink/archive/v0.5/programmersguide/elpg-configuration-dictionary.html): The configuration dictionary is a key-value store containing all the options necessary for the proper functioning of ExpressLink modules.
- [6 Event handling](https://docs.aws.amazon.com/iot-expresslink/archive/v0.5/programmersguide/elpg-event-handling.html): Events are asynchronous messages on one of the subscribed topics that the ExpressLink module has received and queued.
- [7 ExpressLink module OTA updates](https://docs.aws.amazon.com/iot-expresslink/archive/v0.5/programmersguide/elpg-ota-updates.html): ExpressLink modules natively support over the air (OTA) firmware updates utilizing the AWS IoT OTA service (as currently implemented in the AWS Embedded C-SDK v.202103.00).
- [8 AWS IoT Services](https://docs.aws.amazon.com/iot-expresslink/archive/v0.5/programmersguide/elpg-iot-services.html)
- [9 Additional services](https://docs.aws.amazon.com/iot-expresslink/archive/v0.5/programmersguide/elpg-additional-services.html)
