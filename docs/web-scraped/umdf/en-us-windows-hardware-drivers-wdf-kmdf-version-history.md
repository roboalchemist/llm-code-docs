# Source: https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/kmdf-version-history

Title: KMDF Version History - Windows drivers

URL Source: https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/kmdf-version-history

Markdown Content:
This topic lists versions of Kernel-Mode Driver Framework (KMDF), the corresponding versions of the Windows operating system, and the changes made in each release.

The following table shows the release history of the KMDF library. You can use the **In this article** sidebar on the right to navigate quickly to a specific version.

| KMDF version | Initial release | Included in | Drivers using this KMDF version run on |
| --- | --- | --- | --- |
| 1.33 | Windows 11, version 21H2 WDK; WDK for Windows Server 2022 | Windows 11, version 24H2; Windows 11, version 23H2; Windows 11, version 22H2; Windows 11, version 21H2; Windows Server 2022 | Windows 11, version 21H2 and later; Windows Server 2022 and later |
| 1.31 | Windows 10, version 2004 WDK | Windows 10, version 2004 | Windows 10, version 2004 and later |
| 1.29 | Not released in WDK | Windows 10, version 1903 | Windows 10, version 1903 and later |
| 1.27 | Windows 10, version 1809 WDK | Windows 10, version 1809 | Windows 10, version 1809 and later |
| 1.25 | Windows 10, version 1803 WDK | Windows 10, version 1803 | Windows 10, version 1803 and later |
| 1.23 | Windows 10, version 1709 WDK | Windows 10, version 1709 | Windows 10, version 1709 and later |
| 1.21 | Windows 10, version 1703 WDK | Windows 10, version 1703 | Windows 10, version 1703 and later |
| 1.19 | Windows 10, version 1607 WDK | Windows 10, version 1607 | Windows 10 version 1607, Windows Server 2016 and later |
| 1.17 | Windows 10, version 1511 WDK | Windows 10, version 1511 | Windows 10 version 1511, Windows Server 2016 and later |
| 1.15 | Windows 10 WDK | Windows 10, version 1507 | Windows 10, version 1507, Windows Server 2016 and later |
| 1.13 | Windows 8.1 WDK | Windows 8.1 | Windows 8.1 and later |
| 1.11 | Windows 8 WDK | Windows 8 | Windows Vista and later |
| 1.9 | Windows 7 WDK | Windows 7 | Windows XP and later |
| 1.7 | Windows Server 2008 WDK | Windows Vista with Service Pack 1 (SP1); Windows Server 2008 | Windows 2000 and later |
| 1.5 | Windows Vista WDK | Windows Vista | Windows 2000 and later |
| 1.1 | Download only | None | Windows 2000 and later |
| 1.0 | Download only | None | Windows XP and later |

You can use the Windows Driver Kit (WDK)with Microsoft Visual Studio 2022 to build drivers that run on Windows 10 and later.

For help determining what version of WDF to use, see [Which framework version should I use?](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/building-and-loading-a-kmdf-driver#which-framework-version-should-i-use).

For a complete list of callbacks and methods, and which frameworks and versions they apply to, see [Summary of WDF Callbacks and Methods](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/_wdf/).

For information about the new features for KMDF drivers in Windows 10, see [What's New for WDF Drivers](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/).

For each KMDF version section below, the Windows version in which it was released is listed in parentheses.

* For devices that specify **SystemManagedIdleTimeout** or **SystemManagedIdleTimeoutWithHint** in the [WDF_POWER_POLICY_IDLE_TIMEOUT_TYPE](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/ne-wdfdevice-_wdf_power_policy_idle_timeout_type) enumeration, when calling the [**WdfDeviceStopIdle**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicestopidle) macro with _WaitForD0_ set to **FALSE**, if the device is still in D0 and the idle timeout period has not yet elapsed, **WdfDeviceStopIdle** returns STATUS_SUCCESS (in previous versions this resulted in a return value of STATUS_PENDING).
* [**WDF_POWER_FRAMEWORK_SETTINGS**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_power_framework_settings) structure has two new members (**PoFxDeviceFlags** and **DirectedPoFxEnabled**).

* Added new API [**WdfDeviceSetDeviceInterfaceStateEx**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetdeviceinterfacestateex)
* Improved existing API [**WdfDeviceGetSystemPowerAction**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicegetsystempoweraction)
* Added new API [**WdfPdoInitRemovePowerDependencyOnParent**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoinitremovepowerdependencyonparent)
* [Introduction to the Directed Power Management Framework](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/introduction-to-the-directed-power-management-framework)

Unchanged from version 1.25.

Unchanged from version 1.25.

* [Building a WDF driver for multiple versions of Windows](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/building-a-wdf-driver-for-multiple-versions-of-windows).

* Companion functionality added for internal use only. For more info, see [Wdfcompanion.h](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfcompanion/).

* [**WdfFileObjectGetInitiatorProcessId**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdffileobject/nf-wdffileobject-wdffileobjectgetinitiatorprocessid) was previously UMDF-only, now available in KMDF.
* [**WdfRequestGetRequestorProcessId**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestgetrequestorprocessid) was previously UMDF-only, now available in KMDF.
* [**WdfObjectDereferenceActual**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdereferenceactual): Type of _File_ parameter changed from PCHAR to PCCH.
* [**WdfObjectReferenceActual**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectreferenceactual): Type of _File_ parameter changed from PCHAR to PCCH.
* Added WDF registry values **ObjectLeakDetectionLimit** and **ObjectsForLeakDetection** for debugging excessive object creation. For more info, see [Registry Values for Debugging WDF Drivers](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/registry-values-for-debugging-kmdf-drivers).
* The SleepStudy software tool reports the number of power references that a KMDF driver has that are preventing the system from going to sleep. For more info, see [Modern standby SleepStudy](https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/modern-standby-sleepstudy).

* Added [**WdfDmaTransactionSetSingleTransferRequirement**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionsetsingletransferrequirement)
* Added **WDF_DMA_ENABLER_CONFIG_REQUIRE_SINGLE_TRANSFER** flag in [**WDF_DMA_ENABLER_CONFIG_FLAGS**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdmaenabler/ne-wdfdmaenabler-_wdf_dma_enabler_config_flags)
* Added **STATUS_WDF_TOO_MANY_TRANSFERS** return value for [**WdfDmaTransactionInitialize**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioninitialize) and [**WdfDmaTransactionDmaCompleted**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactiondmacompleted)
* Added output messages for single transfer output to [**!wdfkd.wdfdmatransaction**](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/-wdfkd-wdfdmatransaction) and [**!wdfkd.wdfdmaenabler**](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/-wdfkd-wdfdmaenabler)
* For more info about single transfer DMA, see [Using Single Transfer DMA](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/using-single-transfer-dma).

* The new [**WdfDeviceOpenDevicemapKey**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceopendevicemapkey) method allows a driver to access subkeys and values under **HKEY_LOCAL_MACHINE\HARDWARE\DEVICEMAP**.
* WDF source code is publicly available from [Windows Driver Frameworks](https://github.com/Microsoft/Windows-Driver-Frameworks). The private symbol files for WDF are available through the Microsoft Symbol Server. Also see [Debugging with WDF Source](https://github.com/Microsoft/Windows-Driver-Frameworks/wiki/Debugging-with-WDF-Source) and [Video: Debugging your driver with WDF source code](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/video--debugging-your-driver-with-wdf-source-code).
* Inflight Trace Recorder (IFR) now available. Note this is separate from the [framework's event logger](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/using-the-framework-s-event-logger). For more info, see [Inflight Trace Recorder (IFR) for logging traces](https://learn.microsoft.com/en-us/windows-hardware/drivers/devtest/using-wpp-recorder) and [Using Inflight Trace Recorder in KMDF and UMDF Drivers](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/using-wpp-software-tracing-in-kmdf-and-umdf-2-drivers).
* Support for interrupts for GPIO-backed devices. For more information, see [Creating an Interrupt Object](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/creating-an-interrupt-object).

KMDF version 1.13 adds the following functionality:

* Added **CanWakeDevice** member to [**WDF_INTERRUPT_CONFIG**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfinterrupt/ns-wdfinterrupt-_wdf_interrupt_config) structure to support interrupts that can be used to bring a device from a low-power Dx state back to its fully on D0 state. For more information, see [Using an Interrupt to Wake a Device](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/using-an-interrupt-to-wake-a-device).
* Support for high resolution timers. For more information, see [Using Timers](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/using-timers).
* Support for timers that do not wake the system if they expire when the system is in a low-power state. For more information, see [Using Timers](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/using-timers).
* The following KMDF/UMDF methods described in [Accessing the Unified Device Property Model](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/accessing-the-unified-device-property-model):
  * [**WdfDeviceAllocAndQueryPropertyEx**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceallocandquerypropertyex)
  * [**WdfDeviceAssignProperty**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassignproperty)
  * [**WdfDeviceInitSetIoTypeEx**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetiotypeex)
  * [**WdfDeviceQueryPropertyEx**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicequerypropertyex)
  * [**WdfFdoInitAllocAndQueryPropertyEx**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitallocandquerypropertyex)
  * [**WdfFdoInitQueryPropertyEx**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitquerypropertyex)

For information about UMDF versions, see [UMDF Version History](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/umdf-version-history).

Version 1.11 adds the following functionality:

* [System-mode DMA](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/supporting-system-mode-dma)

* Support for [passive-level interrupts](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/supporting-passive-level-interrupts)

* [Functional power states](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/supporting-functional-power-states) for multiple components within a single device

* [Dispatching IRPs to I/O Queues](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/dispatching-irps-to-i-o-queues)

* The following methods:

  * [**WdfDeviceConfigureWdmIrpDispatchCallback**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceconfigurewdmirpdispatchcallback)
  * [**WdfDeviceInitSetReleaseHardwareOrderOnFailure**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetreleasehardwareorderonfailure)
  * [**WdfDeviceInitSetRemoveLockOptions**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetremovelockoptions)
  * [**WdfDeviceWdmDispatchIrp**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmdispatchirp)
  * [**WdfDmaEnablerConfigureSystemProfile**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdmaenabler/nf-wdfdmaenabler-wdfdmaenablerconfiguresystemprofile)
  * [**WdfDmaTransactionAllocateResources**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionallocateresources)
  * [**WdfDmaTransactionCancel**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioncancel)
  * [**WdfDmaTransactionFreeResources**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionfreeresources)
  * [**WdfDmaTransactionGetTransferInfo**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactiongettransferinfo)
  * [**WdfDmaTransactionInitializeUsingOffset**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactioninitializeusingoffset)
  * [**WdfDmaTransactionSetChannelConfigurationCallback**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionsetchannelconfigurationcallback)
  * [**WdfDmaTransactionSetDeviceAddressOffset**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionsetdeviceaddressoffset)
  * [**WdfDmaTransactionSetImmediateExecution**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionsetimmediateexecution)
  * [**WdfDmaTransactionSetTransferCompleteCallback**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionsettransfercompletecallback)
  * [**WdfDmaTransactionWdmGetTransferContext**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdmatransaction/nf-wdfdmatransaction-wdfdmatransactionwdmgettransfercontext)
  * [**WdfInterruptQueueWorkItemForIsr**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptqueueworkitemforisr)
  * [**WdfInterruptReportActive**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptreportactive)
  * [**WdfInterruptReportInactive**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptreportinactive)
  * [**WdfInterruptTryToAcquireLock**](https://learn.microsoft.com/en-us/previous-versions/hh439284(v=vs.85))
  * [**WdfIoQueueStopAndPurge**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestopandpurge)
  * [**WdfIoQueueStopAndPurgeSynchronously**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestopandpurgesynchronously)
  * [**WdfIoTargetPurge**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetpurge)
  * [**WdfUsbTargetDeviceCreateIsochUrb**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreateisochurb)
  * [**WdfUsbTargetDeviceCreateUrb**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreateurb)
  * [**WdfUsbTargetDeviceCreateWithParameters**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreatewithparameters)
  * [**WdfUsbTargetDeviceQueryUsbCapability**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicequeryusbcapability)

* Added [_EvtDeviceUsageNotificationEx_](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_usage_notification_ex).

* Added **IdleTimeoutType** and **ExcludeD3Cold** members to [**WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_device_power_policy_idle_settings).

* Added **ReportInactiveOnPowerDown** member to [**WDF_INTERRUPT_CONFIG**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfinterrupt/ns-wdfinterrupt-_wdf_interrupt_config).

* Added **WdfIoTargetPurged** value to [**WDF_IO_TARGET_STATE**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfiotarget/ne-wdfiotarget-_wdf_io_target_state).

* Added **WdfSpecialFileBoot** value to [**WDF_SPECIAL_FILE_TYPE**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/ne-wdfdevice-_wdf_special_file_type).

* Added **DbgWaitForSignalTimeoutInSec** to [Registry Values for Debugging Framework-based Drivers](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/registry-values-for-debugging-kmdf-drivers).

* Added [InstallWdf](https://learn.microsoft.com/en-us/samples/browse/), [MultiComp](https://learn.microsoft.com/en-us/samples/browse/), and [SingleComp](https://learn.microsoft.com/en-us/samples/browse/) samples.

Version 1.9 adds the following functionality:

* [Guaranteed forward progress](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/guaranteeing-forward-progress-of-i-o-operations) for I/O queues

* Support for [requeuing I/O requests](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/requeuing-i-o-requests) from a child device's I/O queue to a parent device's I/O queue

* Ability to specify [queue-level synchronization](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfobject/ne-wdfobject-_wdf_synchronization_scope) for individual queue objects.

* The following methods:

  * [**WdfDeviceGetSystemPowerAction**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicegetsystempoweraction)
  * [**WdfDeviceRemoveDependentUsageDeviceObject**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceremovedependentusagedeviceobject)
  * [**WdfInterruptSetExtendedPolicy**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptsetextendedpolicy)
  * [**WdfPdoInitAllowForwardingRequestToParent**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoinitallowforwardingrequesttoparent)
  * [**WdfPdoInitAssignContainerID**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoinitassigncontainerid)
  * [**WdfPreDeviceInstallEx**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfinstaller/nf-wdfinstaller-wdfpredeviceinstallex)
  * [**WdfRequestForwardToParentDeviceIoQueue**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestforwardtoparentdeviceioqueue)
  * [**WdfRequestMarkCancelableEx**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelableex)

* Added the **NumberOfPresentedRequests** member to the [**WDF_IO_QUEUE_CONFIG**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfio/ns-wdfio-_wdf_io_queue_config) structure so drivers can limit the number of I/O requests that the framework delivers to the driver from a parallel I/O queue.

* Added the **WdfFileObjectCanBeOptional** flag to the [**WDF_FILEOBJECT_CLASS**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/ne-wdfdevice-_wdf_fileobject_class) structure.

* Added the **TolerableDelay** member to the [**WDF_TIMER_CONFIG**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdftimer/ns-wdftimer-_wdf_timer_config) structure.

* Added [WdfDefaultIdleInWorkingState and WdfDefaultWakeFromSleepState](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/user-control-of-device-idle-and-wake-behavior) registry values.

* The [**WdfDeviceEnqueueRequest**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceenqueuerequest) method can be called at IRQL<=DISPATCH_LEVEL.

* The [**WdfWorkItemEnqueue**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfworkitem/nf-wdfworkitem-wdfworkitemenqueue) method can be called if the specified work item is already on the work-item queue.

* Added the [_EvtDeviceArmWakeFromSxWithReason_](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_arm_wake_from_sx_with_reason) event callback function.

* Added **ArmForWakeIfChildrenAreArmedForWake** and **IndicateChildWakeOnParentWake** members to the [**WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_device_power_policy_wake_settings) structure.

* [**WdfUsbInterfaceGetNumSettings**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbinterfacegetnumsettings)

* Added the **DriverPoolTag** member to [**WDF_DRIVER_CONFIG**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdriver/ns-wdfdriver-_wdf_driver_config).

* The following methods:
  * [**WdfCommonBufferCreateWithConfig**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfcommonbuffer/nf-wdfcommonbuffer-wdfcommonbuffercreatewithconfig)
  * [**WdfDmaEnablerGetFragmentLength**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdmaenabler/nf-wdfdmaenabler-wdfdmaenablergetfragmentlength)
  * [**WdfDmaEnablerWdmGetDmaAdapter**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdmaenabler/nf-wdfdmaenabler-wdfdmaenablerwdmgetdmaadapter)

Initial release.
