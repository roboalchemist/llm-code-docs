#!/usr/bin/env python3
"""
Process the docs_tickets.csv queue, running /WTFM for each topic.

For each ticket not already done/in-review:
1. Claim ticket (mark in-progress in CSV)
2. Create worktree for llm-code-docs
3. Run: clauded -p "/WTFM <topic>"
4. Merge worktree back to master
5. Mark as in-review in trckr and CSV

Usage:
    python3 scripts/process-docs-queue.py [--dry-run] [--limit N] [--workers N]
"""

import csv
import fcntl
import subprocess
import sys
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from threading import Lock

CSV_PATH = Path(__file__).parent.parent / "output" / "docs_tickets.csv"
LLM_DOCS_REPO = Path.home() / "github" / "llm-code-docs"
LIBRARIAN_REPO = Path(__file__).parent.parent

# Lock for CSV file operations
csv_lock = Lock()
print_lock = Lock()


def safe_print(*args, **kwargs):
    """Thread-safe print."""
    with print_lock:
        print(*args, **kwargs)


def run_command(cmd: list[str], cwd: Path = None, check: bool = True, quiet: bool = False) -> subprocess.CompletedProcess:
    """Run a command and return the result."""
    if not quiet:
        safe_print(f"  $ {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
    if check and result.returncode != 0 and not quiet:
        safe_print(f"  ERROR: {result.stderr}")
    return result


def read_csv() -> tuple[list[dict], list[str]]:
    """Read CSV with file locking."""
    with csv_lock:
        with open(CSV_PATH, 'r') as f:
            fcntl.flock(f.fileno(), fcntl.LOCK_SH)
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames
            rows = list(reader)
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)
    return rows, fieldnames


def write_csv(rows: list[dict], fieldnames: list[str]):
    """Write CSV with file locking."""
    with csv_lock:
        with open(CSV_PATH, 'w', newline='') as f:
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
            writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            writer.writeheader()
            writer.writerows(rows)
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)


def update_ticket_status(ticket: str, new_status: str, rows: list[dict], fieldnames: list[str]):
    """Update a ticket's status in the CSV."""
    for row in rows:
        if row['ticket'] == ticket:
            row['status'] = new_status
            break
    write_csv(rows, fieldnames)


def claim_ticket(ticket: str, rows: list[dict], fieldnames: list[str]) -> bool:
    """Atomically claim a ticket by marking it in-progress. Returns True if claimed."""
    with csv_lock:
        # Re-read to get latest state
        with open(CSV_PATH, 'r') as f:
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
            reader = csv.DictReader(f)
            current_rows = list(reader)

            # Find and check ticket status
            for row in current_rows:
                if row['ticket'] == ticket:
                    if row['status'] not in ('triage', 'todo'):
                        fcntl.flock(f.fileno(), fcntl.LOCK_UN)
                        return False  # Already claimed
                    row['status'] = 'in-progress'
                    break

            fcntl.flock(f.fileno(), fcntl.LOCK_UN)

        # Write updated state
        with open(CSV_PATH, 'w', newline='') as f:
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
            writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            writer.writeheader()
            writer.writerows(current_rows)
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)

        # Update our in-memory copy
        for row in rows:
            if row['ticket'] == ticket:
                row['status'] = 'in-progress'
                break

    return True


def sanitize_branch_name(name: str) -> str:
    """Convert topic to valid git branch name."""
    # Replace spaces and special chars with dashes
    name = re.sub(r'[^a-zA-Z0-9-]', '-', name.lower())
    # Remove consecutive dashes
    name = re.sub(r'-+', '-', name)
    return name.strip('-')


def process_ticket(ticket: str, topic: str, status: str, rows: list[dict], fieldnames: list[str], dry_run: bool = False, worker_id: int = 0) -> bool:
    """Process a single ticket. Returns True on success."""
    prefix = f"[W{worker_id}]" if worker_id > 0 else ""
    branch_name = f"{ticket}-{sanitize_branch_name(topic)}"
    worktree_path = Path(f"/tmp/llm-code-docs-{branch_name}")

    safe_print(f"\n{prefix} {ticket}: {topic} (status: {status})")

    if dry_run:
        safe_print(f"{prefix}   [DRY RUN] Would create worktree at {worktree_path}")
        safe_print(f"{prefix}   [DRY RUN] Would run: clauded -p \"/WTFM {topic}\"")
        safe_print(f"{prefix}   [DRY RUN] Would merge branch {branch_name} to master")
        safe_print(f"{prefix}   [DRY RUN] Would update {ticket} status: {status} -> in-review")
        return True

    # Claim the ticket
    if not claim_ticket(ticket, rows, fieldnames):
        safe_print(f"{prefix}   SKIPPED: Already claimed by another worker")
        return False

    try:
        # Create worktree with new branch
        safe_print(f"{prefix}   Creating worktree: {worktree_path}")

        # Clean up if exists from previous failed run
        if worktree_path.exists():
            run_command(["git", "-C", str(LLM_DOCS_REPO), "worktree", "remove", "--force", str(worktree_path)], quiet=True, check=False)

        # Try to delete branch if it exists
        run_command(["git", "-C", str(LLM_DOCS_REPO), "branch", "-D", branch_name], quiet=True, check=False)

        # Create worktree
        result = run_command(
            ["git", "-C", str(LLM_DOCS_REPO), "worktree", "add", str(worktree_path), "-b", branch_name],
            check=False
        )
        if result.returncode != 0:
            safe_print(f"{prefix}   FAILED: Could not create worktree")
            update_ticket_status(ticket, status, rows, fieldnames)  # Revert status
            return False

        # Run clauded with /WTFM in the worktree directory
        safe_print(f"{prefix}   Running /WTFM {topic}...")
        result = run_command(
            [
                "claude",
                "--dangerously-skip-permissions",
                "--add-dir", "/tmp",
                "--add-dir", str(worktree_path),
                "-p", f"/WTFM {topic}"
            ],
            cwd=worktree_path,
            check=False
        )

        if result.returncode != 0:
            safe_print(f"{prefix}   FAILED: clauded returned {result.returncode}")
            # Cleanup worktree
            run_command(["git", "-C", str(LLM_DOCS_REPO), "worktree", "remove", "--force", str(worktree_path)], quiet=True, check=False)
            run_command(["git", "-C", str(LLM_DOCS_REPO), "branch", "-D", branch_name], quiet=True, check=False)
            update_ticket_status(ticket, 'failed', rows, fieldnames)
            return False

        # Merge worktree branch back to master
        safe_print(f"{prefix}   Merging {branch_name} to master...")

        # First, ensure worktree changes are committed
        run_command(["git", "-C", str(worktree_path), "add", "-A"], check=False)
        run_command(
            ["git", "-C", str(worktree_path), "commit", "-m", f"{ticket}: Add {topic} documentation", "--allow-empty"],
            check=False
        )

        # Switch to master and merge
        run_command(["git", "-C", str(LLM_DOCS_REPO), "checkout", "master"], check=False)
        result = run_command(
            ["git", "-C", str(LLM_DOCS_REPO), "merge", branch_name, "-m", f"Merge {ticket}: Add {topic} documentation"],
            check=False
        )

        if result.returncode != 0:
            safe_print(f"{prefix}   WARNING: Merge conflict, attempting resolution...")
            run_command(["git", "-C", str(LLM_DOCS_REPO), "merge", "--abort"], quiet=True, check=False)
            # Try rebase instead
            run_command(["git", "-C", str(LLM_DOCS_REPO), "checkout", branch_name], check=False)
            run_command(["git", "-C", str(LLM_DOCS_REPO), "rebase", "master"], check=False)
            run_command(["git", "-C", str(LLM_DOCS_REPO), "checkout", "master"], check=False)
            run_command(["git", "-C", str(LLM_DOCS_REPO), "merge", branch_name], check=False)

        # Push master
        run_command(["git", "-C", str(LLM_DOCS_REPO), "push", "origin", "master"], check=False)

        # Cleanup worktree and branch
        safe_print(f"{prefix}   Cleaning up worktree...")
        run_command(["git", "-C", str(LLM_DOCS_REPO), "worktree", "remove", str(worktree_path)], quiet=True, check=False)
        run_command(["git", "-C", str(LLM_DOCS_REPO), "branch", "-D", branch_name], quiet=True, check=False)

        # Update trckr status
        run_command(["trckr", "issue", "update", ticket, "--status", "in-review"], check=False)

        # Update CSV to in-review
        update_ticket_status(ticket, 'in-review', rows, fieldnames)

        # Commit and push CSV update
        run_command(["git", "-C", str(LIBRARIAN_REPO), "add", "output/docs_tickets.csv"], check=False)
        run_command(
            ["git", "-C", str(LIBRARIAN_REPO), "commit", "-m", f"{ticket}: Add {topic} documentation"],
            check=False
        )
        run_command(["git", "-C", str(LIBRARIAN_REPO), "push", "origin", "master"], check=False)

        safe_print(f"{prefix}   Done - {status} -> in-review (merged & pushed)")
        return True

    except Exception as e:
        safe_print(f"{prefix}   EXCEPTION: {e}")
        # Cleanup on error
        run_command(["git", "-C", str(LLM_DOCS_REPO), "worktree", "remove", "--force", str(worktree_path)], quiet=True, check=False)
        run_command(["git", "-C", str(LLM_DOCS_REPO), "branch", "-D", branch_name], quiet=True, check=False)
        update_ticket_status(ticket, status, rows, fieldnames)  # Revert status
        return False


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Process docs queue with /WTFM")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done")
    parser.add_argument("--limit", type=int, default=0, help="Max items to process (0=all)")
    parser.add_argument("--workers", type=int, default=1, help="Number of parallel workers (default: 1)")
    parser.add_argument("--status", default="triage,todo", help="Statuses to process (comma-separated)")
    args = parser.parse_args()

    allowed_statuses = set(args.status.split(","))

    # Read CSV
    rows, fieldnames = read_csv()

    print(f"Loaded {len(rows)} tickets from {CSV_PATH}")

    # Filter to processable items
    to_process = [r for r in rows if r['status'] in allowed_statuses]
    print(f"Found {len(to_process)} tickets with status in {allowed_statuses}")

    if args.limit > 0:
        to_process = to_process[:args.limit]
        print(f"Limited to {args.limit} tickets")

    if not to_process:
        print("Nothing to process!")
        return 0

    if args.workers > 1:
        print(f"Running with {args.workers} parallel workers")

    processed = 0
    failed = 0

    if args.workers == 1:
        # Serial processing
        for i, row in enumerate(to_process, 1):
            print(f"\n[{i}/{len(to_process)}]", end="")
            success = process_ticket(
                row['ticket'], row['topic'], row['status'],
                rows, fieldnames, args.dry_run
            )
            if success:
                processed += 1
            else:
                failed += 1
    else:
        # Parallel processing with worktrees
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {}
            for i, row in enumerate(to_process):
                future = executor.submit(
                    process_ticket,
                    row['ticket'], row['topic'], row['status'],
                    rows, fieldnames, args.dry_run, i % args.workers + 1
                )
                futures[future] = row

            for future in as_completed(futures):
                row = futures[future]
                try:
                    success = future.result()
                    if success:
                        processed += 1
                    else:
                        failed += 1
                except Exception as e:
                    safe_print(f"Exception processing {row['ticket']}: {e}")
                    failed += 1

    print(f"\n{'='*50}")
    print(f"Processed: {processed}")
    print(f"Failed: {failed}")
    print(f"Remaining: {len(to_process) - processed - failed}")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
