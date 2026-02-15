# Zendesk Voice/Talk API - Complete Reference

Source: https://developer.zendesk.com/documentation/voice/

The Zendesk Voice API (also called Talk API) enables integration with telephony systems for call center automation, call recording, and ticket creation from phone interactions.

## Overview

Zendesk Voice provides:

- Inbound/outbound call management
- Call recording and transcription
- Voicemail handling
- Call routing and IVR
- Integration with ticket system
- Real-time call metrics
- Call history and analytics

## Core Concepts

### Phone Numbers

Zendesk-provided or custom phone numbers for receiving calls.

### Phone Lines

Collections of phone numbers grouped by location or team.

### IVR (Interactive Voice Response)

Automated call handling with menu options and routing.

### Agents

Support staff who answer calls and create tickets from interactions.

### Call Recordings

Audio files of conversations for training and compliance.

### Voicemails

Messages left when agents unavailable.

### Phone Tags

Categorization of calls and voicemails.

## Authentication

Use API token authentication:

```bash
curl -H "Authorization: Bearer YOUR_API_TOKEN" \
  https://yoursubdomain.zendesk.com/api/v2/channels/voice/...
```

## API Endpoints

### Phone Numbers (Provisioning)

```bash
GET /phone_numbers                    # List phone numbers
POST /phone_numbers                   # Provision new number
GET /phone_numbers/{id}              # Get number details
PUT /phone_numbers/{id}              # Update number settings
DELETE /phone_numbers/{id}           # Delete number

GET /phone_numbers/{id}/ivr          # Get IVR configuration
PUT /phone_numbers/{id}/ivr          # Configure IVR
```

**Phone Number Properties:**

- `id` - Unique identifier
- `number` - Phone number with country code
- `display_name` - Display name for calls
- `country_code` - Country/region
- `phone_line_id` - Associated phone line
- `enabled` - Active/inactive status
- `capabilities` - Inbound, outbound, SMS, etc.
- `created_at`, `updated_at` - Timestamps

### Phone Lines (Management)

```bash
GET /phone_lines                      # List phone lines
POST /phone_lines                     # Create phone line
GET /phone_lines/{id}                # Get line details
PUT /phone_lines/{id}                # Update line
DELETE /phone_lines/{id}             # Delete line
```

### Call Logs (History)

```bash
GET /phone_calls                      # List call history
GET /phone_calls/{id}                # Get call details
GET /phone_calls/{id}/recordings     # Get call recording
POST /phone_calls/{id}/create_ticket # Create ticket from call
```

**Call Log Properties:**

- `id` - Call identifier
- `from` - Caller phone number
- `to` - Called phone number
- `direction` - Inbound or outbound
- `duration` - Call length in seconds
- `started_at`, `ended_at` - Timestamps
- `agents` - Participating agents
- `status` - Connected, abandoned, missed
- `recording_url` - Audio file URL
- `transcription` - Call transcript (if available)
- `tags` - Associated tags

### Voicemails (Messages)

```bash
GET /phone_voicemails                # List voicemails
GET /phone_voicemails/{id}          # Get voicemail details
GET /phone_voicemails/{id}/audio    # Download audio file
DELETE /phone_voicemails/{id}       # Delete voicemail
POST /phone_voicemails/{id}/create_ticket  # Create ticket
```

**Voicemail Properties:**

- `id` - Voicemail identifier
- `from` - Caller phone number
- `to` - Voicemail box number
- `received_at` - Timestamp
- `duration` - Message length in seconds
- `audio_url` - Audio file URL
- `transcription` - Voice-to-text (if available)
- `status` - New, read, archived
- `tags` - Associated tags

### Call Recordings (Audio Files)

```bash
GET /phone_recordings                # List recordings
GET /phone_recordings/{id}          # Get recording details
GET /phone_recordings/{id}/download # Download audio file
DELETE /phone_recordings/{id}       # Delete recording

GET /phone_calls/{id}/recordings    # Get recordings for call
```

**Recording Properties:**

- `id` - Recording identifier
- `call_id` - Associated call
- `duration` - Recording length
- `format` - Audio format (MP3, WAV)
- `download_url` - Audio file URL
- `transcription_status` - Pending, completed, failed
- `transcription` - Text version
- `created_at` - Timestamp

### IVR Configuration (Menus)

```bash
GET /phone_numbers/{id}/ivr         # Get IVR settings
PUT /phone_numbers/{id}/ivr         # Update IVR

POST /phone_ivr_menus               # Create IVR menu
GET /phone_ivr_menus/{id}          # Get menu
PUT /phone_ivr_menus/{id}          # Update menu
```

**IVR Menu Structure:**

```json
{
  "ivr_menu": {
    "greeting": "Thank you for calling...",
    "options": [
      {
        "digit": "1",
        "label": "Sales",
        "action": "transfer",
        "target_id": "queue-123"
      },
      {
        "digit": "2",
        "label": "Support",
        "action": "transfer",
        "target_id": "queue-456"
      },
      {
        "digit": "0",
        "label": "Operator",
        "action": "transfer",
        "target_id": "agent-789"
      }
    ],
    "repeat_message": "Press 1 for sales, 2 for support",
    "invalid_message": "Invalid option, please try again"
  }
}
```

### Agent Status

```bash
GET /agents/{id}/phone_status       # Get agent phone status
PUT /agents/{id}/phone_status       # Update agent status
```

**Agent Status Values:**

- `available` - Ready to take calls
- `unavailable` - Not taking calls
- `on_call` - Currently on call
- `after_call_work` - Processing call

### Call Routing

```bash
GET /phone_queues                    # List call queues
POST /phone_queues                   # Create queue
GET /phone_queues/{id}              # Get queue details
PUT /phone_queues/{id}              # Update queue
DELETE /phone_queues/{id}           # Delete queue

GET /phone_queues/{id}/members      # Get queue members
POST /phone_queues/{id}/members     # Add to queue
DELETE /phone_queues/{id}/members/{agent_id}  # Remove from queue
```

**Queue Properties:**

- `id` - Queue identifier
- `name` - Queue name
- `members` - Agent IDs in queue
- `max_wait_time` - Max hold time
- `overflow_action` - Action when queue full
- `overflow_target` - Where to route overflow calls

## Creating Tickets from Calls

### From Call Log

```bash
POST /phone_calls/{id}/create_ticket
{
  "ticket": {
    "subject": "Call from customer regarding order",
    "description": "Discussed order #123 status",
    "tags": ["phone", "inbound"],
    "custom_fields": [
      {
        "id": 12345,
        "value": "Called in"
      }
    ]
  }
}
```

### From Voicemail

```bash
POST /phone_voicemails/{id}/create_ticket
{
  "ticket": {
    "subject": "Voicemail from customer",
    "description": "Customer called requesting callback",
    "priority": "high"
  }
}
```

## Common Workflows

### Call Recording Access

```bash
# 1. Get call log entry
GET /phone_calls/12345

# 2. Check if recording exists
{
  "phone_call": {
    "recording_url": "https://..."
  }
}

# 3. Download recording
GET /phone_recordings/67890/download
```

### Voicemail-to-Ticket Automation

```bash
# 1. List new voicemails
GET /phone_voicemails?filter=new

# 2. Get voicemail details
GET /phone_voicemails/abcd

# 3. Create ticket with recording attached
POST /tickets
{
  "ticket": {
    "subject": "Voicemail followup required",
    "description": "Customer called while unavailable",
    "attachments": [
      {
        "url": "https://voicemail-recording.mp3"
      }
    ]
  }
}

# 4. Mark voicemail handled
DELETE /phone_voicemails/abcd
```

### Agent Availability Management

```bash
# 1. Update agent status to available
PUT /agents/12345/phone_status
{
  "status": "available"
}

# 2. Route inbound calls to available agents
# (Configured in IVR or queue settings)

# 3. Monitor agent activity
GET /agents/12345/phone_status
```

### Call Quality Monitoring

```bash
# 1. Get recent calls for agent
GET /phone_calls?agent_id=123&limit=50

# 2. Access call recordings for review
GET /phone_calls/456/recordings

# 3. Check transcription for quality assessment
GET /phone_calls/456
{
  "phone_call": {
    "transcription": "Full call transcript..."
  }
}
```

## Analytics & Reporting

### Call Metrics

```bash
GET /phone_calls?start_date=2024-02-01&end_date=2024-02-14

Response includes:
- Total calls
- Average duration
- Missed calls
- Voicemails
- Agent performance
```

### Queue Analytics

```bash
GET /phone_queues/{id}/analytics
{
  "average_wait_time": 45,
  "max_queue_depth": 12,
  "abandoned_calls": 3,
  "success_rate": 94.2
}
```

### Transcription Insights

```bash
# Access transcriptions for compliance and training
GET /phone_calls/{id}
{
  "transcription": "...",
  "sentiment": "positive|neutral|negative",
  "keywords": ["urgent", "complaint", "refund"]
}
```

## Integration with Zendesk Support

### Ticket Context

Call information automatically available in ticket:

- Caller phone number
- Call duration
- Call recording link
- Transcription
- Associated agent

### Automatic Ticket Creation

Configure rules to create tickets from:

- Inbound calls (on answer)
- Missed calls
- Voicemails
- Calls by first-time customers

### Call Logging

Manually or automatically log calls to ticket:

```bash
POST /tickets/{id}/comments
{
  "comment": {
    "body": "Phone call - 15 minutes - discussed billing issue",
    "public": false
  }
}
```

## Partner Edition API

**Talk Partner Edition API** for custom telephony integration:

```bash
POST /phone_call_events        # Log call events
POST /phone_recording_upload   # Upload recordings
POST /voicemail_upload         # Upload voicemails
```

Enables integration of custom phone systems while maintaining Zendesk integration.

## Best Practices

### Call Recording Compliance

- Obtain consent before recording (varies by jurisdiction)
- Store recordings securely
- Implement retention policies
- Handle deletion requests promptly

### Agent Training

- Review call recordings regularly
- Use transcriptions for QA
- Identify common customer issues
- Provide coaching feedback

### Performance Optimization

- Monitor queue metrics
- Adjust staffing based on demand
- Implement callback systems
- Route to specialized agents

### Data Management

- Retain recordings per compliance requirements
- Archive old call logs
- Implement data retention policies
- Secure personal information

## Limits & Quotas

- **Recording Storage**: Depends on subscription
- **Recording Duration**: No limit per call
- **Transcription**: Automatic for most plans
- **API Rate**: 600 requests per minute
- **Queue Size**: Up to 1000 pending calls

## Error Handling

**Common Errors:**

```json
{
  "error": "Invalid phone number",
  "description": "Phone number must be valid E.164 format"
}

{
  "error": "Recording not available",
  "description": "Call recording has been deleted"
}

{
  "error": "Agent not available",
  "description": "Agent is on call or unavailable"
}
```

## Migration from Previous Phone Systems

1. Import call history into Zendesk
2. Migrate phone numbers
3. Configure IVR and routing
4. Train agents on new system
5. Monitor quality during transition

## Resources

- [Voice API Documentation](https://developer.zendesk.com/api-reference/voice/)
- [Talk Partner Edition API](https://developer.zendesk.com/api-reference/voice/talk-partner-edition-api/)
- [Zendesk Voice Setup Guide](https://support.zendesk.com/hc/en-us/sections/202911607)
- [Call Recording Compliance](https://support.zendesk.com/hc/en-us/articles/203661906)
