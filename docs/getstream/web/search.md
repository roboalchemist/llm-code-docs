# Stream.io Documentation
# Source: https://getstream.io/chat/docs/search/

* [Chat Messaging](/chat/)

/

  * [Docs](/chat/docs/)

/

  * [React](/chat/docs/react/)

/

  * [Message Search](/chat/docs/react/search/)

# Message Search

Search messages across channels using full-text search or specific field
filters. Enable or disable search indexing per channel type in the Stream
Dashboard.

## Searching Messages

Search requires a channel filter and either a text query or message filter
conditions.

JavaScriptKotlinSwiftJavaPythonRubyPHPGoC#Unity

    
    
    // Search for messages containing text
    const results = await client.search(
      { members: { $in: ["john"] } },
      "supercalifragilisticexpialidocious",
      { limit: 10 },
    );
    
    // Search with message filters
    const filtered = await client.search(
      { members: { $in: ["john"] } },
      { text: { $autocomplete: "super" }, attachments: { $exists: true } },
      { limit: 10 },
    );
    
    
    val channelFilter = Filters.eq("cid", "messaging:my-channel")
    val messageFilter = Filters.autocomplete("text", "supercali")
    
    client.searchMessages(
      channelFilter = channelFilter,
      messageFilter = messageFilter,
      limit = 10,
    ).enqueue { result ->
      if (result is Result.Success) {
        val messages: List<Message> = result.value.messages
      } else {
        // Handle Result.Failure
      }
    }
    
    
    let controller = client.messageSearchController()
    controller.loadNextMessages(limit: 10) { error in
      if let error = error {
        // Handle error
      } else {
        let messages = controller.messages
      }
    }
    
    
    var searchResult = Message.search()
      .filterCondition("text", condition)
      .query("supercalifragilisticexpialidocious")
      .limit(10)
      .request();
    
    
    channel_filters = {"cid": "messaging:my-channel"}
    message_filters = {"text": {"$autocomplete": "supercali"}}
    
    page1 = client.search(
      channel_filters,
      message_filters,
      sort=[{"relevance": -1}, {"updated_at": 1}],
      limit=10
    )
    
    
    channel_filters = { cid: 'messaging:my-channel' }
    message_filters = { text: { '$autocomplete': 'supercali' }}
    
    page1 = client.search(
      channel_filters,
      message_filters,
      sort: [{ relevance: -1 }, { updated_at: 1 }],
      limit: 10
    )
    
    
    $response = $serverClient->search(
      $filters,
      'supercalifragilisticexpialidocious',
      ['limit' => 10]
    );
    
    
    resp, err := client.Search(ctx, SearchRequest{
      Query: "supercalifragilisticexpialidocious",
      Filters: map[string]interface{}{
        "members": map[string][]string{
          "$in": {"john"},
        },
      },
      Limit: 10,
    })
    
    
    var response = await messageClient.SearchAsync(SearchOptions.Default
      .WithMessageFilterConditions(new Dictionary<string, object>
      {
        {
          "members", new Dictionary<string, object>
          {
            { "$in", new[] {"john"} },
          }
        },
      })
      .WithQuery("supercalifragilisticexpialidocious")
      .WithLimit(10));
    
    
    var results = await Client.LowLevelClient.MessageApi.SearchMessagesAsync(new SearchRequest
    {
      FilterConditions = new Dictionary<string, object>
      {
        {
          "members", new Dictionary<string, object>
          {
            { "$in", new[] { "John" } }
          }
        }
      },
      Query = "supercalifragilisticexpialidocious",
      Limit = 30
    });
    
    foreach (var searchResult in results.Results)
    {
      Debug.Log(searchResult.Message.Id);
      Debug.Log(searchResult.Message.Text);
      Debug.Log(searchResult.Message.User);
      Debug.Log(searchResult.Message.Channel);
    }

### Query Parameters

Name| Type| Description| Default| Optional  
filter_conditions| object| Channel filters. Maximum 500 channels are searched.
See [Querying Channels](/chat/docs/react/query_channels/).| -|  
message_filter_conditions| object| Message filters. See Message Filter
Conditions below. Either this or `query` is required.| -| â  
query| string| Full-text search string. Equivalent to `{text: {$q: <query>}}`.
Either this or `message_filter_conditions` is required.| -| â  
limit| integer| Number of messages to return.| 100| â  
offset| integer| Pagination offset. Cannot be used with `sort` or `next`.| 0|
â  
sort| object/array| Sort order. Use field names with `1` (ascending) or `-1`
(descending).| [{relevance: -1}, {id: 1}]| â  
next| string| Pagination cursor. See Pagination below.| -| â  
  
### Message Filter Conditions

Field| Description| Operators  
id| Message ID| $eq, $gt, $gte, $lt, $lte, $in  
text| Message text| $q, $autocomplete, $eq, $gt, $gte, $lt, $lte, $in  
type| Message type. System and deleted messages are excluded| $eq, $gt, $gte,
$lt, $lte, $in  
parent_id| Parent message ID (for replies)| $eq, $gt, $gte, $lt, $lte, $in  
reply_count| Number of replies| $eq, $gt, $gte, $lt, $lte, $in  
attachments| Whether message has attachments| $exists, $eq, $gt, $gte, $lt,
$lte, $in  
attachments.type| Attachment type| $eq, $in  
mentioned_users.id| Mentioned user ID| $contains  
user.id| Sender user ID| $eq, $gt, $gte, $lt, $lte, $in  
created_at| Creation timestamp| $eq, $gt, $gte, $lt, $lte, $in  
updated_at| Update timestamp| $eq, $gt, $gte, $lt, $lte, $in  
pinned| Whether message is pinned| $eq  
custom field| Any custom field on the message| $eq, $gt, $gte, $lt, $lte, $in  
  
## Sorting

Results are sorted by relevance by default, with message ID as a tiebreaker.
If your query does not use `$q` or `$autocomplete`, all results are equally
relevant.

Sort by any filterable field, including custom fields. Numeric custom fields
are sorted numerically; string fields are sorted lexicographically.

## Pagination

Two pagination methods are available:

**Offset pagination** allows access to up to 1,000 results. Results are sorted
by relevance and message ID. You cannot use custom sorting with offset
pagination.

**Cursor pagination** (using `next`/`previous`) allows access to all matching
results with custom sorting. The response includes `next` and `previous`
cursors to navigate between pages.

JavaScriptKotlinPythonRubyJavaPHPGoC#Unity

    
    
    const channelFilters = { cid: "messaging:my-channel" };
    const messageFilters = { text: { $autocomplete: "supercali" } };
    
    // First page with custom sorting
    const page1 = await client.search(channelFilters, messageFilters, {
      sort: [{ relevance: -1 }, { updated_at: 1 }, { my_custom_field: -1 }],
      limit: 10,
    });
    
    // Next page using cursor
    const page2 = await client.search(channelFilters, messageFilters, {
      limit: 10,
      next: page1.next,
    });
    
    // Previous page
    const page1Again = await client.search(channelFilters, messageFilters, {
      limit: 10,
      next: page2.previous,
    });
    
    
    val channelFilter = Filters.eq("cid", "messaging:my-channel")
    val messageFilter = Filters.autocomplete("text", "supercali")
    val sort = QuerySortByField.descByName<Message>("relevance")
      .descByName("updatedAt")
      .descByName("my_custom_field")
    
    var nextPage: String? = null
    
    client.searchMessages(
      sort = sort,
      limit = 10,
      channelFilter = channelFilter,
      messageFilter = messageFilter,
    ).enqueue { result ->
      if (result is Result.Success) {
        nextPage = result.value.next
        val messages: List<Message> = result.value.messages
      }
    }
    
    // Next page
    var previousPage: String? = null
    client.searchMessages(
      limit = 10,
      channelFilter = channelFilter,
      messageFilter = messageFilter,
      next = nextPage,
    ).enqueue { result ->
      if (result is Result.Success) {
        previousPage = result.value.previous
        val messages: List<Message> = result.value.messages
      }
    }
    
    // Previous page
    client.searchMessages(
      limit = 10,
      channelFilter = channelFilter,
      messageFilter = messageFilter,
      next = previousPage,
    ).enqueue { /* ... */ }
    
    
    channel_filters = {"cid": "messaging:my-channel"}
    message_filters = {"text": {"$autocomplete": "supercali"}}
    
    # First page
    page1 = client.search(
      channel_filters,
      message_filters,
      sort=[{"relevance": -1}, {"updated_at": 1}, {"my_custom_field": -1}],
      limit=10
    )
    
    # Next page
    page2 = client.search(channel_filters, message_filters, next=page1["next"], limit=10)
    
    # Previous page
    page1_again = client.search(channel_filters, message_filters, next=page2["previous"], limit=10)
    
    
    channel_filters = { cid: 'messaging:my-channel' }
    message_filters = { text: { '$autocomplete': 'supercali' }}
    
    # First page
    page1 = client.search(
      channel_filters,
      message_filters,
      sort: [{ relevance: -1 }, { updated_at: 1 }, { my_custom_field: -1 }],
      limit: 10
    )
    
    # Next page
    page2 = client.search(channel_filters, message_filters, next: page1.next, limit: 10)
    
    # Previous page
    page1_again = client.search(channel_filters, message_filters, next: page2.previous, limit: 10)
    
    
    var searchResult = Message.search()
      .filterCondition("text", condition)
      .query("supercalifragilisticexpialidocious")
      .limit(2)
      .request();
    
    // Next page
    var nextResult = Message.search()
      .filterCondition("text", condition)
      .query("supercalifragilisticexpialidocious")
      .sort(Sort.builder().field("relevance").direction(Sort.Direction.ASC).build())
      .sort(Sort.builder().field("updated_at").direction(Sort.Direction.DESC).build())
      .limit(2)
      .next(searchResult.getNext())
      .request();
    
    
    $response = $serverClient->search(
      $filters,
      'supercalifragilisticexpialidocious',
      ['limit' => 10]
    );
    
    // Next page
    $response = $serverClient->search(
      $filters,
      'supercalifragilisticexpialidocious',
      ['limit' => 10, 'next' => $response['next']]
    );
    
    
    resp, err := client.Search(ctx, SearchRequest{
      Query: "supercalifragilisticexpialidocious",
      Filters: map[string]interface{}{
        "members": map[string][]string{
          "$in": {"john"},
        },
      },
      Limit: 10,
    })
    
    // Next page
    client.SearchWithFullResponse(ctx, SearchRequest{
      Query: "supercalifragilisticexpialidocious",
      Filters: map[string]interface{}{
        "members": map[string][]string{
          "$in": {"john"},
        },
      },
      Next: resp.Next,
      Limit: 10,
    })
    
    
    var response = await messageClient.SearchAsync(SearchOptions.Default
      .WithMessageFilterConditions(new Dictionary<string, object>
      {
        {
          "members", new Dictionary<string, object>
          {
            { "$in", new[] {"john"} },
          }
        },
      })
      .WithQuery("supercalifragilisticexpialidocious")
      .WithLimit(10));
    
    // Next page
    response = await messageClient.SearchAsync(SearchOptions.Default
      .WithMessageFilterConditions(new Dictionary<string, object>
      {
        {
          "members", new Dictionary<string, object>
          {
            { "$in", new[] {"john"} },
          }
        },
      })
      .WithQuery("supercalifragilisticexpialidocious")
      .WithLimit(10)
      .WithNext(response.Next));
    
    
    // First page
    var resultsPage1 = await Client.LowLevelClient.MessageApi.SearchMessagesAsync(new SearchRequest
    {
      FilterConditions = new Dictionary<string, object>
      {
        {
          "members", new Dictionary<string, object>
          {
            { "$in", new[] { "John" } }
          }
        }
      },
      Query = "supercalifragilisticexpialidocious",
      Limit = 30
    });
    
    // Next page
    var resultsPage2 = await Client.MessageApi.SearchMessagesAsync(new SearchRequest
    {
      FilterConditions = new Dictionary<string, object>
      {
        {
          "members", new Dictionary<string, object>
          {
            { "$in", new[] { "John" } }
          }
        }
      },
      Next = resultsPage1.Next,
      Query = "supercalifragilisticexpialidocious",
      Limit = 30
    });

Did you find this page helpful?

It was helpful

It was not helpful

I have feedback

Submit

Thank you for the feedback.

An error has occurred. Please refresh the page and try again.

[PreviousPinned Messages](/chat/docs/react/pinned_messages/)[NextSilent &
System Messages](/chat/docs/react/silent_messages/)

Â© Stream.io, Inc. All Rights Reserved.

[Chat Messaging](https://getstream.io/chat/)[Video &
Audio](https://getstream.io/video/)[Activity
Feeds](https://getstream.io/activity-
feeds/)[Moderation](https://getstream.io/moderation/)

  * Copy LLM prompt
  * [ View as markdown](https://getstream.io/chat/docs/react/search.md)
  *   * [ Open in ChatGPT](https://chatgpt.com/?q=I'm working with the Stream Chat React SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/react/search.md)
  * [ Open in Claude](https://claude.ai/new?q=I'm working with the Stream Chat React SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/react/search.md)
  * [ Open in Gemini](https://gemini.google.com/app?query=I'm working with the Stream Chat React SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/react/search.md)
  * [ Open in Grok](https://x.com/i/grok?text=I'm working with the Stream Chat React SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/react/search.md)
  * [ Open in Perplexity](https://www.perplexity.ai/search/new?q=I'm working with the Stream Chat React SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/react/search.md)

On this page:

  * Searching Messages

    * Query Parameters
    * Message Filter Conditions

  * Sorting
  * Pagination

Is this helpful?

Thank you .

An error has occurred.