# Source: https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.hostandport.md.txt

An object containing the hostname and port number of an emulator.

<br />

**Signature:**  

    export interface HostAndPort 

## Properties

|                                                                Property                                                                |  Type  |                                                                             Description                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [host](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.hostandport.md#hostandporthost) | string | The host of the emulator. Can be omitted if discovered automatically through the hub or specified via environment variables. See`TestEnvironmentConfig`for details. |
| [port](https://firebase.google.com/docs/reference/emulator-suite/rules-unit-testing/rules-unit-testing.hostandport.md#hostandportport) | number | The port of the emulator. Can be omitted if discovered automatically through the hub or specified via environment variables. See`TestEnvironmentConfig`for details. |

## HostAndPort.host

The host of the emulator. Can be omitted if discovered automatically through the hub or specified via environment variables. See`TestEnvironmentConfig`for details.

**Signature:**  

    host: string;

## HostAndPort.port

The port of the emulator. Can be omitted if discovered automatically through the hub or specified via environment variables. See`TestEnvironmentConfig`for details.

**Signature:**  

    port: number;