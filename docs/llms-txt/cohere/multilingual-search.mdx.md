# Source: https://docs.cohere.com/page/multilingual-search.mdx

***

title: Multilingual Search with Cohere and Langchain
slug: /page/multilingual-search
description: >-
This page contains a basic tutorial on how to do search across different
languages with Cohere's LLM platform.
image:
type: fileId
value: 'https://files.buildwithfern.com/cohere.docs.buildwithfern.com/8ba30b46486ea7bfab24f3e8856d7411d1b745b26e9026abff3ee62af52ce268/assets/images/f1cc130-cohere_meta_image.jpg'
keywords: 'Cohere, ElasticSearch'
---------------------------------

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Multilingual_Search_with_Cohere_and_Langchain.ipynb" />

***Read the accompanying [blog post here](https://cohere.com/blog/search-cohere-langchain/).***

This notebook contains two examples for performing multilingual search using Cohere and Langchain. Langchain is a library that assists the development of applications built on top of large language models (LLMs), such as Cohere's models.

In short, Cohere makes it easy for developers to leverage LLMs and Langchain makes it easy to build applications with these models.

We'll go through the following examples:

* **Example 1 - Basic Multilingual Search**

  This is a simple example of multilingual search over a list of documents.

  The steps in summary:

  * Import a list of documents
  * Embed the documents and store them in an index
  * Enter a query
  * Return the document most similar to the query

* **Example 2 - Search-Based Question Answering**

  This example shows a more involved example where search is combined with text generation to answer questions about long-form documents.

  The steps in summary:

  * Add an article and chunk it into smaller passages
  * Embed the passages and store them in an index
  * Enter a question
  * Answer the question based on the most relevant documents

```python PYTHON
from langchain.embeddings.cohere import CohereEmbeddings
from langchain.llms import Cohere
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import RetrievalQA
from langchain.vectorstores import Qdrant
from langchain.document_loaders import TextLoader
import textwrap as tr
import random
import dotenv
import os

dotenv.load_dotenv(".env") # Upload an '.env' file containing an environment variable named 'COHERE_API_KEY' using your Cohere API Key
```

```txt title="Output"
True
```

### Import a list of documents

```python PYTHON
import tensorflow_datasets as tfds
dataset = tfds.load('trec', split='train')
texts = [item['text'].decode('utf-8') for item in tfds.as_numpy(dataset)]
print(f"Number of documents: {len(texts)}")
```

```txt title="Output"
Downloading and preparing dataset 350.79 KiB (download: 350.79 KiB, generated: 636.90 KiB, total: 987.69 KiB) to /root/tensorflow_datasets/trec/1.0.0...



Dl Completed...: 0 url [00:00, ? url/s]



Dl Size...: 0 MiB [00:00, ? MiB/s]



Extraction completed...: 0 file [00:00, ? file/s]



Generating splits...:   0%|          | 0/2 [00:00<?, ? splits/s]



Generating train examples...:   0%|          | 0/5452 [00:00<?, ? examples/s]



Shuffling /root/tensorflow_datasets/trec/1.0.0.incompleteWOR5EP/trec-train.tfrecord*...:   0%|          | 0/54…



Generating test examples...:   0%|          | 0/500 [00:00<?, ? examples/s]



Shuffling /root/tensorflow_datasets/trec/1.0.0.incompleteWOR5EP/trec-test.tfrecord*...:   0%|          | 0/500…


Dataset trec downloaded and prepared to /root/tensorflow_datasets/trec/1.0.0. Subsequent calls will reuse this data.
Number of documents: 5452
```

```python PYTHON
random.seed(11)
for item in random.sample(texts, 5):
  print(item)
```

```txt title="Output"
What is the starting salary for beginning lawyers ?
Where did Bill Gates go to college ?
What task does the Bouvier breed of dog perform ?
What are the top boy names in the U.S. ?
What is a female rabbit called ?
```

### Embed the documents and store them in an index

```python PYTHON
embeddings = CohereEmbeddings(model = "multilingual-22-12")

db = Qdrant.from_texts(texts, embeddings, location=":memory:", collection_name="my_documents", distance_func="Dot")
```

### Enter a query

```python PYTHON
queries = ["How to get in touch with Bill Gates",
           "Comment entrer en contact avec Bill Gates",
           "Cara menghubungi Bill Gates"]

queries_lang = ["English", "French", "Indonesian"]
```

### Return the document most similar to the query

```python PYTHON
answers = []
for query in queries:
  docs = db.similarity_search(query)
  answers.append(docs[0].page_content)
```

```python PYTHON
for idx,query in enumerate(queries):
  print(f"Query language: {queries_lang[idx]}")
  print(f"Query: {query}")
  print(f"Most similar existing question: {answers[idx]}")
  print("-"*20,"\n")
```

```txt title="Output"
Query language: English
Query: How to get in touch with Bill Gates
Most similar existing question: What is Bill Gates of Microsoft E-mail address ?
--------------------

Query language: French
Query: Comment entrer en contact avec Bill Gates
Most similar existing question: What is Bill Gates of Microsoft E-mail address ?
--------------------

Query language: Indonesian
Query: Cara menghubungi Bill Gates
Most similar existing question: What is Bill Gates of Microsoft E-mail address ?
--------------------
```

## Add an article and chunk it into smaller passages

```python PYTHON

!wget 'https://docs.google.com/uc?export=download&amp;id=1f1INWOfJrHTFmbyF_0be5b4u_moz3a4F' -O steve-jobs-commencement.txt
```

```txt title="Output"
--2023-06-08 06:11:19--  https://docs.google.com/uc?export=download&amp;id=1f1INWOfJrHTFmbyF_0be5b4u_moz3a4F
Resolving docs.google.com (docs.google.com)... 74.125.200.101, 74.125.200.138, 74.125.200.102, ...
Connecting to docs.google.com (docs.google.com)|74.125.200.101|:443... connected.
HTTP request sent, awaiting response... 303 See Other
Location: https://doc-0g-84-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/84t4moii9dmg08hmrh6rfpp8ecrjh6jq/1686204675000/12721472133292131824/*/1f1INWOfJrHTFmbyF_0be5b4u_moz3a4F?e=download&amp;uuid=a26288c7-ad0c-4707-ae0b-72cb94c224dc [following]
Warning: wildcards not supported in HTTP.
--2023-06-08 06:11:19--  https://doc-0g-84-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/84t4moii9dmg08hmrh6rfpp8ecrjh6jq/1686204675000/12721472133292131824/*/1f1INWOfJrHTFmbyF_0be5b4u_moz3a4F?e=download&amp;uuid=a26288c7-ad0c-4707-ae0b-72cb94c224dc
Resolving doc-0g-84-docs.googleusercontent.com (doc-0g-84-docs.googleusercontent.com)... 74.125.130.132, 2404:6800:4003:c01::84
Connecting to doc-0g-84-docs.googleusercontent.com (doc-0g-84-docs.googleusercontent.com)|74.125.130.132|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 11993 (12K) [text/plain]
Saving to: ‘steve-jobs-commencement.txt’

steve-jobs-commence 100%[===================>]  11.71K  --.-KB/s    in 0s

2023-06-08 06:11:20 (115 MB/s) - ‘steve-jobs-commencement.txt’ saved [11993/11993]
```

```python PYTHON
loader = TextLoader("steve-jobs-commencement.txt")
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
texts = text_splitter.split_documents(documents)
```

## Embed the passages and store them in an index

```python PYTHON
embeddings = CohereEmbeddings(model = "multilingual-22-12")
db = Qdrant.from_documents(texts, embeddings, location=":memory:", collection_name="my_documents", distance_func="Dot")
```

## Enter a question

```python PYTHON
questions = [
           "What did the author liken The Whole Earth Catalog to?",
           "What was Reed College great at?",
           "What was the author diagnosed with?",
           "What is the key lesson from this article?",
           "What did the article say about Michael Jackson?",
           ]
```

## Answer the question based on the most relevant documents

```python PYTHON

prompt_template = """Text: {context}

Question: {question}

Answer the question based on the text provided. If the text doesn't contain the answer, reply that the answer is not available."""

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)
```

```python PYTHON
chain_type_kwargs = {"prompt": PROMPT}

qa = RetrievalQA.from_chain_type(llm=Cohere(model="command", temperature=0),
                                 chain_type="stuff",
                                 retriever=db.as_retriever(),
                                 chain_type_kwargs=chain_type_kwargs,
                                 return_source_documents=True)

for question in questions:
  answer = qa({"query": question})
  result = answer["result"].replace("\n","").replace("Answer:","")
  sources = answer['source_documents']
  print("-"*150,"\n")
  print(f"Question: {question}")
  print(f"Answer: {result}")

  ### COMMENT OUT THE 4 LINES BELOW TO HIDE THE SOURCES
  print(f"\nSources:")
  for idx, source in enumerate(sources):
    source_wrapped = tr.fill(str(source.page_content), width=150)
    print(f"{idx+1}: {source_wrapped}")
```

```txt title="Output"
------------------------------------------------------------------------------------------------------------------------------------------------------

Question: What did the author liken The Whole Earth Catalog to?
Answer: It was sort of like Google in paperback form, 35 years before Google came along

Sources:
1: When I was young, there was an amazing publication called The Whole Earth Catalog, which was one of the bibles of my generation. It was created by a
fellow named Stewart Brand not far from here in Menlo Park, and he brought it to life with his poetic touch. This was in the late 1960s, before
personal computers and desktop publishing, so it was all made with typewriters, scissors and Polaroid cameras. It was sort of like Google in paperback
form, 35 years before Google came along: It was
2: Stewart and his team put out several issues of The Whole Earth Catalog, and then when it had run its course, they put out a final issue. It was the
mid-1970s, and I was your age. On the back cover of their final issue was a photograph of an early morning country road, the kind you might find
yourself hitchhiking on if you were so adventurous. Beneath it were the words: “Stay Hungry. Stay Foolish.” It was their farewell message as they
signed off. Stay Hungry. Stay Foolish. And I have always
3: idealistic, and overflowing with neat tools and great notions.
4: beautiful, historical, artistically subtle in a way that science can’t capture, and I found it fascinating.
------------------------------------------------------------------------------------------------------------------------------------------------------

Question: What was Reed College great at?
Answer: Reed College was great at calligraphy instruction.

Sources:
1: Reed College at that time offered perhaps the best calligraphy instruction in the country. Throughout the campus every poster, every label on every
drawer, was beautifully hand calligraphed. Because I had dropped out and didn’t have to take the normal classes, I decided to take a calligraphy class
to learn how to do this. I learned about serif and sans serif typefaces, about varying the amount of space between different letter combinations,
about what makes great typography great. It was
2: I dropped out of Reed College after the first 6 months, but then stayed around as a drop-in for another 18 months or so before I really quit. So why
did I drop out?
3: never dropped out, I would have never dropped in on this calligraphy class, and personal computers might not have the wonderful typography that they
do. Of course it was impossible to connect the dots looking forward when I was in college. But it was very, very clear looking backward 10 years
later.
4: OK. It was pretty scary at the time, but looking back it was one of the best decisions I ever made. The minute I dropped out I could stop taking the
required classes that didn’t interest me, and begin dropping in on the ones that looked interesting.
------------------------------------------------------------------------------------------------------------------------------------------------------

Question: What was the author diagnosed with?
Answer: The author was diagnosed with cancer.

Sources:
1: I lived with that diagnosis all day. Later that evening I had a biopsy, where they stuck an endoscope down my throat, through my stomach and into my
intestines, put a needle into my pancreas and got a few cells from the tumor. I was sedated, but my wife, who was there, told me that when they viewed
the cells under a microscope the doctors started crying because it turned out to be a very rare form of pancreatic cancer that is curable with
surgery. I had the surgery and I’m fine now.
2: About a year ago I was diagnosed with cancer. I had a scan at 7:30 in the morning, and it clearly showed a tumor on my pancreas. I didn’t even know
what a pancreas was. The doctors told me this was almost certainly a type of cancer that is incurable, and that I should expect to live no longer than
three to six months. My doctor advised me to go home and get my affairs in order, which is doctor’s code for prepare to die. It means to try to tell
your kids everything you thought you’d have the
3: Stewart and his team put out several issues of The Whole Earth Catalog, and then when it had run its course, they put out a final issue. It was the
mid-1970s, and I was your age. On the back cover of their final issue was a photograph of an early morning country road, the kind you might find
yourself hitchhiking on if you were so adventurous. Beneath it were the words: “Stay Hungry. Stay Foolish.” It was their farewell message as they
signed off. Stay Hungry. Stay Foolish. And I have always
4: beautiful, historical, artistically subtle in a way that science can’t capture, and I found it fascinating.
------------------------------------------------------------------------------------------------------------------------------------------------------

Question: What is the key lesson from this article?
Answer: The key lesson from this article is that you have to trust that the dots will somehow connect in your future. You have to trust in something -- your gut, destiny, life, karma, whatever. This approach has never let me down, and it has made all the difference in my life.

Sources:
1: Again, you can’t connect the dots looking forward; you can only connect them looking backward. So you have to trust that the dots will somehow connect
in your future. You have to trust in something — your gut, destiny, life, karma, whatever. This approach has never let me down, and it has made all
the difference in my life.  My second story is about love and loss.
2: Remembering that I’ll be dead soon is the most important tool I’ve ever encountered to help me make the big choices in life. Because almost everything
— all external expectations, all pride, all fear of embarrassment or failure — these things just fall away in the face of death, leaving only what is
truly important. Remembering that you are going to die is the best way I know to avoid the trap of thinking you have something to lose. You are
already naked. There is no reason not to follow your
3: Your time is limited, so don’t waste it living someone else’s life. Don’t be trapped by dogma — which is living with the results of other people’s
thinking. Don’t let the noise of others’ opinions drown out your own inner voice. And most important, have the courage to follow your heart and
intuition. They somehow already know what you truly want to become. Everything else is secondary.
4: I really didn’t know what to do for a few months. I felt that I had let the previous generation of entrepreneurs down — that I had dropped the baton
as it was being passed to me. I met with David Packard and Bob Noyce and tried to apologize for screwing up so badly. I was a very public failure, and
I even thought about running away from the valley. But something slowly began to dawn on me — I still loved what I did. The turn of events at Apple
had not changed that one bit. I had been rejected,
------------------------------------------------------------------------------------------------------------------------------------------------------

Question: What did the article say about Michael Jackson?
Answer: The text did not provide information about Michael Jackson.

Sources:
1: baby boy; do you want him?” They said: “Of course.” My biological mother later found out that my mother had never graduated from college and that my
father had never graduated from high school. She refused to sign the final adoption papers. She only relented a few months later when my parents
promised that I would someday go to college.
2: beautiful, historical, artistically subtle in a way that science can’t capture, and I found it fascinating.
3: I really didn’t know what to do for a few months. I felt that I had let the previous generation of entrepreneurs down — that I had dropped the baton
as it was being passed to me. I met with David Packard and Bob Noyce and tried to apologize for screwing up so badly. I was a very public failure, and
I even thought about running away from the valley. But something slowly began to dawn on me — I still loved what I did. The turn of events at Apple
had not changed that one bit. I had been rejected,
4: This was the closest I’ve been to facing death, and I hope it’s the closest I get for a few more decades. Having lived through it, I can now say this
to you with a bit more certainty than when death was a useful but purely intellectual concept:
```

## Questions in French

```python PYTHON
questions_fr = [
           "À quoi se compare The Whole Earth Catalog ?",
           "Dans quoi Reed College était-il excellent ?",
           "De quoi l'auteur a-t-il été diagnostiqué ?",
           "Quelle est la leçon clé de cet article ?",
           "Que disait l'article sur Michael Jackson ?",
           ]
```

```python PYTHON
```

```python PYTHON

chain_type_kwargs = {"prompt": PROMPT}

qa = RetrievalQA.from_chain_type(llm=Cohere(model="command", temperature=0),
                                 chain_type="stuff",
                                 retriever=db.as_retriever(),
                                 chain_type_kwargs=chain_type_kwargs,
                                 return_source_documents=True)

for question in questions_fr:
  answer = qa({"query": question})
  result = answer["result"].replace("\n","").replace("Answer:","")
  sources = answer['source_documents']
  print("-"*20,"\n")
  print(f"Question: {question}")
  print(f"Answer: {result}")
```

```txt title="Output"
--------------------

Question: À quoi se compare The Whole Earth Catalog ?
Answer: The Whole Earth Catalog was like Google in paperback form, 35 years before Google came along.
--------------------

Question: Dans quoi Reed College était-il excellent ?
Answer: Reed College offered the best calligraphy instruction in the country.
--------------------

Question: De quoi l'auteur a-t-il été diagnostiqué ?
Answer: The author was diagnosed with a very rare form of pancreatic cancer that is curable with surgery.
--------------------

Question: Quelle est la leçon clé de cet article ?
Answer: The key lesson of this article is that remembering that you will die soon is the most important tool to help one make the big choices in life.
--------------------

Question: Que disait l'article sur Michael Jackson ?
Answer: The text does not contain the answer to the question.
```
