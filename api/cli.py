#!/usr/bin/env python3
"""CLI for librarian REST API"""
import click, requests, json

@click.group()
@click.option('--url', default='http://chungus2:8081')
@click.pass_context
def cli(ctx, url):
    ctx.obj = {'url': url}

@cli.command()
@click.pass_context  
def health(ctx):
    r = requests.get(f"{ctx.obj['url']}/health", timeout=5)
    d = r.json()
    print(f"Status: {d['status']}")
    if 'dependencies' in d:
        print(f"Documents: {d['dependencies']['opensearch']['details']['document_count']:,}")

@cli.command()
@click.argument('query')
@click.option('-l', '--limit', default=10)
@click.pass_context
def search(ctx, query, limit):
    r = requests.get(f"{ctx.obj['url']}/search", params={'q': query, 'limit': limit})
    d = r.json()
    print(f"Results: {len(d['results'])} of {d['total_hits']:,}\n")
    for i, res in enumerate(d['results'], 1):
        print(f"{i}. {res['title']} ({res['framework']} / {res['category']})")

@cli.command()
@click.argument('query')
@click.option('-l', '--limit', default=5)
@click.pass_context
def suggest(ctx, query, limit):
    r = requests.get(f"{ctx.obj['url']}/suggest", params={'q': query, 'limit': limit})
    d = r.json()
    print(f"Suggestions: {len(d['suggestions'])} of {d['total_hits']}\n")
    for i, s in enumerate(d['suggestions'], 1):
        print(f"{i}. {s['framework_name']} - {s['description']}")

if __name__ == '__main__':
    cli()
