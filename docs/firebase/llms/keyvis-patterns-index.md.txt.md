# Source: https://firebase.google.com/docs/firestore/key-visualizer/keyvis-patterns-index.md.txt

This page shows examples of patterns that you might see in a Key Visualizer
heatmap. These patterns can help you troubleshoot specific performance
issues.

## Evenly distributed usage

![Heatmap showing evenly distributed reads and writes](https://firebase.google.com/static/docs/firestore/images/keyvis-patterns-ideal.png)

If a heatmap shows a fine-grained mix of dark and bright colors, then write/delete operations for
index keys are evenly distributed throughout the database. This heatmap likely
represents an effective usage pattern for Cloud Firestore.