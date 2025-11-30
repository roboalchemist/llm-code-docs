# Source: https://docs.tavily.com/documentation/partnerships/IBM.md

# IBM

> Tavily and IBM have partnered to deliver AI-enriched spreadsheets, combining real-time web search with advanced foundation models to transform business data workflows.

<p align="center">
  <img src="https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/logo_circle.png?fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=d818735b0cfebd7617f00a2ba9fa97ff" alt="Tavily Logo" width="80" style={{ display: 'inline', verticalAlign: 'middle' }} data-og-width="1024" data-og-height="1024" data-path="images/logo_circle.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/logo_circle.png?w=280&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=c7a94053fc5322f121c025e92b8d6f0e 280w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/logo_circle.png?w=560&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=cb43157c27d7233123bdd7a065da5110 560w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/logo_circle.png?w=840&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=5298fcdddf61b3992483038709a40319 840w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/logo_circle.png?w=1100&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=d2166a894523380ad65db68eb37ddf30 1100w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/logo_circle.png?w=1650&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=1ae230ebf66fd7df8f3d97a3c73b1dee 1650w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/logo_circle.png?w=2500&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=f4d2586f664e6fb1eff1035dd3973422 2500w" />

  <img src="https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/watsonx_circle.svg?fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=7e36765e09c53fd6fe7497ea6cc03d22" alt="IBM watsonx Logo" width="80" style={{ display: 'inline', verticalAlign: 'middle', marginLeft: 20 }} data-og-width="32" data-og-height="32" data-path="images/watsonx_circle.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/watsonx_circle.svg?w=280&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=da05e0b399bf9a2cf1b2a65c81da5beb 280w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/watsonx_circle.svg?w=560&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=ebb1e8aec28c0d4f50c453fd01211100 560w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/watsonx_circle.svg?w=840&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=0281df6af483e66b7eea33b7709deb17 840w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/watsonx_circle.svg?w=1100&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=ba81d52347b40a387e90200e549039fc 1100w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/watsonx_circle.svg?w=1650&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=a05f02d0ce22d0d1df67648c7e4b221f 1650w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/watsonx_circle.svg?w=2500&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=4608fc23e92572b6f99f3f7c223c799e 2500w" />
</p>

<p align="center">
  Powered by <a href="https://tavily.com">Tavily</a> and <a href="https://www.ibm.com/products/watsonx-ai">IBM® watsonx.ai™</a>
</p>

## Overview

Tavily and IBM have partnered to deliver [AI-enriched spreadsheets](https://github.com/tavily-ai/watsonx-tavily-spreadsheets) that combine Tavily's real-time web search with IBM watsonx.ai's advanced foundation models. This open-source solution enables users to enrich spreadsheet data with live, cited web information and powerful LLM-driven insights.

## What is it?

With this application, you can:

* 📊 Enrich spreadsheet cells with AI-generated content backed by live web data
* 🧠 Entity extraction and data processing with Granite LLMs
* 🔄 Process entire columns in batch for efficient data enhancement
* 📑 Access source citations for all web-sourced information
* 📂 Export your enriched data as CSV files for further use

## How it Works

1. **Fill in spreadsheet columns** with your data
2. **Enrich your spreadsheet**: The app uses Tavily's search and IBM watsonx.ai models to add live, relevant information
3. **Export as CSV** for further use

<div align="center" style={{ margin: '32px 0' }}>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/fv1TnJfTC0E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />
</div>

## Architecture

<img src="https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/spreadsheet.png?fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=9b15deaf4fe13bd422f49b1e7a6c07f7" alt="Architecture Diagram" data-og-width="1029" width="1029" data-og-height="923" height="923" data-path="images/spreadsheet.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/spreadsheet.png?w=280&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=afcc8ba679fb55a499504c41df741349 280w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/spreadsheet.png?w=560&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=6c8ccc1eb2964fed62e6196e9cb2c964 560w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/spreadsheet.png?w=840&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=bcebfc1d4f729100c8bd39fec6f03ab5 840w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/spreadsheet.png?w=1100&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=5d1bd21c50d74e576ef1332eaaa08612 1100w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/spreadsheet.png?w=1650&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=03a68bf9466507381ec972c01ea3f89a 1650w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/spreadsheet.png?w=2500&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=7b2b6d9d10c2c5907b79c20e80d0c6fb 2500w" />

## Setup Instructions

<AccordionGroup>
  <Accordion title="API Keys & Environment Variables">
    <ul>
      <li>Get your <a href="https://app.tavily.com/home">Tavily API key</a> and <a href="https://www.ibm.com/products/watsonx-ai">IBM watsonx.ai API key</a>.</li>
      <li>Create a <code>.env</code> file in the project root.</li>
    </ul>

    ```
    TAVILY_API_KEY=<your API key>
    WATSONX_API_KEY=<your API key>
    WATSONX_PROJECT_ID=<your project id>
    WATSONX_URL=<your data center url>
    FOUNDATION_MODEL_ID=<watsonx.ai model id>
    ```

    <em>Note: <code>FOUNDATION\_MODEL\_ID</code> is optional. Defaults to <code>ibm/granite-3-2-8b-instruct</code> if not set.</em>

    <ul>
      <li>Create <code>.env.development</code> in <code>ui/</code> directory.</li>
    </ul>

    ```
    VITE_API_URL=http://localhost:8000
    VITE_WS_URL=ws://localhost:8000
    ```
  </Accordion>

  <Accordion title="Backend Setup (Python)">
    <ul>
      <li>Create and activate a Python 3.11 virtual environment.</li>
    </ul>

    ```
    python3.11 -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

    <ul>
      <li>Install dependencies.</li>
    </ul>

    ```
    python3.11 -m pip install -r requirements.txt
    ```

    <ul>
      <li>Run the backend server.</li>
    </ul>

    ```
    python app.py
    ```
  </Accordion>

  <Accordion title="Backend Setup (Docker)">
    <ul>
      <li>Build the Docker image.</li>
    </ul>

    ```
    docker build -t spreadsheet .
    ```

    <ul>
      <li>Run the container.</li>
    </ul>

    ```
    docker run -p 8000:8000 --env-file .env spreadsheet
    ```
  </Accordion>

  <Accordion title="Frontend Setup">
    <ul>
      <li>Navigate to the frontend directory.</li>
    </ul>

    ```
    cd ui
    ```

    <ul>
      <li>Install dependencies.</li>
    </ul>

    ```
    npm install
    ```

    <ul>
      <li>Start the development server.</li>
    </ul>

    ```
    npm run dev
    ```

    <ul>
      <li>Open <a href="http://localhost:5174">[http://localhost:5174](http://localhost:5174)</a> in your browser.</li>
    </ul>
  </Accordion>
</AccordionGroup>

See full setup, usage, and contribution details in the [GitHub repository](https://github.com/tavily-ai/watsonx-tavily-spreadsheets).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.tavily.com/llms.txt