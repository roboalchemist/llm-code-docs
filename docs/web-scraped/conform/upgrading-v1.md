# Source: https://conform.guide/upgrading-v1

# Upgrading to v1 

In this guide, we will walk you through all the changes that were introduced in v1 and how to upgrade your existing codebase.

## [\#](/upgrading-v1#minimum-react-version)Minimum React version 

Conform now requires React 18 or higher. If you are using an older version of React, you will need to upgrade your react version first.

## [\#](/upgrading-v1#the-conform-object-is-removed)The `conform` object is removed 

First, all helpers are renamed and can be imported individually:

-   `conform.input` -\> [getInputProps](/api/react/getInputProps)
-   `conform.select` -\> [getSelectProps](/api/react/getSelectProps)
-   `conform.textarea` -\> [getTextareaProps](/api/react/getTextareaProps)
-   `conform.fieldset` -\> [getFieldsetProps](/api/react/getFieldsetProps)
-   `conform.collection` -\> [getCollectionProps](/api/react/getCollectionProps)

If you are using `conform.VALIDATION_UNDEFINED` and `conform.VALIDATION_SKIPPED` before, you will find them on our zod integration (`@conform-to/zod`) instead.

-   `conform.VALIDATION_SKIPPED` -\> [conformZodMessage.VALIDATION_SKIPPED](/api/zod/conformZodMessage.md#conformzodmessagevalidation_skipped)
-   `conform.VALIDATION_UNDEFINED` -\> [conformZodMessage.VALIDATION_UNDEFINED](/api/zod/conformZodMessage.md#conformzodmessagevalidation_undefined)

Be aware that `conform.INTENT` is no longer exported. If you need to setup an intent button, you can name it [intent] (or anything you preferred) in combination with [z.discriminatedUnion()](https://zod.dev/?id=discriminated-unions) from zod for better type safety.

There are also some breaking changes on the options:

-   The `type` option on `getInputProps` is now required.

``` 
1<input )} />
```

-   The `description` option is renamed to `ariaDescribedBy` and expects a string (the `id` of the description element) instead of a boolean.

``` 
1<input
2  )}
5/>
```

## [\#](/upgrading-v1#form-setup-changes)Form setup changes 

First,`form.props` is removed. You can use the [getFormProps()](/api/react/getFormProps) helper instead.

``` 
1import  from '@conform-to/react';
2
3function Example()  />;
7}
```

Both `useFieldset` and `useFieldList` hooks are removed. You can call the `getFieldset()` or `getFieldList()` method on the field metadata instead.

``` 
1function Example() ></li>;
18        })}
19      </ul>
20    </form>
21  );
22}
```

Both `validate` and `list` exports are merged into the form metadata object:

``` 
1function Example() ></li>;
10        })}
11      </ul>
12      <button )}>
13        Add (Declarative API)
14      </button>
15      <button onClick=)}>
16        Add (Imperative API)
17      </button>
18    </form>
19  );
20}
```

Here are all the equivalent methods:

-   `validate` -\> `form.validate`
-   `list.insert` -\> `form.insert`
-   `list.remove` -\> `form.remove`
-   `list.reorder` -\> `form.reorder`
-   `list.replace` -\> `form.update`
-   `list.append` and `list.prepend` are removed. You can use `form.insert` instead.

## [\#](/upgrading-v1#schema-integration)Schema integration 

We have also renamed the APIs on each of the integrations with an unique name to avoid confusion. Here are the equivalent methods:

#### `@conform-to/zod` 

-   `parse` -\> [parseWithZod](/api/zod/parseWithZod)
-   `getFieldsetConstraint` -\> [getZodConstraint](/api/zod/getZodConstraint)

#### `@conform-to/yup` 

-   `parse` -\> [parseWithYup](/api/yup/parseWithYup)
-   `getFieldsetConstraint` -\> [getYupConstraint](/api/yup/getYupConstraint)

## [\#](/upgrading-v1#improved-submission-handling)Improved submission handling 

We have redesigned the submission object to simplify the setup.

``` 
1export async function action(: ActionArgs) );
4
5  /**
6   * The submission status could be either "success", "error" or undefined
7   * If the status is undefined, it means that the submission is not ready (i.e. `intent` is not `submit`)
8   */
9  if (submission.status !== 'success') );
14  }
15
16  const result = await save(submission.value);
17
18  if (!result.successful) ,
26
27        // or avoid sending the the field value back to client by specifying the field names
28        hideFields: ['password'],
29      }),
30    );
31  }
32
33  // Reply the submission with `resetForm` option
34  return json(submission.reply());
35}
36
37export default function Example() );
43
44  // We can now find out the status of the submission from the form metadata as well
45  console.log(form.status); // "success", "error" or undefined
46}
```

## [\#](/upgrading-v1#simplified-integration-with-the-useinputcontrol-hook)Simplified integration with the `useInputControl` hook 

The `useInputEvent` hook is replaced by the [useInputControl](/api/react/useInputControl) hook with some new features.

-   There is no need to provide a ref of the inner input element anymore. It looks up the input element from the DOM and will insert one for you if it is not found.

-   You can now use `control.value` to integrate a custom input as a controlled input and update the value state through `control.change(value)`. The value will also be reset when a form reset happens

``` 
1import  from '@conform-to/react';
2import  from './some-ui-library';
3
4function Example() 
11      value=
12      onChange=
13      onFocus=
14      onBlur=
15    />
16  );
17}
```