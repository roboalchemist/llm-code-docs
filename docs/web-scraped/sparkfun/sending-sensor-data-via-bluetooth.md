# Source: https://learn.sparkfun.com/tutorials/sending-sensor-data-via-bluetooth

## Introduction

Is there anything more tedious than having to connect dozens of wires to get your latest project up and running? Wouldn't it be nice if there was some way to wirelessly send data over short distances and eliminate the need for all those pesky wires? Enter Bluetooth! It's a relatively simple way for electronic devices to wirelessly connect by using a radio frequency to share data over short distances. In this tutorial, we'll teach you how to get started using Bluetooth in your projects by sending sensor data between multiple SparkFun Thing Plus ESP32 Wroom USB-C devices.

## The Project: Displaying Accelerometer Data Over Bluetooth

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/7/7/2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/7/7/2.jpg)

For this project, we are going to connect an accelerometer and SparkFun Thing Plus ESP32 board to display axis data over the serial monitor. We'll keep this example as simple as possible by using Qwiic Connect hardware to eliminate the need for soldering. The parts list is simple; two ESP32 Thing Plus Wroom USB-C boards, a Qwiic SparkFun Triple Axis Accelerometer, a Qwiic cable, lithium ion battery, and USB-C cable for programming. You can add all these items to your cart using the wishlist below.

 

 

## Step 1: Downloading the CH340C Driver

The SparkFun Thing Plus ESP32 Wroom USB-C requires a different driver than previous versions of the ESP32 Thing Plus. Since CH340C serial-to-UART is used on this board, you will need to download the CH340C driver.

If you do not already have this driver downloaded, instructions can be found here:

[](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers)

### How to Install CH340 Drivers 

August 6, 2019

How to install CH340 drivers (if you need them) on Windows, Mac OS X, and Linux.

Note: Use the "Pages" tabs on the right to navigate through different sections of the tutorial. Make sure that you use the instructions that match your computer\'s operating system (Windows, MacOSX, or Linux).

## Step 2: Setting up Arduino IDE

In order to send code to the ESP32 Thing Plus C, you will need to install the latest ESP32 board definitions in the Arduino IDE.

Here is the [.json file](https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json) for the Espressif Arduino core.

If you are not familiar with manually installing third-party cores, follow the instructions in this tutorial:

[](https://learn.sparkfun.com/tutorials/installing-board-definitions-in-the-arduino-ide)

### Installing Board Definitions in the Arduino IDE 

September 9, 2020

How do I install a custom Arduino board/core? It\'s easy! This tutorial will go over how to install an Arduino board definition using the Arduino Board Manager. We will also go over manually installing third-party cores, such as the board definitions required for many of the SparkFun development boards.

Instructions for manually installing third party cores are also available [here](https://docs.arduino.cc/learn/starting-guide/cores)

When selecting a board to program in the Arduino IDE, you should choose the SparkFun ESP32 Thing Plus C from the Tools drop down menu (Tools -\> Board -\> ESP32 -\> SparkFun ESP32 Thing Plus C).

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/7/7/BoardManagerTutorial1.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/7/7/BoardManagerTutorial1.PNG)

## Step 3: Connecting the Hardware

Connect the KX132 Accelerometer to one of the Thing Plus boards using a Qwiic cable, this is the \"Server\" board. Upload the Server code to the board using the USB-C cable (diagram shown above in \"The Project\" section). Feel free to use a different accelerometer, but make sure to remove the KX132 library and import the library compatible for the other module. When uploading is complete, disconnect this board from the computer. Now, connect the Lithium Ion battery to the \"Server\" Thing Plus. Next, connect the second Thing Plus to your computer and upload the Client code to the board.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/0/7/8/image0.jpeg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/0/7/8/image0.jpeg)

## Step 4: Uploading the Code

As mentioned in the \"Connecting Hardware\" section, we have two Arduino sketches to upload to the Thing Plus boards. Upload the first sketch to the Server Thing Plus and the second sketch to the Client Thing Plus. If you are having trouble uploading the code, review the troubleshooting tips below and ensure that the CH340C Driver is properly installed onto your computer.

**Server code:**

    /*
    Based on Neil Kolban example for IDF: https://github.com/nkolban/esp32-snippets/blob/master/cpp_utils/tests/BLE%20Tests/SampleServer.cpp
    Ported to Arduino ESP32 by Evandro Copercini
    updates by chegewara
    */

    #include <BLEDevice.h>
    #include <BLEUtils.h>
    #include <BLEServer.h>
    #include <Wire.h>                 // Must include Wire library for I2C
        #include <SparkFun_KX13X.h> // Click here to get the library: http://librarymanager/All#SparkFun_KX13X

    SparkFun_KX132 kxAccel;
    outputData myData; // Struct for the accelerometer's data
    // See the following for generating UUIDs:
    // https://www.uuidgenerator.net/

    #define SERVICE_UUID        "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
    #define CHARACTERISTIC_UUID "beb5483e-36e1-4688-b7f5-ea07361b26a8"
    #define CHARACTERISTIC_ACCX_UUID "fb6cf981-31cc-4f36-af06-1f2f3e919840"
    #define CHARACTERISTIC_ACCY_UUID "35b17f66-73d1-4c92-92f6-9032ef1987d3"
    #define CHARACTERISTIC_ACCZ_UUID "3cab9341-e65b-46e9-83ed-c8a7f2f841c2"
    // makes the chracteristic globlal
    static BLECharacteristic *pCharacteristicAccX;
    static BLECharacteristic *pCharacteristicAccY;
    static BLECharacteristic *pCharacteristicAccZ;
    void setup() 
       if (kxAccel.softwareReset())
        Serial.println("Reset.");

      // Give some time for the accelerometer to reset.
      // It needs two, but give it five for good measure.
      delay(5);

      // Many settings for KX13X can only be
      // applied when the accelerometer is powered down.
      // However there are many that can be changed "on-the-fly"
      // check datasheet for more info, or the comments in the
      // "...regs.h" file which specify which can be changed when.
      kxAccel.enableAccel(false);

      kxAccel.setRange(SFE_KX132_RANGE16G); // 16g Range
      // kxAccel.setRange(SFE_KX134_RANGE16G);         // 16g for the KX134

      kxAccel.enableDataEngine(); // Enables the bit that indicates data is ready.
      // kxAccel.setOutputDataRate(); // Default is 50Hz
      kxAccel.enableAccel();
      BLEDevice::init("Long name works now");
      BLEServer *pServer = BLEDevice::createServer();
      BLEService *pService = pServer->createService(SERVICE_UUID);
      BLECharacteristic *pCharacteristic = pService->createCharacteristic(
                                             CHARACTERISTIC_UUID,
                                             BLECharacteristic::PROPERTY_READ |
                                             BLECharacteristic::PROPERTY_WRITE
                                           );
      pCharacteristicAccX = pService->createCharacteristic(
                                             CHARACTERISTIC_ACCX_UUID,
                                             BLECharacteristic::PROPERTY_READ |
                                             BLECharacteristic::PROPERTY_WRITE
                                           );
      pCharacteristicAccY = pService->createCharacteristic(
                                             CHARACTERISTIC_ACCY_UUID,
                                             BLECharacteristic::PROPERTY_READ |
                                             BLECharacteristic::PROPERTY_WRITE
                                           );
    pCharacteristicAccZ = pService->createCharacteristic(
                                             CHARACTERISTIC_ACCZ_UUID,
                                             BLECharacteristic::PROPERTY_READ |
                                             BLECharacteristic::PROPERTY_WRITE
                                           );
      pCharacteristic->setValue("Hello World says Neil");
      pService->start();
      // BLEAdvertising *pAdvertising = pServer->getAdvertising();  // this still is working for backward compatibility
      BLEAdvertising *pAdvertising = BLEDevice::getAdvertising();
      pAdvertising->addServiceUUID(SERVICE_UUID);
      pAdvertising->setScanResponse(true);
      pAdvertising->setMinPreferred(0x06);  
      pAdvertising->setMinPreferred(0x12);
      BLEDevice::startAdvertising();
      Serial.println("Characteristic defined!");
    }

    void loop() 
      delay(100);// 100 ms
    }

**Client code:**

    /**
     * A BLE client example that is rich in capabilities.
     * There is a lot new capabilities implemented.
     * author unknown
     * updated by chegewara
     */

    #include "BLEDevice.h"
    //#include "BLEScan.h"

    // The remote service we wish to connect to.
    static BLEUUID serviceUUID("4fafc201-1fb5-459e-8fcc-c5c9c331914b");
    // The characteristic of the remote service we are interested in.
    static BLEUUID    charUUID("beb5483e-36e1-4688-b7f5-ea07361b26a8");
    static BLEUUID    charAccXUUID("fb6cf981-31cc-4f36-af06-1f2f3e919840");// use the same UUID as on the server
    static BLEUUID    charAccYUUID("35b17f66-73d1-4c92-92f6-9032ef1987d3");
    static BLEUUID    charAccZUUID("3cab9341-e65b-46e9-83ed-c8a7f2f841c2");
    //#define CHARACTERISTIC_ACC_UUID 
    static boolean doConnect = false;
    static boolean connected = false;
    static boolean doScan = false;
    static BLERemoteCharacteristic* pRemoteCharacteristic;
    static BLERemoteCharacteristic* pRemoteCharacteristicACCx;
    static BLERemoteCharacteristic* pRemoteCharacteristicACCy;
    static BLERemoteCharacteristic* pRemoteCharacteristicACCz;
    static BLEAdvertisedDevice* myDevice;

    static void notifyCallback(
      BLERemoteCharacteristic* pBLERemoteCharacteristic,
      uint8_t* pData,
      size_t length,
      bool isNotify) 

    class MyClientCallback : public BLEClientCallbacks 

      void onDisconnect(BLEClient* pclient) 
    };

    bool connectToServer() 
        Serial.println(" - Found our service");

        // Obtain a reference to the characteristic in the service of the remote BLE server.
        pRemoteCharacteristic = pRemoteService->getCharacteristic(charUUID);
        if (pRemoteCharacteristic == nullptr) 
        Serial.println(" - Found our characteristic");
        //ACC X Obtain a reference to the characteristic in the service of the remote BLE server.
        pRemoteCharacteristicACCx = pRemoteService->getCharacteristic(charAccXUUID);
        if (pRemoteCharacteristicACCx == nullptr) 
        Serial.println(" - Found our characteristic");
     //ACC Y Obtain a reference to the characteristic in the service of the remote BLE server.
        pRemoteCharacteristicACCy = pRemoteService->getCharacteristic(charAccYUUID);
        if (pRemoteCharacteristicACCy == nullptr) 
        Serial.println(" - Found our characteristic");
         //ACC Z Obtain a reference to the characteristic in the service of the remote BLE server.
        pRemoteCharacteristicACCz = pRemoteService->getCharacteristic(charAccZUUID);
        if (pRemoteCharacteristicACCz == nullptr) 
        Serial.println(" - Found our characteristic");
        // Read the value of the characteristic.
        if(pRemoteCharacteristic->canRead()) 

        if(pRemoteCharacteristic->canNotify())
          pRemoteCharacteristic->registerForNotify(notifyCallback);

        connected = true;
        return true;
    }
    /**
     * Scan for BLE servers and find the first one that advertises the service we are looking for.
     */
    class MyAdvertisedDeviceCallbacks: public BLEAdvertisedDeviceCallbacks  // Found our server
      } // onResult
    }; // MyAdvertisedDeviceCallbacks

    void setup()  // End of setup.

    // This is the Arduino main loop function.
    void loop()  else 
        doConnect = false;
      }

      // If we are connected to a peer BLE Server, update the characteristic each time we are reached
      // with the current time since boot.
      if (connected) else if(doScan)

    // read the Characteristics and store them in a variable
    // This also makes the print command do float handling
    float XValue = pRemoteCharacteristicACCx->readFloat();
    float YValue = pRemoteCharacteristicACCy->readFloat();
    float ZValue = pRemoteCharacteristicACCz->readFloat();
    Serial.print(XValue);
    Serial.print("\t");
    Serial.print(YValue);
    Serial.print("\t");
    Serial.println(ZValue);

    delay(100); // Delay a 100 ms between loops. 
    } // End of loop

## Step 5: Serial Monitor

To see if uploading the code was successful, access the Serial Monitor of the Client Thing Plus in the top right corner of the IDE. There will be readings in the X, Y, and Z directions from the accelerometer. If you do not see readings, make sure the Baud rate is reading at 115200. Successful Serial Monitor reading should look similar to the diagram below. How\'d you do? Comment for assistance or let us know about your experience!

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/7/7/SerialPortTutorial2.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/7/7/SerialPortTutorial2.PNG)

## Troubleshooting

If you're having trouble uploading code to either of the ESP32 boards, ensure that the CH340C driver is installed correctly by following the instructions outlined in Step One of this tutorial. You should also ensure that "Sparkfun ESP32 Thing Plus C" is the selected board. You can confirm this by clicking on the "Tools" tab at the top of the Arduino IDE and then looking to see what the "Board" is listed as. Note that there are multiple boards with names that are similar to "Sparkfun ESP32 Thing Plus C". Take care to choose the correct board.

## Different Ways to Display the Data

The focus of this project was to get you started with sending sensor data over Bluetooth. The next step would be to get past seeing the data on a serial monitor and display the data in more helpful options. Check out the tutorial below to see how to display the sensor data on an OLED, a Python graph or on a mobile device.

[](https://learn.sparkfun.com/tutorials/displaying-sensor-data-with-bluetooth)

### Displaying Sensor Data with Bluetooth 

March 28, 2023

In our previous Bluetooth tutorial called Sending Sensor Data Via Bluetooth, we showed how to display data from a triple axis accelerometer over the Arduino IDE's serial monitor. Continuing off of the first tutorial, we are going to expand this project to include more capabilities for visualizing and interacting with your accelerometer data.