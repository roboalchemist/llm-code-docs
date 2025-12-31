# Source: https://conform.guide/checkbox-and-radio-group

# Checkbox and Radio Group 

Setting up a checkbox or radio group is no different from any standard inputs.

## [\#](/checkbox-and-radio-group#radio-group)Radio Group 

To set up a radio group, make sure the [name] attribute is the same for all the inputs. You can also use the initialValue from the field metadata to derive whether the radio button should be checked.

``` 
1import  from '@conform-to/react';
2
3function Example() >
8      <fieldset>
9        <legend>Please select your favorite color</legend>
10        >
12            <label></label>
13            <input
14              type="radio"
15              name=
16              value=
17              defaultChecked=
18            />
19          </div>
20        ))}
21        <div></div>
22      </fieldset>
23      <button>Submit</button>
24    </form>
25  );
26}
```

## [\#](/checkbox-and-radio-group#checkbox)Checkbox 

Setting up a checkbox group would be similar to a radio group except the initialValue can be either a string or an array because of missing information on the server side whether the checkbox is a boolean or a group. You can derive the [defaultChecked] value from the initialValue as shown below. As the errors from both yup and zod are mapped based on the corresponding paths and the errors of each option will be mapped to its corresponding index, e.g. `answer[0]` instead of the array itself, e.g. `answers`. If you want to display all the errors, you can consider using the [allErrors] property on the field metadata instead.

``` 
1import  from '@conform-to/react';
2
3function Example() >
8      <fieldset>
9        <legend>Please select the correct answers</legend>
10        >
12            <label></label>
13            <input
14              type="checkbox"
15              name=
16              value=
17              defaultChecked=
23            />
24          </div>
25        ))}
26        <div></div>
27      </fieldset>
28      <button>Submit</button>
29    </form>
30  );
31}
```

However, if it is just a single checkbox, you can check if the initialValue matches the input [value] which defaults to [on] by the browser.

``` 
1import  from '@conform-to/react';
2
3function Example() >
8      <div>
9        <label>Terms and conditions</label>
10        <input
11          name=
12          defaultChecked=
13        />
14        <div></div>
15      </div>
16      <button>Submit</button>
17    </form>
18  );
19}
```