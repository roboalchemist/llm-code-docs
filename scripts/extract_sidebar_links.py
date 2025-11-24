#!/usr/bin/env python3
"""
Script to extract all sidebar navigation links from Claude Code SDK documentation.
Scrapes the sidebar from https://docs.anthropic.com/en/docs/claude-code/sdk
and compares with existing links to verify completeness and detect new docs.
"""

import requests
from bs4 import BeautifulSoup
from pathlib import Path
import sys
from urllib.parse import urljoin, urlparse
import time

def extract_sidebar_links(url, timeout=10):
    """Extract all sidebar navigation links from the documentation page."""
    try:
        print(f"Fetching page: {url}")
        
        # Add headers to mimic a real browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, timeout=timeout, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Look for sidebar navigation elements
        # Try multiple possible sidebar selectors
        sidebar_selectors = [
            'nav[aria-label*="Sidebar"]',  # Common pattern
            '.sidebar-nav',
            '.docs-sidebar',
            '.navigation-sidebar',
            '[data-testid*="sidebar"]',
            '.sidebar',
            'nav.sidebar',
            'aside nav',
            '.docs-nav'
        ]
        
        sidebar_links = set()
        base_url = 'https://docs.anthropic.com'
        
        # Try each selector until we find content
        for selector in sidebar_selectors:
            sidebar = soup.select(selector)
            if sidebar:
                print(f"Found sidebar using selector: {selector}")
                
                # Extract all links from the sidebar
                for link in sidebar[0].find_all('a', href=True):
                    href = link.get('href')
                    if href:
                        # Convert relative URLs to absolute
                        full_url = urljoin(base_url, href)
                        
                        # Only include Claude Code documentation links ending in .md
                        if '/docs/claude-code/' in full_url and full_url.endswith('.md'):
                            sidebar_links.add(full_url)
                
                if sidebar_links:
                    break
        
        # If no specific sidebar found, try to find all navigation links
        if not sidebar_links:
            print("No sidebar found with specific selectors, trying general navigation links...")
            
            # Look for any navigation elements that might contain docs links
            nav_elements = soup.find_all(['nav', 'ul', 'div'], class_=lambda x: x and any(
                term in str(x).lower() for term in ['nav', 'menu', 'sidebar', 'toc', 'docs']
            ))
            
            for nav in nav_elements:
                links = nav.find_all('a', href=True)
                for link in links:
                    href = link.get('href')
                    if href:
                        full_url = urljoin(base_url, href)
                        if '/docs/claude-code/' in full_url and full_url.endswith('.md'):
                            sidebar_links.add(full_url)
        
        return sorted(list(sidebar_links))
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return []
    except Exception as e:
        print(f"Error parsing page: {e}")
        return []

def load_existing_links(file_path):
    """Load existing links from the links file."""
    links = []
    if Path(file_path).exists():
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and line.startswith('http'):
                    links.append(line)
    return sorted(links)

def compare_links(extracted_links, existing_links):
    """Compare extracted links with existing links."""
    extracted_set = set(extracted_links)
    existing_set = set(existing_links)
    
    # Find differences
    new_links = extracted_set - existing_set
    missing_links = existing_set - extracted_set
    common_links = extracted_set & existing_set
    
    return {
        'new_links': sorted(list(new_links)),
        'missing_links': sorted(list(missing_links)),
        'common_links': sorted(list(common_links)),
        'total_extracted': len(extracted_links),
        'total_existing': len(existing_links)
    }

def save_extracted_links(links, output_file):
    """Save extracted links to a file."""
    with open(output_file, 'w') as f:
        for link in sorted(links):
            f.write(f"{link}\n")
    print(f"Extracted links saved to: {output_file}")

def main():
    """Main function to extract and compare sidebar links."""
    
    # Configuration
    docs_url = "https://docs.anthropic.com/en/docs/claude-code/sdk"
    existing_links_file = "claude-code-sdk-links.txt"
    extracted_links_file = "extracted-sidebar-links.txt"
    
    print("Claude Code SDK Documentation Link Extractor")
    print("=" * 50)
    print()
    
    # Extract links from the sidebar
    print("Step 1: Extracting sidebar links...")
    extracted_links = extract_sidebar_links(docs_url)
    
    if not extracted_links:
        print("❌ Failed to extract any links from the sidebar!")
        print("This could mean:")
        print("  - The page structure has changed")
        print("  - Network connectivity issues")
        print("  - The sidebar uses JavaScript to load content")
        sys.exit(1)
    
    print(f"✅ Extracted {len(extracted_links)} links from sidebar")
    print()
    
    # Save extracted links
    save_extracted_links(extracted_links, extracted_links_file)
    print()
    
    # Load existing links for comparison
    print("Step 2: Comparing with existing links...")
    existing_links = load_existing_links(existing_links_file)
    
    if not existing_links:
        print(f"⚠️  No existing links file found at {existing_links_file}")
        print("Creating new links file with extracted links...")
        save_extracted_links(extracted_links, existing_links_file)
        sys.exit(0)
    
    # Compare the links
    comparison = compare_links(extracted_links, existing_links)
    
    print(f"📊 Comparison Results:")
    print(f"  Extracted links: {comparison['total_extracted']}")
    print(f"  Existing links:  {comparison['total_existing']}")
    print(f"  Common links:    {len(comparison['common_links'])}")
    print(f"  New links:       {len(comparison['new_links'])}")
    print(f"  Missing links:   {len(comparison['missing_links'])}")
    print()
    
    # Report new links
    if comparison['new_links']:
        print("🆕 New links found (not in existing file):")
        for link in comparison['new_links']:
            print(f"  + {link}")
        print()
    
    # Report missing links
    if comparison['missing_links']:
        print("❓ Links in existing file but not found in sidebar:")
        for link in comparison['missing_links']:
            print(f"  - {link}")
        print()
    
    # Success assessment
    coverage = len(comparison['common_links']) / comparison['total_existing'] * 100 if comparison['total_existing'] > 0 else 0
    
    print("📈 Success Assessment:")
    print(f"  Coverage: {coverage:.1f}% of existing links found in sidebar")
    
    if coverage >= 90:
        print("  ✅ SUCCESS: High coverage - sidebar extraction working well")
        exit_code = 0
    elif coverage >= 70:
        print("  ⚠️  PARTIAL: Good coverage - some links may be in different sections")
        exit_code = 0
    else:
        print("  ❌ LOW COVERAGE: Many existing links not found - check sidebar structure")
        exit_code = 1
    
    # Show sample of extracted links for verification
    print()
    print("📋 Sample of extracted links:")
    for i, link in enumerate(extracted_links[:5]):
        print(f"  {i+1}. {link}")
    if len(extracted_links) > 5:
        print(f"  ... and {len(extracted_links) - 5} more")
    
    sys.exit(exit_code)

if __name__ == "__main__":
    main()