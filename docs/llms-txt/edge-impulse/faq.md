# Source: https://docs.edgeimpulse.com/knowledge/faq.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# FAQ

## Data

<AccordionGroup>
  <Accordion title="Does Edge impulse integrate with cloud storage services?">
    Yes. The enterprise version of Edge Impulse can integrate directly with your cloud storage provider to access and transform data.
  </Accordion>

  <Accordion title="How is the labeling of the data performed?">
    Using the Edge Impulse Studio data acquisition tools (like the [serial daemon](/tools/clis/edge-impulse-cli/serial-daemon) or [data forwarder](/tools/clis/edge-impulse-cli/data-forwarder)), you can collect data samples manually with a pre-defined label.

    If you have a dataset that was collected outside of Edge Impulse, you can upload your dataset using the [Edge Impulse CLI](/tools/clis/edge-impulse-cli/uploader), [Ingestion API](/apis/ingestion), [web uploader](/tools/clis/edge-impulse-cli/uploader), [enterprise data storage bucket tools](/studio/organizations/data) or [enterprise upload portals](/studio/organizations/upload-portals). You can then use the Edge Impulse Studio to split up your data into labeled chunks, crop your data samples, and more to create high quality machine learning datasets.
  </Accordion>
</AccordionGroup>

## Processing

<AccordionGroup>
  <Accordion title="What signal processing is available in Edge Impulse?">
    A big part of Edge Impulse are the processing blocks, as they clean up the data, and extract important features from your data before passing it to a machine learning model.

    The source code for these processing blocks can be found on GitHub: [edgeimpulse/processing-blocks](https://github.com/edgeimpulse/processing-blocks) (and you can build [your own processing blocks](/studio/organizations/custom-blocks/custom-processing-blocks) as well).
  </Accordion>

  <Accordion title="How does the feature explorer visualize data that has more that 3 dimensions?">
    Edge Impulse uses [UMAP](https://umap-learn.readthedocs.io/en/latest/) (a dimensionality reduction algorithm) to project high dimensionality input data into a 2 or 3 dimensional space. This even works for extremely high dimensionality data such as images.
  </Accordion>
</AccordionGroup>

## Learning

<AccordionGroup>
  <Accordion title="What frameworks does Edge Impulse use to train the machine learning models?">
    We use a wide variety of tools, depending on the machine learning model. For neural networks we typically use TensorFlow and Keras, for object detection models we use TensorFlow with Google's Object Detection API, and for 'classic' non-neural network machine learning algorithms we mainly use sklearn. For neural networks you can see (and modify) the Keras code by clicking `⋮`, and selecting **Switch to expert mode**.
  </Accordion>

  <Accordion title="Can I use a model that has been trained outside of Edge Impulse?">
    Yes you can! Check out our documentation on [Bring your own model (BYOM)](/studio/projects/dashboard/byom) to see how to import your model into your Edge Impulse project, and using the [Edge Impulse Python SDK](/tools/libraries/sdks/studio/python)!
  </Accordion>
</AccordionGroup>

## Deployment

<AccordionGroup>
  <Accordion title="What are the minimum hardware requirements to run the Edge Impulse inferencing library on my embedded device?">
    The minimum hardware requirements for the embedded device depends on the use case. Anything from a Cortex-M0+ for vibration analysis to Cortex-M4F for audio, Cortex-M7 for image classification to Cortex-A for object detection in video should work.

    View our [inference performance metrics](/knowledge/metrics/inference-performance) for more details.
  </Accordion>

  <Accordion title="What is the typical power consumption of the Edge Impulse machine learning processes on my device?">
    Simple answer: To get an indication of time per inference we show performance metrics in every DSP and ML block in Studio. Multiply this by the active power consumption of your MCU to get an indication of power cost per inference.

    More complicated answer: It depends. Normal techniques to conserve power still apply to ML, so try to do as little as possible (do you need to classify every second, or can you do it once a minute?), be smart about when to run inference (can there be an external trigger like a motion sensor before you run inference on a camera?), and collect data in a lower power mode (don't run at full speed when sampling low-resolution data, and see if your sensor can use an interrupt to wake your MCU - rather than polling).

    Also see [Analyse Power Consumption in Embedded ML Solutions](https://edgeimpulse.com/blog/analyze-power-consumption-in-embedded-ml-solutions).
  </Accordion>

  <Accordion title="What engine does Edge Impulse use to compile the impulse?">
    It depends on the hardware.

    For general-purpose MCUs we typically use EON Compiler with TFLite Micro and additional kernels (including hardware optimization, e.g. via CMSIS-NN, ESP-NN).

    On Linux, if you run the impulse on CPU, we use LiteRT (previously Tensorflow Lite).

    For accelerators we use a wide variety of other runtimes, e.g. hardcoded network in silicon for Syntiant, custom SNN-based inference engine for Brainchip Akida, DRP-AI for Renesas RZV2L, etc...
  </Accordion>

  <Accordion title="Is there a downside to enabling the EON Compiler?">
    The [EON Compiler](https://edgeimpulse.com/blog/introducing-eon) compiles your neural networks to C++ source code, which then gets compiled into your application. This is great if you need the lowest RAM and ROM possible (EON typically uses 30-50% less memory than LiteRT (previously Tensorflow Lite) but you also lose some flexibility to update your neural networks in the field - as it is now part of your firmware).

    By disabling EON we place the full neural network (architecture and weights) into ROM, and load it on demand. This increases memory usage, but you could just update this section of the ROM (or place the neural network in external flash, or on an SD card) to make it easier to update.
  </Accordion>

  <Accordion title="What is the .eim model format for Edge Impulse for Linux?">
    See [.eim models?](/tools/libraries/sdks/inference/linux#eim-models) on the Edge Impulse for Linux pages.
  </Accordion>

  <Accordion title="Can I use an unsupported development board or a custom PCB (with a different microcontroller or microprocessor) with Edge Impulse?">
    Yes! A "supported board" simply means that there is an official or community-supported firmware that has been developed specifically for that board that helps you collect data and run impulses. Edge Impulse is designed to be extensible to computers, smartphones, and a nearly endless array of microcontroller build systems.

    You can collect data from you custom board and upload it to Edge Impulse in a variety of ways. For example:

    * Transmitting data to the [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder)
    * Using the [Edge Impulse for Linux](/tools/libraries/sdks/inference/linux) SDK
    * By [uploading files directly](/studio/projects/data-acquisition/uploader) (e.g. CBOR, JSON, CSV, WAV, JPG, PNG)

    Your trained model can be deployed as part a [C++ library](/hardware/deployments/run-cpp-overview). It requires some effort, but most build systems will work with our C++ library, as long as that build system has a C++ compiler and there is enough flash/RAM on your device to run the library (which includes the DSP block and model).
  </Accordion>
</AccordionGroup>

## Other

<AccordionGroup>
  <Accordion title="How can I share my Edge Impulse project?">
    To collaboration on your projects, go to your [project dashboard](/studio/projects/dashboard), find the *Collaborators* section, and click the '+' icon.

    <Frame caption="Managing collaborators on a project">
      <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/317f9dc-screenshot_2021-06-09_at_105802.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=a112f36cd680232d45b655c0eb24090d" width="474" height="314" data-path=".assets/images/317f9dc-screenshot_2021-06-09_at_105802.png" />
    </Frame>

    You can also create a public version of your Edge Impulse project. This makes your project available to the whole world - including your data, your impulse design, your models, and all intermediate information - and can easily be cloned by anyone in the community. To do so, go to **Dashboard**, and click **Make this project public**.

    <Frame caption="Public project versioning on the Edge Impulse dashboard">
      <img src="https://mintcdn.com/edgeimpulse/LSbqkaU8tx8Cie9-/.assets/images/ea4b4b2-screenshot_2021-06-09_at_105832.png?fit=max&auto=format&n=LSbqkaU8tx8Cie9-&q=85&s=990a791db277f1bdec138b22b41ffab1" width="470" height="208" data-path=".assets/images/ea4b4b2-screenshot_2021-06-09_at_105832.png" />
    </Frame>
  </Accordion>

  <Accordion title="How can I cite Edge Impulse in scientific publications?">
    If you use Edge Impulse in a scientific publication, we would appreciate citations to the following paper:

    [Edge Impulse: An MLOps Platform for Tiny Machine Learning](https://arxiv.org/abs/2212.03332)

    ```
    @misc{hymel2023edgeimpulsemlopsplatform,
          title={Edge Impulse: An MLOps Platform for Tiny Machine Learning},
          author={Shawn Hymel and Colby Banbury and Daniel Situnayake and Alex Elium and Carl Ward and Mat Kelcey and Mathijs Baaijens and Mateusz Majchrzycki and Jenny Plunkett and David Tischler and Alessandro Grande and Louis Moreau and Dmitry Maslov and Artie Beavis and Jan Jongboom and Vijay Janapa Reddi},
          year={2023},
          eprint={2212.03332},
          archivePrefix={arXiv},
          primaryClass={cs.DC},
          url={https://arxiv.org/abs/2212.03332},
    }
    ```
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).