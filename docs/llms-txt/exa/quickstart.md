# Source: https://exa.ai/docs/reference/quickstart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get started with Exa

> Make your first request to one of Exa's API endpoints

<Tabs>
  <Tab title="Python">
    <ol className="steps-list">
      <li>
        <div className="step-number">1</div>

        <div className="step-line" />

        <div className="step-title">Set up your API key</div>

        <div className="step-content">
          <p>Get your API key from the <a href="https://dashboard.exa.ai/login?redirect=/">Exa Dashboard</a> and set it as an environment variable.</p>
          <p>Create a file called `.env` in the root of your project and add the following line:</p>

          ```bash  theme={null}
          EXA_API_KEY=your api key without quotes
          ```
        </div>
      </li>

      <li>
        <div className="step-number">2</div>

        <div className="step-line" />

        <div className="step-title">Install the SDK</div>

        <div className="step-content">
          <p>Install the Python SDKs with pip. If you want to store your API key in a `.env` file, make sure to install the dotenv library.</p>

          ```bash  theme={null}
          pip install exa-py
          pip install openai
          pip install python-dotenv
          ```
        </div>
      </li>

      <li>
        <div className="step-number">3</div>

        <div className="step-line" />

        <div className="step-title">Create your code</div>

        <div className="step-content">
          <p>Once you've installed the SDKs, create a file called `exa.py` and add the code below.</p>

          <Tabs>
            <Tab title="Search and crawl">
              <p>Get a list of results and their full text content.</p>

              ```python python theme={null}
              from exa_py import Exa
              from dotenv import load_dotenv

              import os

              # Use .env to store your API key or paste it directly into the code
              load_dotenv()
              exa = Exa(os.getenv('EXA_API_KEY'))

              result = exa.search(
                "An article about the state of AGI",
                type="auto",
                contents={
                  "text": True
                }
              )

              print(result)
              ```
            </Tab>

            <Tab title="Answer">
              <p>Get an answer to a question, grounded by citations from exa.</p>

              ```python python theme={null}
              from exa_py import Exa
              from dotenv import load_dotenv

              import os

              # Use .env to store your API key or paste it directly into the code
              load_dotenv()
              exa = Exa(os.getenv('EXA_API_KEY'))

              result = exa.stream_answer(
                "What are the latest findings on gut microbiome's influence on mental health?",
                text=True,
              )

              for chunk in result:
                print(chunk, end='', flush=True)
              ```
            </Tab>

            <Tab title="Chat Completions">
              <p>Get a chat completion from exa.</p>

              ```python python theme={null}
              from openai import OpenAI
              from dotenv import load_dotenv

              import os

              # Use .env to store your API key or paste it directly into the code
              load_dotenv()

              client = OpenAI(
                base_url="https://api.exa.ai",
                api_key=os.getenv('EXA_API_KEY'),
              )

              completion = client.chat.completions.create(
                model="exa",
                messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "What are the latest developments in quantum computing?"}
              ],

                extra_body={
                  "text": True
                }
              )
              print(completion.choices[0].message.content)
              ```
            </Tab>

            <Tab title="Find similar links and get full text">
              <p>Find similar links to a given URL and get the full text for each link.</p>

              ```python python theme={null}
              from exa_py import Exa
              from dotenv import load_dotenv

              import os

              load_dotenv()

              exa = Exa(os.getenv('EXA_API_KEY'))

              # get similar links to this post about AGI
              result = exa.find_similar(
                "https://amistrongeryet.substack.com/p/are-we-on-the-brink-of-agi",
                exclude_domains = ["amistrongeryet.substack.com"],
                num_results = 3
              )
              urls = [link_data.url for link_data in result.results]

              # get full text for each url
              web_pages = exa.get_contents(
                urls,
                text=True
              )

              for web_page in web_pages.results:
                print(f"URL: {web_page.url}")
                print(f"Text snippet: {web_page.text[:500]} ...")
                print("-"*100)
              ```
            </Tab>
          </Tabs>
        </div>
      </li>
    </ol>
  </Tab>

  <Tab title="JavaScript">
    <ol className="steps-list">
      <li>
        <div className="step-number">1</div>

        <div className="step-line" />

        <div className="step-title">Set up your API key</div>

        <div className="step-content">
          <p>Get your API key from the <a href="https://dashboard.exa.ai/login?redirect=/">Exa Dashboard</a> and set it as an environment variable.</p>
          <p>Create a file called `.env` in the root of your project and add the following line:</p>

          ```bash  theme={null}
          EXA_API_KEY=your api key without quotes
          ```
        </div>
      </li>

      <li>
        <div className="step-number">2</div>

        <div className="step-line" />

        <div className="step-title">Install the SDK</div>

        <div className="step-content">
          <p>Install the JavaScript SDK with npm. If you want to store your API key in a `.env` file, make sure to install the dotenv library.</p>

          ```bash  theme={null}
          npm install exa-js
          npm install openai
          npm install dotenv
          ```
        </div>
      </li>

      <li>
        <div className="step-number">3</div>

        <div className="step-line" />

        <div className="step-title">Create your code</div>

        <div className="step-content">
          <p>Once you've installed the SDK, create a file called `exa.ts` and add the code below.</p>

          <Tabs>
            <Tab title="Search and crawl">
              <p>Get a list of results and their full text content.</p>

              ```javascript javascript theme={null}
              import dotenv from 'dotenv';
              import Exa from 'exa-js';

              dotenv.config();

              const exa = new Exa(process.env.EXA_API_KEY);

              const result = await exa.search(
                "An article about the state of AGI",
                {
                  type: "auto",
                  contents: {
                    text: true
                  }
                }
              );

              // print the first result
              console.log(result.results[0]);
              ```
            </Tab>

            <Tab title="Answer">
              <p>Get an answer to a question, grounded by citations from exa.</p>

              ```javascript javascript theme={null}
              import dotenv from 'dotenv';
              import Exa from 'exa-js';

              dotenv.config();

              const exa = new Exa(process.env.EXA_API_KEY);
              for await (const chunk of exa.streamAnswer(
                "What is the population of New York City?",
                {
                  text: true
                }
              )) {
                if (chunk.content) {
                  process.stdout.write(chunk.content);
                }
                if (chunk.citations) {
                  console.log("\nCitations:", chunk.citations);
                }
              }
              ```
            </Tab>

            <Tab title="Chat Completions">
              <p>Get a chat completion from exa.</p>

              ```javascript javascript theme={null}
              import OpenAI from "openai";
              import dotenv from 'dotenv';
              import Exa from 'exa-js';

              dotenv.config();

              const openai = new OpenAI({
                baseURL: "https://api.exa.ai",
                apiKey: process.env.EXA_API_KEY,
              });

              async function main() {
                const completion = await openai.chat.completions.create({
                  model: "exa",
                  messages: [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "What are the latest developments in quantum computing?"}
                  ],
                  store: true,
                  stream: true,
                  extra_body: {
                    text: true // include full text from sources
                  }
                });

                for await (const chunk of completion) {
                  console.log(chunk.choices[0].delta.content);
                  }
              }

              main();
              ```
            </Tab>

            <Tab title="Find similar links and get full text">
              <p>Find similar links to a given URL and get the full text for each link.</p>

              ```javascript javascript theme={null}
              import Exa from 'exa-js';
              import dotenv from 'dotenv';

              dotenv.config();

              const exa = new Exa(process.env.EXA_API_KEY);

              // Find similar links to this post about AGI
              const result = await exa.findSimilar(
                "https://amistrongeryet.substack.com/p/are-we-on-the-brink-of-agi",
                {
                  excludeDomains: ["amistrongeryet.substack.com"],
                  numResults: 3
                }
              );

              const urls = result.results.map(linkData => linkData.url);

              // Get full text for each URL
              const webPages = await exa.getContents(urls, { text: true });

              webPages.results.forEach(webPage => {
                console.log(`URL: ${webPage.url}`);
                console.log(`Text snippet: ${webPage.text.slice(0, 500)} ...`);
                console.log("-".repeat(100));
              });
              ```
            </Tab>
          </Tabs>
        </div>
      </li>
    </ol>
  </Tab>

  <Tab title="cURL">
    <ol className="steps-list">
      <li>
        <div className="step-number">1</div>

        <div className="step-line" />

        <div className="step-title">Set up your API key</div>

        <div className="step-content">
          <p>Get your API key from the <a href="https://dashboard.exa.ai/login?redirect=/">Exa Dashboard</a> and set it as an environment variable:</p>

          ```bash  theme={null}
          export EXA_API_KEY='your-api-key-here'
          ```
        </div>
      </li>

      <li>
        <div className="step-number">2</div>

        <div className="step-line" />

        <div className="step-title">Make your first API call</div>

        <div className="step-content">
          <p>Pass one of the following commands to your terminal to make an API request.</p>

          <Tabs>
            <Tab title="Search and crawl">
              <p>Get a list of results and their full text content.</p>

              ```bash bash theme={null}
              curl --request POST \
                  --url https://api.exa.ai/search \
                  --header 'accept: application/json' \
                  --header 'content-type: application/json' \
                  --header "x-api-key: ${EXA_API_KEY}" \
                  --data '
              {
                  "query": "An article about the state of AGI",
                  "type": "auto",
                  "contents": {
                    "text": true
                  }
              }'
              ```
            </Tab>

            <Tab title="Answer">
              <p>Get an answer to a question, grounded by citations from exa.</p>

              ```bash bash theme={null}
              curl --request POST \
                --url https://api.exa.ai/answer \
                --header 'accept: application/json' \
                --header 'content-type: application/json' \
                --header "x-api-key: ${EXA_API_KEY}" \
                --data "{
                  \"query\": \"What are the latest findings on gut microbiome's influence on mental health?\",
                  \"text\": true
                }"
              ```
            </Tab>

            <Tab title="Chat Completions">
              <p>Get a chat completion from exa.</p>

              ```bash bash theme={null}
              curl https://api.exa.ai/chat/completions \
                -H "Content-Type: application/json" \
                -H "x-api-key: ${EXA_API_KEY}" \
                -d '{
                  "model": "exa", 
                  "messages": [
                    {
                      "role": "system",
                      "content": "You are a helpful assistant."
                    },
                    {
                      "role": "user",
                      "content": "What are the latest developments in quantum computing?"
                    }
                  ],
                  "extra_body": {
                    "text": true
                  }
                }'
              ```
            </Tab>
          </Tabs>
        </div>
      </li>
    </ol>
  </Tab>
</Tabs>
