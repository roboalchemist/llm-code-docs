# Source: https://docs.snowflake.com/en/release-notes/2025/other/2025-09-25-file-data-type-ga.md

# Sep 25, 2025: FILE data type (*General availability*)

The FILE data type enables multimodal Cortex AI Functions workflows with unstructured data stored on internal or external stages. FILE
values provide a way to reference files without encapsulating the actual file content. FILE objects let you:

* Store references to files in tables and pass them to Cortex AI Functions like AI_COMPLETE, AI_CLASSIFY, AI_EXTRACT,
  AI_PARSE_DOCUMENT, and AI_TRANSCRIBE for automated multimodal processing workflows.
* Avoid duplicating file data and process it more efficiently by creating ad passing FILE values as references.
* Integrate with existing data architectures by combining DIRECTORY functions with TO_FILE to create FILE references
  for entire collections of files for batch processing.

For more information, see the [FILE data type](../../../sql-reference/data-types-unstructured.md) and the [TO_FILE function](../../../sql-reference/functions/to_file.md).
