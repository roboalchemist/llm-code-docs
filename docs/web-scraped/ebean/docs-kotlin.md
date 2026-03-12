# Source: https://ebean.io/docs/kotlin

Title: Kotlin | Ebean

URL Source: https://ebean.io/docs/kotlin

Markdown Content:
Constructors
------------

Ebean does not require a default constructor. We should use constructors to supply the required / non-nullable properties when creating entity bean instances.

For example, if a Customer entity bean requires a name property we can have that in the constructor and use a Kotlin non-nullable type.

...
@Entity
class Customer(name : String) : BaseModel() {

  @Length(100)
  var name: String = name  // Kotlin non-nullable type

}

The _suggested_ constructor style to use with Kotlin is like the above with the constructor parameter assigned to the property. The reason for this is that with entity bean properties we often have mapping annotations (`@Length` etc) and it can be easier / clearer to not have those as part of the constructor (where there are more targets for the annotations - method, field, parameter etc).

Non-nullable types
------------------

Ebean is aware of Kotlin non nullable types and automatically treats them as `@NotNull`. We don't need to specify `@NotNull` or `@Column(nullable=false)` or `@ManyToOne(optional=false)` when the property is a Kotlin non nullable type.

MappedSuperclass
----------------

It is common to have a mapped superclass that extends `io.ebean.Model` and has `@WhenCreated` and `@WhenModified` like below:

@MappedSuperclass
abstract class BaseModel : Model() {

  @Id
  var id: Long = 0

  @Version
  var version: Long = 0

  @WhenCreated
  lateinit var whenCreated: Instant

  @WhenModified
  lateinit var whenModified: Instant

}

It is ok to use `lateinit` for the whenCreated and whenModified properties and have them as nullable types.

It is good to use non nullable `Int = 0` and `Long = 0` for `@Id` properties like the example above (JVM primitive int and long).

@OneToMany
----------

For collection types `@OneToMany` and `@ManyToMany` it is good to use non nullable mutable lists and initialise then with `mutableListOf()`. Ebean enhancement will optimise this and collection types will only be initialised when needed (so it's good to model it as a Kotlin non nullable collection type).

@Entity
@Table(name = "orders")
class Order(customer: Customer) : BaseModel() {

  ...

  @OneToMany(mappedBy = "order", cascade = [CascadeType.PERSIST])
  var details: MutableList<OrderDetail> = mutableListOf()

}
