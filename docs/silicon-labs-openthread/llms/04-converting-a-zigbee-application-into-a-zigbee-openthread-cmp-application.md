# Source: https://docs.silabs.com/openthread/3.0.0/concurrent-mp-soc/04-converting-a-zigbee-application-into-a-zigbee-openthread-cmp-application.md

# Converting a Zigbee Application into a Zigbee-OpenThread CMP Application

This section describes the steps involved in converting a Z3Light into a Concurrent Multiprotocol application that includes the OpenThread stack.

1. Use the Simplicity Studio **Create New Project** wizard to create a Zigbee – SoC Light project for your board of choice.
2. Open the **Software Components** tab of the generated project to add the OpenThread > **Stack (FTD)** component. Note that the addition of this component automatically adds a Real Time Operating System (RTOS) to the project.  
   ![image](/concurrent-mp-soc/0.1/images/sld678-image3.png)
3. Select the IO Stream > Driver > IOS Stream: USART > **vcom** component and configure it by increasing **Receive buffer size** to 128.  
   ![image](/concurrent-mp-soc/0.1/images/sld678-image4.png)  
   ![image](/concurrent-mp-soc/0.1/images/sld678-image5.png)
4. Search for the **Memory Manager region** component and increase stack size to 4608 to account for the OpenThread stack usage. Heap size is set automatically to use up any remaining RAM.  
   ![image](/concurrent-mp-soc/0.1/images/sld678-image6.png)  
   ![image](/concurrent-mp-soc/0.1/images/sld678-image7.png)

> **Note**: On Series 3 Platforms all sample application are required to be run by an RTOS. Therefore, if you are using a Series 3 part you will not need to follow Step 5.

1. The RTOS selection defaults to FreeRTOS with an option to use Micrium RTOS instead. If your project uses Micrium, select Micrium > Common > **Micrium OS Common Module Core** component and configure it to decrease “size of heap memory” to 0 to prevent Micrium RTOS from allocating its own heap memory.  
   ![image](/concurrent-mp-soc/0.1/images/sld678-image8.png)  
   ![image](/concurrent-mp-soc/0.1/images/sld678-image9.png)
2. Add OpenThread CLI commands by installing the Zigbee > Zigbee 3.0 > **OpenThread CLI using Silabs unified platform** (ot_up_cli) component.  
   ![image](/concurrent-mp-soc/0.1/images/sld678-image10.png)
3. Select the OpenThread > **Platform Abstraction** component and configure the following:  
   - OpenThread stack task priority is set to 49 to match the Zigbee stack task RTOS priority.  
   - OpenThread app task priority is set to 48 to match Zigbee app framework RTOS priority  
   ![image](/concurrent-mp-soc/0.1/images/sld678-image11.png)  
   ![image](/concurrent-mp-soc/0.1/images/sld678-image12.png)
4. Search for **Circular Queue** and configure queue size to 16. This will ensure proper operation of the OpenThread radio Rx buffers.  
   ![image](/concurrent-mp-soc/0.1/images/sld678-image13.png)  
   ![image](/concurrent-mp-soc/0.1/images/sld678-image14.png)
5. Right click the Z3Light project in Simplicity Studio’s Project Explorer view and click Properties. Open C/C++ Build Settings and Under GNU ARM C Compiler, select Preprocessor. Add two preprocessor define symbols:  
   - For Micrium OS Only - OS_CFG_COMPAT_INIT (Used in conjunction with LIB_MEM_CFG_HEAP_SIZE to allow the application to handle heap allocation)
6. Click **Apply and Close** to save.  
   ![image](/concurrent-mp-soc/0.1/images/sld678-image15.png)
7. Open app.c file in the project folder and add the code below to the beginning of the file to initialize OpenThread. Save file and build the project.  
   ```C  
   #if defined(OPENTHREAD_FTD)  
     #include <assert.h>  
     #include <openthread-core-config.h>  
     #include <openthread/config.h>  
     
     #include <openthread/ncp.h>  
     #include <openthread/diag.h>  
     #include <openthread/tasklet.h>  
     
     #include "openthread-system.h"  
     
   static otInstance *     sInstance       = NULL;  
     
   void sl_ot_create_instance(void)  
   {  
     #if OPENTHREAD_CONFIG_MULTIPLE_INSTANCE_ENABLE  
     size_t   otInstanceBufferLength = 0;  
     uint8_t *otInstanceBuffer       = NULL;  
     
     // Call to query the buffer size  
     (void)otInstanceInit(NULL, &otInstanceBufferLength);  
     
     // Call to allocate the buffer  
     otInstanceBuffer = (uint8_t *)malloc(otInstanceBufferLength);  
     assert(otInstanceBuffer);  
     
     // Initialize OpenThread with the buffer  
     sInstance = otInstanceInit(otInstanceBuffer, &otInstanceBufferLength);  
     #else  
     sInstance = otInstanceInitSingle();  
     #endif  
     assert(sInstance);  
   }  
     
   otInstance *otGetInstance(void)  
   {  
     return sInstance;  
   }  
     
   #endif //#if defined(OPENTHREAD_FTD)  
   ```
8. Force generate the project and build project.  
   ![image](/concurrent-mp-soc/0.1/images/sld678-image16.png)

This application can now form a distributed Zigbee network or join any Zigbee network (centralized or distributed). It can also function as a leader, child, or router on the OpenThread network.

## Optional - Adding Bluetooth to the Concurrent Multiprotocol Application

This section describes the steps involved in adding Bluetooth to the above application. Search for and install the following components:

- `bluetooth_stack` in the software components  
  ![image](/concurrent-mp-soc/0.1/images/sld678-image17.png)
- `gatt_configuration`  
  ![image](/concurrent-mp-soc/0.1/images/sld678-image18.png)
- `bluetooth_feature_legacy_advertiser`  
  ![image](/concurrent-mp-soc/0.1/images/sld678-image19.png)
- `bluetooth_feature_connection`  
  ![image](/concurrent-mp-soc/0.1/images/sld678-image20.png)
- `bluetooth_feature_gatt` – Install the GATT Client and GATT Server  
  ![image](/concurrent-mp-soc/0.1/images/sld678-image21.png)  
  ![image](/concurrent-mp-soc/0.1/images/sld678-image22.png)
- `bluetooth_feature_legacy_scanner`  
  ![image](/concurrent-mp-soc/0.1/images/sld678-image23.png)
- `bluetooth_feature_sm`  
  ![image](/concurrent-mp-soc/0.1/images/sld678-image24.png)
- `bluetooth_feature_system`  
  ![image](/concurrent-mp-soc/0.1/images/sld678-image25.png)
- `zigbee_ble_dmp_cli`  
  ![image](/concurrent-mp-soc/0.1/images/sld678-image26.png)

In addition to the above, add the following snippet of code in the project app.c file. This sample code provides an implementation for the Bluetooth event handler (`sl_bt_on_event` function).

```C
#ifdef SL_CATALOG_BLUETOOTH_PRESENT

//------------------------------------------------------------------------------
// Bluetooth Event handler

#include "zigbee_app_framework_event.h"
#include "sl_zigbee_system_common.h"
#include "sl_bluetooth.h"
#include "sl_bluetooth_advertiser_config.h"
#include "sl_bluetooth_connection_config.h"
#include "sl_component_catalog.h"
static uint8_t cli_adv_handle;
static uint8_t activeBleConnections = 0;
void zb_ble_dmp_print_ble_address(uint8_t *address)
{
  sl_zigbee_app_debug_print("\nBLE address: [%02X %02X %02X %02X %02X %02X]\n",
                            address[5], address[4], address[3],
                            address[2], address[1], address[0]);
}
struct {
  bool inUse;
  bool isMaster;
  uint8_t connectionHandle;
  uint8_t bondingHandle;
  uint8_t remoteAddress[6];
} bleConnectionTable[SL_BT_CONFIG_MAX_CONNECTIONS];

void bleConnectionInfoTableInit(void)
{
  uint8_t i;
  for (i = 0; i < SL_BT_CONFIG_MAX_CONNECTIONS; i++) {
    bleConnectionTable[i].inUse = false;
  }
}
uint8_t bleConnectionInfoTableFindUnused(void)
{
  uint8_t i;
  for (i = 0; i < SL_BT_CONFIG_MAX_CONNECTIONS; i++) {
    if (!bleConnectionTable[i].inUse) {
      return i;
    }
  }
  return 0xFF;
}

bool bleConnectionInfoTableIsEmpty(void)
{
  uint8_t i;
  for (i = 0; i < SL_BT_CONFIG_MAX_CONNECTIONS; i++) {
    if (bleConnectionTable[i].inUse) {
      return false;
    }
  }
  return true;
}

uint8_t bleConnectionInfoTableLookup(uint8_t connHandle)
{
  uint8_t i;
  for (i = 0; i < SL_BT_CONFIG_MAX_CONNECTIONS; i++) {
    if (bleConnectionTable[i].inUse
        && bleConnectionTable[i].connectionHandle == connHandle) {
      return i;
    }
  }
  return 0xFF;
}

void bleConnectionInfoTablePrintEntry(uint8_t index)
{
  assert(index < SL_BT_CONFIG_MAX_CONNECTIONS
        && bleConnectionTable[index].inUse);
  sl_zigbee_app_debug_println("**** Connection Info index[%d]****", index);
  sl_zigbee_app_debug_println("connection handle 0x%x",
                              bleConnectionTable[index].connectionHandle);
  sl_zigbee_app_debug_println("bonding handle = 0x%x",
                              bleConnectionTable[index].bondingHandle);
  sl_zigbee_app_debug_println("local node is %s",
                               (bleConnectionTable[index].isMaster) ? "master" : "slave");
  sl_zigbee_app_debug_print("remote address: ");
  zb_ble_dmp_print_ble_address(bleConnectionTable[index].remoteAddress);
  sl_zigbee_app_debug_println("");
  sl_zigbee_app_debug_println("*************************");
}

void sl_bt_on_event(sl_bt_msg_t* evt)
{
  switch (SL_BT_MSG_ID(evt->header)) {
    case sl_bt_evt_system_boot_id: {
      bd_addr ble_address;
      uint8_t type;
      sl_status_t status = sl_bt_system_hello();
      sl_zigbee_app_debug_println("BLE hello: %s",
                                   (status == SL_STATUS_OK) ? "success" : "error");
      #define SCAN_WINDOW 5
      #define SCAN_INTERVAL 10

      status = sl_bt_scanner_set_parameters(sl_bt_scanner_scan_mode_active,
                                            (uint16_t)SCAN_INTERVAL,
                                            (uint16_t)SCAN_WINDOW);
      status = sl_bt_system_get_identity_address(&ble_address, &type);
      zb_ble_dmp_print_ble_address(ble_address.addr);

      status = sl_bt_advertiser_create_set(&cli_adv_handle);
      if (status) {

        sl_zigbee_app_debug_println("sl_bt_advertiser_create_set status 0x%02x", status);
      }
    }
    break;

    case sl_bt_evt_connection_opened_id: {
      sl_zigbee_app_debug_println("sl_bt_evt_connection_opened_id \n");
      sl_bt_evt_connection_opened_t *conn_evt =
        (sl_bt_evt_connection_opened_t*) &(evt->data);
      uint8_t index = bleConnectionInfoTableFindUnused();
      if (index == 0xFF) {
        sl_zigbee_app_debug_println("MAX active BLE connections");
        assert(index < 0xFF);
      } else {
        bleConnectionTable[index].inUse = true;
        bleConnectionTable[index].isMaster = (conn_evt->role > 0);
        bleConnectionTable[index].connectionHandle = conn_evt->connection;
        bleConnectionTable[index].bondingHandle = conn_evt->bonding;
        (void) memcpy(bleConnectionTable[index].remoteAddress,
                      conn_evt->address.addr, 6);

        activeBleConnections++;
        sl_bt_connection_set_preferred_phy(conn_evt->connection, sl_bt_test_phy_1m, 0xff);
        sl_zigbee_app_debug_println("BLE connection opened");
        bleConnectionInfoTablePrintEntry(index);
        sl_zigbee_app_debug_println("%d active BLE connection",
                                    activeBleConnections);
      }
    }
    break;
    case sl_bt_evt_connection_phy_status_id: {
      sl_bt_evt_connection_phy_status_t *conn_evt =
         (sl_bt_evt_connection_phy_status_t *)&(evt->data);
      // indicate the PHY that has been selected
      sl_zigbee_app_debug_println("now using the %dMPHY\r\n",
                                  conn_evt->phy);
    }
    break;
    case sl_bt_evt_connection_closed_id: {
      sl_bt_evt_connection_closed_t *conn_evt =
        (sl_bt_evt_connection_closed_t*) &(evt->data);

      uint8_t index = bleConnectionInfoTableLookup(conn_evt->connection);
      assert(index < 0xFF);

      bleConnectionTable[index].inUse = false;
      if  ( activeBleConnections ) {
        --activeBleConnections;
      }

      sl_zigbee_app_debug_println(
        "BLE connection closed, handle=0x%02x, reason=0x%02x : [%d] active BLE connection",
        conn_evt->connection, conn_evt->reason, activeBleConnections);
    }
    break;

    case sl_bt_evt_scanner_legacy_advertisement_report_id: {
      sl_zigbee_app_debug_print("Scan response, address type=0x%02x",
                                evt->data.evt_scanner_legacy_advertisement_report.address_type);
      zb_ble_dmp_print_ble_address(evt->data.evt_scanner_legacy_advertisement_report.address.addr);
      sl_zigbee_app_debug_println("");
    }
    break;

    case sl_bt_evt_connection_parameters_id: {
      sl_bt_evt_connection_parameters_t* param_evt =
        (sl_bt_evt_connection_parameters_t*) &(evt->data);
      sl_zigbee_app_debug_println(
        "BLE connection parameters are updated, handle=0x%02x, interval=0x%02x, latency=0x%02x, timeout=0x%02x, security=0x%02x",
        param_evt->connection,
        param_evt->interval,
        param_evt->latency,
        param_evt->timeout,
        param_evt->security_mode);
    }
    break;

    case sl_bt_evt_gatt_service_id: {
      sl_bt_evt_gatt_service_t* service_evt =
        (sl_bt_evt_gatt_service_t*) &(evt->data);
      uint8_t i;
      sl_zigbee_app_debug_println(
        "GATT service, conn_handle=0x%02x, service_handle=0x%04x",
        service_evt->connection, service_evt->service);
      sl_zigbee_app_debug_print("UUID=[");
      for (i = 0; i < service_evt->uuid.len; i++) {
        sl_zigbee_app_debug_print("0x%04x ", service_evt->uuid.data[i]);
    }
    sl_zigbee_app_debug_println("]");
  }
  break;

  default:
  break;
  }
}
void zb_ble_dmp_print_ble_connections(void)
{
  uint8_t i;
  for (i = 0; i < SL_BT_CONFIG_MAX_CONNECTIONS; i++) {
    if (bleConnectionTable[i].inUse) {
      bleConnectionInfoTablePrintEntry(i);
    }
  }
}
#endif //SL_CATALOG_BLUETOOTH_PRESENT
```