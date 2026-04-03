#!/usr/bin/env python3
"""
Fetch HATEOAS documentation from multiple sources:
- Spring HATEOAS official docs
- RESTful API best practices guide
"""

import httpx
import re
from pathlib import Path
from typing import Optional

def extract_text_from_html(html: str) -> str:
    """Simple HTML to text extraction using regex."""
    # Remove script and style tags
    html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove HTML tags but keep content
    html = re.sub(r'<[^>]+>', '\n', html)
    
    # Clean up whitespace
    lines = [line.strip() for line in html.split('\n') if line.strip()]
    return '\n'.join(lines)

def fetch_spring_hateoas() -> Optional[str]:
    """Fetch Spring HATEOAS documentation."""
    try:
        resp = httpx.get(
            'https://docs.spring.io/spring-hateoas/docs/1.2.1/reference/html/',
            timeout=15,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        if resp.status_code == 200:
            # Extract meaningful text content
            text = extract_text_from_html(resp.text)
            # Filter to Spring-specific HATEOAS content
            if 'EntityModel' in text or 'LinkBuilder' in text or 'Spring HATEOAS' in text:
                return text
    except Exception as e:
        print(f"Error fetching Spring HATEOAS: {e}")
    return None

def fetch_restfulapi_hateoas() -> Optional[str]:
    """Fetch RESTful API HATEOAS guide."""
    try:
        resp = httpx.get(
            'https://restfulapi.net/hateoas/',
            timeout=15,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        if resp.status_code == 200:
            text = extract_text_from_html(resp.text)
            if 'HATEOAS' in text or 'hypermedia' in text:
                return text
    except Exception as e:
        print(f"Error fetching restfulapi.net: {e}")
    return None

def main():
    output_dir = Path('docs/web-scraped/hateoas')
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("Fetching Spring HATEOAS documentation...")
    spring_content = fetch_spring_hateoas()
    
    print("Fetching RESTful API HATEOAS guide...")
    restful_content = fetch_restfulapi_hateoas()
    
    if spring_content:
        with open(output_dir / '001-spring-hateoas.md', 'w') as f:
            f.write('# Source: https://docs.spring.io/spring-hateoas/docs/current/reference/html/\n\n')
            f.write(spring_content[:50000])  # Limit size
        print(f"✓ Saved Spring HATEOAS content")
    
    if restful_content:
        with open(output_dir / '002-restfulapi-guide.md', 'w') as f:
            f.write('# Source: https://restfulapi.net/hateoas/\n\n')
            f.write(restful_content[:50000])  # Limit size
        print(f"✓ Saved RESTful API HATEOAS guide")

if __name__ == '__main__':
    main()
