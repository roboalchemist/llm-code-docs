# Source: https://docs.edgeimpulse.com/tutorials/end-to-end/hr-hrv-estimation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# HR/HRV estimation

In this tutorial, you'll learn how to set up the **HR/HRV Features** block within Edge Impulse Studio to process your physiological data and extract meaningful heart rate (HR) and heart rate variability (HRV) features. These features can be leveraged in various downstream machine learning tasks, such as activity classification, stress detection, and health monitoring. We will extend this section over time with more examples.

For this guide, we will be using a subset of the publicly available PPG-DaLiA dataset, which contains data collected from 15 subjects during daily activities. This dataset includes physiological signals such as photoplethysmography (PPG), accelerometer data, and heart rate ground truth, allowing us to explore how the HR/HRV Features block can be applied to real-world data.

You can download the DaLIA-PPG dataset or clone the project S1\_E4 from the links below:

<Frame caption="DaLIA-PPG Public Project">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/HRV/public-project.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=2fdf62dd4e71d9a12d1bf0200d137554" width="1600" height="943" data-path=".assets/images/HRV/public-project.png" />
</Frame>

* [Public Project](https://studio.edgeimpulse.com/studio/533651)

<Info>
  **Evaluation available for everyone, deployment only available to Enterprise plan**

  All users (developer and enterprise) can extract HR/HRV features using this processing block for testing purposes. However, **the deployment option is only available for Enterprise users**. Contact your Solution Engineer to enable it.
</Info>

## Understanding HR and HRV

### **Heart Rate (HR)**

Heart Rate refers to the number of times your heart beats per minute (BPM). It's a straightforward metric that indicates your cardiac activity and is influenced by factors like physical activity, stress, and overall health.

### **Heart Rate Variability (HRV)**

<Frame caption="Illustration of deriving HRV data from ECG and PPG signals, (a) RR intervals in the ECG signal, and (b) PP intervals in the PPG signal. N.U.: Normalised units.">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/HRV/ppg-hr-hrv.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=38cfb117a7723bb51863c6a64f0a3fb5" width="1250" height="1000" data-path=".assets/images/HRV/ppg-hr-hrv.png" />
</Frame>

Heart Rate Variability measures the variation in time intervals between successive heartbeats, known as **interbeat intervals (IBIs)**. HRV provides deeper insights into the autonomic nervous system's regulation of the heart, reflecting your body's ability to adapt to stress, recover, and maintain homeostasis.

**Key HRV Metrics:**

* **RMSSD (Root Mean Square of Successive Differences)**: Reflects short-term HRV and parasympathetic activity.
* **SDNN (Standard Deviation of NN intervals)**: Indicates overall HRV.
* **pNN50**: Percentage of intervals differing by more than 50 ms, another measure of parasympathetic activity.

Understanding both HR and HRV can provide a comprehensive view of an individual's cardiovascular and autonomic health.

## Prerequisites

* **Physiological Data**: You can download a subset of PPG-DaLIA the DaLIA-PPG dataset S1\_E4:

## Step-by-Step Guide

### Step 1: Prepare or Collect Your Time-Series Data

Ensure your CSV file is structured with the following columns:

* **Time**: The timestamp for each data point.
* **X, Y, Z**: Accelerometer data for motion artifact compensation (optional).
* **ECG/PPG**: The PPG or ECG signal for heart rate estimation.
* **HR**: Heart rate value, if available (should be uploaded as a multi-label sample for regression).
* **Label**: The activity label (optional but useful for classification tasks).

<Info>
  **HR Calculation**:
  Avoid uploading data in short snippets. HR calculation relies on history and feedback to accumulate a continuous stream for better calculation and smoothing. Upload long, contiguous data for the most accurate results.

  Developer plan users need to use single label and should keep the length to 2 seconds for the best accuracy.
</Info>

You can download a subset of the PPG-DaLIA dataset S1\_E4:

[Download CSV](https://cdn.edgeimpulse.com/datasets/HRV/ppg_dalia_subject1_acc_ppg_activity_temp.csv)

<Accordion title="Click to view a sample CSV file structure for HR/HRV data">
  ```csv  theme={"system"}
  Time,acc_x,acc_y,acc_z,ppg,eda,temp,hr,activity,activity_label,Subject
  2018-06-29 08:44:52.000000,-27,1,58,-0.0,0.0,32.15,76.0,NO_ACTIVITY,NO_ACTIVITY,Subject_1
  2018-06-29 08:44:52.031250,-27,2,59,-0.0,0.0,32.15,76.0,NO_ACTIVITY,NO_ACTIVITY,Subject_1
  2018-06-29 08:44:52.062500,-27,1,59,-0.0,0.0,32.15,76.0,NO_ACTIVITY,NO_ACTIVITY,Subject_1
  2018-06-29 08:44:52.093750,-27,1,58,-0.0,0.0,32.15,76.0,NO_ACTIVITY,NO_ACTIVITY,Subject_1
  2018-06-29 08:44:52.125000,-27,1,59,-0.0,0.0,32.15,76.0,NO_ACTIVITY,NO_ACTIVITY,Subject_1
  2018-06-29 08:44:52.156250,-27,1,59,0.0,0.832765,32.15,76.0,NO_ACTIVITY,NO_ACTIVITY,Subject_1
  2018-06-29 08:44:52.187500,-27,1,59,0.01,0.832765,32.15,76.0,NO_ACTIVITY,NO_ACTIVITY,Subject_1
  2018-06-29 08:44:52.218750,-27,1,58,-0.03,0.832765,32.15,76.0,NO_ACTIVITY,NO_ACTIVITY,Subject_1
  2018-06-29 08:44:52.250000,-27,1,58,-0.05,0.832765,32.15,76.0,NO_ACTIVITY,NO_ACTIVITY,Subject_1
  2018-06-29 08:44:52.281250,-27,1,59,0.13,0.832765,32.15,76.0,NO_ACTIVITY,NO_ACTIVITY,Subject_1
  2018-06-29 08:44:52.312500,-27,1,59,0.66,0.832765,32.15,76.0,NO_ACTIVITY,NO_ACTIVITY,Subject_1
  2018-06-29 08:44:52.343750,-27,1,59,1.37,0.832765,32.15,76.0,NO_ACTIVITY,NO_ACTIVITY,Subject_1
  2018-06-29 08:44:52.375000,-27,1,59,2.06,0.832765,32.15,76.0,NO_ACTIVITY,NO_ACTIVITY,Subject_1
  2018-06-29 08:44:52.406250,-27,1,59,2.79,1.180231,32.15,76.0,NO_ACTIVITY,NO_ACTIVITY,Subject_1
  2018-06-29 08:44:52.437500,-27,1,58,3.8,1.180231,32.15,76.0,NO_ACTIVITY,NO_ACTIVITY,Subject_1
  2018-06-29 08:44:52.468750,-27,1,59,5.06,1.180231,32.15,76.0,NO_ACTIVITY,NO_ACTIVITY,Subject_1
  2018-06-29 08:44:52.500000,-27,1,58,6.2,1.180231,32.15,76.0,NO_ACTIVITY,NO_ACTIVITY,Subject_1
  2018-06-29 08:44:52.531250,-27,1,59,7.15,1.180231,32.15,76.0,NO_ACTIVITY,NO_ACTIVITY,Subject_1
  2018-06-29 08:44:52.562500,-27,1,59,8.31,1.180231,32.15,76.0,NO_ACTIVITY,NO_ACTIVITY,Subject_1
  2018-06-29 08:44:52.593750,-27,1,59,10.09,1.180231,32.15,76.0,NO_ACTIVITY,NO_ACTIVITY,Subject_1
  2018-06-29 08:44:52.625000,-27,1,59,11.88,1.180231,32.15,76.0,NO_ACTIVITY,NO_ACTIVITY,Subject_1
  2018-06-29 08:44:52.656250,-27,2,59,13.14,1.618462,32.15,76.0,NO_ACTIVITY,NO_ACTIVITY,Subject_1
  2018-06-29 08:44:52.687500,-27,1,59,14.65,1.618462,32.15,76.0,NO_ACTIVITY,NO_ACTIVITY,Subject_1
  2018-06-29 08:44:52.718750,-27,1,59,17.91,1.618462,32.15,76.0,NO_ACTIVITY,NO_ACTIVITY,Subject_1
  2018-06-29 08:44:52.750000,-27,1,58,22.9,1.618462,32.15,76.0,NO_ACTIVITY,NO_ACTIVITY,Subject_1
  2018-06-29 08:44:52.781250,-27,1,59,27.58,1.618462,32.15,76.0,NO_ACTIVITY,NO_ACTIVITY,Subject_1
  ...
  Download the CSV here
  ```
</Accordion>

### Step 2: Upload Data to Edge Impulse

1. Log into your Edge Impulse Studio.
2. Navigate to **Data Acquisition** in the left-hand panel.
3. Click **Upload Data** and select your CSV file for each subject.
4. Ensure that the data is correctly parsed, and assign appropriate labels for heartrate applicable (e.g., 100, 90, etc.).

<Frame caption="Data Upload">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-upload-hr-hrv.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=d9c0499503b5c08317266a47ca513e61" width="1600" height="776" data-path=".assets/images/data-upload-hr-hrv.png" />
</Frame>

### Step 3: Create an Impulse for HR/HRV Processing

1. Go to **Impulse Design** > **Create Impulse**.
2. Add a **HR and HRV Features** block:
   * **Input Axes**: Select accX, accY, accZ, PPG (if using accelerometer data for motion artifact correction).
   * Set **Window Size** to 2000 ms.
   * Set **Frequency (Hz)** to 25 Hz (tolerance +/- 1 Hz) or 50 Hz (tolerance +/- 3 Hz).

<Frame caption="Create Impulse">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/HRV/regression-block-configuration.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=923f87d6e1518f65b416c51e14b490de" width="1600" height="921" data-path=".assets/images/HRV/regression-block-configuration.png" />
</Frame>

### Step 4: Add the HR/HRV Block

1. Under **Impulse Design**, add the **HR/HRV Features** block.

<Tabs>
  <Tab title="PPG Configuration">
    * **Input Axes**: Select your PPG signal for HR estimation.
    * **HR Window Size**: Set the window size for heart rate computation (e.g., 9 seconds, and no shorter than 2 seconds).
    * **HRV Settings**: Enable all HRV features to see RMSSD and other params.

    <Frame caption="PPG HR-HRV Settings">
      <img src="https://mintcdn.com/edgeimpulse/C0SzOGcUNl7GskyL/.assets/images/hr-hrv-ppg.png?fit=max&auto=format&n=C0SzOGcUNl7GskyL&q=85&s=6b9f8153c2c077bcbeaafc3b24d7ef37" width="1600" height="847" data-path=".assets/images/hr-hrv-ppg.png" />
    </Frame>
  </Tab>

  <Tab title="ECG Configuration">
    * **Input Axes**: Select your ECG signal for HR estimation.
    * **HR Window Size**: Set the window size for heart rate computation (e.g., 10 seconds and upwards of 90 seconds for best accuracy).
    * **HRV Settings**: Enable HRV features such as RMSSD or time-series statistics.

    <Frame caption="ECG HR-HRV Settings">
      <img src="https://mintcdn.com/edgeimpulse/C0SzOGcUNl7GskyL/.assets/images/hr-hrv-ecg.png?fit=max&auto=format&n=C0SzOGcUNl7GskyL&q=85&s=2bb9411ed46f503efb302af6bf830755" width="1600" height="847" data-path=".assets/images/hr-hrv-ecg.png" />
    </Frame>
  </Tab>

  <Tab title="PPG + Accelerometer Configuration">
    * **Input Axes**: Select your PPG signal for HR estimation.
    * **Accelerometer X, Y, Z**: Include these axes to filter motion artifacts.
    * **HR Window Size**: Set the window size for heart rate computation (e.g., 10 seconds).
    * **HRV Settings**: Enable HRV features such as RMSSD or time-series statistics.

    <Frame caption="PPG + Accelerometer HR-HRV Settings">
      <img src="https://mintcdn.com/edgeimpulse/C0SzOGcUNl7GskyL/.assets/images/hr-hrv-ppg-accelerometer.png?fit=max&auto=format&n=C0SzOGcUNl7GskyL&q=85&s=92eebdf51da1afb68084850cb28e7ab1" width="1600" height="905" data-path=".assets/images/hr-hrv-ppg-accelerometer.png" />
    </Frame>
  </Tab>
</Tabs>

### Step 5: Generate Features

1. Click on **Generate Features** from the top menu.
2. Review the feature generation output to ensure that the raw signals are correctly processed.
3. Edge Impulse will generate the features for both heart rate and HRV over the specified window size.

<Frame caption="HR-HRV Block Generate Features">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/HRV/generate-features.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=c6de6e7aab153212166c280b121e2ea0" width="1600" height="961" data-path=".assets/images/HRV/generate-features.png" />
</Frame>

### Step 6: Configure the Regression Block

1. Add a **Learning Block** such as a **Regression** if you wish to estimate HR
2. Ensure that **HR/HRV** is selected as the input feature.
3. Train the model using your labeled data to predict different heart rate.

<Frame caption="Regression Block Configuration">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/HRV/regression-block-configuration.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=923f87d6e1518f65b416c51e14b490de" width="1600" height="921" data-path=".assets/images/HRV/regression-block-configuration.png" />
</Frame>

### Step 7: Test and Validate the Model

1. After training, use **Model Testing** to evaluate the performance of your HR/HRV feature extraction and heart rate prediction model.
2. Upload test data to ensure that the heart rate is correctly estimated and any HRV features are extracted as expected.

<Frame caption="HR-HRV Test Classification">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/HRV/test-classification-output.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=0229fbbc6612b6e5df062f172b451bcc" width="875" height="1000" data-path=".assets/images/HRV/test-classification-output.png" />
</Frame>

### Step 8: Deploy the Model (Enterprise Only)

For enterprise users, you can deploy the model to your target device and start collecting real-time heart rate and HRV data. When the model is trained and validated, you can deploy it to your target device or C++ binary for real-time heart rate and HRV monitoring.

Deployment will look as follows:

<Frame caption="HR-HRV Enterprise Deployment">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/HRV/deployment-enabled.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=b86ae4a4ba02b1be492b7eb70ae92fd7" width="1179" height="1000" data-path=".assets/images/HRV/deployment-enabled.png" />
</Frame>

To include heart rate extraction alongside your classifier results, define the following macro in your deployment:

```cpp  theme={"system"}
#if EI_DSP_ENABLE_RUNTIME_HR == 1
    ei_impulse_result_hr_t hr_calcs;
#endif
```

This macro will enable the HR/HRV Features block to calculate heart rate and HRV features in real-time.

```cpp  theme={"system"}
typedef struct {
    float heart_rate;  // The calculated heart rate in beats per minute (BPM)
} ei_impulse_result_hr_t;
```

Read on in the [HR/HRV Features block documentation for more deployment details](/studio/projects/processing-blocks/blocks/hr-hrv) or speak with your enterprise support team for more guidance.

For Developer plan users, the deployment option is not available, contact our sales team if you want to upgrade to an [Enterprise plan](https://edgeimpulse.com/pricing):

<Frame caption="HR-HRV Deployment">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/HRV/deployment.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=874712894f64f5d47b278ebff7af3290" width="1584" height="368" data-path=".assets/images/HRV/deployment.png" />
</Frame>

## Conclusion

By following this tutorial, you've successfully set up the HR/HRV Features block in Edge Impulse Studio, extracted meaningful cardiovascular features, and optionally trained a machine learning model. This foundation enables you to build robust, real-time heart rate and HRV monitoring solutions for applications like health monitoring, stress detection, and fitness tracking.

## Additional Resources

* **Edge Impulse Documentation**: [HR/HRV Features](/studio/projects/processing-blocks/blocks/hr-hrv)

If you have any questions or need further assistance, feel free to reach out on the [Edge Impulse Forum](https://forum.edgeimpulse.com) or consult the documentation.


Built with [Mintlify](https://mintlify.com).