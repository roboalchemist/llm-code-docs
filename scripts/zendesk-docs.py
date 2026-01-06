#!/usr/bin/env python3
"""
Scraper for Zendesk Developer Documentation.
Output: docs/web-scraped/zendesk/

Extracts documentation from developer.zendesk.com including:
- API references
- Product documentation
- SDKs and guides
- Integration documentation
"""

import requests
from pathlib import Path
from urllib.parse import urljoin, urlparse
import json
from html.parser import HTMLParser
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "zendesk"
BASE_URL = "https://developer.zendesk.com"
SESSION = requests.Session()
SESSION.headers.update({
    'User-Agent': 'Mozilla/5.0 (compatible; DocumentationBot/1.0)'
})

# Rate limiting
RATE_LIMIT_DELAY = 0.5  # seconds between requests

class DocumentationExtractor(HTMLParser):
    """Extract main content from Zendesk documentation pages."""

    def __init__(self):
        super().__init__()
        self.in_main = False
        self.in_script = False
        self.in_style = False
        self.content = []
        self.title = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'title':
            pass
        elif tag in ['script', 'style']:
            self.__dict__[f'in_{tag}'] = True
        elif tag in ['main', 'article'] or (tag == 'div' and 'main' in attrs_dict.get('class', '')):
            self.in_main = True
        elif tag == 'h1' and not self.in_script and not self.in_style:
            self.content.append('\n# ')
        elif tag in ['h2'] and not self.in_script and not self.in_style:
            self.content.append('\n## ')
        elif tag in ['h3'] and not self.in_script and not self.in_style:
            self.content.append('\n### ')
        elif tag == 'p' and not self.in_script and not self.in_style:
            self.content.append('\n')
        elif tag == 'code' and not self.in_script and not self.in_style:
            self.content.append('`')
        elif tag == 'pre' and not self.in_script and not self.in_style:
            self.content.append('\n```\n')
        elif tag in ['li', 'dd'] and not self.in_script and not self.in_style:
            self.content.append('\n- ')
        elif tag == 'br' and not self.in_script and not self.in_style:
            self.content.append('\n')

    def handle_endtag(self, tag):
        if tag in ['script', 'style']:
            self.__dict__[f'in_{tag}'] = False
        elif tag in ['main', 'article']:
            self.in_main = False
        elif tag == 'code' and not self.in_script and not self.in_style:
            self.content.append('`')
        elif tag == 'pre' and not self.in_script and not self.in_style:
            self.content.append('\n```\n')
        elif tag in ['p', 'li', 'dd', 'h1', 'h2', 'h3']:
            self.content.append('\n')

    def handle_data(self, data):
        if not self.in_script and not self.in_style:
            text = data.strip()
            if text:
                self.content.append(text + ' ')

    def get_text(self):
        text = ''.join(self.content)
        # Clean up multiple newlines
        while '\n\n\n' in text:
            text = text.replace('\n\n\n', '\n\n')
        return text.strip()


def fetch_page(url):
    """Fetch and extract text from a page."""
    try:
        logger.info(f"Fetching: {url}")
        response = SESSION.get(url, timeout=10)
        response.raise_for_status()

        parser = DocumentationExtractor()
        parser.feed(response.text)

        return parser.get_text()
    except Exception as e:
        logger.error(f"Error fetching {url}: {e}")
        return None


def get_documentation_pages():
    """Get list of key documentation pages to scrape."""
    pages = {
        # API Basics
        "api-basics.md": f"{BASE_URL}/documentation/api-basics/",

        # Core APIs
        "ticketing-api.md": f"{BASE_URL}/api-reference/ticketing/",
        "help-center-api.md": f"{BASE_URL}/api-reference/help_center/",
        "conversations-api.md": f"{BASE_URL}/api-reference/conversations/",
        "voice-api.md": f"{BASE_URL}/api-reference/voice/",
        "chat-api.md": f"{BASE_URL}/api-reference/chat/",
        "sell-api.md": f"{BASE_URL}/api-reference/sell/",
        "ai-agents-api.md": f"{BASE_URL}/api-reference/ai-agents/",

        # SDKs and Widgets
        "web-widget-sdk.md": f"{BASE_URL}/documentation/zendesk-web-widget-sdks/",

        # Integration
        "webhooks.md": f"{BASE_URL}/documentation/webhooks/",
        "apps.md": f"{BASE_URL}/documentation/apps/",
        "integration-services.md": f"{BASE_URL}/documentation/integration-services/",

        # Custom Data
        "custom-objects.md": f"{BASE_URL}/documentation/custom-data/",

        # Product Documentation
        "ticketing.md": f"{BASE_URL}/documentation/ticketing/",
        "help-center.md": f"{BASE_URL}/documentation/help_center/",
        "live-chat.md": f"{BASE_URL}/documentation/live-chat/",
        "sales-crm.md": f"{BASE_URL}/documentation/sales-crm/",
    }
    return pages


def create_index():
    """Create an index markdown file."""
    index_content = """# Zendesk Developer Documentation

Source: https://developer.zendesk.com/

Zendesk is a customer service and support platform offering:
- Ticketing system (Support)
- Help Center for knowledge bases
- Live Chat and messaging
- Voice/Call center (Talk)
- Sales CRM (Sell)
- Conversational AI agents
- Multi-channel messaging (Conversations)
- Custom data and objects
- Integration APIs and webhooks
- Web widgets and SDKs

## Key Sections

### API Documentation
- **Ticketing API** - Manage tickets, users, organizations
- **Help Center API** - Manage knowledge base articles and communities
- **Conversations API** - Multi-channel messaging
- **Voice/Talk API** - Call center and voice
- **Chat API** - Live chat messaging
- **Sell API** - Sales CRM automation
- **AI Agents API** - Conversational AI and automation

### SDKs & Widgets
- Web Widget SDK
- Mobile SDKs (iOS, Android, Unity)
- Classic Web Widget

### Integrations
- Webhooks - Real-time event notifications
- Apps - Custom applications
- Integration Services
- Amazon EventBridge
- Channel Framework

### Authentication
All APIs use OAuth 2.0 or API token authentication.

## Documentation Files

- `api-basics.md` - Core API concepts and authentication
- `ticketing-api.md` - Support ticketing API reference
- `help-center-api.md` - Knowledge base and community API
- `conversations-api.md` - Multi-channel messaging API
- `voice-api.md` - Voice and call center API
- `chat-api.md` - Live chat API
- `sell-api.md` - Sales CRM API
- `ai-agents-api.md` - Conversational AI API
- `web-widget-sdk.md` - Web widget and SDK documentation
- `webhooks.md` - Event webhooks and integrations
- `apps.md` - Custom app development
- `integration-services.md` - Integration platform
- `custom-objects.md` - Custom data objects API
- `ticketing.md` - Support product documentation
- `help-center.md` - Help center product guide
- `live-chat.md` - Live chat product guide
- `sales-crm.md` - Sales CRM product documentation

## Getting Started

1. Create a Zendesk account at https://www.zendesk.com
2. Obtain API credentials from Admin > Channels & integrations > APIs
3. Review API basics for authentication patterns
4. Check specific API reference for your use case
5. Explore SDKs for your platform (Web, Mobile, etc.)

For complete documentation, visit: https://developer.zendesk.com/
"""
    return index_content


def scrape_documentation():
    """Scrape all documentation pages."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    logger.info(f"Scraping Zendesk documentation to {OUTPUT_DIR}")

    pages = get_documentation_pages()
    scraped_count = 0

    for filename, url in pages.items():
        content = fetch_page(url)

        if content:
            filepath = OUTPUT_DIR / filename
            filepath.write_text(f"# Source: {url}\n\n{content}\n")
            logger.info(f"Saved: {filename}")
            scraped_count += 1

        time.sleep(RATE_LIMIT_DELAY)

    # Create index
    index_content = create_index()
    index_path = OUTPUT_DIR / "INDEX.md"
    index_path.write_text(index_content)
    logger.info(f"Saved: INDEX.md")

    logger.info(f"\nCompleted! Scraped {scraped_count} pages + index")
    logger.info(f"Output: {OUTPUT_DIR}")


if __name__ == "__main__":
    scrape_documentation()
