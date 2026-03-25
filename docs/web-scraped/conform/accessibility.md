# Source: https://conform.guide/accessibility

# Accessibility 

Making your form accessible requires configuring each form element with proper attributes. But Conform can help you with that.

## [\#](/accessibility#aria-attributes)Aria Attributes 

When it comes to accessibility, aria attributes are usually the first thing that comes to mind, which usually requires some unique ids to associate different elements together. Conform helps you by generating all the ids for you.

``` 
1import  from '@conform-to/react';
2
3function Example() >
8      <label htmlFor=>Message</label>
9      <input
10        type="text"
11        id=
12        name=
13        aria-invalid=
14        aria-describedby= $`
17            : fields.message.descriptionId
18        }
19      />
20      <div id=>The message you want to send</div>
21      <div id=></div>
22      <button>Send</button>
23    </form>
24  );
25}
```

## [\#](/accessibility#validation-attributes)Validation attributes 

Validation attributes also play an important role in accessibility, such as improving the hint for screen readers. With Conform, you can derive the validation attributes from your zod or yup schema and have them populated on each field metadata.

``` 
1import  from '@conform-to/zod';
2import  from '@conform-to/react';
3import  from 'zod';
4
5const schema = z.object($/),
11});
12
13function Example() ) );
18    },
19  });
20
21  return (
22    <form id=>
23      <input
24        type="text"
25        name=
26        required=
27        minLength=
28        maxLength=
29        pattern=
30      />
31      <button>Send</button>
32    </form>
33  );
34}
```

## [\#](/accessibility#progressive-enhancement)Progressive enhancement 

Progressive enhancement also helps with accessibility, such as minimizing the impact of temporary network issues. For example, Conform make it possible to manipulate a list of fields with the form data and state persisted even across page refreshes.

``` 
1import  from '@conform-to/react';
2
3export default function Example() >
8      <ul>
9        >
11            <input name= defaultValue= />
12            <button
13              )}
17            >
18              Delete
19            </button>
20          </li>
21        ))}
22      </ul>
23      <button
24        )}
27      >
28        Add task
29      </button>
30      <button>Save</button>
31    </form>
32  );
33}
```

## [\#](/accessibility#reducing-boilerplate)Reducing boilerplate 

Setting up all the attributes mentioned above can be tedious and error prone. Conform wants to help you with that by providing a set of helpers that derive all the related attributes for you.

> Note: All the helpers mentioned are designed for the native HTML elements. You might not need them if you are using custom UI components, such as react-aria-components or Radix UI, which might already have the attributes set up for you through their own APIs.

-   [getFormProps](/api/react/getFormProps)
-   [getFieldsetProps](/api/react/getFieldsetProps)
-   [getInputProps](/api/react/getInputProps)
-   [getSelectProps](/api/react/getSelectProps)
-   [getTextareaProps](/api/react/getTextareaProps)
-   [getCollectionProps](/api/react/getButtonProps)

Here is an example of how it compares to the manual setup. If you want to know more about the helpers, please check the corresponding documentation linked above

``` 
1import  from '@conform-to/zod';
2import  from '@conform-to/react';
3import  from 'zod';
4
5const schema = z.object($/),
11});
12
13function Example() ) );
18    },
19  });
20
21  return (
22    <form id=>
23      
24      <input
25        type="text"
26        id=
27        name=
28        required=
29        minLength=
30        maxLength=
31        pattern=
32        aria-invalid=
33        aria-describedby= $`
36            : fields.message.descriptionId
37        }
38      />
39      
40      <input
41        )}
45      />
46      <button>Send</button>
47    </form>
48  );
49}
```