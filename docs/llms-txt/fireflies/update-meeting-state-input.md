# Source: https://docs.fireflies.ai/schema/input/update-meeting-state-input.md

# UpdateMeetingStateInput

> Schema for UpdateMeetingStateInput

<ParamField path="meeting_id" type="ID!" required>
  The ID of the live meeting to update state for
</ParamField>

<ParamField path="action" type="MeetingStateAction!" required>
  The action to perform. Must be one of: `pause_recording` or `resume_recording`
</ParamField>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.fireflies.ai/llms.txt