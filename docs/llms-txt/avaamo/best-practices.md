# Source: https://docs.avaamo.com/user-guide/ref/best-practices.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/best-practices.md

# Source: https://docs.avaamo.com/user-guide/llamb/regression-testing/best-practices.md

# Best Practices

* Collaborate with **subject matter experts** to build a regression test file during the discovery phase.
* Iteratively test and improve throughout the development and testing phase before entering the UAT phase of the project.
* **Use a sample file for reference:** To prevent errors in the input file, use the sample file available for download during the input file upload process. Refer to [Run regression test](https://docs.avaamo.com/user-guide/llamb/regression-testing/run-regression-test) for more details.
* **Match query and test language:** To avoid inconsistent results in regression tests, always ensure that the `selected test language` matches the `input file language`. This helps in accurately evaluating responses.
* **Avoid using incorrect input files:**&#x20;

  * Ensure the input file does not contain empty query fields.
  * Ensure there are no extra rows or extra columns.
  * Ensure there are no blank entries between queries.
  * Ensure the input file is not empty.

  If any of these conditions are found, the upload of an input file gets rejected.
* **Use corrected queries:** Ensure all queries are properly structured and refined to improve response accuracy. You can test the conversation in the web channel to validate the corrected query before using it in the input file.
* **Use fully formed queries:** Avoid incomplete or fragmented queries or short queries, as they may lead to inaccurate responses. Always provide clear, complete, and well-structured input to ensure responses are accurate and consistent.

  **Examples of fully formed queries:**

  * **Short query:** EPF?\
    **Fully formed query:** What is EPF?
  * **Co-referencing query:**\
    **Q1:** What is the population of Japan?\
    **Q2:** And how about France?\
    **Fully formed query:** What is the population of France?
  * **Fragmented query:** New York weather\
    **Fully formed query:** How is the weather today in New York?
* **Avoid co-reference in queries:** Queries should be self-contained without relying on the previous context to generate accurate results.
* **Check for spelling errors:** Ensure all queries are free from typos and spelling mistakes to avoid misinterpretation by the model.
* **Limit per regression test file:** Each regression test file should contain a maximum of **1,000 questions** to ensure efficient processing and accurate evaluation.
* **Ground Truth relevance:**&#x20;
  * Ensure that the `ground_truth` is **directly aligned with the intent** of the query.
  * It should reflect the **ideal or expected answer** that the model is being evaluated against.
* **Completeness of Ground Truth:**&#x20;
  * Avoid partial or vague `ground_truth` responses.
  * Ensure the expected answer is **complete and self-contained**, offering sufficient context for an accurate assessment.
* **Leveraging `user_properties` for contextual responses**
  * Use `user_properties` effectively to retrieve context-specific responses.
  * This helps align model outputs with relevant `document_properties` from source content, ensuring answers are contextualized based on both user and document metadata.
* **Be precise when expecting specific answers**
  * When asking a query that expects a **specific number or type of answers,** be clear and precise in your wording. This ensures consistency and clarity in the model’s responses.
