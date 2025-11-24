# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/create-an-evaluation-set.md

# Create an Evaluation Set

> Before starting your experiments, we recommend creating an evaluation set.

**Best Practices:**

1. **Representativeness:** Ensure that the evaluation set is representative of the real-world data or the population of interest. This means the data should reflect the full range of variations expected in the actual use case, including different demographics, behaviors, or other relevant characteristics.

2. **Separation from Training Data:** The evaluation set should be entirely separate from the training dataset. Using different data ensures that you are testing the application's ability to generalize to new, unseen data.

3. **Sufficient Size:** The evaluation set should be large enough to provide statistically meaningful results. The size will depend on the complexity of the application and the variability of the data. As a rule of thumb, we recommend 50-100 data points for most basic use cases. A few hundred for more mature ones.

4. **Update Regularly:** As more data becomes available, or as the real-world conditions change, update the evaluation set to continue reflecting the target environment accurately. This is especially important for models deployed in rapidly changing fields.

5. **Over-represent edge cases:** Include tough scenarios you want your application to handle well (e.g. prompt injections, abusive requests, angry users, irrelevant questions). It's important to include these to battle-test your application against outlier and abusive behavior.

Your Evaluation Set should stay constant throughout your experiments. This will allow you to make apple-to-apples comparisons for the runs on your projects.

Note: Using GPT4 or similar can be a quick and easy way to bootstrap an evaluation set. We recommend manually going over the questions and editing as well.

###

**Running Evaluations on your Eval Set**

Once you have your Eval Set, you're ready to start your first evaluation run.

* If you have not written any code yet and are looking to evaluate a model and template for your use case, check out [Creating Prompt Runs](/galileo/gen-ai-studio-products/galileo-evaluate/quickstart).

* If you have an application or prototype you'd like to evaluate, check out [Integrating Evaluate into my existing application](/galileo/gen-ai-studio-products/galileo-evaluate/quickstart/integrate-evaluate-into-my-existing-application-with-python).
