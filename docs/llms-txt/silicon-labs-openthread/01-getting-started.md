# Source: https://docs.silabs.com/openthread/3.0.0/openthread-with-free-rtos/01-getting-started.md

# Getting Started

Integrating FreeRTOS into your application is simply a matter of installing the FreeRTOS component for the project in Simplicity Studio. The ot-ble-dmp sample application runs on FreeRTOS by default, and you can add FreeRTOS to any OpenThread project. The ot-cli-ftd sample application is a good starting example.

1. In your project, double-click the **.slcp file** for the project in the Project Explorer to open the project window.
2. Click the SOFTWARE COMPONENTS tab to see a complete list of Component categories.
3. Find the FreeRTOS component located under RTOS > FreeRTOS in the list of components.
4. Select **FreeRTOS** and then click **Install**.  
   ![ot-cli-ftd screen](/openthread-with-free-rtos/0.1/images/sld698-image1.png)  
   This component brings all the FreeRTOS kernel files into your project, along with some integration files and some additional components it depends on.
5. Click **View Dependencies** to display the components.

One dependency is the CMSIS-RTOS2 component, which is an RTOS abstraction layer used by the integration files. Silicon Labs recommends that application developers use the FreeRTOS API directly rather than using the CMSIS-RTOS2 API.

Another dependency is the heap implementation used by FreeRTOS. FreeRTOS comes with five different heap implementations. Each appears as a component. By default, the FreeRTOS Heap 4 component is added to the project. You can change this by selecting a different heap component and clicking **Install**. For example, FreeRTOS HEAP 3 uses the system `malloc()` and `free()` implementation and is a common choice.
