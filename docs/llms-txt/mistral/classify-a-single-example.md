# Classify a single example
text = "I've been experiencing frequent headaches and vision problems."
clf.predict([get_text_embedding([text])])
```

Output
```
'Migraine'
```

### Comparison with fastText
Additionally, let's take a look at the performance using fastText embeddings in this classification task. It appears that the classification model achieves better performance with Mistral AI Embeddings model as compared to using fastText embeddings.

```python