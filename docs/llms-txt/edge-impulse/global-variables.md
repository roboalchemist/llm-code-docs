# Source: https://docs.edgeimpulse.com/tools/libraries/sdks/inference/cpp/global-variables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Global variables

Global variables accessible outside of the C++ SDK library.

## ei\_classifier\_inferencing\_categories\[]

```cpp  theme={"system"}
const char* ei_classifier_inferencing_categories[] = { ... };
```

**Brief**: Array of class label strings

**Source**: Can be found in *model-parameters/model\_variables.h* if you deploy your impulse as a C++ library.

**Description:**
Global variable containing a static array of class labels in alphabetical order. Each label is a string.

Number of labels is equal to `EI_CLASSIFIER_LABEL_COUNT`.

**Example:**
You can print out all of the available labels with, for example:

```
for (int ix = 0; ix < EI_CLASSIFIER_LABEL_COUNT; ix++) {
    ei_printf("%s\r\n", ei_classifier_inferencing_categories[ix]);
}
```


Built with [Mintlify](https://mintlify.com).