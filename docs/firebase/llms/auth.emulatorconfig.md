# Source: https://firebase.google.com/docs/reference/js/auth.emulatorconfig.md.txt

# EmulatorConfig interface

Configuration of Firebase Authentication Emulator.

**Signature:**  

    export interface EmulatorConfig 

## Properties

|                                                Property                                                 |                  Type                  |                                                            Description                                                            |
|---------------------------------------------------------------------------------------------------------|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [host](https://firebase.google.com/docs/reference/js/auth.emulatorconfig.md#emulatorconfighost)         | string                                 | The hostname of the emulator, which may be a domain ("localhost"), IPv4 address ("127.0.0.1") or quoted IPv6 address ("\[::1\]"). |
| [options](https://firebase.google.com/docs/reference/js/auth.emulatorconfig.md#emulatorconfigoptions)   | { readonly disableWarnings: boolean; } | The emulator-specific options.                                                                                                    |
| [port](https://firebase.google.com/docs/reference/js/auth.emulatorconfig.md#emulatorconfigport)         | number \| null                         | The port of the emulator, or null if port isn't specified (i.e. protocol default).                                                |
| [protocol](https://firebase.google.com/docs/reference/js/auth.emulatorconfig.md#emulatorconfigprotocol) | string                                 | The protocol used to communicate with the emulator ("http"/"https").                                                              |

## EmulatorConfig.host

The hostname of the emulator, which may be a domain ("localhost"), IPv4 address ("127.0.0.1") or quoted IPv6 address ("\[::1\]").

**Signature:**  

    readonly host: string;

## EmulatorConfig.options

The emulator-specific options.

**Signature:**  

    readonly options: {
            readonly disableWarnings: boolean;
        };

## EmulatorConfig.port

The port of the emulator, or null if port isn't specified (i.e. protocol default).

**Signature:**  

    readonly port: number | null;

## EmulatorConfig.protocol

The protocol used to communicate with the emulator ("http"/"https").

**Signature:**  

    readonly protocol: string;