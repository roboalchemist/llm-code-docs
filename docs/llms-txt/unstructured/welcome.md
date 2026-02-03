# Source: https://docs.unstructured.io/welcome.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Welcome to Unstructured!

<Tip>To start using Unstructured right away, skip ahead to the <Icon icon="desktop" /> [UI quickstart](#unstructured-ui-quickstart) or <Icon icon="rectangle-terminal" /> [API quickstart](#unstructured-api-quickstart) now!</Tip>

## What is Unstructured?

<Frame caption="Unstructured turns your organization's unstructured documents into structured, AI-ready data at scale with high performance, accuracy, and relevance">
  <img src="https://mintcdn.com/unstructured-53/HIy1tdX-YgPq1b1H/img/welcome/conceptual-flow.png?fit=max&auto=format&n=HIy1tdX-YgPq1b1H&q=85&s=eda1bc5280bfd7a7ee9ae07d6058e9ed" alt="Unstructured conceptual data flow" data-og-width="768" width="768" data-og-height="182" height="182" data-path="img/welcome/conceptual-flow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/HIy1tdX-YgPq1b1H/img/welcome/conceptual-flow.png?w=280&fit=max&auto=format&n=HIy1tdX-YgPq1b1H&q=85&s=5434ec0887912432d07058a4494cc87e 280w, https://mintcdn.com/unstructured-53/HIy1tdX-YgPq1b1H/img/welcome/conceptual-flow.png?w=560&fit=max&auto=format&n=HIy1tdX-YgPq1b1H&q=85&s=3407069e35a8872f022fe2c3f110343e 560w, https://mintcdn.com/unstructured-53/HIy1tdX-YgPq1b1H/img/welcome/conceptual-flow.png?w=840&fit=max&auto=format&n=HIy1tdX-YgPq1b1H&q=85&s=8378838d3e06ca529ce742cc5d7db004 840w, https://mintcdn.com/unstructured-53/HIy1tdX-YgPq1b1H/img/welcome/conceptual-flow.png?w=1100&fit=max&auto=format&n=HIy1tdX-YgPq1b1H&q=85&s=90e34f0293f1a8301098c153788f2ae5 1100w, https://mintcdn.com/unstructured-53/HIy1tdX-YgPq1b1H/img/welcome/conceptual-flow.png?w=1650&fit=max&auto=format&n=HIy1tdX-YgPq1b1H&q=85&s=6d7f5b9585a2b09eeca0407d803c6a37 1650w, https://mintcdn.com/unstructured-53/HIy1tdX-YgPq1b1H/img/welcome/conceptual-flow.png?w=2500&fit=max&auto=format&n=HIy1tdX-YgPq1b1H&q=85&s=00fcaf9db899ad53b964c1e51d15823b 2500w" />
</Frame>

Unstructured provides a platform and tools to ingest and process your unstructured documents for:

* [Enhancing retrieval-augmented generation (RAG)](https://unstructured.io/blog/rag-whitepaper): RAG boosts AI accuracy and relevance by working with the data that's most important to you, providing results that are more current, focused, and meaningful to your queries and tasks.
* [Fueling agentic AI](https://unstructured.io/problems-we-solve#powering-agentic-ai): Agentic AI acts like virtual teammates that can plan, decide, and take action on their own to get things done on your behalf, freeing you up for bigger challenges.

We empower your organization to take full advantage of RAG and agentic AI opportunities through:

* [Rapid prototyping](https://unstructured.io/problems-we-solve#rapid-prototyping): Quickly iterating on AI experiences powered by enterprise data.
* [Replacing do-it-yourself data transformation pipelines](https://unstructured.io/problems-we-solve#replacing-diy-pipelines): Building your own data transformation pipelines is time-consuming and error-prone.
* [Unifying data silos](https://unstructured.io/problems-we-solve#unifying-data-silos): Eliminating data barriers and creating shared GenAI data layers.
* [Continuous data delivery](https://unstructured.io/problems-we-solve#continuous-data-delivery): Scheduling jobs, routing documents, and optimizing every task.
* [Business process automation](https://unstructured.io/problems-we-solve#business-process-automation): Report generation, automatic responses, decision-making, content analysis, and more!

This 60-second video describes more about what Unstructured does and its benefits (no sound):

<iframe width="560" height="315" src="https://www.youtube.com/embed/b2AcxJDXOLs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

This 40-second video demonstrates a simple use case that Unstructured helps solve (no sound):

<iframe width="560" height="315" src="https://www.youtube.com/embed/E-tupjji22U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

This 60-second video shows why using Unstructured is preferable to building your own similar solution:

<iframe width="560" height="315" src="https://www.youtube.com/embed/P9HzldV72ho" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

You can use Unstructured through a user interface (UI), an API, or both. Read on to learn more.

<Frame caption="An example of the Unstructured user interface, showing a local file being partitioned">
  <img src="https://mintcdn.com/unstructured-53/HIy1tdX-YgPq1b1H/img/welcome/user-interface.png?fit=max&auto=format&n=HIy1tdX-YgPq1b1H&q=85&s=ce845e77a23b31d82aa2d3eea405e07e" alt="Unstructured user interface example" data-og-width="847" width="847" data-og-height="454" height="454" data-path="img/welcome/user-interface.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/HIy1tdX-YgPq1b1H/img/welcome/user-interface.png?w=280&fit=max&auto=format&n=HIy1tdX-YgPq1b1H&q=85&s=29a32b0aebc8f086cd7174f54664e26f 280w, https://mintcdn.com/unstructured-53/HIy1tdX-YgPq1b1H/img/welcome/user-interface.png?w=560&fit=max&auto=format&n=HIy1tdX-YgPq1b1H&q=85&s=14c13dd9265fca636177c76a76999d70 560w, https://mintcdn.com/unstructured-53/HIy1tdX-YgPq1b1H/img/welcome/user-interface.png?w=840&fit=max&auto=format&n=HIy1tdX-YgPq1b1H&q=85&s=2be1c444b6eea963c18db2d16760ab4f 840w, https://mintcdn.com/unstructured-53/HIy1tdX-YgPq1b1H/img/welcome/user-interface.png?w=1100&fit=max&auto=format&n=HIy1tdX-YgPq1b1H&q=85&s=86907d2abfaf06254d2d3d225f24ac53 1100w, https://mintcdn.com/unstructured-53/HIy1tdX-YgPq1b1H/img/welcome/user-interface.png?w=1650&fit=max&auto=format&n=HIy1tdX-YgPq1b1H&q=85&s=6c85afdb0f0c44ff8c90672c5d5a77e0 1650w, https://mintcdn.com/unstructured-53/HIy1tdX-YgPq1b1H/img/welcome/user-interface.png?w=2500&fit=max&auto=format&n=HIy1tdX-YgPq1b1H&q=85&s=ad9a607a5deda7a3d7bc071372fe08cb 2500w" />
</Frame>

<Frame caption="An example of the Unstructured API, showing the code to process a local file on demand">
  <img src="https://mintcdn.com/unstructured-53/HIy1tdX-YgPq1b1H/img/welcome/api.png?fit=max&auto=format&n=HIy1tdX-YgPq1b1H&q=85&s=33a4944ecb1c94b25e5a70f0c4723089" alt="Unstructured API example" data-og-width="547" width="547" data-og-height="635" height="635" data-path="img/welcome/api.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/HIy1tdX-YgPq1b1H/img/welcome/api.png?w=280&fit=max&auto=format&n=HIy1tdX-YgPq1b1H&q=85&s=04eca8e1293c949e2d1d70e837b1f423 280w, https://mintcdn.com/unstructured-53/HIy1tdX-YgPq1b1H/img/welcome/api.png?w=560&fit=max&auto=format&n=HIy1tdX-YgPq1b1H&q=85&s=b48a286058c01d0081b99bacdaee2d25 560w, https://mintcdn.com/unstructured-53/HIy1tdX-YgPq1b1H/img/welcome/api.png?w=840&fit=max&auto=format&n=HIy1tdX-YgPq1b1H&q=85&s=d11584bd2f75b3b446e16670421ac542 840w, https://mintcdn.com/unstructured-53/HIy1tdX-YgPq1b1H/img/welcome/api.png?w=1100&fit=max&auto=format&n=HIy1tdX-YgPq1b1H&q=85&s=dc2161e7726ac4b5ed81f39e6d37175b 1100w, https://mintcdn.com/unstructured-53/HIy1tdX-YgPq1b1H/img/welcome/api.png?w=1650&fit=max&auto=format&n=HIy1tdX-YgPq1b1H&q=85&s=990c1ff16459ef167c774021b16850e8 1650w, https://mintcdn.com/unstructured-53/HIy1tdX-YgPq1b1H/img/welcome/api.png?w=2500&fit=max&auto=format&n=HIy1tdX-YgPq1b1H&q=85&s=efe183400a78d8879edb5d09cbd94d47 2500w" />
</Frame>

***

## <Icon icon="desktop" />    Unstructured UI quickstart

This quickstart shows how, in just a few minutes, you can use the Unstructured user interface (UI) to quickly and easily see Unstructured's
best-in-class transformation results for a single file that is stored on your local computer.

<Tip>
  This quickstart focuses on a single, local file for ease-of-use demonstration purposes.

  To use Unstructured later to do
  large-scale batch processing of multiple files and semi-structured data that are stored in remote locations,
  [skip over](/ui/quickstart#remote-quickstart) to the remote quickstart after you finish this one.
</Tip>

If you do not already have an Unstructured account, [sign up for free](https://unstructured.io/?modal=try-for-free).
After you sign up, you are automatically signed in to your new Unstructured **Let's Go** account, at [https://platform.unstructured.io](https://platform.unstructured.io).

<Note>
  If you already have an Unstructured **Pay-As-You-Go** or **Business SaaS** account, you are already signed up for Unstructured.
  Sign in to your existing Unstructured **Pay-As-You-Go** or **Business SaaS** account, at [https://platform.unstructured.io](https://platform.unstructured.io).

  If you already have an Unstructured **dedicated instance** or **in-VPC** deployment, your sign-in link will be unique to your deployment.
  If you're not sure what your unique sign-in link is, see your Unstructured account administrator, or email Unstructured Support at
  [support@unstructured.io](mailto:support@unstructured.io).
</Note>

Do the following:

1. After you are signed in, the **Start** page appears.

2. In the **Welcome** area, do one of the following:

   * Click one of the sample files, such as **realestate.pdf**, to have Unstructured parse and transform that sample file.
   * Click **Browse files**, or drag and drop a file onto **Drop file to test**, to have Unstructured parse and transform your own file.

     If you choose to use your own file, the file must be 10 MB or less in size. Also, the file must be one of the following supported file types:

     | File extension |
     | -------------- |
     | `.bmp`         |
     | `.csv`         |
     | `.doc`         |
     | `.docx`        |
     | `.eml`         |
     | `.epub`        |
     | `.heic`        |
     | `.html`        |
     | `.jpeg`        |
     | `.jpg`         |
     | `.md`          |
     | `.msg`         |
     | `.odt`         |
     | `.org`         |
     | `.p7s`         |
     | `.pdf`         |
     | `.png`         |
     | `.ppt`         |
     | `.pptx`        |
     | `.rst`         |
     | `.rtf`         |
     | `.tif`         |
     | `.tiff`        |
     | `.tsv`         |
     | `.txt`         |
     | `.xls`         |
     | `.xlsx`        |
     | `.xml`         |

   <img src="https://mintcdn.com/unstructured-53/rMc-icsfF1CGWovL/img/ui/single-file/welcome.png?fit=max&auto=format&n=rMc-icsfF1CGWovL&q=85&s=4afd67de1ca6df270150830c59dfecb8" alt="Welcome interface on the Start page" data-og-width="1346" width="1346" data-og-height="591" height="591" data-path="img/ui/single-file/welcome.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/rMc-icsfF1CGWovL/img/ui/single-file/welcome.png?w=280&fit=max&auto=format&n=rMc-icsfF1CGWovL&q=85&s=818915212bfeef72c2ad4a4cab6791b9 280w, https://mintcdn.com/unstructured-53/rMc-icsfF1CGWovL/img/ui/single-file/welcome.png?w=560&fit=max&auto=format&n=rMc-icsfF1CGWovL&q=85&s=90e90e00480392191b2e6fb1f60988d4 560w, https://mintcdn.com/unstructured-53/rMc-icsfF1CGWovL/img/ui/single-file/welcome.png?w=840&fit=max&auto=format&n=rMc-icsfF1CGWovL&q=85&s=6834886e1bcc3a152a96b09bf32a7a23 840w, https://mintcdn.com/unstructured-53/rMc-icsfF1CGWovL/img/ui/single-file/welcome.png?w=1100&fit=max&auto=format&n=rMc-icsfF1CGWovL&q=85&s=c31509604224a6f506926c46304b5a30 1100w, https://mintcdn.com/unstructured-53/rMc-icsfF1CGWovL/img/ui/single-file/welcome.png?w=1650&fit=max&auto=format&n=rMc-icsfF1CGWovL&q=85&s=99830aaf06da67c702e50df0916728de 1650w, https://mintcdn.com/unstructured-53/rMc-icsfF1CGWovL/img/ui/single-file/welcome.png?w=2500&fit=max&auto=format&n=rMc-icsfF1CGWovL&q=85&s=6b0bc597eeeec032355169fcdb0e2e21 2500w" />

3. After Unstructured has finished parsing and transforming the file (a process known as
   [partitioning](/ui/partitioning)), you will see the file's contents in the
   **Preview** pane in the center and Unstructured's results in the **Result** pane on the right.

   <img src="https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/results.png?fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=57319fe777c4db089f8eb4fcd18006b9" alt="Unstructured's parse and transform results" data-og-width="3454" width="3454" data-og-height="1912" height="1912" data-path="img/ui/single-file/results.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/results.png?w=280&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=75626bd309bed12d5775f7861c5d267f 280w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/results.png?w=560&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=37be4068bfdb16674d06340d3e5c3072 560w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/results.png?w=840&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=97b2a4f5659532eb82dca29d1683bf3f 840w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/results.png?w=1100&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=c6a51560737fa64966bf77ccc467eede 1100w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/results.png?w=1650&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=e202516fad57db627141f7d8349ffd08 1650w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/results.png?w=2500&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=7f083c7412c7da412ba130a35e1bb5dc 2500w" />

4. The **Result** pane shows a formatted view of Unstructured's results by default. This formatted view is designed for human
   readability. To see the underlying JSON view of the results, which is designed for RAG and agentic AI,
   click **JSON** at the top of the **Result** pane.
   [Learn about what's in the JSON view](/ui/document-elements).

   <img src="https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/json-view.png?fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=0947a7c013ae1e4127f9bb1cb4dc050c" alt="Switching to the JSON view of the results" data-og-width="784" width="784" data-og-height="191" height="191" data-path="img/ui/single-file/json-view.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/json-view.png?w=280&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=c886e31ae32d65c395311975a48e3735 280w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/json-view.png?w=560&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=2c5dc92ff56b32da8484177b55a00fad 560w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/json-view.png?w=840&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=65d097403265d3ee3f9fc83031cba1b7 840w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/json-view.png?w=1100&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=01e946242f70c299ad8c3ae5b9ea03f4 1100w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/json-view.png?w=1650&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=05aeb2509c8979a8575a3aad5aa84b7e 1650w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/json-view.png?w=2500&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=7ea6e1c05e51d09311248430512ef19f 2500w" />

5. Unstructured's initial results are based on its **High Res** [partitioning strategy](/ui/partitioning), which
   begins processing the file's contents and converting these contents into a series of Unstructured
   [document elements and metadata](/ui/document-elements). This partitioning strategy provides good results overall, depending on the complexity of the file's contents.
   This partitioning strategy also generates a bounding box for each detected object in the file. A *bounding box* is
   an imaginary rectangular box drawn around the object to show its location and extent within the file.

   After the High Res partitioning results are shown, Unstructured begins improving these initial results by
   using vision language models (VLMs) to apply a series of generative refinements known as *enrichments*. These
   enrichments include:

   * An [image description](ui/enriching/image-descriptions) enrichment, which uses a VLM to provide a text-based summary of the contents of each detected image.
   * A [generative OCR](/ui/enriching/generative-ocr) enrichment, which uses a VLM to improve the accuracy of each block of initially-processed text.
   * A [table to HTML](/ui/enriching/table-to-html) enrichment, which uses a VLM to provide an HTML-structured representation of each detected table.

   While these enrichments are being applied, a banner appears at the top of the **Result** pane.

   <img src="https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/generative-refinement.png?fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=aaa55fe34d402659f4bb83d7c93e003e" alt="Updating the initial results with enrichments" data-og-width="779" width="779" data-og-height="138" height="138" data-path="img/ui/single-file/generative-refinement.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/generative-refinement.png?w=280&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=f462804d182e7d8152edae863dea917f 280w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/generative-refinement.png?w=560&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=924b8bd75faf8b79004287d0980967ab 560w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/generative-refinement.png?w=840&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=81de21e1de9ebbfa2e1f93dd272b0c7e 840w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/generative-refinement.png?w=1100&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=dfd3dcf0a6fed54a5afa4ce185ace462 1100w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/generative-refinement.png?w=1650&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=bac362b5cd2ac8f2cba28f3fcc54e35d 1650w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/generative-refinement.png?w=2500&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=1302f2aadbf8059f1a47cb71bf6a301b 2500w" />

   To see these enrichments applied to the initial results, click **Update results** in the banner as soon as this button appears,
   which might take up to a minute or more.

   <img src="https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/apply-generative-refinement.png?fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=c202060fb848a8d6b2f9e66d56f237e3" alt="Seeing the initial results updated with the enrichments" data-og-width="780" width="780" data-og-height="136" height="136" data-path="img/ui/single-file/apply-generative-refinement.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/apply-generative-refinement.png?w=280&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=17e2c361e58150cc835104992fcc1f94 280w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/apply-generative-refinement.png?w=560&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=807074d22044d67c874ed64905ff0bc2 560w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/apply-generative-refinement.png?w=840&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=b51f77a1feb7c274c413b341864acb39 840w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/apply-generative-refinement.png?w=1100&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=85191b797d7497912da2c307082fdd4a 1100w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/apply-generative-refinement.png?w=1650&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=8a41a763664ec3b6838e2613770c6f7c 1650w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/apply-generative-refinement.png?w=2500&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=1f9015b9a4aa1bb4837736cc05f62aac 2500w" />

   <Warning>
     Each page that Unstructured processes by using this approach is counted as two pages for usage and billing purposes.

     This is because Unstructured processes each page once with its **High Res** partitioning strategy and then reprocesses each
     page with a VLM to improve the quality, accuracy, and relevance of the initial partitioning results.
     The final results of these two processing passes for each page count as two pages for usage and billing purposes.
     This two-pass process happens regardless of whether you click **Update results** in the banner.

     This two-page usage and billing behavior is a known issue and will be addressed in a future release.
   </Warning>

6. To synchronize the scrolling of the **Preview** pane's selected contents with the **Result** pane's **Formatted** results,
   rest your mouse pointer anywhere inside the contents of the **Preview** pane until a bounding box appears.
   Then click the bounding box. Unstructured automatically scrolls the **Result** pane's **Formatted**
   results to match the selected bounding box. (You cannot synchronize the scrolling of the **JSON** results.)

   <img src="https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/bounding-box.png?fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=c5a484c1385880cbdc2bbde4a3a834e5" alt="Selecting a bounding box" data-og-width="2890" width="2890" data-og-height="688" height="688" data-path="img/ui/single-file/bounding-box.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/bounding-box.png?w=280&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=0c8d1f5e270559ad98a81810db22b3ca 280w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/bounding-box.png?w=560&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=28f092a737f0e95124d471b3f2e974f0 560w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/bounding-box.png?w=840&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=9de350d69271ca8fee42016b271e1bd3 840w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/bounding-box.png?w=1100&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=709239c6e08a0a577244447b8303045c 1100w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/bounding-box.png?w=1650&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=8f2da6c9a7063343e7a0a55b4b012a0c 1650w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/bounding-box.png?w=2500&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=809f3a54800de57262a6884292a34b50 2500w" />

   To show all of the bounding boxes in the **Preview** pane at once, turn on the **Show all bounding boxes** toggle at the top of the **Preview** pane.
   You can now click any of the bounding boxes without first needing to rest your mouse pointer on them to show them.

   <img src="https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/show-all-bounding-boxes.png?fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=128e06817ba5fa7ad8b2d953926450e4" alt="Showing all bounding boxes" data-og-width="1448" width="1448" data-og-height="856" height="856" data-path="img/ui/single-file/show-all-bounding-boxes.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/show-all-bounding-boxes.png?w=280&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=0e9f20c2eafb8eee57ef40cad0269f68 280w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/show-all-bounding-boxes.png?w=560&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=d54dc49ba20c167edc076b6b13f464f6 560w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/show-all-bounding-boxes.png?w=840&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=3eb61f726e0ae6665310c0d5d0d833fb 840w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/show-all-bounding-boxes.png?w=1100&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=193dbb29ca31d0d99503de31c374fa81 1100w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/show-all-bounding-boxes.png?w=1650&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=94736d75a145fa1a624c8236b8e5194d 1650w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/show-all-bounding-boxes.png?w=2500&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=f022c60a98cb66cda9455236afa7245b 2500w" />

You can also do the following:

* To download the JSON view of the results as a local JSON file, click the download icon to the left of the **Formatted** and **JSON** buttons in the **Result** pane.
  (You cannot download the formatted view of the results.)

  <img src="https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/download.png?fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=456cb0a98ef3a3ef0d86e22462f5a11f" alt="Downloading the results as a local JSON file" data-og-width="784" width="784" data-og-height="191" height="191" data-path="img/ui/single-file/download.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/download.png?w=280&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=fda4c4752406ca36683396c236561186 280w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/download.png?w=560&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=304350da7c151e2aef43bdc9383bc5b8 560w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/download.png?w=840&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=c8103fc50b1c7b72d92b02c59acb72a6 840w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/download.png?w=1100&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=019df03cbd4db8c43becfa30d844c52e 1100w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/download.png?w=1650&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=da42a107483e4400797702b2d34c9af5 1650w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/download.png?w=2500&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=85093ecb522c74769c89d62de23ebf6f 2500w" />

* To have Unstructured partition a different file, click **Add new file** in the **Files** pane on the left, and then browse to and select the target file.

* To view the results for a file that was previously partitioned during this session, click the file's name in the **Recent files** list in the **Files** pane.

* To return to the **Start** page, click the **X** (close) button at the left on the title bar, next to **Transform**.

* To have Unstructured do more—such as
  [chunking](/ui/chunking), [embedding](/ui/embedding),
  applying additional kinds of [enrichments](/ui/enriching/overview), and
  processing larger files and semi-structured data in batches at scale—click
  **Edit in Workflow Editor** at the right on the title bar, and then [skip over to the walkthrough](/ui/walkthrough-2).

  <img src="https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/workflow-editor.png?fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=26be748d279c116a252e5b6c6f67a4d9" alt="Switching to the workflow editor" data-og-width="732" width="732" data-og-height="204" height="204" data-path="img/ui/single-file/workflow-editor.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/workflow-editor.png?w=280&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=642196362851e6712f147852b25f4c2e 280w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/workflow-editor.png?w=560&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=ce9d1f294fcce62e765aa0eb779b7d6b 560w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/workflow-editor.png?w=840&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=630afa312e041fe9108b4b2619b81b61 840w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/workflow-editor.png?w=1100&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=0e0c3660d434f1cd0b4ec3105fc90220 1100w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/workflow-editor.png?w=1650&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=95c8df27fd2134ec386f5a7f89f4a308 1650w, https://mintcdn.com/unstructured-53/7V13mJi2iZBZVTP5/img/ui/single-file/workflow-editor.png?w=2500&fit=max&auto=format&n=7V13mJi2iZBZVTP5&q=85&s=a258ffbc479e29cdeb6ded440a5e4e33 2500w" />

What's next?

* <Icon icon="plus" />  [Learn how to add chunking, embeddings, and additional enrichments to your local file results](/ui/walkthrough-2).
* <Icon icon="database" />  [Learn how to do large-scale batch processing of multiple files and semi-structured data that are stored in remote locations instead](/ui/quickstart#remote-quickstart).
* <Icon icon="desktop" />  [Learn more about the Unstructured user interface](/ui/overview).

***

## <Icon icon="rectangle-terminal" />    Unstructured API quickstart

This quickstart shows how you can use the Unstructured API to quickly and easily see Unstructured's
transformation results for files that are stored locally.

<Note>
  This quickstart is designed to work *only by processing local files*.

  To process files (and data) in remote file and blob storage, databases, and vector stores, you must use
  workflow operations in the Unstructured API other than the ones that are used in this quickstart. To learn how, see for example the notebook
  [Dropbox-To-Pinecone Connector API Quickstart for Unstructured](https://colab.research.google.com/github/Unstructured-IO/notebooks/blob/main/notebooks/Dropbox_To_Pinecone_Connector_Quickstart.ipynb).
</Note>

1. If you do not already have an Unstructured account, [sign up for free](https://unstructured.io/?modal=try-for-free).
   After you sign up, you are automatically signed in to your Unstructured **Let's Go** account, at [https://platform.unstructured.io](https://platform.unstructured.io).

   <Note>
     If you already have an Unstructured **Pay-As-You-Go** or **Business SaaS** account, you are already signed up for Unstructured.
     Sign in to your existing Unstructured **Pay-As-You-Go** or **Business SaaS** account, at [https://platform.unstructured.io](https://platform.unstructured.io).

     If you already have an Unstructured **dedicated instance** or **in-VPC** deployment, your sign-in link will be unique to your deployment.
     If you're not sure what your unique sign-in link is, see your Unstructured account administrator, or email Unstructured Support at
     [support@unstructured.io](mailto:support@unstructured.io).
   </Note>

2. Get your Unstructured API key:

   a. After you sign in to your Unstructured account, click **API Keys** on the sidebar.<br />

   <Note>
     For a **Business** account, before you click **API Keys**, make sure you have selected the organizational workspace you want to create an API key
     for. Each API key works with one and only one organizational workspace. [Learn more](/ui/account/workspaces#create-an-api-key-for-a-workspace).
   </Note>

   b. Click **Generate API Key**.<br />
   c. Follow the on-screen instructions to finish generating the key.<br />
   d. Click the **Copy** icon next to your new key to add the key to your system's clipboard. If you lose this key, simply return and click the **Copy** icon again.<br />

3. Now that you have your Unstructured API key, choose one of the following options to continue:

   * [Use a remote notebook](https://colab.research.google.com/github/Unstructured-IO/notebooks/blob/main/notebooks/Unstructured_API_On_Demand_Jobs_Quickstart.ipynb) - This option uses a remotely hosted Google Colab notebook. There are no additional setup steps required.
   * [Use your local machine](/api-reference/quickstart) - This option requires you to install the Unstructured Python SDK on your local machine.

<Icon icon="person-chalkboard" />  [Learn more](/api-reference/overview).

***

## <Icon icon="money-check-dollar" />    Pricing

Unstructured offers different account types with different pricing plans:

* <Icon icon="person" />  **Let's Go** and **Pay-As-You-Go** - A single user, with a single workspace, hosted alongside other accounts on Unstructured's cloud infrastructure.
* <Icon icon="building" />  **Business** - Multiple users and workspaces, with three options:

  * <Icon icon="people-group" />  **Business SaaS** - Hosted alongside other accounts on Unstructured's cloud infrastructure.
  * <Icon icon="shield-halved" />  **Dedicated instance** - Hosted within a virtual private cloud (VPC) running inside Unstructured's cloud infrastructure. Dedicated instances are isolated from all other accounts, for additional security and control.
  * <Icon icon="shield" />  **In-VPC** - Hosted within your own VPC on your own cloud infrastructure.

  **Business** accounts also allow for robust customization of Unstructured's features for your unique needs.

For more details, see the [Unstructured Pricing](https://unstructured.io/pricing) page.

To upgrade your account from **Let's Go** or **Pay-As-You-Go** to **Business**,
email Unstructured Sales at [sales@unstructured.io](mailto:sales@unstructured.io).

Some of these plans have billing details that are determined on a per-page basis.

Unstructured calculates a page as follows:

* For these file types, a page is a page, slide, or image: `.pdf`, `.pptx`, and `.tiff`.
* For `.docx` files that have page metadata, Unstructured calculates the number of pages based on that metadata.
* For all other file types, Unstructured calculates the number of pages as the file's size divided by 100 KB.
* For non-file data, Unstructured calculates a page as 100 KB of incoming data to be processed.

***

## <Icon icon="question" />    Questions? Need help?

* For general questions about Unstructured products and pricing, email Unstructured Sales at [sales@unstructured.io](mailto:sales@unstructured.io).
* For technical support for Unstructured accounts, email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).
* For technical support for the Unstructured open source library, use our [Slack community](https://short.unstructured.io/pzw05l7).
