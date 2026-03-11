# Source: https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/porting-a-driver-from-umdf-1-to-umdf-2

Title: Porting a Driver from UMDF 1 to UMDF 2 - Windows drivers

URL Source: https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/porting-a-driver-from-umdf-1-to-umdf-2

Markdown Content:
This topic describes how to port a User-Mode Driver Framework (UMDF) 1 driver to UMDF 2. You can start with a UMDF 1 driver that uses Sources/Dirs files (not a Visual Studio project), or you can convert a UMDF 1 driver that is contained in a Visual Studio project. The result will be a UMDF 2 driver project in Visual Studio. UMDF 2 drivers run on both Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) and Windows 10 Mobile.

The Echo driver sample is an example of a driver that has been ported from UMDF 1 to UMDF 2.

* [Echo Sample (UMDF Version 1)](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/user-mode-driver-framework-design-guide)
* [Echo Sample (UMDF Version 2)](https://go.microsoft.com/fwlink/p/?LinkId=617708)

To start, open a new driver project in Visual Studio. Select the **Visual C++->Windows Driver->WDF->User Mode Driver (UMDF 2)** template. Visual Studio opens a partially populated template that includes stubs for the callback functions that your driver must implement. This new driver project will be the foundation of your UMDF 2 driver. Use the UMDF 2 Echo sample as a guide to the type of code you should introduce.

Next, review your existing UMDF 1 driver code and determine object mappings. Each COM object in UMDF 1 has a corresponding WDF object in UMDF 2. For example, the **IWDFDevice** interface maps to the WDF device object, which is represented by a WDFDEVICE handle. Nearly all framework-supplied interface methods in UMDF 1 have corresponding methods in UMDF 2. For example, [**IWDFDevice::GetDefaultIoQueue**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-getdefaultioqueue) maps to [**WdfDeviceGetDefaultQueue**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicegetdefaultqueue).

Similarly, driver-supplied callback functions have equivalents in the two versions. In UMDF 1, the naming convention for driver-supplied interfaces (except for **IDriverEntry**) is _I_ Object _Callback_ Xxx**, while in UMDF 2 the naming convention for driver-supplied routines is _Evt_ ObjectXxx**. For example, the [**IDriverEntry::OnDeviceAdd**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-idriverentry-ondeviceadd) callback method maps to [_EvtDriverDeviceAdd_](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add).

Your driver implements callback functions in both UMDF 1 and 2, but the way that the driver supplies pointers to its callbacks differs. In UMDF 1, the driver implements callback methods as members of driver-supplied interfaces. The driver registers these interfaces with the framework when it creates framework objects, for example by calling [**IWDFDriver::CreateDevice**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdriver-createdevice).

In UMDF 2, the driver provides pointers to driver-supplied callback functions in configuration structures such as [**WDF_DRIVER_CONFIG**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdriver/ns-wdfdriver-_wdf_driver_config) and [**WDF_IO_QUEUE_CONFIG**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfio/ns-wdfio-_wdf_io_queue_config).

Drivers that use UMDF 1 must implement reference counting in order to determine when it is safe to delete objects. Because the framework tracks object references on the driver's behalf, a UMDF 2 driver does not need to count references.

In UMDF 2, each framework object has a default parent object. When a parent object is deleted, the framework deletes associated child objects. When your driver calls an object creation method such as [**WdfDeviceCreate**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate), it can accept the default parent, or it can specify a custom parent in a [**WDF_OBJECT_ATTRIBUTES**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfobject/ns-wdfobject-_wdf_object_attributes) structure. For a list of framework objects and their default parent objects, see [Summary of Framework Objects](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/summary-of-framework-objects).

A UMDF 1 driver implements the [**IDriverEntry**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-idriverentry) interface. In its [**IDriverEntry::OnDeviceAdd**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-idriverentry-ondeviceadd) callback method, the driver typically:

* Creates and initializes an instance of the device callback object.
* Creates the new framework device object by calling [**IWDFDriver::CreateDevice**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdriver-createdevice).
* Sets up the device's queues and their corresponding callback objects.
* Creates an instance of a device interface class by calling [**IWDFDevice::CreateDeviceInterface**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-createdeviceinterface).

A UMDF 2 driver implements [**DriverEntry**](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/driverentry-for-kmdf-drivers) and [_EvtDriverDeviceAdd_](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add). In its **DriverEntry** routine, a UMDF 2 driver typically calls [**WDF_DRIVER_CONFIG_INIT**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdf_driver_config_init) to initialize the driver's [**WDF_DRIVER_CONFIG**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdriver/ns-wdfdriver-_wdf_driver_config) structure. Then it passes this structure to [**WdfDriverCreate**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdrivercreate).

In its [_EvtDriverDeviceAdd_](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) function, the driver might do some of the following:

* Fill in the [WDFDEVICE_INIT](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/wdfdevice_init) structure, which supplies information that is used to create the device object. For more information about using WDFDEVICE_INIT, see [Creating a Framework Device Object](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/creating-a-framework-device-object).
* Set up the device object’s context area. For information about allocating and accessing context space for framework objects, see [Framework Object Context Space](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/framework-object-context-space).
* [Create the device object](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/creating-a-framework-device-object).
* Specify [request handlers](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/request-handlers) for the device object.
* [Create I/O queues](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/creating-i-o-queues).
* [Create device interfaces](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/using-device-interfaces).
* Set [device idle policy](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/supporting-idle-power-down) and [wake settings](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/supporting-system-wake-up), if the device object owns power policy.
* [Create interrupt objects](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/creating-an-interrupt-object), if the hardware supports interrupts.

When you create a new driver project in Visual Studio, the new project contains an .inx file. When you build your driver, Visual Studio compiles your .inx file into an INF file that can be used as part of a driver package.

While an INF file for a UMDF 1 driver must include a driver class ID, a DriverCLSID is not required in an INF file for a UMDF 2 driver.

Also, although a UMDF 1 driver must reference the co-installer in its INF file, no constaller reference is required in a UMDF 2 INF file. Though a coinstaller reference can appear in an INF file for a UMDF 2 driver, one is not required.

In UMDF 1, the driver usually stores device context in a driver-created callback object, for example by specifying private members of the device callback object class. Alternatively, a UMDF 1 driver can call the [**IWDFObject::AssignContext**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfobject-assigncontext) method to register context on a framework object.

In UMDF 2, the framework allocates context space based on the optional [**WDF_OBJECT_ATTRIBUTES**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfobject/ns-wdfobject-_wdf_object_attributes) structure that the driver provides when it calls an object creation method. After calling an object's create method, a driver can call [**WdfObjectAllocateContext**](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectallocatecontext) one or more times to allocate additional context space to a specific object. For the steps a UMDF 2 driver should use to define a context structure and accessor method, see [Framework Object Context Space](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/framework-object-context-space).

To debug a UMDF 2 driver, you'll use extensions in Wdfkd.dll instead of Wudfext.dll. For more info about extensions in Wudfext.dll, see [Summary of Debugger Extensions in Wdfkd.dll](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/debugger-extensions-for-kmdf-drivers).

In UMDF 2, you can also get additional driver debugging information through the Inflight Trace Recorder (IFR), as described in [Using Inflight Trace Recorder in KMDF and UMDF 2 Drivers](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/using-wpp-software-tracing-in-kmdf-and-umdf-2-drivers). Also, you can use the framework's own _In-flight Recorder_ (IFR). See [Using the Framework's Event Logger](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/using-the-framework-s-event-logger).

[Getting Started with UMDF](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2)

[Framework Object Context Space](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/framework-object-context-space)

[UMDF Version History](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/umdf-version-history)

[Framework Objects](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdf/framework-objects)
