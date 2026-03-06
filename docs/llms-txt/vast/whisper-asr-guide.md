# Source: https://docs.vast.ai/whisper-asr-guide.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Whisper ASR Guide

<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
__html: JSON.stringify({
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Use Whisper ASR on Vast.ai",
  "description": "A step-by-step guide to using Whisper automatic speech recognition web service on Vast.ai for audio transcription and language detection.",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Select Whisper Template",
      "text": "Go to the templates tab and search for 'Whisper' or click the provided link to the Whisper ASR Webservice template. After selecting the template by pressing the triangle button, the next step is to choose a GPU."
    },
    {
      "@type": "HowToStep",
      "name": "Select a GPU Offering and Rent",
      "text": "Select a GPU from the search results that meets your requirements. The template provides access to both Jupyter and SSH, plus the Instance Portal web interface via the Open button. Click Rent to launch your instance."
    },
    {
      "@type": "HowToStep",
      "name": "Install TLS Certificate and Access Instance",
      "text": "HTTP and token-based auth are enabled by default. To avoid certificate errors, install the TLS certificate by following the instructions for secure HTTPS connections to your instance via its IP. Use the open button to open the instance. Default username: vastai, password: OPEN_BUTTON_TOKEN environment variable value (or run 'echo $OPEN_BUTTON_TOKEN' in terminal)."
    },
    {
      "@type": "HowToStep",
      "name": "Access SwaggerUI",
      "text": "After accessing the Instance Portal, click the triangle button to expand services, wait for the page to load (can take 5-10 minutes), then click into the link aligning with SwaggerUI. You should see the Swagger documentation interface."
    },
    {
      "@type": "HowToStep",
      "name": "Use Whisper Endpoints",
      "text": "Two POST endpoints are exposed: /detect-language (automatically detect spoken language in audio file) and /asr (transcription and translation of audio files). Both endpoints are documented using OpenAPI standard and can be tested in web browser. Select an endpoint, click 'try it out', upload an audio clip, and press execute. Check response body for results. Note: If getting internal 500 error, the file selected might be too large."
    }
  ]
})
}}
/>

**Whisper** is a general-purpose speech recognition model trained on a large dataset of diverse audio. Go through the [Readme](https://cloud.vast.ai/template/readme/0c0c7d65cd4ebb2b340fbce39879703b) first before using.&#x20;

**Connecting to the Instance**

1. Go to the templates tab and search for “*Whisper*” or click the provided link to the template [here](https://cloud.vast.ai/?ref_id=62897\&creator_id=62897\&name=Whisper%20ASR%20Webservice) .&#x20;
2. After you select the template by pressing the triangle button the next step is to choose a gpu.

<img src="https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text.png?fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=66af3dd1c3607f2eef10502462f94540" alt="" data-og-width="1166" width="1166" data-og-height="1088" height="1088" data-path="images/use-cases-audio-to-text.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text.png?w=280&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=512e742a5d7f977794db3982a7e90c24 280w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text.png?w=560&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=967119acddc90f71fa6d6f71d2058833 560w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text.png?w=840&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=59abde76eae5b0f8a9c1ab576aeb627d 840w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text.png?w=1100&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=41b7209857f468b942bd4d06ecfc7951 1100w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text.png?w=1650&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=81e5bc088cadf1cdc62b07a9e37ba7f2 1650w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text.png?w=2500&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=de2b52f5e19aca1f20a4011414ca4976 2500w" />

3\. **Select a GPU Offering&#x20;**

<img src="https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-2.png?fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=1b73a9a02194da22890e2442d5816a18" alt="" data-og-width="1265" width="1265" data-og-height="670" height="670" data-path="images/use-cases-audio-to-text-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-2.png?w=280&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=780c44c7fb01a43cbaccc429b8d3ae61 280w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-2.png?w=560&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=5e339b1de83e0656fd964781b4199f4c 560w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-2.png?w=840&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=57099eb7d2f00f45ec02cbc52534f4b3 840w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-2.png?w=1100&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=6a01844cb74a4d057ef6bc41ae960f43 1100w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-2.png?w=1650&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=48e1d4fde1b8002eda8ddb09510828d6 1650w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-2.png?w=2500&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=c9093dd77ef8fe676f2dbe040536802e 2500w" />

The template you selected will give your instance access to both Jupyter and SSH. Additionally the Open button will connect you to the instance portal web interface.&#x20;

4\. HTTP and token-based auth are both enabled by default. To avoid certificate errors in your browser, please follow the instructions for installing the TLS certificate [here](/documentation/instances/jupyter#1SmCz) to allow secure HTTPS connections to your instance via its IP.&#x20;

<img src="https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-3.png?fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=fced8cc2a8ed092f724e2d4f4c229a77" alt="" data-og-width="896" width="896" data-og-height="216" height="216" data-path="images/use-cases-audio-to-text-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-3.png?w=280&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=30edab899d9a154e51c23be9dec620dc 280w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-3.png?w=560&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=f409ae4c6858e14cecf6bd340710a696 560w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-3.png?w=840&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=556f8977797f0ea95588f7f8602f270b 840w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-3.png?w=1100&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=27f781cad8fb1847c3dbc9212afa1724 1100w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-3.png?w=1650&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=1204c339d50b05e2dcc2a246b261ad6c 1650w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-3.png?w=2500&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=3d0dde02c064242ac1c061b4983e8660 2500w" />

5\. Use the open button to open up the instance, if you are not using the open button the default username will be: vastai , and the password will be the value of the environment variable:*&#x20;OPEN\_BUTTON\_TOKEN*. You can also find the token value by accessing the terminal and executing this command: *echo \$OPEN\_BUTTON\_TOKEN*

<img src="https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-4.png?fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=c22ace26047bee59dc113d7eec023619" alt="" data-og-width="1280" width="1280" data-og-height="489" height="489" data-path="images/use-cases-audio-to-text-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-4.png?w=280&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=c8bcdc747a18ee48c5b5051942dd43b5 280w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-4.png?w=560&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=a7d4b7eef15d2fb0e9a3d74d5b2a4817 560w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-4.png?w=840&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=25888c36e15dba231b159eac2362d4e3 840w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-4.png?w=1100&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=811e77b2a6d00f667fcf51c32499f636 1100w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-4.png?w=1650&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=1e8fb901f203541d424479c5a5047de5 1650w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-4.png?w=2500&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=a1ae7b242fca211589b7e1a66e9620c0 2500w" />

6\. After accessing the SwaggerUi by clicking the triangle button first then waiting for the page to load, then clicking into the link aligning with SwaggerUI you should see the page below. (note: usually loads fast but can take 5-10 minutes)&#x20;

<img src="https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-5.png?fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=4582d62ecc00b116421db56a8c9a2a35" alt="" data-og-width="1154" width="1154" data-og-height="601" height="601" data-path="images/use-cases-audio-to-text-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-5.png?w=280&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=fcdb58beb0d30aee8b86edc43376d96c 280w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-5.png?w=560&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=5453f339a637b848c1d11ea397d03d69 560w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-5.png?w=840&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=741cdfd31be34b5d6ee600e37ab8c28e 840w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-5.png?w=1100&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=c002c7fcbad11880b422741aed167e5b 1100w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-5.png?w=1650&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=06d550e69c33d2c7f2950ebeb4bb4f21 1650w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-5.png?w=2500&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=b1ac6d0f3a669a2c0313f2ffdcba6fc1 2500w" />

**Usage**

Two POST endpoints are exposed in this template:

**/detect-language**

Use this endpoint to automatically detect the spoken language in a given audio file.

<img src="https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-6.png?fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=18950fe4f6e962ce51085815d1ed1526" alt="" data-og-width="1109" width="1109" data-og-height="942" height="942" data-path="images/use-cases-audio-to-text-6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-6.png?w=280&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=040d71ce4101d47aeb3350c450d8cf42 280w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-6.png?w=560&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=b05305002ed7a562a258dd1be69f0a04 560w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-6.png?w=840&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=f66b84a4cd8026432d70151cff692962 840w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-6.png?w=1100&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=a04795a1596c67e75ceb27e1239fe3ae 1100w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-6.png?w=1650&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=d3ba68f63379b7e5285dd775c6124b28 1650w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-6.png?w=2500&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=3d923ab4905226baa8cd8b6418e94733 2500w" />

**/asr**

Use this endpoint for both transcription and translation of audio files.

*Both of these endpoints are documented using the OpenAPI standard and can be tested in a web browser.&#x20;*

<img src="https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-7.png?fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=6cd4c43fbe5e4b36ae9f5060e1943bfb" alt="" data-og-width="1111" width="1111" data-og-height="1048" height="1048" data-path="images/use-cases-audio-to-text-7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-7.png?w=280&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=9ecff89e12a97ea462b247d95b5d352f 280w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-7.png?w=560&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=218facf0a61ea3678be636f618919fdf 560w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-7.png?w=840&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=c8ec55f1c6cefec572276e34d928efc3 840w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-7.png?w=1100&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=c1434ac7b96cc7dc5b402d229cdaa386 1100w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-7.png?w=1650&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=f47c010775502fdc2c6f6fce45bdabf2 1650w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-7.png?w=2500&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=dfda3c8ac530cdd2a98e3168c40b9b91 2500w" />

7\. *Select the detect language endpoint*

8\. *Then click try it out.&#x20;*

<img src="https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-8.png?fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=425d3820c122aa88e3fb047b815c1e23" alt="" data-og-width="1099" width="1099" data-og-height="105" height="105" data-path="images/use-cases-audio-to-text-8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-8.png?w=280&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=c1b493090a39bde212cc020ffb756b13 280w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-8.png?w=560&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=c8e914c3ad9e979e159f3b7015aa6bcb 560w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-8.png?w=840&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=4f5b93c3d624e09fe504ba49198f0241 840w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-8.png?w=1100&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=f7f738d6ff1c387bd7e8dc2d0f05d71d 1100w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-8.png?w=1650&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=fb81b99245985df5b8a5bf70501534e4 1650w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-8.png?w=2500&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=d6fb02a8f6c339ebd3600ad0af32ad07 2500w" />

9.*&#x20;From here upload an audio clip*&#x20;

10\. *Then press the execute button.&#x20;*

<img src="https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-9.png?fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=31135a8d4b05ea585c0680295ad7bdcd" alt="" data-og-width="1109" width="1109" data-og-height="385" height="385" data-path="images/use-cases-audio-to-text-9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-9.png?w=280&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=d178a0fa4e8124ec9bc28a5d3de56226 280w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-9.png?w=560&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=fa8b8b69123e4b67b9bb070ecef3c791 560w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-9.png?w=840&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=f55872a3ca6aa64d3005b9c05e7581b1 840w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-9.png?w=1100&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=b12cb36eb8211c355b56da5d817c94db 1100w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-9.png?w=1650&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=edcc1ed7ae2a8538e53eb51a1b37ecbc 1650w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-9.png?w=2500&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=b886b1a0a798948ab17cca1aa295b14c 2500w" />

11.*&#x20;If you look in the response body (see below) you can see it was able to detect the language was English.*&#x20;

*Note: If you are getting an internal 500 error its most likely the file you selected to upload is to large.&#x20;*

<img src="https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-10.png?fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=b4229287b94dc286939c28b54dac7b18" alt="" data-og-width="800" width="800" data-og-height="601" height="601" data-path="images/use-cases-audio-to-text-10.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-10.png?w=280&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=f1ac03d77a38cb9fb7847997ec63e946 280w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-10.png?w=560&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=da9ec9fd783f02eeb8c9f5a8344a5b42 560w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-10.png?w=840&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=080df835b1e0efaa0c47f8583922c489 840w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-10.png?w=1100&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=7cde6f5bb2f2bf846775d53f0c7d7048 1100w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-10.png?w=1650&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=d78a1227f7257c8819a4dbd4b7c460f4 1650w, https://mintcdn.com/vastai-80aa3a82/rfbLJXS6cduyf_mj/images/use-cases-audio-to-text-10.png?w=2500&fit=max&auto=format&n=rfbLJXS6cduyf_mj&q=85&s=f4fc44f6ff6de8b9434fea28b0c3d184 2500w" />

*For more information and specifics on things such as but not limited to Configuration, Additional Functionality, Instance Logs, Cloudflared, Api request, ssh tunnels and port reference mapping, and Caddy you can visit the*[ Readme linked here to learn more. ](https://cloud.vast.ai/template/readme/0c0c7d65cd4ebb2b340fbce39879703b)

**Links**

* [GitHub Repository](https://github.com/ahmetoner/whisper-asr-webservice/)
* [Docker Image](https://hub.docker.com/r/onerahmet/openai-whisper-asr-webservice)
