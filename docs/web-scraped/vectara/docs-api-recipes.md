# Source: https://docs.vectara.com/docs/api-recipes

Title: API Recipes | Vectara Docs

URL Source: https://docs.vectara.com/docs/api-recipes

Markdown Content:
Explore common API patterns and use cases for building with Vectara. Each recipe shows complete request and response examples you can adapt for your application.

How to use these recipes[​](https://docs.vectara.com/docs/api-recipes#how-to-use-these-recipes "Direct link to How to use these recipes")
-----------------------------------------------------------------------------------------------------------------------------------------

These examples demonstrate real-world patterns for working with the Vectara API:

*   [**Search for answers in a corpus**](https://docs.vectara.com/docs/api-recipes#search-for-answers-in-a-corpus)
*   [**Add content to a corpus**](https://docs.vectara.com/docs/api-recipes#add-content-to-a-corpus)
*   [**Query with result limits**](https://docs.vectara.com/docs/api-recipes#query-with-result-limits)
*   [**List and delete corpora**](https://docs.vectara.com/docs/api-recipes#list-and-delete-corpora)

**Ready to explore?** Each recipe includes complete code examples with explanations.

Search for answers in a corpus[​](https://docs.vectara.com/docs/api-recipes#search-for-answers-in-a-corpus "Direct link to Search for answers in a corpus")
-----------------------------------------------------------------------------------------------------------------------------------------------------------

**Use case:** Query an existing corpus and get AI-generated answers with context.

In this example, you have a corpus with uploaded data from an Employee Handbook. You want to ask, _"How much PTO is offered to employees each year?"_

To issue the cURL command in the example, you input the following field values:

*   `x-api-key` = `YOUR_API_KEY`
*   `corpus_key` = `employee-handbook`
*   `query` = How much PTO is offered to employees each year?

#### Example cURL command[​](https://docs.vectara.com/docs/api-recipes#example-curl-command "Direct link to Example cURL command")

This example queries the corpus with the question about annual PTO.

1 curl -L -X POST 'https://api.vectara.io/v2/corpora/employee-handbook/query' \

2-H 'Content-Type: application/json' \

3-H 'Accept: application/json' \

4-H 'x-api-key: YOUR_API_KEY' \?

5-d '{

6 "query": "How much PTO is offered to employees each year?",

7 "stream_response": false,

8 "search": {

9 "limit": 20,?

10 "context_configuration": {

11 "sentences_before": 3,

12 "sentences_after": 3,

13 "start_tag": "<b>",

14 "end_tag": "</b>"

15 },

16 "metadata_filter": "part.lang = 'eng'",

17 "lexical_interpolation": 0.005,

18 },

19 "generation": [

20 {

21 "generation_preset_name": "mockingbird-2.0",?

22 "max_used_search_results": 20

23 }

24 ]

25}'

#### Example JSON response[​](https://docs.vectara.com/docs/api-recipes#example-json-response "Direct link to Example JSON response")

Let’s take a closer look at the first response:

1{

2 "summary": "Employee Handbook PTO is 20 days a year for all new employees. ?

3<b>Employees earn more vacation days per year of service up to 5 extra days.

4</b> Example: Once you begin your 5th year, you now have 25 vacation days.",

5 "summary_language": "eng",?

6 "search_results": [

7 {

8 "text": "Employee Handbook PTO is 20 days a year for all new employees.

9<b>Employees earn more vacation days per year of service up to 5 extra days.

10</b> Example: Once you begin your 5th year, you now have 25 vacation days.",

11 "score": 4.30505,

12 "part_metadata": {

13 "lang": "eng",

14 "section": "1",

15 "offset": "63",

16 "len": "73"

17 },

18 "document_metadata": {},

19 "document_id": "doc_123456789",

20 "request_corpora_index": 0

21 }

22 ]

23

24}

The example API call provided the following response:

_"Employee Handbook PTO is 20 days a year for all new employees. **Employees earn more vacation days per year of service up to 5 extra days.** Example: Once you begin your 5th year, you now have 25 vacation days."_

The result answers the question and returns additional details about the query, such as the language, section, and offset.

Let's take a look at some other API calls that you can make.

* * *

Add content to a corpus[​](https://docs.vectara.com/docs/api-recipes#add-content-to-a-corpus "Direct link to Add content to a corpus")
--------------------------------------------------------------------------------------------------------------------------------------

**Use case:** Upload files or index structured documents into an existing corpus.

You can add content to a corpus in two ways: upload files (PDF, Word, etc.) or index structured documents with JSON. Choose the method that fits your data format.

You need to input the following information:

*   `x-api-key`
*   `corpus_key`
*   File path (for file upload) or document content (for direct indexing)

#### Option 1: Upload a file[​](https://docs.vectara.com/docs/api-recipes#option-1-upload-a-file "Direct link to Option 1: Upload a file")

In this example, you have a local `doc.rtf` file that you want to upload the corpus with the `corpus_key` as `employee-handbook`:

1 curl -L -X POST 'https://api.vectara.io/v2/corpora/employee-handbook/upload_file' \

2-H 'Content-Type: multipart/form-data' \

3-H 'Accept: application/json' \

4-H 'x-api-key: YOUR_API_KEY' \?

5-F 'file=@"//Users/username/Documents/tmp/doc.rtf"'?

#### Example JSON response[​](https://docs.vectara.com/docs/api-recipes#example-json-response-1 "Direct link to Example JSON response")

The file uploads successfully and you get the following response:

1{

2"document": {

3 "id": "doc.rtf",

4 "title": "Sample Document",?

5 "sections": [{

6 "id": 1,

7 "text": "Simple test doc. Lorem ipsum dolor sit amet..."

8 }]?

9},

10"status": "indexed"

11}

#### Option 2: Index a document directly[​](https://docs.vectara.com/docs/api-recipes#option-2-index-a-document-directly "Direct link to Option 2: Index a document directly")

If you don't have a file to upload, you can create a document directly with text content:

1 curl -X POST 'https://api.vectara.io/v2/corpora/employee-handbook/documents' \

2-H 'Content-Type: application/json' \

3-H 'x-api-key: YOUR_API_KEY' \?

4-d '{

5"id": "pto-policy",?

6"title": "PTO Policy",

7"sections": [{

8 "text": "All new employees receive 20 days of PTO annually. Employees earn additional vacation days based on years of service, up to 5 extra days. After 5 years of service, employees have 25 vacation days total."?

9}]

10}'

* * *

Query with result limits[​](https://docs.vectara.com/docs/api-recipes#query-with-result-limits "Direct link to Query with result limits")
-----------------------------------------------------------------------------------------------------------------------------------------

**Use case:** Control how many search results are returned and processed.

In this example, you want to search for "technology" and limit the results to 50, then use those results for generating a summary.

#### Example cURL command[​](https://docs.vectara.com/docs/api-recipes#example-curl-command-1 "Direct link to Example cURL command")

1 curl -L -X POST 'https://api.vectara.io/v2/corpora/technology-corpus/query' \

2-H 'Content-Type: application/json' \

3-H 'Accept: application/json' \

4-H 'x-api-key: YOUR_API_KEY' \?

5-d '{

6 "query": "Technology",

7 "stream_response": false,

8 "search": {

9 "limit": 50,?

10 "metadata_filter": "part.lang = 'eng'",

11 "lexical_interpolation": 0.005,

12 "semantics": "default"

13 },

14 "generation": {

15 "generation_preset_name": "vectara-summary-ext-24-05-med-omni",?

16 "max_used_search_results": 50

17 }

18 }'

#### Example JSON response with 5 results[​](https://docs.vectara.com/docs/api-recipes#example-json-response-with-5-results "Direct link to Example JSON response with 5 results")

1{

2"summary": "The future of technology is AI. Technology is evolving rapidly, with?

3 generative AI technology being revolutionary. While technology has its pros and cons,

4 it plays a significant role in modern society.",

5"summary_language": "eng",?

6"search_results": [

7 {

8 "text": "The future of technology is AI.",

9 "score": 0.98,

10 "document_id": "doc_1",

11 "request_corpora_index": 0

12 },

13 {

14 "text": "Technology is evolving rapidly.",

15 "score": 0.95,

16 "document_id": "doc_2",

17 "request_corpora_index": 0

18 },

19 {

20 "text": "Generative AI technology is revolutionary.",

21 "score": 0.92,

22 "document_id": "doc_3",

23 "request_corpora_index": 0

24 },

25 {

26 "text": "Technology has its pros and cons.",

27 "score": 0.90,

28 "document_id": "doc_4",

29 "request_corpora_index": 0

30 },

* * *

List and delete corpora[​](https://docs.vectara.com/docs/api-recipes#list-and-delete-corpora "Direct link to List and delete corpora")
--------------------------------------------------------------------------------------------------------------------------------------

**Use case:** Manage your corpora by listing, filtering, and deleting them.

In this example, you'll list all corpora that contain "handbook" in the name, then delete a specific corpus.

1.   Execute the following curl command to list the corpora:

1 curl -L -X GET 'https://api.vectara.io/v2/corpora?limit=8&filter=handbook' \?

2 -H 'Content-Type: application/json' \

3 -H 'Accept: application/json' \

4 -H 'x-api-key: abc_12345defg67890hij09876'?

You get the following response:

1{

2"corpus": [

3 {?

4 "id": 6,

5 "key": "Employee handbook",

6 "description": "Employee guidelines from HR",

7 "enabled": true,

8 "queries_are_answers": false,

9 "documents_are_questions": false,

10 "encoder_id": "enc_0",

11 },

12{?

13 "id": 11,

14 "name": "Employee Handbook",

15 "description": "Pet Policy",

16 "enabled": true,

17 "queries_are_answers": false,

18 "documents_are_questions": false,

19 "encoder_id": "enc_0",

20},

21{

22 "id": 13,

23 "name": "2025 handbook",

24 "description": "",

25 "enabled": true,

26 "queries_are_answers": false,

27 "documents_are_questions": false,

28 "encoder_id": "enc_0",

29}

30],

1.   Execute the following curl command to delete a specific corpus with `corpus_key` = `2025-handbook`.

1 curl -L -X DELETE 'https://api.vectara.io/v2/corpora/2025-handbook' \?

2-H 'Content-Type: application/json' \

3-H 'Accept: application/json' \

4-H 'x-api-key: abc_12345defg67890hij09876'?

You get the following response:

1{

2"status": 204,?

3"message": "Corpus deleted successfully"

4}

1.   Execute the curl command from Step 1 again and the corpus you deleted no longer exists.
