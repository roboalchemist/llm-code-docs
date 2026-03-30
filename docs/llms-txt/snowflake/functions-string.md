# Source: https://docs.snowflake.com/en/sql-reference/functions-string.md

# String & binary functions

This family of functions perform operations on a string input value, or binary input value (for certain functions), and return a string or numeric value.

The functions are grouped by type of operation performed.

| Function Name | Binary Input Supported | Collation Supported | Notes |
| --- | --- | --- | --- |
| **General Manipulation** |  |  |  |
| [ASCII](functions/ascii.md) |  |  |  |
| [BIT_LENGTH](functions/bit_length.md) | ✔ |  |  |
| [CHR , CHAR](functions/chr.md) |  |  |  |
| [CONCAT , ||](functions/concat.md) | ✔ | ✔ |  |
| [CONCAT_WS](functions/concat_ws.md) | ✔ | ✔ |  |
| [INSERT](functions/insert.md) | ✔ |  |  |
| [LENGTH, LEN](functions/length.md) | ✔ |  |  |
| [LPAD](functions/lpad.md) | ✔ |  |  |
| [LTRIM](functions/ltrim.md) |  |  |  |
| [OCTET_LENGTH](functions/octet_length.md) | ✔ |  |  |
| [PARSE_IP](functions/parse_ip.md) |  |  |  |
| [PARSE_URL](functions/parse_url.md) |  |  |  |
| [REPEAT](functions/repeat.md) |  |  |  |
| [REVERSE](functions/reverse.md) | ✔ |  |  |
| [RPAD](functions/rpad.md) | ✔ |  |  |
| [RTRIM](functions/rtrim.md) |  |  |  |
| [RTRIMMED_LENGTH](functions/rtrimmed_length.md) |  |  |  |
| [SOUNDEX](functions/soundex.md) |  |  |  |
| [SOUNDEX_P123](functions/soundex_p123.md) |  |  |  |
| [SPACE](functions/space.md) |  |  |  |
| [SPLIT](functions/split.md) |  | ✔ | Provides partial support for collation. For details, see the documentation of the function. |
| [SPLIT_PART](functions/split_part.md) |  |  |  |
| [SPLIT_TO_TABLE](functions/split_to_table.md) |  |  |  |
| [STRTOK](functions/strtok.md) |  |  |  |
| [STRTOK_TO_ARRAY](functions/strtok_to_array.md) |  |  |  |
| [STRTOK_SPLIT_TO_TABLE](functions/strtok_split_to_table.md) |  |  |  |
| [TRANSLATE](functions/translate.md) |  |  |  |
| [TRIM](functions/trim.md) |  |  |  |
| [UNICODE](functions/unicode.md) |  |  |  |
| [UUID_STRING](functions/uuid_string.md) |  |  |  |
| **Full-Text Search** |  |  |  |
| [SEARCH](functions/search.md) |  |  |  |
| [SEARCH_IP](functions/search_ip.md) |  |  |  |
| **Case Conversion** |  |  |  |
| [INITCAP](functions/initcap.md) |  |  |  |
| [LOWER](functions/lower.md) |  |  |  |
| [UPPER](functions/upper.md) |  |  |  |
| **Regular Expression Matching** |  |  |  |
| [[ NOT ] REGEXP](functions/regexp.md) |  |  | Alias for RLIKE. |
| [REGEXP_COUNT](functions/regexp_count.md) |  |  |  |
| [REGEXP_EXTRACT_ALL](functions/regexp_substr_all.md) |  |  | Alias for REGEXP_SUBSTR_ALL. |
| [REGEXP_INSTR](functions/regexp_instr.md) |  |  |  |
| [REGEXP_LIKE](functions/regexp_like.md) |  |  | Alias for RLIKE. |
| [REGEXP_REPLACE](functions/regexp_replace.md) |  |  |  |
| [REGEXP_SUBSTR](functions/regexp_substr.md) |  |  |  |
| [REGEXP_SUBSTR_ALL](functions/regexp_substr_all.md) |  |  |  |
| [[ NOT ] RLIKE](functions/rlike.md) |  |  |  |
| **Other Matching/Comparison** |  |  |  |
| [CHARINDEX](functions/charindex.md) | ✔ | ✔ | Alias for POSITION. Provides partial support for collation. For details, see the documentation of the POSITION function. |
| [CONTAINS](functions/contains.md) | ✔ | ✔ | Provides partial support for collation. For details, see the documentation of the function. |
| [EDITDISTANCE](functions/editdistance.md) |  |  |  |
| [ENDSWITH](functions/endswith.md) | ✔ | ✔ | Provides partial support for collation. For details, see the documentation of the function. |
| [[ NOT ] ILIKE](functions/ilike.md) |  |  | Case-insensitive alternative for LIKE. |
| [ILIKE ANY](functions/ilike_any.md) |  |  | Case-insensitive alternative for LIKE ANY. |
| [JAROWINKLER_SIMILARITY](functions/jarowinkler_similarity.md) |  |  |  |
| [LEFT](functions/left.md) | ✔ | ✔ |  |
| [[ NOT ] LIKE](functions/like.md) |  |  |  |
| [LIKE ALL](functions/like_all.md) |  |  |  |
| [LIKE ANY](functions/like_any.md) |  |  |  |
| [POSITION](functions/position.md) | ✔ | ✔ | Provides partial support for collation. For details, see the documentation of the function. |
| [REPLACE](functions/replace.md) |  |  |  |
| [RIGHT](functions/right.md) | ✔ | ✔ |  |
| [STARTSWITH](functions/startswith.md) | ✔ | ✔ | Provides partial support for collation. For details, see the documentation of the function. |
| [SUBSTR , SUBSTRING](functions/substr.md) | ✔ | ✔ |  |
| **Compression/Decompression** |  |  |  |
| [COMPRESS](functions/compress.md) | ✔ |  |  |
| [DECOMPRESS_BINARY](functions/decompress_binary.md) | ✔ |  |  |
| [DECOMPRESS_STRING](functions/decompress_string.md) | ✔ |  |  |
| **Encoding/Decoding** |  |  |  |
| [BASE64_DECODE_BINARY](functions/base64_decode_binary.md) |  |  |  |
| [BASE64_DECODE_STRING](functions/base64_decode_string.md) |  |  |  |
| [BASE64_ENCODE](functions/base64_encode.md) | ✔ |  |  |
| [HEX_DECODE_BINARY](functions/hex_decode_binary.md) |  |  |  |
| [HEX_DECODE_STRING](functions/hex_decode_string.md) |  |  |  |
| [HEX_ENCODE](functions/hex_encode.md) | ✔ |  |  |
| [TRY_BASE64_DECODE_BINARY](functions/try_base64_decode_binary.md) |  |  | Error-handling version of BASE64_DECODE_BINARY. |
| [TRY_BASE64_DECODE_STRING](functions/try_base64_decode_string.md) |  |  | Error-handling version of BASE64_DECODE_STRING. |
| [TRY_HEX_DECODE_BINARY](functions/try_hex_decode_binary.md) |  |  | Error-handling version of HEX_DECODE_BINARY. |
| [TRY_HEX_DECODE_STRING](functions/try_hex_decode_string.md) |  |  | Error-handling version of HEX_DECODE_STRING. |
| **Cryptographic/Checksum** |  |  |  |
| [MD5 , MD5_HEX](functions/md5.md) |  |  | Intended primarily for checksum operations. Not recommended for cryptography. |
| [MD5_BINARY](functions/md5_binary.md) |  |  | Intended primarily for checksum operations. Not recommended for cryptography. |
| [MD5_NUMBER_LOWER64](functions/md5_number_lower64.md) |  |  | Intended primarily for checksum operations. Not recommended for cryptography. |
| [MD5_NUMBER_UPPER64](functions/md5_number_upper64.md) |  |  | Intended primarily for checksum operations. Not recommended for cryptography. |
| [SHA1 , SHA1_HEX](functions/sha1.md) |  |  |  |
| [SHA1_BINARY](functions/sha1_binary.md) |  |  |  |
| [SHA2 , SHA2_HEX](functions/sha2.md) |  |  |  |
| [SHA2_BINARY](functions/sha2_binary.md) |  |  |  |
| **Hash (Non-cryptographic)** |  |  |  |
| [HASH](functions/hash.md) | ✔ |  | Allows data types other than string and binary. Not intended for cryptography. |
| [HASH_AGG](functions/hash_agg.md) | ✔ |  | Allows data types other than string and binary. Not intended for cryptography. |
| **Collation** |  |  |  |
| [COLLATE](functions/collate.md) |  |  |  |
| [COLLATION](functions/collation.md) |  |  |  |
| **AI Functions** |  |  |  |
| [AGENT_RUN (SNOWFLAKE.CORTEX)](functions/agent_run-snowflake-cortex.md) |  |  |  |
| [AI_AGG](functions/ai_agg.md) |  |  |  |
| [AI_CLASSIFY](functions/ai_classify.md) |  |  |  |
| [AI_COMPLETE](functions/ai_complete.md) |  |  |  |
| [AI_COUNT_TOKENS](functions/ai_count_tokens.md) |  |  |  |
| [AI_EMBED](functions/ai_embed.md) |  |  |  |
| [AI_FILTER](functions/ai_filter.md) |  |  |  |
| [AI_REDACT](functions/ai_redact.md) |  |  |  |
| [AI_SENTIMENT](functions/ai_sentiment.md) |  |  |  |
| [AI_SIMILARITY](functions/ai_similarity.md) |  |  |  |
| [AI_SUMMARIZE_AGG](functions/ai_summarize_agg.md) |  |  |  |
| [AI_TRANSLATE](functions/ai_translate.md) |  |  |  |
| [CLASSIFY_TEXT (SNOWFLAKE.CORTEX)](functions/classify_text-snowflake-cortex.md) |  |  |  |
| [COMPLETE (SNOWFLAKE.CORTEX)](functions/complete-snowflake-cortex.md) |  |  |  |
| [DATA_AGENT_RUN (SNOWFLAKE.CORTEX)](functions/data_agent_run-snowflake-cortex.md) |  |  |  |
| [EMBED_TEXT_768 (SNOWFLAKE.CORTEX)](functions/embed_text-snowflake-cortex.md) |  |  |  |
| [EMBED_TEXT_1024 (SNOWFLAKE.CORTEX)](functions/embed_text_1024-snowflake-cortex.md) |  |  |  |
| [ENTITY_SENTIMENT (SNOWFLAKE.CORTEX)](functions/entity_sentiment-snowflake-cortex.md) |  |  |  |
| [EXTRACT_ANSWER (SNOWFLAKE.CORTEX)](functions/extract_answer-snowflake-cortex.md) |  |  |  |
| [FINETUNE (SNOWFLAKE.CORTEX)](functions/finetune-snowflake-cortex.md) |  |  |  |
| [PARSE_DOCUMENT (SNOWFLAKE.CORTEX)](functions/parse_document-snowflake-cortex.md) |  |  |  |
| [SPLIT_TEXT_MARKDOWN_HEADER (SNOWFLAKE.CORTEX)](functions/split_text_markdown_header-snowflake-cortex.md) |  |  |  |
| [SPLIT_TEXT_RECURSIVE_CHARACTER (SNOWFLAKE.CORTEX)](functions/split_text_recursive_character-snowflake-cortex.md) |  |  |  |
| [SENTIMENT (SNOWFLAKE.CORTEX)](functions/sentiment-snowflake-cortex.md) |  |  |  |
| [SUMMARIZE (SNOWFLAKE.CORTEX)](functions/summarize-snowflake-cortex.md) |  |  |  |
| [TRANSLATE (SNOWFLAKE.CORTEX)](functions/translate-snowflake-cortex.md) |  |  |  |
| [COUNT_TOKENS (SNOWFLAKE.CORTEX)](functions/count_tokens-snowflake-cortex.md) |  |  |  |
| [TRY_COMPLETE (SNOWFLAKE.CORTEX)](functions/try_complete-snowflake-cortex.md) |  |  |  |
| [SEARCH_PREVIEW (SNOWFLAKE.CORTEX)](functions/search_preview-snowflake-cortex.md) |  |  |  |
