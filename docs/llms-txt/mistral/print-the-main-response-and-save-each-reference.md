# Print the main response and save each reference
for chunk in chat_response.choices[0].message.content:
    if isinstance(chunk, TextChunk):
        print(chunk.text, end="")
    elif isinstance(chunk, ReferenceChunk):
        refs_used += chunk.reference_ids