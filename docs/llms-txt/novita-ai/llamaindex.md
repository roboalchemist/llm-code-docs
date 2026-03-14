# Source: https://novita.ai/docs/guides/llamaindex.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LlamaIndex

> Effortlessly integrate Novita AI with LlamaIndex to build intelligent, data-powered applications.

Designed for optimal indexing and retrieval, LlamaIndex excels in delivering high efficiency for applications requiring precise and fast data access. By combining [Novita AI](https://novita.ai/) with LlamaIndex, you will unlock key benefits such as superior data retrieval accuracy, unmatched scalability, and cost-effective performance.

This guide will walk you through how to use LlamaIndex with Novita AI based on the OpenAl APl, offering smarter, scalable, and highly efficient AI solutions that drive innovation and deliver exceptional results for developers.

## **How to Integrate Novita AI API with LlamaIndex**

Step 1: Visit [Model Library](https://novita.ai/llm-api) on Novita AI and select a model of interest.

<Frame>
    <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step1VisitModelLibraryonNovitaAIandselectamodelofinterest.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=d3db29afa82f298487c3284f24397510" alt="images/Step1VisitModelLibraryonNovitaAIandselectamodelofinterest.png" width="3841" height="1905" data-path="images/Step1VisitModelLibraryonNovitaAIandselectamodelofinterest.png" />
</Frame>

Step 2: Navigate to the demo page of the chosen model and click the `Code` button on the right.

<Frame>
    <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step2NavigatetothedemopageofthechosenmodelandclicktheCodebuttonontheright.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=e5ca58627abad4dd217b7ac3abd598e7" alt="images/Step2NavigatetothedemopageofthechosenmodelandclicktheCodebuttonontheright.png" width="3841" height="1905" data-path="images/Step2NavigatetothedemopageofthechosenmodelandclicktheCodebuttonontheright.png" />
</Frame>

Step 3: Copy the model’s name and make a note of it.

<Frame>
    <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step3Copythemodel%E2%80%99snameandmakeanoteofit.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=816f535a6a61bc39356d6e050b462511" alt="images/Step3Copythemodel’snameandmakeanoteofit.png" width="3841" height="1905" data-path="images/Step3Copythemodel’snameandmakeanoteofit.png" />
</Frame>

Step 4: [Log in ](https://novita.ai/user/login)to the Novita platform.

<Frame>
    <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step4LogintotheNovitaplatform.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=d274e15bfd1b4c639512ec19a7ddf6ed" alt="images/Step4LogintotheNovitaplatform.png" width="3841" height="1905" data-path="images/Step4LogintotheNovitaplatform.png" />
</Frame>

Step 5: After logging in, go to the platform’s [settings page](https://novita.ai/settings).

<Frame>
    <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step5Afterloggingin,gototheplatform%E2%80%99ssettingspage.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=8792b12498ad8c59383777d528f340e9" alt="images/Step5Afterloggingin,gototheplatform’ssettingspage.png" width="3841" height="1905" data-path="images/Step5Afterloggingin,gototheplatform’ssettingspage.png" />
</Frame>

Step 6: Create a new [API key](https://novita.ai/settings/key-management) and copy it for service authentication.

<Frame>
    <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step6CreateanewAPIkeyandcopyitforserviceauthentication.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=07b03a5c86e922736118a779e34041ff" alt="images/Step6CreateanewAPIkeyandcopyitforserviceauthentication.png" width="2057" height="617" data-path="images/Step6CreateanewAPIkeyandcopyitforserviceauthentication.png" />
</Frame>

Step 7: Install `llama_index` and related Python libraries by running:

<Frame>
    <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step7Installllama_indexandrelatedPythonlibrariesbyrunning.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=fd802a1818ff357dfcede0fe966e61a9" alt="images/Step7Installllama_indexandrelatedPythonlibrariesbyrunning.png" width="2224" height="682" data-path="images/Step7Installllama_indexandrelatedPythonlibrariesbyrunning.png" />
</Frame>

Step 8: Write Python code and set the model name and API key as parameters in the NovitaAI class.

<Frame>
    <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step8WritePythoncodeandsetthemodelnameandAPIkeyasparametersintheNovitaAIclass.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=dc8c9b21bd91d18469faab2d238fa9ce" alt="images/Step8WritePythoncodeandsetthemodelnameandAPIkeyasparametersintheNovitaAIclass.png" width="1291" height="437" data-path="images/Step8WritePythoncodeandsetthemodelnameandAPIkeyasparametersintheNovitaAIclass.png" />
</Frame>

Step 9: Run the code to get the output.

<Frame>
    <img src="https://mintcdn.com/novitaai/bnRhXPrVKQGiPndx/images/Step9Runthecodetogettheoutput.png?fit=max&auto=format&n=bnRhXPrVKQGiPndx&q=85&s=4f3bf4015516d4acfc6c079b8a7f8c65" alt="images/Step9Runthecodetogettheoutput.png" width="2089" height="41" data-path="images/Step9Runthecodetogettheoutput.png" />
</Frame>

For more examples, refer to the documentation: [llama\_index/llama-index-integrations/llms/llama-index-llms-novita at main · run-llama/llama\_index](https://github.com/run-llama/llama_index/tree/main/llama-index-integrations/llms/llama-index-llms-novita).


Built with [Mintlify](https://mintlify.com).