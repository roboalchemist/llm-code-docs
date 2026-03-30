# Source: https://conform.guide/complex-structures

# Nested object and Array 

Conform support both nested object and array by leveraging a naming convention on the name attribute.

## [\#](/complex-structures#naming-convention)Naming Convention 

Conform uses the `object.property` and `array[index]` syntax to denote data structure. These notations could be combined for nested array as well. e.g. `tasks[0].content`. If the form data has an entry `['tasks[0].content', 'Hello World']`, the object constructed will become `] }`.

However, there is no need to set the name attribute of each field manually. Conform will always infer the name for you and you will have better type safety if you are using the generated name.

## [\#](/complex-structures#nested-object)Nested Object 

To set up a nested field, just call the `getFieldset()` method from the parent field metadata to get access to each child field with name infered automatically.

``` 
1import  from '@conform-to/react';
2import  from '@conform-to/zod';
3import  from 'zod';
4
5const schema = z.object(),
12});
13
14function Example() ) );
18    },
19  });
20  const address = fields.address.getFieldset();
21
22  return (
23    <form id=>
24      
25      <input name= />
26      <div></div>
27      <input name= />
28      <div></div>
29      <input name= />
30      <div></div>
31      <input name= />
32      <div></div>
33    </form>
34  );
35}
```

## [\#](/complex-structures#array)Array 

When you need to setup a list of fields, you can call the `getFieldList()` method from the parent field metadata to get access to each item field with name infered automatically as well. If you want to modify the items in the list, you can also use the `insert`, `remove` and `reorder` intents as explained in the [Intent button](/intent-button#form-controls) page.

``` 
1import  from '@conform-to/react';
2import  from '@conform-to/zod';
3import  from 'zod';
4
5const schema = z.object();
8
9function Example() ) );
13    },
14  });
15  const tasks = fields.tasks.getFieldList();
16
17  return (
18    <form id=>
19      <ul>
20        >
22            
23            <input name= />
24            <div></div>
25          </li>
26        ))}
27      </ul>
28    </form>
29  );
30}
```

## [\#](/complex-structures#nested-array)Nested Array 

You can also combine both `getFieldset()` and `getFieldList()` for nested array.

``` 
1import  from '@conform-to/react';
2import  from '@conform-to/zod';
3import  from 'zod';
4
5const schema = z.object(),
11  ),
12});
13
14function Example() ) );
18    },
19  });
20  const todos = fields.todos.getFieldList();
21
22  return (
23    <form id=>
24      <ul>
25        >
30              <input name= />
31              <div></div>
32              <input name= />
33              <div></div>
34            </li>
35          );
36        })}
37      </ul>
38    </form>
39  );
40}
```