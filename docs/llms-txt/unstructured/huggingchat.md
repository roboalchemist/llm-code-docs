# Source: https://docs.unstructured.io/examplecode/codesamples/api/huggingchat.md

# Query processed PDF with HuggingChat

This example uses the [Unstructured Ingest Python library](/open-source/ingestion/python-ingest) or the
[Unstructured JavaScript/TypeScript SDK](/api-reference/partition/sdk-jsts) to send a PDF file to
the [Unstructured Partition Endpoint](/api-reference/partition/overview) for processing. Unstructured processes the PDF and extracts the PDF's content.
This example then sends some of the content to [HuggingChat](https://huggingface.co/chat/), Hugging Face's open-source AI chatbot,
along with some queries about this content.

To run this example, you'll need:

* The [hugchat](https://pypi.org/project/hugchat/) package for Python, or the [huggingface-chat](https://www.npmjs.com/package/huggingface-chat) package for JavaScript/TypeScript.
* Your Unstructured API key and API URL. [Get an API key and API URL](/api-reference/partition/overview).
* Your Hugging Face account's email address and account password. [Get an account](https://huggingface.co/join).
* A PDF file for Unstructured to process. This example uses a sample PDF file containing the text of the United States Constitution,
  available for download from [https://constitutioncenter.org/media/files/constitution.pdf](https://constitutioncenter.org/media/files/constitution.pdf).

These environment variables:

* `UNSTRUCTURED_API_KEY` - Your Unstructured API key value.
* `UNSTRUCTURED_API_URL` - Your Unstructured API URL.

These environment variables:

* `HUGGING_FACE_EMAIL`, representing your Hugging Face account's email address.
* `HUGGING_FACE_PASSWORD`, representing your Hugging Face account's email address.
* `HUGGING_FACE_COOKIE_DIR_PATH`, representing a login cookie cache path, typically `./cookies/` or `./login_cache/`.

This example's code is as follows:

<AccordionGroup>
  <Accordion title="Ingest Python library">
    ```python Python theme={null}
    from unstructured_ingest.pipeline.pipeline import Pipeline
    from unstructured_ingest.interfaces import ProcessorConfig
    from unstructured_ingest.processes.connectors.local import (
        LocalIndexerConfig,
        LocalDownloaderConfig,
        LocalConnectionConfig,
        LocalUploaderConfig
    )
    from unstructured_ingest.processes.partitioner import PartitionerConfig

    import os, json
    from hugchat import hugchat
    from hugchat.login import Login
        
    def generate_json_from_local(
            input_path: str,
            output_dir: str,
            partition_by_api: bool = False,
            api_key: str = None,
            partition_endpoint: str = None,
            split_pdf_page: bool = True,
            split_pdf_allow_failed: bool = True,
            split_pdf_concurrency_level: int = 15
        ):
        Pipeline.from_configs(
            context=ProcessorConfig(),
            indexer_config=LocalIndexerConfig(input_path=input_path),
            downloader_config=LocalDownloaderConfig(),
            source_connection_config=LocalConnectionConfig(),
            partitioner_config=PartitionerConfig(
                partition_by_api=partition_by_api,
                api_key=api_key,
                partition_endpoint=partition_endpoint,
                additional_partition_args={
                    "split_pdf_page": split_pdf_page,
                    "split_pdf_allow_failed": split_pdf_allow_failed,
                    "split_pdf_concurrency_level": split_pdf_concurrency_level
                }
            ),
            uploader_config=LocalUploaderConfig(output_dir=output_dir)
        ).run()

    def extract_matching_texts_from_local(input_json_file_path: str, text_to_match: str) -> str:
        voting_texts = ""

        with open(input_json_file_path, 'r') as file:
            file_elements = json.load(file)

        for element in file_elements:
            if text_to_match in element["text"]:
                voting_texts += " " + element["text"]

        return voting_texts

    def log_in_to_hugging_face(email: str, passwd: str, cookie_dir_path: str) -> hugchat.ChatBot:
        sign = Login(
            email=email,
            passwd=passwd
        )

        cookies = sign.login(cookie_dir_path=cookie_dir_path)

        return hugchat.ChatBot(cookies=cookies.get_dict())

    if __name__ == "__main__":
        generate_json_from_local(
            input_path=os.getenv("LOCAL_FILE_INPUT_DIR"),
            output_dir=os.getenv("LOCAL_FILE_OUTPUT_DIR"),
            partition_by_api=True,
            api_key=os.getenv("UNSTRUCTURED_API_KEY"),
            partition_endpoint=os.getenv("UNSTRUCTURED_API_URL")
        )

        chatbot = log_in_to_hugging_face(
            email=os.getenv("HUGGING_FACE_EMAIL"),
            passwd=os.getenv("HUGGING_FACE_PASSWORD"),
            cookie_dir_path=os.getenv("HUGGING_FACE_COOKIE_DIR_PATH")
        )

        voting_texts = extract_matching_texts_from_local(
            input_json_file_path=f"{os.getenv("LOCAL_FILE_OUTPUT_DIR")}/constitution.json",
            text_to_match="vot"
        )

        print("\n-----\n")
        print("Querying HuggingChat...")
        print("\n-----\n")

        req = f"Given the following information, what is the minimum voting age in the United States? {voting_texts}"
        print(req)
        print("\n-----\n")
        print(chatbot.chat(text=req))

        print("\n-----\n")
        print("Querying HuggingChat again...")
        print("\n-----\n")

        follow_up = "And when were women given the right to vote in the United States?"
        print(follow_up)
        print("\n-----\n")

        print(chatbot.chat(text=follow_up))
    ```
  </Accordion>

  <Accordion title="JavaScript/TypeScript SDK">
    <Warning>
      Unstructured recommends that you use the [Unstructured Ingest Python library](/open-source/ingestion/python-ingest) instead.

      The Ingest Python library provides faster processing of larger individual files, and faster and easier processing of multiple files at a time in batches.
    </Warning>

    ```typescript TypeScript theme={null}
    import { UnstructuredClient } from "unstructured-client";
    import { Strategy } from "unstructured-client/sdk/models/shared/index.js";
    import { PartitionResponse } from "unstructured-client/sdk/models/operations";

    import * as fs from "fs";
    import * as path from 'path';
    import { fileURLToPath } from 'url';
    import { Login, ChatBot} from "huggingface-chat";

    const key = process.env.UNSTRUCTURED_API_KEY || '';
    const url = process.env.UNSTRUCTURED_API_URL || '';
    const username = process.env.HUGGING_FACE_EMAIL || '';
    const userpassword = process.env.HUGGING_FACE_PASSWORD || '';
    const cookieDirPath = process.env.HUGGING_FACE_COOKIE_DIR_PATH || '';

    const inputFilepath = path.dirname(fileURLToPath(import.meta.url)) + 
                          "/local-ingest-pdf-source/constitution.pdf"

    async function getChatBot(email: string, password: string, cachePath: string): Promise<ChatBot> {
        const signin = new Login(email, password)
        const result = await signin.login(cachePath)
        const chat = new ChatBot(result)

        return chat
    }

    async function queryAndResponse(chatbot: ChatBot, query: string) {
        let data = await chatbot.chat(query)

        if (! data) {
            console.log("No data available.");
            return;
        }
        
        let reader = data.stream?.getReader();

        if (! reader) {
            console.log("No stream available.");
            return;
        }

        while (true) {
            const { done, value } = await reader?.read();
            if (done) break;
            process.stdout.write(value);
        }    
    }

    const client = new UnstructuredClient({
        security: { apiKeyAuth: key },
        serverURL: new URL(url).origin
    });

    const data = fs.readFileSync(inputFilepath);

    client.general.partition({
        partitionParameters: {
            files: {
                content: data,
                fileName: inputFilepath
            },
            strategy: Strategy.HiRes,
            splitPdfPage: true,
            splitPdfAllowFailed: true,
            splitPdfConcurrencyLevel: 15
        }
    }).then(async (res: PartitionResponse) => {
        if (res.statusCode == 200) {
            let voting_texts = ""

            if (res)
                for (const element of res) {
                    if (element.text.includes("vot")) {
                        voting_texts += " " + element.text;
                    }
            }

            let chat = await getChatBot(username, userpassword, cachePath)
            
            await chat.initialize()

            const firstQuery = 'Given the following information, what is the minimum voting age in the United States?'
            const secondQuery = 'And when were women given the right to vote in the United States?'

            console.log(`${firstQuery} ${voting_texts}\n\n-----\n`)
            await queryAndResponse(chat, firstQuery)
            console.log(`\n\n-----\n`)
            console.log(`${secondQuery}\n\n-----\n`)
            await queryAndResponse(chat, secondQuery)
        }    
    }).catch((e) => {
        if (e.statusCode) {
            console.log(e.statusCode);
            console.log(e.body);
        } else {
            console.log(e);
        }
    });
    ```
  </Accordion>
</AccordionGroup>
