# Source: https://docs.asapp.com/generativeagent/configuring/tasks-and-functions/reference-variables.md

# Reference Variables

> Learn how to use reference variables to store and reuse data from function responses

Reference variables let you store and reuse specific data returned from a function response.

Reference variables offer a powerful way to condition your GenerativeAgent tasks and functions on real data returned by your APIs—all without requiring code edits.

By properly naming, key-pathing, and optionally transforming your variables, you can build flexible, dynamic flows that truly adapt to each user's situation.

Once a reference variable is created, you can use it to:

* Conditionally make other Functions available
* Set conditional logic in prompt instructions
* Compare values across different parts of your GenerativeAgent workflow
* Control Function exposure based on data from previous function calls.
* Toggle conditional instructions in your Task s prompt depending on returned data
* Extract and transform values without hard‐coding logic into prompts or code

<Frame>
  <img src="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reference-variables.png?fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=6682090dbf9e508cced9cbe1d3cdd7bc" data-og-width="1480" width="1480" data-og-height="179" height="179" data-path="images/generativeagent/reference-variables.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reference-variables.png?w=280&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=963cecb972e917154c5044c2f1fd2d84 280w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reference-variables.png?w=560&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=6713f6204ab2c41d3c9c6a1064450c05 560w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reference-variables.png?w=840&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=0c33120f5afc09fc9a575960011a846e 840w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reference-variables.png?w=1100&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=1fd5b46a9f9e1e44e675f9f3b4acf38c 1100w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reference-variables.png?w=1650&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=264dd6c7b67f7bd3705661c747738d0c 1650w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/reference-variables.png?w=2500&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=03e0ae893d1ea16c8cf3a0a3d994e7b9 2500w" />
</Frame>

Reference variables can be configured in the GenerativeAgent Tooling Function edit page under the "Reference vars " option.

## Define a Reference Variable

To create a reference variable in the GenerativeAgent UI:

1. Navigate to the Function's settings
2. Find the "Reference vars (Optional)" section and click "Add"
3. Configure the following fields:

* **Name**
* **Response Keypath**
* **Transform Expression** (Optional)

### Name

This is the identifier you'll use to reference this variable in Jinja expressions.

```jinja  theme={null}
vars.get("variable_name")
```

### Response Keypath

This is the JSON path where the data will be extracted from, using dot notation.

```json  theme={null}
// For a response like:
{
  "available_rooms": [...]
}
// Use keypath:
response.available_rooms
```

### Transform Expression (Optional)

This is a Jinja expression to transform the extracted value. Common patterns include:

```jinja  theme={null}
# Check for specific string value
val == "COMPLIANT"

    # Check boolean values
    val == true or val == false

# Check for non-empty arrays/strings
val is not none and val|length > 0
```

Once saved, GenerativeAgent will automatically update these variables whenever the Function executes successfully and returns data matching the specified keypath.

<Note>
  Reference variable names are not unique across the entire system.

  If more than one Function defines a reference variable with the same name, whichever Function is called last may overwrite a variable's value.

  Reference variables are also used at runtime, meaning GenerativeAgent extracts the specified response data from each API call that returns successfully and updates the variable accordingly.
</Note>

## Example Condition

The following example calls a Condition on a `CheckRoomAvailability` Function.

1. Suppose a Reference Variable named `rooms_available` and defined with:
   * Response Keypath: `response.available_rooms `
   * Transform: `val is not none and val|length > 0 `
2. The `rooms_available` variable will be True whenever the returned list has a length greater than zero. You can then write:
3. In a Function's conditions (to make a function available for use, conditioned on the reference variable):
   ```json  theme={null}
       conditions: vars.get("rooms_available")
   ```
4. In Task instructions using Jinja:
   ```jinja  theme={null}
           {%- if vars.get("rooms_available") %}
           The requested rooms are available.  
           {%- else %}
           No rooms are currently available.  
           {%- endif %}
   ```

### Tips and Best Practice

Here are some tips to enhance your experience with  Reference Variables:

<AccordionGroup>
  <Accordion title="Prefix Variables">
    Consider prefixing variable names to avoid clashes if multiple teams define references.

    Example: `user_is_compliant` vs. `is_compliant`
  </Accordion>

  <Accordion title="Short-circuit logic">
    Use short-circuit logic in transforms to avoid "NoneType cannot have length" errors

    Example `val is not none and val|length > 0`
  </Accordion>

  <Accordion title="Functions consideration">
    Keep in mind that if multiple Functions define the same reference variable name, one may overwrite the other depending on the call order.
  </Accordion>
</AccordionGroup>
