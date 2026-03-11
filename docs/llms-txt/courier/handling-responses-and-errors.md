# Source: https://www.courier.com/docs/platform/sending/handling-responses-and-errors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Responses & Error Codes

After sending a message with the Courier API, you’ll receive a response indicating whether the request was successful and how to track its delivery. Understanding these responses and handling errors correctly ensures reliable delivery and better visibility into message outcomes.

This guide explains how to:

* Interpret success and error responses from the Send API
* Implement robust error-handling logic in production
* Monitor message status in the Courier dashboard
* Receive real-time delivery updates through webhooks

By following these patterns, you can build resilient notification workflows that recover from temporary issues and provide clear delivery insight to your team.

## Response Handling

### Success Response

Successful sends return a request ID for tracking:

```json  theme={null}
{
  "requestId": "87e7c05b-4f46-fda24e356e23"
}
```

### Error Responses

If a send request fails, the Courier API returns an error response with an HTTP status code and message explaining the issue.

Common error scenarios include:

* **`400`**: Bad Request - Invalid message format or missing fields
* **`401`**: Unauthorized - Invalid or expired auth token
* **`500`**: Internal Server Error - Courier service issue

## Monitoring & Debugging

### Message Logs

Message Logs in the [Courier dashboard](https://app.courier.com/logs) provide real-time visibility into every message your system sends. Each log entry shows the message’s delivery path, status, and any associated errors. This helps you confirm successful sends and troubleshoot failed or delayed deliveries.

Common message statuses include:

* **`SENT`**: The message was successfully handed off to the provider.
* **`DELIVERED`**: The provider confirmed successful delivery to the recipient.
* **`FAILED`**: Delivery was not completed. Review error details to identify the cause.
* **`THROTTLED`**: The message was rate limited or blocked by configured guardrails.

<Note>
  **Message Status Details**: For a full list of message statuses and their definitions, see the [Message Logs documentation](/platform/analytics/message-logs).
</Note>

### Delivery Status Updates via Webhooks

Use webhooks to receive real-time updates when a message’s delivery status changes. Courier sends a `message:updated` event to your configured webhook endpoint each time a message is sent, delivered, failed, or retried.

Webhook events let your application track delivery progress without polling the API. You can use them to update user interfaces, trigger automations, or store delivery data in your own systems.

```json  theme={null}
{
  "type": "message:updated",
  "data": {
    "id": "1-6143cf63-4f27670f6304f465462695f2",
    "status": "DELIVERED",
    "recipient": "c156665c-a76c-4440-9676-f25c1b04ba93",
    "timestamp": "2024-01-15T10:30:00Z"
  }
}
```

<Note>
  **Webhook Setup**: To receive these notifications, you need to configure outbound webhooks in your Courier workspace. Go to [Settings → Outbound Webhooks](https://app.courier.com/settings/general) and add your webhook endpoint URL.

  **Implementation**: Your webhook endpoint should return a 200 response quickly and handle the event data asynchronously. For complete webhook setup instructions, including signature verification and event handling, see [Outbound Webhooks](/platform/workspaces/outbound-webhooks).
</Note>

## Best Practices

### Error Handling

Implement proper error handling for production use:

<CodeGroup>
  ```javascript Node.js theme={null}
  try {
    const { requestId } = await courier.send(messageData);
    console.log(`Message sent successfully: ${requestId}`);
  } catch (error) {
    if (error.statusCode === 429) {
      // Rate limited - implement backoff
      console.log("Rate limited, retrying later...");
    } else if (error.statusCode >= 500) {
      // Server error - retry with exponential backoff
      console.log("Server error, retrying...");
    } else {
      // Client error - check request format
      console.log("Invalid request:", error.message);
    }
  }
  ```

  ```python Python theme={null}
  try:
    response = client.send(message_data)
    print(f"Message sent successfully: {response.request_id}")
  except Exception as error:
    if hasattr(error, 'status_code'):
      if error.status_code == 429:
        # Rate limited - implement backoff
        print("Rate limited, retrying later...")
      elif error.status_code >= 500:
        # Server error - retry with exponential backoff
        print("Server error, retrying...")
      else:
        # Client error - check request format
        print(f"Invalid request: {error.message}")
    else:
      print(f"Unexpected error: {error}")
  ```

  ```ruby Ruby theme={null}
  begin
    res = client.send(message_data)
    puts "Message sent successfully: #{res.request_id}"
  rescue => error
    if error.respond_to?(:status_code)
      case error.status_code
      when 429
        # Rate limited - implement backoff
        puts "Rate limited, retrying later..."
      when 500..599
        # Server error - retry with exponential backoff
        puts "Server error, retrying..."
      else
        # Client error - check request format
        puts "Invalid request: #{error.message}"
      end
    else
      puts "Unexpected error: #{error}"
    end
  end
  ```

  ```php PHP theme={null}
  try {
    $result = $courier->send($messageData);
    echo "Message sent successfully: " . $result->requestId . "\n";
  } catch (Exception $error) {
    if (property_exists($error, 'statusCode')) {
      if ($error->statusCode === 429) {
        // Rate limited - implement backoff
        echo "Rate limited, retrying later...\n";
      } elseif ($error->statusCode >= 500) {
        // Server error - retry with exponential backoff
        echo "Server error, retrying...\n";
      } else {
        // Client error - check request format
        echo "Invalid request: " . $error->getMessage() . "\n";
      }
    } else {
      echo "Unexpected error: " . $error->getMessage() . "\n";
    }
  }
  ```

  ```java Java theme={null}
  try {
    SendMessageResponse response = courier.send(sendMessageRequest);
    System.out.println("Message sent successfully: " + response.getRequestId());
  } catch (Exception error) {
    if (error instanceof CourierException) {
      CourierException courierError = (CourierException) error;
      int statusCode = courierError.getStatusCode();
      
      if (statusCode == 429) {
        // Rate limited - implement backoff
        System.out.println("Rate limited, retrying later...");
      } else if (statusCode >= 500) {
        // Server error - retry with exponential backoff
        System.out.println("Server error, retrying...");
      } else {
        // Client error - check request format
        System.out.println("Invalid request: " + courierError.getMessage());
      }
    } else {
      System.out.println("Unexpected error: " + error.getMessage());
    }
  }
  ```

  ```go Go theme={null}
  response, err := client.SendMessage(context.Background(), messageData)
  if err != nil {
    if courierErr, ok := err.(*courier.CourierError); ok {
      switch courierErr.StatusCode {
      case 429:
        // Rate limited - implement backoff
        log.Println("Rate limited, retrying later...")
      case 500, 502, 503, 504:
        // Server error - retry with exponential backoff
        log.Println("Server error, retrying...")
      default:
        // Client error - check request format
        log.Printf("Invalid request: %s", courierErr.Message)
      }
    } else {
      log.Printf("Unexpected error: %v", err)
    }
    return
  }
  log.Printf("Message sent successfully: %s", response.RequestID)
  ```

  ```csharp C# theme={null}
  try
  {
    var response = await courier.SendAsync(sendMessageRequest);
    Console.WriteLine($"Message sent successfully: {response.RequestId}");
  }
  catch (CourierException error)
  {
    switch (error.StatusCode)
    {
      case 429:
        // Rate limited - implement backoff
        Console.WriteLine("Rate limited, retrying later...");
        break;
      case >= 500:
        // Server error - retry with exponential backoff
        Console.WriteLine("Server error, retrying...");
        break;
      default:
        // Client error - check request format
        Console.WriteLine($"Invalid request: {error.Message}");
        break;
    }
  }
  catch (Exception error)
  {
    Console.WriteLine($"Unexpected error: {error.Message}");
  }
  ```
</CodeGroup>
