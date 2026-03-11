# Source: https://docs.edgeimpulse.com/tutorials/end-to-end/obd-automotive-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# OBD Automotive Data

This tutorial shows how to process automotive or industrial time-series data (**OBD-II** / **CAN**) data in your project. We’ll keep things general by working from CSV logs and then replaying them into an exported .eim model on a Linux SBC (e.g., Raspberry Pi).

<Frame caption="OBD formatted data">
  <img src="https://mintcdn.com/edgeimpulse/VGjHB--ZSDHOyx4y/.assets/images/obd-data/obd-data.png?fit=max&auto=format&n=VGjHB--ZSDHOyx4y&q=85&s=890c6b9e1f23176d880f489398fb04ae" width="2998" height="1720" data-path=".assets/images/obd-data/obd-data.png" />
</Frame>

We’ll classify short windows as healthy vs air-leak + NOx fault. If you don’t have live hardware, you can still follow along entirely with CSV files.

<Frame caption="Impulse">
  <img src="https://mintcdn.com/edgeimpulse/VGjHB--ZSDHOyx4y/.assets/images/obd-data/obd-impulse.png?fit=max&auto=format&n=VGjHB--ZSDHOyx4y&q=85&s=64f78306f763fe9407480f465d4b28aa" width="1970" height="1326" data-path=".assets/images/obd-data/obd-impulse.png" />
</Frame>

We’ll validate a known drivability issue: an intake air leak (lean condition) that can elevate NOx, often associated with P0171/P0174 DTCs. If you don’t have a vehicle or adapter handy, use the public project dataset: [public project](https://studio.edgeimpulse.com/public/767694/live) created for this tutorial.

## Prerequisites

Before you begin, ensure you have the following:

* An Edge Impulse account
* A compatible **OBD-II** adapter (e.g., **ELM327**)
* CSV of **OBD-II** data for healthy and unhealthy vehicle states

> Take the sample CSV to get started or collect a sample from your **OBD-II** interface using your pi and the [telemetry-obd project](https://github.com/thatlarrypearson/telemetry-obd).

## 1. Problem overview

**Goal:** Detect an **intake air leak** from **OBD-II** signals by finding windows where **NOx** is disproportionately high **relative to load** (throttle / airflow / RPM).

### Signals we will use

We’ll use a minimal, interpretable set (more can be added later):

* **MAF \[g/s]** : proxy for air mass entering the engine (load).
* **NOx \[ppm]** : emission outcome; rises with lean burn / mis-mix.
* **Throttle position \[%]** : driver demand / load request.
* *(Optional)* **RPM**, **MAP \[kPa]**, **Lambda**, **STFT/LTFT** for context.

**Healthy hypothesis:** For a given load (MAF / throttle / RPM), **NOx** stays within a predictable range.\
**Leak hypothesis:** With unmetered air, mixture trends lean > **NOx** is **higher than expected** for the same load.

### 2 Capture Options

<Frame caption="**ELM327** USB or Bluetooth logger">
  <img alt="**ELM327**" src="https://mintcdn.com/edgeimpulse/VGjHB--ZSDHOyx4y/.assets/images/obd-data/elm-bluetooth.png?fit=max&auto=format&n=VGjHB--ZSDHOyx4y&q=85&s=aa5e75dbc92d1e873352ea9b9d493044" width="860" height="622" data-path=".assets/images/obd-data/elm-bluetooth.png" />
</Frame>

**ELM327(USB/Bluetooth):** simplest path to Mode 01 PIDs (RPM, throttle, MAF, etc.).

**CAN HAT (direct bus):** robust for field installs/industrial; wire **OBD-II** **PIN 6 (CAN-H), PIN 14 (CAN-L), PIN 4 (GND)**.

<Frame caption="**OBD-II** connector pinout">
  <img alt="OBD pinout" src="https://mintcdn.com/edgeimpulse/VGjHB--ZSDHOyx4y/.assets/images/obd-data/can-wiring.png?fit=max&auto=format&n=VGjHB--ZSDHOyx4y&q=85&s=df4f2b6b49580f193642456196571376" width="656" height="452" data-path=".assets/images/obd-data/can-wiring.png" />
</Frame>

**Pi HAT wiring**

<Frame caption="Pi Hat wiring">
  <img src="https://mintcdn.com/edgeimpulse/VGjHB--ZSDHOyx4y/.assets/images/obd-data/pi-hat.png?fit=max&auto=format&n=VGjHB--ZSDHOyx4y&q=85&s=dbb664b4d4ade150a289379d812d4351" width="730" height="552" data-path=".assets/images/obd-data/pi-hat.png" />
</Frame>

> **Safety note:** Induce a small, reversible leak (loosen an intake boot or remove a tiny vacuum cap). **unplug the airflow sensor** (MAF/MAP) : this can trigger limp mode and confound data.

### 3 Data capture (reproducible method)

Capture

* **Sampling:** 2 Hz (every 500 ms).
* **Drive cycle:** idle > gentle accelerations > light cruise > decel.
* **Classes:**
  * `healthy`: intact intake, warmed-up closed loop.
  * `airleak_nox`: the same drive cycle with a small, controlled leak.
* **Windows:** 2000 ms window, 1000 ms step (overlapping).
* **Duration target:** \~10 min per class (balanced).

### 4

**Healthy window example**

<Frame caption="Healthy window (reference)">
  <img src="https://mintcdn.com/edgeimpulse/VGjHB--ZSDHOyx4y/.assets/images/obd-data/obd-impulse-pi-sig-good.png?fit=max&auto=format&n=VGjHB--ZSDHOyx4y&q=85&s=132621fa9e59a7d1d06b8d3772ee3367" width="1226" height="810" data-path=".assets/images/obd-data/obd-impulse-pi-sig-good.png" />
</Frame>

**Leak window example** : **NOx** too high relative to throttle/MAF (typical of a vacuum leak)

<Frame caption="Air-leak window (high NOx vs load)">
  <img src="https://mintcdn.com/edgeimpulse/VGjHB--ZSDHOyx4y/.assets/images/obd-data/obd-impulse-pi-sig-high-nox.png?fit=max&auto=format&n=VGjHB--ZSDHOyx4y&q=85&s=e0c502aecbe8a773fd38d637f3ced997" width="1226" height="810" data-path=".assets/images/obd-data/obd-impulse-pi-sig-high-nox.png" />
</Frame>

### 5 Simple, interpretable features (used by the classifier)

Over each 2 s window, compute:

* `nox_per_maf = NOx / max(MAF, 0.1)`
* `nox_per_throttle = NOx / max(throttle, 1)`
* `maf_per_rpm = MAF / max(RPM, 500)`
* Short-window **mean** and \*\*slope \*\* for NOx and MAF

**Decision intuition:** Windows with **high `nox_per_maf`** and/or **positive NOx slope** at modest load are more likely **air-leak**.

With the signals defined, wiring settled, and an explicit labeling protocol, we can now build the model.

## 2. Prepare the CSV

The **CSV Wizard** expects:

* A time column named **`time (ms.)`** (milliseconds since the first sample)
* One **label column** (here **`fault_label`**)
* One numeric column per OBD signal

> Take the sample CSV to get started or collect a sample from your **OBD-II** interface using your pi and the [telemetry-obd project](https://github.com/thatlarrypearson/telemetry-obd).

The CSVs for the sample project have the following headings:

```
time (ms.),fault_label,RPM [RPM],PEDAL INPUT [%],MAF [g/s],NOx [ppm]
```

## 3. Import with the CSV Wizard

1.Open your project   **Data acquisition**   **CSV Wizard**\
2\. Upload `n53_healthy_ei.csv` and `n53_faulty_ei.csv` (or your own files)\
3\. Set **Label column** = `fault_label` and **Time column** = `time (ms.)`\
4\. Confirm sampling rate ≈ **2 Hz** (every 500 ms)\
5\. Finish import : the wizard converts each file into time-aligned samples

## 4. Windowing (time-series slicing)

Use windows long enough for trims/lambda to show trends:

* **Window size:** `3000 ms`
* **Window increase:** `1500 ms`

This creates overlapping 3-second windows sliding every 1.5 s.

## 5. Create the impulse

1. Go to **Create impulse**
2. **Input:** your time-series window
3. **Processing block:** **Flatten** *(start simple)*
   * *(Optional)* add **Spectral features** for fast-changing channels (e.g., `mass_air_flow_gps`, `nox_sensor_ppm`)
   * *(Optional)* enable **Normalization** if feature scales differ by ≥10×
4. **Learning block:** **Classification (Keras)**

**Flatten settings:** defaults are fine.

> Start with **Flatten** only. If accuracy plateaus, add **Spectral features** as a second block.

## 6. Generate features

Open **Generate features** and run on all samples.\
Use **Feature explorer** to verify clusters separate (healthy vs. fault).

## 7. Train the classifier

In **Classification (Keras)**:

<Frame caption="Classification">
  <img src="https://mintcdn.com/edgeimpulse/VGjHB--ZSDHOyx4y/.assets/images/obd-data/obd-classification.png?fit=max&auto=format&n=VGjHB--ZSDHOyx4y&q=85&s=63b4b9c55e44635193b924f48bd7303e" width="964" height="1722" data-path=".assets/images/obd-data/obd-classification.png" />
</Frame>

**Network (starter):**

* Dense **128** (ReLU)   Dropout **0.20**
* Dense **64** (ReLU)
* Dense **N\_classes** (Softmax)

**Training:**

* Split: **70/30** train/validation
* Epochs: **50–100**
* Batch size: **32**
* Enable **Class weighting** if classes are imbalanced

Click **Start training** and review metrics.\
**Target:** ≥ **95%** precision/recall per class on the validation set.

* **Confusion matrix:** identify misclassifications (e.g., healthy   fault)
* **Feature explorer:** confirm separation (trims/lambda/MAF/MAP)
* If one sensor dominates (e.g., only NOx), add more context:
  * **STFT/LTFT** (fuel trims)
  * **Lambda** (bank1/2)
  * **Ratios** (e.g., `maf_per_rpm`, `map_per_throttle`)

## 9. Deploy

Open **Deploy** and choose your target:

* **Linux/Aarch64** (Raspberry Pi4)

### Scripts

We have created a short script that will play back a recording of the CSV file and simulate real-time classification of the **OBD-II** signals. This allows us to test the model's performance in a controlled environment before deploying it to a live vehicle, scripts and instructions are available from the public repository. [obd automotive data](https://github.com/edgeimpulse/obd-automotive-data)

Run the collection script to log data from your **ELM327**:

```
python3 collect_obd_data.py \
  --model ./obd_fault.eim \
  --csv ./airleak_MAF_NOx.csv \
  --axes "RPM [RPM],PEDAL INPUT [%],MAF [g/s],NOx [ppm]" \
  --hz 2 --window-ms 1000 --step-ms 1000 --label-col fault_label
```

Play back the CSV file:

```
python3 play_csv_to_eim.py \
  --model ./obd_fault.eim \
  --csv ./airleak_MAF_NOx.csv \
  --axes "RPM [RPM],PEDAL INPUT [%],MAF [g/s],NOx [ppm]" \
  --hz 2 --window-ms 1000 --step-ms 1000 --label-col fault_label
```

For live capture on Pi, a wired **CAN HAT** is typically more reliable than Bluetooth ELM clones. **USB ELM327** also works well.

### Conclusion

In this tutorial, we explored how to collect **OBD-II** data from vehicles using both Bluetooth adapters and direct CAN bus connections. This workflow generalizes to other vehicle faults (misfire, EGR, sensor bias) and industrial CAN signals.


Built with [Mintlify](https://mintlify.com).