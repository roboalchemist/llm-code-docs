# Source: https://dev.writer.com/home/models.md

# Choose a model

> Choose the right Palmyra model for your needs. Compare capabilities, context windows, and pricing for X5, Fin, Med, Creative, and Vision models.

Whether you use no-code, Agent Builder, or APIs, you need to choose a model. Here is an overview of the Palmyra models and their capabilities.

## Model comparison

| Feature              | Palmyra X5                         | Palmyra X4                                | Palmyra X 003 Instruct                                         | Palmyra Vision                 | Palmyra Med                            | Palmyra Fin                                     | Palmyra Creative                                |
| -------------------- | ---------------------------------- | ----------------------------------------- | -------------------------------------------------------------- | ------------------------------ | -------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| **Description**      | Our latest and most advanced model | Advanced language model for complex tasks | Highly proficient in generating precise and detailed responses | Designed for processing images | Language model tailored for healthcare | Developed specifically for the financial sector | Purpose-built for creative thinking and writing |
| **API model ID**     | `palmyra-x5`                       | `palmyra-x4`                              | `palmyra-x-003-instruct`                                       | `palmyra-vision`               | `palmyra-med`                          | `palmyra-fin`                                   | `palmyra-creative`                              |
| **Bedrock model ID** | `writer.palmyra-x5-v1:0`           | `writer.palmyra-x4-v1:0`                  | N/A                                                            | N/A                            | N/A                                    | N/A                                             | N/A                                             |
| **Pricing (Input)**  | \$0.60 / 1M tokens                 | \$2.50 / 1M tokens                        | \$7.50 / 1M tokens                                             | \$7.50 / 1M tokens             | \$5.00 / 1M tokens                     | \$5.00 / 1M tokens                              | \$5.00 / 1M tokens                              |
| **Pricing (Output)** | \$6.00 / 1M tokens                 | \$10.00 / 1M tokens                       | \$22.50 / 1M tokens                                            | See note\*                     | \$12.00 / 1M tokens                    | \$12.00 / 1M tokens                             | \$12.00 / 1M tokens                             |
| **Context window**   | 1M tokens                          | 128k tokens                               | 32k tokens                                                     | 8k tokens                      | 32k tokens                             | 128k tokens                                     | 128k tokens                                     |
| **Max output**       | 8,192 tokens                       | 4,096 tokens                              | 4,096 tokens                                                   | 4,096 tokens                   | 4,096 tokens                           | 4,096 tokens                                    | 4,096 tokens                                    |

<Note>
  * Palmyra Vision pricing: \$0.005 per image and \$7.50 per 1M tokens (text output)
  * All models are available in No-code, Agent Builder, and API, except Palmyra Vision, which is not available in Agent Builder. However, you can use [vision capabilities with Palmyra X5](/home/chat-with-images) in Agent Builder.
</Note>

## Model details

<AccordionGroup>
  <Accordion title="Palmyra X5" icon="comment" iconType="regular">
    <Tabs>
      <Tab title="Overview">
        Palmyra X5 is Writer's newest and most advanced model for building and scaling AI agents, featuring a 1 million token context window, adaptive reasoning, and industry-leading speed and cost efficiency.

        **Pricing**:

        * Input: \$0.60 per 1M tokens
        * Output: \$6.00 per 1M tokens

        **Content window**: 1M
      </Tab>

      <Tab title="Use cases and capabilities">
        Palmyra X5's 1M token context window further streamlines enterprise workflows and unlocks complex, multi-step use cases that weren't possible before.

        **Multi-step agentic workflows**

        * **Support documentation**: Classify requests, assess urgency, assign a human review, stage updates in a CMS, and publish after approval.
        * **Fund reporting**: Streamline the analysis and preparation of detailed reports on the performance and status of investment funds, using reporting and research data pulled in from third-party systems
        * **Content lifecycle management**: Flag content that could be outdated, generate suggested revisions, and share them for human review.

        **Large data requirements**:

        * **Customer feedback analysis**: Analyze large volumes of customer feedback to identify common themes, summarize sentiments, and generate actionable insights.
        * **Research and development**: Process and summarize multiple technical reports, research papers, and experimental data, accelerating innovation and product development.
        * **Financial reporting**: Process and summarize annual reports, SEC filings, and market analysis reports together at once to extract financial data, identify trends, and generate executive summaries.
        * **Legal document analysis**: Analyze lengthy legal documents, including contracts, patents, and compliance reports, to identify key clauses, flag potential risks, and ensure regulatory compliance.
        * **Medical records analysis**: Analyze and summarize large files of medical records containing structured and unstructured data, including patient records, clinical trial reports, audit reports, and more.
      </Tab>

      <Tab title="Benchmarking">
        Palmyra X5 demonstrates robust performance across a suite of industry-standard benchmarks, showcasing its capabilities in reasoning, retrieval, and domain-specific tasks.

        * **BBH (Big-Bench Hard)**: Evaluates complex reasoning and compositional logic. Palmyra X5 achieves a competitive score of 70.99%, aligning closely with top-tier models.
        * **GPQA (Graduate-Level Google-Proof Q\&A)**: Assesses the model's ability to answer challenging, graduate-level questions in biology, physics, and chemistry that are resistant to simple lookup strategies. X5's score of 47.20% indicates strong performance in scientific reasoning tasks.
        * **MMLU\_PRO**: Focuses on professional-level knowledge across various domains such as law, medicine, and finance. Palmyra X5 scores 65.02%, demonstrating its suitability for enterprise applications in regulated sectors.
        * **MATH\_HARD**: Tests symbolic reasoning and multi-step problem-solving abilities. X5's score of 71.57% showcases its proficiency in handling complex analytical tasks.
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="Palmyra X4" icon="comment" iconType="regular">
    <Tabs>
      <Tab title="Overview">
        `palmyra-x4` is an advanced language model that excels in processing and understanding complex tasks. It's ideal for workflow automation, coding tasks, and data analysis.

        **Pricing**:

        * Input: \$2.50 per 1M tokens
        * Output: \$10.00 per 1M tokens

        **Content window**: 128k
      </Tab>

      <Tab title="Use cases and capabilities">
        * **Agents & actions**: Palmyra X4 acts as an advanced AI agent, capable of executing tasks beyond simple text generation by interacting with external systems like databases, applications, and other services. This enables it to perform real-time data updates and automate complex workflows.
        * **Retrieval-augmented generation (RAG)**: Equipped with RAG, Palmyra X4 can retrieve and incorporate relevant information from vast data sources, enhancing the model's accuracy and ensuring responses are always grounded in current, context-specific data.
        * **Code generation**: The model supports advanced code generation, enabling it to automate scripting and integrate seamlessly with various programming environments, optimizing workflows for technical teams.
        * **Tool calling**: Palmyra X4 is built to handle precise API interactions, allowing it to execute complex functions directly, making it a versatile tool for enterprise-level integrations and automated actions.
      </Tab>

      <Tab title="Benchmarking">
        Palmyra X4 consistently ranks at the top in structured output, API tool calling, and accuracy for complex, multi-step workflows.

        * **Top accuracy (ACC)**: Palmyra X4 achieves 78.76% accuracy in tool call identification and execution, leading the industry by nearly 20%.
        * **Structured call planning (AST)**: Palmyra X4 scores 87.93% in planning and organizing tool calls, accurately interpreting input, generating parameters, and sequencing steps.
        * **Execution performance (Exec)**: With an 88.27% score in executing tool calls, Palmyra X4 ranks highest in efficiently carrying out enterprise actions.
        * **Global benchmarks**: Palmyra X4 ranks in the world's top 10 on HELM Lite (86.1%) and HELM MMLU (81.3%), excelling across 57 subjects.
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="Palmyra X 003 Instruct" icon="book" iconType="regular">
    <Tabs>
      <Tab title="Overview">
        `palmyra-x-003-instruct` is highly proficient in generating precise and detailed responses. It's particularly useful for applications that require fine-grained language generation.

        **Pricing**:

        * Input: \$7.50 per 1M tokens
        * Output: \$22.50 per 1M tokens

        **Content window**: 32k
      </Tab>

      <Tab title="Use cases and capabilities">
        * **Instruction-based content generation**: Palmyra X 003 excels at following detailed instructions to create structured documents, from reports and proposals to step-by-step guides, assisting with accuracy and consistency across workflows.
        * **Data-driven analysis**: Ideal for complex datasets, Palmyra X 003 can analyze and summarize information into concise, actionable insights, making it easy for teams to digest lengthy reports or research findings quickly.
        * **Multilingual support**: Palmyra X 003's multilingual capabilities allow it to generate and adapt content across multiple languages, supporting enterprises with global operations.
      </Tab>

      <Tab title="Benchmarking">
        Palmyra X 003 launched as the #3 model on Stanford's HELM benchmark and has since claimed the top spot in translation accuracy. Its industry-leading performance in multilingual tasks ensures precise, culturally relevant translations, making it a trusted choice for global organizations that require consistent and reliable content across languages.

        | Model                    | GSM8K | LegalBench | MedQA | WMT 2014 |
        | ------------------------ | ----- | ---------- | ----- | -------- |
        | Palmyra X V3 (72B)       | 0.831 | 0.709      | 0.684 | 0.262    |
        | PaLM-2 (Unicorn)         | 0.831 | 0.677      | 0.684 | 0.26     |
        | PaLM-2 (Bison)           | 0.61  | 0.654      | 0.547 | 0.241    |
        | Claude 3 Opus (20240229) | 0.924 | 0.662      | 0.775 | 0.24     |
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="Palmyra Vision" icon="glasses" iconType="regular">
    <Tabs>
      <Tab title="Overview">
        `palmyra-vision` is specifically designed for processing images. It combines the power of natural language processing with computer vision techniques to analyze and generate textual descriptions of images. Palmyra Vision can be used for tasks such as image captioning, visual question answering, and image-to-text generation.

        **Pricing**:

        * Image: \$.005 per image
        * Video: \$.005 per second
        * Text: \$7.50 per 1M tokens

        **Content window**: 8k
      </Tab>

      <Tab title="Use cases and capabilities">
        * **Image-based compliance checks**: Palmyra Vision can identify and analyze visual elements helping enable you to meet your regulatory and brand guidelines and requirements.
        * **Product description generation**: Automatically generates detailed descriptions from product images, streamlining e-commerce workflows and enhancing catalog consistency.
        * **Chart and graph interpretation**: Transforms complex data visualizations into summarized, text-based insights, enabling quick analysis of trends and metrics in reports and presentations.
        * **Handwritten text extraction**: Accurately reads and digitizes handwritten notes or annotations, simplifying data entry and documentation processes.
      </Tab>

      <Tab title="Benchmarking">
        Palmyra Vision sets new standards in multimodal AI performance, excelling in key visual and text generation benchmarks.

        * **Visual Question Answering (VQAv2)**: Achieved an 84.4% accuracy rate, outperforming leading models like GPT-4V and Gemini 1.0 Ultra in interpreting and answering questions based on visual content.
        * **Image-text comprehension**: Consistently high performance in understanding and generating accurate text from diverse visual inputs, from scanned documents to complex graphics.
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="Palmyra Med" icon="stethoscope" iconType="regular">
    <Tabs>
      <Tab title="Overview">
        `palmyra-med` is a language model tailored for the healthcare industry. It is an assistive tool for processing, summarizing, and understanding extensive medical texts, making it ideal for comprehensive medical document analysis, patient record summarization, and supporting medical research.

        This model is not designed to provide medical advice, and must not be used for any diagnostic or therapeutic purposes. It is not to be used in direct patient care. Any output generated by the model must always be reviewed and verified by a qualified and licensed physician, based on their professional judgement, before any use is made of it.

        **Pricing**:

        * Input: \$5.00 per 1M tokens
        * Output: \$12.00 per 1M tokens

        **Content window**: 32k
      </Tab>

      <Tab title="Use cases and capabilities">
        * **Medical coding**: Palmyra Med supports highly accurate retrieval and application of medical codes, including RxNorm for medications, ICD-10-CM for diagnoses, and SNOMED CT for medical concepts, making it a powerful tool for healthcare documentation and billing.
        * **Clinical decision support**: With healthcare-specific knowledge, Palmyra Med can assist in diagnostics and treatment planning, helping healthcare providers make informed, data-backed decisions.
        * **Document summarization and reporting**: Optimized for summarizing lengthy medical records and generating concise reports, Palmyra Med enhances efficiency in patient documentation and case review.
      </Tab>

      <Tab title="Benchmarking">
        Palmyra Med sets the industry standard in healthcare-specific performance, excelling across a range of medical benchmarks with unmatched accuracy and clinical relevance.

        * **Overall medical benchmarks**: Palmyra Med averaged 85.9% across all medical benchmarks, surpassing Med-PaLM-2 by nearly 2 percentage points. Unlike Med-PaLM-2, which requires multiple examples to reach similar scores, Palmyra Med achieved these results in a zero-shot setting, highlighting its advanced capabilities.
        * **Clinical knowledge and anatomy**: Scoring 90.9% in MMLU Clinical Knowledge and 83.7% in MMLU Anatomy, Palmyra Med demonstrates a strong understanding of clinical procedures and human anatomy, making it an invaluable tool for assisting with medical analsyis and treatment planning.
        * **Genetics and college medicine**: With scores of 94.0% in Medical Genetics and 84.4% in College Medicine, Palmyra Med excels in interpreting genetic data and applying complex medical knowledge, supporting use cases in assisting with genetic counseling and medical education.
        * **Biomedical research**: Palmyra Med achieved 80% on PubMedQA, showcasing its ability to extract and analyze information from biomedical literature, which is essential for research and evidence-based medical practices.
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="Palmyra Fin" icon="money-bill" iconType="regular">
    <Tabs>
      <Tab title="Overview">
        `palmyra-fin` is a language model developed specifically for the financial sector. This model is an assistive tool for analyzing and synthesizing long financial documents, including comprehensive market reports, detailed investment analyses, and lengthy regulatory filings. With its ability to grasp complex financial narratives and perform deep contextual analysis, `palmyra-fin` is ideal for applications requiring a thorough understanding of extensive textual information.

        This model is not designed to assess the suitability of an investment or transaction, and must not be used directly to advise on or recommend any investment or financial transaction. Any output generated by the model must always be reviewed and verified by a qualified and licensed financial advisor, based on their professional judgment, before any use is made of it.

        **Pricing**:

        * Input: \$5.00 per 1M tokens
        * Output: \$12.00 per 1M tokens

        **Content window**: 128k
      </Tab>

      <Tab title="Use cases and capabilities">
        * **Market and financial analysis**: Palmyra Fin interprets and analyzes data trends, enabling financial analysts to generate insights and forecasts for strategic decision-making.
        * **Risk assessment**: With a deep understanding of financial language and terminology, Palmyra Fin helps assess risk factors, generating precise reports that aid in risk management compliance.
        * **Data summarization**: Palmyra Fin excels at summarizing complex financial documents, providing concise overviews and insights to support quick, informed decisions.
      </Tab>

      <Tab title="Benchmarking">
        Palmyra Fin leads the industry in financial expertise and benchmark performance, making it the top choice for finance-related AI applications.

        * **CFA Level III performance**: Palmyra Fin scored 73% on the multiple-choice section of a CFA Level III sample test, becoming the first AI model to pass this prestigious exam. For perspective, the average passing score is 60%, and less than half of test takers typically pass. This achievement marks a significant leap over general-purpose models like GPT-4, which scored only 33%.
        * **Long-fin-eval benchmark**: In real-world financial tasks, Palmyra Fin outperformed popular models such as Claude 3.5 Sonnet, GPT-4o, and Mixtral-8x7b on the long-fin-eval benchmark, showcasing its superior financial acumen and capability across diverse financial use cases.
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="Palmyra Creative" icon="pen-fancy" iconType="regular">
    <Tabs>
      <Tab title="Overview">
        `palmyra-creative` is Writer's purpose-built language model, engineered to elevate creative thinking and writing across diverse professional contexts. With capabilities that amplify originality and adaptability, it caters to industries and teams where innovation drives success. Available via API, No-code tools, Agent Builder, and as an NVIDIA NIM microservice, Palmyra Creative is tailored to inspire bold ideas and solutions.

        **Pricing**:

        * Input: \$5.00 per 1M tokens
        * Output: \$12.00 per 1M tokens

        **Content window**: 128k
      </Tab>

      <Tab title="Use cases and capabilities">
        * **Imaginative brainstorming**: Palmyra Creative generates a wide range of unique, innovative ideas tailored to specific challenges. Whether brainstorming marketing campaigns or conceptualizing new products, it empowers users to think beyond the obvious.
        * **Enhanced storytelling**: The model transforms basic content into engaging, impactful narratives. From crafting compelling copy to simplifying technical explanations, Palmyra Creative ensures every story resonates with its audience.
        * **Retail**: Palmyra Creative empowers retailers to craft highly personalized marketing campaigns, design innovative loyalty programs, and develop engaging in-store experiences. For example, it can generate unique, on-brand promotional ideas or create compelling product descriptions that resonate with target audiences.
        * **Healthcare**: In healthcare, Palmyra Creative simplifies complex communications, inspires empathetic patient outreach strategies, and supports innovative research initiatives. It can help create accessible patient education materials, draft engaging wellness campaigns, or refine technical research papers for broader audiences.
        * **Finance**: For finance professionals, Palmyra Creative humanizes messaging, creates educational tools, and designs strategies to enhance portfolio performance. It can assist in simplifying complex financial concepts for clients, drafting engaging investment reports, or generating impactful outreach campaigns for wealth management firms.
      </Tab>

      <Tab title="Benchmarking">
        Measuring creativity is inherently challenging. Unlike traditional benchmarks that focus on accuracy or reasoning—like HELM or MMLU—creativity is subjective, messy, and thrives on adaptability and originality. Rather than fitting into rigid metrics, Palmyra Creative's impact is best demonstrated through comparisons with general-purpose models like Palmyra X4.

        Here, we showcase two examples that highlight Palmyra Creative's ability to transform workflows: brainstorming innovative strategies for a small-town bakery and refining a technical explanation to make it engaging and relatable.

        ### Example 1: Creative thinking

        **Prompt**: Imagine you're a struggling small-town bakery competing with a chain that opened across the street. Brainstorm unconventional strategies to win over customers without lowering prices.

        <Tabs>
          <Tab title="Palmyra Creative">
            The classic David vs. Goliath battle of the bakeries! Here are three unconventional strategies to help you, the plucky underdog, win over customers without sacrificing your margins:

            **Bake My Memory Experience**:
            Host free sensory baking sessions for seniors and individuals with memory loss. Recreate their favorite childhood treats and offer them for free. Word-of-Mouth will spread, and their families will follow.

            **Bake-Off with a Twist**:
            Host a baking competition where local businesses and groups compete to benefit a local charity. The winning team chooses the charity, and you provide a year's worth of free baked goods. Promote on social media and invite the community to cheer.

            **Breadwinner's Club Loyalty Program 2.0**:
            Ditch traditional loyalty cards. Create a "Breadwinner's Club" where customers earn "dough points" for completing baking challenges (try a new flavor, attend a class, share a photo). Redeem points for exclusive rewards, like a free custom cake or behind-the-scenes tour.
          </Tab>

          <Tab title="Palmyra X4">
            Absolutely, here are three unconventional strategies to help your small-town bakery compete with a chain:

            **Bakery Scavenger Hunt**:
            Organize a monthly scavenger hunt where participants have to find clues hidden around town that lead them back to your bakery. The winner gets a special prize, like a custom-designed cake or a free baking class. This not only creates excitement but also gets people talking about your bakery.

            **Bake-Off Challenges with Local Celebrities**:
            Host a bake-off challenge where local celebrities (like the mayor, a popular teacher, or a local athlete) compete against each other using your bakery's ingredients and recipes. Stream the event live on social media to generate buzz and engagement.

            **Personalized Baking Kits**:
            Offer DIY baking kits that include pre-measured ingredients and step-by-step instructions for customers to recreate your signature treats at home. This can be a fun family activity and also introduces your bakery's unique flavors to a wider audience.
          </Tab>
        </Tabs>

        ### Example 2: Creative writing

        **Prompt**: Write a guide for a programmer who wants to explain their AI side project to a grandparent. The explanation must be engaging, simple, and use humorous analogies, while avoiding technical jargon.

        <Tabs>
          <Tab title="Palmyra Creative">
            **Explaining AI to Grandma (or Grandpa) 101**

            **Step 1: Start with something familiar**
            "Hey Grandma, you know how you're amazing at recognizing my voice on the phone, even when I'm all grown up and sound like a stranger? That's kind of like what I've been working on with my computer project. But instead of voices, I'm teaching the computer to recognize patterns in things like pictures, words, and even conversations!"

            **Step 2: Introduce the "Super Smart Assistant"**
            "Imagine you had a super smart, super patient assistant who could help you with anything. You could show them a picture of a cat and say, 'What's that?' And they'd say, 'Oh, that's a cat!' But here's the cool part: the more pictures of cats you show them, the better they get at recognizing new pictures of cats they've never seen before!"

            **Step 3: Use a relatable example**
            "Think of it like when you were learning to bake your famous chocolate chip cookies. At first, you had to follow a recipe to the letter. But the more you baked, the more you could just look at the ingredients and the dough and say, 'Ah, yeah, I know exactly what to do!' That's kind of what I'm teaching the computer to do, but instead of cookies, it's learning to recognize patterns in data."

            **Step 4: Keep it light and fun**
            "Don't worry if it still sounds a bit like magic, Grandma! The important thing is that it's like having a really smart, really helpful friend who can assist us with all sorts of things. And who knows, maybe one day it'll even be able to recognize your famous cookie recipe just by looking at a picture!"
          </Tab>

          <Tab title="Palmyra X4">
            **Explaining Your AI Side Project to Grandma**

            **Step 1: Start with a Familiar Analogy**
            Imagine you're teaching a parrot to talk. You repeat words, and over time, the parrot learns to mimic you. AI is like a super smart parrot that can learn from lots of examples.

            **Step 2: Explain What AI Does**
            Just like how the parrot learns to say "Hello!" when you wave, AI can learn to recognize patterns. For example, it can learn to tell the difference between a cat and a dog in pictures.

            **Step 3: Describe Your Project**
            Let's say your project is about teaching AI to recognize different types of flowers. You can say, "I'm teaching the computer to be a flower expert. I show it lots of pictures of roses, daisies, and tulips, and it learns to tell them apart."

            **Step 4: Make It Relatable**
            You can joke, "It's like having a really helpful gardener who never forgets what each flower looks like, even if it's been a long time since they last saw it."

            **Step 5: Talk About the Benefits**
            Explain how this can be useful. For example, "This could help people who love gardening but have trouble remembering the names of all the flowers. They can just take a picture, and the AI will tell them what it is!"

            **Step 6: Keep It Light and Fun**
            End with a funny note, like, "And the best part is, unlike a real parrot, the computer won't squawk at you if you forget to feed it!"
          </Tab>
        </Tabs>
      </Tab>
    </Tabs>
  </Accordion>
</AccordionGroup>

## Using models with the Writer API

<Tabs>
  <Tab title="Chat completions">
    To select the Palmyra model you want to use for a chat completion, specify the model ID in the [`model` parameter](/api-reference/completion-api/chat-completion#body-model) of the request.

    Below is an example of specifying the `palmyra-x5` model in a chat completion request.

    <CodeGroup>
      ```bash cURL theme={null}
      curl --location 'https://api.writer.com/v1/chat' \
      --header 'Content-Type: application/json' \
      --header "Authorization: Bearer $WRITER_API_KEY" \
      --data '{
        "model": "palmyra-x5",
        "messages": [
          {
            "role": "user",
            "content": "Summarize GDPR compliance requirements for a cloud-based data storage provider"
          }
        ]
      }'
      ```

      ```python Python theme={null}
      from writerai import Writer

      # Initialize the client. If you don't pass the `api_key` parameter,
      # the client looks for the `WRITER_API_KEY` environment variable.
      client = Writer()

      chat_completion = client.chat.completions.create(
        model="palmyra-x5",
        messages=[
          {
            "role": "user",
            "content": "Summarize GDPR compliance requirements for a cloud-based data storage provider"
          }
        ]
      )

      print(chat_completion.choices[0].message.content)
      ```

      ```javascript JavaScript theme={null}
      import { Writer } from 'writer-sdk';

      // Initialize the client. If you don't pass the `apiKey` parameter,
      // the client looks for the `WRITER_API_KEY` environment variable.
      const client = new Writer();

      const chat_completion = await client.chat.completions.create({
        model: 'palmyra-x5',
        messages: [
          {
            "role": "user",
            "content": "Summarize GDPR compliance requirements for a cloud-based data storage provider"
          }
        ]
      });

      console.log(chat_completion.choices[0].message.content);
      ```
    </CodeGroup>

    You can also use prebuilt tools to interact with specialized LLMs within a general purpose chat completion request, or to use the Palmyra Vision model in a chat completion.

    See more details in the tool calling guides:

    * [LLM tool for calling specialized models](/home/model-delegation)
    * [Vision tool for analyzing images](/home/vision-tool)
  </Tab>

  <Tab title="Text generation">
    To select the Palmyra model you want to use for text generation, specify the model ID in the [`model` parameter](/api-reference/completion-api/text-generation#body-model) of the request.

    Below is an example of specifying the `palmyra-x5` model in a text generation request.

    <CodeGroup>
      ```bash cURL theme={null}
      curl --location 'https://api.writer.com/v1/completions' \
      --header 'Content-Type: application/json' \
      --header "Authorization: Bearer $WRITER_API_KEY" \
      --data '{
        "model": "palmyra-x5",
        "prompt": "Summarize GDPR compliance requirements for a cloud-based data storage provider"
      }'
      ```

      ```python Python theme={null}
      from writerai import Writer

      # Initialize the client. If you don't pass the `api_key` parameter,
      # the client looks for the `WRITER_API_KEY` environment variable.
      client = Writer()

      text_generation = client.completions.create(
        model="palmyra-x5",
        prompt="Summarize GDPR compliance requirements for a cloud-based data storage provider"
      )

      print(text_generation.choices[0].text)
      ```

      ```javascript JavaScript theme={null}
      import { Writer } from 'writer-sdk';

      // Initialize the client. If you don't pass the `apiKey` parameter,
      // the client looks for the `WRITER_API_KEY` environment variable.
      const client = new Writer();

      const text_generation = await client.completions.create({
        model: 'palmyra-x5',
        prompt: 'Summarize GDPR compliance requirements for a cloud-based data storage provider'
      });

      console.log(text_generation.choices[0].text);
      ```
    </CodeGroup>
  </Tab>
</Tabs>

Get started with the Writer API by signing up for a free account and following the [API quickstart](/home/quickstart).

## Deprecation policy

### Timeline for deprecation

* We'll announce the deprecation of a model at least three months in advance. This will give customers time to plan for the migration to the new model.
* We'll continue to support deprecated models for a period of time after they're deprecated. This will give customers time to migrate to the new model.
* We'll eventually stop supporting deprecated models. The timeline for this will vary depending on the model. We will announce the end of support for a deprecated model at least six months in advance.

### Deprecated models

| Model name             | Deprecation Date |
| ---------------------- | ---------------- |
| Palmyra Fin 32k        | 2025-03-03       |
| Palmyra X 002 32k      | 2024-09-06       |
| Palmyra X 32k Instruct | 2024-09-06       |
| Palmyra X 002 Instruct | 2024-09-06       |

### Migration path

* We'll provide customers with a migration path to the new model, including detailed documentation and support to help them migrate their applications.
* We'll also offer training and consulting services to help customers transition.
