# Extract the code snippets from the structures to a separate list
code_snippets = [\
    structure["context"]["snippet"] for structure in structures\
]

points = [\
    models.PointStruct(\
        id=uuid.uuid4().hex,\
        vector={\
            "text": models.Document(\
                text=text, model="sentence-transformers/all-MiniLM-L6-v2"\
            ),\
            "code": models.Document(\
                text=code, model="jinaai/jina-embeddings-v2-base-code"\
            ),\
        },\
        payload=structure,\
    )\
    for text, code, structure in zip(text_representations, code_snippets, structures)\
]