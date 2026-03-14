# Source: https://ebean.io/docs/features/softdelete

Title: SoftDelete | Ebean

URL Source: https://ebean.io/docs/features/softdelete

Markdown Content:
Add a boolean property to your entity beans to indicate the deleted state. This property can be on the entity bean or on a MappedSuperclass as per the example below:

This property must be a boolean type with a true value meaning that the row/bean has been logically deleted.

@MappedSuperclass
public class BaseSoftDelete {

  @Id
  Long id;

  @Version
  Long version;

  @SoftDelete
  boolean deleted;

Delete
------

A delete of an entity bean that has SoftDelete becomes a SQL update.

// delete becomes an update if the bean has soft delete property
database.delete(bean);

-- soft delete ... sets deleted = true
update mybean set version=?, deleted=? where id=? and version=?; --bind(2,true,1,1,)

Delete Permanent
----------------

Delete permanent is used to perform a SQL delete (hard delete).

// delete becomes an update if the bean has soft delete property
database.deletePermanent(bean);

-- delete permanent
delete from mybean where id=? and version=?; --bind(1,2,)

Cascading behavior
------------------

A soft delete will cascade along the same relationships as a hard delete as long as the beans support soft delete. If the 'target' bean does not have a `@SoftDelete` property (and hence does not support soft delete) then the soft delete will not cascade to that relationship.

#### ManyToMany

Soft delete will not cascade to the intersection table of a `@ManyToMany`.

#### Draftable

Soft delete will not propagate to the associated "live" row of a @Draftable entity bean.

Query (normal)
--------------

A normal query automatically includes a predicate to filter out soft deleted rows. A predicate is added for each table (SQL FROM or JOIN) that has a soft delete column. This is done for any subsequent lazy loading queries as necessary.

> and t0.deleted=false and t1.deleted=false ... additional predicates

select t0.id c0, t0.name ...
from ebasic_soft_delete t0
left outer join ebasic_sdchild t1 on t1.owner_id = t0.id
where t0.id = ?
  -- Additional predicates for soft delete
  and t0.deleted=false and t1.deleted=false
order by t0.id; --bind(1)

Query - includeSoftDeletes
--------------------------

A query can have `includeSoftDeletes()` set and in this case the soft delete predicates are not added to the query and this means all rows including soft deleted rows are included in the result.

> Query.includeSoftDeletes()

// find a bean that could be soft deleted
List<MyBean> beans =
  database.find(MyBean.class)
  .includeSoftDeletes()
  .where().icontains("name", "rob")
  .findList();

// find a bean that could be soft deleted
MyBean bean =
  database.find(MyBean.class)
    .includeSoftDeletes()
    .setId(idValue)
    .findOne();

Notifications
-------------

For BeanPersistController, BeanPersistListener, L2 Cache and Cluster notifications a soft delete is treated the same as a hard delete and the same event notifications occur.

Change Log
----------

For ChangeLog soft deletes are treated as updates as this reflects the actual change that occured.
