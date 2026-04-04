# pgvector - Open-Source Vector Similarity Search for PostgreSQL

Open-source vector similarity search for Postgres. Store your vectors with the rest of your data.

## Overview

pgvector is a PostgreSQL extension that adds support for storing and searching vector embeddings. It enables you to:

- Perform exact and approximate nearest neighbor search
- Work with single-precision, half-precision, binary, and sparse vectors
- Use multiple distance metrics: L2 distance, inner product, cosine distance, L1 distance, Hamming distance, and Jaccard distance
- Use any language with a Postgres client

Plus you get ACID compliance, point-in-time recovery, JOINs, and all of the great features of PostgreSQL.

**Source Documentation:** https://github.com/pgvector/pgvector

---

## Installation

### Linux and Mac

Compile and install the extension (supports Postgres 13+):

```sh
cd /tmp
git clone --branch v0.8.2 https://github.com/pgvector/pgvector.git
cd pgvector
make
make install # may need sudo
```

See the installation notes if you run into issues.

You can also install it with:

- Docker
- Homebrew
- PGXN
- APT
- Yum
- pkg
- APK
- conda-forge

pgvector comes preinstalled with Postgres.app and many hosted providers. There are also instructions for GitHub Actions.

### Windows

Ensure C++ support in Visual Studio is installed and run `x64 Native Tools Command Prompt for VS [version]` as administrator. Then use `nmake` to build:

```cmd
set "PGROOT=C:\Program Files\PostgreSQL\18"
cd %TEMP%
git clone --branch v0.8.2 https://github.com/pgvector/pgvector.git
cd pgvector
nmake /F Makefile.win
nmake /F Makefile.win install
```

You can also install it with Docker or conda-forge.

### Docker

```docker
FROM pgvector/pgvector:0.8.2-postgres18
```

### Homebrew

```bash
brew install pgvector
```

### PGXN

```bash
pgxn install vector
```

### APT

```bash
apt-get install postgresql-18-pgvector
```

### Yum

```bash
yum install pgvector_18-devel
```

### pkg

```bash
pkg install pgvector
```

### APK

```bash
apk add pgvector-postgresql
```

### conda-forge

```bash
conda install -c conda-forge pgvector
```

### Postgres.app

pgvector comes preinstalled with Postgres.app.

### Hosted Providers

pgvector is available on:

- Amazon RDS
- Azure Database for PostgreSQL
- Google Cloud SQL
- Heroku
- Supabase
- And many others

---

## Quick Start

### Enable the Extension

Enable the extension (do this once in each database where you want to use it):

```sql
CREATE EXTENSION vector;
```

### Create a Vector Column

Create a vector column with 3 dimensions:

```sql
CREATE TABLE items (id bigserial PRIMARY KEY, embedding vector(3));
```

### Insert Vectors

```sql
INSERT INTO items (embedding) VALUES ('[1,2,3]'), ('[4,5,6]');
```

### Query for Nearest Neighbors

Get the nearest neighbors by L2 distance:

```sql
SELECT * FROM items ORDER BY embedding <-> '[3,1,2]' LIMIT 5;
```

Also supports:

- Inner product: `<#>`
- Cosine distance: `<=>`
- L1 distance: `<+>`

Note: `<#>` returns the negative inner product since Postgres only supports `ASC` order index scans on operators.

---

## Storage and Management

### Creating Tables

Create a new table with a vector column:

```sql
CREATE TABLE items (id bigserial PRIMARY KEY, embedding vector(3));
```

Or add a vector column to an existing table:

```sql
ALTER TABLE items ADD COLUMN embedding vector(3);
```

You can also use half-precision, binary, and sparse vectors.

### Inserting Data

Basic insert:

```sql
INSERT INTO items (embedding) VALUES ('[1,2,3]'), ('[4,5,6]');
```

Load vectors in bulk using `COPY`:

```sql
COPY items (embedding) FROM STDIN WITH (FORMAT BINARY);
```

### Upserting

```sql
INSERT INTO items (id, embedding) VALUES (1, '[1,2,3]'), (2, '[4,5,6]')
    ON CONFLICT (id) DO UPDATE SET embedding = EXCLUDED.embedding;
```

### Updating

```sql
UPDATE items SET embedding = '[1,2,3]' WHERE id = 1;
```

### Deleting

```sql
DELETE FROM items WHERE id = 1;
```

---

## Querying

### Nearest Neighbors

Get the nearest neighbors to a vector:

```sql
SELECT * FROM items ORDER BY embedding <-> '[3,1,2]' LIMIT 5;
```

Supported distance operators:

- `<->` - L2 distance
- `<#>` - (negative) inner product
- `<=>` - cosine distance
- `<+>` - L1 distance
- `<~>` - Hamming distance (binary vectors)
- `<%>` - Jaccard distance (binary vectors)

### Get Nearest Neighbors to a Row

```sql
SELECT * FROM items WHERE id != 1 ORDER BY embedding <-> (SELECT embedding FROM items WHERE id = 1) LIMIT 5;
```

### Range Queries

Get rows within a certain distance:

```sql
SELECT * FROM items WHERE embedding <-> '[3,1,2]' < 5;
```

Note: Combine with `ORDER BY` and `LIMIT` to use an index.

### Distance Calculations

Get the distance:

```sql
SELECT embedding <-> '[3,1,2]' AS distance FROM items;
```

For inner product, multiply by -1 (since `<#>` returns the negative inner product):

```sql
SELECT (embedding <#> '[3,1,2]') * -1 AS inner_product FROM items;
```

For cosine similarity, use 1 - cosine distance:

```sql
SELECT 1 - (embedding <=> '[3,1,2]') AS cosine_similarity FROM items;
```

### Aggregates

Average vectors:

```sql
SELECT AVG(embedding) FROM items;
```

Average groups of vectors:

```sql
SELECT category_id, AVG(embedding) FROM items GROUP BY category_id;
```

---

## Indexing

By default, pgvector performs exact nearest neighbor search, which provides perfect recall.

You can add an index to use approximate nearest neighbor search, which trades some recall for speed. Unlike typical indexes, you will see different results for queries after adding an approximate index.

### Index Types

pgvector supports two index types:

1. **HNSW** - Hierarchical Navigable Small World (better for most use cases)
2. **IVFFlat** - Inverted File (legacy, now replaced by HNSW)

### Creating an Index

```sql
CREATE INDEX ON items USING hnsw (embedding vector_l2_ops);
```

Or for cosine distance:

```sql
CREATE INDEX ON items USING hnsw (embedding vector_cosine_ops);
```

### IVFFlat Index

```sql
CREATE INDEX ON items USING ivfflat (embedding vector_l2_ops) WITH (lists = 100);
```

### Index Options

For HNSW:

- `m` (default: 16) - Number of neighbors per node
- `ef_construction` (default: 64) - Size of dynamic candidate list

For IVFFlat:

- `lists` - Number of quantization cells

### Querying with Indexes

Indexes are used automatically. For better results:

1. Use LIMIT to constrain results
2. Combine with WHERE clauses when possible
3. Use the right distance operator

### Approximate vs Exact Search

With an HNSW index, you can use the `hnsw.ef_search` parameter to control accuracy:

```sql
SET hnsw.ef_search = 100;
SELECT * FROM items ORDER BY embedding <-> '[3,1,2]' LIMIT 5;
```

Higher values are more accurate but slower.

---

## Vector Types

### vector

Fixed-size float32 vectors (most common):

```sql
CREATE TABLE items (embedding vector(1536));
```

### halfvec

16-bit float vectors (lower precision, less memory):

```sql
CREATE TABLE items (embedding halfvec(1536));
```

### sparsevec

Sparse vectors (for high-dimensional sparse data):

```sql
CREATE TABLE items (embedding sparsevec(1000));
```

### bit

Binary vectors for Hamming distance:

```sql
CREATE TABLE items (embedding bit(128));
```

---

## Functions

### Distance Functions

- `l2_distance(vector, vector)` - L2 (Euclidean) distance
- `inner_product(vector, vector)` - Inner product
- `cosine_distance(vector, vector)` - Cosine distance
- `l1_distance(vector, vector)` - L1 (Manhattan) distance
- `hamming_distance(bit, bit)` - Hamming distance
- `jaccard_distance(bit, bit)` - Jaccard distance

### Utility Functions

- `l2_normalize(vector)` - Normalize vector to unit length
- `binary_quantize(vector)` - Convert to binary vector
- `subvector(vector, int, int)` - Extract subvector

---

## Performance Tips

1. **Use appropriate vector dimensions** - Larger dimensions require more memory and computation
2. **Denormalize when needed** - Store embeddings in the same table as other data for better performance
3. **Use batch operations** - COPY is faster than individual INSERTs
4. **Consider indexing strategy**:
   - Use HNSW for most cases
   - Adjust `m` and `ef_construction` based on your needs
   - Test different values for your workload
5. **Monitor index size** - Indexes can be large; consider trade-offs
6. **Use appropriate precision** - halfvec uses less memory than vector

---

## Monitoring and Maintenance

### Index Statistics

```sql
SELECT * FROM pg_stat_user_indexes WHERE relname = 'items';
```

### Vacuuming

Regular VACUUM helps maintain index performance:

```sql
VACUUM ANALYZE items;
```

### Index Size

```sql
SELECT pg_size_pretty(pg_relation_size('items_embedding_idx')) AS index_size;
```

---

## Language Support

pgvector works with any language that has a PostgreSQL client library:

- Python (psycopg2, asyncpg)
- JavaScript/Node.js (node-postgres)
- Go (pq, pgx)
- Ruby (pg)
- Java (pgjdbc)
- PHP (PDO)
- And many others

---

## Changelog Summary

### v0.8.2 (2026-02-25)

- Fixed buffer overflow with parallel HNSW index build
- Improved `install` target on Windows
- Fixed `Index Searches` in `EXPLAIN` output for Postgres 18

### v0.8.1 (2025-09-04)

- Added support for Postgres 18 rc1
- Improved performance of `binary_quantize` function

### v0.8.0 (2024-10-30)

- Added support for iterative index scans
- Added casts for arrays to `sparsevec`
- Improved cost estimation for better index selection when filtering
- Improved performance of HNSW index scans, inserts, and on-disk index builds
- Dropped support for Postgres 12

### v0.7.0 (2024-04-29)

- Added `halfvec` type
- Added `sparsevec` type
- Added support for indexing `bit` type
- Added support for indexing L1 distance with HNSW
- Added `binary_quantize`, `hamming_distance`, `jaccard_distance`, and `l2_normalize` functions
- Added subvector function
- Added concatenate operator for vectors
- Added CPU dispatching for distance functions on Linux x86-64

---

## Resources

- **GitHub**: https://github.com/pgvector/pgvector
- **Website**: https://pgvector.dev/
- **GitHub Issues**: https://github.com/pgvector/pgvector/issues
- **GitHub Discussions**: https://github.com/pgvector/pgvector/discussions
