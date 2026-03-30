# Perplexity API Documentation Update - 2026-02-16

## Summary

Successfully updated Perplexity API documentation from the latest llms-full.txt source. The update reorganized the documentation structure with improved file naming conventions and added several new API features.

## Source Information

- **Source URL**: https://docs.perplexity.ai/llms-full.txt
- **Download Date**: 2026-02-16
- **Original Size**: 23,216 lines
- **Full Documentation File**: perplexity-full.md

## Documentation Statistics

- **Total Files**: 92 individual markdown files
- **Total Size**: 1.3 MB
- **Files Removed**: 18 (consolidated or renamed)
- **Files Added**: 27 new files
- **Files Updated**: 47 files with refreshed content

## Key Changes and New Features Added

### New API Endpoints

1. **Embeddings APIs**
   - `POST /v1/embeddings` - Create embeddings for texts
   - `POST /v1/contextualizedembeddings` - Create contextualized embeddings
   - Standard embeddings API documentation
   - Contextualized embeddings for document-based applications

2. **Improved Async Operations**
   - `GET /async/chat/completions/{api_request}` - Retrieve async chat completion
   - `GET /async/chat/completions` - List async chat completions
   - `POST /async/chat/completions` - Create async chat completion

### New Documentation Sections

- Agent API comprehensive guide
- API Groups and Billing documentation
- API Roadmap (updated feature planning)
- Media Attachments API reference
- Memory Management for persistent chat
- Chat Summary Memory Buffer
- Persistent Chat Memory
- OpenAI Agents Integration
- OpenAI SDK Compatibility
- Output Control documentation
- Built-in Tool Capabilities
- Pro Search Classifier
- Stream Mode (Concise vs Full) guide
- System Status page

### Enhanced Sections

- API Key Management (expanded with rotation features)
- Best Practices (comprehensive guide)
- Configuration (updated settings)
- Error Handling (detailed error codes)
- Performance Optimization (refined guidance)
- Rate Limits and Usage Tiers (tier-based limits clarification)
- Pricing documentation
- Quickstart guide
- Changelog (complete update history)
- Frequently Asked Questions

### Improved File Naming

All files now use consistent lowercase hyphenated naming:
- `4point-Hoops.md` → `4point-hoops-ai-basketball-analytics-platform.md`
- `briefo.md` → `briefo-perplexity-powered-news-finance-social-app.md`
- `faq.md` → `frequently-asked-questions.md`
- `status.md` → `system-status.md`

### Example Applications Updated

- 4Point Hoops AI Basketball Analytics Platform
- Ellipsis - One-Click Podcast Generation Agent
- BazaarAISaathi - AI Powered Indian Stock Market Assistant
- Briefo - Perplexity Powered News/Finance/Social App
- CityPulse AI - Powered Geospatial Discovery Search
- CycleSyncAI - Personalized Health Plans
- Daily Knowledge Bot
- Disease Information App
- Executive Intelligence - Strategic Decision Platform
- Fact Checker CLI
- Financial News Tracker
- Academic Research Finder CLI
- And many more...

## File Organization

Files are organized by functionality:
- **Core APIs**: async-chat, chat-completion, embeddings, responses, search
- **Authentication**: auth-token, key management, API groups
- **Filters & Search**: date-time filters, domain filters, search modes
- **Configuration**: configuration, rate limits, models, presets
- **Performance**: optimization, best practices, type safety
- **Integrations**: langchain, MCP server, OpenAI SDK
- **Examples**: cookbook, example apps

## Index Update

- Index file regenerated with 628 total sources
- 342 llms.txt sites documented
- 149 GitHub-sourced repositories
- 137 web-scraped sources
- Perplexity entry: 92 files, 1.3MB

## Verification

- All files contain proper `Source: URL` headers
- No corrupted or truncated files
- No null/empty sections
- Consistent formatting across all files
- All source URLs point to official Perplexity documentation

## Git Commit

- **Commit Hash**: 39beb3f4b
- **Files Changed**: 169 (deletions and additions)
- **Net Change**: +23,888 insertions, -54,379 deletions
- **Branch**: master
- **Status**: Pushed to remote

## Next Steps

The documentation is now up-to-date and ready for LLM consumption. To keep this current:
- Re-run `python3 scripts/llms-txt-scraper.py --site perplexity --force` to refresh periodically
- Monitor Perplexity's changelog for new features
- Update index with `python3 scripts/update-index.py` after any changes
