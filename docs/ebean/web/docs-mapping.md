# Source: https://ebean.io/docs/mapping

Title: Mapping | Ebean

URL Source: https://ebean.io/docs/mapping

Markdown Content:
##### Types

[All types](https://ebean.io/docs/mapping/type/), [Enum](https://ebean.io/docs/mapping/type/enum), [UUID](https://ebean.io/docs/mapping/type/uuid), [File](https://ebean.io/docs/mapping/type/file), [Boolean](https://ebean.io/docs/mapping/type/boolean), [Date and Time](https://ebean.io/docs/mapping/type/time), [Numeric](https://ebean.io/docs/mapping/type/numeric), [Other](https://ebean.io/docs/mapping/type/)

##### JPA mapping

##### Ebean mapping extenions

[Constructors](https://ebean.io/docs/mapping/constructors)
----------------------------------------------------------

Unlike JPA Ebean does **NOT** require a default constructor. You are free to create entity beans that have a constructor with arguments.

[Naming convention](https://ebean.io/docs/mapping/naming-convention)
--------------------------------------------------------------------

Ebean uses a Naming convention API. This is relatively important as it typically means we only need to specify a `@Column name` when the naming convention is not followed.

Similarly we tend to not require explicit use of `@JoinColumn` or `@JoinTable` as long as the naming convention is followed (which defaults to "underscore naming convention").

[Collections](https://ebean.io/docs/mapping/collections)
--------------------------------------------------------

Unlike Hibernate the recommendation with Ebean is to use `List` rather than `Set` for mapping collections.

JPA Notes
---------

Ebean uses the same mapping as per the JPA specification. You can learn and use the same mapping annotations. This is generally a good part of the specification and I'd expect this part of the specification to mostly stand the test of time.

There are some aspects where JPA is generally insufficient.

| Enum | Enum mapping in JPA is poor. Ebean provides 2 better alternatives in the form of `@DbEnumValue` and `@EnumValue`. We are monitoring the progress of this issue in the JPA JIRA issue tracker. |
| --- |
| FetchType EAGER / LAZY | JPA mapping encourages the use of FetchType.EAGER and LAZY which is contrary to Ebean's query approach which instead looks to optimise the queries per use case (and provides automatic query tuning by profiling the application). The use of EAGER LAZY mapping annotations is generally not useful when using Ebean. |

@Size and @NotNull
------------------

Ebean supports the use of `javax validation` annotations `@Size` and `@NotNull`.

| @Size | Defines the mapped column width. For example, @Size(50) is equivalent to @Column(length=50) |
| --- |
| @NotNull | Define the mapped column as non null. Equivalent to @Column(nullable = false) or @ManyToOne(optional=false). |

Current limitations
-------------------

There are a number of JPA mappings that Ebean does not currently support but would like to in time. These are logged as enhancement requests.

[116](https://github.com/ebean-orm/ebean/issues/116)Only single table inheritance is supported.

There is no planned support for JOINED or TABLE PER CLASS inheritance strategies.
[1777](https://github.com/ebean-orm/ebean/issues/1777)Only a single type converter per type is supported.

JPA @Converter autoApply false is not honoured. This means that we expect a type to be mapped consistently for all properties that it is used. For example, we can't have two Converters mapping Boolean two different ways in the same Ebean database instance.

You can review the entire list of outstanding issue and enhancements in the [Github Issues](https://github.com/ebean-orm/ebean/issues)

Refer to github issues marked with the [Limitation](https://github.com/ebean-orm/ebean/issues?q=is%3Aissue+is%3Aclosed+label%3ALimitation) tag.

[Edit Page](https://github.com/ebean-orm/website-source/blob/master/docs/mapping/index.html)

[Next: Naming convention](https://ebean.io/docs/mapping/naming-convention)
