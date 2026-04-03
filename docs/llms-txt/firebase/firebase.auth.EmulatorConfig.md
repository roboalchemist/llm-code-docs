# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.EmulatorConfig.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.auth.EmulatorConfig.md.txt

# EmulatorConfig | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/node/firebase).
- [auth](https://firebase.google.com/docs/reference/node/firebase.auth).
- EmulatorConfig

Configuration of Firebase Authentication Emulator.

## Index

### Properties

- [host](https://firebase.google.com/docs/reference/node/firebase.auth.EmulatorConfig#host)
- [options](https://firebase.google.com/docs/reference/node/firebase.auth.EmulatorConfig#options)
- [port](https://firebase.google.com/docs/reference/node/firebase.auth.EmulatorConfig#port)
- [protocol](https://firebase.google.com/docs/reference/node/firebase.auth.EmulatorConfig#protocol)

## Properties

### host

host: string  
The hostname of the emulator, which may be a domain ("localhost"), IPv4 address ("127.0.0.1")
or quoted IPv6 address ("\[::1\]").

### options

options: { disableWarnings: boolean }  
The emulator-specific options.  

#### Type declaration

-

  ##### disableWarnings: boolean

  Whether the warning banner attached to the DOM was disabled.

### port

port: number \| null  
The port of the emulator, or null if port isn't specified (i.e. protocol default).

### protocol

protocol: string  
The protocol used to communicate with the emulator ("http"/"https").