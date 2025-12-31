# Source: https://learn.sparkfun.com/tutorials/getting-started-with-machinechat

## Introduction

The [SparkFun OpenLog Artemis (without IMU)](https://www.sparkfun.com/products/19426) is an open source data logger that comes preprogrammed to automatically log GPS, serial data, and various pressure, humidity, and distance data as well as the ability to expand out to any number of our Qwiic sensors. This makes it ideal for data collection, but what about data display? In comes Machinechat and JEDI One!

Machinechat\'s JEDI One provides an easy-to-use, customizable, one stop dashboard solution for IoT data collection, transformation, visualization, and reporting. Built-in HTTP and TCP servers allow you to start collecting data from sensors and devices in minutes, and custom plug-ins allow you to collect data from virtually any sensor or device. In addition, a fully integrated and self-contained MQTT broker makes it easy to integrate any MQTT based device or sensor. No need to set up a separate broker or use Azure or AWS for MQTT. Just configure and go!

### Required Materials

To get started, you really only need the [SparkFun OpenLog Artemis (without IMU)](https://www.sparkfun.com/products/19426) and a [Jedi One License](https://www.sparkfun.com/products/20674), but you can also get going with any of these kits:

[![SparkFun OpenLog Data Collector with Machinechat - Air Quality Monitoring](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/5/2/2/KIT-20684_SparkFun___Machinechat_Qwiic_loT-_01.jpg)](https://www.sparkfun.com/sparkfun-openlog-data-collector-with-machinechat-air-quality-monitoring.html)

### [SparkFun OpenLog Data Collector with Machinechat - Air Quality Monitoring](https://www.sparkfun.com/sparkfun-openlog-data-collector-with-machinechat-air-quality-monitoring.html) 

[ KIT-20684 ]

The Air Quality Monitoring version of the OpenLog Data Collector Kit with Machinechat allows you to display your data with th...

[ [\$199.95] ]

[![SparkFun OpenLog Data Collector with Machinechat - Environmental Monitoring](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/5/2/1/KIT-20683_SparkFun___Machinechat_Qwiic_loT-_01.jpg)](https://www.sparkfun.com/sparkfun-openlog-data-collector-with-machinechat-environmental-monitoring.html)

### [SparkFun OpenLog Data Collector with Machinechat - Environmental Monitoring](https://www.sparkfun.com/sparkfun-openlog-data-collector-with-machinechat-environmental-monitoring.html) 

[ KIT-20683 ]

The Environmental Monitoring version of the OpenLog Data Collector Kit with Machinechat allows you to display your data with ...

[ [\$189.95] ]

[![SparkFun OpenLog Data Collector with Machinechat - Base Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/2/0/5/0/8/KIT-20673_SparkFun___Machinechat_Qwiic_loT_Data_Mo-_01.jpg)](https://www.sparkfun.com/sparkfun-openlog-data-collector-with-machinechat-base-kit.html)

### [SparkFun OpenLog Data Collector with Machinechat - Base Kit](https://www.sparkfun.com/sparkfun-openlog-data-collector-with-machinechat-base-kit.html) 

[ KIT-20673 ]

The Base version of the SparkFun OpenLog Data Collector Kit with Machinechat is an easy way to organize and display your data...

[ [\$244.95] ]

### Suggested Reading

If you aren\'t familiar with the Qwiic system, we recommend reading [here for an overview](https://www.sparkfun.com/qwiic).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  [![Qwiic Connect System](https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo.png "Qwiic Connect System")](https://www.sparkfun.com/qwiic)
  -----------------------------------------------------------------------------------------------------------------------------------------------------

We would also recommend taking a look at the following tutorials if you aren\'t familiar with them. Depending on which kit you have, or which Qwiic board(s) you are planning to use, you may want to read through their respective Hookup Guides as well.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

[](https://learn.sparkfun.com/tutorials/connectivity-of-the-internet-of-things)

### Connectivity of the Internet of Things 

An overview of the different protocols that can be used for the development of Internet of Things (IoT)-based projects.

[](https://learn.sparkfun.com/tutorials/introduction-to-mqtt)

### Introduction to MQTT 

An introduction to MQTT, one of the main communication protocols used with the Internet of Things (IoT).

[](https://learn.sparkfun.com/tutorials/openlog-artemis-hookup-guide)

### OpenLog Artemis Hookup Guide 

How to use and re-program the OpenLog Artemis, an open source datalogger. The OLA comes preprogrammed to automatically log data. The OLA can also record serial data, analog voltages, or readings from external Qwiic-enabled I2C devices. Some of these Qwiic-enabled devices include GPS/GNSS modules, pressure, altitude, humidity, temperature, air quality, environment, distance, and weight sensors.

## Software Installation

Machinechat has a number of installation packages, depending on your platform. For this guide, we\'re using the JEDIOne PC Mac installation on Windows. The button below will redirect you to the Jedi Download page:

[JEDIOne Installation Downloads](https://www.machinechat.io/jedione-pcmac)

Go ahead and download the correct installation package for your platform.

[![Jedi One download page](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/0/JediOneDownloadPage.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/0/JediOneDownloadPage.png)

\

Extract your installation install, and click on that mcjedi executable and you should see the MachineChat server start running. It should look something like this:

[![Command window with the machine chat exe running](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/0/MachineChatServerWindow.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/0/MachineChatServerWindow.png)

## Logging In

Once you\'ve got the server running, you can view your dashboard in your web browser. To navigate to your dashboard, you\'ll need to go to http://\<ipaddress\>:9123/ - if you are running your web browser on the same machine as your server, you can simply type in <http://127.0.0.1:9123/>.

When logging into JEDI One for the first time, you\'ll use \"admin\" as both the login and the password. Once you\'ve logged in for the first time, you\'ll be prompted to change your password for future use. More details can be found [here: Log in to JEDI One for the first time](https://support.machinechat.io/hc/en-us/articles/360048802974-Log-in-to-JEDI-One-for-the-first-time).

[![Initial login page showing user id as admin and password as admin](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/0/machinechatloginpage.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/0/machinechatloginpage.png)

*Having a hard time seeing the details? Click the image for a closer look.*

## Firmware

In order to use the OpenLog Artemis with MachineChat, you\'ll need to make sure your OpenLog Artemis board has Firmware v2.4 or later. If you don\'t know what version you have on your OpenLog Artemis, go ahead and plug in your board and open a [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics) on the correct port. The data that spits out will tell you what version you are running:

[![COM8 serial port monitor shows output from the Artemis OpenLog and the version number is highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/0/FindingFirmwareVersion.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/0/FindingFirmwareVersion.png)

*Having a hard time seeing the details? Click the image for a closer look.*

If you DO need to update your firmware, the stable version 2.4 can be found [here](https://github.com/sparkfun/OpenLog_Artemis/releases) or by clicking the button below:

[Artemis OpenLog Firmware v2.4](https://github.com/sparkfun/OpenLog_Artemis/releases)

\

Instructions on how to update the firmware are included in the [OpenLog Artemis Hookup Guide](https://learn.sparkfun.com/tutorials/openlog-artemis-hookup-guide).

[](https://learn.sparkfun.com/tutorials/openlog-artemis-hookup-guide)

### OpenLog Artemis Hookup Guide 

August 20, 2020

How to use and re-program the OpenLog Artemis, an open source datalogger. The OLA comes preprogrammed to automatically log data. The OLA can also record serial data, analog voltages, or readings from external Qwiic-enabled I2C devices. Some of these Qwiic-enabled devices include GPS/GNSS modules, pressure, altitude, humidity, temperature, air quality, environment, distance, and weight sensors.

There\'s a lot of really great information in this tutorial, but if you want to skip all that and go directly to the \"Updating Firmware\" section, feel free to click the button below:

[Updating the Artemis OpenLog Firmware](https://learn.sparkfun.com/tutorials/openlog-artemis-hookup-guide/all#updating-firmware)

## Configuring Your Dashboard

Once you\'re logged into Machine chat, you should be able to click on **Settings** -\> **Data Collectors** and the OpenLogSerial will be listed. Go ahead and click on that ***Edit Collector*** button.

[![WebBrowser open to home page and Data Collectors Page open. OpenLogSerial shows up and the Edit Collector button is the blue button with the pencil](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/0/EditOpenLogCollector.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/0/EditOpenLogCollector.png)

*Having a hard time seeing the details? Click the image for a closer look.*

\

You may need to change some settings - verify that you\'ve got the correct Serial Port selected, and set the rest of the settings as so:

- Baud Rate (115200)
- Data Bits (8)
- Parity (No parity)
- Stop Bits (One Stop Bit)
- Record Delimiter (Newline)
- Time Stamp at Server
- Is After Line (selected) and text entry should be Content-Type: text/csv.

[![Settings are filled in for the OpenLogSerial Data Collector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/0/EditingOpenLog.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/0/EditingOpenLog.png)

*Having a hard time seeing the details? Click the image for a closer look.*

Once you\'ve checked all the above, go ahead and click Save at the bottom of the page.

You\'ll be redirected back to the Data Collectors page; if the OpenLog Collector is disabled, click on the green **Enable Collector** icon.

[![Enable the Collector by clicking on thge Green Button](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/0/EnableCollector.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/0/EnableCollector.png)

*Having a hard time seeing the details? Click the image for a closer look.*

If you click the **Edit Collector** button again, you should be able to scroll down and see the variables and data that are being collected from the OpenLog Artemis. These are the variables we\'ll use to create dashboard views!

[![In the Edit Collectors window, scroll all the way down and you should see variables from the ArtemisOpenLog](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/0/AvailableFields.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/0/AvailableFields.png)

*Having a hard time seeing the details? Click the image for a closer look.*

## Displaying Data

Now we get to do the fun stuff!

Go to Data Dashboard, and click on the Orange **ADD CHART** Button.

[![Data Dashboard and Add Chart are highlighted](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/0/CreatingDataDashboard.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/0/CreatingDataDashboard.png)

*Having a hard time seeing the details? Click the image for a closer look.*

Go ahead and fill in as you see fit. You\'ll need to click on the green plus button to add a Data Source:

[![Filling in the information we want](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/0/SettingUpNewChart.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/0/SettingUpNewChart.png)

*Having a hard time seeing the details? Click the image for a closer look.*

Click on the Green Plus button to the right of **Data Sources** to add your Data Source for your Data Table and then click ADD:

[![Add the DataSource to the table](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/0/AddDataSourceForTable.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/0/AddDataSourceForTable.png)

*Having a hard time seeing the details? Click the image for a closer look.*

Make sure you\'ve got this page filled out to your satisfaction, and then click the green \"ADD\" button.

[![Add Data Source information filled out](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/0/SettingUpNewChartWithDataSource.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/0/SettingUpNewChartWithDataSource.png)

*Having a hard time seeing the details? Click the image for a closer look.*

Aaaaand VOILA!

[![Data Dashboard shows the variable and the Data we just added](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/0/DataDashboard.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/0/DataDashboard.png)

*Having a hard time seeing the details? Click the image for a closer look.*

Take some time to poke around - you can add charts and data as you see fit - including data from Qwiic breakout boards. Here\'s a System Dashboard with some of the data from our Environmental and Air Quality sensors:

[![Image showing Temp, Humidity, Altitude, Pressure, and VOC Index Widgets](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/7/5/0/WidgetDataDisplay.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/0/WidgetDataDisplay.png)

*Having a hard time seeing the details? Click the image for a closer look.*

## Troubleshooting

### Troubleshooting the Artemis OpenLog

The Artemis OpenLog Hookup Guide has a wonderful section on troubleshooting this board. If you need help with your Artemis OpenLog, head over to the \[OpenLog Artemis Hookup Guide\] (https://learn.sparkfun.com/tutorials/openlog-artemis-hookup-guide) or click on the button below to be redirected directly to the Troubleshooting and FAQ section of the hookup guide:

[Artemis OpenLog Troubleshooting and FAQs](https://learn.sparkfun.com/tutorials/openlog-artemis-hookup-guide/troubleshooting-and-faqs)

### Troubleshooting MachineChat

MachineChat has its own Troubleshooting and Support channel - click the button below to be redirected to their website:

[MachineChat Help center](https://support.machinechat.io/hc/en-us)