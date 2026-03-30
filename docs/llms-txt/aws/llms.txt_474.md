# Source: https://docs.aws.amazon.com/iot-expresslink/latest/programmersguide/llms.txt

# AWS IoT ExpressLink Programmer's Guide

> Provides detailed information about ExpressLink modules that are connectivity modules connected via serial interface (initially UART based) that use an abstracted Application Programming Interface (API) to connect any host application to AWS IoT Core and its services.

## [AWS IoT ExpressLink programmer's guide v1.3](https://docs.aws.amazon.com/iot-expresslink/latest/programmersguide/elpg.html)

- [1 Overview](https://docs.aws.amazon.com/iot-expresslink/latest/programmersguide/elpg-overview.html): An AWS IoT ExpressLink qualified module is a hardware connectivity module that communicates with a host processor by means of a serial interface (UART) and allows it to quickly and securely access AWS IoT Core and its services.
- [2 Hardware](https://docs.aws.amazon.com/iot-expresslink/latest/programmersguide/elpg-hardware.html): An AWS IoT ExpressLink qualified module is generally composed of the following elements: (see block diagram)
- [3 Run states](https://docs.aws.amazon.com/iot-expresslink/latest/programmersguide/elpg-run-states.html): An ExpressLink module operates as a state machine that moves through a number of internal states.
- [4 ExpressLink commands](https://docs.aws.amazon.com/iot-expresslink/latest/programmersguide/elpg-commands.html)
- [5 Messaging](https://docs.aws.amazon.com/iot-expresslink/latest/programmersguide/elpg-messaging.html)
- [6 Configuration Dictionary](https://docs.aws.amazon.com/iot-expresslink/latest/programmersguide/elpg-configuration-dictionary.html): The configuration dictionary is a key-value store containing all the options necessary for the proper functioning of ExpressLink modules.
- [7 Status dictionary](https://docs.aws.amazon.com/iot-expresslink/latest/programmersguide/elpg-status-dictionary.html): The status dictionary has been removed since rev 0.6 of the ExpressLink Specifications.
- [8 Event handling](https://docs.aws.amazon.com/iot-expresslink/latest/programmersguide/elpg-event-handling.html)
- [9 ExpressLink module Updates](https://docs.aws.amazon.com/iot-expresslink/latest/programmersguide/elpg-ota-updates.html): ExpressLink modules natively support firmware updates utilizing the AWS IoT OTA service and, locally, using Over the Wire (OTW) updates.
- [10 AWS IoT Services](https://docs.aws.amazon.com/iot-expresslink/latest/programmersguide/elpg-iot-services.html)
- [11 Additional services](https://docs.aws.amazon.com/iot-expresslink/latest/programmersguide/elpg-additional-services.html): Â 
- [12 Provisioning and Onboarding](https://docs.aws.amazon.com/iot-expresslink/latest/programmersguide/elpg-provisioning.html): All ExpressLink modules will be equipped with a pre-provisioned hardware root of trust (on chip or external secure element, secure enclave, TPM, iSIM).
- [13 Bluetooth Low Energy (BLE)](https://docs.aws.amazon.com/iot-expresslink/latest/programmersguide/elpg-ble.html): ExpressLink modules can take advantage of additional (local) connectivity capabilities, optionally available on selected SoCs.
- [14 GPIO control (new with v1.3)](https://docs.aws.amazon.com/iot-expresslink/latest/programmersguide/elpg-gpio-control.html): General Purpose I/O control is provided to allow ExpressLink modules to act as I/O expanders for the host processor by allowing control with serial interface of additional pins beyond the basic set defined in section 2.2.
- [Appendix â Manufacturer Module Datasheet Requirements](https://docs.aws.amazon.com/iot-expresslink/latest/programmersguide/elpg-appendix-b.html): The following is a summary of commands and features that are listed as optional for implementation by the manufacturer.
- [Document history](https://docs.aws.amazon.com/iot-expresslink/latest/programmersguide/elpg-history.html): The following table describes important changes to the AWS IoT ExpressLink Programmer's Guide starting with v1.0.
- [Archive](https://docs.aws.amazon.com/iot-expresslink/latest/programmersguide/elpg-archive.html): The following archive versions of this Programmer's Guide are available:
