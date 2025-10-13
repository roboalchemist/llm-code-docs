#!/usr/bin/env python3
"""
Comprehensive Claude Code SDK Documentation Downloader
Downloads all Claude Code SDK documentation from the sidebar navigation.
Supports both using existing links file or extracting fresh links from the sidebar.
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse
import time
import json
import subprocess

def download_file(url, output_path):
    """Download a file from URL to the specified output path."""
    try:
        print(f"Downloading: {url}")
        
        # Add timeout for the request
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Create directory if it doesn't exist
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write the content to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(response.text)
            
        print(f"  → Saved to: {output_path}")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"  → Error downloading {url}: {e}")
        return False
    except Exception as e:
        print(f"  → Error saving {url}: {e}")
        return False

def extract_file_path(url):
    """Extract the file path from the URL to preserve directory structure."""
    parsed = urlparse(url)
    # Remove the leading /en/docs/claude-code/ part to get the relative path
    path = parsed.path
    if path.startswith('/en/docs/claude-code/'):
        relative_path = path[len('/en/docs/claude-code/'):]
        return relative_path
    else:
        # Fallback to just the filename
        return Path(path).name

def extract_sidebar_links():
    """Extract current sidebar links from the live documentation."""
    print("🔍 Extracting current sidebar links from documentation...")

    # Use the live extraction script we created
    try:
        # Get the directory where this script is located
        script_dir = Path(__file__).parent
        extraction_script = script_dir / 'extract_sidebar_links_automated.py'

        result = subprocess.run([
            'python3', str(extraction_script)
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print("✅ Successfully extracted current sidebar links")
            # Read the extracted links
            extracted_file = Path("extracted-sidebar-links.txt")
            if extracted_file.exists():
                with open(extracted_file, 'r') as f:
                    links = []
                    for line in f:
                        line = line.strip()
                        if line and line.startswith('http'):
                            links.append(line)
                    return links
        else:
            print(f"⚠️  Sidebar extraction failed: {result.stderr}")
    except Exception as e:
        print(f"⚠️  Error extracting sidebar links: {e}")
    
    return []

def get_links_to_download(use_cached=False):
    """Get the list of URLs to download, always extracting fresh by default."""
    links_file = Path("claude-code-sdk-links.txt")
    
    # Option 1: Use cached file if explicitly requested
    if use_cached and links_file.exists():
        print(f"📂 Using cached links file: {links_file}")
        urls = []
        with open(links_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and line.startswith('http'):
                    urls.append(line)
        
        if urls:
            print(f"Found {len(urls)} URLs in cached file")
            return urls
        else:
            print("⚠️  Cached file is empty, extracting fresh links...")
    
    # Option 2: Extract fresh links (default behavior)
    print("🔄 Extracting fresh sidebar links from documentation...")
    fresh_links = extract_sidebar_links()
    
    if fresh_links:
        # Save the fresh links for future reference
        print(f"💾 Saving {len(fresh_links)} fresh links to {links_file}")
        with open(links_file, 'w') as f:
            f.write("# Claude Code SDK Documentation Links\n")
            f.write("# Automatically extracted from sidebar navigation\n")
            f.write(f"# Generated on {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("\n")
            for link in fresh_links:
                f.write(f"{link}\n")
    
    return fresh_links

def check_existing_files(output_dir):
    """Check what files already exist and their status."""
    if not output_dir.exists():
        return {"total": 0, "files": []}
    
    existing_files = []
    for file_path in output_dir.rglob("*.md"):
        stat = file_path.stat()
        existing_files.append({
            "path": file_path,
            "size": stat.st_size,
            "modified": stat.st_mtime
        })
    
    return {"total": len(existing_files), "files": existing_files}

def main():
    """Main function to download all Claude Code documentation files."""
    
    # Parse command line arguments
    use_cached = len(sys.argv) > 1 and sys.argv[1] == "--cached"
    
    print("📚 Claude Code SDK Documentation Downloader")
    print("=" * 50)
    print("Downloads all Claude Code SDK documentation from the official site")
    print("Automatically extracts fresh links from the sidebar by default")
    if use_cached:
        print("Using cached links file (--cached mode)")
    print()
    
    # Output directory
    output_dir = Path("claude-code-sdk")
    
    # Check existing files
    existing_status = check_existing_files(output_dir)
    if existing_status["total"] > 0:
        print(f"📁 Found {existing_status['total']} existing documentation files")
        print("   (Files will be updated if they have changed)")
    else:
        print("📁 No existing documentation files found - performing fresh download")
    print()
    
    # Get URLs to download
    urls = get_links_to_download(use_cached)
    
    if not urls:
        print("❌ No URLs found to download!")
        print("This could mean:")
        print("  • Network connectivity issues")
        print("  • Problems with the sidebar extraction")
        print("  • Missing or empty links file")
        sys.exit(1)
    
    print(f"🎯 Found {len(urls)} documentation pages to download")
    print(f"📂 Output directory: {output_dir}")
    print()
    
    # Download each file
    successful = 0
    failed = 0
    updated = 0
    skipped = 0
    
    start_time = time.time()
    
    for i, url in enumerate(urls, 1):
        # Extract the relative path from URL
        relative_path = extract_file_path(url)
        output_path = output_dir / relative_path
        
        # Show progress
        print(f"[{i:2d}/{len(urls)}] ", end="", flush=True)
        
        # Check if file exists and get its modification time
        file_exists = output_path.exists()
        old_size = output_path.stat().st_size if file_exists else 0
        
        # Add small delay between requests to be respectful
        time.sleep(0.3)
        
        if download_file(url, output_path):
            new_size = output_path.stat().st_size if output_path.exists() else 0
            
            if file_exists:
                if new_size != old_size:
                    print(f"    📝 Updated (size: {old_size} → {new_size} bytes)")
                    updated += 1
                else:
                    print(f"    ✓ Unchanged ({new_size} bytes)")
                    skipped += 1
            else:
                print(f"    🆕 New file ({new_size} bytes)")
            
            successful += 1
        else:
            failed += 1
    
    # Final summary
    elapsed = time.time() - start_time
    
    print()
    print("=" * 50)
    print(f"📊 Download Summary")
    print("=" * 50)
    print(f"✅ Successful downloads:  {successful}")
    print(f"❌ Failed downloads:      {failed}")
    print(f"📝 Updated files:         {updated}")
    print(f"⏭️  Unchanged files:       {skipped}")
    print(f"🆕 New files:             {successful - updated - skipped}")
    print(f"⏱️  Total time:            {elapsed:.1f} seconds")
    print(f"📁 Output directory:      {output_dir}")
    
    # Calculate total size
    if output_dir.exists():
        total_size = sum(f.stat().st_size for f in output_dir.rglob("*.md"))
        print(f"💾 Total documentation:   {total_size:,} bytes ({total_size/1024:.1f} KB)")
    
    print()
    
    if failed > 0:
        print(f"⚠️  {failed} downloads failed - check network connection and URLs")
        sys.exit(1)
    else:
        print("🎉 All documentation downloaded successfully!")
        
        # Show sample of downloaded files
        if output_dir.exists():
            md_files = list(output_dir.rglob("*.md"))
            if md_files:
                print()
                print("📋 Sample of downloaded files:")
                for i, file_path in enumerate(sorted(md_files)[:5], 1):
                    rel_path = file_path.relative_to(output_dir)
                    size = file_path.stat().st_size
                    print(f"  {i}. {rel_path} ({size} bytes)")
                if len(md_files) > 5:
                    print(f"  ... and {len(md_files) - 5} more files")
        
        sys.exit(0)

if __name__ == "__main__":
    main()