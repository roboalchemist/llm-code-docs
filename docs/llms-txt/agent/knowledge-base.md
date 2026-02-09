# Source: https://docs.agent.ai/knowledge-agents/knowledge-base.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Knowledge Base

> Train your knowledge agent with custom knowledge from documents, websites, videos, and more

## What is a Knowledge Base?

A knowledge base is the collection of information your knowledge agent can search and reference when answering questions or making decisions. Think of it as your agent's memory - the more relevant knowledge you add, the more helpful and accurate your agent becomes.

Unlike traditional chatbots that only know what they were trained on, knowledge agents use **Retrieval Augmented Generation (RAG)** to dynamically search your knowledge and incorporate it into responses.

## How Knowledge Retrieval Works (RAG Simplified)

Here's what happens when someone asks your knowledge agent a question:

```
User asks: "What's our refund policy?"
        ↓
Agent converts question to a search query
        ↓
Searches knowledge base for relevant content
        ↓
Finds: "Refund Policy.pdf" - page 2, section 3
        ↓
AI reads the relevant section
        ↓
Generates answer using that specific information
        ↓
Responds: "According to our refund policy, customers can..."
```

**Key point:** Your agent doesn't memorize everything - it searches and retrieves relevant pieces on-demand. This means:

* You can add lots of knowledge without "retraining"
* Answers come from your actual documents
* You can update knowledge anytime
* Agent cites sources (useful for verification)

## Supported Knowledge Sources

You can train your knowledge agent with six types of content:

| Source Type       | What It's For                      | Processing Time |
| ----------------- | ---------------------------------- | --------------- |
| **Files**         | PDFs, Word docs, text files        | 10-30 seconds   |
| **URLs**          | Web pages, articles, documentation | 15-45 seconds   |
| **YouTube**       | Video transcripts                  | 20-60 seconds   |
| **Google Docs**   | Workspace documents                | 10-30 seconds   |
| **Google Sheets** | Spreadsheet data                   | 10-30 seconds   |
| **Twitter/X**     | Tweets and threads                 | 15-45 seconds   |
| **LinkedIn**      | Profiles and posts                 | 20-60 seconds   |

All sources are automatically:

* Chunked into searchable segments
* Embedded as vectors for semantic search
* Stored in your agent's vector database
* Instantly available for retrieval

## Adding Knowledge: Step-by-Step

### Files (PDF, DOCX, TXT)

**Best for:** Documentation, reports, guides, research papers

**How to add:**

1. Navigate to your knowledge agent builder
2. Click the **"Training"** tab
3. Click the **"Files"** sub-tab
4. Click **"Upload"** or drag and drop files
5. Wait for processing (progress bar shows status)
6. File appears in the list when ready

**Supported formats:**

* PDF (.pdf)
* Microsoft Word (.doc, .docx)
* Plain text (.txt)
* Markdown (.md)

**Tips:**

* PDFs work best when they contain actual text (not scanned images)
* Remove unnecessary pages to improve relevance
* File names help the agent understand context - use descriptive names

<Warning>
  **File size limit:** 25MB per file. For larger documents, consider splitting them or using a URL if the content is available online.
</Warning>

### Web URLs

**Best for:** Websites, blog posts, online documentation, public articles

**How to add:**

1. Go to the **"Training"** tab
2. Click the **"URLs"** sub-tab
3. Paste the full URL (starting with https\://)
4. Click **"Add URL"**
5. Content is scraped and processed automatically

**What gets extracted:**

* Main text content from the page
* Headings and structure
* Some metadata (title, author if available)
* **Not extracted:** Images, videos, interactive elements

**Special handling:**

**Google Docs:**

* Paste the sharing link (make sure it's accessible via link)
* Agent automatically exports to readable format
* Formatting is preserved

**Google Sheets:**

* Paste the sharing link
* Data is exported and indexed
* Useful for product catalogs, pricing, data tables

<Tip>
  **Pro tip:** For documentation sites with many pages, add the most important/overview pages. You don't need every single page - the agent will direct users based on what you've added.
</Tip>

### YouTube Videos

**Best for:** Tutorials, presentations, interviews, educational content

**How to add:**

1. Go to the **"Training"** tab
2. Click the **"YouTube Videos"** sub-tab
3. Paste the YouTube video URL
4. Click **"Add Video"**
5. Agent automatically extracts the transcript

**What gets indexed:**

* Full transcript of spoken words
* Video title and description
* Channel information
* Key moments/chapters (if available)

**Important notes:**

* Video must have captions/subtitles (auto-generated works)
* Videos without transcripts cannot be processed
* Transcript language is auto-detected

**Use cases:**

* Index your tutorial videos so agent can answer "how-to" questions
* Add conference talks or presentations
* Include product demos or walkthroughs
* Reference expert interviews or talks

### Twitter/X Posts

**Best for:** Twitter threads, announcements, thought leadership content

**How to add:**

1. Go to the **"Training"** tab
2. Click the **"Twitter"** sub-tab
3. Enter a Twitter username (without @) or paste a tweet URL
4. Click **"Add"**

**What gets indexed:**

* Tweet text content
* Thread structure (if it's a thread)
* Author information
* Timestamps

**Use cases:**

* Add your own tweets to train agent on your thinking
* Include industry expert threads
* Reference announcement tweets
* Capture Twitter-based discussions

### LinkedIn Content

**Best for:** Professional profiles, thought leadership posts, company updates

**How to add:**

1. Go to the **"Training"** tab
2. Click the **"LinkedIn"** sub-tab
3. Enter a LinkedIn profile URL or post URL
4. Click **"Add"**

**What gets indexed:**

* Profile headline and about section
* Recent posts and articles
* Experience and background (for profiles)
* Post content and engagement

**Use cases:**

* Add your LinkedIn profile to train agent on your expertise
* Include company LinkedIn posts
* Reference industry leader profiles
* Capture professional insights and articles

## Managing Your Knowledge Base

### Viewing Your Knowledge

In the **Training** tab, you'll see all your knowledge sources listed with:

* Source name/title
* Type (file, URL, video, etc.)
* Upload date
* Processing status
* File size or length

### Refreshing Content

For URLs, YouTube videos, and social media sources, you can refresh the content to get updates:

1. Find the source in the list
2. Click the **refresh icon** next to it
3. Agent re-fetches and re-processes the content
4. Updated content replaces the old version

**When to refresh:**

* Documentation has been updated
* YouTube video captions were improved
* Twitter thread was extended
* Website content changed

<Note>
  **Files can't be refreshed** - you'll need to delete and re-upload if you have a newer version.
</Note>

### Deleting Knowledge

To remove a knowledge source:

1. Find it in the Training tab list
2. Click the **delete icon** (trash can)
3. Confirm deletion
4. Source is removed immediately from knowledge base

**Important:** Deleting knowledge affects all future conversations. Past conversations won't change, but new chats won't have access to that information anymore.

### Organizing Your Knowledge

While there's no folder structure, you can organize by:

* Using clear, descriptive file names
* Adding related content in batches
* Keeping a separate document tracking what you've added
* Deleting outdated content regularly

## Knowledge Base Best Practices

### Quality Over Quantity

**Don't do this:**

* Upload hundreds of barely relevant documents
* Add your entire website including footer text and navigation
* Include duplicate or very similar content
* Add content "just in case"

**Do this instead:**

* Curate high-quality, relevant sources
* Include core documentation and key resources
* Remove or don't include boilerplate/duplicate content
* Think "What do users actually need to know?"

**Why:** Too much irrelevant content can actually hurt performance. The agent might retrieve less relevant chunks if there's too much noise.

### Keep Content Fresh

* **Review quarterly:** Check if knowledge is still accurate
* **Update when things change:** New product features, policy changes, etc.
* **Remove outdated info:** Delete deprecated content
* **Refresh URLs:** Re-fetch content from living documents

### Structure Matters

**Good knowledge sources:**

* Well-organized with clear headings
* Use bullet points and lists
* Have logical flow
* Include examples and specifics

**Poor knowledge sources:**

* Wall of text with no structure
* Overly vague or general
* Lots of irrelevant tangents
* Poorly formatted (weird spacing, encoding issues)

### Match Your Use Case

**For Q\&A agents:**

* Add FAQs, help docs, policies
* Include troubleshooting guides
* Add product documentation

**For research agents:**

* Add research papers and reports
* Include industry analysis
* Add expert content and thought leadership

**For task-oriented agents:**

* Add process documentation
* Include how-to guides
* Add standard operating procedures

### Test Your Knowledge

After adding knowledge, test if the agent can retrieve it:

1. Ask direct questions from the content
2. Ask questions that require combining multiple sources
3. Try edge cases or less obvious questions
4. Check if sources are cited correctly

**If retrieval isn't working:**

* Question may not match terminology in knowledge
* Content may be too scattered or vague
* May need more (or different) context
* Try rephrasing the question

## Troubleshooting Knowledge Issues

<AccordionGroup>
  <Accordion title="Agent isn't using my knowledge">
    **Symptoms:** Agent gives generic answers instead of using uploaded content

    **Possible causes:**

    1. Knowledge still processing (check for status indicator)
    2. Question doesn't semantically match content
    3. System prompt doesn't encourage knowledge use
    4. Content is too vague or poorly structured

    **Solutions:**

    * Wait for all files to finish processing
    * Ask questions more directly related to your content
    * Update system prompt: "Always search your knowledge base first"
    * Restructure content with clear headings and sections
    * Try asking: "What do you know about \[topic from your knowledge]?"
  </Accordion>

  <Accordion title="Agent retrieves wrong or irrelevant knowledge">
    **Symptoms:** Agent cites sources but they're not relevant to the question

    **Possible causes:**

    1. Knowledge base has too much content
    2. Multiple sources with similar but different info
    3. Content lacks clear topic markers
    4. Semantic search matching wrong chunks

    **Solutions:**

    * Remove less relevant sources
    * Add more specific/targeted knowledge
    * Use clearer headings in source documents
    * Be more specific in questions
    * Consider splitting large documents into focused pieces
  </Accordion>

  <Accordion title="Upload fails or gets stuck">
    **Symptoms:** File upload never completes or shows error

    **Possible causes:**

    1. File too large (>25MB limit)
    2. File format not supported
    3. File is corrupted or password-protected
    4. Network connection issue

    **Solutions:**

    * Check file size (compress or split if too large)
    * Convert to supported format (PDF, DOCX, TXT)
    * Remove password protection
    * Try uploading again with stable connection
    * For large documents, try URL if available online
  </Accordion>

  <Accordion title="YouTube video transcript not extracting">
    **Symptoms:** Error when adding YouTube video

    **Possible causes:**

    1. Video doesn't have captions/transcripts
    2. Video is private or age-restricted
    3. Captions are disabled by creator
    4. Invalid YouTube URL

    **Solutions:**

    * Check if video has captions (watch on YouTube first)
    * Use public, unrestricted videos
    * Ensure URL is correct YouTube format
    * Try a different video if captions unavailable
  </Accordion>

  <Accordion title="Google Docs/Sheets not loading">
    **Symptoms:** Can't add Google Workspace content

    **Possible causes:**

    1. Sharing settings not set to "Anyone with the link"
    2. Document is private
    3. Requires authentication to access
    4. Invalid share link

    **Solutions:**

    * Change sharing to "Anyone with the link can view"
    * Copy the full sharing URL (should have /edit or /view)
    * Make sure document isn't restricted to your organization
    * Test link in incognito browser to verify public access
  </Accordion>

  <Accordion title="How do I know which knowledge was used?">
    **Answer:** As a builder, when you test your knowledge agent, you can see knowledge retrieval:

    * Look for **\[file search]** indicator in responses
    * Agent may cite sources in its answer
    * Some responses show which documents were referenced

    For end users, citations depend on how you've prompted the agent. You can encourage citations in system instructions: "Always cite which document you used."
  </Accordion>
</AccordionGroup>

## Knowledge Base Limits

**Per agent:**

* No hard limit on number of sources
* Recommended: 50-100 high-quality sources for best performance
* Each file limited to 25MB

**Processing:**

* Files process individually (can upload multiple at once)
* URLs are processed on-demand
* Large knowledge bases may have slightly slower retrieval

**Storage:**

* Knowledge is stored in vector database
* Counts toward your plan's storage limits
* Deleted knowledge is removed from storage

## Advanced Tips

<Tip>
  **Create a "master FAQ" document**

  Instead of uploading 20 separate PDFs, create one well-structured FAQ document with all common questions. Use clear headings like "## Pricing Questions" and "## Feature Questions". This helps retrieval accuracy.
</Tip>

<Tip>
  **Use knowledge categories**

  Name your files descriptively and consider prefixes:

  * "\[POLICY] Refund Policy.pdf"
  * "\[GUIDE] Getting Started Guide.pdf"
  * "\[FAQ] Common Questions.pdf"

  This helps both you and the agent understand context.
</Tip>

<Tip>
  **Test with "knowledge audit" questions**

  After adding knowledge, ask: "What do you know about \[topic]?" or "What information do you have about \[subject]?" This shows you what the agent can access.
</Tip>

<Tip>
  **Combine sources for depth**

  For comprehensive topics, add multiple source types:

  * Documentation (files)
  * Tutorial video (YouTube)
  * FAQ page (URL)
  * Expert thread (Twitter)

  This gives the agent multiple perspectives and formats.
</Tip>

<Tip>
  **Keep a knowledge changelog**

  Track what you've added and when. This helps you:

  * Remember what's in the knowledge base
  * Know when content was last updated
  * Identify gaps in coverage
  * Plan future additions
</Tip>

## Next Steps

Now that you understand the knowledge base system:

<CardGroup cols={2}>
  <Card title="Configure Your Agent" icon="sliders" href="/knowledge-agents/configuration">
    Write system prompts that encourage knowledge use
  </Card>

  <Card title="Add Tools" icon="wrench" href="/knowledge-agents/tools-integration">
    Combine knowledge with action-taking capabilities
  </Card>

  <Card title="Best Practices" icon="star" href="/knowledge-agents/best-practices">
    Learn optimization strategies for knowledge bases
  </Card>

  <Card title="Troubleshooting" icon="triangle-exclamation" href="/knowledge-agents/troubleshooting">
    Solve common knowledge retrieval issues
  </Card>
</CardGroup>

<Note>
  **Remember:** Your knowledge base is living and evolving. Start with core content, test with real questions, and continuously refine based on what works. Quality, relevance, and organization matter more than quantity.
</Note>
