# Source: https://docs.pylonsproject.org/projects/colander/en/latest/binding.html

Title: Schema Binding — colander 2.0 documentation

URL Source: https://docs.pylonsproject.org/projects/colander/en/latest/binding.html

Markdown Content:
Note

Schema binding is new in colander 0.8.

Sometimes, when you define a schema at module-scope using a `class` statement, you simply don't have enough information to provide fully-resolved arguments to the [`colander.SchemaNode`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode "colander.SchemaNode") constructor. For example, the `validator` of a schema node may depend on a set of values that are only available within the scope of some function that gets called much later in the process lifetime; definitely some time very much later than module-scope import.

You needn't use schema binding at all to deal with this situation. You can instead mutate a cloned schema object by changing its attributes and assigning it values (such as widgets, validators, etc) within the function which has access to the missing values imperatively within the scope of that function.

However, if you'd prefer, you can use "deferred" values as SchemaNode keyword arguments to a schema defined at module scope, and subsequently use "schema binding" to resolve them later. This can make your schema seem "more declarative": it allows you to group all the code that will be run when your schema is used together at module scope.

What Is Schema Binding?[¶](https://docs.pylonsproject.org/projects/colander/en/latest/binding.html#what-is-schema-binding "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------

*   Any value passed as a keyword argument to a SchemaNode (e.g. `description`, `missing`, etc.) may be an instance of the `colander.deferred` class. Instances of the `colander.deferred` class are callables which accept two positional arguments: a `node` and a `kw` dictionary.

*   When a schema node is bound, it is cloned, and any `colander.deferred` values it has as attributes will be resolved by invoking the callable represented by the deferred value.

*   A `colander.deferred` value is a callable that accepts two positional arguments: the schema node being bound and a set of arbitrary keyword arguments. It should return a value appropriate for its usage (a widget, a missing value, a validator, etc).

*   Deferred values are not resolved until the schema is bound.

*   Schemas are bound via the [`colander.SchemaNode.bind()`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode.bind "colander.SchemaNode.bind") method. For example: `someschema.bind(a=1, b=2)`. The keyword values passed to `bind` are presented as the value `kw` to each `colander.deferred` value found.

*   The schema is bound recursively. Each of the schema node's children are also bound.

An Example[¶](https://docs.pylonsproject.org/projects/colander/en/latest/binding.html#an-example "Link to this heading")
------------------------------------------------------------------------------------------------------------------------

Let's take a look at an example:

 1   import datetime
 2   import colander
 3   import deform
 4
 5   @colander.deferred
 6   def deferred_date_validator(node, kw):
 7       max_date = kw.get('max_date')
 8       if max_date is None:
 9           max_date = datetime.date.today()
 10       return colander.Range(min=datetime.date.min, max=max_date)
 11
 12   @colander.deferred
 13   def deferred_date_description(node, kw):
 14       max_date = kw.get('max_date')
 15       if max_date is None:
 16           max_date = datetime.date.today()
 17       return 'Blog post date (no earlier than %s)' % max_date.ctime()
 18
 19   @colander.deferred
 20   def deferred_date_missing(node, kw):
 21       default_date = kw.get('default_date')
 22       if default_date is None:
 23           default_date = datetime.date.today()
 24       return default_date
 25
 26   @colander.deferred
 27   def deferred_body_validator(node, kw):
 28       max_bodylen = kw.get('max_bodylen')
 29       if max_bodylen is None:
 30           max_bodylen = 1 << 18
 31       return colander.Length(max=max_bodylen)
 32
 33   @colander.deferred
 34   def deferred_body_description(node, kw):
 35       max_bodylen = kw.get('max_bodylen')
 36       if max_bodylen is None:
 37           max_bodylen = 1 << 18
 38       return 'Blog post body (no longer than %s bytes)' % max_bodylen
 39
 40   @colander.deferred
 41   def deferred_body_widget(node, kw):
 42       body_type = kw.get('body_type')
 43       if body_type == 'richtext':
 44           widget = deform.widget.RichTextWidget()
 45       else:
 46           widget = deform.widget.TextAreaWidget()
 47       return widget
 48
 49   @colander.deferred
 50   def deferred_category_validator(node, kw):
 51       categories = kw.get('categories', [])
 52       return colander.OneOf([ x[0] for x in categories ])
 53
 54   @colander.deferred
 55   def deferred_category_widget(node, kw):
 56       categories = kw.get('categories', [])
 57       return deform.widget.RadioChoiceWidget(values=categories)
 58
 59   @colander.deferred
 60   def deferred_author_node(node, kw):
 61       if kw.get('with_author'):
 62           return colander.SchemaNode(
 63               colander.String(),
 64               title='Author',
 65               description='Blog author',
 66               validator=colander.Length(min=3, max=100),
 67               widget=deform.widget.TextInputWidget(),
 68           )
 69
 70   class BlogPostSchema(colander.Schema):
 71       title = colander.SchemaNode(
 72           colander.String(),
 73           title='Title',
 74           description='Blog post title',
 75           validator=colander.Length(min=5, max=100),
 76           widget=deform.widget.TextInputWidget(),
 77           )
 78       date = colander.SchemaNode(
 79           colander.Date(),
 80           title='Date',
 81           missing=deferred_date_missing,
 82           description=deferred_date_description,
 83           validator=deferred_date_validator,
 84           widget=deform.widget.DateInputWidget(),
 85           )
 86       body = colander.SchemaNode(
 87           colander.String(),
 88           title='Body',
 89           description=deferred_body_description,
 90           validator=deferred_body_validator,
 91           widget=deferred_body_widget,
 92           )
 93       category = colander.SchemaNode(
 94           colander.String(),
 95           title='Category',
 96           description='Blog post category',
 97           validator=deferred_category_validator,
 98           widget=deferred_category_widget,
 99           )
100       author = deferred_author_node
101
102   schema = BlogPostSchema().bind(
103       max_date=datetime.date.max,
104       max_bodylen=5000,
105       body_type='richtext',
106       default_date=datetime.date.today(),
107       categories=[('one', 'One'), ('two', 'Two')]
108       with_author=True,
109       )

We use `colander.deferred` in its preferred manner here: as a decorator to a function that takes two arguments. For a schema node value to be considered deferred, it must be an instance of `colander.deferred` and using that class as a decorator is the easiest way to ensure that this happens.

To perform binding, the `bind` method of a schema node must be called. `bind` returns a _clone_ of the schema node (and its children, recursively), with all `colander.deferred` values resolved. In the above example:

*   The `date` node's `missing` value will be `datetime.date.today()`.

*   The `date` node's `validator` value will be a [`colander.Range`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Range "colander.Range") validator with a `max` of `datetime.date.max`.

*   The `date` node's `widget` will be of the type `DateInputWidget`.

*   The `body` node's `description` will be the string 
```
Blog post
body (no longer than 5000 bytes)
```
.

*   The `body` node's `validator` value will be a [`colander.Length`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.Length "colander.Length") validator with a `max` of 5000.

*   The `body` node's `widget` will be of the type `RichTextWidget`.

*   The `category` node's `validator` will be of the type [`colander.OneOf`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.OneOf "colander.OneOf"), and its `choices` value will be 
```
['one',
'two']
```
.

*   The `category` node's `widget` will be of the type `RadioChoiceWidget`, and the values it will be provided will be `[('one', 'One'), ('two', 'Two')]`.

*   The `author` node will only exist if the schema is bound with `with_author=True`.

`after_bind`[¶](https://docs.pylonsproject.org/projects/colander/en/latest/binding.html#after-bind "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------

Whenever a cloned schema node has had its values successfully bound, it can optionally call an `after_bind` callback attached to itself. This can be useful for adding and removing children from schema nodes:

 1   def maybe_remove_date(node, kw):
 2       if not kw.get('use_date'):
 3           del node['date']
 4
 5   class BlogPostSchema(colander.Schema):
 6       title = colander.SchemaNode(
 7           colander.String(),
 8           title = 'Title',
 9           description = 'Blog post title',
10           validator = colander.Length(min=5, max=100),
11           widget = deform.widget.TextInputWidget(),
12           )
13       date = colander.SchemaNode(
14           colander.Date(),
15           title = 'Date',
16           description = 'Date',
17           widget = deform.widget.DateInputWidget(),
18           )
19
20    blog_schema = BlogPostSchema(after_bind=maybe_remove_date)
21    blog_schema = blog_schema.bind(use_date=False)

An `after_bind` callback is called after a clone of this node has bound all of its values successfully. The above example removes the `date` node if the `use_date` keyword in the binding keyword arguments is not true.

The deepest nodes in the node tree are bound first, so the `after_bind` methods of the deepest nodes are called before the shallowest.

An `after_bind` callback should should accept two values: `node` and `kw`. `node` will be a clone of the bound node object, `kw` will be the set of keywords passed to the `bind` method. It usually operates on the `node` it is passed using the API methods described in `SchemaNode`.

Unbound Schemas With Deferreds[¶](https://docs.pylonsproject.org/projects/colander/en/latest/binding.html#unbound-schemas-with-deferreds "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------

If you use a schema with deferred `validator`, `missing` or `default` attributes, but you use it to perform serialization and deserialization without calling its `bind` method:

*   If `validator` is deferred, [`deserialize()`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode.deserialize "colander.SchemaNode.deserialize") will raise an [`UnboundDeferredError`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.UnboundDeferredError "colander.UnboundDeferredError").

*   If `missing` is deferred, the field will be considered _required_.

*   If `default` is deferred, the serialization default will be assumed to be `colander.null`.

See Also[¶](https://docs.pylonsproject.org/projects/colander/en/latest/binding.html#see-also "Link to this heading")
--------------------------------------------------------------------------------------------------------------------

See also the [`colander.SchemaNode.bind()`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode.bind "colander.SchemaNode.bind") method and the description of `after_bind` in the documentation of the [`colander.SchemaNode`](https://docs.pylonsproject.org/projects/colander/en/latest/api.html#colander.SchemaNode "colander.SchemaNode") constructor.
