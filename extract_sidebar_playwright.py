#!/usr/bin/env python3
"""
Script to extract all sidebar navigation links from Claude Code SDK documentation using Playwright.
Handles JavaScript-rendered content by using a real browser to load the page.
"""

import json
import sys
from pathlib import Path
import subprocess
import re

def run_playwright_command(command_type, **kwargs):
    """Helper to run playwright commands via subprocess."""
    cmd = ['python3', '-c', f'''
import sys
sys.path.insert(0, "/Users/joe/.claude/tools/playwright")
from playwright_tools import {command_type}

result = {command_type}({", ".join(f"{k}={repr(v)}" for k, v in kwargs.items())})
print(json.dumps(result) if isinstance(result, dict) else result)
''']
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running playwright command: {e.stderr}")
        return None

def extract_links_with_playwright(url):
    """Use Playwright to extract sidebar links from the documentation page."""
    extracted_links = []
    
    try:
        # Navigate to the page
        print(f"Loading page with Playwright: {url}")
        
        # First, let's try to see what we can extract using the WebFetch tool
        # which might handle the page better than requests
        
        # For now, let's create a simple JavaScript extraction script
        js_script = '''
        // Extract all links from navigation elements
        const links = [];
        const baseUrl = 'https://docs.anthropic.com';
        
        // Try multiple selectors for sidebar/navigation
        const selectors = [
            'nav[aria-label*="sidebar" i]',
            'nav[aria-label*="navigation" i]',
            '.sidebar',
            '.navigation',
            '.docs-sidebar',
            'nav',
            '[role="navigation"]'
        ];
        
        for (const selector of selectors) {
            const elements = document.querySelectorAll(selector);
            for (const element of elements) {
                const anchors = element.querySelectorAll('a[href]');
                for (const anchor of anchors) {
                    let href = anchor.getAttribute('href');
                    if (href) {
                        // Convert relative URLs to absolute
                        if (href.startsWith('/')) {
                            href = baseUrl + href;
                        }
                        // Only include Claude Code docs links ending in .md
                        if (href.includes('/docs/claude-code/') && href.endsWith('.md')) {
                            links.push(href);
                        }
                    }
                }
            }
        }
        
        // Also try to find any links in the page that match our pattern
        const allLinks = document.querySelectorAll('a[href]');
        for (const anchor of allLinks) {
            let href = anchor.getAttribute('href');
            if (href) {
                if (href.startsWith('/')) {
                    href = baseUrl + href;
                }
                if (href.includes('/docs/claude-code/') && href.endsWith('.md')) {
                    links.push(href);
                }
            }
        }
        
        // Remove duplicates and sort
        const uniqueLinks = [...new Set(links)].sort();
        return JSON.stringify(uniqueLinks);
        '''
        
        return js_script
        
    except Exception as e:
        print(f"Error with Playwright extraction: {e}")
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
    """Main function using WebFetch to get the page content first."""
    
    # Configuration
    docs_url = "https://docs.anthropic.com/en/docs/claude-code/sdk"
    existing_links_file = "claude-code-sdk-links.txt"
    extracted_links_file = "extracted-sidebar-links.txt"
    
    print("Claude Code SDK Documentation Link Extractor (Playwright)")
    print("=" * 60)
    print()
    
    print("This script will use the MCP Playwright tool to extract links.")
    print("Since we need to handle JavaScript-rendered content, we'll use")
    print("the WebFetch tool first to see if we can extract links from the HTML.")
    print()
    
    # Load existing links for reference
    existing_links = load_existing_links(existing_links_file)
    print(f"Loaded {len(existing_links)} existing links for comparison")
    
    # Show what we're looking for
    print("Sample of existing links:")
    for i, link in enumerate(existing_links[:5]):
        print(f"  {i+1}. {link}")
    if len(existing_links) > 5:
        print(f"  ... and {len(existing_links) - 5} more")
    print()
    
    print("To complete the extraction, we need to use MCP Playwright tools.")
    print("This script provides the framework - the actual extraction needs")
    print("to be completed using the mcp__playwright tools.")
    
    return existing_links

if __name__ == "__main__":
    main()