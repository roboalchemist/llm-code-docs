# Source: https://docs.edgeimpulse.com/tutorials/end-to-end/temp-anomaly-detection-opta-plc.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Temperature anomaly detection on Opta PLC

This tutorial demonstrates how to implement and integrate [anomaly detection](/studio/projects/learning-blocks/blocks/anomaly-detection-gmm) on an Arduino Opta PLC using Edge Impulse. Anomaly detection is a machine learning technique that identifies unusual patterns in data, making it ideal for monitoring industrial processes and equipment. By training a model to recognize normal behavior, you can detect deviations that may indicate faults or malfunctions.

<Frame caption="Arduino OPTA plc">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/opta-plc.png?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=18c415999a529c15b8b8a99534abceb6" width="1024" height="573" data-path=".assets/images/opta-plc.png" />
</Frame>

## Overview

To showcase how easy it is to integrate Edge Impulse with the [Arduino Opta PLC](https://www.arduino.cc/pro/hardware-arduino-opta), we'll walk through a practical example using the Arduino DIN Celsius board that comes with the kit, but also a Motor to demonstrate this setup can be used interchangeably. This example demonstrates how to set up a temperature-controlled system, collect data, train a machine learning model, and deploy it for anomaly detection.

In this tutorial, you will:

* Collect temperature data from a sensor connected to the Opta PLC.
* Train a machine learning model in Edge Impulse to detect anomalies in the data.
* Deploy the model to the Opta PLC for real-time inference.
* Optionally, integrate the model with Arduino Cloud for remote monitoring and visualization.

### Webinar: Integrating Edge Impulse with Arduino Opta PLC and Blues Wireless

<iframe src="https://www.youtube.com/embed/6lTeBpy1QrQ?start=297s" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

We ran a webinar on integrating Edge Impulse with Arduino Opta PLC and Blues Wireless for remote monitoring and anomaly detection. The webinar covered the following topics:

* **Arduino Opta PLC:** Learn about the flexibility and ease of integration of the Arduino Opta micro PLC, designed for industrial environments.
* **Edge Impulse for Machine Learning:** Understand how to train and implement ML models for anomaly detection on industrial data directly on your Opta PLC.
* **Blues for Wireless Connectivity:** Explore how Blues' Wireless for PLC Expansion enables secure cellular connectivity, allowing your Opta PLC to communicate with cloud-based monitoring systems.

The webinar is now available on-demand [here](https://www.youtube.com/watch?v=6lTeBpy1QrQ\&t=297s).

## Prerequisites

### Hardware

* [Arduino Opta PLC](https://store.arduino.cc/collections/opta-family) (Wi-Fi version recommended)
* [Opta PLC Starter Kit](https://store.arduino.cc/products/plc-starter-kit)

### Software

* Arduino IDE 2 ([Download here](https://www.arduino.cc/en/software))
* Edge Impulse account ([Sign up here](https://www.edgeimpulse.com))
* Edge Impulse CLI ([Installation guide](/tools/clis/edge-impulse-cli/installation))

## Step 1: Set Up Your Hardware

### Hardware Setup

#### About the DIN Celsius Board

<Frame caption="DIN Celsius">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/Celsius-Top-with-Adaptor.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=1f65fdde678229ac8ff62e6d09a4193d" width="890" height="501" data-path=".assets/images/Celsius-Top-with-Adaptor.png" />
</Frame>

The DIN Celsius is an all-in-one temperature laboratory offering two independent heaters and a temperature sensor. It allows you to simulate heating scenarios and monitor temperature changes, making it ideal for testing our anomaly detection use case, we can introduce an anomaly by turning off one of the heaters to cause a deviation from the normal condition.

#### Connecting the DIN Celsius to the Opta PLC

**Safety First:** Before making any connections, ensure that all power sources are disconnected to prevent electric shock or short circuits.

**Connections Overview:**

**Power Connections:**

* Connect the +24V and GND terminals of the DIN Celsius to the corresponding power supply pins.

**Heater Control:**

* Connect Relay 3 (pin 2) on the Opta PLC to Input Heat 1 on the DIN Celsius.
* Connect Relay 4 (pin 3) on the Opta PLC to Input Heat 2 on the DIN Celsius.
* These connections will control the two independent heaters on the DIN Celsius.

**Temperature Sensor Input:**

* Connect the Output Voltage from the DIN Celsius to the I8 input (analog pin A7) on the Opta PLC.
* This connection allows the PLC to read the temperature sensor data.

**Pin Definitions:**

* HEAT\_LEFT (Relay 3) connected to pin 2
* HEAT\_RIGHT (Relay 4) connected to pin 3
* TEMP\_SENS connected to analog pin A7
* BTN (User Button) on the Opta PLC

<Frame caption="Wiring Diagram">
  <img src="https://mintcdn.com/edgeimpulse/BnOEP1CPlKpl2ntM/.assets/images/celsius_schematic.png?fit=max&auto=format&n=BnOEP1CPlKpl2ntM&q=85&s=cdba3f2b0d83f088cbdd4c7c3bec8828" width="1338" height="1000" data-path=".assets/images/celsius_schematic.png" />
</Frame>

## Step 2: Set Up Your Software

#### Arduino IDE Configuration

**Install Necessary Libraries:**

* Ensure you have the latest Arduino IDE 2 installed.
* Install any required libraries via the Library Manager, such as Edge Impulse SDK and Arduino\_HTS221 if using temperature/humidity sensors.

**Define Pin Constants:**

```cpp  theme={"system"}
#define BTN         BTN_USER       // User button on Opta WiFi
#define HEAT_LEFT   2              // Left heater control pin
#define HEAT_RIGHT  3              // Right heater control pin
#define TEMP_SENS   A7             // Temperature sensor analog pin
```

#### Testing the Connections

**Heater Control Test Code:**

```cpp  theme={"system"}
void setup() {
  pinMode(HEAT_LEFT, OUTPUT);
  pinMode(HEAT_RIGHT, OUTPUT);
}

void loop() {
  digitalWrite(HEAT_LEFT, HIGH);
  digitalWrite(HEAT_RIGHT, HIGH);
  delay(1000);
  digitalWrite(HEAT_LEFT, LOW);
  digitalWrite(HEAT_RIGHT, LOW);
  delay(1000);
}
```

* **Upload the Code:** Use the Arduino IDE to upload the sketch to the Opta PLC.
* **Verify Operation:** The LEDs on the DIN Celsius should blink, indicating the heaters are being activated.

**Temperature Sensor Reading Test:**

```cpp  theme={"system"}
void setup() {
  Serial.begin(9600);
  pinMode(TEMP_SENS, INPUT);
}

void loop() {
  int sensorValue = analogRead(TEMP_SENS);
  Serial.println(sensorValue);
  delay(250);
}
```

* **Open Serial Monitor:** Set the baud rate to 9600.
* **Observe Readings:** You should see numerical values corresponding to the temperature sensor output.

## Step 3: Collecting Data with Edge Impulse

### Create a New Project

* **Log In:** Access your Edge Impulse account.
* **New Project:** Create a project named, for example, "Opta PLC Anomaly Detection."

### Data Forwarding Sketch

Upload a sketch to the Opta PLC that reads the temperature sensor and sends data to Edge Impulse.

**Steps:**

1. **Upload the Data Forwarder Sketch:** Use the Arduino IDE to upload the sketch to the Opta PLC.
2. **Run Data Forwarder:** In your terminal, execute the data forwarding command.
3. **Select Serial Port:** Choose the serial port corresponding to the Opta PLC.
4. **Label the Data:** As you collect data, assign labels to your data (e.g., "normal," "anomalous") based on the system's behavior.

> **Note:** If you are new to Edge Impulse, please refer to our [CLI Data Forwarder documentation](/tools/clis/edge-impulse-cli/data-forwarder) for detailed instructions.

<Accordion title="Toggle to expand - Data Forwarder Sketch">
  **Data Forwarder Sketch:**

  ```cpp  theme={"system"}
  void setup() {
    Serial.begin(115200);
    while (!Serial);

    pinMode(TEMP_SENS, INPUT);
    Serial.println("Edge Impulse Data Forwarder Example");
  }

  void loop() {
    float temperature = analogRead(TEMP_SENS) * (10.0 / 1024.0); // Convert to voltage
    Serial.print("Temperature: ");
    Serial.println(temperature);

    // Send data in edge-impulse-data-forwarder format
    Serial.print("1,");
    Serial.println(temperature);

    delay(1000);
  }
  ```
</Accordion>

* **Run Data Forwarder:** In your terminal, execute:
  ```bash  theme={"system"}
  edge-impulse-data-forwarder
  ```
* **Select Serial Port:** Choose the serial port corresponding to the Opta PLC.
* **Label the Data:** Assign labels to your data (e.g., "normal," "anomalous") as you collect it.

If you are new to Edge Impulse please see our [CLI Data Forwarder documentation](/tools/clis/edge-impulse-cli/data-forwarder).

## Step 4: Training the Machine Learning Model

### Create an Impulse

**Add Blocks:**
2\. **Add Blocks:**

* **Processing Block:** Select a **Time Series** or **Spectral Analysis** block based on your data characteristics.
* **Learning Block:** Choose **Anomaly Detection** using the Gaussian Mixture Model (GMM).

<Frame caption="Impulse Studio">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/opta-plc/plc-studio1.png?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=830b37e7f34207572a7ff30c2fa8235d" width="1600" height="647" data-path=".assets/images/opta-plc/plc-studio1.png" />
</Frame>

### Configure the Impulse

* **Window Size:** Set according to the data frequency (e.g., 1000 ms).
* **Window Increase:** Set overlap (e.g., 500 ms).

### Generate Features

* **Compute Features:** Navigate to the Generate Features tab and run feature generation.

<Frame caption="Generate Features">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/opta-plc/plc-studio4.png?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=39c89f370d6b99d19b8d0c3194e41875" width="911" height="1000" data-path=".assets/images/opta-plc/plc-studio4.png" />
</Frame>

### Train the Model

**Training Parameters:**

* **Epochs:** Start with 100 and adjust as needed.
* **Learning Rate:** Default of 0.005 is usually sufficient.
  **Start Training:** Monitor the accuracy and loss graphs.

<Frame caption="Training Model">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/opta-plc/plc-studio5.png?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=0fbb42f0f4c2919b26a959f0da80dc4b" width="1226" height="1000" data-path=".assets/images/opta-plc/plc-studio5.png" />
</Frame>

### Validate the Model

* **Model Testing:** Use a separate dataset to evaluate model performance.
* **Adjust if Necessary:** Retrain or adjust parameters based on results.

<Frame caption="Model Validation">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/opta-plc/plc-studio6.png?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=b0da9cb8a9371a93f0a68f8ab3222e17" width="1600" height="638" data-path=".assets/images/opta-plc/plc-studio6.png" />
</Frame>

## Step 5: Deploying the Model to the Opta PLC

### Download the Arduino Library

* **Deployment Tab:** In Edge Impulse, go to Deployment.
* **Select Arduino Library:** Download the library tailored for your model.

<Frame caption="Download Library">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/opta-plc/arduino_library.avif?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=03229fc8f5dacf8c5be97a45cac1ca78" width="1536" height="1293" data-path=".assets/images/opta-plc/arduino_library.avif" />
</Frame>

Read on [here](/hardware/deployments/run-arduino-2-0#download-the-arduino-library)

### Include the Library in Your Sketch

* **Add Library to IDE:** Import the downloaded library into your Arduino IDE.

### Add the Inference Code

If you are new to Arduino inference code, see our Arduino inference code documentation [here](/hardware/deployments/run-arduino-2-0) for more information.

<Accordion title="Toggle to expand - Inference Code Example">
  **Inference Code Example:**

  ```cpp  theme={"system"}
  #include <Your_Edge_Impulse_Inference_Library.h>
  #include <edge-impulse-sdk/classifier/ei_run_classifier.h>

  // Define the feature buffer
  float features[EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE];

  void setup() {
    Serial.begin(115200);
    while (!Serial);

    pinMode(TEMP_SENS, INPUT);
    Serial.println("Edge Impulse Inference Example");
  }

  void loop() {
    // Collect data
    for (size_t i = 0; i < EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE; i++) {
      features[i] = analogRead(TEMP_SENS) * (10.0 / 1024.0);
      delay(10); // Adjust delay as needed
    }

    // Prepare signal
    signal_t signal;
    numpy::signal_from_buffer(features, EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE, &signal);

    // Run inference
    ei_impulse_result_t result = { 0 };
    EI_IMPULSE_ERROR res = run_classifier(&signal, &result, false);

    if (res != EI_IMPULSE_OK) {
      Serial.print("ERR: Failed to run classifier (");
      Serial.print(res);
      Serial.println(")");
      return;
    }

    // Print results
    Serial.println("Inference results:");
    for (size_t ix = 0; ix < EI_CLASSIFIER_LABEL_COUNT; ix++) {
      Serial.print(result.classification[ix].label);
      Serial.print(": ");
      Serial.println(result.classification[ix].value);
    }

    // Control heaters based on anomaly detection
    if (result.anomaly > ANOMALY_THRESHOLD) {
      // Anomaly detected, take action
      Serial.println("Anomaly detected!");
      digitalWrite(HEAT_LEFT, LOW);
      digitalWrite(HEAT_RIGHT, LOW);
    } else {
      // Normal operation
      digitalWrite(HEAT_LEFT, HIGH);
      digitalWrite(HEAT_RIGHT, HIGH);
    }

    delay(1000);
  }
  ```
</Accordion>

* Replace `Your_Edge_Impulse_Inference_Library.h` with the actual header file name from your downloaded library.
* Set `ANOMALY_THRESHOLD` to an appropriate value based on your model's performance.

### Upload the Sketch

* **Compile and Upload:** Use the Arduino IDE to program the Opta PLC with your new inference code.
* **Monitor Output:** Open the Serial Monitor to observe inference results and system behavior.

## Step 6: Viewing Data on Arduino Cloud via Blues Wireless (Optional)

This section demonstrates integrating Blues Wireless for remote connectivity and monitoring. By connecting your Opta PLC to the cloud, you can visualize data, receive alerts, and monitor system performance from anywhere.

<Frame caption="Arduino Cloud">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/opta-plc/serial_celsius.gif?s=7c8952d983fbbc3bfade77e38e5079d9" width="784" height="461" data-path=".assets/images/opta-plc/serial_celsius.gif" />
</Frame>

See the full Arduino OPTA for Arduino Cloud guide [here](https://docs.arduino.cc/tutorials/din-celsius/getting-started/).

### Blues for Wireless Connectivity:

<Frame caption="Blues Wireless">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/opta-plc/bluesopta.avif?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=291c647bfd277bfb51188b216a9c87dd" width="988" height="600" data-path=".assets/images/opta-plc/bluesopta.avif" />
</Frame>

Explore how Blues' Wireless for PLC Expansion enables seamless, secure cellular connectivity, allowing your Opta PLC to communicate with your cloud-based monitoring systems, regardless of location and without the hassle of local Wi-Fi.

See the Blues Wireless [here](https://dev.blues.io/quickstart/wireless-for-plc-quickstart).

<Info>
  This section will be updated following the Blues Wireless Webinar on the 30th of October [Sign up here](https://blues.com/webinar-revolutionize-industrial-control-deploying-anomaly-detection-plcs/)
</Info>

## Step 7: Integration with Ladder Logic (Optional)

In this section, we will integrate the anomaly detection model deployed on the Arduino Opta PLC with a ladder logic program. This integration will allow the machine learning inferences to interact with the PLC's native ladder logic control system, providing intelligent control responses to anomalies in temperature or motor power.

### Overview of Ladder Logic Integration

The Arduino PLC IDE allows you to combine an Arduino sketch with ladder logic using Shared Variables. These shared variables act as a bridge between the Edge Impulse inference running on the PLC and the PLC's control logic written in Ladder Diagram (LD) or other IEC-61131-3 programming languages (such as Function Block Diagram or Structured Text). This enables real-time decision-making based on the machine learning model's output.

### Steps for Integration

#### Create Shared Variables

In the Arduino PLC IDE, navigate to the `Global_vars` section to create shared variables that will store the results from the Edge Impulse inference. Define a shared variable for the anomaly score or classification output of the model.

**Example:**

Shared variable for storing inference result (e.g., `float anomaly_score`).

#### Modify Inference Sketch

Update the Edge Impulse inference sketch to store the inference result in the shared variable. This will allow the ladder logic to access the result.

**Example:**

```cpp  theme={"system"}
float anomaly_score;  // Shared variable to store the inference result

void setup() {
  Serial.begin(115200);
  pinMode(A7, INPUT);  // Sensor input
}

void loop() {
  float sensorValue = analogRead(A7) * (10.0 / 1024.0);  // Read sensor value
  anomaly_score = run_inference(sensorValue);  // Store inference result
  delay(1000);  // Adjust as needed
}
```

#### Ladder Logic Program

In the PLC IDE, create a new ladder logic program that will read the `anomaly_score` shared variable. The logic can then trigger actions based on the value, such as activating relays, generating alarms, or shutting down equipment in response to detected anomalies.

**Example Ladder Logic:**

Create a rung that monitors the `anomaly_score`. If the score exceeds a certain threshold, the logic can trigger an alarm (e.g., turn on an LED or activate a relay).

<Frame caption="Ladder Logic - Anomaly integration">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/opta-plc/OPTA-LD.png?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=37ecbace33caceb0b4b1abaa797731e7" width="1600" height="956" data-path=".assets/images/opta-plc/OPTA-LD.png" />
</Frame>

**Add Inputs and Outputs:**

* Define Inputs (e.g., sensor values, inference results from the Arduino sketch) and Outputs (e.g., control signals like turning on a relay).
* Click Add in the "Shared Inputs" and "Shared Outputs" sections to create global variables. These variables will allow communication between your inference sketch and ladder logic.

<Frame caption="Shared Variables">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/opta-plc/plc-global-vars.png?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=b392c40f2f8ef823c9b7b9de1f47ebf2" width="726" height="612" data-path=".assets/images/opta-plc/plc-global-vars.png" />
</Frame>

**Set up the Inputs/Outputs:**

* **Inputs:** Define variables that will receive values from the Arduino sketch (e.g., anomaly\_score).
* **Outputs:** Define variables that will control actuators (e.g., relay\_control).

#### Step 2: Accessing the Ladder Logic Editor

**Create a New Ladder Logic Program:**

* Go to the Project tab (top-left section).
* Right-click on Programs and select New Program.
* Name the program (e.g., AnomalyDetection\_LD) and select Ladder Diagram (LD) as the language.

**Opening the Ladder Logic Editor:**

* Once the program is created, double-click it to open the Ladder Diagram editor. You will see a canvas where you can start adding blocks.

#### Step 3: Designing the Ladder Logic

<Frame caption="Ladder Logic Editor">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/opta-plc/local-vars-syntax.png?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=5b27c4e499bb39379545ee789c2d97e8" width="707" height="602" data-path=".assets/images/opta-plc/local-vars-syntax.png" />
</Frame>

**Drag and Drop Components:**

* On the right panel under the Library Tree, you can see various block types, such as Comparison, Logic, and Arithmetic.
* Comparison blocks will allow you to compare the input (e.g., anomaly\_score) to a threshold (e.g., >=).

**Creating Logic:**

* **Input Condition:** Drag a Comparison block (e.g., >=) to compare the anomaly\_score to a threshold (e.g., 0.8).
* **Output Control:** Connect the result of the comparison to an Output coil that controls the relay (e.g., relay\_control).

**Steps for Adding Logic:**

* **Input:** Select anomaly\_score as the input to the comparison block.
* **Condition:** Set the threshold (e.g., >= 0.8).
* **Output:** Set the output to control a relay (e.g., activate relay\_control when the condition is met).

#### Assigning the Ladder Logic to a Task

In the PLC IDE, assign the Arduino sketch (which runs the inference) to a task such as Fast (runs every 10ms) or Background (runs every 500ms) based on your system’s real-time requirements. Attach the ladder logic program to the same or another appropriate task to ensure it reacts to the updated shared variables in a timely manner.

**Steps:**

* Go to the Project tab and locate the Tasks section.
* Assign the ladder logic program (e.g., AnomalyDetection\_LD) to an appropriate task (e.g., Fast Task for real-time control).

<Frame caption="Ladder Logic - Sketch Integration">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/opta-plc/sketch-integration.png?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=be046157c446ea89ec96f848da9a6286" width="1600" height="836" data-path=".assets/images/opta-plc/sketch-integration.png" />
</Frame>

#### Monitor and Debug

Use the Watch window in the PLC IDE to monitor the shared variables and ensure the system responds correctly to anomalies detected by the machine learning model.

**Upload the Arduino Sketch:**

* Ensure your Arduino sketch is uploaded to the Opta PLC to provide the inference results.

**Run the Ladder Logic:**

* Start the ladder logic program from the Arduino PLC IDE.
* Monitor the shared variables using the Watch window to see how the ladder logic reacts to the inference results.

### Benefits of Ladder Logic Integration

* **Real-time Control:** By integrating anomaly detection with ladder logic, you can implement real-time, intelligent control systems that take action based on data-driven decisions from the Edge Impulse model.
* **Easy Troubleshooting:** Using ladder logic alongside machine learning allows for clear, visual representation of control logic, making it easier to debug and monitor the system's responses to anomalies.
* **Seamless PLC Integration:** The Arduino PLC IDE provides a smooth environment for combining traditional control logic with modern machine learning, ensuring compatibility and ease of use.

Later will will revisit this with C++ and Siemens PLCs, for now, you can explore the [Arduino PLC IDE](https://www.arduino.cc/pro/platform-software/).

## Conclusion

Congratulations! You have successfully implemented anomaly detection on an Arduino Opta PLC using Edge Impulse. This tutorial demonstrates the seamless integration of machine learning models with industrial automation systems, enabling real-time monitoring and fault detection.

Please share your experiences and feedback with us on the [Edge Impulse forum](https://forum.edgeimpulse.com).

For more information on Edge Impulse and Arduino Opta PLC, visit the official websites:

* [Arduino Opta PLC](https://www.arduino.cc/pro/hardware-arduino-opta)

* **Arduino Cloud Issues:** We are aware of issues with Arduino Cloud .properties file format vs IDE and are working with Arduino. If you have issues try moving the .properties file to the same folder as the .ino file and re-uploading the sketch.


Built with [Mintlify](https://mintlify.com).