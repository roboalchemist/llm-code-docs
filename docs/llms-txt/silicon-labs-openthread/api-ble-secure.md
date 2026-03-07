# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api-ble-secure.md

# BLE Secure

This module includes functions that control BLE Secure (TLS over BLE) communication.

This module includes functions that implement TCAT communication.

The functions in this module are available when BLE Secure API feature (`OPENTHREAD_CONFIG_BLE_TCAT_ENABLE`) is enabled.

The functions in this module are available when TCAT feature (`OPENTHREAD_CONFIG_BLE_TCAT_ENABLE`) is enabled.

## Modules

[otTcatAdvertisedDeviceId](ot-tcat-advertised-device-id)

[otTcatGeneralDeviceId](ot-tcat-general-device-id)

[otTcatVendorInfo](ot-tcat-vendor-info)

## Enumerations

### otTcatStatusCode

```c
enum otTcatStatusCode {
    OT_TCAT_STATUS_SUCCESS = 0
    OT_TCAT_STATUS_UNSUPPORTED = 1
    OT_TCAT_STATUS_PARSE_ERROR = 2
    OT_TCAT_STATUS_VALUE_ERROR = 3
    OT_TCAT_STATUS_GENERAL_ERROR = 4
    OT_TCAT_STATUS_BUSY = 5
    OT_TCAT_STATUS_UNDEFINED = 6
    OT_TCAT_STATUS_HASH_ERROR = 7
    OT_TCAT_STATUS_INVALID_STATE = 8
    OT_TCAT_STATUS_UNAUTHORIZED = 16
}
```

**Description:**

Represents TCAT status code.

**Enumerator:**

|   |   |
|---|---|
|OT_TCAT_STATUS_SUCCESS|Command or request was successfully processed.|
|OT_TCAT_STATUS_UNSUPPORTED|Requested command or received TLV is not supported.|
|OT_TCAT_STATUS_PARSE_ERROR|Request / command could not be parsed correctly.|
|OT_TCAT_STATUS_VALUE_ERROR|The value of the transmitted TLV has an error.|
|OT_TCAT_STATUS_GENERAL_ERROR|An error not matching any other category occurred.|
|OT_TCAT_STATUS_BUSY|Command cannot be executed because the resource is busy.|
|OT_TCAT_STATUS_UNDEFINED|The requested value, data or service is not defined (currently) or not present.|
|OT_TCAT_STATUS_HASH_ERROR|The hash value presented by the commissioner was incorrect.|
|OT_TCAT_STATUS_INVALID_STATE|The TCAT device is not in a correct state for the given command.|
|OT_TCAT_STATUS_UNAUTHORIZED|Sender does not have sufficient authorization for the given command.|

### otTcatApplicationProtocol

```c
enum otTcatApplicationProtocol {
    OT_TCAT_APPLICATION_PROTOCOL_NONE = 0
    OT_TCAT_APPLICATION_PROTOCOL_STATUS = 0x01
    OT_TCAT_APPLICATION_PROTOCOL_RESPONSE =
        0x02
    OT_TCAT_APPLICATION_PROTOCOL_1 = 0x81
    OT_TCAT_APPLICATION_PROTOCOL_2 = 0x82
    OT_TCAT_APPLICATION_PROTOCOL_3 = 0x83
    OT_TCAT_APPLICATION_PROTOCOL_4 = 0x84
    OT_TCAT_APPLICATION_PROTOCOL_VENDOR = 0x9F
}
```

**Description:**

Represents TCAT application protocol options.

**Enumerator:**

|   |   |
|---|---|
|OT_TCAT_APPLICATION_PROTOCOL_NONE|Message which has been sent without activating the TCAT agent.|
|OT_TCAT_APPLICATION_PROTOCOL_STATUS||
|OT_TCAT_APPLICATION_PROTOCOL_RESPONSE|Message directed to any application protocol indicating a response with status value (one byte otTcatStatusCode)|
|OT_TCAT_APPLICATION_PROTOCOL_1|Message directed to application protocol 1.|
|OT_TCAT_APPLICATION_PROTOCOL_2|Message directed to application protocol 2.|
|OT_TCAT_APPLICATION_PROTOCOL_3|Message directed to application protocol 3.|
|OT_TCAT_APPLICATION_PROTOCOL_4|Message directed to application protocol 4.|
|OT_TCAT_APPLICATION_PROTOCOL_VENDOR|Message directed to a vendor specific application protocol.|

### otTcatCommandClass

```c
enum otTcatCommandClass {
    OT_TCAT_COMMAND_CLASS_GENERAL = 0
    OT_TCAT_COMMAND_CLASS_COMMISSIONING = 1
    OT_TCAT_COMMAND_CLASS_EXTRACTION = 2
    OT_TCAT_COMMAND_CLASS_DECOMMISSIONING = 3
    OT_TCAT_COMMAND_CLASS_APPLICATION = 4
}
```

**Description:**

Represents a TCAT command class.

**Enumerator:**

|   |   |
|---|---|
|OT_TCAT_COMMAND_CLASS_GENERAL|TCAT commands related to general operations.|
|OT_TCAT_COMMAND_CLASS_COMMISSIONING|TCAT commands related to commissioning.|
|OT_TCAT_COMMAND_CLASS_EXTRACTION|TCAT commands related to key extraction.|
|OT_TCAT_COMMAND_CLASS_DECOMMISSIONING|TCAT commands related to de-commissioning.|
|OT_TCAT_COMMAND_CLASS_APPLICATION|TCAT commands related to application layer.|

### otTcatAdvertisedDeviceIdType

```c
enum otTcatAdvertisedDeviceIdType {
    OT_TCAT_DEVICE_ID_EMPTY = 0
    OT_TCAT_DEVICE_ID_OUI24 = 1
    OT_TCAT_DEVICE_ID_OUI36 = 2
    OT_TCAT_DEVICE_ID_DISCRIMINATOR = 3
    OT_TCAT_DEVICE_ID_IANAPEN = 4
    OT_TCAT_DEVICE_ID_MAX = 5
}
```

**Description:**

Represents Advertised Device ID type.

**Details:**

Used during TCAT advertisement.

**Enumerator:**

|   |   |
|---|---|
|OT_TCAT_DEVICE_ID_EMPTY|Advertised device ID type not set.|
|OT_TCAT_DEVICE_ID_OUI24|Advertised device ID type IEEE OUI-24.|
|OT_TCAT_DEVICE_ID_OUI36|Advertised device ID type IEEE OUI-36.|
|OT_TCAT_DEVICE_ID_DISCRIMINATOR|Advertised device ID type Device Discriminator.|
|OT_TCAT_DEVICE_ID_IANAPEN|Advertised device ID type IANA PEN.|
|OT_TCAT_DEVICE_ID_MAX|Advertised device ID max number of types.|

## Typedefs

### otHandleBleSecureConnect

`typedef void(* otHandleBleSecureConnect) (otInstance *aInstance, bool aConnected, bool aBleConnectionOpen, void *aContext)`

**Description:**

Pointer to call when ble secure connection state changes.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aInstance|A pointer to an OpenThread instance.|
||[in]|aConnected|TRUE, if a secure connection was established, FALSE otherwise.|
||[in]|aBleConnectionOpen|TRUE if a BLE connection was established to carry a TLS data stream, FALSE otherwise.|
||[in]|aContext|A pointer to arbitrary context information.|

**Details:**

### otHandleBleSecureReceive

`typedef otHandleTcatApplicationDataReceive otHandleBleSecureReceive`

**Description:**

Pointer to call when data was received over a BLE Secure TLS connection.

**Details:**

When TCAT has been started, the TCAT agent automatically responds with status OT_TCAT_STATUS_UNSUPPORTED if no response has been generated or no handler is defined. The application may generate a response to incoming TCAT application data or vendor-specific data by calling [otBleSecureSendApplicationTlv](api-ble-secure#ot-ble-secure-send-application-tlv).

### otTcatStatusCode (Typedefs)

`typedef enum otTcatStatusCode otTcatStatusCode`

**Description:**

Represents TCAT status code.

### otTcatApplicationProtocol (Typedefs)

`typedef enum otTcatApplicationProtocol otTcatApplicationProtocol`

**Description:**

Represents TCAT application protocol options.

### otTcatCommandClass (Typedefs)

`typedef enum otTcatCommandClass otTcatCommandClass`

**Description:**

Represents a TCAT command class.

### otTcatAdvertisedDeviceIdType (Typedefs)

`typedef enum otTcatAdvertisedDeviceIdType otTcatAdvertisedDeviceIdType`

**Description:**

Represents Advertised Device ID type.

**Details:**

Used during TCAT advertisement.

### otTcatAdvertisedDeviceId

`typedef struct otTcatAdvertisedDeviceId otTcatAdvertisedDeviceId`

### otTcatGeneralDeviceId

`typedef struct otTcatGeneralDeviceId otTcatGeneralDeviceId`

**Description:**

Represents General Device ID type.

### otTcatVendorInfo

`typedef struct otTcatVendorInfo otTcatVendorInfo`

**Description:**

This structure represents a TCAT vendor information.

**Details:**

The content of this structure MUST persist and remain unchanged while a TCAT session is running.

### otHandleTcatApplicationDataReceive

`typedef void(* otHandleTcatApplicationDataReceive) (otInstance *aInstance, const otMessage *aMessage, int32_t aOffset, otTcatApplicationProtocol aTcatApplicationProtocol, void *aContext)`

**Description:**

Pointer to call when application data or vendor-specific data was received over a TCAT TLS connection.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aInstance|A pointer to an OpenThread instance.|
||[in]|aMessage|A pointer to the message.|
||[in]|aOffset|The offset where the application data begins.|
||[in]|aTcatApplicationProtocol|The application protocol the message is targeted to.|
||[in]|aContext|A pointer to arbitrary context information.|

**Details:**

The application may generate a response to an incoming TCAT application data packet. The TCAT agent automatically responds with status OT_TCAT_STATUS_UNSUPPORTED if no response has been generated or no handler is defined.

### otHandleTcatJoin

`typedef void(* otHandleTcatJoin) (otError aError, void *aContext)`

**Description:**

Pointer to call to notify the completion of a network join/leave operation performed under guidance of a TCAT Commissioner.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aError|OT_ERROR_NONE if the network join/leave operation was successfully started. OT_ERROR_INVALID_STATE if network join was requested but network credentials were missing or incomplete. OT_ERROR_REJECTED if a network join/leave operation was requested, but the TCAT Commissioner is not authorized to make such a request. OT_ERROR_SECURITY is reserved for future use for a failed join due to credential mismatch.|
||[in]|aContext|A pointer to arbitrary context information.|

**Details:**

## Functions

### otBleSecureStart

`otError otBleSecureStart(otInstance *aInstance, otHandleBleSecureConnect aConnectHandler, otHandleBleSecureReceive aReceiveHandler, bool aTlvMode, void *aContext)`

**Description:** Starts the BLE Secure service.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otHandleBleSecureConnect](api-ble-secure#ot-handle-ble-secure-connect)|[in]|aConnectHandler|A pointer to a function that will be called when the connection state changes.|
|[otHandleBleSecureReceive](api-ble-secure#ot-handle-ble-secure-receive)|[in]|aReceiveHandler|A pointer to a function that will be called once data has been received over the TLS connection.|
|bool|[in]|aTlvMode|A boolean value indicating if TLV mode (TRUE) shall be activated, or line mode (FALSE).|
|void *|[in]|aContext|A pointer to arbitrary context information. May be NULL if not used.|

When TLV mode is active, the function `aReceiveHandler` will be called once a complete TLV or line was received and the message offset points to the TLV value.

### otBleSecureSetTcatVendorInfo

`otError otBleSecureSetTcatVendorInfo(otInstance *aInstance, const otTcatVendorInfo *aVendorInfo)`

**Description:** Sets TCAT vendor info.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otTcatVendorInfo](ot-tcat-vendor-info) *|[in]|aVendorInfo|A pointer to the Vendor Information (MUST remain valid after the method call).|

The vendor info is used for advertising in TCAT Advertisements, as well as for responding to particular TCAT commands that supply vendor info to the TCAT Commissioner.

### otBleSecureTcatStart

`otError otBleSecureTcatStart(otInstance *aInstance, otHandleTcatJoin aJoinHandler)`

**Description:** Enables the TCAT protocol over BLE Secure.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otHandleTcatJoin](api-ble-secure#ot-handle-tcat-join)|[in]|aJoinHandler|A pointer to a function that is called when a network join or leave operation is requested under guidance of the TCAT Commissioner.|

### otBleSecureStop

`void otBleSecureStop(otInstance *aInstance)`

**Description:** Stops the BLE Secure server.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

If the TCAT agent is active, it is also stopped and any ongoing connection is forcibly ended.

### otBleSecureSetTcatAgentState

`otError otBleSecureSetTcatAgentState(otInstance *aInstance, bool aActive, uint32_t aDelayMs, uint32_t aDurationMs)`

**Description:** Sets the TCAT agent over BLE Secure into active or standby state.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|bool|[in]|aActive|If TRUE, attempts to set TCAT agent to active state. If FALSE, attempts to set TCAT agent to standby (inactive) state.|
|uint32_t|[in]|aDelayMs|Delay in ms before activating TCAT agent. If 0, activate immediately.|
|uint32_t|[in]|aDurationMs|Duration in ms of the activation of the TCAT agent. If 0, activate indefinitely.|

In standby state, no BLE advertisements are sent and TCAT Commissioners can't connect. TCAT can be automatically enabled via a TMF message while in standby.

### otBleSecureSetPsk

`void otBleSecureSetPsk(otInstance *aInstance, const uint8_t *aPsk, uint16_t aPskLength, const uint8_t *aPskIdentity, uint16_t aPskIdLength)`

**Description:** Sets the Pre-Shared Key (PSK) and cipher suite TLS_PSK_WITH_AES_128_CCM_8.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const uint8_t *|[in]|aPsk|A pointer to the PSK.|
|uint16_t|[in]|aPskLength|The PSK length.|
|const uint8_t *|[in]|aPskIdentity|The Identity Name for the PSK.|
|uint16_t|[in]|aPskIdLength|The PSK Identity Length.|

#### Note

- Requires the build-time feature `MBEDTLS_KEY_EXCHANGE_PSK_ENABLED` to be enabled.

### otBleSecureGetPeerCertificateBase64

`otError otBleSecureGetPeerCertificateBase64(otInstance *aInstance, unsigned char *aPeerCert, size_t *aCertLength)`

**Description:** Returns the peer x509 certificate base64 encoded.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|unsigned char *|[out]|aPeerCert|A pointer to the base64 encoded certificate buffer.|
|size_t *|[inout]|aCertLength|On input, the size the max size of `aPeerCert`. On output, the length of the base64 encoded peer certificate.|

#### Note (otBleSecureGetPeerCertificateBase64)

- Requires the build-time features `MBEDTLS_BASE64_C` and `MBEDTLS_SSL_KEEP_PEER_CERTIFICATE` to be enabled.

### otBleSecureGetPeerCertificateDer

`otError otBleSecureGetPeerCertificateDer(otInstance *aInstance, unsigned char *aPeerCert, size_t *aCertLength)`

**Description:** Returns the DER encoded peer x509 certificate.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|unsigned char *|[out]|aPeerCert|A pointer to the DER encoded certificate buffer.|
|size_t *|[inout]|aCertLength|On input, the size the max size of `aPeerCert`. On output, the length of the DER encoded peer certificate.|

#### Note (otBleSecureGetPeerCertificateDer)

- Requires the build-time feature `MBEDTLS_SSL_KEEP_PEER_CERTIFICATE` to be enabled.

### otBleSecureGetPeerSubjectAttributeByOid

`otError otBleSecureGetPeerSubjectAttributeByOid(otInstance *aInstance, const char *aOid, size_t aOidLength, uint8_t *aAttributeBuffer, size_t *aAttributeLength, int *aAsn1Type)`

**Description:** Returns an attribute value identified by its OID from the subject of the peer x509 certificate.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const char *|[in]|aOid|A pointer to the OID to be found.|
|size_t|[in]|aOidLength|The length of the OID.|
|uint8_t *|[out]|aAttributeBuffer|A pointer to the attribute buffer.|
|size_t *|[inout]|aAttributeLength|On input, the size the max size of `aAttributeBuffer`. On output, the length of the attribute written to the buffer.|
|int *|[out]|aAsn1Type|A pointer to the ASN.1 type of the attribute written to the buffer.|

The peer OID is provided in binary format. The attribute length is set if the attribute was successfully read or zero if unsuccessful. The ASN.1 type as is set as defineded in the ITU-T X.690 standard if the attribute was successfully read.

#### Note (otBleSecureGetPeerSubjectAttributeByOid)

- Requires the build-time feature `MBEDTLS_SSL_KEEP_PEER_CERTIFICATE` to be enabled.

### otBleSecureGetThreadAttributeFromPeerCertificate

`otError otBleSecureGetThreadAttributeFromPeerCertificate(otInstance *aInstance, int aThreadOidDescriptor, uint8_t *aAttributeBuffer, size_t *aAttributeLength)`

**Description:** Returns an attribute value for the OID 1.3.6.1.4.1.44970.x from the v3 extensions of the peer x509 certificate, where the last digit x is set to aThreadOidDescriptor.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|int|[in]|aThreadOidDescriptor|The last digit of the Thread attribute OID.|
|uint8_t *|[out]|aAttributeBuffer|A pointer to the attribute buffer.|
|size_t *|[inout]|aAttributeLength|On input, the size the max size of `aAttributeBuffer`. On output, the length of the attribute written to the buffer.|

The attribute length is set if the attribute was successfully read or zero if unsuccessful. Requires a connection to be active.

#### Note (otBleSecureGetThreadAttributeFromPeer...)

- Requires the build-time feature `MBEDTLS_SSL_KEEP_PEER_CERTIFICATE` to be enabled.

### otBleSecureGetThreadAttributeFromOwnCertificate

`otError otBleSecureGetThreadAttributeFromOwnCertificate(otInstance *aInstance, int aThreadOidDescriptor, uint8_t *aAttributeBuffer, size_t *aAttributeLength)`

**Description:** Returns an attribute value for the OID 1.3.6.1.4.1.44970.x from the v3 extensions of the own x509 certificate, where the last digit x is set to aThreadOidDescriptor.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|int|[in]|aThreadOidDescriptor|The last digit of the Thread attribute OID.|
|uint8_t *|[out]|aAttributeBuffer|A pointer to the attribute buffer.|
|size_t *|[inout]|aAttributeLength|On input, the size the max size of `aAttributeBuffer`. On output, the length of the attribute written to the buffer.|

The attribute length is set if the attribute was successfully read or zero if unsuccessful. Requires a connection to be active.

### otBleSecureSetSslAuthMode

`void otBleSecureSetSslAuthMode(otInstance *aInstance, bool aVerifyPeerCertificate)`

**Description:** Sets the authentication mode for the BLE secure connection.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|bool|[in]|aVerifyPeerCertificate|true, to verify the peer certificate.|

Disable or enable the verification of peer certificate. Must be called before start.

### otBleSecureSetCertificate

`void otBleSecureSetCertificate(otInstance *aInstance, const uint8_t *aX509Cert, uint32_t aX509Length, const uint8_t *aPrivateKey, uint32_t aPrivateKeyLength)`

**Description:** Sets the local device's X509 certificate and corresponding private key.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const uint8_t *|[in]|aX509Cert|A pointer to the PEM formatted X509 certificate.|
|uint32_t|[in]|aX509Length|The length of certificate.|
|const uint8_t *|[in]|aPrivateKey|A pointer to the PEM formatted private key.|
|uint32_t|[in]|aPrivateKeyLength|The length of the private key.|

Used for TLS sessions with cipher suite TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256.

#### Note (otBleSecureSetCertificate)

- Requires `MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED=1`.

### otBleSecureSetCaCertificateChain

`void otBleSecureSetCaCertificateChain(otInstance *aInstance, const uint8_t *aX509CaCertificateChain, uint32_t aX509CaCertChainLength)`

**Description:** Sets the trusted top level CAs.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const uint8_t *|[in]|aX509CaCertificateChain|A pointer to the PEM formatted X509 CA chain.|
|uint32_t|[in]|aX509CaCertChainLength|The length of chain.|

It is needed for validating the certificate of the peer via TLS.

Used for TLS sessions with cipher suite TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256.

#### Note (otBleSecureSetCaCertificateChain)

- Requires `MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED=1`.

### otBleSecureConnect

`otError otBleSecureConnect(otInstance *aInstance)`

**Description:** Initializes TLS session with a peer using an already open BLE connection.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

### otBleSecureDisconnect

`void otBleSecureDisconnect(otInstance *aInstance)`

**Description:** Stops the BLE and TLS connections.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

### otBleSecureIsConnectionActive

`bool otBleSecureIsConnectionActive(otInstance *aInstance)`

**Description:** Indicates whether or not the TLS session is active (connected or connecting).

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

### otBleSecureIsConnected

`bool otBleSecureIsConnected(otInstance *aInstance)`

**Description:** Indicates whether or not the TLS session is connected.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

### otBleSecureIsTcatAgentStarted

`bool otBleSecureIsTcatAgentStarted(otInstance *aInstance)`

**Description:** Indicates whether or not the TCAT agent is started over BLE secure.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|N/A|aInstance||

### otBleSecureIsCommandClassAuthorized

`bool otBleSecureIsCommandClassAuthorized(otInstance *aInstance, otTcatCommandClass aCommandClass)`

**Description:** Indicates whether or not a TCAT command class is authorized for the current TCAT Commissioner.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otTcatCommandClass](api-ble-secure#ot-tcat-command-class)|[in]|aCommandClass|A command class to check.|

### otBleSecureSendMessage

`otError otBleSecureSendMessage(otInstance *aInstance, otMessage *aMessage)`

**Description:** Sends a secure BLE message.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otMessage](api-message#ot-message) *|[in]|aMessage|A pointer to the message to send.|

If the return value is OT_ERROR_NONE, OpenThread takes ownership of `aMessage`, and the caller should no longer reference `aMessage`. If the return value is not OT_ERROR_NONE, the caller retains ownership of `aMessage`, including freeing `aMessage` if the message buffer is no longer needed.

### otBleSecureSend

`otError otBleSecureSend(otInstance *aInstance, uint8_t *aBuf, uint16_t aLength)`

**Description:** Sends a secure BLE data packet.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint8_t *|[in]|aBuf|A pointer to the data to send as the Value of the TCAT Send Application Data TLV.|
|uint16_t|[in]|aLength|A number indicating the length of the data buffer.|

### otBleSecureSendApplicationTlv

`otError otBleSecureSendApplicationTlv(otInstance *aInstance, otTcatApplicationProtocol aApplicationProtocol, uint8_t *aBuf, uint16_t aLength)`

**Description:** Sends a secure BLE data packet containing application data directed to the application layer `aApplicationProtocol` or a response to the latest received application data packet.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otTcatApplicationProtocol](api-ble-secure#ot-tcat-application-protocol)|[in]|aApplicationProtocol|An application protocol the data is directed to.|
|uint8_t *|[in]|aBuf|A pointer to the data to send as the Value of the TCAT Send Application Data TLV.|
|uint16_t|[in]|aLength|A number indicating the length of the data buffer.|

Only a single response can be sent while executing the `otHandleBleSecureReceive` handler. If no (further) response is expected `OT_ERROR_REJECTED` is returned.

For responses with a payload `aApplicationProtocol` shall be set to `OT_TCAT_APPLICATION_PROTOCOL_PAYLOAD`. For responses with a status `aApplicationProtocol` shall be `OT_TCAT_APPLICATION_PROTOCOL_STATUS` and @ aBuf shall contain a single byte `otTcatStatusCode` value.

### otBleSecureFlush

`otError otBleSecureFlush(otInstance *aInstance)`

**Description:** Flushes the send buffer.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

### otBleSecureGetInstallCodeVerifyStatus

`bool otBleSecureGetInstallCodeVerifyStatus(otInstance *aInstance)`

**Description:** Gets the Install Code Verify Status during the current session.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

## Macros

`#define OT_TCAT_SERVICE_NAME_MAX_LENGTH     15`

**Description**: Maximum string length of a UDP or TCP service name (does not include null char).

`#define OT_TCAT_APPLICATION_LAYER_MAX_COUNT 4`

**Description**: Maximum number of application layer service names supported.

`#define OT_TCAT_ADVERTISEMENT_MAX_LEN 29`

**Description**: Maximum length of TCAT advertisement.

`#define OT_TCAT_OPCODE 0x2`

**Description**: TCAT Advertisement Operation Code.

`#define OT_TCAT_MAX_ADVERTISED_DEVICEID_SIZE 5`

**Description**: TCAT max size of any type of advertised Device ID.

`#define OT_TCAT_MAX_DEVICEID_SIZE 64`

**Description**: TCAT max size of device ID.

`#define OT_TCAT_ENABLE_MAX 600`

**Description**: TCAT_ENABLE_MAX, default max TMF TCAT enable time, in seconds.
