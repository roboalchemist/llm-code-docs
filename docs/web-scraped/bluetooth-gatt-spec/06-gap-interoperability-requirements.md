# Source: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/Core-54/out/en/host/generic-attribute-profile--gatt-.html

## 6. GAP interoperability requirements

### 6.1. BR/EDR GAP interoperability requirements

#### 6.1.1. Connection Establishment

To establish an Unenhanced ATT bearer, the Channel Establishment procedure (as defined in [[Vol 3]
Part C,
Section 7.2](generic-access-profile.html#UUID-66e26fe4-1dca-77b1-e1f5-96965a52bf53 "7.2 Channel Establishment")) shall be used with the PSM set to ATT.

Either device may establish an ATT bearer at any time.

To establish an Enhanced ATT bearer, the  [Section 5.3](generic-attribute-profile--gatt-.html#UUID-2f352749-51c3-45d3-fb4e-63d05aab9263 "5.3 Enhanced ATT bearer L2CAP interoperability requirements") procedure shall be used with the fixed PSM set to EATT. A device shall not attempt to establish an Enhanced ATT bearer with a peer unless it is aware that the peer supports Enhanced ATT bearers, for example by using an out of band method, via a higher layer protocol, or because the device has checked the peer’s Server Supported Features characteristic (see  [Section 7.4](generic-attribute-profile--gatt-.html#UUID-d42e9f3c-fbec-1849-cac4-127fc7de6c4c "7.4 Server Supported Features")) or its SDP record.

Either device may terminate an ATT bearer at any time.

No idle mode procedures or modes are defined by this profile.

### 6.2. LE GAP interoperability requirements

#### 6.2.1. Connection Establishment

To establish an Unenhanced ATT bearer, the Connection Establishment procedure (as defined in [[Vol 3]
Part C,
Section 9.3.5](generic-access-profile.html#UUID-0d008ea0-c2ae-7196-3cce-5f548a281331 "9.3.5 Auto Connection Establishment procedure") to [Section 9.3.8](generic-access-profile.html#UUID-c6c4fc0c-7b55-28a9-c370-c796fb94511a "9.3.8 Direct Connection Establishment procedure")) shall be used.

To establish an Enhanced ATT bearer, the  [Section 5.3](generic-attribute-profile--gatt-.html#UUID-2f352749-51c3-45d3-fb4e-63d05aab9263 "5.3 Enhanced ATT bearer L2CAP interoperability requirements") procedure shall be used with the fixed PSM set to EATT.

Either device may terminate an ATT bearer at any time.

No idle mode procedures or modes are defined by this profile.

# Note

Note: Unlike BR/EDR, it is not necessary to check the Server Supported Features characteristic before attempting to establish an Enhanced ATT bearer.

#### 6.2.2. Profile roles

This profile can be used in the following profile roles (as defined in [[Vol 3]
Part C,
Section 2.2.2](generic-access-profile.html#UUID-d61411b2-8e14-ec23-af7c-e2cc5b807025 "2.2.2 Roles when operating over an LE physical transport")):

- Central
- Peripheral

### 6.3. Disconnected events

#### 6.3.1. Notifications and indications while disconnected

If a client has configured the server to send a notification or indication to the client, it shall be configured to allow re-establishment of the connection when it is disconnected.

If the client is disconnected, but intends to become a Central in the connection it shall perform a GAP connection establishment procedure. If the client is disconnected, but intends to become a Peripheral in the connection it shall go into a GAP connectable mode.

A server shall re-establish a connection with a client when an event or trigger operation causes a notification or indication to a client.

If the server is disconnected, but intends to become a Peripheral in the connection it shall go into a GAP connectable mode. If the server is disconnected, but intends to become a Central in the connection it shall perform a GAP connection establishment procedure.

If the server cannot re-establish a connection, then the notification or indication for this event shall be discarded and no further connection re-establishment shall occur, until another event occurs.
