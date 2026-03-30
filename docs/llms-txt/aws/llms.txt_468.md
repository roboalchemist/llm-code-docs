# Source: https://docs.aws.amazon.com/iot-expresslink/archive/v1.0/programmersguide/llms.txt

# ExpressLink Programmer's Guide

> Provides detailed information about ExpressLink modules that are connectivity modules connected via serial interface (initially UART based) that use an abstracted Application Programming Interface (API) to connect any host application to AWS IoT Core and its services.

## [AWS IoT ExpressLink programmer's guide v1.0](https://docs.aws.amazon.com/iot-expresslink/archive/v1.0/programmersguide/elpg.html)

- [1 Hardware](https://docs.aws.amazon.com/iot-expresslink/archive/v1.0/programmersguide/elpg-hardware.html)
- [2 Run states](https://docs.aws.amazon.com/iot-expresslink/archive/v1.0/programmersguide/elpg-run-states.html): An ExpressLink module operates as a state machine that moves through a number of internal states (see figure 2 for a partial representation).
- [3 ExpressLink commands](https://docs.aws.amazon.com/iot-expresslink/archive/v1.0/programmersguide/elpg-commands.html)
- [4 Messaging](https://docs.aws.amazon.com/iot-expresslink/archive/v1.0/programmersguide/elpg-messaging.html)
- [5 Configuration Dictionary](https://docs.aws.amazon.com/iot-expresslink/archive/v1.0/programmersguide/elpg-configuration-dictionary.html): The configuration dictionary is a key-value store containing all the options necessary for the proper functioning of ExpressLink modules.
- [6 Status dictionary](https://docs.aws.amazon.com/iot-expresslink/archive/v1.0/programmersguide/elpg-status-dictionary.html): The status dictionary has been removed since revision 0.6 of the ExpressLink Specifications.
- [7 Event handling](https://docs.aws.amazon.com/iot-expresslink/archive/v1.0/programmersguide/elpg-event-handling.html)
- [8 ExpressLink module updates](https://docs.aws.amazon.com/iot-expresslink/archive/v1.0/programmersguide/elpg-ota-updates.html): ExpressLink modules natively support firmware updates utilizing the AWS IoT OTA service (as currently implemented in the AWS Embedded C-SDK v.202103.00) and Over the Wire (OTW).
- [9 Additional services](https://docs.aws.amazon.com/iot-expresslink/archive/v1.0/programmersguide/elpg-additional-services.html)
- [10 Provisioning](https://docs.aws.amazon.com/iot-expresslink/archive/v1.0/programmersguide/elpg-provisioning.html): All ExpressLink modules will be equipped with a pre-provisioned hardware root of trust (on chip or external secure element, secure enclave, TPM, iSIM).
