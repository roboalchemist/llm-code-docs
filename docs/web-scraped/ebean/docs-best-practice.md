# Source: https://ebean.io/docs/best-practice

Title: Best practice | Docs | Ebean

URL Source: https://ebean.io/docs/best-practice

Markdown Content:
Identity - equals/hashCode
--------------------------

Do not implement `equals()` and `hashCode()` on `@Entity` beans. Instead, leave this to Ebean enhancement.

Ebean will automatically enhance entity beans with an optimal implementation of `equals()` and `hashCode()`. Ebean does not enhance `toString()`.

toString() - avoid getters
--------------------------

Avoid using getter methods in `toString()`. We want to avoid invoking any accidental lazy loading when using a debugger. Using the debugger and inspecting entity beans will implicitly call toString() methods on entity beans. If the toString() implementation uses getter methods, this may cause different behavior when debugging.

Kotlin data classes
-------------------

Do not use Kotlin data classes for `@Entity` beans as the equals/hashCode implementation is not desirable. Instead use normal Kotlin classes for entity beans.

Do use Kotlin data classes for `@EmbeddedId` beans.

Prefer List over Set
--------------------

For `@OneToMany` and `@ManyToMany` collections prefer the use of List over Set. The use of Set will implicitly calls `equals()` and `hashCode()` and it's preferable to not call those methods until entity beans have Id values.

@JoinColumn
-----------

Don't use `@JoinColumn` or `@JoinTable` unless we have to. The naming convention will provide good names of foreign key columns and join tables. Only use these annotations when there are existing foreign keys, and they do not match the naming convention.

@Column(name=...)
-----------------

Do not use `@Column(name=...)` to map database column names but instead use the naming convention. Only specify explicit `@Column(name=...)` when it for some reason does not match the naming convention used.

*   [java](https://ebean.io/docs/best-practice)
*   [kotlin](https://ebean.io/docs/best-practice)

@Column(name="when_activated")    // This is redundant, just adds "annotation noise"
OffsetDateTime whenActivated;

@Column(name="when_activated")    // This is redundant, just adds "annotation noise"
val whenActivated: OffsetDateTime? = null

Use @MappedSuperclass
---------------------

Make use of `@MappedSuperclass` to hold common properties. A common mapped superclass might have:

*   [java](https://ebean.io/docs/best-practice)
*   [kotlin](https://ebean.io/docs/best-practice)

...
@MappedSuperclass
public abstract class BaseDomain extends Model {

  @Id
  long id;

  @Version
  long version;

  @WhenCreated
  Instant whenCreated;

  @WhenModified
  Instant whenModified;

  // getters and setters
  ...
}

...
@MappedSuperclass
open class BaseDomain : Model() {

  @Id
  var id: Long = 0

  @Version
  var version: Long = 0

  @WhenModified
  lateinit var whenModified: Instant

  @WhenCreated
  lateinit var whenCreated: Instant

}

DDL Generation
--------------

Use Ebean to generate all DDL including DB migrations (a.k.a prefer forward generation of DDL). This keeps all the DDL "in sync" for testing and db migrations. It eases support of multiple database platforms or migration between database platforms (e.g. MySql to Postgres).

Hand-crafting DDL increases the chance of variation between the model and actual database schema which can make testing harder.

Promote use of NOT NULL constraint
----------------------------------

Make as much of the model NOT NULL as we can - prefer DB columns to have the NOT NULL constraint if possible. Reduce the amount of 3 valued logic required - have a "tighter" model.

Use Constructors
----------------

Use constructors to help enforce non nullable properties (Kotlin) or promote non nullable properties (Java).

For example, if a Customer should always have a name, define a constructor that takes the name property.

*   [java](https://ebean.io/docs/best-practice)
*   [kotlin](https://ebean.io/docs/best-practice)

@Entity
public class Customer extends BaseModel {

  @NotNull @Length(100)
  private String name;

  ...

  public Customer(String name) {
    this.name = name;
  }

  // getters and setters

}

...
@Entity
class Customer(name : String) : BaseModel() {

  @Length(100)
  var name: String = name    // Ebean knows this is Kotlin non-nullable type

}

Now when we create a new Customer we must create it with a name.

For Kotlin we should make _name_ a `non-nullable type`. Ebean will treat Kotlin non-nullable types as _NOT NULL_ from a database perspective as well giving us a tighter model.

Getters Setters
---------------

Ebean does NOT need getters and setters as it adds it's own accessor methods via enhancement.

We can omit getter and setter methods as desired. We can have setter methods follow a fluid style returning _this_ if desired.

Builder pattern
---------------

Rather than generate an additional builder class for a given entity (that duplicates all the properties of the entity and reduces maintainability) a simpler approach is to have the "setter" methods on the entity bean use the fluid style and return _this_.

@Entity
public class Customer extends BaseModel {

  @NotNull @Length(100)
  private String name;

  private String notes;

  private int level;
  ...

  public Customer(String name) {
    this.name = name;
  }

  // accessors

  public Customer setNotes(String notes) { // fluid style
    this.notes = notes;
    return this;
  }

  public Customer setLevel(int level) {  // fluid style
    this.level = level;
    return this;
  }
  ...
}

// using fluid style

Customer customer =
  new Customer("Roberto")
    .setNotes("An example")
    .setLevel(42);

Bulk update queries
-------------------

Prefer the use of [bulk update](https://ebean.io/docs/query/update) and [delete](https://ebean.io/docs/query/delete) statements where appropriate. Avoid fetching beans just to iterate and delete, or iterate and update all in the same way.

Reference beans
---------------

When we have the id value, use a reference bean rather than execute a query to find by id (unless we actually need to query the database).

For inserts and updates when we have the `@Id` value we can use reference bean for the _foreign key value_> rather than execute an extra query against the database.

#### Do **NOT** do this - as it executes an extra database query

*   [java](https://ebean.io/docs/best-practice)
*   [kotlin](https://ebean.io/docs/best-practice)

Order order = new Order()
order.setCustomer(database.find(Customer.class, 42)); // extra db query for customer
...
database.save(order);

val order = Order()
order.setCustomer(database.find(Customer.class, 42));
...
database.save(order)

#### Do **THIS** - use reference bean instead

*   [java](https://ebean.io/docs/best-practice)
*   [kotlin](https://ebean.io/docs/best-practice)

Order order = new Order()
order.setCustomer(database.getReference(Customer.class, 42)); // no extra db query
...
database.save(order);

val order = Order()
order.setCustomer(database.getReference(Customer.class, 42));
...
database.save(order)

Naming entity beans
-------------------

As a "Rob Preference" rather than strictly a "best practice" I have found that I often prefer to give entity beans a `D` prefix (Hungarian notation) like:

*   DCustomer instead of Customer
*   DProduct instead of Product
*   DOrder instead of Order 

Entity beans are generally considered _internal_ and not publicly exposed. Entity bean names often match/clash with types/names that we want to use in the public API and we frequently want to map to/from the publicly exposed API types and our internal entity beans.

Giving the entity beans a _D_ prefix (D for Domain) generally:

*   Avoids name clashes with public API types
*   Avoids needing full package qualified types in mappers
*   Can be more obvious when code is using _internal_ entity beans (persistence domain objects)

Generally entity beans are in a `domain` package. The beans being generally related to each other via _@OneToMany_, _@ManyToOne_ etc means that I prefer to keep them together as a holistic model.

Database design mindset
-----------------------

When we are building / modelling entity beans I strongly subscribe to being in a "database design mindset". We should be primarily focused on normalization and good database design principals that will last for the long term, regardless of any ORM or persistence layer we use to interact with the database.

Design for the long term.

[Edit Page](https://github.com/ebean-orm/website-source/blob/master/docs/best-practice/index.html)

[Next: Queries](https://ebean.io/docs/query)
