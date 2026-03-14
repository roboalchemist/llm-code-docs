# Source: https://docs.edgeimpulse.com/projects/expert-network/soil-quality-detection-lorawan-seeed-sensecap-a1101.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Soil Quality Detection Using AI and LoRaWAN - Seeed Sensecap A1101

Created By: Kutluhan Aktar

Public Project Link: [https://studio.edgeimpulse.com/public/233660/latest](https://studio.edgeimpulse.com/public/233660/latest)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/finished_1.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=0edfce7e81ef080f415c0d21be3a2c15" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/finished_1.jpg" />
</Frame>

## Description

To achieve a successful harvest season with prolific plants, farmers utilized a type of fertilizer to increase soil fertility, dating back to the earliest attempts to provide enough food in order to sustain larger populations. Until the industrial revolution, farmers mostly applied organic fertilizers and materials to supply adequate nutrients for plants, including naturally available mineral sources, manure, crop residues, etc. However, due to the evergrowing human population and declining fertile lands, agriculturalists started to utilize organic fertilizers in conjunction with chemical fertilizers to improve crop yield, even to the extent of causing soil contamination.

Chemical fertilizers are synthesized industrially out of estimated proportions of elements like nitrogen, phosphorus, and potassium\[^1], which provide necessary nutrients for plants to flourish vigorously. Due to intensive cultivation and the insufficient replenishment of nutrients, fertilizers mitigate precipitously declining soil fertility. In combination with organic fertilizers, chemical fertilizers can even revitalize arable lands. Although chemical fertilizers are indispensable to sustain soil fertility and avoid food shortages considering the current human population, they can also be noxious without painstaking attention to soil test reports. Since chemical fertilizers directly affect soil integrity and permeate through water bodies, they can contaminate the groundwater and the environment. Also, chemical fertilizers infiltrate the soil and make plants vulnerable to various pathogens by hampering their roots\[^1].

When chemical fertilizers disperse throughout water bodies, they increase macronutrients in the environment, such as nitrogen, potassium, and phosphorus, resulting in contamination and eutrophication (nutrient pollution). These macronutrients can cause serious health problems due to overexposure. For instance, nitrogen can remain in water bodies for several years and cause nitrite (and nitrate) to accumulate exponentially. As a result of the high nitrite accumulation, nitrite-contaminated water can cause a blood disorder called methemoglobinemia (MetHb), also known as Blue Baby Syndrome. Furthermore, chemical reactions between nitrites heavily used in synthetic fertilizers instigate DNA damage, lipid peroxidation, and oxidative stress, which can all result in increased cellular degeneration. As a major health issue caused by the excessive use of chemical (synthetic) fertilizers, cellular degeneration can increase the risk of developing cancer. Forebodingly, a 2009 study by researchers at Rhode Island Hospital has found a substantial link between increased levels of nitrates in our environment and food with increased deaths from diseases, including Alzheimer's, diabetes mellitus, and Parkinson's\[^2].

According to earlier estimations, fertilizers provided approximately 70% of plant nutrients in 2020 at a global level\[^3]. Therefore, at this point, we cannot obviate the need for organic and chemical fertilizers to achieve sustainable crop production. Nevertheless, applying organic fertilizers in conjunction with chemical fertilizers can engender unexpected results and exacerbates the detrimental effects of chemical (synthetic) fertilizers. Since organic fertilizers behave differently depending on their manufacturing conditions, they change the degree of soil permeability of different soil types, such as loamy, peaty, silty, chalky, etc., not only unpredictably but also structurally. Hence, applying chemical fertilizers to the soil structurally altered by organic fertilizers may intensify the mentioned hazardous effects and lead to serious health conditions.

After scrutinizing the recent research papers on the effects of chemical and organic fertilizers, I noticed there are nearly no appliances focusing on detecting the excessive use of chemical fertilizers in the presence of organic fertilizers and providing real-time detection results for further inspection. Therefore, I decided to build a budget-friendly and easy-to-use proof-of-concept device to detect chemical fertilizer contamination levels with object recognition and inform the user of the model detection results simultaneously in the hope of averting the detrimental effects of fertilizer overuse by pre-warning farmers.

To detect chemical fertilizer contamination levels accurately in relation to organic fertilizers, I needed to collect data from a controlled environment manifesting different soil conditions so as to train my object detection model with notable validity. Since utilizing manure as organic fertilizer affects soil acidification, integrity, and structure depending on the manure decomposition stages (fresh, active, mature, and old), I decided to produce my organic fertilizers by composting manure. Fortunately, I am raising quails on my balcony and have experience in utilizing quail manure as organic fertilizer. To change the soil integrity and structure in relation to the applied organic fertilizer, I collected quail manure in different decomposition stages:

* Fresh (1 month)
* Active (3 months)
* Old (6 months)

After producing organic fertilizers in different decomposition stages, I applied them to the soil in three separate flowerpots. Then, I added chemical fertilizers to each flowerpot in the same amount to examine the excessive use of chemical fertilizers depending on the soil integrity and structure. To demonstrate the fertilizer contamination effects on the environment, I sowed different types of tomato seedlings in each flowerpot.

* Calcium Nitrate
* Magnesium Sulphate
* Ammonium Sulphate
* Ammonium Phosphate

Since Wi-Fi and Bluetooth transmissions may not be suitable options for a device operating in farms, I decided to utilize a [SenseCAP A1101 Vision AI](https://www.seeedstudio.com/SenseCAP-A1101-LoRaWAN-Vision-AI-Sensor-p-5367.html) sensor manufactured by Seeed Studio. The SenseCAP A1101 provides a 400Mhz DSP Himax camera for image recognition and a Wio-E5 LoRaWAN module for LoRaWAN long-range transmission. Also, it is compatible with different types of LoRaWAN® gateways and networks, such as the Helium LongFi Network. As shown in the following steps, I explained how to activate a SenseCAP M2 data-only LoRaWAN indoor gateway (EU868) and connect SenseCAP A1101 to the Helium LongFi Network through the SenseCAP M2 data-only gateway. SenseCAP gateways are only required if the Helium network does not cover your surroundings. Since SenseCAP A1101 supports uploading TinyML object detection models as firmware, I was able to run my model without a single line of code. Nevertheless, SenseCAP A1101 does not give you the option to capture images with different labels out of the box. Therefore, I connected three control buttons and an SH1106 OLED screen to Arduino Nano in order to build a simple remote control. Then, I employed LattePanda 3 Delta to program SenseCAP A1101 to capture images according to labels transferred by the remote control via serial communication.

After completing my data set by taking pictures of fertilizer-exerted soils from my three separate flowerpots, I built my object detection model with Edge Impulse to detect chemical fertilizer contamination levels. I utilized Edge Impulse FOMO (Faster Objects, More Objects) algorithm to train my model, which is a novel machine learning algorithm that brings object detection to highly constrained devices. Since Edge Impulse is nearly compatible with all microcontrollers and development boards, I have not encountered any issues while uploading and running my model on SenseCAP A1101.

As labels, I utilized fertilizer contamination levels based on the soil integrity and structure altered by the applied organic fertilizer (manure) decomposition stage:

* Enriched
* Unsafe
* Toxic

After training and testing my object detection (FOMO) model, I deployed and uploaded the model on SenseCAP A1101 as its compatible firmware (UF2). Therefore, the device is capable of detecting fertilizer contamination levels by running the model independently without any additional procedures or latency.

Since I focused on building a full-fledged AIoT appliance detecting fertilizer contamination levels despite utilizing the LoRaWAN network as the primary transmission method, I decided to develop a Python application from scratch informing the user of the recent model detection results via WhatsApp. Plausibly, all SenseCAP AI devices are capable of logging information to the SenseCAP Portal via the LoRaWAN network. Also, Seeed Studio provides the SenseCAP HTTP API to obtain registered data records from the SenseCAP Portal via HTTP GET requests. Therefore, firstly, I utilized the application to get the recent model detection results from the given SenseCAP Portal account.

Then, this complementing application employs Twilio's WhatsApp API to send the latest model detection results to the verified phone number, which SenseCAP A1101 registered to the SenseCAP Portal via the Helium LongFi Network.

Since I decided to capture images with SenseCAP A1101 and run my Python application on LattePanda 3 Delta, I wanted to build a mobile and compact apparatus to access LattePanda 3 Delta in the field without requiring an additional procedure. To improve the user experience, I utilized a high-quality 8.8" IPS monitor from Elecrow. As explained in the following steps, I designed a two-part case (3D printable) in which I placed the Elecrow IPS monitor.

Lastly, to make the device as robust and sturdy as possible while operating outdoors, I designed a plant-themed case providing screw holes to attach the SenseCAP A1101 bracket, a sliding front cover, and a separate section for the remote control compatible with a diagonal top cover with snap-fit joints (3D printable).

So, this is my project in a nutshell 😃

In the following steps, you can find more detailed information on coding, capturing soil images with SenseCAP A1101, building an object detection (FOMO) model with Edge Impulse, running the model on SenseCAP A1101, transferring data to the SenseCAP Portal via the LoRaWAN network, and developing a full-fledged Python application to obtain model detection results and inform the user via WhatsApp.

🎁🎨 Huge thanks to [Elecrow](https://www.elecrow.com/?idd=3) for sending me an [Elecrow 8.8" IPS Monitor (1920\*480)](https://www.elecrow.com/elecrow-8-8-inch-display-1920-480-ips-screen-lcd-panel-raspberry-pi-compatible-monitor.html?idd=3).

🎁🎨 Huge thanks to [DFRobot](https://www.dfrobot.com/?tracking=60f546f8002be) for sending me a [LattePanda 3 Delta 864](https://www.dfrobot.com/product-2594.html?tracking=60f546f8002be).

🎁🎨 Also, huge thanks to [Anycubic](https://www.anycubic.com/) for sponsoring a brand-new [Anycubic Kobra 2](https://bit.ly/3Ov2PJh).

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/finished_2.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=73a3ff0f2c9b6e86b8af57ae6d082b20" width="750" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/finished_2.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/assembly_12.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=2b8e61ee6a786a0573d16202de2fae4c" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/assembly_12.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/finished_1.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=0edfce7e81ef080f415c0d21be3a2c15" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/finished_1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_extraction_1.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=6d26451ae006c90e18bd85379cbbf942" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_extraction_1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_extraction_8.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=c013c7891e9da8c51b6ef2a0d5743b1b" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_extraction_8.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_chemical_0.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=47700facf25fb90fab5638bd931fff12" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_chemical_0.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_chemical_8.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=d0b7c4ba3367fcbf41d09d65c432fede" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_chemical_8.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/collect_2.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=ef7bb98ab8e7d153e65ff82707776bc5" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/collect_2.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/collect_4.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=51461cf607959229ceb4924743f03757" width="750" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/collect_4.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/collect_5.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=84912c530555e7fc20636c7bced56214" width="750" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/collect_5.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/collect_6.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=11da3d985a74a0d3db1b3c676ecc8f67" width="750" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/collect_6.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/collect_7.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=690a821a7d63c60a350ae3115403467f" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/collect_7.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/edgeimpulse/.assets/images/sensecap-a1101-lorawan-soil-quality/gif_collect.gif" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/data_collect_2.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=5a991989355acb34a338c17847206703" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/data_collect_2.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/data_collect_7.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=2abdf6167066e1c22a905e7f68baebed" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/data_collect_7.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_sample_collect_2.png?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=05b4cbf46312df88ec167c405d26745b" width="1600" height="869" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_sample_collect_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/run_2.jpg?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=e213e01cbf4157cc239a1676a1c88ddd" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/run_2.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/whatsapp_3.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=3bd7cad57566d952189f02037686e379" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/whatsapp_3.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/whatsapp_4.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=6c1f42bcbdc61b4e98afe2cf697932b2" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/whatsapp_4.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/gif_run.gif?s=c31299bddb3a13c5814c366338d260e1" width="1000" height="493" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/gif_run.gif" />
</Frame>

## Step 1: Designing and printing a plant-themed case

Since I focused on building a budget-friendly and accessible appliance that captures images of fertilizer-exerted soils and runs an object detection model to inform the user of the excessive use of chemical fertilizers over WhatsApp via the LoRaWAN network, I decided to design a modular and compact case allowing the user to place the remote control and position SenseCAP A1101 with LattePanda 3 Delta effortlessly. To avoid overexposure to dust and prevent loose wire connections, I added a sliding front cover. Then, I designed a diagonal top cover for the separate remote control section of the main case, mountable via snap-fit joints. Also, I decided to inscribe the Helium logo and the Arduino symbol on the sliding front cover and the diagonal top cover to highlight the LoRaWAN-enabled fertilizer contamination detection.

Since I needed to attach SenseCAP A1101 to the main case via its bracket, I decided to add compatible screw holes on the top of the main case. Due to the separate section, I was able to fit the remote control and connect it to LattePanda 3 Delta as a single unit.

I designed the main case, its sliding front cover, and the diagonal top cover in Autodesk Fusion 360. You can download their STL files below.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/model_1.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=d4fe0f0feeaf4b23cfcea830a3d3a8ca" width="1600" height="870" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/model_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/model_2.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=5280f634dd7af2b44ba7ae086f1af291" width="1600" height="869" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/model_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/model_3.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=031df81ce9034e51d0438b391502972d" width="1600" height="869" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/model_3.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/model_4.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=dd2f5fb4031e59778033d89b730ea970" width="1600" height="869" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/model_4.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/model_5.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=b5929934465c8e0eb1c885397cc498aa" width="1600" height="869" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/model_5.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/model_6.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=4bb857f0e88ad4b1de3d0f1a506b4dbc" width="1600" height="871" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/model_6.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/model_7.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=02d6a8283430ff2b039586409a1131d1" width="1600" height="870" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/model_7.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/model_8.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=1d2960f46f0d42b58545bb4eca16ae01" width="1600" height="871" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/model_8.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/model_9.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=a51e5d45e776ff8b35cbbebcb11594ba" width="1600" height="869" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/model_9.png" />
</Frame>

Then, I sliced all 3D models (STL files) in Ultimaker Cura.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/model_10.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=4520de73f324626596738e9a3583c36f" width="1600" height="869" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/model_10.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/model_11.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=a76ca6bb39ebe9c2c111c8225157beca" width="1600" height="870" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/model_11.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/model_12.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=9b4e3b0515c58c8875e71992388a97aa" width="1600" height="870" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/model_12.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/model_13.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=a55b11e13f10590fc4dacd89cbe6a100" width="1600" height="870" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/model_13.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/model_14.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=2abd16beef11a670a1ebdbb6814869e5" width="1600" height="871" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/model_14.png" />
</Frame>

Since I wanted to create a glistening plant structure for the main case and apply a unique verdant theme denoting burgeoning plants, I utilized these PLA filaments:

* eSilk Lime
* Green RAL 6029

Finally, I printed all parts (models) with my brand-new Anycubic Kobra 2 3D Printer.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/printed_1.jpg?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=79e491a3a1f708cad591aefff3ae96ee" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/printed_1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/printed_2.jpg?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=15ee5af3bb128befb1e4399967c75a99" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/printed_2.jpg" />
</Frame>

Since Anycubic Kobra 2 is budget-friendly and specifically designed for high-speed printing, I highly recommend Anycubic Kobra 2 if you are a maker or hobbyist needing to print multiple prototypes before finalizing a complex project.

Thanks to its upgraded direct extruder, Anycubic Kobra 2 provides 150mm/s recommended print speed (up to 250mm/s) and dual-gear filament feeding. Also, it provides a cooling fan with an optimized dissipation design to support rapid cooling complementing the fast printing experience. Since the Z-axis has a double-threaded rod structure, it flattens the building platform and reduces the printing layers, even at a higher speed.

Furthermore, Anycubic Kobra 2 provides a magnetic suction platform on the heated bed for the scratch-resistant spring steel build plate allowing the user to remove prints without any struggle. Most importantly, you can level the bed automatically via its user-friendly LeviQ 2.0 automatic bed leveling system. Also, it has a smart filament runout sensor and the resume printing function for power failures.

:hash: First of all, install the gantry and the spring steel build plate.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/kobra_assembly_1.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=3f676f7baf72dcf0d5e0a3816ccbdfa4" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/kobra_assembly_1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/kobra_assembly_2.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=bada22442410e561100b08e849a340f6" width="750" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/kobra_assembly_2.jpg" />
</Frame>

:hash: Install the print head, the touch screen, and the filament runout sensor.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/kobra_assembly_3.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=95376c7e3e5abb37199b03ab403a265c" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/kobra_assembly_3.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/kobra_assembly_4.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=60d1a34dd5ce5f9722dbf1064200526a" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/kobra_assembly_4.jpg" />
</Frame>

:hash: Connect the stepper, switch, screen, and print head cables. Then, attach the filament tube.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/kobra_assembly_5.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=1385107fc77305bf908318c639d41ed9" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/kobra_assembly_5.jpg" />
</Frame>

:hash: If the print head is shaking, adjust the hexagonal isolation column under the print head.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/kobra_assembly_6.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=433aa9e77ef3807912ceccda5b52a309" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/kobra_assembly_6.jpg" />
</Frame>

:hash: Go to *Prepare➡ Leveling ➡ Auto-leveling* to initiate the LeviQ 2.0 automatic bed leveling system.

:hash: After preheating and wiping the nozzle, Anycubic Kobra 2 probes the predefined points to level the bed.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/kobra_assembly_7.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=f625b3d1c26f674f3ca6db3b49661ea1" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/kobra_assembly_7.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/kobra_assembly_8.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=fe84b0e43e859959b35b9c9147e0b3ca" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/kobra_assembly_8.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/kobra_assembly_9.jpg?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=71b1faa9728b8b93e41b5593031243f8" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/kobra_assembly_9.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/kobra_assembly_10.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=59ee72f305783e40fe0195257388e894" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/kobra_assembly_10.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/kobra_assembly_11.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=58278f40ab75c1798174300ac4489b0b" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/kobra_assembly_11.jpg" />
</Frame>

:hash: Finally, fix the filament tube with the cable clips, install the filament holder, and insert the filament into the extruder.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/kobra_assembly_12.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=b24b63eb5804d337a67f25da5322fc76" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/kobra_assembly_12.jpg" />
</Frame>

:hash: Since Anycubic Kobra 2 is not officially supported by Cura yet, download the latest [PrusaSlicer](https://www.prusa3d.com/page/prusaslicer_424/) version and import the printer profile (configuration) file provided by Anycubic.

:hash: Then, create a custom printer profile on Cura for Anycubic Kobra 2 and change *Start G-code* and *End G-code*.

:hash: Based on the provided *Start G-code* and *End G-code* in the configuration file, I modified new *Start G-code* and *End G-code* compatible with Cura.

```
Start G-code:

G90 ; use absolute coordinates
M83 ; extruder relative mode
G28 ; move X/Y/Z to min endstops
G1 Z2.0 F3000 ; lift nozzle a bit
G92 E0 ; Reset Extruder
G1 X10.1 Y20 Z0.28 F5000.0 ; Move to start position
G1 X10.1 Y200.0 Z0.28 F1500.0 E15 ; Draw the first line
G1 X10.4 Y200.0 Z0.28 F5000.0 ; Move to side a little
G1 X10.4 Y20 Z0.28 F1500.0 E30 ; Draw the second line
G92 E0 ; zero the extruded length again
G1 E-2 F500 ; Retract a little
M117
G21 ; set units to millimeters
G90 ; use absolute coordinates
M82 ; use absolute distances for extrusion
G92 E0
M107

End G-code:

M104 S0 ; Extruder off
M140 S0 ; Heatbed off
M107    ; Fan off
G91     ; relative positioning
G1 E-5 F3000
G1 Z+0.3 F3000 ; lift print head
G28 X0  F3000
M84            ; disable stepper motors
```

:hash: Finally, adjust the official printer settings depending on the filament type while copying them from PrusaSlicer to Cura.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/kobra_2_set_1.png?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=3091a88fe74ca60d7e8bd98f6cffe28c" width="1600" height="851" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/kobra_2_set_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/kobra_2_set_2.png?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=915a10a6e2f6610b1c240b6abbbefe43" width="1600" height="850" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/kobra_2_set_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/kobra_2_set_3.png?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=acb47d9319f0887dff725c16c00dba88" width="1600" height="848" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/kobra_2_set_3.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/kobra_2_set_4.png?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=f6f48d212f1d813abb45b2877cf85ab3" width="1600" height="850" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/kobra_2_set_4.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/kobra_2_set_5.png?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=f2822b1281cc101b0101145d553a7b07" width="1600" height="848" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/kobra_2_set_5.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/kobra_2_set_6.png?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=e127407707a53fe722fe10329fb57971" width="1600" height="848" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/kobra_2_set_6.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/kobra_2_set_7.png?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=022cfe3200fcda5ad68f16a2b89cc8ef" width="1600" height="848" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/kobra_2_set_7.png" />
</Frame>

## Step 1.1: Assembling the case and making connections & adjustments

```
// Connections
// Arduino Nano :
//                                SH1106 OLED Display (128x64)
// D11  --------------------------- SDA
// D13  --------------------------- SCK
// D8   --------------------------- RST
// D9   --------------------------- DC
// D10  --------------------------- CS
//                                Control Button (A)
// A0   --------------------------- +
//                                Control Button (B)
// A1   --------------------------- +
//                                Control Button (C)
// A2   --------------------------- +
//                                5mm Common Anode RGB LED
// D3   --------------------------- R
// D5   --------------------------- G
// D6   --------------------------- B
```

Since [SenseCAP A1101](https://files.seeedstudio.com/wiki/SenseCAP-A1101/SenseCAP_A1101_LoRaWAN_Vision_AI_Sensor_User_Guide_V1.0.2.pdf) does not support capturing images with different labels out of the box, I decided to build a simple remote control with Arduino Nano to capture pictures easily. Then, I employed LattePanda 3 Delta to program SenseCAP A1101 to capture images according to labels transferred by the remote control via serial communication.

To be able to transfer commands to SenseCAP A1101 via serial communication, I connected Arduino Nano directly to LattePanda 3 Delta via a USB cable. I utilized an SH1106 OLED screen to display ongoing operations and visualize the selected fertilizer contamination classes (levels). Then, I added three control buttons to transfer the user commands to LattePanda 3 Delta via serial communication. Also, I added an RGB LED to inform the user of the device status, indicating serial communication success.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/breadboard_1.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=52d93c06e8eb8cc2cc4c01a2bdeee85a" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/breadboard_1.jpg" />
</Frame>

After printing all parts (models), I fastened the remote control to the separate section of the main case via a hot glue gun. I also utilized the SenseCAP A1101's screw kit to attach its bracket firmly to the screw holes on the top of the main case.

I placed LattePanda 3 Delta in the main case and attached SenseCAP A1101 to its bracket. Then, I attached the diagonal top cover to the main case via its snap-fit joints.

Finally, I inserted the sliding front cover via the dents on the main case.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/assembly_1.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=c32b4f50eb1efbb7f73468a5fa42a836" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/assembly_1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/assembly_2.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=c791e4f3660373b85aaa46fdde3662b8" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/assembly_2.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/assembly_3.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=c6077cb2b82cf1127d73cdbc430012f1" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/assembly_3.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/assembly_4.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=e822e4ced702b6d30dab6b1e84ecc371" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/assembly_4.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/assembly_5.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=f62cadb0677f664ec1c443821151dc6f" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/assembly_5.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/assembly_6.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=6588687eee9fd03db4a84de1ef4b6c0d" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/assembly_6.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/assembly_7.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=f9de0344036af16813fd16cca637c6f9" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/assembly_7.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/assembly_8.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=7fe0f18e4addf5c9c3f03e68876da00b" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/assembly_8.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/assembly_9.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=d4a41f1e1350967b60834417c53c1bd9" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/assembly_9.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/assembly_10.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=5f694eb25ee82d8d83010d574a43bd42" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/assembly_10.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/assembly_11.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=af9d7be92e5c358378423eff6b38db3a" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/assembly_11.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/assembly_12.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=2b8e61ee6a786a0573d16202de2fae4c" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/assembly_12.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/assembly_13.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=d8c23de9047fffa75b33500cd2af4771" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/assembly_13.jpg" />
</Frame>

As mentioned earlier, the diagonal top cover can be utilized to hide the remote control when running the object detection model instead of collecting data.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/finished_1.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=0edfce7e81ef080f415c0d21be3a2c15" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/finished_1.jpg" />
</Frame>

## Step 1.2: Creating a LattePanda Deck to display the video stream

Since I decided to program SenseCAP A1101 with LattePanda 3 Delta to capture images depending on labels transferred by the remote control via serial communication, I decided to design a unique and compact LattePanda Deck to display the real-time video stream generated by SenseCAP A1101, which is not only compatible with LattePanda but also any single-board computer supporting HDMI.

I decided to employ [Elecrow's 8.8" (1920\*480) high-resolution IPS monitor](https://www.elecrow.com/elecrow-8-8-inch-display-1920-480-ips-screen-lcd-panel-raspberry-pi-compatible-monitor.html?idd=3) as the screen of my LattePanda Deck. Thanks to its converter board, this monitor can be powered via a USB port and works without installing any drivers. Therefore, it is a compact plug-and-play monitor for LattePanda 3 Delta, providing high resolution and up to 60Hz refresh rate.

Due to the fact that I wanted to build a sturdy and easy-to-use deck, I designed a two-part case covering the screen frame and providing a slot for the converter board. To avoid overexposure to dust and provide room for cable management, I added a mountable back cover adorned with the brand logo.

I designed the two-part case and its mountable back cover in Autodesk Fusion 360. You can download their STL files below.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/model_elecrow_1.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=395f3435535270dd30896540d3121266" width="1600" height="848" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/model_elecrow_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/model_elecrow_2.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=fdbe068648dba32709cb5e8a0ff92279" width="1600" height="848" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/model_elecrow_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/model_elecrow_3.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=0e4f960ec28e43c6b9f072c5d6dbe6ad" width="1600" height="848" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/model_elecrow_3.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/model_elecrow_4.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=0e829184021b0a6b0f456c50d6141dba" width="1600" height="848" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/model_elecrow_4.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/model_elecrow_5.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=2566d4e570eba55553dd53da2a73332a" width="1600" height="848" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/model_elecrow_5.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/model_elecrow_6.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=f1aff1ee2ad4e5c8309fc4f498fbb19f" width="1600" height="848" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/model_elecrow_6.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/model_elecrow_7.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=6a4daf893eaa6c3fd06b44a959b11c1a" width="1600" height="848" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/model_elecrow_7.png" />
</Frame>

Then, I sliced all 3D models (STL files) in Ultimaker Cura.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/model_elecrow_8.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=91cc67b374627f52258b677313de2f8f" width="1600" height="851" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/model_elecrow_8.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/model_elecrow_9.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=9d9db48e74800efcf24306aca339d0c9" width="1600" height="848" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/model_elecrow_9.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/model_elecrow_10.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=14d4e6319a9d87efcdbdba1e5511afec" width="1600" height="848" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/model_elecrow_10.png" />
</Frame>

After printing all deck parts (models) with my Anycubic Kobra 2 3D Printer, I affixed the two-part case together via the hot glue gun.

Then, I fastened the Elecrow's IPS monitor to the case covering the screen frame and inserted the converter board into its slot.

After attaching the required cables to the converter board, I fixed the mountable back cover via M3 screws.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/elecrow_0.jpg?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=46b01d5ba8e5a1caa59ff9448f53f617" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/elecrow_0.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/elecrow_1.jpg?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=ca119ecc61aab3b39d94fca237d3e8c9" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/elecrow_1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/elecrow_2.jpg?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=89ca724dda28e4cfacc837eabf7f70c6" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/elecrow_2.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/elecrow_3.jpg?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=5f6687afd99421043358bcdfff853234" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/elecrow_3.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/elecrow_4.jpg?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=a99cfd3369328d0fb22ea0191ea18302" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/elecrow_4.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/elecrow_5.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=af11078527b491a6903edcacfcb87b34" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/elecrow_5.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/elecrow_6.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=b082c663506a3e8946af51e3a74607e0" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/elecrow_6.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/elecrow_7.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=5f602e027416c92148882486b75daa2a" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/elecrow_7.jpg" />
</Frame>

After connecting the converter board to LattePanda 3 Delta via its USB and HDMI ports, LattePanda recognizes the IPS monitor automatically.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/elecrow_8.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=cdbb96b7cb6562c17e083ab7e1f2ed46" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/elecrow_8.jpg" />
</Frame>

## Step 2: Creating an account to utilize Twilio's WhatsApp API

Since I decided to inform the user of the model detection results over WhatsApp via the LoRaWAN network, I needed to utilize Twilio's WhatsApp API. [Twilio](https://www.twilio.com/docs/libraries/python) gives the user a simple and reliable way to communicate with a Twilio-verified phone over WhatsApp via its WhatsApp API for trial accounts. Also, Twilio provides official helper libraries for different programming languages, including Python.

:hash: First of all, sign up for [Twilio](https://www.twilio.com/try-twilio) and create a new free trial account (project).

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/twilio_set_1.png?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=8a861edd4fbbfe986d78011a31ee1117" width="1600" height="825" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/twilio_set_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/twilio_set_2.png?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=591e29ea39a470f171a8e85a5b850440" width="1600" height="823" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/twilio_set_2.png" />
</Frame>

:hash: Then, verify a phone number for the account (project) and set the account settings for WhatsApp in Python.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/twilio_set_3.png?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=2b653575121ad2ff51e79526a8164911" width="1600" height="827" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/twilio_set_3.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/twilio_set_4.png?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=7abc731083d3ad23608bd6a9c3c121bc" width="1600" height="826" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/twilio_set_4.png" />
</Frame>

:hash: Go to *Twilio Sandbox for WhatsApp* and verify your device by sending the given code over WhatsApp, which activates a WhatsApp session.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/twilio_set_5.png?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=79ccded726ec69c4d69b5be8fb8d98f2" width="1600" height="823" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/twilio_set_5.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/whatsapp_1.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=65e48ee2ddb1412b098e0709fdc2f3ce" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/whatsapp_1.jpg" />
</Frame>

:hash: After verifying your device, download the [Twilio Python Helper Library](https://github.com/twilio/twilio-python) or directly install it on Thonny. Then, go to *Account ➡ API keys & tokens* to get the account SID and the auth token under *Live credentials* so as to communicate with the verified phone over WhatsApp.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/twilio_set_6.png?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=cf3102896642d229a2299dbdb568f43f" width="1600" height="824" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/twilio_set_6.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/twilio_set_7.png?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=9edab9edcb0b1e86bdb9c3b9cf8540f7" width="1600" height="870" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/twilio_set_7.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/twilio_set_8.png?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=50ca1b73ef8a4e05c13551fa65f35256" width="1600" height="826" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/twilio_set_8.png" />
</Frame>

## Step 3: Producing organic fertilizers from quail manure in different decomposition stages

As mentioned earlier, utilizing composted manure as organic fertilizer can affect soil acidification, integrity, and structure depending on the manure decomposition stages (fresh, active, mature, and old). Since I needed a controlled environment manifesting varying soil structure and integrity in order to build a valid object detection model to detect excessive chemical fertilizer use, I decided to produce my organic fertilizers by composting manure.

Fortunately, I am raising quails for egg production on my balcony and have experience in composting quail manure as organic fertilizer. To examine the correlation between the chemical (synthetic) fertilizer contamination and the soil integrity differences due to the applied organic fertilizers, I started to compost quail manure and collected the manure in different decomposition stages:

* Fresh (1 month)
* Active (3 months)
* Old (6 months)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_extraction_1.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=6d26451ae006c90e18bd85379cbbf942" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_extraction_1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_extraction_2.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=b51acbd52f7a388c383793eec607f6a9" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_extraction_2.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_extraction_3.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=0450eeec0d8099c3ab2632c45756d6b5" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_extraction_3.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_extraction_4.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=ab8819868a3a39c768d4d7b4420f0795" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_extraction_4.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_extraction_5.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=6069b45cc86dc5ea42aa13752712a93c" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_extraction_5.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_extraction_6.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=f6599d66791a7ea17616526a54bd234a" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_extraction_6.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_extraction_7.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=576cc1c9c35f7369f14ab56357771b27" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_extraction_7.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_extraction_8.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=c013c7891e9da8c51b6ef2a0d5743b1b" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_extraction_8.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_extraction_9.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=2acf8635c0f592f8062e13deaa1089dc" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_extraction_9.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_extraction_10.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=e51f5c32ee6766b47228f4e045741924" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_extraction_10.jpg" />
</Frame>

After producing organic fertilizers from manure in different decomposition stages, I applied them to the soil in three separate flowerpots.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_extraction_11.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=db226838ae12de82b2cb63c0c046086f" width="750" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_extraction_11.jpg" />
</Frame>

## Step 3.1: Adding chemical fertilizers and sowing tomato seedlings

After adding organic fertilizers to the flowerpots, I ploughed the organic fertilizer-exerted soils and let them rest for a while.

Then, I added chemical (synthetic) fertilizers to each flowerpot in the same amount to examine the excessive use of chemical fertilizers depending on the soil integrity and structure altered by organic fertilizers. I applied some of the most common water-soluble chemical fertilizers:

* Calcium Nitrate
* Magnesium Sulphate
* Ammonium Sulphate
* Ammonium Phosphate

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_chemical_0.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=47700facf25fb90fab5638bd931fff12" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_chemical_0.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_chemical_1.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=95a4ea4bd2b478a809fb17d7646ec6d2" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_chemical_1.jpg" />
</Frame>

To demonstrate the detrimental effects of chemical fertilizer contamination on the environment depending on the soil integrity altered by organic fertilizers, I sowed different types of tomato seedlings in each flowerpot.

As demonstrated below, fertilizer contamination killed some tomato seedlings depending on the pollution levels based on the soil integrity and structure altered by the applied organic fertilizer (manure) decomposition stage:

* Enriched
* Unsafe
* Toxic

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_chemical_2.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=4ad45cf917ca0ea71ccac0a1bd5bb31c" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_chemical_2.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_chemical_3.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=3759988ae32e17a3fc9363a0b496276d" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_chemical_3.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_chemical_4.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=9fafb1b249c37675894e5d6f96cef91f" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_chemical_4.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_chemical_5.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=7c3e8f3b5267dbd502959a88a971a0a8" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_chemical_5.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_chemical_6.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=0ae29bb728473c0396c673b56e0efd18" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_chemical_6.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_chemical_7.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=8b3ce7e79606939f32d1647c94f51377" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_chemical_7.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_chemical_8.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=d0b7c4ba3367fcbf41d09d65c432fede" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_chemical_8.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_chemical_9.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=9dfc6550176ffbb5df0e13e9cb7b3418" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_chemical_9.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_chemical_10.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=fce4376b3d7c9b79d7d1e42a7acddf77" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/fertilizer_chemical_10.jpg" />
</Frame>

## Step 4: Utilizing Arduino Nano as a remote control to send commands via serial communication

As explained earlier, SenseCAP A1101 does not support capturing images and saving them with different labels out of the box. Therefore, I decided to build a simple remote control with Arduino Nano to transfer commands (labels) to SenseCAP A1101 via serial communication, both connected to LattePanda 3 Delta.

You can download the *AIoT\_Fertilizer\_Contamination\_Detector\_remote\_control.ino* file to try and inspect the code for transferring commands to SenseCAP A1101 via serial communication.

:hash: Firstly, download the required libraries to utilize the SH1106 OLED screen with Arduino Nano:

Adafruit\_SH1106 | [Download](https://github.com/wonho-maker/Adafruit_SH1106)

Adafruit-GFX-Library | [Download](https://github.com/adafruit/Adafruit-GFX-Library)

⭐ Include the required libraries.

```
#include &lt;SPI.h>
#include &lt;Adafruit_GFX.h>
#include &lt;Adafruit_SH1106.h>
```

⭐ Define the SH1106 OLED display (128x64) settings.

⭐ Define monochrome graphics.

```
#define OLED_MOSI      11  // MOSI (SDA)
#define OLED_CLK       13  // SCK
#define OLED_DC        9
#define OLED_CS        10
#define OLED_RESET     8
Adafruit_SH1106 display(OLED_MOSI, OLED_CLK, OLED_DC, OLED_RESET, OLED_CS);
```

⭐ Define the fertilizer contamination class (label) names and color codes.

```
String classes[] = {"Enriched", "Unsafe", "Toxic"};
int color_codes[3][3] = {{0,255,0}, {255,255,0}, {255,0,0}};
```

⭐ Initialize the default serial port (Serial) to communicate with LattePanda 3 Delta.

```
  Serial.begin(115200);
```

⭐ Initialize the SH1106 OLED display.

```
  display.begin(SH1106_SWITCHCAPVCC);
  display.display();
  delay(1000);
```

⭐ In the *home\_screen* function, show the menu interface on the SH1106 OLED display, demonstrating classes (labels).

```
void home_screen(){
  display.clearDisplay();
  display.drawBitmap((128 - 40), 20, _home, 40, 40, WHITE);
  display.setTextSize(1);
  display.setTextColor(BLACK, WHITE);
  display.setCursor(10,5);
  display.println(" Select Label: ");
  display.setTextColor(WHITE);
  display.setCursor(10,25);
  display.println("A) Enriched");
  display.setCursor(10,40);
  display.println("B) Unsafe");
  display.setCursor(10,55);
  display.println("C) Toxic");
  display.display();
  delay(100);
}
```

⭐ In the *data\_screen* function, display the selected fertilizer contamination class with its unique icon on the SH1106 OLED screen.

⭐ Then, adjust the RGB LED to the color code of the selected class.

```
void data_screen(int i){
  display.clearDisplay();
  if(i==0) display.drawBitmap((128 - 40) / 2, 0, enriched, 40, 40, WHITE);
  if(i==1) display.drawBitmap((128 - 40) / 2, 0, unsafe, 40, 40, WHITE);
  if(i==2) display.drawBitmap((128 - 40) / 2, 0, toxic, 40, 40, WHITE);
  // Print:
  int str_x = classes[i].length() * 11;
  display.setTextSize(2);
  display.setTextColor(WHITE);
  display.setCursor((128 - str_x) / 2, 48);
  display.println(classes[i]);
  display.display();
  adjustColor(color_codes[i][0], color_codes[i][1], color_codes[i][2]);
  delay(4000);
  adjustColor(255,0,255);
}
```

⭐ If one of the control buttons (A, B, or C) is pressed, transmit the selected fertilizer contamination class (label) to LattePanda 3 Delta via serial communication.

```
  if(!digitalRead(button_A)){ Serial.println("Label: Enriched"); data_screen(0); delay(2000); }
  if(!digitalRead(button_B)){ Serial.println("Label: Unsafe"); data_screen(1); delay(2000); }
  if(!digitalRead(button_C)){ Serial.println("Label: Toxic"); data_screen(2); delay(2000); }
```

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/code_1.png?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=97e6c28efa08ae6225dd69c1801353cd" width="1600" height="786" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/code_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/code_2.png?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=ac95489d7d89d65a8ee6f7496077de4b" width="1600" height="786" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/code_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/code_3.png?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=cc9be57e8eb39a167eec2f1960745f2d" width="1600" height="787" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/code_3.png" />
</Frame>

After uploading and running the code for transferring commands to LattePanda 3 Delta via serial communication:

🌱🪴📲 Arduino Nano prints notifications on the serial monitor for debugging.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/serial_remote_1.png?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=4acc0bda483531857814212974541e0e" width="1600" height="716" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/serial_remote_1.png" />
</Frame>

## Step 4.1: Displaying images on the SH1106 OLED screen

To display images (black and white) on the SH1106 OLED screen successfully, I needed to create monochromatic bitmaps from PNG or JPG files and convert those bitmaps to data arrays.

:hash: First of all, download the [LCD Assistant](http://en.radzio.dxp.pl/bitmap_converter/).

:hash: Then, upload a monochromatic bitmap and select *Vertical* or *Horizontal* depending on the screen type.

:hash: Convert the image (bitmap) and save the output (data array).

:hash: Finally, add the data array to the code and print it on the screen.

```
static const unsigned char PROGMEM toxic [] = {
0x00, 0x00, 0x81, 0x00, 0x00, 0x00, 0x03, 0x00, 0xC0, 0x00, 0x00, 0x06, 0x00, 0x60, 0x00, 0x00,
0x0C, 0x00, 0x30, 0x00, 0x00, 0x18, 0x00, 0x18, 0x00, 0x00, 0x38, 0x00, 0x1C, 0x00, 0x00, 0x30,
0x00, 0x0C, 0x00, 0x00, 0x70, 0x00, 0x0E, 0x00, 0x00, 0x70, 0x00, 0x0E, 0x00, 0x00, 0x70, 0x00,
0x0E, 0x00, 0x00, 0x70, 0x7E, 0x0E, 0x00, 0x00, 0x71, 0xFF, 0x8E, 0x00, 0x00, 0x73, 0xFF, 0xCE,
0x00, 0x00, 0x7B, 0x81, 0xDE, 0x00, 0x00, 0xFD, 0x00, 0xBF, 0x00, 0x01, 0xFC, 0x00, 0x3F, 0x80,
0x07, 0xFF, 0x00, 0xFF, 0xE0, 0x0F, 0xFF, 0xC3, 0xFF, 0xF0, 0x0F, 0xFF, 0xFF, 0xFF, 0xF0, 0x1E,
0x07, 0xE7, 0xE0, 0x78, 0x18, 0x31, 0xC3, 0x8C, 0x18, 0x30, 0x30, 0xC3, 0x0C, 0x0C, 0x30, 0x30,
0x00, 0x0C, 0x0C, 0x20, 0x30, 0x24, 0x0C, 0x04, 0x60, 0x38, 0x3C, 0x1C, 0x06, 0x40, 0x38, 0x3C,
0x1C, 0x02, 0x40, 0x1C, 0x3C, 0x38, 0x02, 0x40, 0x1C, 0x3C, 0x38, 0x02, 0x40, 0x0F, 0x3C, 0xF0,
0x02, 0x00, 0x07, 0xBD, 0xE0, 0x00, 0x00, 0x03, 0xBD, 0xC0, 0x00, 0x00, 0x01, 0x7E, 0x80, 0x00,
0x00, 0x00, 0x7E, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x00, 0x00, 0x08, 0x01, 0xFF, 0x80, 0x10, 0x04,
0x03, 0xFF, 0xC0, 0x20, 0x03, 0x9F, 0xE7, 0xF9, 0xC0, 0x00, 0xFF, 0x81, 0xFF, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
};

...

display.clearDisplay();
display.drawBitmap((128 - 40) / 2, 0, toxic, 40, 40, WHITE);
display.display();
```

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/img_convert_1.png?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=8684a7fc54f62257c818c7867b932c95" width="597" height="520" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/img_convert_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/img_convert_2.png?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=99d09921f7a34ba9e1942677f3e5b747" width="1600" height="789" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/img_convert_2.png" />
</Frame>

## Step 5.0: Setting up SenseCAP A1101 on LattePanda 3 Delta

Before proceeding with the following steps, I needed to set up SenseCAP A1101 to program it with LattePanda 3 Delta in Python.

Even though Seeed Studio provides official firmware (UF2) to capture images in Python, I needed to upgrade the BootLoader to the latest version. If your device's BootLoader version is greater than 2.0.0, you do not need to upgrade the BootLoader.

:hash: First of all, connect SenseCAP A1101 to LattePanda 3 Delta via a USB Type-C cable.

:hash: Then, double-click the boot button on SenseCAP A1101 to enter the boot mode and open the storage drive.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/A1101_data_collection_1.png?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=ac7dd98ff811f4d03ea2b6f78fb98b86" width="993" height="539" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/A1101_data_collection_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/A1101_data_collection_2.png?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=ee03e812afd4761af16c14f21eb96547" width="993" height="360" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/A1101_data_collection_2.png" />
</Frame>

:hash: After accessing the storage drive, open the *INFO\_UF2.txt* file and check for the BootLoader version.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/A1101_firmware_update_1.png?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=2d66ef76281b5ec97c666414a18eec68" width="1144" height="823" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/A1101_firmware_update_1.png" />
</Frame>

:hash: If the BootLoader version is less than 2.0.0, update it with the latest version.

:hash: Download the latest release of the BootLoader:

[*tinyuf2-sensecap\_vision\_ai\_x.x.x.bin*](https://github.com/Seeed-Studio/Seeed_Arduino_GroveAI/releases/)

:hash: This firmware controls the BL702 chip that builds the connection between the computer and the Himax chip.

:hash: After downloading the latest BootLoader version, download [the BLDevCube.exe software](https://wiki.seeedstudio.com/Train-Deploy-AI-Model-A1101/#update-bootloader), select *BL702/704/706*, and then click *Finish*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/A1101_firmware_update_2.png?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=7d6dc9f8cfbb6859e719c273f8513192" width="755" height="528" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/A1101_firmware_update_2.png" />
</Frame>

:hash: Click *View*, choose *MCU*, and enter the BootLoader firmware path on *Image File*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/A1101_firmware_update_3.png?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=35b5c871aa204805f9af5306ae239625" width="1265" height="898" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/A1101_firmware_update_3.png" />
</Frame>

:hash: Select the COM port of SenseCAP A1101. If the port is not recognized by BLDevCube, connect SenseCAP A1101 to LattePanda 3 Delta again while holding the boot button.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/A1101_firmware_update_4.png?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=4cd943b7210eb1a8ce2b7ad36c6a6a92" width="1261" height="900" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/A1101_firmware_update_4.png" />
</Frame>

:hash: Then, click *Open UART* and set *Chip Erase* to *True*.

:hash: Finally, click *Create & Program* and wait until the BootLoader is updated.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/A1101_firmware_update_5.png?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=f8ef0981fead38715fef3c1f220d205a" width="1264" height="899" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/A1101_firmware_update_5.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/A1101_firmware_update_6.png?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=afa03da21a1bfa6864375d193ffd1053" width="1263" height="901" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/A1101_firmware_update_6.png" />
</Frame>

:hash: After updating the BootLoader, download the official firmware (UF2) for capturing pictures in Python.

[*sensecap\_ai\_capture\_firmware\_vxx-xx.uf2*](https://github.com/Seeed-Studio/Seeed_Arduino_GroveAI/releases/)

:hash: Then, open the storage drive and copy the official firmware (UF2) to the drive.

:hash: As soon as the uf2 file is uploaded into the storage drive, it should disappear.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/A1101_data_collection_3.png?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=b78b99c76fbf6bfa7bc707bfc3653b0a" width="1124" height="631" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/A1101_data_collection_3.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/A1101_data_collection_3.1.png?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=1557c3b4d8376f059e1391e5859f5d89" width="1143" height="807" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/A1101_data_collection_3.1.png" />
</Frame>

:hash: Finally, install the required modules on Thonny.

*pip3 install libusb1*

*pip3 install opencv-python*

*pip3 install numpy*

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/A1101_data_collection_4.png?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=3b543ed2a11e59ea44ecdcbf1e15a206" width="1600" height="871" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/A1101_data_collection_4.png" />
</Frame>

## Step 5: Capturing fertilizer-exerted soil images w/ SenseCAP A1101 and communicating with Arduino Nano via serial communication

After setting up SenseCAP A1101 and installing the required libraries, I programmed SenseCAP A1101 via LattePanda 3 Delta to obtain the commands transferred by Arduino Nano via serial communication and capture pictures of fertilizer-exerted soils. As explained in the previous steps, SenseCAP A1101 does not provide the option to capture images with different labels out of the box.

Since I needed to assign fertilizer contamination levels as labels for each image while capturing pictures of fertilizer-exerted soils with altered soil integrity to create a valid data set for my object detection model, I utilized three control buttons connected to Arduino Nano so as to choose among classes and transfer commands via serial communication. After selecting a fertilizer contamination class by pressing a control button, Arduino Nano transmits the selected class to LattePanda 3 Delta via serial communication.

* Control Button (A) ➡ Enriched
* Control Button (B) ➡ Unsafe
* Control Button (C) ➡ Toxic

You can download the *A1101\_data\_img\_collection.py* file to try and inspect the code for obtaining commands via serial communication and capturing images with SenseCAP A1101.

To decrypt the image buffer generated by SenseCAP A1101, I modified [these functions](https://github.com/Seeed-Studio/Seeed_Arduino_GroveAI/blob/master/tools/capture_images_script.py) provided by Seeed Studio.

Firstly, I created a class named *A1101\_data\_img\_collection* to bundle the following functions under a specific structure.

⭐ Include the required modules.

```
import cv2
import serial
from threading import Thread
from time import sleep
import os
from PIL import Image
from io import BytesIO
import usb1
import numpy as np
import datetime
```

⭐ In the ***init*** function: ⭐ Define the required settings to obtain generated data packets from SenseCAP A1101.

⭐ Get the connected USB device context.

⭐ Initialize serial communication with Arduino Nano to obtain the transferred commands.

⭐ Initialize and test the SenseCAP A1101 USB connection.

```
class A1101_data_img_collection():
    def __init__(self):
        # Define the required settings to obtain information from SenseCAP A1101 LoRaWAN Vision AI Sensor.
        self.WEBUSB_JPEG = (0x2B2D2B2D)
        self.WEBUSB_TEXT = 0x0F100E12
        self.VendorId = 0x2886
        self.ProductId = [0x8060, 0x8061]
        self.img_buff = bytearray()
        self.buff_size = 0
        self.time_out = 1000
        # Get the connected USB device context.
        self.context = usb1.USBContext()
        # Initialize serial communication with Arduino Nano to obtain the given commands.
        self.arduino_nano = serial.Serial("COM7", 115200, timeout=2000)
        # Initialize and test SenseCAP A1101 connection.
        self.get_rlease_device(False)
        self.disconnect()
```

⭐ In the *read\_data* function:

⭐ If SenseCAP A1101 is accessible, get the data endpoints and all transferred data objects.

⭐ Check for any submitted data object in the received data packet.

```
    def read_data(self):
        # If SenseCAP A1101 is accessible:
        with self.handle.claimInterface(2):
            # Get the data endpoints.
            self.handle.setInterfaceAltSetting(2, 0)
            self.handle.controlRead(0x01 &lt;&lt; 5, request=0x22, value=0x01, index=2, length=2048, timeout=self.time_out)
            # Get all transferred data objects.
            transfer_list = []
            for _ in range(1):
                transfer = self.handle.getTransfer()
                transfer.setBulk(usb1.ENDPOINT_IN | 2, 2048, callback=self.processReceivedData, timeout=self.time_out)
                transfer.submit()
                transfer_list.append(transfer)
            # Check for any submitted data object in the received data packet.
            while any(x.isSubmitted() for x in transfer_list):
                self.context.handleEvents()
```

⭐ In the *processReceivedData* function:

⭐ If SenseCAP A1101 generates a data packet successfully, process the received data packet.

⭐ Decrypt the captured image buffer from the processed data packet.

⭐ Resubmit the data packet after processing to avoid errors.

```
    def processReceivedData(self, transfer):
        # If SenseCAP A1101 generates a data packet successfully, process the received information.
        if transfer.getStatus() != usb1.TRANSFER_COMPLETED:
            # transfer.close()
            return
        # Extract the captured image from the processed data packet.
        data = transfer.getBuffer()[:transfer.getActualLength()]
        self.convert_and_show_img(data)
        # Resubmit the data packet after processing to avoid errors.
        transfer.submit()
```

⭐ In the *convert\_and\_show\_img* function:

⭐ Convert the received data packet to an image buffer.

⭐ If the received data packet is converted to an image buffer successfully, display the generated image on the screen to create a real-time video stream.

⭐ Stop the video stream when requested.

⭐ Store the latest image buffer (frame) captured by SenseCAP A1101.

```
    def convert_and_show_img(self, data: bytearray):
        # Convert the received data packet.
        if (len(data) == 8) and (int.from_bytes(bytes(data[:4]), 'big') == self.WEBUSB_JPEG):
            self.buff_size = int.from_bytes(bytes(data[4:]), 'big')
            self.img_buff = bytearray()
        elif (len(data) == 8) and (int.from_bytes(bytes(data[:4]), 'big') == self.WEBUSB_TEXT):
            self.buff_size = int.from_bytes(bytes(data[4:]), 'big')
            self.img_buff = bytearray()
        else:
            self.img_buff = self.img_buff + data
        # If the received data packet is converted to an image buffer successfully, display the generated image on the screen.
        if self.buff_size == len(self.img_buff):
            try:
                img = Image.open(BytesIO(self.img_buff))
                img = np.array(img)
                cv2.imshow('A1101_data_img_collection', cv2.cvtColor(img,cv2.COLOR_RGB2BGR))
                # Stop the video stream if requested.
                if cv2.waitKey(1) != -1:
                    cv2.destroyAllWindows()
                    print("\nCamera Feed Stopped!")
                # Store the latest frame captured by SenseCAP A1101.
                self.latest_frame = img
            except:
                self.img_buff = bytearray()
                return
```

⭐ In the *connect* function, connect to SenseCAP A1101 if detected successfully.

```
    def connect(self):
        # Connect to SenseCAP A1101.
        self.handle = self.get_rlease_device(True)
        if self.handle is None:
            print('\nSenseCAP A1101 not detected!')
            return False
        with self.handle.claimInterface(2):
            self.handle.setInterfaceAltSetting(2, 0)
            self.handle.controlRead(0x01 &lt;&lt; 5, request=0x22, value=0x01, index=2, length=2048, timeout=self.time_out)
            print('\nSenseCAP A1101 detected successfully!')
        return True
```

⭐ In the *disconnect* function, reset the USB connection between SenseCAP A1101 and LattePanda 3 Delta.

```
    def disconnect(self):
        # Reset the SenseCAP A1101 connection.
        try:
            print('Resetting the device connection... ')
            with usb1.USBContext() as context:
                handle = context.getByVendorIDAndProductID(self.VendorId, self.d_ProductId, skip_on_error=False).open()
                handle.controlRead(0x01 &lt;&lt; 5, request=0x22, value=0x00, index=2, length=2048, timeout=self.time_out)
                handle.close()
                print('Device connection has been reset successfully!')
            return True
        except:
            return False
```

⭐ In the *get\_rlease\_device* function:

⭐ Establish the USB connection between SenseCAP A1101 and LattePanda 3 Delta.

⭐ Retrieve the device information and check if there is a successfully connected device.

⭐ Open or close the SenseCAP A1101 data transmission.

```
    def get_rlease_device(self, get=True):
        # Establish the SenseCAP A1101 connection.
        print('*' * 50)
        print('Establishing connection...')
        # Get the device information.
        for device in self.context.getDeviceIterator(skip_on_error=True):
            product_id = device.getProductID()
            vendor_id = device.getVendorID()
            device_addr = device.getDeviceAddress()
            bus = '->'.join(str(x) for x in ['Bus %03i' % (device.getBusNumber(),)] + device.getPortNumberList())
            # Check if there is a connected device.
            if(vendor_id == self.VendorId) and (product_id in self.ProductId):
                self.d_ProductId = product_id
                print('\r' + f'\033[4;31mID {vendor_id:04x}:{product_id:04x} {bus} Device {device_addr} \033[0m', end='')
                # Turn on or off SenseCAP A1101.
                if get:
                    return device.open()
                else:
                    device.close()
                    print('\r' + f'\033[4;31mID {vendor_id:04x}:{product_id:04x} {bus} Device {device_addr} CLOSED\033[0m', flush=True)
```

⭐ In the *get\_transferred\_data\_packets* function, obtain the transferred commands from Arduino Nano via serial communication, including fertilizer contamination classes (labels).

```
    def get_transferred_data_packets(self):
        # Obtain the transferred commands from Arduino Nano via serial communication, including fertilizer hazard classes (labels).
        if self.arduino_nano.in_waiting > 0:
            command = self.arduino_nano.readline().decode("utf-8", "ignore").rstrip()
            if(command.find("Enriched") >= 0):
                print("\nCapturing an image! Label: Enriched")
                self.save_img_sample("Enriched")
            if(command.find("Unsafe") >= 0):
                print("\nCapturing an image! Label: Unsafe")
                self.save_img_sample("Unsafe")
            if(command.find("Toxic") >= 0):
                print("\nCapturing an image! Label: Toxic")
                self.save_img_sample("Toxic")
        sleep(1)
```

⭐ In the *save\_img\_sample* function, depending on the obtained class name, save the latest stored image buffer (frame) captured by SenseCAP A1101 to the *samples* folder by appending the current date & time to its file name:

*Enriched\_IMG\_20230530\_165521.jpg*

```
    def save_img_sample(self, _class):
        date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = './samples/{}_IMG_{}.jpg'.format(_class, date)
        # If requested, save the recently captured image (latest frame) as a sample.
        cv2.imwrite(filename, self.latest_frame)
        print("\nSample Saved Successfully: " + filename)
```

:hash: Since displaying a real-time video stream generated by SenseCAP A1101 and communicating with Arduino Nano to obtain commands via serial communication cannot be executed in a single loop, I utilized the [Python Thread](https://realpython.com/intro-to-python-threading/) class to run simultaneous processes (functions).

```
soil = A1101_data_img_collection()

# Define and initialize threads.
def A1101_camera_feed():
    soil.collect_data()

def activate_received_commands():
    while True:
        soil.get_transferred_data_packets()

Thread(target=A1101_camera_feed).start()
Thread(target=activate_received_commands).start()
```

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/code_img_1.png?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=7d972672a105c3e733eabb6e7fd03975" width="1600" height="854" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/code_img_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/code_img_2.png?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=9dff3e7d05a14589bcf08421c3ac400b" width="1600" height="858" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/code_img_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/code_img_3.png?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=3ffa53203cb7dc7db10b22511f91fff9" width="1600" height="852" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/code_img_3.png" />
</Frame>

## Step 5.1: Saving the captured images as samples on LattePanda 3 Delta

After uploading and running the code for obtaining commands via serial communication and capturing images with SenseCAP A1101 on LattePanda 3 Delta:

🌱🪴📲 If the device works accurately, the remote control shows the menu interface on the SH1106 OLED display and turns the RGB LED to magenta.

* A) Enriched
* B) Unsafe
* C) Toxic

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/collect_1.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=7d008318eaa6f9c572bb4b576e340384" width="750" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/collect_1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/collect_2.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=ef7bb98ab8e7d153e65ff82707776bc5" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/collect_2.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/collect_3.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=abc72158125893a5ec6b1260b8a279c0" width="750" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/collect_3.jpg" />
</Frame>

🌱🪴📲 If the control button (A) is pressed, Arduino Nano adds *Enriched* as the selected fertilizer contamination class to the command, transfers the modified command to LattePanda 3 Delta via serial communication, displays the selected fertilizer contamination class with its unique monochrome icon on the SH1106 OLED screen, and turns the RGB LED to green.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/collect_4.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=51461cf607959229ceb4924743f03757" width="750" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/collect_4.jpg" />
</Frame>

🌱🪴📲 If the control button (B) is pressed, Arduino Nano adds *Unsafe* as the selected fertilizer contamination class to the command, transfers the modified command to LattePanda 3 Delta via serial communication, displays the selected fertilizer contamination class with its unique monochrome icon on the SH1106 OLED screen, and turns the RGB LED to yellow.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/collect_5.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=84912c530555e7fc20636c7bced56214" width="750" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/collect_5.jpg" />
</Frame>

🌱🪴📲 If the control button (C) is pressed, Arduino Nano adds *Toxic* as the selected fertilizer contamination class to the command, transfers the modified command to LattePanda 3 Delta via serial communication, displays the selected fertilizer contamination class with its unique monochrome icon on the SH1106 OLED screen, and turns the RGB LED to red.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/collect_6.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=11da3d985a74a0d3db1b3c676ecc8f67" width="750" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/collect_6.jpg" />
</Frame>

🌱🪴📲 When LattePanda 3 Delta receives a command transferred by Arduino Nano via serial communication, including the selected fertilizer contamination class, it saves the latest stored image buffer generated by SenseCAP A1101 to the *samples* folder depending on the selected class name by appending the current date & time to its file name:

*Enriched\_IMG\_20230530\_165528.jpg*

*Unsafe\_IMG\_20230530\_170541.jpg*

*Toxic\_IMG\_20230530\_171326.jpg*

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/collect_7.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=690a821a7d63c60a350ae3115403467f" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/collect_7.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/edgeimpulse/.assets/images/sensecap-a1101-lorawan-soil-quality/gif_collect.gif" />
</Frame>

🌱🪴📲 Also, LattePanda 3 Delta shows the real-time video stream generated by SenseCAP A1101 while capturing pictures and prints notifications with the saved image file paths on the shell for debugging.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_sample_collect_1.png?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=ea28a9c1fbba4c2ba9f30f39f76f9898" width="1600" height="871" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_sample_collect_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_sample_collect_2.png?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=05b4cbf46312df88ec167c405d26745b" width="1600" height="869" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_sample_collect_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_sample_collect_3.png?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=44031d8d8fcd636272f9ccdd90ece3b1" width="1600" height="871" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_sample_collect_3.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_sample_collect_4.png?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=1bd994775ce3bb26943ddb36a8cd65a7" width="1600" height="871" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_sample_collect_4.png" />
</Frame>

After capturing images of fertilizer-exerted soils in three separate flowerpots for nearly two months, whose soil integrity and structure were altered in relation to the applied organic fertilizer (manure) decomposition stage, I managed to construct my data set with eminent validity and veracity.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/data_collect_1.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=b5a689d37ef84aa4250a080d31d18641" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/data_collect_1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/data_collect_2.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=5a991989355acb34a338c17847206703" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/data_collect_2.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/data_collect_3.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=e889d2964308a99fa496cba50d5cea5a" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/data_collect_3.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/data_collect_4.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=787e75d9192bc0caf06b726cf763d6bd" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/data_collect_4.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/data_collect_5.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=04e9118c20c352f55c952f8b4d6af57a" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/data_collect_5.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/data_collect_6.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=d9414643d5cd8f0aca57acefe1a46647" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/data_collect_6.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/data_collect_7.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=2abdf6167066e1c22a905e7f68baebed" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/data_collect_7.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/data_collect_8.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=a8811913f2f31049227f834fdce5c747" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/data_collect_8.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/data_collected.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=2f1aa46547180f98e5c2d04336fa9d6d" width="1600" height="577" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/data_collected.png" />
</Frame>

## Step 6: Building an object detection (FOMO) model with Edge Impulse

As explained in the previous steps, I needed a controlled environment manifesting varying soil structure and integrity in order to build a valid object detection model. Therefore, I applied composted quail manure collected in different decomposition stages (fresh, active, mature, and old) as organic fertilizers to alter soil acidification, integrity, and structure in three separate flowerpots. Then, I added chemical fertilizers to each flowerpot in the same amount to examine the excessive use of chemical fertilizers.

When I completed capturing images of fertilizer-exerted soils in three separate flowerpots and storing them on LattePanda 3 Delta, I started to work on my object detection (FOMO) model to detect the excessive use of chemical fertilizers in relation to organic fertilizers so as to prevent their hazardous effects on the environment and our health.

Since Edge Impulse supports almost every microcontroller and development board due to its model deployment options, I decided to utilize Edge Impulse to build my object detection model. Also, Edge Impulse provides an elaborate machine learning algorithm (FOMO) for running more accessible and faster object detection models on edge devices such as SenseCAP A1101.

[Edge Impulse FOMO (Faster Objects, More Objects)](/studio/projects/learning-blocks/blocks/object-detection/fomo) is a novel machine learning algorithm that brings object detection to highly constrained devices. FOMO models can count objects, find the location of the detected objects in an image, and track multiple objects in real time, requiring up to 30x less processing power and memory than MobileNet SSD or YOLOv5.

Even though Edge Impulse supports JPG or PNG files to upload as samples directly, each target object in a training or testing sample needs to be labeled manually. Therefore, I needed to follow the steps below to format my data set so as to train my object detection model accurately:

* Data Scaling (Resizing)
* Data Labeling

Since I added fertilizer contamination levels based on the soil integrity and structure altered by the applied organic fertilizer (manure) to the file names while capturing images of soils in the mentioned flowerpots, I preprocessed my data set effortlessly to label each target object on an image sample on Edge Impulse by utilizing the contamination classes:

* Enriched
* Unsafe
* Toxic

Plausibly, Edge Impulse allows building predictive models optimized in size and accuracy automatically and deploying the trained model as a supported firmware (UF2) for SenseCAP A1101. Therefore, after scaling (resizing) and preprocessing my data set to label target objects, I was able to build an accurate object detection model to detect chemical fertilizer overuse, which runs on SenseCAP A1101 without any additional requirements.

You can inspect [my object detection (FOMO) model on Edge Impulse](https://studio.edgeimpulse.com/public/233660/latest) as a public project.

## Step 6.1: Uploading images (samples) to Edge Impulse and labeling objects

After collecting training and testing image samples, I uploaded them to my project on Edge Impulse. Then, I labeled each target object on the image samples.

:hash: First of all, sign up for [Edge Impulse](https://www.edgeimpulse.com/) and create a new project.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_1.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=3fd4f28a06c39c72fa83371c51e16a4d" width="1600" height="811" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_1.png" />
</Frame>

:hash: To be able to label image samples manually on Edge Impulse for object detection models, go to *Dashboard ➡ Project info ➡ Labeling method* and select *Bounding boxes (object detection)*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_2.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=9decbd1888030c0380c818c0a59fbf80" width="1600" height="785" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_2.png" />
</Frame>

:hash: Navigate to the *Data acquisition* page and click the *Upload data* button.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_3.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=a2e7b24eb988d9886d162c031979dbe2" width="1600" height="786" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_3.png" />
</Frame>

:hash: Then, choose the data category (training or testing), select image files, and click the *Upload data* button.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_4.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=91558b62169be8a68c876f6cee65206c" width="1600" height="783" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_4.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_5.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=f98634913de1de217e5fe83391ab237e" width="1600" height="823" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_5.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_6.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=358a0927ce0d894cd73f606c3ec85e38" width="1600" height="822" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_6.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_7.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=9fb3c6ea9cb2321c0e117b99a95ca1a0" width="1600" height="823" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_7.png" />
</Frame>

After uploading my data set successfully, I labeled each target object on the image samples by utilizing the fertilizer contamination classes. In Edge Impulse, labeling an object is as easy as dragging a box around it and entering a class. Also, Edge Impulse runs a tracking algorithm in the background while labeling objects, so it moves the bounding boxes automatically for the same target objects in different images.

:hash: Go to *Data acquisition ➡ Labeling queue (Object detection labeling)*. It shows all unlabeled items (training and testing) remaining in the given data set.

:hash: Finally, select an unlabeled item, drag bounding boxes around target objects, click the *Save labels* button, and repeat this process until all samples have at least one labeled target object.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_8.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=e0517595bdf1db900890605bf235e353" width="1600" height="820" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_8.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_9.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=4dee434b07e7ef3939fe24fe08caba41" width="1600" height="824" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_9.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_10.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=ca27e83a7f914875ace71139315ffc83" width="1600" height="823" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_10.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_11.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=d58faf9f390aec048be04624c1652f19" width="1600" height="823" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_11.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_12.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=76099d6b9f4d8db917d5ccdeaa9db994" width="1600" height="823" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_12.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_13.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=e784987b3ca9e6b974240d45653ebc77" width="1600" height="821" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_13.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_13.1.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=94d591a952802e80d036b660608ef9b0" width="1600" height="823" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_13.1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_13.2.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=2449c235171b045be6ea86bcf4fe2aae" width="1600" height="823" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_13.2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_14.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=3540ef57398c15f7e979f1bd14d22cfd" width="1600" height="824" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_14.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_15.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=245466007d39bd53d9c466ed62d13166" width="1600" height="823" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_15.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_16.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=cf3bd9541c446c689cd85d8929d01729" width="1600" height="819" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_16.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_17.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=6662357ebf1a8c02878a9ea1fac1fae9" width="1600" height="823" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_17.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_18.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=191a8b9b5d7904299e697dc66e7cc46d" width="1600" height="824" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_18.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_19.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=37d3dd714d67753f9a4db2ddff322304" width="1600" height="823" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_19.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_20.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=881c25f264f4ddb508507b6ad00aaeff" width="1600" height="819" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_20.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_21.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=bf4fe3b8eb093f66b1b38c02d3990184" width="1600" height="819" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_21.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_22.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=63dc22cb4b8f5468c2e6560e8589fb2b" width="1600" height="820" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_22.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_23.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=0abfe2d02a0129a63528861e5bc54d0b" width="1600" height="825" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_23.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_24.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=e948dea1d1d80ef51c04ed4e8a8ce457" width="1600" height="820" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_24.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_25.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=bd45dce4366045116454e17b3aa4ba6f" width="1600" height="821" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_25.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_26.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=6bd147d7f5cd6dec6c65b4cbb6e77053" width="1600" height="821" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_set_26.png" />
</Frame>

## Step 6.2: Training the FOMO model on the fertilizer-exerted soil images

After labeling target objects on my training and testing samples successfully, I designed an impulse and trained it on detecting the excessive use of chemical fertilizers in relation to organic fertilizers.

An impulse is a custom neural network model in Edge Impulse. I created my impulse by employing the *Image* preprocessing block and the *Object Detection (Images)* learning block.

The *Image* preprocessing block optionally turns the input image format to grayscale and generates a features array from the raw image.

The *Object Detection (Images)* learning block represents a machine learning algorithm that detects objects on the given image, distinguished between model labels.

:hash: Go to the *Create impulse* page and set image width and height parameters to 120. Then, select the resize mode parameter as *Fit shortest axis* so as to scale (resize) given training and testing image samples.

:hash: Select the *Image* preprocessing block and the *Object Detection (Images)* learning block. Finally, click *Save Impulse*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_train_1.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=9e13a36d2ed9ce629c902973cd49cd1e" width="1600" height="826" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_train_1.png" />
</Frame>

:hash: Before generating features for the object detection model, go to the *Image* page and set the *Color depth* parameter as *Grayscale*. Then, click *Save parameters*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_train_2.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=2f4b8f805540aa97201bf508eeb3f443" width="1600" height="823" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_train_2.png" />
</Frame>

:hash: After saving parameters, click *Generate features* to apply the *Image* preprocessing block to training image samples.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_train_3.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=af354ffdfaa0bb1168210c3ccc057dfd" width="1600" height="821" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_train_3.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_train_4.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=920af31b156f30b10d0172c03f0695d6" width="1600" height="809" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_train_4.png" />
</Frame>

After conducting preliminary experiments with my object detection model, I noticed some target objects with the *Enriched* label decreased the model accuracy when being separated while the validation split.

Therefore, I applied a metadata key to the erroneous samples to prevent leaking data between my train and validation sets.

:hash: To add a metadata key, go to *Data acquisition ➡ Dataset ➡ Training*.

:hash: Then, select the faulty sample and click the *Add new metadata* button.

:hash: Finally, enter the metadata key and value parameters:

* confused\_soil ➡ confused\_soil

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_meta_1.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=cf7d701ccfa30318384a2bc98768e9df" width="1600" height="810" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_meta_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_meta_2.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=e506ef4e3a9f891ad29027b4e1310954" width="1600" height="821" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_meta_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_meta_3.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=5bc4103395a19ae8918cbe1178f68984" width="1600" height="827" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_meta_3.png" />
</Frame>

:hash: After adding metadata parameters to the faulty samples, navigate to the *Object detection* page and click *Start training*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_train_5.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=ae5d12bdd6bbad19c777df46ab36a814" width="1090" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_train_5.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_train_6.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=d5293ca727dfe17d775b2c16978a4119" width="864" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_train_6.png" />
</Frame>

According to my experiments with my object detection model, I modified the neural network settings and architecture to build an object detection model with high accuracy and validity:

📌 Neural network settings:

* Number of training cycles ➡ 90
* Learning rate ➡ 0.052
* Validation set size ➡ 5
* Split train/validation set on metadata key ➡ confused\_soil

📌 Neural network architecture:

* FOMO (Faster Objects, More Objects) MobileNetV2 0.35

After generating features and training my FOMO model with training samples, Edge Impulse evaluated the F1 score (accuracy) as *77.8%*.

The F1 score (accuracy) is approximately *77.8%* due to the modest volume of training samples of varying fertilizer-exerted soil structures with a similar color scheme, excluding the applied chemical fertilizer colors. Due to this soil color scheme, I noticed the model misinterprets some *Enriched* and *Toxic* target objects. Therefore, I am still collecting samples to improve my data set.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_train_7.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=96c83b8a079437f9860a980d279a0c57" width="1600" height="824" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_train_7.png" />
</Frame>

## Step 6.3: Evaluating the model accuracy and deploying the model

After building and training my object detection model, I tested its accuracy and validity by utilizing testing image samples.

The evaluated accuracy of the model is *80%*.

:hash: To validate the trained model, go to the *Model testing* page and click *Classify all*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_test_1.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=28f96ed853f74c3445729d6c570a916f" width="1600" height="821" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_test_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_test_2.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=00e6a09040db31e01e4c65bba2834655" width="1600" height="824" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_test_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_test_3.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=1e95e5ca663a04326f469f707ef235fb" width="1600" height="826" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_test_3.png" />
</Frame>

After validating my object detection model, I deployed it as a fully optimized SenseCAP A1101 firmware (UF2) supported by Seeed Studio.

:hash: To deploy the validated model as the supported SenseCAP A1101 firmware (UF2), navigate to the *Deployment* page and search for *SenseCAP A1101*.

:hash: Then, choose the *Quantized (int8)* optimization option to get the best performance possible while running the deployed model.

:hash: Finally, click *Build* to download the model as the supported SenseCAP A1101 firmware — [firmware.uf2](/hardware/devices/seeed-sensecap-a1101#deploying-back-to-device).

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_deploy_1.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=e324d26a5cf29abe2f6d753c08a1152b" width="1600" height="825" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_deploy_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_deploy_2.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=c2b207261ee4e28e27169177394aa980" width="1600" height="823" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_deploy_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/yqewpHUBf8fNwyUZ/.assets/images/sensecap-a1101-lorawan-soil-quality/edge_deploy_3.png?fit=max&auto=format&n=yqewpHUBf8fNwyUZ&q=85&s=7812a9798ff85e4988de58f8483b868d" width="1600" height="824" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/edge_deploy_3.png" />
</Frame>

## Step 7: Connecting SenseCAP A1101 to SenseCAP Mate App and setting up the Edge Impulse FOMO model

After downloading the supported SenseCAP A1101 firmware — *firmware.uf2*, follow the instructions shown in Step 5.0 to upload the Edge Impulse object detection model to the storage drive of SenseCAP A1101.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_model_set_1.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=f9cedda64efe9c43f0dc50970427ac53" width="1121" height="882" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_model_set_1.png" />
</Frame>

After uploading the model successfully:

:hash: Install and open the [SenseCAP Mate](https://wiki.seeedstudio.com/One-Stop-Model-Training-with-Edge-Impulse/#configure-your-model-on-the-sensecap-mate) application provided by Seeed Studio.

:hash: Select the server location as *Global* and create a new account.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_1.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=e4b78cf28dbef296aac86ede9b1b650c" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_2.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=85b0f14def18af1ee663029a71e17623" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_2.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_3.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=a4731085bd3990e14c88133f9a5884ae" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_3.jpg" />
</Frame>

:hash: Under *Config* screen, select *Vision AI Sensor*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_4.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=e8aaae17d2eadb4a216efa2e87b10bff" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_4.jpg" />
</Frame>

:hash: Press and hold the configuration button on the SenseCAP A1101 for 3 seconds to activate the Bluetooth pairing mode.

:hash: Then, click the *Setup* button and scan for nearby SenseCAP A1101 devices.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_5.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=2aba86d521fd5b6a25e38ff6fd82c03f" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_5.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_6.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=8a250dd4e363d2153fa0abb0f109820f" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_6.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_7.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=33c180131fd6f3ca2c7314013c29a243" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_7.jpg" />
</Frame>

:hash: If the device software version is not the latest release, click the *Update* button to upgrade the software version.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_8.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=db76fe20344a287746f8ad912d242333" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_8.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_9.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=250b7c1c1e92e624df49fa7c228f9e02" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_9.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_10.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=dd0ef20b930b3731211370945eabb28d" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_10.jpg" />
</Frame>

:hash: After updating the software version, go to *Setting* and select:

* Algorithm ➡ Object Detection
* AI Model ➡ User Defined 1
* Score Threshold ➡ 0.6
* Uplink Interval (min) ➡ 5
* Packet Policy ➡ 2C+1N

:hash: Then, select one of the supported frequency plans depending on your region — e.g., EU868.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_11.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=fac89ff312ed0820d7fb73b657018a3e" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_11.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_12.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=605166359e46bca55fe910d3ee0c7516" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_12.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_13.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=779fb620733701a811cacf22f07cb7cb" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_13.jpg" />
</Frame>

:hash: Under *Platform*, select *SenseCAP for Helium* to utilize the Helium network to transfer data packets to the SenseCAP Portal officially supported by Seeed Studio.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_14.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=70a8eadf152a408dbfc5cb5d6d9a38c0" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_14.jpg" />
</Frame>

:hash: Finally, click *Send ➡ Back to Home* to complete the device configuration.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_15.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=96f415f8c3ae3b90b8d59957277322c3" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_set_15.jpg" />
</Frame>

:hash: After configuring the new device settings, go to *General* and click *Detect* under *AI Preview* so as to inspect the model detection results generated by the uploaded Edge Impulse object detection model.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_model_1.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=5b5d224d9dc730fff8abbab2173352e7" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_model_1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_model_2.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=09bfca620acfb2711a4fde531af16ec9" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_model_2.jpg" />
</Frame>

## Step 8: Transferring the detection results to the SenseCAP Portal via the Helium LongFi Network

After seeing the Edge Impulse model detection results on the SenseCAP Mate application, I needed to bind SenseCAP A1101 as a new device to my account in order to transfer the detection results as data packets to the SenseCAP Portal via the Helium LongFi Network.

:hash: Open the SenseCAP Mate application.

:hash: Under *Device*, click the *Add device* button.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_add_1.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=c86c3664db1cccae9750217480cfc8ea" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_add_1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_add_2.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=e25c4448b3acfbb912222371abe3d419" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_add_2.jpg" />
</Frame>

:hash: Then, scan the QR code on the SenseCAP A1101 to bind it to your account.

:hash: If the QR code sticker is damaged, you can also enter the device EUI manually.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_add_3.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=dd76fa2cecf3aecd638f0b149cc6512e" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_add_3.jpg" />
</Frame>

:hash: After entering the added device name, SenseCAP A1101 starts sending the model detection results to the SenseCAP Portal via the Helium network.

:hash: SenseCAP A1101 runs the Edge Impulse model and uploads the model detection results to the SenseCAP Portal according to the configured *Uplink Interval* parameter, in this case, every five minutes.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_add_4.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=dd3c544fd0aad5b9fdd0d87f2cd90d47" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_add_4.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_add_5.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=a72a6065b15357368432e0aa8a153d4f" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_add_5.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_add_6.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=43b3b91d89fc5c545612733c66419d11" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensemate_add_6.jpg" />
</Frame>

After binding SenseCAP A1101 to the SenseCAP Portal successfully, it finds the nearest Helium gateway and transfers data packets to the SenseCAP Portal automatically.

:hash: To inspect the transferred model detection results on the SenseCAP Portal web dashboard, go to [SenseCAP Portal (web)](https://sensecap.seeed.cc/).

:hash: Then, log in with the same account registered to the SenseCAP Mate App.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_lorawan_web_set_1.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=d1cd48acacee536512ec3dbbf64f571d" width="1600" height="826" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_lorawan_web_set_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_lorawan_web_set_2.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=62ce3e3d07d2be383d4e3796ddf462f7" width="1600" height="826" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_lorawan_web_set_2.png" />
</Frame>

:hash: Under *Devices*, select *Sensor Node* to inspect the bound SenseCAP devices.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_lorawan_web_set_3.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=abd4b9fa417cbf38a0849d28b0a4adee" width="1600" height="828" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_lorawan_web_set_3.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_lorawan_web_set_4.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=878431cf4ad1a1dbd199fcb20a3040c0" width="1600" height="815" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_lorawan_web_set_4.png" />
</Frame>

:hash: To see all data packets transferred by the bound devices, go to *Data ➡ Table*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_lorawan_web_set_5.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=a3a1a50001c9ccfcfbf2990a7a68b3ce" width="1600" height="826" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_lorawan_web_set_5.png" />
</Frame>

As explained earlier, Seeed Studio provides the SenseCAP HTTP API to obtain registered data records from the SenseCAP Portal via HTTP GET requests.

:hash: To retrieve the stored model detection results on the SenseCAP Portal via the SenseCAP HTTP API, go to *Security ➡ Access API keys*.

:hash: Then, click the *Create Access Key* button and copy the generated *API ID* and *Access API keys* parameters for further usage.

You can inspect Step 9 to get more detailed information regarding the SenseCAP HTTP API.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_lorawan_web_set_6.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=3ea639ca3e356d5a1968c111cf7168a8" width="1600" height="828" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_lorawan_web_set_6.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_lorawan_web_set_7.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=7931ba18b95c608678cdadf7c7ccf438" width="1600" height="826" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_lorawan_web_set_7.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_lorawan_web_set_8.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=f0791e2693332434cb840028fc5bcd9a" width="1600" height="824" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_lorawan_web_set_8.png" />
</Frame>

## Step 8.1: Activating SenseCAP M2 data-only LoRaWAN gateway (EU868)

After binding SenseCAP A1101 to your SenseCAP Portal account, it should automatically connect to the nearest Helium gateway to transfer the model detection results via the Helium LongFi Network.

Nonetheless, if the Helium network does not cover your surroundings, you may need to purchase a Helium gateway.

Since Seeed Studio provides various Helium gateways compatible with the SenseCAP Portal, I wanted to show how to activate one of SenseCAP gateways — SenseCAP M2 data-only LoRaWAN indoor gateway (EU868).

:hash: First of all, go to [Helium World](https://world.helium.com/en/network/iot) to check whether a Helium gateway covers your surroundings.

:hash: If so, you do not need to follow the steps below.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_lorawan_network_set_1.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=a236b75db9d216745c6741041708aae8" width="1600" height="824" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_lorawan_network_set_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_lorawan_network_set_2.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=d79f49dac5a5c1f542ae91440bb3c31d" width="1600" height="824" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_lorawan_network_set_2.png" />
</Frame>

:hash: To activate SenseCAP M2 data-only gateway, follow [the Quick Start instructions](https://www.sensecapmx.com/docs/sensecap-m2-data-only/m2-quick-start/) provided by Seeed Studio.

:hash: After setting up the SenseCAP M2 data-only gateway and connecting it to the Internet via an ethernet cable, you should be able to update the device firmware during the first boot and start transferring data packets in less than 30 minutes.

:hash: Do not forget that Helium Wallet will deduct a $10 onboarding fee and a $5 location asserting fee to activate the M2 data-only gateway to transfer data packets via the Helium LongFi Network.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/m2_set_1.jpg?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=cdf6179ee35d999e83d426489b426cea" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/m2_set_1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/m2_set_2.jpg?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=2a065a5e5393cc50f7aaab82660c0897" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/m2_set_2.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/m2_set_3.jpg?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=4acd9dc755993e0586b36476aa5bdb25" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/m2_set_3.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/m2_set_4.jpg?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=fb1fc4ec26b008114297685b85ad553d" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/m2_set_4.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/m2_set_5.jpg?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=10d7d79df591c6e9c273e8e8d9805180" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/m2_set_5.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/m2_set_6.jpg?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=f6a7b6e9bc06dfe19a4985e6efc29a8d" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/m2_set_6.jpg" />
</Frame>

## Step 9: Developing a Python application to transfer the model detection results via WhatsApp

To provide an outstanding user experience while informing the user of the model detection results via WhatsApp over LoRaWAN, I developed a full-fledged application from scratch in Python.

This application obtains the model detection results from the SenseCAP Portal by making HTTP GET requests to the SenseCAP HTTP API. Then, the application utilizes Twilio's WhatsApp API to transfer the retrieved model detection results to the verified phone number in order to inform the user of the excessive chemical fertilizer use in relation to organic fertilizers.

You can download the *A1101\_whatsapp\_interface.py* file to try and inspect the code for obtaining model detection results from the SenseCAP Portal and informing the user of the retrieved detection results via WhatsApp.

:hash: Since Seeed Studio provides the SenseCAP HTTP API for communicating with their various sensors and products, get the correct *Sensor ID* and *Measurement ID* parameters from [SenseCAP Document Center](https://sensecap-docs.seeed.cc/sensor_types_list.html) so as to obtain the data records that SenseCAP A1101 registered to the SenseCAP Portal via the Helium LongFi Network.

* 2036
* 4175 ➡ AI Detection No.01

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_HTTP_API_1.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=107ced899ed9c969782773427d393086" width="1600" height="821" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_HTTP_API_1.png" />
</Frame>

:hash: Since SenseCAP A1101 generates the model detection results in a specific format, I needed to parse the retrieved detection result to obtain the predicted class and the accuracy.

:hash: SenseCAP A1101 stores the predicted class (target number) and the accuracy (confidence level) as a floating point number.

*target number \[1*~~*10], confidence level \[0*~~*99]*

* 🔢0.83
* Predicted Class ➡ 0
* Accuracy ➡ 0.83
* 🔢1.96
* Predicted Class ➡ 1
* Accuracy ➡ 0.96

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_HTTP_API_2.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=d7e644f7f28c1b24ad4d673e3b27b96a" width="1600" height="829" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_HTTP_API_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_portal_data_collection_1.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=6b58946406d0b4609e2d9251ae5f2481" width="1600" height="828" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_portal_data_collection_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_portal_data_collection_2.png?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=633149da85a5d19df96f39775ab7b72d" width="1600" height="826" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_portal_data_collection_2.png" />
</Frame>

⭐ Include the required modules.

```
from twilio.rest import Client
import requests
import json
from time import sleep
```

⭐ Define the Twilio account settings and the client object.

```
twilio_account_sid = '&lt;_SID_>'
twilio_auth_token = '&lt;_TOKEN_>'
twilio_client = Client(twilio_account_sid, twilio_auth_token)
```

⭐ Define the *API ID* and *Access API keys* parameters to connect to the SenseCAP Portal, explained in Step 8.

```
API_ID = '&lt;_ID_>'
API_key = '&lt;_KEY_>'
```

⭐ Define the required device information of SenseCAP A1101.

```
device_eui = "2CF7F1C04340004A"
measurement_id = "4175"
channel_index = "1"
```

⭐ Define the host of the SenseCAP HTTP API.

```
host = "https://sensecap.seeed.cc/openapi/"
```

⭐ Depending on the [Device Data API](https://sensecap-docs.seeed.cc/device_data.html) parameters, define the URL endpoint to obtain the model detection results that SenseCAP A1101 registered to the SenseCAP Portal via the Helium LongFi Network.

*{host}/view\_latest\_telemetry\_data?device\_eui={}\&measurement\_id={}\&channel\_index={}*

```
get_latest_result = "view_latest_telemetry_data?device_eui={}&measurement_id={}&channel_index={}".format(device_eui, measurement_id, channel_index)
```

⭐ In the *send\_WhatsApp\_message* function:

⭐ Send the given text message with a SenseCAP A1101 image to the verified phone number via Twilio's WhatsApp API to inform the user of the latest model detection results via WhatsApp.

```
def send_WhatsApp_message(_from, _to, _message):
    # Send the given message via WhatsApp to inform the user of the model detection results.
    twilio_message = twilio_client.messages.create(
      from_ = 'whatsapp:'+_from,
      body = _message,
      media_url = 'https://media-cdn.seeedstudio.com/media/catalog/product/cache/bb49d3ec4ee05b6f018e93f896b8a25d/1/0/101990962-a1101-first-new-10.17.jpg',
      to = 'whatsapp:'+_to
    )
    print("\nWhatsApp Message Sent: "+twilio_message.sid)
```

⭐ In the *transfer\_latest\_result* function:

⭐ Make an HTTP GET request to the SenseCAP HTTP API by utilizing the HTTP authentication credentials (*API ID* and *Access API keys*) provided by the SenseCAP Portal as username and password.

⭐ Decode the received JSON object to obtain the latest model detection results registered by SenseCAP A1101, including the entry date and time.

⭐ Parse the retrieved detection results to get the predicted class and the precision score (accuracy).

⭐ Create a WhatsApp text message from the converted information.

⭐ Transmit the generated text message with the SenseCAP A1101 image to the verified phone number over WhatsApp.

```
def transfer_latest_result():
    # Obtain the latest model detection result via the SenseCAP HTTP API and notify the user of the received information through WhatsApp.
    url = host + get_latest_result
    # Make an HTTP GET request to the SenseCAP Portal by utilizing the provided HTTP authentication credentials (username and password).
    res = requests.get(url, auth = (API_ID, API_key))
    # Decode the received JSON object.
    res = json.loads(res.text)
    detection_digit = res["data"][0]["points"][0]["measurement_value"]
    date = res["data"][0]["points"][0]["time"]
    # Convert the obtained result digits to the detected class and the precision score.
    detected_class = "Nothing!"
    precision = 0
    if(detection_digit > 0 and detection_digit &lt; 1):
        detected_class = "Enriched"
        precision = detection_digit
    if(detection_digit > 1 and detection_digit &lt; 2):
        detected_class = "Toxic"
        precision = detection_digit-1
    if(detection_digit > 2):
        detected_class = "Unsafe"
        precision = detection_digit-2
    # Create a WhatsApp message from the retrieved information.
    message = "📌 Latest Model Detection Result\n\n🕒 {}\n🌱 Class: {}\n💯 Precision: {}".format(date, detected_class, round(precision, 2))
    print(message)
    # Transmit the generated message to the user via WhatsApp.
    send_WhatsApp_message('+_____________', '+_____________', message)
```

⭐ Via WhatsApp, notify the user of the latest model detection results every 10 minutes.

```
while True:
    # Notify the user of the latest model detection result every 10 minutes.
    transfer_latest_result()
    sleep(60*10)
```

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/code_whatsapp_1.png?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=cd2499c139b2eb1226065d2c727ea9ef" width="1600" height="854" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/code_whatsapp_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/code_whatsapp_2.png?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=393ceca84d87264a467655cc7f091172" width="1600" height="858" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/code_whatsapp_2.png" />
</Frame>

## Step 10: Running the model on SenseCAP A1101 and informing the user of the results via WhatsApp

My Edge Impulse object detection (FOMO) model scans a captured image and predicts possibilities of trained labels to recognize a target object on the given picture. The prediction result (score) represents the model's *"confidence"* that the detected object corresponds to each of the three different labels (classes) \[0 - 2], as shown in Step 6:

* 0 — Enriched
* 1 — Toxic
* 2 — Unsafe

After setting up the Edge Impulse object detection (FOMO) model on SenseCAP A1101 and executing the *A1101\_whatsapp\_interface.py* file on LattePanda 3 Delta:

🌱🪴📲 As explained in the previous steps, SenseCAP A1101 runs an inference with the Edge Impulse object detection model.

🌱🪴📲 Then, every 5 minutes, it transfers the model detection results as data packets to the SenseCAP Portal via the Helium LongFi Network.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/run_1.jpg?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=12ee20745c535706dc0be940903658ed" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/run_1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/WVwKJXsKPZyg_Prf/.assets/images/sensecap-a1101-lorawan-soil-quality/run_2.jpg?fit=max&auto=format&n=WVwKJXsKPZyg_Prf&q=85&s=e213e01cbf4157cc239a1676a1c88ddd" width="1333" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/run_2.jpg" />
</Frame>

🌱🪴📲 Every 10 minutes, the device executes the Python application to obtain the latest registered model detection results from the SenseCAP Portal by making an HTTP GET request to the SenseCAP HTTP API.

🌱🪴📲 After getting and parsing the latest model detection results, the device utilizes Twilio's WhatsApp API to send the obtained detection results to the verified phone number over WhatsApp in order to inform the user of the excessive chemical fertilizer use in relation to organic fertilizers.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/whatsapp_2.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=da366d20ef416a0febdd678a58cfb90d" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/whatsapp_2.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/whatsapp_3.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=3bd7cad57566d952189f02037686e379" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/whatsapp_3.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/whatsapp_4.jpg?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=6c1f42bcbdc61b4e98afe2cf697932b2" width="480" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/whatsapp_4.jpg" />
</Frame>

🌱🪴📲 Also, LattePanda 3 Delta prints notifications and the generated WhatsApp text messages on the shell for debugging.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/_QXsxrTLWLMFrMa7/.assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_whatsapp_send_1.png?fit=max&auto=format&n=_QXsxrTLWLMFrMa7&q=85&s=44ccfd22ba296c7f8b81860faaa8264f" width="1600" height="869" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/sensecap_whatsapp_send_1.png" />
</Frame>

As far as my experiments go, the device detects fertilizer contamination classes accurately, transfers the model detection results to the SenseCAP Portal via the Helium network, and notifies the user of the latest detection results over WhatsApp faultlessly :)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/gif_run.gif?s=c31299bddb3a13c5814c366338d260e1" width="1000" height="493" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/gif_run.gif" />
</Frame>

## Videos and Conclusion

[Data Collection | AI-driven LoRaWAN Fertilizer Pollution Detector w/ WhatsApp](https://youtu.be/jqJkfIb0Ow0)

[Experimenting with the model | AI-driven LoRaWAN Fertilizer Pollution Detector w/ WhatsApp](https://youtu.be/9Z4xEuKCFfU)

## Further Discussions

By applying object detection models trained on numerous fertilizer-exerted soil images in detecting the excessive use of chemical fertilizers in relation to organic fertilizers, we can achieve to:

🌱🪴📲 prevent chemical fertilizers from contaminating the groundwater and the environment,

🌱🪴📲 avoid chemical fertilizers from dispersing throughout water bodies and increasing macronutrients in the environment,

🌱🪴📲 mitigate the risk of severe health issues due to nitrite-contaminated water, such as DNA damage, lipid peroxidation, and oxidative stress,

🌱🪴📲 protect wildlife from the execrable effects of excessive chemical fertilizer use.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Vc7goVAtEpQpB2fo/.assets/images/sensecap-a1101-lorawan-soil-quality/finished_2.jpg?fit=max&auto=format&n=Vc7goVAtEpQpB2fo&q=85&s=73a3ff0f2c9b6e86b8af57ae6d082b20" width="750" height="1000" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/finished_2.jpg" />
</Frame>

## References

\[^1] Devendra Singh, Shobit Thapa, Neelam Geat, Moti Lal Mehriya, Mahendra Vikram Singh Rajawat, *Chapter 12 - Biofertilizers: Mechanisms and application*, Biofertilizers Volume 1: Advances in Bio-Inoculants, Woodhead Publishing, 2021, Pages 151-166, *[https://doi.org/10.1016/B978-0-12-821667-5.00024-5](https://doi.org/10.1016/B978-0-12-821667-5.00024-5)*

\[^2] Lifespan, *Nitrates May Be Environmental Trigger For Alzheimer’s, Diabetes And Parkinson's Disease*, ScienceDaily, 6 July 2009, *[www.sciencedaily.com/releases/2009/07/090705215239.htm](http://www.sciencedaily.com/releases/2009/07/090705215239.htm)*

\[^3] Ayoub, A.T., *Fertilizers and the environment*, Nutrient Cycling in Agroecosystems 55, 117–121, 1999, *[https://doi.org/10.1023/A:1009808118692](https://doi.org/10.1023/A:1009808118692)*

## Schematics

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Z-eQceB7ehSwo9rf/.assets/images/sensecap-a1101-lorawan-soil-quality/SenseCAP_A1101.jpg?fit=max&auto=format&n=Z-eQceB7ehSwo9rf&q=85&s=5066c7456be6e29dedefa9ade016be8f" width="1600" height="897" data-path=".assets/images/sensecap-a1101-lorawan-soil-quality/SenseCAP_A1101.jpg" />
</Frame>


Built with [Mintlify](https://mintlify.com).