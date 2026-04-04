# clf = LogisticRegression(random_state=0, C=1.0, max_iter=1000, solver='sag').fit(train_x, train_y)

print(f"Precision: {100*np.mean(clf.predict(test_x) == test_y.to_list()):.2f}%")
```

Output
```
Precision: 98.75%
```

After we trained the classifier with our embeddings data, we can try classify other text:

```python