# Source: https://firebase.google.com/docs/firestore/solutions/search.md.txt

<br />

Most apps allow users to search app content. For example, you may want to search for posts containing a certain word or notes you've written about a specific topic.

Cloud Firestoredoesn't support native indexing or search for text fields in documents. Additionally, downloading an entire collection to search for fields client-side isn't practical.

To enable full text search of yourCloud Firestoredata, use a dedicated third-party search service. These services provide advanced indexing and search capabilities far beyond what any simple database query can offer.

Before continuing, research then choose one of the search providers below:

- [Elastic](https://www.elastic.co/app-search/)
- [Algolia](https://www.algolia.com/)
- [Typesense](https://typesense.org/)

## Solution: External search service

ElasticAlgoliaTypesense