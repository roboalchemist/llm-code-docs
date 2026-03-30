# Append the tool call message to the chat_history
chat_history.append(tool_call_result)
```

### Make the Final Chat Request

```python
chat_response = client.chat.complete(
    model=model,
    messages=chat_history,
    tools=[get_information_tool],
)

print(chat_response.choices[0].message.content)
```

Output:
```
[TextChunk(text='The Nobel Peace Prize for 2024 was awarded to the Japan Confederation of A- and H-Bomb Sufferers Organizations (Nihon Hidankyo) for their activism against nuclear weapons, including efforts by survivors of the atomic bombings of Hiroshima and Nagasaki', type='text'), ReferenceChunk(reference_ids=[0], type='reference'), TextChunk(text='.', type='text')]
```

### Extract and Print References

```python
from mistralai.models import TextChunk, ReferenceChunk

refs_used = []