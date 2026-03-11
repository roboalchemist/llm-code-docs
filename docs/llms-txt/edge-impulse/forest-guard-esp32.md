# Source: https://docs.edgeimpulse.com/projects/expert-network/forest-guard-esp32.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Forest Guard Decentralized Edge-AI LoRa Mesh Network for Forest Surveillance

Created By: [Mukesh Sankhla](https://www.linkedin.com/in/mukeshsankhla)

Public Project Link: [https://studio.edgeimpulse.com/public/779225/live](https://studio.edgeimpulse.com/public/779225/live)

GitHub Repo: [https://github.com/MukeshSankhla/Forest-Guard](https://github.com/MukeshSankhla/Forest-Guard)

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/cover.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=3efd75fa8e5fe7041277a0221d883c04" alt="" width="1920" height="1080" data-path=".assets/images/forest-guard-esp32/cover.png" />

## Intro

Forests are the lungs of our planet, yet they remain vulnerable to poaching, illegal logging, and devastating wildfires. Remote regions are often unmonitored because they lack infrastructure, no cellular coverage, no internet, and no reliable power. Traditional solutions depend on towers, GSM networks, or satellite links, all of which are either unreliable or prohibitively expensive in deep forest zones.

Forest Guard redefines forest monitoring with a self-sustaining, decentralized, and intelligent mesh network that brings security where no traditional network can.

<iframe src="https://www.youtube.com/embed/ol8-Vw4EQvI" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

**What Makes Forest Guard Different?**
Instead of relying on costly connectivity, our system builds a solar-powered sensor mesh using LoRa Meshtastic. Each node is intelligent at the edge, capable of running AI models locally to detect events like gunshots via an onboard microphone and Edge Impulse classification. Coupled with environmental sensors and a smoke detector, the system can issue real-time alerts about fire outbreaks or human intrusion.

When an anomaly is detected, the alert propagates through the LoRa mesh to a gateway node, which syncs with the cloud when internet is available. The data is visualized on a web-based dashboard, showing sensor activity, live alerts, and precise node locations on a map.

This means no single point of failure, no dependency on fragile infrastructure, and the ability to scale across vast landscapes with just low-power radios and the sun.

**Why It Matters**

1. Early Fire Detection - Prevent small sparks from becoming catastrophic forest fires.
2. Anti-Poaching & Logging Defense - Gunshot detection provides actionable intelligence for rangers.
3. Sustainable Design - Fully solar-powered nodes with custom PCBs for durability.
4. Decentralized & Resilient - Operates even without internet; data flows peer-to-peer until a gateway is reached.
5. Community & Conservation Impact - Helps safeguard biodiversity, human settlements, and natural heritage.

With the NextPCB, we will fabricate custom PCBs for the sensor nodes. These PCBs integrate:

1. ESP32-S3 & RP2040 LoRa modules
2. Solar & battery management
3. Environmental, smoke, and audio sensors

This ensures ruggedness, consistent quality, and rapid deployment of multiple nodes, transforming our prototype into a scalable, field-ready system.

<img src="https://mintcdn.com/edgeimpulse/GfuP4tH_LMl5IjE-/.assets/images/forest-guard-esp32/C1.JPG?fit=max&auto=format&n=GfuP4tH_LMl5IjE-&q=85&s=56817b8ba8ac95b321a04d89874225ef" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/C1.JPG" />

<img src="https://mintcdn.com/edgeimpulse/GfuP4tH_LMl5IjE-/.assets/images/forest-guard-esp32/C2.JPG?fit=max&auto=format&n=GfuP4tH_LMl5IjE-&q=85&s=8e4c42bed2577cf9a8bfdda529d01c5e" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/C2.JPG" />

<img src="https://mintcdn.com/edgeimpulse/GfuP4tH_LMl5IjE-/.assets/images/forest-guard-esp32/C3.JPG?fit=max&auto=format&n=GfuP4tH_LMl5IjE-&q=85&s=dc158e494bcc40be0c89b7478aba978e" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/C3.JPG" />

<img src="https://mintcdn.com/edgeimpulse/GfuP4tH_LMl5IjE-/.assets/images/forest-guard-esp32/C4.JPG?fit=max&auto=format&n=GfuP4tH_LMl5IjE-&q=85&s=be45d870c6d147c9fd07e34d71fc4398" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/C4.JPG" />

<img src="https://mintcdn.com/edgeimpulse/GfuP4tH_LMl5IjE-/.assets/images/forest-guard-esp32/C5.JPG?fit=max&auto=format&n=GfuP4tH_LMl5IjE-&q=85&s=3ca7a7f1c82ee6841a3cd4cf74f523ad" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/C5.JPG" />

<img src="https://mintcdn.com/edgeimpulse/GfuP4tH_LMl5IjE-/.assets/images/forest-guard-esp32/C6.JPG?fit=max&auto=format&n=GfuP4tH_LMl5IjE-&q=85&s=80b5e2427027550586edd8a2045e2599" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/C6.JPG" />

<img src="https://mintcdn.com/edgeimpulse/GfuP4tH_LMl5IjE-/.assets/images/forest-guard-esp32/C7.JPG?fit=max&auto=format&n=GfuP4tH_LMl5IjE-&q=85&s=865d383c4868f93101fa495806cd426c" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/C7.JPG" />

**The Big Picture**
Forest Guard isn’t just a hardware project; it’s a blueprint for protecting forests worldwide. By combining edge AI, mesh networking, and sustainable power, we deliver a system that communities, conservationists, and governments can deploy today to build a safer, greener tomorrow.

## Supplies

**Components For 1x Node Unit:**

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S1.JPG?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=63d2c028fe7cad0b99c364b96c1481e9" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S1.JPG" />

1. 1x Custom Node PCB
2. 1x [Gravity: Multifunctional Environmental sensor](https://www.dfrobot.com/product-2528.html)
3. 1x [Gravity: GNSS Sensor](https://www.dfrobot.com/product-2651.html)
4. 1x [Fermion: I2S MEMS Microphone](https://www.dfrobot.com/product-2637.html)
5. 1x [Fermion: MEMS Smoke Detection Sensor](https://www.dfrobot.com/product-2698.html)
6. 1x [RP2040 LoRa with Type C adapter](https://www.waveshare.com/rp2040-lora.htm?sku=26542)
7. 1x [Li-Po Battery](https://techiesms.com/product/1500mah-3-7v-li-po-battery/)
8. 1x [70x70mm Solar Panel](https://techiesms.com/product/mini-epoxy-solar-panel-70x70-mm/)
9. 8x [M3x10mm Screws](https://www.dfrobot.com/product-841.html)

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S2.JPG?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=228ccf219e738115bb25eee2c6034f4b" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S2.JPG" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S3.JPG?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=fbf8806e0234af6cdc6d62bf81f80819" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S3.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S4.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=9d433a3936ab0e778d2fde55a23125ab" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S4.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S5.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=1ac09fe66fdbbaefbd6a59e6058db403" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S5.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S6.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=df2dfa73a37d1d776281ac3ceb5bd43a" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S6.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S7.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=8c86a7da1228d15fa119ae0038cd1120" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S7.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S8.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=789bb4bf43f3a78c144b4bbc4d7260c7" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S8.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S9.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=c8a8fd2e7655913e4db83e1cbe13971d" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S9.JPG" />

**Components For 1x Gateway Unit:**

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S11.JPG?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=477a23a587bd1a5f7f7784f606d6340e" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S11.JPG" />

1. 1x [Arduino Uno R4 WiFi](https://www.dfrobot.com/product-2700.html)
2. 1x [Fermion: 3.5” 480x320 TFT LCD Display](https://www.dfrobot.com/product-2107.html)
3. 1x [RP2040 LoRa](https://www.waveshare.com/rp2040-lora.htm?sku=26591)
4. 1x [Li-Po Battery](https://techiesms.com/product/1500mah-3-7v-li-po-battery/)
5. 1x [Micro Push Switch](https://www.amazon.com/mxuteuk-Self-Lock-Flashlight-Latching-BK-1208/dp/B086L1WKS3/ref=sr_1_15?crid=36ZOJ9SAIUDS0\&dib=eyJ2IjoiMSJ9.zm2b2eGNCSReGFJuUskv691lpV2tKav6uBLD27VVQZMyCwOMFkUlSbVOTXYy8ZJ7sTGnHgZrt-GpoDlQVplkeHCifur1phAdvndooU-V66zX0g_hdhhLXgztJ8bIVIyqPl8ik91KUjabhdjp9jxUN-TDC53s5StBHNUGw6unWKcd0S0PpCw9AoKzz_joMJNHuyrrl6J_D10sxRjwTmIt6aWTpA_OO-uo6OCelqsNgpw.n93ojHC0ZUD9pckHoKxtWmC_pw6ioAxpVLO76BloI1Q\&dib_tag=se\&keywords=mini%2Bswitch\&qid=1757991302\&sprefix=mini%2Bswitc%2Caps%2C464\&sr=8-15\&th=1)
6. 4x [M2x5mm Screws](https://www.amazon.com/4mm-6mm-10mm-12mm-16mm/dp/B0B93G1H9L/ref=sr_1_1_sspa?crid=2GR42NYXUIMID\&dib=eyJ2IjoiMSJ9.Xe3zLQ7GMbVX4e9UdWnn10jmwVZbrhtrPgqKBL6jyA9giwWnMO_syicAVx0SqjwmyQ3S8ZBgPyBJd7m30o0efQgCu5xpCBUaLdX6_Yr3DZ7eUbAJUxp3BYhjcgL-8RxRY0Uk7VQafZPhQh9Sg9Nxg1LvrvByA1wrTKX4yInN41Ve31AoRWz2lgZMABQR8o6QY-KltVrHKGda8fx43bDSc9X-By4T010KSPjlOLZuI84.2DMZxvKbVecFjM3DbGS6Nj-fDLEpk5pngZRohIU-xzk\&dib_tag=se\&keywords=M2%2Bscrews\&qid=1757991555\&sprefix=m2%2Bscre%2Caps%2C533\&sr=8-1-spons\&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY\&th=1)
7. 1x 3V Buzzer

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S12.JPG?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=c8aabb136de149642395194d078800f5" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S12.JPG" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S13.JPG?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=ff1790f7f847f94cf3c30423a64aba2a" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S13.JPG" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S14.JPG?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=f08c1fbf34f3f83a449790bc404d3d11" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S14.JPG" />

**Tools**

1. 3D Printer (for enclosures and mounting parts)
2. Soldering Kit (iron, solder wire, flux, wick)
3. Screwdriver Kit (for M2/M3 hardware)

## Step 1: PCB Design

<img src="https://mintcdn.com/edgeimpulse/GfuP4tH_LMl5IjE-/.assets/images/forest-guard-esp32/PD2.JPG?fit=max&auto=format&n=GfuP4tH_LMl5IjE-&q=85&s=4dfaae1f58ae05e193f1ab3650717828" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/PD2.JPG" />

Designing the **Forest Guard PCB** was the very first milestone in this project.

I am not a professional PCB designer, but with hands-on experience in electronics and by studying references from existing **ESP32-S3 development boards**, I created a **custom PCB** in **EasyEDA** that integrates:

1. ESP32-S3 as the main controller
2. Battery management and charging circuit
3. Type-C USB for programming/power
4. Headers for plugging in LoRa module and sensors

The PCB design files (Gerber + BOM) are available on my GitHub repository:

👉 [Forest-Guard GitHub Repository](https://github.com/MukeshSankhla/Forest-Guard)

To bring this design to life, I got **5× PCBs fabricated** and **2× fully assembled boards** (with SMD assembly for ESP32-S3, battery & power management, Type-C, etc.) manufactured by **NextPCB**. The sensors and LoRa modules are later mounted as through-hole or header components.

This combination gave me the flexibility to test multiple prototypes, while the assembled PCBs saved me time and ensured **professional quality soldering of fine-pitch SMD parts**.

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/TXschematic.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=698695033bfa0794dbbc52b7cc71aeb8" alt="" width="1652" height="1169" data-path=".assets/images/forest-guard-esp32/TXschematic.png" />

<img src="https://mintcdn.com/edgeimpulse/GfuP4tH_LMl5IjE-/.assets/images/forest-guard-esp32/PCB0.png?fit=max&auto=format&n=GfuP4tH_LMl5IjE-&q=85&s=70acce799cd5d1eee9301ce1a87659e0" alt="" width="1918" height="959" data-path=".assets/images/forest-guard-esp32/PCB0.png" />

<img src="https://mintcdn.com/edgeimpulse/GfuP4tH_LMl5IjE-/.assets/images/forest-guard-esp32/PCB1.png?fit=max&auto=format&n=GfuP4tH_LMl5IjE-&q=85&s=0d05604d0349c1a3ae8398d7ec9309a9" alt="" width="938" height="836" data-path=".assets/images/forest-guard-esp32/PCB1.png" />

<img src="https://mintcdn.com/edgeimpulse/GfuP4tH_LMl5IjE-/.assets/images/forest-guard-esp32/PCB2.png?fit=max&auto=format&n=GfuP4tH_LMl5IjE-&q=85&s=078a338187452fa43dff833c15c70102" alt="" width="970" height="839" data-path=".assets/images/forest-guard-esp32/PCB2.png" />

<img src="https://mintcdn.com/edgeimpulse/GfuP4tH_LMl5IjE-/.assets/images/forest-guard-esp32/PD0.JPG?fit=max&auto=format&n=GfuP4tH_LMl5IjE-&q=85&s=898af0b272ecc803d96ae32289c6ff27" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/PD0.JPG" />

<img src="https://mintcdn.com/edgeimpulse/GfuP4tH_LMl5IjE-/.assets/images/forest-guard-esp32/PD1.JPG?fit=max&auto=format&n=GfuP4tH_LMl5IjE-&q=85&s=6a791591f824793db2ecb784996d7b1e" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/PD1.JPG" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/PD3.JPG?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=e59089600ea644a5318ae20507f706ce" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/PD3.JPG" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/PD4.JPG?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=8b310eb51d192a949b6d4e54a118a8ff" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/PD4.JPG" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/PD5.JPG?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=7336b44b61125fe7c2ac16f789e96f02" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/PD5.JPG" />

## Step 2: Meshtastic Setup on RP2040 LoRa

We’ll flash the Meshtastic firmware onto the RP2040 LoRa modules and configure them for **UART communication**.

⚠️ **Important Safety Note**:

Always connect the **antenna before powering on** the LoRa module to prevent damage.

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S21.JPG?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=4f0db43446fc495abb2f0c649d09fd71" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S21.JPG" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S22.JPG?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=16b94273982a9337a871e07004565fb0" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S22.JPG" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S23.JPG?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=8060db80eccb745f7337016ee906f0f1" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S23.JPG" />

**1. Flashing Meshtastic Firmware**

1. Go to [Meshtastic Downloads](https://meshtastic.org/downloads/).
2. Click **Go to Flasher**.
3. Select **Target Device: RP2040 LoRa**.
4. Choose a version → click **Flash** → then **Continue**.
5. Download the **.UF2 firmware file**.

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S24.png?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=311cd705377111e153fadd33d6648f12" alt="" width="1916" height="994" data-path=".assets/images/forest-guard-esp32/S24.png" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S25.png?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=5d006a0801dbb75edbc0d9c04c2f7572" alt="" width="1919" height="962" data-path=".assets/images/forest-guard-esp32/S25.png" />

**2. Upload Firmware to RP2040**

1. Press and hold the **BOOT** button on the module.
2. While holding BOOT, connect the **USB Type-C** cable to your PC.
3. A new drive named **RP2** will appear.
4. Copy the downloaded **.UF2 file** into the RP2 drive.
5. Once copied, press the **RESET** button.
6. The device will reboot with the new firmware.

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S26.png?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=c43e2b6f3ebda85aef1bac875f30e6bf" alt="" width="1729" height="827" data-path=".assets/images/forest-guard-esp32/S26.png" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S27.png?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=0252446b21d5526cb28298af44fbe88f" alt="" width="1536" height="913" data-path=".assets/images/forest-guard-esp32/S27.png" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S28.png?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=c3bcb3917bddf01f0088e22686630c89" alt="" width="951" height="858" data-path=".assets/images/forest-guard-esp32/S28.png" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S29.png?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=2dff5c8c10ca6ce7ce12fa4ca41aec18" alt="" width="1153" height="853" data-path=".assets/images/forest-guard-esp32/S29.png" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S211.png?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=7b3b504258e4f88863b4f4abbbc2916a" alt="" width="1432" height="875" data-path=".assets/images/forest-guard-esp32/S211.png" />

**3. Connect to Meshtastic Client**

1. Open [Meshtastic Client](https://client.meshtastic.org/).
2. Click **New Connection**.
3. Select **Serial**.
4. Click **New Device** → choose the COM port where your module is connected.
5. You should now see the **Meshtastic Node Page**.

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S212.png?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=b257f8d5c7529f4856202363064ecec8" alt="" width="1918" height="997" data-path=".assets/images/forest-guard-esp32/S212.png" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S213.png?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=88dd3e2d310f7c6557e1b7b1b5af0f76" alt="" width="1918" height="993" data-path=".assets/images/forest-guard-esp32/S213.png" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S214.png?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=7fac0815f4b33b8d8f76420c175a948d" alt="" width="648" height="531" data-path=".assets/images/forest-guard-esp32/S214.png" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S215.png?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=c9da5be5a72202eb7221f924dc15d1a5" alt="" width="1918" height="963" data-path=".assets/images/forest-guard-esp32/S215.png" />

**4. Configure LoRa Region**

1. Go to **Config → LoRa**.
2. Set the **Region** according to your country’s LoRa regulations.

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S216.png?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=96221b9d6fbcdb0d46539c7c2010e4cb" alt="" width="1918" height="960" data-path=".assets/images/forest-guard-esp32/S216.png" />

**5. Configure Serial UART**

1. Go to **Module Config → Serial**.
2. Enable **Serial Output**.
3. Set pins:
4. **Receive Pin (RX): 8**
5. **Transmit Pin (TX): 9**
6. Save by clicking the **top-right save button**.

This configures the module to communicate via **UART** with external devices.

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S217.png?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=348598ad87047bb7e9849d6ec2aadab7" alt="" width="1918" height="961" data-path=".assets/images/forest-guard-esp32/S217.png" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S218.png?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=7fd7e4057e88dcfdec3a05d8a4b18fac" alt="" width="1256" height="806" data-path=".assets/images/forest-guard-esp32/S218.png" />

**6. Repeat for All Modules**

Repeat the above steps for every LoRa module you plan to use in your project.

## Step 3: PCB Assembly

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S31.JPG?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=7926b4a0a1e823b88c15670c3f40704d" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S31.JPG" />

With the custom PCB manufactured, the next step is to carefully solder the sensor modules and communication hardware onto the board.

**Components to Solder**

1. Gravity: Multifunctional Environmental Sensor
2. Fermion I²S MEMS Microphone
3. Fermion MEMS Smoke Detection Sensor
4. RP2040 LoRa Module with Type-C Adapter

**Prepare the Workspace**

1. Use a clean, static-free surface.
2. Preheat your soldering iron to around **350 °C** (for leaded solder) or **370–380 °C** (for lead-free).
3. Have tweezers and flux ready to handle small pins.

**Solder Components One by One**

1. Begin with the **smallest modules** (sensors) first MEMS microphone and Smoke sensor..
2. Than carefully align the Environmental sensor and solder the I²C pins.
3. Finally, solder the **LoRa module.**
4. Double-check pin alignment before applying solder. Incorrect orientation can damage the modules.

**Continuity Testing**

1. After soldering each module, use a **multimeter in continuity mode**.
2. Probe between the module pin and the corresponding PCB pad/trace.
3. A beep or zero-resistance confirms proper connectivity.

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S32.JPG?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=8bace263e162617f5515c2105cf3e7bb" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S32.JPG" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S33.JPG?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=6a11c41282a2495a70bf9852cace1eb1" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S33.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S34.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=49ea486ddb9883a8a884f02cea1d03ea" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S34.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S35.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=2ddb755f59831a8b8cc510f4b9b8b9d2" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S35.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S36.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=a459e5cbba8f0f00b02c0b41504df1a3" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S36.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S37.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=4f89fdc9f310fa2d346e2c06ba707975" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S37.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S38.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=f5573d88eb4719469ff37834e0e1b7ed" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S38.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S39.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=159bad4523304f0c2564d82935bee975" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S39.JPG" />

## Step 4: Node CAD Design and 3D Printing

<img src="https://mintlify.s3.us-west-1.amazonaws.com/edgeimpulse/.assets/images/forest-guard-esp32/design.gif" alt="Demo animation" />

To make the **Forest Guard Node** truly field ready, I designed a custom **enclosure** in **Fusion 360**. This was done by first importing all the standard components and then exporting the PCB 3D model from EasyEDA into Fusion 360, ensuring that every cutout and mount point lined up perfectly.

**Enclosure Features**

The Node enclosure is made up of multiple parts:

1. **Housing** - Holds the custom PCB, with cutouts for the Type-C port, push switch, and top-mounted LoRa antenna. A large center cutout allows light from the onboard RGB LED to pass through.
2. **Diffuser** - A dedicated piece that diffuses the RGB LED light, making it visible in the field without being harsh.
3. **Cover** - Designed to mount the solar panel on top and provide space for the GNSS sensor.
4. **Mount & Clip Set** - Allows the node to be attached securely to trees, walls, or other structures.

The enclosure is secured with **12× M3 screws**, giving it the feel and robustness of a professional product enclosure.

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/TXCAD1.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=7f7b5fd215f5a0d7e0850d326aee2989" alt="" width="2048" height="1536" data-path=".assets/images/forest-guard-esp32/TXCAD1.png" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/TXCAD2.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=9bfe79b6a2ed09e7342db7955ad6008f" alt="" width="2048" height="1536" data-path=".assets/images/forest-guard-esp32/TXCAD2.png" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/TXCAD3.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=253f832f09a5009542f3f3aa524c5263" alt="" width="1922" height="727" data-path=".assets/images/forest-guard-esp32/TXCAD3.png" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/TXCAD4.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=c8d043bdee3aa23c3c5a3b3e250f3c32" alt="" width="1922" height="727" data-path=".assets/images/forest-guard-esp32/TXCAD4.png" />

**3D Printing**

<img src="https://mintcdn.com/edgeimpulse/GfuP4tH_LMl5IjE-/.assets/images/forest-guard-esp32/P1.JPG?fit=max&auto=format&n=GfuP4tH_LMl5IjE-&q=85&s=84371111e127670403448a4f987ec3a3" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/P1.JPG" />

<img src="https://mintcdn.com/edgeimpulse/GfuP4tH_LMl5IjE-/.assets/images/forest-guard-esp32/P2.JPG?fit=max&auto=format&n=GfuP4tH_LMl5IjE-&q=85&s=3aa30b82f528b74fb19b1c528aff6d2f" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/P2.JPG" />

<img src="https://mintcdn.com/edgeimpulse/GfuP4tH_LMl5IjE-/.assets/images/forest-guard-esp32/P3.JPG?fit=max&auto=format&n=GfuP4tH_LMl5IjE-&q=85&s=7803e8cd0d0331791c175b6b9c4d56ed" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/P3.JPG" />

<img src="https://mintcdn.com/edgeimpulse/GfuP4tH_LMl5IjE-/.assets/images/forest-guard-esp32/P7.JPG?fit=max&auto=format&n=GfuP4tH_LMl5IjE-&q=85&s=a0203e2b77f5c3d1acbbe14d3bff02cd" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/P7.JPG" />

I printed the parts on a **Bambu Labs P1S** 3D printer:

1. Housing and cover were printed in **light gray** PLA for durability and aesthetics.
2. Diffuser was printed in **pure white** PLA to achieve soft light diffusion from the RGB LED.

**Files for You**

1. **STL files** - Ready-to-print files for direct 3D printing.
2. **Fusion 360 design file** - For anyone who wants to modify or customize the design further.

#### [Forest Guard Tx Fusion 360 File](https://a360.co/4nuH8am)

## Step 5: Diffuser and Light Visor Assembly

To make the **RGB LED indicator** and **environmental sensor light input** effective, we add a **diffuser** and a **light visor** to the node housing. This ensures the LED glow is soft and visible in the field, while the environmental sensor gets accurate light readings without interference.

**Parts Needed**

1. Housing
2. Diffuser
3. Small piece of clear plastic (cut from packaging or acrylic sheet)
4. Quick glue (super glue or instant adhesive)

**Attach the Diffuser**

1. Apply a thin line of quick glue around the **Diffuser cutout** in the housing.
2. Carefully snap the **diffuser** into place as shown (it should align flush with the cutout).
3. Hold gently for a few seconds until the glue sets.

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S51.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=bffdc7e4e156f6cf257caf82d2865f1d" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S51.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S52.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=c171aa4cb59fafe1d1d850318c4570f6" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S52.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S53.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=9290fd464379668e2d64da9108b87d9f" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S53.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S54.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=d5426e9caed740be81bad53a5d7ceabd" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S54.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S55.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=4f859489c36408a5eb7e8e6d043916e3" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S55.JPG" />

**Install the Clear Plastic Visor**

1. Locate the **cutout for the Environmental Sensor light input**.
2. Apply a small amount of quick glue around the edges of this cutout.
3. Place the **clear plastic piece** over the opening. This acts as a protective window and ensures correct light transmission for the sensor.

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S56.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=6fbe978eb3d9bf2dcfd794a0676b1556" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S56.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S57.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=38b5c96625ee86a9e8ca24c47107738f" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S57.JPG" />

## Step 6: Solar Wire Soldering

1. Cut **two wires**, each about **10 cm** long (one **red**, one **black**).
2. Solder the **red wire** to the **+ pad** on the back of the battery connector.
3. Solder the **black wire** to the **– pad**.

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S61.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=7002ab2232f713d711fa8e947245e044" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S61.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S62.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=b4a98fe5b13979bd6a4fe81872ad12af" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S62.JPG" />

## Step 7: Housing Assembly

1. Take the **assembled PCB**, **housing**, **battery**, and the **LoRa antenna**.
2. First, **connect the antenna** to the LoRa module.
3. ⚠️ *Never power on without the antenna connected.*
4. Connect the **battery** to the PCB.
5. Place the PCB inside the housing, aligning the **Type-C port** with the cutout.
6. Secure the PCB using **4× M3 screws**.
7. Unscrew the antenna, pass it through the **top housing hole**, and screw it back in place.
8. Finally, use **double-sided tape** to fix the battery to the back of the PCB.

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S71.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=21df3ec45a6a291931016d006056816f" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S71.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S72.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=c860b2b986c18dcfb9f0091ab46b2f1d" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S72.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S73.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=78239592af07dda6985164c7b0646620" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S73.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S74.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=cda83c5a3116b3441f7a453dd99c7261" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S74.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S75.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=90cd74767e61039dfba38049f106d81a" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S75.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S76.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=b20b0eedc7149edaa7b80c507eae1f1a" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S76.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S77.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=946554f4e47ca75b95a05491a65e684e" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S77.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S78.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=b24ef3885037ec6875e54e84127c1aa8" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S78.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S79.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=41a365498edcc921d26b0c33540a8174" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S79.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S711.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=8ec36f6330f086dedc1518c74709a869" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S711.JPG" />

## Step 8: Solar Panel Assembly

1. Take the **solar panel**, **cover**, and **quick glue**.
2. Align the solar panel with the **cutout on the cover** and snap it into place.
3. From the **back side of the cover**, locate the four holes.
4. Apply a small amount of **quick glue** into each hole to secure the panel firmly.
5. Let it sit for a few minutes to allow the glue to set fully.

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S81.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=e6bc805f2e9edb1660ea9ea824856b0e" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S81.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S82.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=54c1ca619d4df20bece0fea3d264bca9" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S82.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S83.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=fe35411865664899db155bc1429001d6" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S83.JPG" />

## Step 9: Cover Assembly

1. Take the **cover** and the **GNSS sensor module**.
2. Connect the **GNSS antenna** to the GNSS module.
3. Place the module over the **mounting holes** on the cover.
4. Secure the module using **4× M3 screws**.
5. Use **double-sided tape** to secure the antenna on the cover so it stays in place.

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S92.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=70c13b61dc6436edc72ada535244ab97" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S92.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S92.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=70c13b61dc6436edc72ada535244ab97" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S92.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S93.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=b84f94094e9793da15dd9938cb530503" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S93.JPG" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/S94.JPG?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=cdc4b080175686dc2e22bf7448387cf4" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S94.JPG" />

## Step 10: Final Connections

Take the **Housing Assembly** and the **Cover Assembly**.
Use the **4-pin connector** that came with the GNSS sensor:

1. Cut the connector in half using a cutter.
2. Plug one side into the GNSS sensor.
3. Strip the wires on the other side and solder them to the PCB as follows:
   * **Red to 3V3**
   * **Black to GND**
   * **Green to SDA**
   * **Blue to SCL**

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S101.JPG?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=c575d8c9364ae7e0bce8d63abb500e40" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S101.JPG" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S102.JPG?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=69648519e31806bb07fbf3974ee667d2" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S102.JPG" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S103.JPG?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=417807bd61d2f5ce9ac7d968e46f253c" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S103.JPG" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S105.JPG?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=2b7d4cad2efeb307553f472111e93017" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S105.JPG" />

Now connect the **solar wires** coming from the PCB to the solar panel:

* **Black to -Ve**
* **Red to +Ve**

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S106.JPG?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=5b77fb26cdfb8fca8cc1e8cee905d085" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S106.JPG" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S104.JPG?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=652780d7f58f5ad9f90d75631f20cc70" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S104.JPG" />

Double-check all connections before powering on.

## Step 11: Final Assembly

1. Take the **assembled housing** and the **assembled cover**.
2. Carefully align the cover on top of the housing.
3. ⚠️ Make sure **no wires get pinched** during this step.
4. Once aligned, snap the cover into place.
5. Use **4× M3 screws** to securely fasten the cover to the housing.
   Now your **Forest Guard Node** is fully assembled and ready for field testing!

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S111.JPG?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=03f79c2abfdd187c0f2357272140b4c1" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S111.JPG" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S112.JPG?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=d6eae5c84a5332706d0679695521cf96" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/S112.JPG" />

## Step 12: Pre-Requisite to Program Node (Edge Impulse)

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/ST111.png?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=1944aa51b23174331056512ae36455c2" alt="" width="1354" height="845" data-path=".assets/images/forest-guard-esp32/ST111.png" />

Before uploading the **final Node firmware**, we need to prepare the **machine learning (ML) model** that runs locally on the ESP32-S3. This is done using **Edge Impulse**, a powerful platform for developing and deploying ML models directly to embedded devices.

### What is Edge Impulse?

Edge Impulse is an **edge AI development platform** that makes it simple to:

1. Collect and label sensor data (audio, vibration, environmental, camera, etc.).
2. Train ML models using classical algorithms or neural networks.
3. Optimize models for low-power microcontrollers like ESP32, RP2040, and STM32.
4. Generate ready-to-use **Arduino libraries** that can be imported directly into your Node firmware.

This enables us to bring AI directly to the forest, without needing internet access or cloud inference — the model runs **entirely on the Node itself**.

### Audio Classification for Gunshot Detection

For this project, we focus on **audio classification** using the onboard MEMS microphone:

**Data Collection**

1. Record short audio clips of **gunshots** and **background forest sounds** (wind, birds, insects, etc.).
2. Upload these samples into your Edge Impulse project.

**Feature Extraction**

1. Edge Impulse automatically converts raw audio into **spectrograms (MFCCs)**, which represent the frequency patterns of the sound.
2. This allows the model to detect unique signatures of gunshot sounds compared to other noises.

**Model Training**

1. A **classification model** is trained to output labels like:
2. "gunshot"
3. "background"
4. The model learns the difference in frequency and amplitude patterns.

**Deployment**

1. Once trained and tested, export the model as an **Arduino library**.
2. Include this library in your Node code.
3. The ESP32-S3 runs the inference on its second core, ensuring real-time classification without blocking sensor updates or LoRa communication.

### Why This Matters

This setup means that every Node becomes an **intelligent sentinel**:

1. Capable of **hearing gunshots** in the forest.
2. Making real-time decisions without cloud dependency.
3. Sending alerts through the LoRa mesh instantly.

And importantly, this is just the beginning — with Edge Impulse, you can retrain the model on other audio events like **chainsaws (illegal logging)** or **calls of endangered animals**, making the Forest Guard system highly **adaptable and future-proof**.

### Create Edge Impulse Project

To train and deploy your ML model, you first need to set up a project in **Edge Impulse Studio**.

**Create a Project**

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/ST112.png?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=bc79744570d20e01c23b7936d94132d4" alt="" width="1919" height="934" data-path=".assets/images/forest-guard-esp32/ST112.png" />

1. Open [Edge Impulse Studio](https://studio.edgeimpulse.com/).
2. **Login** with your account credentials.
3. Click on **“Create New Project”**.
4. Give your project a meaningful name, e.g., *Forest Guard Gunshot Detector*.

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/ST113.png?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=7f41e77ee63c64510695337d5d32d167" alt="" width="1919" height="928" data-path=".assets/images/forest-guard-esp32/ST113.png" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/ST114.png?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=8c0b829a63e1af134cdc2f5f09ee3c20" alt="" width="1918" height="926" data-path=".assets/images/forest-guard-esp32/ST114.png" />

**Get Your Project Key**

1. After the project is created, go to **Dashboard → Keys**.
2. Locate your **Project API Key**.
3. Copy this key and keep it handy — you’ll need it in the Flask tool and Node code to connect data and models to Edge Impulse.

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/ST115.png?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=9f4e980baed5296bfed1562c77425960" alt="" width="1915" height="935" data-path=".assets/images/forest-guard-esp32/ST115.png" />

## Step 13: Challenge to Collect Data

One of the biggest hurdles when working with **Edge Impulse** is data collection, especially for **audio** and **image** inputs. While numeric sensor streams (like temperature or humidity) can be pushed directly via serial, Edge Impulse currently doesn’t allow us to easily stream **raw audio** or **image frames** from the ESP32 to their platform in the same fast-forward way.

This means we normally have to:

1. Log data to an **SD card**.
2. Remove the card.
3. Copy files to the computer.
4. Upload them manually to Edge Impulse.

This process quickly becomes tedious when collecting **hundreds of samples**.

### My Solution: Flask Data Uploader

To make this seamless, I built a **Flask-based desktop tool** that bridges the ESP32 and Edge Impulse:

**ESP32 Data Firmware**

1. First, flash a simple Arduino sketch onto the ESP32 that streams audio (from the microphone) or images (from a camera) over **Serial USB**.

**Flask App**

1. On the PC side, run my **Flask tool**.
2. It listens to the ESP32’s serial port and captures the incoming raw data.
3. Using your **Edge Impulse API key**, the tool automatically uploads this data into your project.

**Benefits**

1. No need for SD cards or manual file transfers.
2. Data is organized and labeled as it’s uploaded.
3. Faster iteration when training models with new samples.

## Step 14: ESP32 Audio Serial Code

Before we can collect and upload audio samples into Edge Impulse, we need the ESP32-S3 to **stream raw microphone data** over Serial USB. This is done by flashing a small Arduino sketch that continuously records from the I²S microphone and sends the audio buffer to the PC.

**Install the ESP32 Board Package (Board Manager)**

1. Open **Arduino IDE → File → Preferences**.
2. In **Additional Boards Manager URLs**, add:

[https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package\_esp32\_index.json](https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json)

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/ST121.png?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=07108121f3b902883b8c3c8e155918ac" alt="" width="856" height="550" data-path=".assets/images/forest-guard-esp32/ST121.png" />

3. Click **OK**.
4. Go to **Tools → Board → Boards Manager…**.
5. Search **“ESP32”** and install **esp32 by Espressif Systems** (latest).

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/ST122.png?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=fd04dafdfe4baed3066cf5d7fbbab534" alt="" width="1286" height="754" data-path=".assets/images/forest-guard-esp32/ST122.png" />

> Tip: After install, restart Arduino IDE if the boards list doesn’t refresh.

1. Open the provided esp32\_audio\_serial.ino sketch into Arduino IDE.
2. This code initializes the microphone, records a buffer, and streams it line-by-line over Serial.
3. Inside the sketch, you’ll see a configurable parameter:

```cpp  theme={"system"}
constexpr int SECONDS_TO_GRAB = 10;
```

Change this value if you want longer or shorter recordings.

Default is **10 seconds** per sample.

1. Go to **Tools → Board → ESP32 → DFRobot FireBeetle 2 ESP32-S3**.
2. Connect your ESP32-S3 to the PC with USB-C.
3. Under **Tools → Port**, choose the correct COM port.
4. Under Tools **→ USB CDC On Boot → Enable**
5. Click **Upload** to flash the code onto your ESP32-S3.

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/ST123.png?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=b4aa14596cd9d89d62b5154402cb4d5b" alt="" width="1245" height="972" data-path=".assets/images/forest-guard-esp32/ST123.png" />

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/ST124.png?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=f7d19c1117e99f6c3379310dbe4e1abf" alt="" width="1915" height="1009" data-path=".assets/images/forest-guard-esp32/ST124.png" />

## Step 15: Run Flask Tool

Now that your ESP32-S3 is streaming microphone data over Serial, let’s use the **Flask Data Tool** to capture it and upload directly into your Edge Impulse project.

**Setup the Flask Tool**

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/ST133.png?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=0eeeef29194f0de2947e8c8a0c7f3d30" alt="" width="1286" height="813" data-path=".assets/images/forest-guard-esp32/ST133.png" />

1. Download the project repository:
2. 👉 [Forest-Guard GitHub Repository](https://github.com/MukeshSankhla/Forest-Guard/)
3. Open the **Edge Impulse Data Tool** folder.
4. Run the Flask app:

```
python app.py
```

(File path: Edge Impulse Data Tool/app.py)

**Access the Web Interface**

1. Once the server is running, open your browser and go to:
   [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
2. You will see the **data collection dashboard**.

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/ST131.png?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=359f751c0601c003e6d392f6384242eb" alt="" width="1919" height="995" data-path=".assets/images/forest-guard-esp32/ST131.png" />

**Collect Audio Data**

1. **Select COM Port** → Choose the port where your ESP32 is connected.
2. **Paste API Key** → Enter your Edge Impulse **project API key** (from Step 14).
3. **Choose Mode** → Select whether this sample is for **training** or **testing**.
4. **Enter Label** → e.g., gunshot or background.
5. **Select Data Type** → Choose **Audio**.
6. **Click Capture** → Recording will begin.
7. The **Node LED will glow green** while audio is being recorded.
8. Once the LED turns off, the captured audio file is automatically uploaded to your Edge Impulse project.

You should now see your labeled audio samples appear inside the **Edge Impulse Studio → Data Acquisition** tab. From here, you can repeat the process to build up your dataset of gunshots and background noise.

<img src="https://mintcdn.com/edgeimpulse/L2EIDTstX9ynB0g2/.assets/images/forest-guard-esp32/ST132.png?fit=max&auto=format&n=L2EIDTstX9ynB0g2&q=85&s=f8bc02e9afb91cbafcdba35972cbee52" alt="" width="1916" height="932" data-path=".assets/images/forest-guard-esp32/ST132.png" />

## Step 16: Collect Data

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST161.png?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=18ed38ce01e816583e4329e59183583d" alt="" width="1918" height="960" data-path=".assets/images/forest-guard-esp32/ST161.png" />

Now that the Flask tool is ready and connected to Edge Impulse, it’s time to build our **training dataset**. A good dataset is the most important factor for achieving a reliable classification model.

**Collect Background Noise Data**

1. Set the **label** flag to **Noise**.
2. Start recording samples in different environments:

* **Indoors** → quiet rooms, fan noise, people talking.
* **Outdoors** → wind, birds, insects, cars, etc.

3. Collect at least **120 seconds of audio** in each scenario.
4. The more variety, the better the model can tell background noise apart from gunshots.

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST162.png?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=1b3cff13f06d61d7e95a9f6252cc2758" alt="" width="1916" height="958" data-path=".assets/images/forest-guard-esp32/ST162.png" />

**Collect Gunshot Data**

1. Set the **label** flag to **Gun**.
2. Play **different gunshot audio samples** (different calibers, environments, echo levels).
3. Record up to **120 seconds** of audio in total.

Using multiple gunshot sound samples with slightly different characteristics helps the model generalize better to real-world scenarios.

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST163.png?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=76be05b3fd92365cc1e7991859a986f4" alt="" width="1915" height="959" data-path=".assets/images/forest-guard-esp32/ST163.png" />

**To make sure the model is reliable:**

1. Split your dataset **80:20** → 80% for **training**, 20% for **testing**.
2. Edge Impulse automatically suggests the split, but you can also move samples manually if needed.

**Tips for Better Results**

1. Collect data at **different volumes and distances**.
2. Try to balance the number of Noise and Gunshot samples.
3. Keep background data diverse - this prevents false positives.

## Step 17: Split Data

Right now, each recorded audio sample is **10 seconds long**. For better accuracy, we need to **split these into smaller 1-second samples** that can be used as training features in Edge Impulse.

**Splitting Process in Edge Impulse**

1. In **Edge Impulse Studio**, go to the **Data Acquisition** tab.
2. Find one of your **10-second audio samples** (either Noise or Gunshot).
3. Click on the **three dots (…) menu** next to the sample.
4. Choose **Split Sample**.
5. Use the tool to crop each segment into **1-second chunks**.
6. Example: a 10-second audio file becomes **10× 1-second samples**.
7. For gunshot recordings, isolate the exact segment of the shot to ensure the model learns the event clearly.
8. Click **Split** to save.

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST172.png?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=aebc933a9a2e52a739a8aa8c5648e1dd" alt="" width="1916" height="961" data-path=".assets/images/forest-guard-esp32/ST172.png" />

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST171.png?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=b761f6c59728a7532f4374e3e0a07ed4" alt="" width="1189" height="756" data-path=".assets/images/forest-guard-esp32/ST171.png" />

## Step 18: Create Impulse

With your dataset ready and split into 1-second audio clips, the next step in Edge Impulse is to **design the impulse**, the pipeline that converts raw audio into features, and then trains a classification model.

**Create a New Impulse**

1. In **Edge Impulse Studio**, go to the **Create Impulse** tab.
2. Set the **Window Size** and **Frequency** as shown in the reference image (these define how much audio is processed in each slice and at what sample rate).

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST181.png?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=903832b62a203fa9928984e71d6f0a1f" alt="" width="1918" height="962" data-path=".assets/images/forest-guard-esp32/ST181.png" />

**Add Blocks**

1. **Processing Block:** Select **Audio (MFCC)**.
2. MFCC (Mel-Frequency Cepstral Coefficients) transforms raw sound waves into a spectrogram — a compact representation of sound patterns that the ML model can learn from.
3. **Learning Block:** Select **Classification**.
4. This will train a neural network to classify between labels like Gunshot and Noise.

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST182.png?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=6be1584077e5f774780dd780db2d331c" alt="" width="1917" height="961" data-path=".assets/images/forest-guard-esp32/ST182.png" />

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST183.png?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=b25eb24f45faa1c69a9fa31fe776c434" alt="" width="1916" height="962" data-path=".assets/images/forest-guard-esp32/ST183.png" />

**Save the Impulse**

1. Once both blocks are added and configured, click **Save Impulse**. This locks in the pipeline that will be used in the next steps for feature extraction and training.

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST184.png?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=9791ace26fececba69e0d4a24830041b" alt="" width="1917" height="963" data-path=".assets/images/forest-guard-esp32/ST184.png" />

## Step 19: Generate Features

Now that the impulse is created, we need to **extract features** from our audio samples. This is the process that converts raw sound into meaningful patterns (MFCCs) that the classifier can learn from.

1. In **Edge Impulse Studio**, go to the **MFCC** block (under *Impulse Design*).
2. Click **Save Parameters** to confirm the default MFCC settings.

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST191.png?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=22f07f43f01fd37439178a89692a8f65" alt="" width="1914" height="959" data-path=".assets/images/forest-guard-esp32/ST191.png" />

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST192.png?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=355c4c1dcb26922f2cc4148733a0d199" alt="" width="1917" height="960" data-path=".assets/images/forest-guard-esp32/ST192.png" />

3. Press **Generate Features**.

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST193.png?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=39105aca2cd47a1377a7a1334076cbda" alt="" width="1919" height="960" data-path=".assets/images/forest-guard-esp32/ST193.png" />

4. Edge Impulse will now process all your audio samples.
5. This step can take a few minutes depending on dataset size.
6. Once finished, you’ll see a **Feature Explorer graph** on the right side of the screen.
7. Each point on the graph represents a **1-second audio sample**.
8. Samples with similar characteristics (like background noise) will cluster together, while distinct sounds (like gunshots) will form separate groups.
9. Clear separation between Gunshot and Noise clusters is a **good sign** — it means your model will be easier to train accurately.

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST194.png?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=8205fc46d7a939bf1d43f8f347d6e060" alt="" width="1917" height="958" data-path=".assets/images/forest-guard-esp32/ST194.png" />

## Step 20: Train Classification Model

With your features generated, it’s time to train the **Neural Network classifier** that will distinguish between **Gunshot** and **Noise**.

1. In **Edge Impulse Studio**, go to the **Classifier** tab.
2. Click **Save and Train**.
3. Training will take a few minutes depending on dataset size.

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST201.png?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=358c851d689df0bd0408307bca50f043" alt="" width="1916" height="961" data-path=".assets/images/forest-guard-esp32/ST201.png" />

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST202.png?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=bb5fad8889c02a78d2d617d8b04926c9" alt="" width="1915" height="957" data-path=".assets/images/forest-guard-esp32/ST202.png" />

Default training settings usually work well:

1. **Number of training cycles:** 100
2. **Learning rate:** 0.005
3. **Processor:** CPU
4. **Architecture:** 1D Convolutional Neural Network (recommended for audio)

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST203.png?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=b6d0b828a777cbdb714337e0a1d218a5" alt="" width="1916" height="958" data-path=".assets/images/forest-guard-esp32/ST203.png" />

**Results**

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST204.png?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=6a2e7a4d1dc8b0f3c8e826f2232247d7" alt="" width="795" height="582" data-path=".assets/images/forest-guard-esp32/ST204.png" />

Once training is complete, you’ll see:

1. **Accuracy** → \~96% (based on your dataset).
2. **Loss** → around 0.25 (lower is better).
3. **Confusion Matrix** →
4. Gunshot classified correctly \~94% of the time.
5. Noise classified correctly \~100% of the time.

**Metrics** →

1. Precision: 0.97
2. Recall: 0.96
3. F1 Score: 0.96

**On-device performance** →

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST205.png?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=5c82aa48b691444eb0c7fc8d7aed8671" alt="" width="794" height="504" data-path=".assets/images/forest-guard-esp32/ST205.png" />

1. Inferencing time: \~3 ms
2. RAM usage: \~12.5 KB
3. Flash usage: \~45 KB

## Step 21: Build and Download the Model

Once your classifier is trained and performing well, the next step is to **export the model** so it can run directly on your ESP32-S3 Node. Edge Impulse makes this very easy by packaging the trained model into an Arduino-compatible library.

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST211.png?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=15311095bd0f246f6f9806d9b8db62d7" alt="" width="1917" height="958" data-path=".assets/images/forest-guard-esp32/ST211.png" />

1. In **Edge Impulse Studio**, go to the **Deployment** tab.
2. Under **Deployment options**, select **Arduino library**.
3. This will create a .zip library that can be imported into the Arduino IDE.
4. Click **Build**.

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST212.png?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=f63bb745163abaa2dc826377bf0c54fa" alt="" width="1916" height="961" data-path=".assets/images/forest-guard-esp32/ST212.png" />

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST213.png?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=8c9272d5b069f8cf08c1e784676e761e" alt="" width="1916" height="959" data-path=".assets/images/forest-guard-esp32/ST213.png" />

Once the build completes, Edge Impulse will automatically download the library to your computer.

The file will be named something like:

`Forest\_Guard\_Gunshot\_Detector\_arduino-1.0.0.zip`

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST214.png?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=3acdcc0cc0348abf06d7ca6c79f8ab76" alt="" width="1915" height="958" data-path=".assets/images/forest-guard-esp32/ST214.png" />

## Step 22: Arduino Setup

Now that we have our trained Edge Impulse model ready, let’s set up the Arduino IDE with all the required libraries to compile and upload the **Node code**.

**Open the Project**

1. Launch **Arduino IDE**.
2. Open the Node\_V2.ino file (this is the main code for the Forest Guard Node).

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S221.png?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=90fefe6e4f8e1a8cdc314aaae73bc901" alt="" width="1918" height="1034" data-path=".assets/images/forest-guard-esp32/S221.png" />

**Install Required Libraries**

**1. Edge Impulse Model Library**

1. Go to **Sketch → Include Library → Add .ZIP Library…**
2. Select the **.zip** file you downloaded from Edge Impulse in **Step 20**.
3. This adds your custom ML model to the project.

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S222.png?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=4b6e2fbde5fb874e0598f1f7c09f7169" alt="" width="1916" height="1035" data-path=".assets/images/forest-guard-esp32/S222.png" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S223.png?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=3fda6e5994086615a860f65dd0a259e5" alt="" width="1874" height="953" data-path=".assets/images/forest-guard-esp32/S223.png" />

**2. GNSS Library**

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S226.png?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=985bdd470665f626d0ae2f3c04d75f2f" alt="" width="1260" height="794" data-path=".assets/images/forest-guard-esp32/S226.png" />

Download and install the GNSS driver library from DFRobot:

👉 [DFRobot GNSS Library](https://github.com/DFRobot/DFRobot_GNSS)

1. Install it the same way (**Add .ZIP Library**).

**3. Environmental Sensor Library**

Download the library for the multifunction environmental sensor:

👉 [DFRobot Environmental Sensor Library](https://github.com/DFRobot/DFRobot_EnvironmentalSensor)

1. Install it the same way (**Add .ZIP Library**).

**4. NeoPixel Library**

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S225.png?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=e93c1b98c4f24a46a665aded67a1be49" alt="" width="1214" height="743" data-path=".assets/images/forest-guard-esp32/S225.png" />

1. In Arduino IDE, open **Library Manager** (Sketch → Include Library → Manage Libraries…).
2. Search for **Adafruit NeoPixel**.
3. Install the latest version.

## Step 23: Upload the Code

Now that everything is configured, it’s time to **flash the Node firmware** to the ESP32-S3.

**Code Adjustments Before Upload**

Open the Node\_V2.ino sketch in Arduino IDE and check the following user configuration section:

1. **Edge Impulse Include**
2. Change the `#include <...inferencing.h>` line to match the filename of the model you downloaded in **Step 20**.
3. Example:

```cpp  theme={"system"}
#include <Forest_Guard_Gunshot_Detector_inferencing.h>
```

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S224.png?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=924d917b557013fd47e845429ceb0f85" alt="" width="1919" height="1034" data-path=".assets/images/forest-guard-esp32/S224.png" />

**Node ID**

1. Set a unique **NODE\_ID** for each device.
2. Example: "01", "02", etc.

**GNSS Availability**

1. If your Node has a GNSS sensor attached → set GNSS\_AVAILABLE = true.
2. If not → set it to false.

**Manual Location (Optional)**

1. When GNSS is disabled, update the fallback latitude and longitude:

```cpp  theme={"system"}
static const float INITIAL_LAT = "------";
static const float INITIAL_LON = "------";
```

**Arduino IDE Settings**

1. Go to **Tools → Board → ESP32 → DFRobot FireBeetle 2 ESP32-S3**.
2. Connect your ESP32-S3 via **USB-C cable**.
3. Under **Tools → Port**, select the correct **COM port**.
4. Go to **Tools → USB CDC On Boot → Disable**.

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST231.png?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=b138e455a1272efdc70bddde8a24c905" alt="" width="1440" height="924" data-path=".assets/images/forest-guard-esp32/ST231.png" />

**Upload the Code**

1. Click the **Upload** button in Arduino IDE.
2. The code will compile (this may take a while since the Edge Impulse model is large).
3. Once complete, the firmware will be flashed to your ESP32-S3 Node.

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S232.png?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=5fa37f9a1208cdaca58ee5527b479256" alt="" width="1917" height="1031" data-path=".assets/images/forest-guard-esp32/S232.png" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/S233.png?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=b222569f83f5733620e24a823717d957" alt="" width="1919" height="1028" data-path=".assets/images/forest-guard-esp32/S233.png" />

**After Upload**

1. The Node should boot with a **Blue breathing LED** (boot + LoRa init).
2. After registration with the Gateway, it will begin sending sensor data and detecting events.

## Step 24: Gateway Design and 3D Printing

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/RXCAD2.png?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=969fedf603ea2e65e1bec58ed42a6e48" alt="" width="2048" height="1536" data-path=".assets/images/forest-guard-esp32/RXCAD2.png" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/RXCAD3.png?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=052ed18974b3b3b55d2f409cdd99b509" alt="" width="2048" height="1536" data-path=".assets/images/forest-guard-esp32/RXCAD3.png" />

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/RXCAD1.png?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=41e141a6c826ae54d710adf6e5f73581" alt="" width="2048" height="1536" data-path=".assets/images/forest-guard-esp32/RXCAD1.png" />

For the **Gateway enclosure**, I started by importing the **Arduino Uno R4 WiFi** and the **3.5” TFT display model** into **Fusion 360**. This allowed me to design the case around the exact dimensions of the components.

**Enclosure Features**

1. **Housing** - Includes cutouts for the TFT display, LoRa antenna, and the Arduino Type-C port.
2. **Cover** - Designed with mounting holes to securely fix the Arduino board inside.

**3D Printing**

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST241.JPG?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=970d74c5e786e251ab615d0d2bdb9aa6" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST241.JPG" />

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST242.JPG?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=e410bafb7637555f7c272d8b01f8d89a" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST242.JPG" />

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST243.JPG?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=02e15fa7b197536d0c1ac93bde313c1a" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST243.JPG" />

I 3D printed both the housing and the cover in **light gray** using my Bambu Labs P1S printer. The parts came out strong, precise, and professional-looking, making the gateway unit both robust and visually consistent with the Node design.

#### [Forest Guard Rx Fusion 360 File](https://a360.co/4nx2MuO)

## Step 25: Housing Assembly

1. Take the **gateway housing** and the **TFT display**.
2. Place the display into the housing, making sure it is in the **correct orientation** with the screen aligned to the cutout.
3. Secure the display using **4× M2 screws**.
4. Double-check that the screen sits flush with the housing and is firmly fixed in place.

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST251.JPG?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=e89e936b828c4c54ddcbc1a6cb17ed04" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST251.JPG" />

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST252.JPG?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=ec2d03193bc578e974178bda69983c20" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST252.JPG" />

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST253.JPG?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=359c707433995fd41fae552908e6a395" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST253.JPG" />

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST254.JPG?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=643b1ba2cb230e53f7d7de65581f0a80" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST254.JPG" />

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST255.JPG?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=0e290b1defadec99456d71ccd152570a" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST255.JPG" />

## Step 26: Antenna Assembly

1. Take the **LoRa antenna**.
2. Unscrew the antenna connector from the module.
3. Pass the antenna through the **antenna hole** on the housing.
4. Screw the antenna back onto the LoRa module from the outside.
5. Make sure the antenna is firmly seated and facing upright.

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST261.JPG?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=773eccc6f16ab965c449095c4f2ba4e1" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST261.JPG" />

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST262.JPG?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=102a0e41df98eead11f91437af5a16c9" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST262.JPG" />

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST263.JPG?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=d20d90b22fc114e4946f5d558b058437" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST263.JPG" />

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST264.JPG?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=7a3073e45401dca060502be1498fff62" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST264.JPG" />

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST265.JPG?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=623365a852aaceefb125dab4d3d9d62f" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST265.JPG" />

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST266.JPG?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=7d982b44ad38fb93f078065817c43c4f" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST266.JPG" />

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST267.JPG?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=703773c11ebc675e8c0739c777e19efe" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST267.JPG" />

## Step 27: Arduino Assembly

1. Take the **Arduino Uno R4 WiFi** and the **gateway cover**.
2. Align the Arduino with the **mounting holes** on the cover.
3. Secure it in place using **4× M2 screws**.
4. Ensure the **Type-C port** and headers remain accessible through the cover cutouts.

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST271.JPG?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=7791578182eab15fa85b4fa773da9ceb" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST271.JPG" />

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST272.JPG?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=9e11cd8688462c037558616f8b6fa258" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST272.JPG" />

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST273.JPG?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=4ad4f87121302b6edd20a0c0caf37363" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST273.JPG" />

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST274.JPG?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=db17bb74a0164484a39eefaff708d1fe" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST274.JPG" />

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST275.JPG?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=235677ad267b642785fd5b42ac78f9d1" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST275.JPG" />

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST276.JPG?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=9c029cf83d9fcf4ace70c4c60345c099" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST276.JPG" />

## Step 28: Buzzer and Power Switch Assembly

1. Take the **buzzer**, the **power switch**, and some **quick glue**.
2. Insert the **buzzer** into its dedicated slot on the cover.
3. Insert the **power switch** into its cutout hole on the cover.
4. Apply a small amount of **quick glue** around the switch edges to secure it in place.

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST281.JPG?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=4676b90e8623d01a74ac7a6a38cec2fb" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST281.JPG" />

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST282.JPG?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=d6befe63e930ccf8ce98abb3816aeebb" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST282.JPG" />

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST283.JPG?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=dd7990bad5c5d4e35693b960953ee908" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST283.JPG" />

<img src="https://mintcdn.com/edgeimpulse/aAButg-StuHcT2QT/.assets/images/forest-guard-esp32/ST284.JPG?fit=max&auto=format&n=aAButg-StuHcT2QT&q=85&s=8a3e4c31d8d3247b6030c098dd3dace2" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST284.JPG" />

## Step 29: Connections

<img src="https://mintcdn.com/edgeimpulse/-Z3DlC5HMsxcVfoh/.assets/images/forest-guard-esp32/RXCircuit.png?fit=max&auto=format&n=-Z3DlC5HMsxcVfoh&q=85&s=0d0894d31532bb2282a81751f4b24d55" alt="" width="1920" height="1080" data-path=".assets/images/forest-guard-esp32/RXCircuit.png" />

Now it’s time to wire everything together. Follow the **circuit diagram** carefully when connecting the **Arduino**, **TFT Display**, and **LoRa module**.

I used **male header pins** to avoid soldering directly to the Arduino. This way, the display and modules can be **plugged and unplugged** easily for debugging or replacement.

Arduino ↔ Display (TFT)

1. Connect as shown in the **wiring diagram above** (image).
2. Ensure all data and control pins are matched correctly, with **5V and GND** powering the display.

Arduino ↔ LoRa Module

1. **GND → GNS (LoRa GND)**
2. **5V → VSys (LoRa Power)**
3. **Pin 2 → Pin 9** (LoRa UART RX/TX pair)
4. **Pin 3 → Pin 8** (LoRa UART TX/RX pair)

Power & Peripherals

1. Connect the **battery and power switch** between **GND** and **5V** of the Arduino.
2. Connect the **buzzer**:
3. GND → Arduino GND
4. +Ve → Arduino Pin5

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST291.JPG?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=b43b2324a57601406ab0c888570fa8ce" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST291.JPG" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST292.JPG?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=27d19dff5d773f8092625df858562701" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST292.JPG" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST293.JPG?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=88f0749345ae842ad6d7520f35a271ae" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST293.JPG" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST294.JPG?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=732f5cb7a3c749fdfbf2c8a6df8cdfa7" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST294.JPG" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST295.JPG?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=e0976de08ba84b041b8b1c2582900151" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST295.JPG" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST296.JPG?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=850df7f5a6176e2908321cd3445f8d65" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST296.JPG" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST297.JPG?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=798b609678506eff58ca02e6330cb5e5" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST297.JPG" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST298.JPG?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=79d71dd5c23d3151d3b77e90a11491d8" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST298.JPG" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST299.JPG?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=e78e218c78e7c9134e4491f41b88adbd" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST299.JPG" />

## Step 30: Arduino Code

Now let’s program the **Gateway** so it can communicate with the nodes, process sensor/event data, and upload everything to Firebase.

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST301.jpg?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=e364d0ff7fae5962c06e20de95371efc" alt="" width="591" height="1280" data-path=".assets/images/forest-guard-esp32/ST301.jpg" />

**Download the Code**

1. Go to the [Forest Guard GitHub repository.](https://github.com/MukeshSankhla/Forest-Guard)
2. Download and extract the files.
3. Open **Gateway\_V1.ino** in the **Arduino IDE**.

**Setup Arduino IDE**

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST302.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=d8c78a25e01b103daaf2257c9de7a137" alt="" width="639" height="517" data-path=".assets/images/forest-guard-esp32/ST302.png" />

1. Make sure the **Arduino Uno R4 WiFi board package** is installed via **Board Manager**.
2. Install all required **libraries** as shown in the reference images (WiFiS3, ArduinoHttpClient, NTPClient, [DFRobot UI/TFT libraries](https://codeload.github.com/DFRobot/DFRobot_GDL/zip/master), etc.).

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST303.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=5ef85f81856edd78f1306c178abbb8de" alt="" width="716" height="542" data-path=".assets/images/forest-guard-esp32/ST303.png" />

**Add Your Credentials**

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST306.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=8f6088f95cce3092bba2e830f023f7eb" alt="" width="1916" height="1020" data-path=".assets/images/forest-guard-esp32/ST306.png" />

Inside the sketch:

1. Enter your **WiFi SSID and password**.
2. Enter your **Google Firebase host URL** and **authentication key**.

```cpp  theme={"system"}
// Wi-Fi
const char* WIFI_SSID = "";
const char* WIFI_PASS = "";

// Firebase RTDB (no https://, no trailing slash)
const char* FB_HOST = "-default-rtdb.asia-southeast1.firebasedatabase.app";
// Legacy database secret copied in Step 3
const char* FB_AUTH = "";
```

**Upload the Code**

1. In **Tools → Board**, select **Arduino UNO R4 WiFi**.
2. In **Tools → Port**, select the correct COM port for your board.
3. Click **Upload**.

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST304.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=15e4fe21cf9fca62613cd9eb34247ee6" alt="" width="1233" height="738" data-path=".assets/images/forest-guard-esp32/ST304.png" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST305.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=01e9672ef7ab063416bf65c24c972e60" alt="" width="1202" height="799" data-path=".assets/images/forest-guard-esp32/ST305.png" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST307.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=b9ad861db4656e30036813f87c80deec" alt="" width="1909" height="1025" data-path=".assets/images/forest-guard-esp32/ST307.png" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST308.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=cba8028a3d43db2c5d0e4a17460ca7ee" alt="" width="1912" height="1022" data-path=".assets/images/forest-guard-esp32/ST308.png" />

Once uploaded, the Gateway will:

1. Connect to WiFi.
2. Sync time via NTP.
3. Register nodes and receive LoRa messages.
4. Push ENV, LOC, and event data into **Firebase**.
5. Drive the TFT display and buzzer for real-time monitoring.

## Step 31: Firebase Project Setup

**1) Create a Firebase project**

1. Open **[https://console.firebase.google.com/](https://console.firebase.google.com/)**
2. **Create project** → (Google Analytics optional; you can keep default).
3. Wait for provisioning to finish.

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST313.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=52de71e5c11424ede9912bbfb18e06c2" alt="" width="1916" height="959" data-path=".assets/images/forest-guard-esp32/ST313.png" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST311.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=0598c5e3a44769810318c587efb4f490" alt="" width="1916" height="962" data-path=".assets/images/forest-guard-esp32/ST311.png" />

**2) Create a Realtime Database**

1. Left sidebar → **Build → Realtime Database** → **Create Database**
2. Choose a region close to you (e.g., **asia-southeast1 / Singapore**).
3. For quick testing select **Start in Test mode** (Firebase allows open read/write for 30 days).

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST316.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=cf6d4ff8484f7a6137c7d30ff2e1e1ee" alt="" width="1918" height="962" data-path=".assets/images/forest-guard-esp32/ST316.png" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST317.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=f071caac1a55f8834283109f36f4f552" alt="" width="844" height="406" data-path=".assets/images/forest-guard-esp32/ST317.png" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST314.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=f4b12a82c4ffcc3388194e0cd55f016c" alt="" width="842" height="570" data-path=".assets/images/forest-guard-esp32/ST314.png" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST315.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=40aeb4c9c299e35befe59fe6cb5eabf6" alt="" width="1485" height="874" data-path=".assets/images/forest-guard-esp32/ST315.png" />

**Copy the Database URL** shown at the top of the Data tab.

It looks like:

```
https://<your-project-id>-default-rtdb.asia-southeast1.firebasedatabase.app/
```

You will use this as FB\_HOST in the Gateway sketch.

**3) Get an auth token (Database Secret) for REST**
Your GA uses simple HTTPS REST with the ?auth=... query param.

1. **Project settings (gear) → Service accounts**
2. Click **Database secrets** → **Show** → **Copy** the secret.

You will use this as FB\_AUTH in the Gateway sketch.

**Add a Web App (for your dashboard)**

1. **Project Overview → Add app → Web**
2. Give it a name (e.g., **Forest Guard**) → **Register app**
3. On the next screen you’ll see your Web SDK config:

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST318.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=44fab1130b46b35968938ed453c778df" alt="" width="1372" height="840" data-path=".assets/images/forest-guard-esp32/ST318.png" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST319.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=ea2cd97ec9bac84682779d483d3df1b5" alt="" width="669" height="320" data-path=".assets/images/forest-guard-esp32/ST319.png" />

```javascript  theme={"system"}
const firebaseConfig = {
  apiKey: "...",
  authDomain: "...",
  databaseURL: "https://-default-rtdb..firebasedatabase.app",
  projectId: "...",
  storageBucket: "...",
  messagingSenderId: "...",
  appId: "..."
};
```

Copy these values into your dashboard (Lovable.dev) settings.

## Step 32: How the System Works

**1) Node (NA) boot & registration**

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/flow1.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=f02385f6ad294d3804ecdda98335ffdd" alt="" width="3840" height="2160" data-path=".assets/images/forest-guard-esp32/flow1.png" />

1. NA = **ESP32-S3** with Env + Smoke + Mic + (optional) GNSS + **RP2040 LoRa (Meshtastic)**.
2. On boot:
3. LED **Blue** breath.
4. Initializes sensors.
5. Checks GNSS\_AVAILABLE. If present, uses GNSS time; **location is sent only when satsUsed > 3**.
6. **Registers** with GA by broadcasting #\* every **10 s** until GA replies #+OK\*.
7. Only after registration do **Edge Impulse** (gunshot) and **fire/smoke** checks start.

**2) Periodic telemetry (non-blocking)**

1. Every **10sec** the NA sends:
2. **ENV:** #E,,temp,humidity,uv,lux,pressure,alt\*
3. **LOC:** #L,,lat,lon\* (only if GNSS fix has **>3 sats**; if GNSS is not fitted, system can use your initial set location).
4. LED **Green** breath on successful send.

**3) Event detection & retry**

1. **Gunshot:** Edge Impulse score crosses threshold (e.g., ≥0.90).
2. **Fire:** Smoke reading crosses threshold with hysteresis.
3. Node latches a single “current event” and creates eventId = random(0..100).
4. Sends every **10 s** until cleared by GA:
5. **Fire:** #F+,,,YYYY/MM/DD,HH:MM:SS\* or NT if no GNSS time.
6. **Gun:** #G+,,,YYYY/MM/DD,HH:MM:SS\* or NT.
7. LED **Red** breath while event is latched.

**4) Gateway (GA) reception & reliability**

1. GA = **Arduino UNO R4 WiFi** + TFT UI + Buzzer.
2. **LoRa noise-proofing:** both sides parse \*\*only bytes between # and \*\*\*; everything else is ignored.
3. On #\* → replies #+OK\* (register ACK).
4. On telemetry:
5. Maintains last posted values and **only uploads to Firebase when changed**
6. ENV changed by ≥ **±1.0** per field
7. LOC changed by ≥ **0.00010°** (\~11 m)
8. **NTP gate:** GA writes to Firebase **only after epoch ≥ 2025-01-01** (NTP warmup).

**5) Cloud logging (your schema)**

1. GA writes to Firebase RTDB paths:
2. nodes//env/ → `{ temp, humi, uvi, li, pres, alt }`
3. nodes//Loc/ → `{ lat, lon }` (capital **L**)
4. nodes//fire/ → `{ value, NodeTime }`
5. nodes//gun/ → `{ score, NodeTime }`
6. nodes//meta → `{ Event, lastSeenAt }`
7. When an event frame arrives:
8. Sets meta/Event = true.
9. Logs the event (de-duplicates by eventId).
10. Starts **buzzer** (non-blocking toggle).

**6) Dashboard + operator loop**

1. Dashboard reads RTDB to render **map, charts, and alerts**.
2. When the site is inspected and safe, the operator **sets meta/Event = false** in the dashboard.

**7) Clearing the event (end-to-end handshake)**

1. GA polls meta/Event. When it becomes **false**:
2. GA **broadcasts** #+C\* (a few times for reliability).
3. Stops buzzer, unlatches its local event, and remembers the last cleared eventId.
4. If NA keeps repeating the **same eventId**, GA does **not** re-log the event; it simply **re-ACKs CLEAR** and moves on.
5. NA receives #+C\* → clears its event latch and resumes normal telemetry.

**8) LED summary (NA)**

1. **Blue**: boot/LoRa/registration
2. **Green**: data sent
3. **Red**: event latched

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/flow3.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=5de8a480bae4d7a40c665dca9f687084" alt="" width="3840" height="2160" data-path=".assets/images/forest-guard-esp32/flow3.png" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/flow2.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=08f69df098874e197f43be0baf44b788" alt="" width="3840" height="2160" data-path=".assets/images/forest-guard-esp32/flow2.png" />

## Step 33: Dashboard

To visualize the data coming from the **Forest Guard Nodes**, I built a custom **web dashboard** using **Lovable.dev**. This dashboard connects directly to **Firebase** and provides both a quick overview and detailed insights into the forest monitoring network.

[Forest Guard Dashboard](https://preview--wildfire-tracker.lovable.app/)

**Setup**

1. When the dashboard is first opened, it takes you to a **Firebase configuration page**.
2. Here, you enter your **Firebase host and authentication key**.
3. Once saved, the dashboard connects to the database and loads the real-time data.

**Map View**

1. The **map view** shows the live location of all deployed nodes.
2. Each node is color-coded by status:
3. **Gray** → Inactive
4. **Green** → Active
5. **Red** → Alert (fire or gunshot detected)
6. By clicking on a node, you can quickly check its latest sensor data and status.

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST331.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=f5d3f0ba102b56ea77ee19ec337704c3" alt="" width="1423" height="873" data-path=".assets/images/forest-guard-esp32/ST331.png" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST333.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=217abbd621a7c59bb5deba480a9d8b71" alt="" width="1382" height="852" data-path=".assets/images/forest-guard-esp32/ST333.png" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/St332.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=169769ba21acc0b3a716181ab61dd6a7" alt="" width="1384" height="855" data-path=".assets/images/forest-guard-esp32/St332.png" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST334.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=07caad0981c7f201f6acc1172c28b3d7" alt="" width="1402" height="855" data-path=".assets/images/forest-guard-esp32/ST334.png" />

**Quick Cards**
At the top of the dashboard, quick cards summarize the system:

1. **Total Nodes** → Number of nodes in the network.
2. **Online Status** → Active vs inactive nodes.
3. **Recent Alerts** → Count of fire/gunshot events in the last 12 hours.
4. **Data Points** → Total environmental readings logged.

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST335.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=4415a299d825fdf66b2cd8c625d53c5a" alt="" width="1447" height="876" data-path=".assets/images/forest-guard-esp32/ST335.png" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST336.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=c39aa5e0f058722875b8b6b55d152a30" alt="" width="1395" height="858" data-path=".assets/images/forest-guard-esp32/ST336.png" />

**Node Details**
Clicking on **“View Node Details”** opens a **full dashboard view** for that node. Here you can monitor:

1. **Current Environmental Conditions** (temperature, humidity, pressure, light, UV, altitude).
2. **Trends over Time** with graphs for Temperature & Humidity, Light & UV Index.
3. **Fire Detection Events** (timestamped alerts from smoke sensor).
4. **Gunshot Detection Events** (with AI confidence scores from Edge Impulse model).

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST337.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=33e9e04bfb8d0290848e7fec643dd753" alt="" width="1248" height="832" data-path=".assets/images/forest-guard-esp32/ST337.png" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST338.png?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=47eea01471159fc39ce52779e08a2f97" alt="" width="1248" height="888" data-path=".assets/images/forest-guard-esp32/ST338.png" />

**Why It Matters**
This dashboard transforms raw sensor data into a **clear, real-time interface** for rangers, researchers, or conservation teams. With one glance, you can see:

1. Which nodes are active, where they are, and what conditions they’re reporting.
2. Whether a **fire or gunshot event** has been detected.
3. Historical trends that help understand the forest’s environmental conditions.

It essentially turns the **Forest Guard network** into a **living digital twin of the forest**.

## Step 34: Conclusion

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST341.JPG?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=39e6264b0a61a8731248d0ab7262b8f5" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST341.JPG" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST342.JPG?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=2cc2bccd6a03838bc239c8e3ec0c888d" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST342.JPG" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST343.JPG?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=0a36bd634383ff9356ca4a7d1162a3b8" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST343.JPG" />

<img src="https://mintcdn.com/edgeimpulse/oeq-hrLw-511kvB_/.assets/images/forest-guard-esp32/ST344.JPG?fit=max&auto=format&n=oeq-hrLw-511kvB_&q=85&s=4f9937658db464ef899a8a7d2812de7f" alt="" width="6000" height="3376" data-path=".assets/images/forest-guard-esp32/ST344.JPG" />

With the completion of this build, we have created **Forest Guard**, a decentralized **forest surveillance system** that can detect and alert about critical events such as **gunshots** or **forest fires** — even in regions with no internet or cellular coverage. By combining **low-power LoRa mesh networking**, **solar-powered sensor nodes**, and **edge AI intelligence**, this project proves that modern technology can play a vital role in **safeguarding our forests** and protecting wildlife.

The **Gateway** provides a central bridge to the cloud, where data is stored and visualized in real time, while the **Nodes** tirelessly monitor the environment, detect anomalies, and forward alerts across the mesh. Together, they form a **scalable, resilient, and sustainable system** that can make a real difference for conservationists, rangers, and environmental researchers.

What makes this system truly exciting is the **flexibility of Edge AI**. Using the **Edge Impulse platform**, we trained a model to detect **gunshots**, but the same pipeline can be extended further:

1. By training on audio recordings of **chainsaws or tree cutting**, the system could become an **anti-illegal logging detector**.
2. With audio datasets of **endangered or extinct species calls**, it could serve as a **wildlife discovery and monitoring system**, helping scientists and communities identify rare animals in the wild.

This adaptability shows that Forest Guard is not just a single-purpose project, but a **platform for innovation in forest conservation**. From **early fire detection** to **biodiversity monitoring**, the possibilities are vast.

In the end, this project is a step toward a future where **technology and nature coexist**, where smart sensors and AI extend the eyes and ears of humans into places we cannot always reach — ensuring our forests remain safe, vibrant, and full of life for generations to come. 🌲🌍💡


Built with [Mintlify](https://mintlify.com).