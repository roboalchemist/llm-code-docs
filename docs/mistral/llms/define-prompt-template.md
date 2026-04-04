# define prompt template
prompt_template = """
Extract information from the following medical notes:
{medical_notes}

Return json format with the following JSON schema: 

{{
        "age": {{
            "type": "integer"
        }},
        "gender": {{
            "type": "string",
            "enum": ["male", "female", "other"]
        }},
        "diagnosis": {{
            "type": "string",
            "enum": ["migraine", "diabetes", "arthritis", "acne", "common cold"]
        }},
        "weight": {{
            "type": "integer"
        }},
        "smoking": {{
            "type": "string",
            "enum": ["yes", "no"]
        }},
        
}}
"""
```

- Step 2: Define how we compare the model response with the golden answer

In step 2, we wrote a function to compare two json objects, with one being the model response and one being the golden answer. In this example, we calculate the percentage of matching values across the JSON keys to assess the accuracy of the JSON output. 

```py


def compare_json_objects(obj1, obj2):
    total_fields = 0
    identical_fields = 0
    common_keys = set(obj1.keys()) & set(obj2.keys())
    for key in common_keys:
        identical_fields += obj1[key] == obj2[key]
    percentage_identical = (identical_fields / max(len(obj1.keys()), 1)) * 100
    return percentage_identical
```

- Step 3: Calculate accuracy rate across test cases 
Now, we're able to go through each test case individually. For each case, we can create a user message based on the prompt template we've already defined. We then retrieve responses from the LLM and compare them to the correct answers. After calculating the accuracy rate for each test case, we can calcate the overall average accuracy rate across all cases.

```py
accuracy_rates = []