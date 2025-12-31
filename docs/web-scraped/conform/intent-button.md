# Source: https://conform.guide/intent-button

# Intent button 

A submit button will contribute to the form data when it triggers the submission as a [submitter](https://developer.mozilla.org/en-US/docs/Web/API/SubmitEvent/submitter).

## [\#](/intent-button#submission-intent)Submission Intent 

The submitter is particularly useful when you want to extend the form with different behaviour based on the intent.

``` 
1import  from '@conform-to/react';
2
3function Product() ) 
16    },
17  });
18
19  return (
20    <form id=>
21      <input type="hidden" name="productId" value="rf23g43" />
22      <button type="submit" name="intent" value="add-to-cart">
23        Add to Cart
24      </button>
25      <button type="submit" name="intent" value="buy-now">
26        Buy now
27      </button>
28    </form>
29  );
30}
```

## [\#](/intent-button#form-controls)Form Controls 

Conform utilizes the submission intent for all form controls, such as validating or removing a field. This is achieved by giving the buttons a reserved name with the intent serialized as the value. To simplify the setup, Conform provides a set of form control helpers, such as `form.validate`, `form.reset` or `form.insert`.

### Validate intent 

To trigger a validation, you can configure a button with the validate intent.

``` 
1import  from '@conform-to/react';
2
3function EmailForm() >
8      <input name= />
9      <button )}>
10        Validate Email
11      </button>
12    </form>
13  );
14}
```

When the button is clicked, conform identifies the serialized intent with the reserved name and trigger a validation by marking the email field as validated and returns the error message if the email is invalid.

However, if you want to trigger the validation once the user leaves the field, you can also trigger the validate intent directly.

``` 
1import  from '@conform-to/react';
2
3function EmailForm() >
8      <input
9        name=
10        onBlur=)}
11      />
12    </form>
13  );
14}
```

### Reset and Update intent 

You can also modify a field with the [reset] and [update] intent.

``` 
1import  from '@conform-to/react';
2
3export default function Tasks() >
8      <button >Reset form</button>
9      <button
10        )}
13      >
14        Reset field (including nested / list field)
15      </button>
16      <button
17        ,
23        })}
24      >
25        Update field (including nested / list field)
26      </button>
27      <button
28        )}
31      >
32        Clear all error
33      </button>
34    </form>
35  );
36}
```

Be aware that both intents requires setting up the inputs with the [key] from the field metadata. As Conform relies on the key to notify React for re-mounting the input with the updated initialValue. The only exception is if you are setting up a controlled input with the [useInputControl](/api/react/useInputControl) hook which will reset the value when the key changes.

### Insert, remove and reorder intents 

To manipulate a field list, you can use the [insert], [remove] and [reorder] intents.

``` 
1import  from '@conform-to/react';
2import  from "@conform-to/zod";
3import  from "zod";
4
5const todosSchema = z.object();
9
10export default function Tasks() ) );
14    },
15    shouldValidate: "onBlur",
16  });
17  const tasks = fields.tasks.getFieldList();
18
19  return (
20    <form id= onSubmit=>
21      <ul>
22        >
24            <input name= />
25            <button
26              )}
31            >
32              Move to top
33            </button>
34            <button
35              )}
39            >
40              Delete
41            </button>
42          </li>
43        ))}
44      </ul>
45      <button
46        )}
49      >
50        Add task
51      </button>
52      <button>Save</button>
53    </form>
54  );
55}
```