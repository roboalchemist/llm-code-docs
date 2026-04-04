# Beanie ODM Documentation Index

**Beanie** is an asynchronous Python Object-Document Mapper (ODM) for MongoDB. It provides a Pydantic-based interface for building modern async MongoDB applications.

## Documentation Contents

This documentation archive contains the following sections:

### Getting Started
- **04-getting-started.md** - Installation and initialization guide
- **05-index.md** - Overview and introduction to Beanie

### Tutorials
- **09-tutorial_finding-documents.md** - Querying and finding documents
- **16-tutorial_indexes.md** - Creating and managing indexes
- **18-tutorial_migrations.md** - Data schema migrations
- **20-tutorial_relations.md** - Document relationships and references

### Changelog
- **changelog.md** - Complete version history and release notes

## Key Features

- **Asynchronous** - Built on PyMongo with Motor for full async/await support
- **Pydantic Integration** - Use Pydantic models for data validation and serialization
- **MongoDB Native** - Full MongoDB query syntax support with pythonic API
- **Type Hints** - Complete type annotations for IDE support and type checking
- **Relations** - Define relationships between documents
- **Migrations** - Out-of-the-box schema migration support
- **Indexes** - Declarative index definitions

## Quick Start

```python
import asyncio
from typing import Optional
from pymongo import AsyncMongoClient
from pydantic import BaseModel
from beanie import Document, Indexed, init_beanie

class Category(BaseModel):
    name: str
    description: str

class Product(Document):
    name: str
    description: Optional[str] = None
    price: Indexed(float)
    category: Category

async def main():
    client = AsyncMongoClient("mongodb://localhost:27017")
    await init_beanie(
        database=client.db_name,
        document_models=[Product]
    )
    
    # Create
    product = Product(
        name="Widget",
        price=9.99,
        category=Category(name="Tools", description="Hand tools")
    )
    await product.insert()
    
    # Query
    found = await Product.find_one(Product.price < 10)
    
    # Update
    await found.set({Product.name: "Premium Widget"})
    
    # Delete
    await found.delete()

asyncio.run(main())
```

## Source

This documentation was extracted from the official Beanie documentation at https://beanie-odm.dev/

For the latest updates and additional resources, visit:
- Documentation: https://beanie-odm.dev/
- GitHub: https://github.com/BeanieODM/beanie
- Discord: https://discord.gg/AwwTrbCASP
- PyPI: https://pypi.org/project/beanie/

---

Last updated: 2026-04-02
