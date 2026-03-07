# Source: https://project-chip.github.io/connectedhomeip-doc/testing/ChipDeviceCtrlAPI.html

# ChipDeviceCtrl.py API

## Contents

# ChipDeviceCtrl.py API

* matter.ChipDeviceCtrl

  * RegisterOnActiveCallback

  * UnregisterOnActiveCallback

  * WaitForCheckIn

  * CallbackContext

  * CommissioningContext

  * CommissionableNode

    * Commission

  * DeviceProxyWrapper

  * ChipDeviceControllerBase

    * Shutdown

    * ShutdownAll

    * CheckIsActive

    * IsConnected

    * ConnectBLE

    * ConnectNFC

    * ContinueCommissioningAfterConnectNetworkRequest

    * UnpairDevice

    * CloseBLEConnection

    * ExpireSessions

    * MarkSessionDefunct

    * MarkSessionForEviction

    * DeleteAllSessionResumptionStorage

    * SetLocalMRPConfig

    * ResetLocalMRPConfig

    * EstablishPASESessionBLE

    * EstablishPASESessionIP

    * EstablishPASESession

    * GetTestCommissionerUsed

    * SetTestCommissionerSimulateFailureOnStage

    * SetTestCommissionerSimulateFailureOnReport

    * SetTestCommissionerPrematureCompleteAfter

    * CheckTestCommissionerCallbacks

    * CheckStageSuccessful

    * CheckTestCommissionerPaseConnection

    * ResolveNode

    * GetAddressAndPort

    * DiscoverCommissionableNodes

    * GetDiscoveredDevices

    * GetIPForDiscoveredDevice

    * OpenCommissioningWindow

    * OpenJointCommissioningWindow

    * GetCompressedFabricId

    * GetFabricIdInternal

    * GetFabricIndexInternal

    * GetNodeIdInternal

    * GetRootPublicKeyBytesInternal

    * GetClusterHandler

    * FindOrEstablishPASESession

    * GetConnectedDeviceSync

    * WaitForActive

    * GetConnectedDevice

    * ComputeRoundTripTimeout

    * GetRemoteSessionParameters

    * TestOnlySendBatchCommands

    * TestOnlySendCommandTimedRequestFlagWithNoTimedInvoke

    * TestOnlyWriteAttributeWithMismatchedTimedRequestField

    * SendCommand

    * SendBatchCommands

    * SendGroupCommand

    * WriteAttribute

    * TestOnlyWriteAttributeWithLegacyList

    * WriteGroupAttribute

    * TestOnlyPrepareToReceiveBdxData

    * TestOnlyPrepareToSendBdxData

    * Read

    * ReadAttribute

    * ReadEvent

    * SetIpk

    * InitGroupTestingData

    * CreateManualCode

  * ChipDeviceController

    * Commission

    * CommissionBleThread

    * CommissionNfcThread

    * CommissionNfcWiFi

    * CommissionBleWiFi

    * SetWiFiCredentials

    * SetThreadOperationalDataset

    * ResetCommissioningParameters

    * SetTimeZone

    * SetDSTOffset

    * SetTCAcknowledgements

    * SetSkipCommissioningComplete

    * SetDefaultNTP

    * SetTrustedTimeSource

    * SetCheckMatchingFabric

    * GenerateICDRegistrationParameters

    * EnableICDRegistration

    * DisableICDRegistration

    * GetFabricCheckResult

    * CommissionOnNetwork

    * CommissionThreadMeshcop

    * get_rcac

    * CommissionWithCode

    * NOCChainCallback

    * IssueNOCChain

    * SetDACRevocationSetPath

  * BareChipDeviceController

    * __init__

# matter.ChipDeviceCtrl

Chip Device Controller interface

## RegisterOnActiveCallback

    def RegisterOnActiveCallback(scopedNodeId: ScopedNodeId,
                                 callback: typing.Callable[[ScopedNodeId], None])
    

Registers a callback when the device with given (fabric index, node id) becomes active.

Does nothing if the callback is already registered.

## UnregisterOnActiveCallback

    def UnregisterOnActiveCallback(scopedNodeId: ScopedNodeId,
                                   callback: typing.Callable[[ScopedNodeId],
                                                             None])
    

Unregisters a callback when the device with given (fabric index, node id) becomes active.

Does nothing if the callback has not been registered.

## WaitForCheckIn

    async def WaitForCheckIn(scopedNodeId: ScopedNodeId, timeoutSeconds: float)
    

Waits for a device becomes active.

__Returns__ :

* A future, completes when the device becomes active.

## CallbackContext

    class CallbackContext()
    

A context manager for handling callbacks that are expected to be called exactly once.

The context manager makes sure that no concurrent operations which use the same callback handlers are executed.

## CommissioningContext

    class CommissioningContext(CallbackContext)
    

A context manager for handling commissioning callbacks that are expected to be called exactly once.

This context also resets commissioning related device controller state.

## CommissionableNode

    class CommissionableNode(discovery.CommissionableNode)
    

### Commission

    def Commission(nodeId: int, setupPinCode: int) -> int
    

Commission the device using the device controller discovered this device.

nodeId: The nodeId commissioned to the device setupPinCode: The setup pin code of the device

__Returns__ :

* `int` \- Effective Node ID of the device (as defined by the assigned NOC)

## DeviceProxyWrapper

    class DeviceProxyWrapper()
    

Encapsulates a pointer to OperationalDeviceProxy on the c++ side that needs to be freed when DeviceProxyWrapper goes out of scope. There is a potential issue where if this is copied around that a double free will occur, but how this is used today that is not an issue that needs to be accounted for and it will become very apparent if that happens.

## ChipDeviceControllerBase

    class ChipDeviceControllerBase()
    

### Shutdown

    def Shutdown()
    

Shuts down this controller and reclaims any used resources, including the bound C++ constructor instance in the SDK.

__Raises__ :

* `ChipStackError` \- On failure.

__Returns__ :

None

### ShutdownAll

    def ShutdownAll()
    

Shut down all active controllers and reclaim any used resources.

### CheckIsActive

    def CheckIsActive()
    

Checks if the device controller is active.

__Raises__ :

* `RuntimeError` \- On failure.

### IsConnected

    def IsConnected()
    

Checks if the device controller is connected.

__Returns__ :

* `bool` \- True if is connected, False if not connected.

__Raises__ :

* `RuntimeError` \- If ‘_isActive’ is False (from the call to CheckIsActive).

### ConnectBLE

    async def ConnectBLE(discriminator: int,
                         setupPinCode: int,
                         nodeId: int,
                         isShortDiscriminator: bool = False) -> int
    

Connect to a BLE device via PASE using the given discriminator and setup pin code.

__Arguments__ :

* `discriminator` _int_ \- The long discriminator for the DNS-SD advertisement. Valid range: 0-4095.

* `setupPinCode` _int_ \- The setup pin code of the device.

* `nodeId` _int_ \- The node ID of the device.

* `isShortDiscriminator` _Optional[bool]_ \- Optional short discriminator.

__Returns__ :

* `int` \- Effective Node ID of the device (as defined by the assigned NOC).

### ConnectNFC

    async def ConnectNFC(discriminator: int, setupPinCode: int,
                         nodeId: int) -> int
    

Connect to a NFC device via PASE using the given discriminator and setup pin code.

__Arguments__ :

* `discriminator` _int_ \- The long discriminator for the DNS-SD advertisement. Valid range: 0-4095.

* `setupPinCode` _int_ \- The setup pin code of the device.

* `nodeId` _int_ \- The node ID of the device.

__Returns__ :

* `int` \- Effective Node ID of the device (as defined by the assigned NOC).

### ContinueCommissioningAfterConnectNetworkRequest

    async def ContinueCommissioningAfterConnectNetworkRequest(nodeId: int) -> int
    

This method is used in case of NFC-based Commissioning without power. It instructs the commissioner to proceed to the 2nd commissioning phase on the operational network, after the device has connected to that network.

__Arguments__ :

* `nodeId` _int_ \- The node ID of the device (commissionee).

__Returns__ :

* `int` \- Effective Node ID of the device (as defined by the assigned NOC).

### UnpairDevice

    async def UnpairDevice(nodeId: int) -> None
    

Unpairs the device with the specified node ID.

__Arguments__ :

* `nodeId` _int_ \- The node ID of the device.

__Returns__ :

None.

### CloseBLEConnection

    def CloseBLEConnection()
    

Closes the BLE connection for the device controller.

__Raises__ :

* `ChipStackError` \- On failure.

### ExpireSessions

    def ExpireSessions(nodeId: int)
    

Close all sessions with `nodeId` (if any existed) so that sessions get re-established.

This is needed to properly handle operations that invalidate a node’s state, such as UpdateNOC.

WARNING: ONLY CALL THIS IF YOU UNDERSTAND THE SIDE-EFFECTS

__Arguments__ :

* `nodeId` _int_ \- The node ID of the device.

__Raises__ :

* `ChipStackError` \- On failure.

### MarkSessionDefunct

    def MarkSessionDefunct(nodeId: int)
    

Marks a previously active session with the specified node as defunct to temporarily prevent it from being used with new exchanges to send or receive messages. This should be called when there is suspicion of a loss-of-sync with the session state on the associated peer, such as evidence of transport failure.

If messages are received thereafter on this session, the session will be put back into the Active state.

This function should only be called on an active session. This will NOT detach any existing SessionHolders.

__Arguments__ :

* `nodeId` _int_ \- The node ID of the device whose session should be marked as defunct.

__Raises__ :

* `RuntimeError` \- If the controller is not active.

* `PyChipError` \- If the operation fails.

### MarkSessionForEviction

    def MarkSessionForEviction(nodeId: int)
    

Marks the session with the specified node for eviction. It will first detach all SessionHolders attached to this session by calling ‘OnSessionReleased’ on each of them. This will force them to release their reference to the session. If there are no more references left, the session will then be de-allocated.

Once marked for eviction, the session SHALL NOT ever become active again.

__Arguments__ :

* `nodeId` _int_ \- The node ID of the device whose session should be marked for eviction.

__Raises__ :

* `RuntimeError` \- If the controller is not active.

* `PyChipError` \- If the operation fails.

### DeleteAllSessionResumptionStorage

    def DeleteAllSessionResumptionStorage()
    

Remove all session resumption information associated with the fabric index of the controller.

__Raises__ :

* `RuntimeError` \- If the controller is not active.

* `PyChipError` \- If the operation fails.

### SetLocalMRPConfig

    def SetLocalMRPConfig(idle_ms: int, active_ms: int, active_threshold_ms: int)
    

Set the local MRP config. This will be advertised to peers and used by them for message retransmissions.

__Arguments__ :

* `idle_ms` _int_ \- The idle retransmission interval in milliseconds.

* `active_ms` _int_ \- The active retransmission interval in milliseconds.

* `active_threshold_ms` _int_ \- The active threshold time in milliseconds.

__Raises__ :

* `ChipStackError` \- On failure.

### ResetLocalMRPConfig

    def ResetLocalMRPConfig()
    

Resets the local MRP config to the default values.

__Raises__ :

* `ChipStackError` \- On failure.

### EstablishPASESessionBLE

    async def EstablishPASESessionBLE(setupPinCode: int, discriminator: int,
                                      nodeId: int) -> None
    

Establish a PASE session over BLE.

Warning: This method attempts to establish a new PASE session, even if an open session already exists. For safer session management that reuses existing sessions, see `FindOrEstablishPASESession`.

__Arguments__ :

* `discriminator` _int_ \- The long discriminator for the DNS-SD advertisement. Valid range: 0-4095.

* `setupPinCode` _int_ \- The setup pin code of the device.

* `nodeId` _int_ \- The node ID of the device.

__Returns__ :

None

### EstablishPASESessionIP

    async def EstablishPASESessionIP(ipaddr: str,
                                     setupPinCode: int,
                                     nodeId: int,
                                     port: int = 0) -> None
    

Establish a PASE session over IP.

Warning: This method attempts to establish a new PASE session, even if an open session already exists. For safer session management that reuses existing sessions, see `FindOrEstablishPASESession`.

__Arguments__ :

* `ipaddr` _str_ \- IP address.

* `port` _int_ \- IP port to use (default is 0).

* `setupPinCode` _int_ \- The setup pin code of the device.

* `nodeId` _int_ \- The node ID of the device.

__Returns__ :

None

### EstablishPASESession

    async def EstablishPASESession(setUpCode: str, nodeId: int) -> None
    

Establish a PASE session using setUpCode.

Warning: This method attempts to establish a new PASE session, even if an open session already exists. For safer session management that reuses existing sessions, see `FindOrEstablishPASESession`.

__Arguments__ :

* `setUpCode` _str_ \- The setup code of the device.

* `nodeId` _int_ \- The node ID assigned to the device for the PASE session.

__Returns__ :

None

### GetTestCommissionerUsed

    def GetTestCommissionerUsed()
    

Get the status of test commissioner in use.

__Returns__ :

* `bool` \- True if the test commissioner is in use, False if not.

### SetTestCommissionerSimulateFailureOnStage

    def SetTestCommissionerSimulateFailureOnStage(stage: int)
    

Simulates a failure on a specific stage of the test commissioner.

__Arguments__ :

* `stage` _int_ \- The commissioning stage where failure will be simulated. This corresponds to the enum `CommissioningStage` (e.g. kError, kSecurePairing, etc.). For full details ref https://github.com/project-chip/connectedhomeip/blob/master/src/controller/CommissioningDelegate.h

__Returns__ :

* `bool` \- True if the failure simulate success, False if not.

### SetTestCommissionerSimulateFailureOnReport

    def SetTestCommissionerSimulateFailureOnReport(stage: int)
    

Simulates a failure on report of the test commissioner.

__Arguments__ :

* `stage` _int_ \- The commissioning stage where failure will be simulated. This corresponds to the enum `CommissioningStage` (e.g. kError, kSecurePairing, etc.). For full details ref https://github.com/project-chip/connectedhomeip/blob/master/src/controller/CommissioningDelegate.h

__Returns__ :

* `bool` \- True if the failure simulate success, False if not.

### SetTestCommissionerPrematureCompleteAfter

    def SetTestCommissionerPrematureCompleteAfter(stage: int)
    

Premature complete of the test commissioner.

__Arguments__ :

* `stage` _int_ \- The commissioning stage after a premature completion is simulated. This corresponds to the enum `CommissioningStage` (e.g. kError, kSecurePairing, etc.). For full details ref https://github.com/project-chip/connectedhomeip/blob/master/src/controller/CommissioningDelegate.h

__Returns__ :

* `bool` \- True if the premature complete success, False if not.

### CheckTestCommissionerCallbacks

    def CheckTestCommissionerCallbacks()
    

Check the test commissioner callbacks.

__Returns__ :

* `bool` \- True if the test commissioner callbacks success, False if not.

### CheckStageSuccessful

    def CheckStageSuccessful(stage: int)
    

Check the test commissioner stage success.

__Arguments__ :

* `stage` _int_ \- The commissioning to simulate.

__Returns__ :

* `bool` \- True if test commissioner stage success, False if not.

### CheckTestCommissionerPaseConnection

    def CheckTestCommissionerPaseConnection(nodeId: int)
    

Check the test commissioner Pase connection success.

__Arguments__ :

* `nodeId` _int_ \- The node ID of the device.

__Returns__ :

* `bool` \- True if test commissioner Pase connection success, False if not.

### ResolveNode

    def ResolveNode(nodeId: int)
    

Resolve node ID.

__Arguments__ :

* `nodeId` _int_ \- The node ID of the device.

### GetAddressAndPort

    def GetAddressAndPort(nodeId: int)
    

Get the address and port.

__Arguments__ :

* `nodeId` _int_ \- The node ID of the device.

__Returns__ :

* `tuple` \- The address and port if no error occurs or None on failure.

### DiscoverCommissionableNodes

    async def DiscoverCommissionableNodes(
        filterType: discovery.FilterType = discovery.FilterType.NONE,
        filter: typing.Any = None,
        stopOnFirst: bool = False,
        timeoutSecond: int = 5
    ) -> typing.Union[None, CommissionableNode, typing.List[CommissionableNode]]
    

Discover commissionable nodes via DNS-SD with specified filters. Supported filters are:

discovery.FilterType.NONE discovery.FilterType.SHORT_DISCRIMINATOR discovery.FilterType.LONG_DISCRIMINATOR discovery.FilterType.VENDOR_ID discovery.FilterType.DEVICE_TYPE discovery.FilterType.COMMISSIONING_MODE discovery.FilterType.INSTANCE_NAME discovery.FilterType.COMMISSIONER discovery.FilterType.COMPRESSED_FABRIC_ID

This function will always return a list of CommissionableDevice. When stopOnFirst is set, this function will return when at least one device is discovered or on timeout.

__Returns__ :

* `list` \- A list of discovered devices.

### GetDiscoveredDevices

    async def GetDiscoveredDevices()
    

Get the discovered devices.

__Returns__ :

* `list` \- A list of discovered devices.

### GetIPForDiscoveredDevice

    def GetIPForDiscoveredDevice(idx, addrStr, length)
    

Get the IP address for a discovered device.

__Arguments__ :

* `idx` _int_ \- Index of the discovered device.

* `addrStr` _str_ \- Address of the device.

* `length` _int_ \- Length of the address.

__Returns__ :

* `bool` \- True if IP for discovered device success, False if not.

### OpenCommissioningWindow

    async def OpenCommissioningWindow(
            nodeId: int, timeout: int, iteration: int, discriminator: int,
            option: CommissioningWindowPasscode) -> CommissioningParameters
    

Opens a commissioning window on the device with the given node ID.

__Arguments__ :

* `nodeId` _int_ \- The node ID of the device.

* `timeout` _int_ \- Command timeout

* `iteration` _int_ \- The PAKE iteration count associated with the PAKE Passcode ID and ephemeral PAKE passcode verifier to be used for this commissioning. Valid range: 1000 - 100000 Ignored if option == 0

* `discriminator` _int_ \- The long discriminator for the DNS-SD advertisement. Valid range: 0-4095 Ignored if option == 0 option (int): 0 = kOriginalSetupCode 1 = kTokenWithRandomPIN

__Returns__ :

CommissioningParameters

### OpenJointCommissioningWindow

    async def OpenJointCommissioningWindow(
            nodeId: int, endpointId: int, timeout: int, iteration: int,
            discriminator: int) -> CommissioningParameters
    

Opens a joint commissioning window on the device with the given node ID.

__Arguments__ :

* `nodeId` _int_ \- The node ID of the device.

* `timeout` _int_ \- Command timeout

* `iteration` _int_ \- The PAKE iteration count associated with the PAKE Passcode ID and ephemeral PAKE passcode verifier to be used for this commissioning. Valid range: 1000 - 100000

* `discriminator` _int_ \- The long discriminator for the DNS-SD advertisement. Valid range: 0-4095

__Returns__ :

CommissioningParameters

### GetCompressedFabricId

    def GetCompressedFabricId()
    

Get compressed fabric Id.

__Returns__ :

* `int` \- The compressed fabric ID as a 64-bit integer.

__Raises__ :

* `ChipStackError` \- On failure.

### GetFabricIdInternal

    def GetFabricIdInternal() -> int
    

Get the fabric ID from the object. Only used to validate cached value from property.

__Returns__ :

* `int` \- The raw fabric ID as a 64-bit integer.

__Raises__ :

* `ChipStackError` \- On failure.

### GetFabricIndexInternal

    def GetFabricIndexInternal() -> int
    

Get the fabric index from the object. Only used to validate cached value from property.

__Returns__ :

* `int` \- fabric index in local fabric table associated with this controller.

__Raises__ :

* `ChipStackError` \- On failure.

### GetNodeIdInternal

    def GetNodeIdInternal() -> int
    

Get the node ID from the object. Only used to validate cached value from property.

__Returns__ :

* `int` \- The Node ID as a 64 bit integer.

__Raises__ :

* `ChipStackError` \- On failure.

### GetRootPublicKeyBytesInternal

    def GetRootPublicKeyBytesInternal() -> bytes
    

Get the root public key associated with our fabric.

__Returns__ :

* `bytes` \- The root public key raw bytes in uncompressed point form.

__Raises__ :

* `ChipStackError` \- On failure.

### GetClusterHandler

    def GetClusterHandler()
    

Get cluster handler

__Returns__ :

* `ChipClusters` \- An instance of the ChipClusters class.

### FindOrEstablishPASESession

    async def FindOrEstablishPASESession(setupCode: str,
                                         nodeId: int,
                                         timeoutMs: typing.Optional[int] = None
                                         ) -> typing.Optional[DeviceProxyWrapper]
    

Find or establish a PASE session.

__Arguments__ :

* `setUpCode` _str_ \- The setup code of the device.

* `nodeId` _int_ \- The node ID of the device.

* `timeoutMs` _Optional[int]_ \- Optional timeout in milliseconds.

__Returns__ :

DeviceProxyWrapper on success, if not is None.

### GetConnectedDeviceSync

    def GetConnectedDeviceSync(
            nodeId: int,
            allowPASE=True,
            timeoutMs: typing.Optional[int] = None,
            payloadCapability: int = TransportPayloadCapability.MRP_PAYLOAD)
    

Gets an OperationalDeviceProxy or CommissioneeDeviceProxy for the specified Node.

__Arguments__ :

* `nodeId` _int_ \- Target’s Node ID

* `allowPASE` _bool_ \- Get a device proxy of a device being commissioned.

* `timeoutMs` _Optional[int]_ \- Timeout for a timed invoke request. Omit or set to ‘None’ to indicate a non-timed request.

__Returns__ :

DeviceProxyWrapper on success.

### WaitForActive

    async def WaitForActive(nodeId: int,
                            *,
                            timeoutSeconds=30.0,
                            stayActiveDurationMs=30000)
    

Waits a LIT ICD device to become active. Will send a StayActive command to the device on active to allow human operations.

__Arguments__ :

* `nodeId` \- Node ID of the LID ICD.

* `stayActiveDurationMs` \- The duration in the StayActive command, in milliseconds.

__Returns__ :

StayActiveResponse on success

### GetConnectedDevice

    async def GetConnectedDevice(
            nodeId: int,
            allowPASE: bool = True,
            timeoutMs: typing.Optional[int] = None,
            payloadCapability: int = TransportPayloadCapability.MRP_PAYLOAD)
    

Gets an OperationalDeviceProxy or CommissioneeDeviceProxy for the specified Node.

__Arguments__ :

* `nodeId` _int_ \- Target’s Node ID.

* `allowPASE` _bool_ \- Get a device proxy of a device being commissioned.

* `timeoutMs` _Optional[int]_ \- Timeout for a timed invoke request. Omit or set to ‘None’ to indicate a non-timed request.

__Returns__ :

DeviceProxyWrapper on success.

### ComputeRoundTripTimeout

    def ComputeRoundTripTimeout(nodeId: int,
                                upperLayerProcessingTimeoutMs: int = 0)
    

Returns a computed timeout value based on the round-trip time it takes for the peer at the other end of the session to receive a message, process it and send it back. This is computed based on the session type, the type of transport, sleepy characteristics of the target and a caller-provided value for the time it takes to process a message at the upper layer on the target For group sessions.

This will result in a session being established if one wasn’t already.

__Returns__ :

* `int` \- The computed timeout value in milliseconds, representing the round-trip time.

### GetRemoteSessionParameters

    def GetRemoteSessionParameters(
            nodeId: int) -> typing.Optional[SessionParameters]
    

Returns the SessionParameters of reported by the remote node associated with `nodeId`. If there is some error in getting SessionParameters None is returned.

This will result in a session being established if one wasn’t already established.

__Returns__ :

* `Optional[SessionParameters]` \- The session parameters.

### TestOnlySendBatchCommands

    async def TestOnlySendBatchCommands(
            nodeId: int,
            commands: typing.List[ClusterCommand.InvokeRequestInfo],
            timedRequestTimeoutMs: typing.Optional[int] = None,
            interactionTimeoutMs: typing.Optional[int] = None,
            busyWaitMs: typing.Optional[int] = None,
            suppressResponse: typing.Optional[bool] = None,
            remoteMaxPathsPerInvoke: typing.Optional[int] = None,
            suppressTimedRequestMessage: bool = False,
            commandRefsOverride: typing.Optional[typing.List[int]] = None)
    

Please see SendBatchCommands for description. TestOnly overridable arguments: remoteMaxPathsPerInvoke: Overrides the number of batch commands we think can be sent to remote node. suppressTimedRequestMessage: When set to true, we suppress sending Timed Request Message. commandRefsOverride: List of commandRefs to use for each command with the same index in `commands`.

__Returns__ :

TestOnlyBatchCommandResponse

### TestOnlySendCommandTimedRequestFlagWithNoTimedInvoke

    async def TestOnlySendCommandTimedRequestFlagWithNoTimedInvoke(
            nodeId: int,
            endpoint: int,
            payload: ClusterObjects.ClusterCommand,
            responseType=None)
    

Please see SendCommand for description.

__Returns__ :

Command response. The type of the response is defined by the command.

__Raises__ :

InteractionModelError on error

### TestOnlyWriteAttributeWithMismatchedTimedRequestField

    async def TestOnlyWriteAttributeWithMismatchedTimedRequestField(
            nodeid: int,
            attributes: typing.List[typing.Union[
                typing.Tuple[int, ClusterObjects.ClusterAttributeDescriptor],
                typing.Tuple[int, ClusterObjects.ClusterAttributeDescriptor,
                             int]]],
            timedRequestTimeoutMs: int,
            timedRequestFieldValue: bool,
            interactionTimeoutMs: typing.Optional[int] = None,
            busyWaitMs: typing.Optional[int] = None,
            payloadCapability: int = TransportPayloadCapability.MRP_PAYLOAD)
    

ONLY TO BE USED FOR TEST: Write attributes with decoupled Timed Request action and TimedRequest field. This allows testing TIMED_REQUEST_MISMATCH scenarios:

* timedRequestTimeoutMs=0, timedRequestFieldValue=True: No action, but field=true (MISMATCH)

* timedRequestTimeoutMs>0, timedRequestFieldValue=False: Action sent, but field=false (MISMATCH)

Please see WriteAttribute for description of common parameters.

Additional parameters: timedRequestTimeoutMs: Timeout for the Timed Request action (0 means no action) timedRequestFieldValue: Value of the TimedRequest field in WriteRequest

__Returns__ :

[AttributeStatus] (list - one for each path).

__Raises__ :

InteractionModelError on error (expected: TIMED_REQUEST_MISMATCH)

### SendCommand

    async def SendCommand(
            nodeId: int,
            endpoint: int,
            payload: ClusterObjects.ClusterCommand,
            responseType=None,
            timedRequestTimeoutMs: typing.Optional[int] = None,
            interactionTimeoutMs: typing.Optional[int] = None,
            busyWaitMs: typing.Optional[int] = None,
            suppressResponse: typing.Optional[bool] = None,
            payloadCapability: int = TransportPayloadCapability.MRP_PAYLOAD)
    

Send a cluster-object encapsulated command to a node and get returned a future that can be awaited upon to receive the response. If a valid responseType is passed in, that will be used to de-serialize the object. If not, the type will be automatically deduced from the metadata received over the wire.

timedWriteTimeoutMs: Timeout for a timed invoke request. Omit or set to ‘None’ to indicate a non-timed request. interactionTimeoutMs: Overall timeout for the interaction. Omit or set to ‘None’ to have the SDK automatically compute the right timeout value based on transport characteristics as well as the responsiveness of the target.

__Returns__ :

command response. The type of the response is defined by the command.

__Raises__ :

InteractionModelError on error

### SendBatchCommands

    async def SendBatchCommands(
            nodeId: int,
            commands: typing.List[ClusterCommand.InvokeRequestInfo],
            timedRequestTimeoutMs: typing.Optional[int] = None,
            interactionTimeoutMs: typing.Optional[int] = None,
            busyWaitMs: typing.Optional[int] = None,
            suppressResponse: typing.Optional[bool] = None,
            payloadCapability: int = TransportPayloadCapability.MRP_PAYLOAD)
    

Send a batch of cluster-object encapsulated commands to a node and get returned a future that can be awaited upon to receive the responses. If a valid responseType is passed in, that will be used to de-serialize the object. If not, the type will be automatically deduced from the metadata received over the wire.

nodeId: Target’s Node ID commands: A list of InvokeRequestInfo containing the commands to invoke. timedWriteTimeoutMs: Timeout for a timed invoke request. Omit or set to ‘None’ to indicate a non-timed request. interactionTimeoutMs: Overall timeout for the interaction. Omit or set to ‘None’ to have the SDK automatically compute the right timeout value based on transport characteristics as well as the responsiveness of the target. busyWaitMs: How long to wait in ms after sending command to device before performing any other operations. suppressResponse: Do not send a response to this action

__Returns__ :

* List of command responses in the same order as what was given in `commands`. The type of the response is defined by the command.

* A value of `None` indicates success.

* If only a single command fails, for example with `UNSUPPORTED_COMMAND`, the corresponding index associated with the command will, contain `interaction_model.Status.UnsupportedCommand`.

* If a command is not responded to by server, command will contain `interaction_model.Status.NoCommandResponse`

__Raises__ :

* InteractionModelError if error with sending of InvokeRequestMessage fails as a whole.

### SendGroupCommand

    def SendGroupCommand(groupid: int,
                         payload: ClusterObjects.ClusterCommand,
                         busyWaitMs: typing.Optional[int] = None)
    

Send a group cluster-object encapsulated command to a group_id and get returned a future that can be awaited upon to get confirmation command was sent.

__Returns__ :

* `None` \- responses are not sent to group commands.

__Raises__ :

InteractionModelError on error.

### WriteAttribute

    async def WriteAttribute(
            nodeId: int,
            attributes: typing.List[typing.Union[
                typing.Tuple[int, ClusterObjects.ClusterAttributeDescriptor],
                typing.Tuple[int, ClusterObjects.ClusterAttributeDescriptor,
                             int]]],
            timedRequestTimeoutMs: typing.Optional[int] = None,
            interactionTimeoutMs: typing.Optional[int] = None,
            busyWaitMs: typing.Optional[int] = None,
            payloadCapability: int = TransportPayloadCapability.MRP_PAYLOAD)
    

Write a list of attributes on a target node.

nodeId: Target’s Node ID timedWriteTimeoutMs: Timeout for a timed write request. Omit or set to ‘None’ to indicate a non-timed request. attributes: A list of tuples of type (endpoint, cluster-object): interactionTimeoutMs: Overall timeout for the interaction. Omit or set to ‘None’ to have the SDK automatically compute the right timeout value based on transport characteristics as well as the responsiveness of the target. E.g (1, Clusters.UnitTesting.Attributes.XYZAttribute(‘hello’)) – Write ‘hello’ to the XYZ attribute on the test cluster to endpoint 1

__Returns__ :

[AttributeStatus] (list - one for each path).

__Raises__ :

InteractionModelError on error.

### TestOnlyWriteAttributeWithLegacyList

    async def TestOnlyWriteAttributeWithLegacyList(
            nodeId: int,
            attributes: typing.List[typing.Union[
                typing.Tuple[int, ClusterObjects.ClusterAttributeDescriptor],
                typing.Tuple[int, ClusterObjects.ClusterAttributeDescriptor,
                             int]]],
            timedRequestTimeoutMs: typing.Optional[int] = None,
            interactionTimeoutMs: typing.Optional[int] = None,
            busyWaitMs: typing.Optional[int] = None,
            payloadCapability: int = TransportPayloadCapability.MRP_PAYLOAD)
    

Please see WriteAttribute for description. This is a test-only wrapper for _WriteAttribute that sets forceLegacyListEncoding to True.

The purpose of this method is to write attributes using the legacy encoding format for list data types, to ensure that end devices support legacy WriteClients.

__Returns__ :

[AttributeStatus] (list - one for each path).

__Raises__ :

InteractionModelError on error.

### WriteGroupAttribute

    def WriteGroupAttribute(groupid: int,
                            attributes: typing.List[typing.Tuple[
                                ClusterObjects.ClusterAttributeDescriptor, int]],
                            busyWaitMs: typing.Optional[int] = None)
    

Write a list of attributes on a target group.

groupid: Group ID to send write attribute to. attributes: A list of tuples of type (cluster-object, data-version). The data-version can be omitted.

E.g (Clusters.UnitTesting.Attributes.XYZAttribute(‘hello’), 1) – Group Write ‘hello’ with data version 1.

__Returns__ :

list = An empty list

__Raises__ :

InteractionModelError on error.

### TestOnlyPrepareToReceiveBdxData

    def TestOnlyPrepareToReceiveBdxData(
            max_block_size: int | None = None) -> asyncio.Future
    

Sets up the system to expect a node to initiate a BDX transfer. The transfer will send data here.

If no BDX transfer is initiated, the caller must cancel the returned future to avoid interfering with other BDX transfers. For example, the Diagnostic Logs clusters won’t start a BDX transfer when the log is small so the future must be cancelled to allow later attempts to retrieve logs to succeed.

If max_block_size is provided (1..65535), it overrides the controller’s default cap.

__Returns__ :

a future that will yield a BdxTransfer with the init message from the transfer.

__Raises__ :

InteractionModelError on error.

### TestOnlyPrepareToSendBdxData

    def TestOnlyPrepareToSendBdxData(data: bytes) -> asyncio.Future
    

Sets up the system to expect a node to initiate a BDX transfer. The transfer will send data to the node.

If no BDX transfer is initiated, the caller must cancel the returned future to avoid interfering with other BDX transfers.

__Returns__ :

A future that will yield a BdxTransfer with the init message from the transfer.

__Raises__ :

InteractionModelError on error.

### Read

    async def Read(
            nodeId: int,
            attributes: typing.
        Optional[typing.List[typing.Union[
            None,  # Empty tuple, all wildcard
            typing.Tuple[int],  # Endpoint
            # Wildcard endpoint, Cluster id present
            typing.Tuple[typing.Type[ClusterObjects.Cluster]],
            # Wildcard endpoint, Cluster + Attribute present
            typing.Tuple[typing.Type[ClusterObjects.ClusterAttributeDescriptor]],
            # Wildcard attribute id
            typing.Tuple[int, typing.Type[ClusterObjects.Cluster]],
            # Concrete path
            typing.Tuple[int,
                         typing.Type[ClusterObjects.ClusterAttributeDescriptor]],
            # Directly specified attribute path
            ClusterAttribute.AttributePath]]] = None,
            dataVersionFilters: typing.Optional[typing.List[typing.Tuple[
                int, typing.Type[ClusterObjects.Cluster], int]]] = None,
            events: typing.Optional[typing.List[typing.Union[
                None,  # Empty tuple, all wildcard
                typing.Tuple[str, int],  # all wildcard with urgency set
                typing.Tuple[int, int],  # Endpoint,
                # Wildcard endpoint, Cluster id present
                typing.Tuple[typing.Type[ClusterObjects.Cluster], int],
                # Wildcard endpoint, Cluster + Event present
                typing.Tuple[typing.Type[ClusterObjects.ClusterEvent], int],
                # Wildcard event id
                typing.Tuple[int, typing.Type[ClusterObjects.Cluster], int],
                # Concrete path
                typing.Tuple[int, typing.Type[ClusterObjects.ClusterEvent],
                             int]]]] = None,
            eventNumberFilter: typing.Optional[int] = None,
            returnClusterObject: bool = False,
            reportInterval: typing.Optional[typing.Tuple[int, int]] = None,
            fabricFiltered: bool = True,
            keepSubscriptions: bool = False,
            autoResubscribe: bool = True,
            payloadCapability: int = TransportPayloadCapability.MRP_PAYLOAD)
    

Read a list of attributes and/or events from a target node

nodeId: Target’s Node ID attributes: A list of tuples of varying types depending on the type of read being requested: (endpoint, Clusters.ClusterA.AttributeA): Endpoint = specific, Cluster = specific, Attribute = specific (endpoint, Clusters.ClusterA): Endpoint = specific, Cluster = specific, Attribute = *(Clusters.ClusterA.AttributeA): Endpoint =*, Cluster = specific, Attribute = specific endpoint: Endpoint = specific, Cluster = *, Attribute =* Clusters.ClusterA: Endpoint = _, Cluster = specific, Attribute = * ‘_ ’ or (): Endpoint = *, Cluster =*, Attribute = *

The cluster and attributes specified above are to be selected from the generated cluster objects.

e.g. ReadAttribute(1, [ 1 ] ) – case 4 above. ReadAttribute(1, [ Clusters.BasicInformation ] ) – case 5 above. ReadAttribute(1, [ (1, Clusters.BasicInformation.Attributes.Location ] ) – case 1 above.

An AttributePath can also be specified directly by [matter.cluster.Attribute.AttributePath(…)]

dataVersionFilters: A list of tuples of (endpoint, cluster, data version).

events: A list of tuples of varying types depending on the type of read being requested: (endpoint, Clusters.ClusterA.EventA, urgent): Endpoint = specific, Cluster = specific, Event = specific, Urgent = True/False (endpoint, Clusters.ClusterA, urgent): Endpoint = specific, Cluster = specific, Event = *, Urgent = True/False (Clusters.ClusterA.EventA, urgent): Endpoint =*, Cluster = specific, Event = specific, Urgent = True/False endpoint: Endpoint = specific, Cluster = *, Event =*, Urgent = True/False Clusters.ClusterA: Endpoint = *, Cluster = specific, Event = _, Urgent = True/False ‘_ ’ or (): Endpoint =*, Cluster = *, Event =*, Urgent = True/False

eventNumberFilter: Optional minimum event number filter.

returnClusterObject: This returns the data as consolidated cluster objects, with all attributes for a cluster inside a single cluster-wide cluster object.

reportInterval: A tuple of two int-s for (MinIntervalFloor, MaxIntervalCeiling). Used by establishing subscriptions. When not provided, a read request will be sent. fabricFiltered: If True (default), the read/subscribe is fabric-filtered and will only see things associated with the fabric of the reader/subscriber. Relevant for attributes with fabric-scoped data. keepSubscriptions: Keep existing subscriptions. If set to False, existing subscriptions with this node will get cancelled and a new one gets setup. autoResubscribe: Automatically resubscribe to the subscription if subscription is lost. The automatic re-subscription only applies if the subscription establishes on first try. If the first subscription establishment attempt fails the function returns right away.

__Returns__ :

* AsyncReadTransaction.ReadResponse. Please see ReadAttribute and ReadEvent for examples of how to access data.

__Raises__ :

* InteractionModelError (matter.interaction_model) on error

### ReadAttribute

    async def ReadAttribute(
            nodeId: int,
            attributes: typing.
        Optional[typing.List[typing.Union[
            None,  # Empty tuple, all wildcard
            typing.Tuple[int],  # Endpoint
            # Wildcard endpoint, Cluster id present
            typing.Tuple[typing.Type[ClusterObjects.Cluster]],
            # Wildcard endpoint, Cluster + Attribute present
            typing.Tuple[typing.Type[ClusterObjects.ClusterAttributeDescriptor]],
            # Wildcard attribute id
            typing.Tuple[int, typing.Type[ClusterObjects.Cluster]],
            # Concrete path
            typing.Tuple[int,
                         typing.Type[ClusterObjects.ClusterAttributeDescriptor]],
            # Directly specified attribute path
            ClusterAttribute.AttributePath]]],
            dataVersionFilters: typing.Optional[typing.List[typing.Tuple[
                int, typing.Type[ClusterObjects.Cluster], int]]] = None,
            returnClusterObject: bool = False,
            reportInterval: typing.Optional[typing.Tuple[int, int]] = None,
            fabricFiltered: bool = True,
            keepSubscriptions: bool = False,
            autoResubscribe: bool = True,
            payloadCapability: int = TransportPayloadCapability.MRP_PAYLOAD)
    

Read a list of attributes from a target node, this is a wrapper of DeviceController.Read()

nodeId: Target’s Node ID attributes: A list of tuples of varying types depending on the type of read being requested: (endpoint, Clusters.ClusterA.AttributeA): Endpoint = specific, Cluster = specific, Attribute = specific (endpoint, Clusters.ClusterA): Endpoint = specific, Cluster = specific, Attribute = *(Clusters.ClusterA.AttributeA): Endpoint =*, Cluster = specific, Attribute = specific endpoint: Endpoint = specific, Cluster = *, Attribute =* Clusters.ClusterA: Endpoint = _, Cluster = specific, Attribute = * ‘_ ’ or (): Endpoint = *, Cluster =*, Attribute = *

The cluster and attributes specified above are to be selected from the generated cluster objects.

e.g. ReadAttribute(1, [ 1 ] ) – case 4 above. ReadAttribute(1, [ Clusters.BasicInformation ] ) – case 5 above. ReadAttribute(1, [ (1, Clusters.BasicInformation.Attributes.Location ] ) – case 1 above.

An AttributePath can also be specified directly by [matter.cluster.Attribute.AttributePath(…)]

returnClusterObject: This returns the data as consolidated cluster objects, with all attributes for a cluster inside a single cluster-wide cluster object.

reportInterval: A tuple of two int-s for (MinIntervalFloor, MaxIntervalCeiling). Used by establishing subscriptions. When not provided, a read request will be sent. fabricFiltered: If True (default), the read/subscribe is fabric-filtered and will only see things associated with the fabric of the reader/subscriber. Relevant for attributes with fabric-scoped data. keepSubscriptions: Keep existing subscriptions. If set to False, existing subscriptions with this node will get cancelled and a new one gets setup. autoResubscribe: Automatically resubscribe to the subscription if subscription is lost. The automatic re-subscription only applies if the subscription establishes on first try. If the first subscription establishment attempt fails the function returns right away.

__Returns__ :

* subscription request: ClusterAttribute.SubscriptionTransaction To get notified on attribute change use SetAttributeUpdateCallback on the returned SubscriptionTransaction. This is used to set a callback function, which is a callable of type Callable[[TypedAttributePath, SubscriptionTransaction], None] Get the attribute value from the change path using GetAttribute on the SubscriptionTransaction You can await changes in the main loop using a trigger mechanism from the callback. ex. queue.SimpleQueue

* read request: AsyncReadTransaction.ReadResponse.attributes. This is of type AttributeCache.attributeCache (Attribute.py), which is a dict mapping endpoints to a list of Cluster (ClusterObjects.py) classes (dict[int, List[Cluster]]) Access as returned_object[endpoint_id][][] Ex. To access the OnTime attribute from the OnOff cluster on endpoint 1 returned_object[1][Clusters.OnOff][Clusters.OnOff.Attributes.OnTime]

__Raises__ :

* InteractionModelError (matter.interaction_model) on error

### ReadEvent

    async def ReadEvent(
            nodeId: int,
            events: typing.List[typing.Union[
                None,  # Empty tuple, all wildcard
                typing.Tuple[str, int],  # all wildcard with urgency set
                typing.Tuple[int, int],  # Endpoint,
                # Wildcard endpoint, Cluster id present
                typing.Tuple[typing.Type[ClusterObjects.Cluster], int],
                # Wildcard endpoint, Cluster + Event present
                typing.Tuple[typing.Type[ClusterObjects.ClusterEvent], int],
                # Wildcard event id
                typing.Tuple[int, typing.Type[ClusterObjects.Cluster], int],
                # Concrete path
                typing.Tuple[int, typing.Type[ClusterObjects.ClusterEvent], int]]],
            eventNumberFilter: typing.Optional[int] = None,
            fabricFiltered: bool = True,
            reportInterval: typing.Optional[typing.Tuple[int, int]] = None,
            keepSubscriptions: bool = False,
            autoResubscribe: bool = True,
            payloadCapability: int = TransportPayloadCapability.MRP_PAYLOAD)
    

Read a list of events from a target node, this is a wrapper of DeviceController.Read()

nodeId: Target’s Node ID events: A list of tuples of varying types depending on the type of read being requested: (endpoint, Clusters.ClusterA.EventA, urgent): Endpoint = specific, Cluster = specific, Event = specific, Urgent = True/False (endpoint, Clusters.ClusterA, urgent): Endpoint = specific, Cluster = specific, Event = *, Urgent = True/False (Clusters.ClusterA.EventA, urgent): Endpoint =*, Cluster = specific, Event = specific, Urgent = True/False endpoint: Endpoint = specific, Cluster = *, Event =*, Urgent = True/False Clusters.ClusterA: Endpoint = *, Cluster = specific, Event = _, Urgent = True/False ‘_ ’ or (): Endpoint =*, Cluster = *, Event =*, Urgent = True/False

The cluster and events specified above are to be selected from the generated cluster objects.

e.g. ReadEvent(1, [ 1 ] ) – case 4 above. ReadEvent(1, [ Clusters.BasicInformation ] ) – case 5 above. ReadEvent(1, [ (1, Clusters.BasicInformation.Events.Location ] ) – case 1 above.

eventNumberFilter: Optional minimum event number filter. reportInterval: A tuple of two int-s for (MinIntervalFloor, MaxIntervalCeiling). Used by establishing subscriptions. When not provided, a read request will be sent. keepSubscriptions: Keep existing subscriptions. If set to False, existing subscriptions with this node will get cancelled and a new one gets setup. autoResubscribe: Automatically resubscribe to the subscription if subscription is lost. The automatic re-subscription only applies if the subscription establishes on first try. If the first subscription establishment attempt fails the function returns right away.

__Returns__ :

* subscription request: ClusterAttribute.SubscriptionTransaction To get notified on event subscriptions, use the SetEventUpdateCallback function on the returned SubscriptionTransaction. This is a callable of type Callable[[EventReadResult, SubscriptionTransaction], None] You can await events using a trigger mechanism in the callback. ex. queue.SimpleQueue

* read request: AsyncReadTransaction.ReadResponse.events. This is a List[ClusterEvent].

__Raises__ :

* InteractionModelError (matter.interaction_model) on error

### SetIpk

    def SetIpk(ipk: bytes)
    

Sets the Identity Protection Key (IPK) for the device controller.

__Raises__ :

* `ChipStackError` \- On failure.

### InitGroupTestingData

    def InitGroupTestingData()
    

Populates the Device Controller’s GroupDataProvider with known test group info and keys.

__Raises__ :

* `ChipStackError` \- On failure.

### CreateManualCode

    def CreateManualCode(discriminator: int, passcode: int) -> str
    

Creates a standard flow manual code from the given discriminator and passcode.

__Arguments__ :

* `discriminator` _int_ \- The long discriminator for the DNS-SD advertisement. Valid range: 0-4095.

* `passcode` _int_ \- The setup passcode of the device.

__Returns__ :

* `str` \- The decoded string from the buffer.

__Raises__ :

* `MemoryError` \- If the output size is invalid during manual code creation.

## ChipDeviceController

    class ChipDeviceController(ChipDeviceControllerBase)
    

The ChipDeviceCommissioner binding, named as ChipDeviceController

### Commission

    async def Commission(nodeId: int) -> int
    

Start the auto-commissioning process on a node after establishing a PASE connection. This function is intended to be used in conjunction with one of the EstablishPASESession functions. It can be called either before or after the DevicePairingDelegate receives the OnPairingComplete call. Commissioners that want to perform simple auto-commissioning should use the supplied “CommissionWithCode” function, which will establish the PASE connection and commission automatically.

__Arguments__ :

* `nodeId` _int_ \- The node ID of the device.

__Raises__ :

A ChipStackError on failure.

__Returns__ :

* `int` \- Effective Node ID of the device (as defined by the assigned NOC).

### CommissionBleThread

    async def CommissionBleThread(discriminator,
                                  setupPinCode,
                                  nodeId: int,
                                  threadOperationalDataset: bytes,
                                  isShortDiscriminator: bool = False) -> int
    

Commissions a Thread device over BLE.

__Arguments__ :

* `discriminator` _int_ \- The long discriminator for the DNS-SD advertisement. Valid range: 0-4095.

* `setupPinCode` _int_ \- The setup pin code of the device.

* `nodeId` _int_ \- The node ID of the device.

* `threadOperationalDataset` _bytes_ \- The Thread operational dataset for commissioning.

* `isShortDiscriminator` _bool_ \- Short discriminator.

__Returns__ :

* `int` \- Effective Node ID of the device (as defined by the assigned NOC).

### CommissionNfcThread

    async def CommissionNfcThread(discriminator, setupPinCode, nodeId: int,
                                  threadOperationalDataset: bytes) -> int
    

Commissions a Thread device over NFC.

__Arguments__ :

* `discriminator` _int_ \- The long discriminator for the DNS-SD advertisement. Valid range: 0-4095.

* `setupPinCode` _int_ \- The setup pin code of the device.

* `nodeId` _int_ \- The node ID of the device.

* `threadOperationalDataset` _bytes_ \- The Thread operational dataset for commissioning.

__Returns__ :

* `int` \- Effective Node ID of the device (as defined by the assigned NOC).

### CommissionNfcWiFi

    async def CommissionNfcWiFi(discriminator, setupPinCode, nodeId: int,
                                ssid: str, credentials: str) -> int
    

Commissions a Wi-Fi device over NFC.

__Arguments__ :

* `discriminator` _int_ \- The long discriminator for the DNS-SD advertisement. Valid range: 0-4095.

* `setupPinCode` _int_ \- The setup pin code of the device.

* `nodeId` _int_ \- The node ID of the device.

* `ssid` _str_ \- SSID of the WiFi network.

* `credentials` _str_ \- WiFi network password.

__Returns__ :

* `int` \- Effective Node ID of the device (as defined by the assigned NOC).

### CommissionBleWiFi

    async def CommissionBleWiFi(discriminator,
                                setupPinCode,
                                nodeId: int,
                                ssid: str,
                                credentials: str,
                                isShortDiscriminator: bool = False) -> int
    

Commissions a Wi-Fi device over BLE.

__Arguments__ :

* `discriminator` _int_ \- The long discriminator for the DNS-SD advertisement. Valid range: 0-4095.

* `setupPinCode` _int_ \- The setup pin code of the device.

* `nodeId` _int_ \- The node ID of the device.

* `ssid` _str_ \- SSID of the WiFi network.

* `credentials` _str_ \- WiFi network password.

* `isShortDiscriminator` _bool_ \- Short discriminator.

__Returns__ :

* `int` \- Effective Node ID of the device (as defined by the assigned NOC).

### SetWiFiCredentials

    def SetWiFiCredentials(ssid: str, credentials: str)
    

Set the Wi-Fi credentials to set during commissioning.

__Arguments__ :

* `ssid` _str_ \- SSID of the WiFi network.

* `credentials` _str_ \- WiFi network password.

__Raises__ :

* `ChipStackError` \- On failure.

### SetThreadOperationalDataset

    def SetThreadOperationalDataset(threadOperationalDataset)
    

Set the Thread operational dataset to set during commissioning.

__Arguments__ :

* `threadOperationalDataset` _bytes_ \- The Thread operational dataset for commissioning.

__Raises__ :

* `ChipStackError` \- On failure.

### ResetCommissioningParameters

    def ResetCommissioningParameters()
    

Sets the commissioning parameters back to the default values.

__Raises__ :

* `ChipStackError` \- On failure.

### SetTimeZone

    def SetTimeZone(offset: int, validAt: int, name: str = "")
    

Set the time zone to set during commissioning. Currently only one time zone entry is supported.

__Arguments__ :

* `offset` _int_ \- Timezone offset.

* `validAt` _int_ \- Timestamp of the timezone.

* `name` _str_ \- Name or label of the timezone.

__Raises__ :

* `ChipStackError` \- On failure.

### SetDSTOffset

    def SetDSTOffset(offset: int, validStarting: int, validUntil: int)
    

Set the DST offset to set during commissioning. Currently only one DST entry is supported.

__Arguments__ :

* `offset` _int_ \- Timezone offset.

* `validStarting` _int_ \- The start timestamp.

* `validUntil` _int_ \- The end timestamp

__Raises__ :

* `ChipStackError` \- On failure.

### SetTCAcknowledgements

    def SetTCAcknowledgements(tcAcceptedVersion: int, tcUserResponse: int)
    

Set the TC acknowledgements to set during commissioning.

__Arguments__ :

* `tcAcceptedVersion` _int_ \- TC accepted version.

* `tcUserResponse` _int_ \- TC user responde.

__Raises__ :

* `ChipStackError` \- On failure.

### SetSkipCommissioningComplete

    def SetSkipCommissioningComplete(skipCommissioningComplete: bool)
    

Set whether to skip the commissioning complete callback.

__Arguments__ :

* `skipCommissioningComplete` _bool_ \- The value skip the commissioning complete.

__Raises__ :

* `ChipStackError` \- On failure.

### SetDefaultNTP

    def SetDefaultNTP(defaultNTP: str)
    

Set the DefaultNTP to set during commissioning.

__Arguments__ :

* `defaultNTP` _str_ \- The default NTP.

__Raises__ :

* `ChipStackError` \- On failure.

### SetTrustedTimeSource

    def SetTrustedTimeSource(nodeId: int, endpoint: int)
    

Set the trusted time source nodeId to set during commissioning. This must be a node on the commissioner fabric.

__Arguments__ :

* `nodeId` _int_ \- The node ID of the device.

* `endpoint` _int_ \- endpoint of the device.

__Raises__ :

* `ChipStackError` \- On failure.

### SetCheckMatchingFabric

    def SetCheckMatchingFabric(check: bool)
    

Instructs the auto-commissioner to perform a matching fabric check before commissioning.

__Arguments__ :

* `check` _bool_ \- Validation fabric before commissioning.

__Raises__ :

* `ChipStackError` \- On failure.

### GenerateICDRegistrationParameters

    def GenerateICDRegistrationParameters()
    

Generates ICD registration parameters for this controller.

__Returns__ :

* `ICDRegistrationParameters` \- An object containing the generated parameters including symmetricKey, checkInNodeId, monitoredSubject, stayActiveMs, and clientType.

### EnableICDRegistration

    def EnableICDRegistration(parameters: ICDRegistrationParameters)
    

Enables ICD registration for the following commissioning session.

__Arguments__ :

* `parameters` \- A ICDRegistrationParameters for the parameters used for ICD registration, or None for default arguments.

__Raises__ :

* `ChipStackError` \- On failure.

### DisableICDRegistration

    def DisableICDRegistration()
    

Disables ICD registration.

__Raises__ :

* `ChipStackError` \- On failure.

### GetFabricCheckResult

    def GetFabricCheckResult() -> int
    

Returns the fabric check result if SetCheckMatchingFabric was used.

__Returns__ :

* `int` \- The fabric check result, or `-1` if no check was performed.

### CommissionOnNetwork

    async def CommissionOnNetwork(
            nodeId: int,
            setupPinCode: int,
            filterType: DiscoveryFilterType = DiscoveryFilterType.NONE,
            filter: typing.Any = None,
            discoveryTimeoutMsec: int = 30000) -> int
    

Does the routine for OnNetworkCommissioning, with a filter for mDNS discovery. Supported filters are:

DiscoveryFilterType.NONE DiscoveryFilterType.SHORT_DISCRIMINATOR DiscoveryFilterType.LONG_DISCRIMINATOR DiscoveryFilterType.VENDOR_ID DiscoveryFilterType.DEVICE_TYPE DiscoveryFilterType.COMMISSIONING_MODE DiscoveryFilterType.INSTANCE_NAME DiscoveryFilterType.COMMISSIONER DiscoveryFilterType.COMPRESSED_FABRIC_ID

The filter can be an integer, a string or None depending on the actual type of selected filter.

__Raises__ :

* `ChipStackError` \- On failure.

__Returns__ :

* Effective Node ID of the device (as defined by the assigned NOC)

### CommissionThreadMeshcop

    async def CommissionThreadMeshcop(nodeId: int, setupPinCode: int,
                                      discriminator: int, borderAgentIPAddr: str,
                                      borderAgentPort: int,
                                      threadOperationalDataset: bytes) -> int
    

Commission with the given node ID from the setupPinCode and discriminator over Thread MeshCoP transport

__Arguments__ :

* `nodeId` _int_ \- The node ID of the device.

* `setupPinCode` _int_ \- The setup pin code of the device.

* `discriminator` _int_ \- The long discriminator for the DNS-SD advertisement. Valid range: 0-4095.

* `borderAgentIPAddr` _str_ \- IP address of Border Agent in Thread network

* `borderAgentPort` _int_ \- The port of Border Agent in Thread network

* `threadOperationalDataset` _bytes_ \- The operational dataset of Thread network

### get_rcac

    def get_rcac()
    

Passes captured RCAC data back to Python test modules for validation

* Setting buffer size to max size mentioned in spec:

* Ref: https://github.com/CHIP-Specifications/connectedhomeip-spec/blob/06c4d55962954546ecf093c221fe1dab57645028/policies/matter_certificate_policy.adoc#615-key-sizes

__Returns__ :

* `bytes` \- A bytes sentence representing the RCAC, or None if no data.

### CommissionWithCode

    async def CommissionWithCode(
            setupPayload: str,
            nodeId: int,
            discoveryType: DiscoveryType = DiscoveryType.DISCOVERY_ALL) -> int
    

Commission with the given node ID from the setupPayload. setupPayload may be a QR or manual code.

__Arguments__ :

* `setupPayload` _str_ \- The setup payload (QR or manual code).

* `nodeId` _int_ \- The node ID of the device.

* `discoveryType` _DiscoveryType.DISCOVERY_ALL_ \- The discovery type to use.

__Raises__ :

* `ChipStackError` \- On failure.

__Returns__ :

* `int` \- Effective Node ID of the device (as defined by the assigned NOC)

### NOCChainCallback

    def NOCChainCallback(nocChain)
    

Callback function for handling the NOC chain result.

__Arguments__ :

* `nocChain` _nocChain_ \- The object NOC chain data received.

__Returns__ :

None

### IssueNOCChain

    async def IssueNOCChain(
            csr: Clusters.OperationalCredentials.Commands.CSRResponse,
            nodeId: int)
    

Issue an NOC chain using the associated OperationalCredentialsDelegate. The NOC chain will be provided in TLV cert format.

__Arguments__ :

* `crs` _cluster_ \- Certificate Signing Request response

* `nodeId` _int_ \- The node ID of the device.

__Returns__ :

* `asyncio.Future` \- A future object that is the result of the NOC Chain operation.

### SetDACRevocationSetPath

    def SetDACRevocationSetPath(dacRevocationSetPath: typing.Optional[str])
    

Set the path to the device attestation revocation set JSON file.

__Arguments__ :

* `dacRevocationSetPath` _Optional[str]_ \- Path to the JSON file containing the device attestation revocation set.

__Raises__ :

* `ChipStackError` \- On failure.

## BareChipDeviceController

    class BareChipDeviceController(ChipDeviceControllerBase)
    

A bare device controller without AutoCommissioner support.

### __init__

    def __init__(operationalKey: p256keypair.P256Keypair,
                 noc: bytes,
                 icac: typing.Union[bytes, None],
                 rcac: bytes,
                 ipk: typing.Union[bytes, None],
                 adminVendorId: int,
                 name: typing.Optional[str] = None)
    

Creates a controller without AutoCommissioner.

The allocated controller uses the noc, icac, rcac and ipk instead of the default, random generated certificates / keys. Which is suitable for creating a controller for manually signing certificates for testing.

__Arguments__ :

* `operationalKey` \- A P256Keypair object for the operational key of the controller.

* `noc` _bytes_ \- The NOC for the controller, in bytes.

* `icac` _Optional[bytes]_ \- The optional ICAC for the controller.

* `rcac` _bytes_ \- The RCAC for the controller.

* `ipk` _Optional[bytes]_ \- The optional IPK for the controller, when None is provided, the defaultIpk will be used.

* `adminVendorId` _int_ \- The adminVendorId of the controller.

* `name` _str_ \- The name of the controller, for debugging use only.

__Raises__ :

* `ChipStackError` \- On failure
