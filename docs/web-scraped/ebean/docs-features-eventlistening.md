# Source: https://ebean.io/docs/features/eventlistening

Title: Event listening | Ebean

URL Source: https://ebean.io/docs/features/eventlistening

Markdown Content:
JPA annotations, @PostUpdate etc
--------------------------------

Ebean supports JPA annotations - `@PostLoad, @PostPersist, @PostRemove, @PostUpdate, @PrePersist, @PreRemove, @PreUpdate`

#### Example:

import jakarata.persistence.PostLoad;
import jakarata.persistence.PostPersist;
import jakarata.persistence.PostRemove;
import jakarata.persistence.PostUpdate;
import jakarata.persistence.PrePersist;
import jakarata.persistence.PreRemove;
import jakarata.persistence.PreUpdate;

...

@Entity
public class Customer {

  @Id
  Long id;

  String name;

  @Version
  Long version;

  @PrePersist
  public void prePersist1() {
  ...
  }

  @PostPersist
  public void postPersist1() {
  ...
  }

  @PreUpdate
  public void preUpdate1() {
  ...
  }

  @PostUpdate
  public void postUpdate1() {
  ...
  }

  @PreRemove
  public void preRemove1() {
  ...
  }

  @PostRemove
  public void postRemove1() {
  ...
  }

  @PostLoad
  public void postLoad1() {
  ...
  }

Using the JPA annotations has some limitations. For example, it doesn't tell us which properties actually changed in an update or give access to the underlying transaction.

When we hit these limitations, we can use `BeanPersistController`.

BeanPersistController
---------------------

To listen for events on entity, we can also use the BeanPersistController and this gives us access to the underlying transaction as well as the specific properties changed in an update etc.

BeanPersistController is used to enhance or override the default bean persistence mechanism.

Object extraBeanToSave = ...;
Transaction t = request.getTransaction();
Database database = request.database();
database.save(extraBeanToSave, t);

BeanPersistListener
-------------------

`BeanPersistListener` is different in two main ways from BeanPersistController postXXX methods.

BeanPersistListener only sees successfully committed events. BeanController pre and post methods occur before the commit or a rollback and as such these methods will see events that are later rolled back.

BeanPersistListener runs in a background thread and will not affect the response time of the actual persist where as BeanController methods will.

BeanQueryAdapter
----------------

Use a BeanQueryAdapter to modify queries prior their execution. Typically, we add expressions to a query, for example to enable query partitioning based on the user executing the query.
