# Source: https://www.traceloop.com/docs/integrations/github.md

# GitHub

> Run experiments in CI and get evaluation results directly in your pull requests

# Track Experiment Results in CI

Instead of deploying blindly and hoping for the best, you can validate changes with real data before they reach production.

Create experiments that automatically run your agent flow in CI, test your changes against production-quality datasets, and get comprehensive evaluation results directly in your pull request. This ensures every change is validated with the same rigor as your application code.

## How It Works

Run an experiment in your CI/CD pipeline with the Traceloop GitHub App integration. Receive experiment evaluation results as comments on your pull requests, helping you validate AI model changes, prompt updates, and configuration modifications before merging to production.

<Steps>
  <Step title="Install the Traceloop GitHub App">
    Go to the [integrations page](https://app.traceloop.com/settings/integrations) within Traceloop and click on the GitHub card.

    Click "Install GitHub App" to be redirected to GitHub where you can install the Traceloop app for your organization or personal account.

    <Info>
      You can also install Traceloop GitHub app [here](https://github.com/apps/traceloop/installations/new)
    </Info>
  </Step>

  <Step title="Configure Repository Access">
    Select the repositories where you want to enable Traceloop experiment runs. You can choose:

    * All repositories in your organization
    * Specific repositories only

    After installing the app you will be redirected to a Traceloop authorization page.

    <Info>
      **Permissions Required:** The app needs read access to your repository contents and write access to pull requests to post evaluation results as comments.
    </Info>
  </Step>

  <Step title="Authorize GitHub app installation at Traceloop">
    <Frame>
      <img className="block dark:hidden" src="https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-auth-light.png?fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=503c0d33e8c72f0fceadea948f723d17" data-og-width="1366" width="1366" data-og-height="1156" height="1156" data-path="img/traceloop-integrations/github-app-auth-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-auth-light.png?w=280&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=783d65809f70ffae9108462044beb75d 280w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-auth-light.png?w=560&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=ab307178cde06ff03be22327ba222fb4 560w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-auth-light.png?w=840&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=be3f08b4694738bdd58182c10d68b35e 840w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-auth-light.png?w=1100&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=f509ac6671695237f69880e49f6714a2 1100w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-auth-light.png?w=1650&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=70318f43eb849ee706d4f73770a32238 1650w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-auth-light.png?w=2500&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=80fa7df8037c5bc750909469bc433e98 2500w" />

      <img className="hidden dark:block" src="https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-auth-dark.png?fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=d4c9f83be0a7e50ab7c16e8090a77255" data-og-width="1366" width="1366" data-og-height="1156" height="1156" data-path="img/traceloop-integrations/github-app-auth-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-auth-dark.png?w=280&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=40acafc4c996b059960626aa67d38405 280w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-auth-dark.png?w=560&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=70105bf56170292d3865ec73d3670035 560w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-auth-dark.png?w=840&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=a5d13263c4235bf4a1187befe9b47094 840w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-auth-dark.png?w=1100&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=4127d3725e7876a0973ec70f994fe3c9 1100w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-auth-dark.png?w=1650&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=3a2b998002238d606e5bc2ae5fafb07d 1650w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-auth-dark.png?w=2500&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=0cc1ea5867e034f4a22b0528a7fe6f23 2500w" />
    </Frame>
  </Step>

  <Step title="Create Your Experiment Script">
    Create an [experiment](/experiments/introduction) script that runs your AI flow. An experiment consists of three key components:

    * **[Dataset](/datasets/quick-start)**: A collection of test inputs that represent real-world scenarios your AI will handle
    * **Task Function**: Your AI flow code that processes each dataset row (e.g., calling your LLM, running RAG, executing agent logic)
    * **[Evaluators](/evaluators/intro)**: Automated quality checks that measure your AI's performance (e.g., accuracy, safety, relevance)

    The experiment runs your task function on every row in the dataset, then applies evaluators to measure quality. This validates your changes with real data before production.

    The script below shows how to test a question-answering flow:

    <CodeGroup>
      ```python Python theme={null}
      import asyncio
      import os
      from openai import AsyncOpenAI
      from traceloop.sdk import Traceloop
      from traceloop.sdk.experiment.model import RunInGithubResponse

      # Initialize Traceloop client
      client = Traceloop.init(
        app_name="research-experiment-ci-cd"
      )

      async def generate_research_response(question: str) -> str:
      """Generate a research response using OpenAI"""
      openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

      response = await openai_client.chat.completions.create(
          model="gpt-4",
          messages=[
              {
                  "role": "system",
                  "content": "You are a helpful research assistant. Provide accurate, well-researched answers.",
              },
              {"role": "user", "content": question},
          ],
          temperature=0.7,
          max_tokens=500,
      )

      return response.choices[0].message.content


      async def research_task(row):
      """Task function that processes each dataset row"""
      query = row.get("query", "")
      answer = await generate_research_response(query)

      return {
          "completion": answer,
          "question": query,
          "sentence": answer
      }


      async def main():
      """Run experiment in GitHub context"""
      print("🚀 Running research experiment in GitHub CI/CD...")

      # Execute tasks locally and send results to backend
      response = await client.experiment.run(
          task=research_task,
          dataset_slug="research-queries",
          dataset_version="v2",
          evaluators=["research-word-counter", "research-relevancy"],
          experiment_slug="research-exp",
      )

      if isinstance(response, RunInGithubResponse):
          print(f"Experiment {response.experiment_slug} completed!")


      if __name__ == "__main__":
      asyncio.run(main())
      ```

      ```typescript TypeScript theme={null}
      import * as traceloop from "@traceloop/node-server-sdk";
      import { OpenAI } from "openai";
      import type { ExperimentTaskFunction } from "@traceloop/node-server-sdk";

      // Initialize Traceloop
      traceloop.initialize({
      appName: "research-experiment-ci-cd",
      disableBatch: true,
      traceloopSyncEnabled: true,
      });

      await traceloop.waitForInitialization();
      const client = traceloop.getClient();

      /**
      * Generate a research response using OpenAI
      */
      async function generateResearchResponse(question: string): Promise<string> {
      const openai = new OpenAI({
      apiKey: process.env.OPENAI_API_KEY,
      });

      const response = await openai.chat.completions.create({
      model: "gpt-4",
      messages: [
        {
          role: "system",
          content: "You are a helpful research assistant. Provide accurate, well-researched answers.",
        },
        { role: "user", content: question },
      ],
      temperature: 0.7,
      max_tokens: 500,
      });

      return response.choices?.[0]?.message?.content || "";
      }

      /**
      * Task function that processes each dataset row
      */
      const researchTask: ExperimentTaskFunction = async (row) => {
      const query = (row.query as string) || "";
      const answer = await generateResearchResponse(query);

      return {
      completion: answer,
      question: query,
      sentence: answer,
      };
      };

      /**
      * Run experiment in GitHub context
      */
      async function main() {
      console.log("🚀 Running research experiment in GitHub CI/CD...");

      // Execute tasks locally and send results to backend
      const response = await client.experiment.run(researchTask, {
      datasetSlug: "research-queries",
      datasetVersion: "v2",
      evaluators: ["research-word-counter", "research-relevancy"],
      experimentSlug: "research-exp",
      });

      console.log(`Experiment research-exp completed!`);
      }

      main().catch((error) => {
      console.error("Experiment failed:", error);
      process.exit(1);
      });
      ```
    </CodeGroup>
  </Step>

  <Step title="Set up Your CI Workflow">
    Add a GitHub Actions workflow to automatically run Traceloop experiments on pull requests.
    Below is an example workflow file you can customize for your project:

    ```yaml ci-cd configuration  theme={null}
    name: Run Traceloop Experiments

    on:
      pull_request:
        branches: [main, master]

    jobs:
      run-experiments:
        runs-on: ubuntu-latest

        steps:
          - name: Checkout code
            uses: actions/checkout@v4

          - name: Set up Python
            uses: actions/setup-python@v5
            with:
              python-version: '3.11'

          - name: Install dependencies
            run: |
              pip install traceloop-sdk openai

          - name: Run experiments
            env:
              TRACELOOP_API_KEY: ${{ secrets.TRACELOOP_API_KEY }}
              OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
            run: |
              python experiments/run_ci_experiments.py
    ```

    <Note>
      **Add secrets to your GitHub repository**

      Make sure all secrets used in your experiment script (like `OPENAI_API_KEY`) are added to both:

      * Your GitHub Actions workflow configuration
      * Your GitHub repository secrets

      Traceloop requires you to add `TRACELOOP_API_KEY` to your GitHub repository secrets. [Generate one in Settings →](/settings/managing-api-keys)
    </Note>

    <Frame>
      <img className="block dark:hidden" src="https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-secrets-light.png?fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=f580a641f03ddae2dbdd20430cd1b7c3" data-og-width="2248" width="2248" data-og-height="566" height="566" data-path="img/traceloop-integrations/github-app-secrets-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-secrets-light.png?w=280&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=7f21d7e17579492e81b1b95e11e72071 280w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-secrets-light.png?w=560&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=05f0b56c16ea976cafe6fd0b7bba2700 560w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-secrets-light.png?w=840&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=cf4bd460e1e8040b08396084b50aaf91 840w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-secrets-light.png?w=1100&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=2e1a406d64bf06e9c59016200bf10225 1100w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-secrets-light.png?w=1650&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=7bcafc0f12fa6fe25c63f962eb71b6f4 1650w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-secrets-light.png?w=2500&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=51834a3f63c4ef40b7dd7710d9bced5c 2500w" />

      <img className="hidden dark:block" src="https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-secrets-dark.png?fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=2922e81fc98d30b96ac5bf2f2b5312ea" data-og-width="2248" width="2248" data-og-height="566" height="566" data-path="img/traceloop-integrations/github-app-secrets-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-secrets-dark.png?w=280&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=16e38ab5a92712b613334b9a5765c976 280w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-secrets-dark.png?w=560&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=dc93eb07251cddc0625585fe172d7ab8 560w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-secrets-dark.png?w=840&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=51856b574b5dd028f8df5a24cd466dd4 840w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-secrets-dark.png?w=1100&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=82a616c5debee3bc9a59c12fb8906db7 1100w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-secrets-dark.png?w=1650&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=7750728ed862ab833d5ef9f4d139820d 1650w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-secrets-dark.png?w=2500&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=d0c6cb0aea751dcafc2c54996f81461d 2500w" />
    </Frame>
  </Step>

  <Step title="View Results in Your Pull Request">
    Once configured, every pull request will automatically trigger the experiment run. The Traceloop GitHub App will post a comment on the PR with a comprehensive summary of the evaluation results.

    <Frame>
      <img className="block dark:hidden" src="https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-comment-light.png?fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=29082d266b0e447fe36306aec969cef9" data-og-width="918" width="918" data-og-height="531" height="531" data-path="img/traceloop-integrations/github-app-comment-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-comment-light.png?w=280&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=99d2b0305e3de24ebfb04ebb2c1fd721 280w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-comment-light.png?w=560&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=bd610949e4a760ab835449aad2aa003d 560w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-comment-light.png?w=840&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=039170b3f8e8b0ccb93da1ca9b93dc5d 840w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-comment-light.png?w=1100&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=456856c0270c58968b1bfb29ec7fea28 1100w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-comment-light.png?w=1650&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=a0c013cdfff0b7b48c1cd52c1f860840 1650w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-comment-light.png?w=2500&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=44b83ec4e1a2a5ccde0311d940f9fd85 2500w" />

      <img className="hidden dark:block" src="https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-comment-dark.png?fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=25120a30f67e789ae23020224c33161a" data-og-width="918" width="918" data-og-height="531" height="531" data-path="img/traceloop-integrations/github-app-comment-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-comment-dark.png?w=280&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=7f8b1d88d2c19524a85601e947b97248 280w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-comment-dark.png?w=560&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=0d59fc0f32a88f65909df07e121d7a1f 560w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-comment-dark.png?w=840&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=99d019e929a06ad83a151702d45341b0 840w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-comment-dark.png?w=1100&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=606d4e1068546c443ed0ce741fda867c 1100w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-comment-dark.png?w=1650&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=422aeb83d7ba8023d3ffa02f56baf790 1650w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-comment-dark.png?w=2500&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=c0351df6ccae448230286a46a84f81ab 2500w" />
    </Frame>

    The PR comment includes:

    * **Overall experiment status**
    * **Evaluation metrics**
    * **Link to detailed results**

    ### Experiment Dashboard

    Click on the link in the PR comment to view the complete experiment run in the Traceloop experiment dashboard, where you can:

    * Review individual test cases and their evaluator scores
    * Analyze which specific inputs passed or failed
    * Compare results with previous runs to track improvements or regressions
    * Drill down into evaluator reasoning and feedback

    <Frame>
      <img className="block dark:hidden" src="https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-exp-run-results-light.png?fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=f48438b396576113e46dcdb947392033" data-og-width="2476" width="2476" data-og-height="1514" height="1514" data-path="img/traceloop-integrations/github-app-exp-run-results-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-exp-run-results-light.png?w=280&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=35d99650899b9b88501d09ec629f1072 280w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-exp-run-results-light.png?w=560&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=3be1ae25bd206a124b64494fcad5f4a1 560w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-exp-run-results-light.png?w=840&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=8e5b8c3f83d2fc664cae0863186c28d8 840w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-exp-run-results-light.png?w=1100&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=0dd11e6b9077a6bb41a10d3bf46696f0 1100w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-exp-run-results-light.png?w=1650&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=775589dff86c5764610dd979740415b0 1650w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-exp-run-results-light.png?w=2500&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=efd8a35ee82c2db42dc9f96239022629 2500w" />

      <img className="hidden dark:block" src="https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-exp-run-results-dark.png?fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=5a0023b8a84b42045de88ae32b620d79" data-og-width="2476" width="2476" data-og-height="1514" height="1514" data-path="img/traceloop-integrations/github-app-exp-run-results-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-exp-run-results-dark.png?w=280&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=840838398a0eeaa2f7d3c04bc5d8ff81 280w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-exp-run-results-dark.png?w=560&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=33193cac0373ed069aa6e2d115a8efec 560w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-exp-run-results-dark.png?w=840&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=8bc19177c80060257166bde8217f9d6d 840w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-exp-run-results-dark.png?w=1100&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=a419410f3619d2cc96e346a7bba5caf1 1100w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-exp-run-results-dark.png?w=1650&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=b2427a47a2e71153aac0d56c4ccaed42 1650w, https://mintcdn.com/enrolla/Xvmb1kKCuNCuc41v/img/traceloop-integrations/github-app-exp-run-results-dark.png?w=2500&fit=max&auto=format&n=Xvmb1kKCuNCuc41v&q=85&s=ce85e2355a2caeb2569370ae878a6fda 2500w" />
    </Frame>
  </Step>
</Steps>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://www.traceloop.com/docs/llms.txt