# Source: https://docs.edgeimpulse.com/tutorials/topics/inference/run-qualcomm-device-cloud.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run on Qualcomm Device Cloud

The [Qualcomm® Device Cloud](https://qdc.qualcomm.com/) lets you remotely access real devices, as an Edge Impulse user this means you can get started without any investment in physical hardware. Gain access to devices like the [Qualcomm Dragonwing RB3 Gen 2 Dev Kit](/hardware/boards/qualcomm-rb3-gen-2-dev-kit) to get started with AI on Qualcomm® hardware. Users get 5000 minutes of free device time, which is more than enough to run inference on a few static images, and do some initial development before you need to invest in hardware.

<Frame caption="Device Cloud – RB3 Gen 2">
  <img src="https://mintcdn.com/edgeimpulse/FtCF_ajfwASxt-xU/.assets/images/device-cloud/image10.png?fit=max&auto=format&n=FtCF_ajfwASxt-xU&q=85&s=aa2aed89f827308fcf205044dd4e8914" width="1600" height="868" data-path=".assets/images/device-cloud/image10.png" />
</Frame>

In this guide, we will show you how to:

* Spin up a virtual **Qualcomm Dragonwing RB3 Gen 2** in **Qualcomm Device Cloud (QDC)**.
* Install the **Edge Impulse CLI** on the device.
* Connect the device to **Edge Impulse Studio**.
* Run AI inference on a **static test image**.

<Frame caption="Device Cloud RB3 Connected your project">
  <img src="https://mintcdn.com/edgeimpulse/FtCF_ajfwASxt-xU/.assets/images/device-cloud/11-Device-connected-to-studio.png?fit=max&auto=format&n=FtCF_ajfwASxt-xU&q=85&s=57d0dc71c47d470dd23fb9f172c883e1" width="1600" height="236" data-path=".assets/images/device-cloud/11-Device-connected-to-studio.png" />
</Frame>

Spin up a **virtual Qualcomm Dragonwing RB3 Gen 2** in **Qualcomm Device Cloud (QDC)**, install the Edge Impulse CLI, and run AI inference on a **static test image**.

## Prerequisites

* **Qualcomm Device Cloud account** – [Sign up](https://qdc.qualcomm.com/signup) for free access to the Device Cloud.
* **Edge Impulse account** – [Sign up](https://studio.edgeimpulse.com/signup) if you don’t already have one.

## 1. Launch an interactive RB3 Gen 2 session

Click the **Devices** tab in the **Qualcomm Device Cloud** web UI, then select **Advanced on-device AI with Qualcomm Dragonwing™ RB3 Gen 2** You should see a suggestion to **Try Now**. If you don’t see this option, you may need to request access to the RB3 Gen 2 device type.

<Frame caption="QDC home - Select RB3 Gen 2">
  <img src="https://mintcdn.com/edgeimpulse/FtCF_ajfwASxt-xU/.assets/images/device-cloud/2-create-rb3-default.png?fit=max&auto=format&n=FtCF_ajfwASxt-xU&q=85&s=87045147bd5b1801d6278dd201b11f64" width="1404" height="1000" data-path=".assets/images/device-cloud/2-create-rb3-default.png" />
</Frame>

1. Log in to **QDC** > **Devices > IoT > RB3 Gen 2** > **Start Interactive Session**.
2. **Session mode**
   * **SSH only** – headless shell (fastest).
   * **Screen mirroring + SSH** – adds VNC if you need the GUI.
3. **Package upload** – This is where you can upload files to the board. Create a zip with your test image (e.g., `example.jpg`) and upload it here.
   * If you skip this step, you can upload files later using the QDC web UI.
4. Click **Start**. QDC powers on the board and shows your SSH credentials.

The following steps will mirror the steps you would take on a physical [Qualcomm Dragonwing RB3 Gen 2 Dev Kit tutorial](/hardware/boards/qualcomm-rb3-gen-2-dev-kit).

## 2. Install the Edge Impulse CLI

QDC images are minimal. We have prepared a script to install **Node.js** and the **Edge Impulse CLI** once per session:

```bash  theme={"system"}
wget https://cdn.edgeimpulse.com/firmware/linux/setup-edge-impulse-qc-linux.sh
sh setup-edge-impulse-qc-linux.sh
```

<Frame caption="CLI install">
  <img src="https://mintcdn.com/edgeimpulse/FtCF_ajfwASxt-xU/.assets/images/device-cloud/7-installs-node-and-cli.png?fit=max&auto=format&n=FtCF_ajfwASxt-xU&q=85&s=1986a1dd42fe63cce8fbd91501628da7" width="1600" height="957" data-path=".assets/images/device-cloud/7-installs-node-and-cli.png" />
</Frame>

## 3. Initialise the CLI environment

```bash  theme={"system"}
source ~/.profile
edge-impulse-linux --version   # verify installation
```

<Frame caption="CLI sourced">
  <img src="https://mintcdn.com/edgeimpulse/FtCF_ajfwASxt-xU/.assets/images/device-cloud/8-source-and-boot-cli.png?fit=max&auto=format&n=FtCF_ajfwASxt-xU&q=85&s=16801cad99211c5c8daae4d438576567" width="1600" height="927" data-path=".assets/images/device-cloud/8-source-and-boot-cli.png" />
</Frame>

## 4. Connect the board to Edge Impulse Studio

```bash  theme={"system"}
edge-impulse-linux
```

1. Paste the one-time authentication key from **Studio > Devices > Connect**.
2. Select or create a project.
3. **Camera prompt:** Choose **None** – we will use a static image.

If you ever need to reset the configuration:

```bash  theme={"system"}
edge-impulse-linux --clean
```

<Frame caption="Device connected">
  <img src="https://mintcdn.com/edgeimpulse/FtCF_ajfwASxt-xU/.assets/images/device-cloud/11-Device-connected-to-studio.png?fit=max&auto=format&n=FtCF_ajfwASxt-xU&q=85&s=57d0dc71c47d470dd23fb9f172c883e1" width="1600" height="236" data-path=".assets/images/device-cloud/11-Device-connected-to-studio.png" />
</Frame>

## 5. Run inference on a static image

### 5.1 Upload a test image

<Frame caption="Uploading a test image">
  <img src="https://mintcdn.com/edgeimpulse/FtCF_ajfwASxt-xU/.assets/images/device-cloud/upload-test-images.png?fit=max&auto=format&n=FtCF_ajfwASxt-xU&q=85&s=e4af041b66713e6df752b806371b1149" width="1600" height="894" data-path=".assets/images/device-cloud/upload-test-images.png" />
</Frame>

Use the **QDC web UI** to upload `example.jpg` (or any JPEG/PNG) to `/data/local/tmp` on the board, then move it to your home directory:

```bash  theme={"system"}
mv /data/local/tmp/example.jpg ~/
```

### 5.2 Classify the image

```bash  theme={"system"}
edge-impulse-linux-runner --disable-camera --image ~/example.jpg
```

The runner downloads your model, performs inference, and prints the predicted label(s) and confidence.

## Summary

You now have access to a virtual **RB3 Gen 2** in Qualcomm Device Cloud, installed the **Edge Impulse CLI**, connected the board to **Edge Impulse Studio**, and ran AI inference on a **static test image** without physical hardware on your desk.

## Next steps

## From virtual RB3 to QNN acceleration

The virtual **RB3 Gen 2** in Device Cloud is a perfect way to validate your Edge Impulse model before you move to a physical Snapdragon device and enable hardware acceleration.

In the companion tutorial, **[QNN Hardware Acceleration on Android](/tutorials/topics/android/qnn-acceleration)**, we take the same kind of object detection model and run it on a Snapdragon device with the **Qualcomm AI Engine Direct (QNN) TFLite delegate**.

On a Qualcomm Dragonwing RB3 Gen 2, we measured:

| Configuration                  | DSP (µs) | Inference (µs) | Speedup            |
| ------------------------------ | -------- | -------------- | ------------------ |
| Baseline (TFLite CPU/DSP only) | 5,640    | 5,748          | 1.0×               |
| With QNN delegate (HTP)        | 3,748    | 527            | **\~10.9× faster** |

Once you’re happy with your model in Device Cloud, you can flash it to a physical RB3 (or other Snapdragon dev kit) and follow the QNN guide to unlock this extra performance on the Hexagon NPU.

Now you can explore more advanced scenarios, such as streaming live camera data or running inference on a physical RB3 Gen 2 board.

* [Running inference on a live camera stream](https://qdc.qualcomm.com/support/user-guide/rtsp-streaming)
* [Run inference on a physical RB3 Gen 2 board](/hardware/boards/qualcomm-rb3-gen-2-dev-kit)


Built with [Mintlify](https://mintlify.com).