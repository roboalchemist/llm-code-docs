# Source: https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/umdf-version-history

Title: UMDF Version History - Windows drivers

URL Source: https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/umdf-version-history

Published Time: Fri, 18 Jul 2025 05:07:10 GMT

Markdown Content:
This topic lists versions of User-Mode Driver Framework (UMDF), the corresponding versions of the Windows operating system, and the changes made in each release.

The following table shows the release history of the UMDF library. You can use the **In this article** sidebar on the right to navigate quickly to a specific version.

| UMDF version | Initial release | Included in | Drivers using this UMDF version run on |
| --- | --- | --- | --- |
| 2.33 | Windows 11, version 21H2 WDK; WDK for Windows Server 2022 | Windows 11, version 24H2; Windows 11, version 23H2; Windows 11, version 22H2; Windows 11, version 21H2; Windows Server 2022 | Windows 11, version 21H2 and later; Windows Server 2022 and later |
| 2.31 | Windows 10, version 2004 WDK | Windows 10, version 2004 (May 2020 Update, Vibranium) | Windows 10, version 2004 and later |
| 2.29 | Not released in WDK | Windows 10, version 1903 (March 2019 Update, 19H1) | Windows 10, version 1903 and later |
| 2.27 | Windows 10, version 1809 WDK | Windows 10, version 1809 (October 2018 Update, Redstone 5) | Windows 10, version 1809 and later |
| 2.25 | Windows 10, version 1803 WDK | Windows 10, version 1803 (April 2018 Update, Redstone 4) | Windows 10, version 1803 and later |
| 2.23 | Windows 10, version 1709 WDK | Windows 10, version 1709 (Fall Creators Update, Redstone 3) | Windows 10, version 1709 and later |
| 2.21 | Windows 10, version 1703 WDK | Windows 10, version 1703 (Creators Update, Redstone 2) | Windows 10, version 1703 and later |
| 2.19 | Windows 10, version 1607 WDK | Windows 10, version 1607 (Anniversary Update, Redstone 1) | Windows 10, version 1607, Windows Server 2016 and later |
| 2.17 | Windows 10, version 1511 WDK | Windows 10, version 1511 (November Update, Threshold 2) | Windows 10, version 1511, Windows Server 2016 and later |
| 2.15 | Windows 10 WDK | Windows 10, version 1507 (Threshold 1) | Windows 10, version 1507, Windows Server 2016 and later |
| 2.0 | Windows Driver Kit (WDK)8.1 | Windows 8.1 | Windows 8.1 and later |
| 1.11 | Windows Driver Kit (WDK)8 | Windows 8 | Windows Vista and later |
| 1.9 | Windows 7 WDK | Windows 7 | Windows XP and later |
| 1.7 | Windows Server 2008 WDK | Windows Vista with Service Pack 1 (SP1), Windows Server 2008 | Windows XP and later |
| 1.5 | Windows Vista WDK | Windows Vista | Windows XP and later |

You can use the Windows Driver Kit (WDK) with Microsoft Visual Studio 2022 to build drivers that run on Windows 10 and later.

For help determining what version of WDF to use, see [Which framework version should I use?](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/building-and-loading-a-kmdf-driver#which-framework-version-should-i-use).

For information about the new features for UMDF drivers in Windows 10, see [What's New for WDF Drivers](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/).

For each UMDF version section below, the Windows version in which it was released is listed in parentheses.

* For devices that specify **SystemManagedIdleTimeout** or **SystemManagedIdleTimeoutWithHint** in the [WDF_POWER_POLICY_IDLE_TIMEOUT_TYPE](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/ne-wdfdevice-_wdf_power_policy_idle_timeout_type) enumeration, when calling the [**WdfDeviceStopIdle**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicestopidle) macro with _WaitForD0_ set to **FALSE**, if the device is still in D0 and the idle timeout period has not yet elapsed, **WdfDeviceStopIdle** returns STATUS_SUCCESS (in previous versions this resulted in a return value of STATUS_PENDING).
* [**WdfDeviceWdmAssignPowerFrameworkSettings**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmassignpowerframeworksettings) function now supports UMDF.
* [**WDF_POWER_FRAMEWORK_SETTINGS**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_power_framework_settings) structure has two new members (**PoFxDeviceFlags** and **DirectedPoFxEnabled**) and can now be used with UMDF. For UMDF, only the **Size**, **PoFxDeviceFlags**, and **DirectedPoFxEnabled** members are used. Other fields are ignored and must be set to zero. The framework does this automatically when a UMDF driver calls the [**WDF_POWER_FRAMEWORK_SETTINGS_INIT**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdf_power_framework_settings_init) function.

* Added new API [**WdfDeviceSetDeviceInterfaceStateEx**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetdeviceinterfacestateex)
* Improved existing API [**WdfDeviceGetSystemPowerAction**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicegetsystempoweraction)
* Added per-driver **HostProcessDbgBreakOnDriverLoad** registry value. For info, see [Registry Values for Debugging WDF Drivers](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/registry-values-for-debugging-kmdf-drivers).
* [Introduction to the Directed Power Management Framework](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/introduction-to-the-directed-power-management-framework)

Unchanged from version 2.27.

* Added new API [**WdfDriverRetrieveDriverDataDirectoryString**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdriverretrievedriverdatadirectorystring)

* [**WdfDeviceRetrieveDeviceDirectoryString**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceretrievedevicedirectorystring)
* [Building a WDF driver for multiple versions of Windows](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/building-a-wdf-driver-for-multiple-versions-of-windows).

* Companion functionality added for internal use only. For the new DDIs, see [Summary of WDF Callbacks and Methods](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/_wdf/).

* [**WdfObjectDereferenceActual**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdereferenceactual): Type of _File_ parameter changed from PCHAR to PCCH.
* [**WdfObjectReferenceActual**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectreferenceactual): Type of _File_ parameter changed from PCHAR to PCCH.
* Added WDF registry values **ObjectLeakDetectionLimit** and **ObjectsForLeakDetection** for debugging excessive object creation. For more info, see [Registry Values for Debugging WDF Drivers](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/registry-values-for-debugging-kmdf-drivers).

There are no changes or additions for UMDF Version 2.19.

This version adds UMDF support for the following existing interfaces:

* [**WdfDeviceConfigureWdmIrpDispatchCallback**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceconfigurewdmirpdispatchcallback)
* [_EvtDeviceWdmIrpDispatch_](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_dispatch)
* [**WdfDeviceWdmDispatchIrp**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmdispatchirp)
* [**WdfDeviceWdmDispatchIrpToIoQueue**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmdispatchirptoioqueue)

For more information, see [Dispatching IRPs to I/O Queues](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/dispatching-irps-to-i-o-queues).

* The new [**WdfDeviceOpenDevicemapKey**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceopendevicemapkey) method allows a driver to access subkeys and values under **HKEY_LOCAL_MACHINE\HARDWARE\DEVICEMAP**.
* A UMDF driver can call [**WdfIoTargetWdmGetTargetFileHandle**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetwdmgettargetfilehandle) to obtain a file handle to the next-lower kernel-mode driver in its stack. The driver can write data to that handle, bypassing the framework's abstractions for sending I/O to the local I/O target.
* A UMDF driver can request that the underlying bus driver re-enumerate it. See [**WdfDeviceSetFailed**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetfailed).
* Setting the **UmdfDirectHardwareAccess** directive is no longer always necessary for devices that have connection resources. See [Specifying WDF Directives in INF Files](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/specifying-wdf-directives-in-inf-files).
* WDF source code is publicly available from [Windows Driver Frameworks](https://github.com/Microsoft/Windows-Driver-Frameworks). The private symbol files for WDF are available through the Microsoft Symbol Server. Also see [Debugging with WDF Source](https://github.com/Microsoft/Windows-Driver-Frameworks/wiki/Debugging-with-WDF-Source) and [Video: Debugging your driver with WDF source code](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/video--debugging-your-driver-with-wdf-source-code).
* Inflight Trace Recorder (IFR) now available. Note this is separate from the [framework's event logger](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/using-the-framework-s-event-logger). For more info, see [Inflight Trace Recorder (IFR) for logging traces](https://learn.microsoft.com/en-us/windows-hardware/drivers/devtest/using-wpp-recorder) and [Using Inflight Trace Recorder in KMDF and UMDF Drivers](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/using-wpp-software-tracing-in-kmdf-and-umdf-2-drivers).
* Support for interrupts for GPIO-backed devices. For more information, see [Creating an Interrupt Object](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/creating-an-interrupt-object).

In addition to the shared functionality described in [Getting Started with UMDF](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2), UMDF version 2.0 adds:

* Support for timers that do not wake the system if they expire when the system is in a low-power state. For more information, see [Using Timers](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/using-timers).

* Added **CanWakeDevice** member to [**WDF_INTERRUPT_CONFIG**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfinterrupt/ns-wdfinterrupt-_wdf_interrupt_config) structure to support interrupts that can be used to bring a device from a low-power Dx state back to its fully on D0 state. For more information, see [Using an Interrupt to Wake a Device](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/using-an-interrupt-to-wake-a-device).

* Single-component, single-state (F0) power management for UMDF drivers. For more information, see [**WdfDeviceAssignS0IdleSettings**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassigns0idlesettings).

* Several debugger extension commands in Wdfkd.dll can now be used for UMDF 2.0 drivers as well. The extension library also contains the following new extension commands designed specifically for debugging UMDF 2.0 drivers:

  * [**!wdfkd.wdfumdevstack**](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/-wdfkd-wdfumdevstack)

  * [**!wdfkd.wdfumdevstacks**](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/-wdfkd-wdfumdevstacks)

  * [**!wdfkd.wdfumdownirp**](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/-wdfkd-wdfumdownirp)

  * [**!wdfkd.wdfumfile**](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/-wdfkd-wdfumfile)

  * [**!wdfkd.wdfumirp**](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/-wdfkd-wdfumirp)

  * [**!wdfkd.wdfumirps**](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/-wdfkd-wdfumirps)

  * [**!wdfkd.wdfdeviceinterrupts**](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/-wdfkd-wdfdeviceinterrupts)

For a list of extension commands and framework applicability, see [Debugger Extensions](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/debugger-extensions-for-kmdf-drivers).

* The [framework's event logger](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/using-the-framework-s-event-logger), or _In-flight Recorder_ (IFR) has been updated to work for UMDF 2.0 drivers.

* Other WDF debugger extensions have been updated to work with UMDF 2.0 drivers. For a full list of extension commands, including information about which ones apply to which framework, see [Debugger Extensions for WDF Drivers](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/debugger-extensions-for-kmdf-drivers).

* Added **WdfIoTargetOpenLocalTargetByFile** to [**WDF_IO_TARGET_OPEN_TYPE**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfiotarget/ne-wdfiotarget-_wdf_io_target_open_type) to allow UMDF drivers to send driver-created requests to lower targets that require an associated file object. For more information, see the Remarks of **WDF_IO_TARGET_OPEN_TYPE**.

* The following UMDF-only routines:

  * [_EvtRequestImpersonate_](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfrequest/nc-wdfrequest-evt_wdf_request_impersonate)
  * [**WDF_IO_TARGET_OPEN_PARAMS_INIT_OPEN_BY_FILE**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdf_io_target_open_params_init_open_by_file)
  * [**WdfDeviceAllocAndQueryInterfaceProperty**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceallocandqueryinterfaceproperty)
  * [**WdfDeviceAssignInterfaceProperty**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassigninterfaceproperty)
  * [**WdfDeviceGetDeviceStackIoType**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicegetdevicestackiotype)
  * [**WdfDeviceGetHardwareRegisterMappedAddress**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicegethardwareregistermappedaddress)
  * [**WdfDeviceMapIoSpace**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicemapiospace)
  * [**WdfDevicePostEvent**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicepostevent)
  * [**WdfDeviceQueryInterfaceProperty**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicequeryinterfaceproperty)
  * [**WdfDeviceUnmapIoSpace**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceunmapiospace)
  * [**WdfFileObjectGetInitiatorProcessId**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdffileobject/nf-wdffileobject-wdffileobjectgetinitiatorprocessid) (added to KMDF 1.21)
  * [**WdfFileObjectGetRelatedFileObject**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdffileobject/nf-wdffileobject-wdffileobjectgetrelatedfileobject)
  * [**WdfRequestGetEffectiveIoType**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestgeteffectiveiotype)
  * [**WdfRequestGetRequestorProcessId**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestgetrequestorprocessid) (added to KMDF 1.21)
  * [**WdfRequestGetUserModeInitiatedIo**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestgetusermodedriverinitiatedio)
  * [**WdfRequestImpersonate**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestimpersonate)
  * [**WdfRequestIsFromUserModeDriver**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestisfromusermodedriver)
  * [**WdfRequestRetrieveActivityId**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveactivityid)
  * [**WdfRequestSetActivityId**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsetactivityid)
  * [**WdfRequestSetUserModeDriverInitiatedIo**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsetusermodedriverinitiatedio)

* The following KMDF/UMDF methods described in [Accessing the Unified Device Property Model](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/accessing-the-unified-device-property-model):

  * [**WdfDeviceAllocAndQueryPropertyEx**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceallocandquerypropertyex)

  * [**WdfDeviceAssignProperty**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassignproperty)

  * [**WdfDeviceInitSetIoTypeEx**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetiotypeex)

  * [**WdfDeviceQueryPropertyEx**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicequerypropertyex)

  * [**WdfFdoInitAllocAndQueryPropertyEx**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitallocandquerypropertyex)

  * [**WdfFdoInitQueryPropertyEx**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitquerypropertyex)

For more information, see [Accessing the Unified Device Property Model](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/accessing-the-unified-device-property-model).

* Support for the following USB configuration types in [**WdfUsbTargetDeviceSelectConfigType**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfusb/ne-wdfusb-_wdfusbtargetdeviceselectconfigtype):

  * **WdfUsbTargetDeviceSelectConfigTypeSingleInterface**
  * **WdfUsbTargetDeviceSelectConfigTypeMultiInterface**
  * **WdfUsbTargetDeviceSelectConfigTypeInterfacesPairs**

* Support for querying the following capability types in [**WdfUsbTargetDeviceQueryUsbCapability**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicequeryusbcapability):

  * **GUID_USB_CAPABILITY_DEVICE_CONNECTION_HIGH_SPEED_COMPATIBLE**
  * **GUID_USB_CAPABILITY_DEVICE_CONNECTION_SUPER_SPEED_COMPATIBLE**

* Added [WDF Register/Port Access Functions](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfhwaccess/)

Version 1.11 adds the following driver-supplied callback interfaces and event callback functions:

* [**IPnpCallbackHardware2**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipnpcallbackhardware2)

* [**IPnpCallbackHardwareInterrupt**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipnpcallbackhardwareinterrupt)

Version 1.11 adds the following framework-supplied interfaces:

* [**IWDFCmResourceList**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfcmresourcelist)

* [**IWDFDevice3**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfdevice3)

* [**IWDFFile3**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdffile3)

* [**IWDFInterrupt**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfinterrupt)

* [**IWDFIoRequest3**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfiorequest3)

* [**IWDFUnifiedPropertyStore**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfunifiedpropertystore)

* [**IWDFUnifiedPropertyStoreFactory**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfunifiedpropertystorefactory)

* [**IWDFWorkItem**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfworkitem)

Version 1.11 adds the following capabilities to UMDF-based drivers:

* [Accessing Hardware and Handling Interrupts](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/accessing-hardware-and-handling-interrupts)

* [Using Device Pooling in UMDF Drivers](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/using-device-pooling-in-umdf-drivers)

* Added **UmdfHostProcessSharing**, **UmdfDirectHardwareAccess**, **UmdfRegisterAccessMode**, **UmdfFileObjectPolicy**, and **UmdfFsContextUsePolicy** directives, described in [Specifying WDF Directives in INF Files](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/specifying-wdf-directives-in-inf-files)

* [Well-known security identifiers (SID) for UMDF drivers](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/controlling-device-access)

* Unified property store support, described in [Using the Registry in UMDF-based Drivers](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/using-the-registry-in-umdf-1-x-drivers)

* [**IoGetDeviceObjectPointer**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceobjectpointer) is integrated to work with UMDF. In prior versions, this routine closes the handle to the device object after taking a reference on the device’s handle. This behavior was incompatible with UMDF’s expectation that the cleanup request on the device object won’t occur until after all the I/O is complete.

* [Creating UMDF-based HID Minidrivers](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/creating-umdf-hid-minidrivers)

* Enhanced support for [Supporting Idle Power-Down in UMDF-based Drivers](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/supporting-idle-power-down-in-umdf-drivers). The framework can now put the device in the D3cold power state when the idle timeout period expires. The framework can also cause the device to return to its working (D0) state when the system returns to its working (S0) state.

* The following samples are new in UMDF 1.11: [WudfVhidmini](https://learn.microsoft.com/en-us/samples/browse/), [NetNfpProvider](https://learn.microsoft.com/en-us/samples/browse/).

Version 1.9 adds the following driver-supplied callback interfaces:

* [IPnpCallbackRemoteInterfaceNotification](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipnpcallbackremoteinterfacenotification)

* [IPowerPolicyCallbackWakeFromS0](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipowerpolicycallbackwakefroms0)

* [IPowerPolicyCallbackWakeFromSx](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipowerpolicycallbackwakefromsx)

* [IQueueCallbackIoCanceledOnQueue](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iqueuecallbackiocanceledonqueue)

* [IRemoteInterfaceCallbackEvent](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iremoteinterfacecallbackevent)

* [IRemoteInterfaceCallbackRemoval](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iremoteinterfacecallbackremoval)

* [IRemoteTargetCallbackRemoval](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iremotetargetcallbackremoval)

* [IWDFRemoteInterfaceInitialize](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfremoteinterfaceinitialize)

Version 1.9 adds the following framework-supplied interfaces:

* [IWDFDevice2](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfdevice2)

* [IWDFDeviceInitialize2](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfdeviceinitialize2)

* [IWDFFile2](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdffile2)

* [IWDFIoRequest2](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfiorequest2)

* [IWDFIoTarget2](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfiotarget2)

* [IWDFNamedPropertyStore2](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfnamedpropertystore2)

* [IWDFPropertyStoreFactory](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfpropertystorefactory)

* [IWDFRemoteTarget](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfremotetarget)

* [IWDFUsbTargetPipe2](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfusb/nn-wudfusb-iwdfusbtargetpipe2)

These interfaces add the following capabilities to UMDF-based drivers:

* [Remote I/O targets](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/general-i-o-targets-in-umdf)

* [Power policy ownership](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/power-policy-ownership-in-umdf)

* The [direct I/O](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/accessing-data-buffers-in-umdf-1-x-drivers) buffer access method

* [Continuous readers](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/working-with-usb-pipes-in-umdf-1-x-drivers) for USB devices

* Enhanced support for [device interfaces](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/using-device-interfaces-in-umdf-drivers)

* Enhanced ability to [cancel I/O requests](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/canceling-i-o-requests)

* Enhanced access to the [registry](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/using-the-registry-in-umdf-1-x-drivers)
