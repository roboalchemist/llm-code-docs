# Source: https://mikro-orm.io/docs/recipes.md

## [📄️<!-- --> <!-- -->Using Entity Constructors](https://mikro-orm.io/docs/entity-constructors.md)

[Internally, MikroORM never calls entity constructor on managed entities (those loaded via EntityManager), so you are free to use it as you wish. The constructor will be called only when you instantiate the class yourself via new operator (or when using em.create() to create new entity instance), so it is a handy place to require your data when creating new entity.](https://mikro-orm.io/docs/entity-constructors.md)
