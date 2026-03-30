# Source: https://docs.snowflake.com/en/sql-reference/functions-file.md

# File functions

File functions enable you to access files staged in cloud storage.

## List of functions

| Function Name | Notes |
| --- | --- |
| **Stages** |  |
| [GET_STAGE_LOCATION](functions/get_stage_location.md) | Returns the URL for an external or internal named stage using the stage name as the input. |
| [GET_RELATIVE_PATH](functions/get_relative_path.md) | Extracts the path of a staged file relative to its location in the stage using the stage name and absolute file path in cloud storage as inputs. |
| [GET_ABSOLUTE_PATH](functions/get_absolute_path.md) | Returns the absolute path of a staged file using the stage name and path of the file relative to its location in the stage as inputs. |
| [GET_PRESIGNED_URL](functions/get_presigned_url.md) | Generates the pre-signed URL to a staged file using the stage name and relative file path as inputs. Access files in an external stage using the function. |
| [BUILD_SCOPED_FILE_URL](functions/build_scoped_file_url.md) | Generates a scoped Snowflake file URL to a staged file using the stage name and relative file path as inputs. |
| [BUILD_STAGE_FILE_URL](functions/build_stage_file_url.md) | Generates a Snowflake file URL to a staged file using the stage name and relative file path as inputs. |
| **AI Functions** |  |
| [AI_COMPLETE](functions/ai_complete.md) | Generates a response (completion) from text or an image using a supported language model. |
| [AI_PARSE_DOCUMENT](functions/ai_parse_document.md) | Returns the extracted content from a document on a Snowflake stage as a JSON-formatted string. |
| [AI_TRANSCRIBE](functions/ai_transcribe.md) | Transcribes text from an audio file with optional timestamps and speaker labels. |

The following functions are for use with the FILE data type. For more information, see [Unstructured data types](data-types-unstructured.md).

| Sub-category | Function |
| --- | --- |
| Constructor | [TO_FILE](functions/to_file.md) |
|  | [TRY_TO_FILE](functions/try_to_file.md) |
| Accessors | [FL_GET_CONTENT_TYPE](functions/fl_get_content_type.md) |
|  | [FL_GET_ETAG](functions/fl_get_etag.md) |
|  | [FL_GET_FILE_TYPE](functions/fl_get_file_type.md) |
|  | [FL_GET_LAST_MODIFIED](functions/fl_get_last_modified.md) |
|  | [FL_GET_RELATIVE_PATH](functions/fl_get_relative_path.md) |
|  | [FL_GET_SCOPED_FILE_URL](functions/fl_get_scoped_file_url.md) |
|  | [FL_GET_SIZE](functions/fl_get_size.md) |
|  | [FL_GET_STAGE](functions/fl_get_stage.md) |
|  | [FL_GET_STAGE_FILE_URL](functions/fl_get_stage_file_url.md) |
| Utility Functions | [FL_IS_AUDIO](functions/fl_is_audio.md) |
|  | [FL_IS_COMPRESSED](functions/fl_is_compressed.md) |
|  | [FL_IS_DOCUMENT](functions/fl_is_document.md) |
|  | [FL_IS_IMAGE](functions/fl_is_image.md) |
|  | [FL_IS_VIDEO](functions/fl_is_video.md) |

## Usage notes

* GET_PRESIGNED_URL and BUILD_SCOPED_FILE_URL are non-deterministic functions; the others are deterministic.
