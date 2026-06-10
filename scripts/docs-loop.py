#!/home/gateway/miniconda3/bin/python
"""
Loop clauded /docs:WTFM-next as long as there are doc-add tickets in todo status.

Logs to both console and file, showing:
- When each issue finishes
- Count of todo tickets remaining
- Count of completed tickets so far

Supports parallel workers for faster processing.
"""

import subprocess
import json
import sys
import logging
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

import click

# Configuration
PROJECT_ID = "0e5104bf-8740-4115-9d70-5036b76186b3"
LOG_FILE = Path(__file__).parent.parent / "output" / "docs-loop.log"
LLM_CODE_DOCS_PATH = Path.home() / "github" / "llm-code-docs"

# Set up logging to both file and console
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("docs-loop")
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter(
    "%(asctime)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
))

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter(
    "%(asctime)s | %(message)s", datefmt="%H:%M:%S"
))

logger.addHandler(file_handler)
logger.addHandler(console_handler)


def get_tickets(status: str) -> list[dict]:
    """Get tickets with the given status."""
    cmd = [
        "trckr", "issue", "list",
        "--project-id", PROJECT_ID,
        "--labels", "docs-add",
        "--status", status
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0 and result.stdout.strip():
            return json.loads(result.stdout)
    except (subprocess.TimeoutExpired, json.JSONDecodeError) as e:
        logger.error(f"Error getting {status} tickets: {e}")
    return []


def get_counts() -> tuple[int, int]:
    """Get current todo and done counts."""
    todo = get_tickets("todo")
    done = get_tickets("done")
    return len(todo), len(done)


def get_latest_commit() -> str:
    """Get the latest commit message from llm-code-docs."""
    cmd = ["git", "-C", str(LLM_CODE_DOCS_PATH), "log", "-1", "--format=%h %s"]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            return result.stdout.strip()
    except subprocess.TimeoutExpired:
        pass
    return "unknown"


CLAUDE_CMD = [
    "claude",
    "--dangerously-skip-permissions",
    "--add-dir", "/tmp",
]


def run_clauded(worker_id: int, dry_run: bool = False) -> bool:
    """Run clauded with /docs:WTFM-next. Returns True on success."""
    cmd = CLAUDE_CMD + ["-p", "/docs:WTFM-next"]
    prefix = f"[W{worker_id}]"
    logger.info(f"{prefix} Directory: {LLM_CODE_DOCS_PATH}")
    logger.info(f"{prefix} Command: {' '.join(cmd)}")

    if dry_run:
        logger.info(f"{prefix} [DRY-RUN] Skipping execution")
        time.sleep(1)  # Simulate some work
        return True

    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            cwd=LLM_CODE_DOCS_PATH,
        )
        process.wait()
        return process.returncode == 0

    except Exception as e:
        logger.error(f"{prefix} Error running clauded: {e}")
        return False


class DocsLoopState:
    """Thread-safe shared state for parallel workers."""

    def __init__(self, limit: int, max_stale: int):
        self.lock = threading.Lock()
        self.limit = limit
        self.max_stale = max_stale
        self.iteration = 0
        self.stale_count = 0
        self.prev_counts: tuple[int, int] | None = None
        self.should_stop = False

    def get_next_iteration(self) -> int | None:
        """Get next iteration number, or None if should stop."""
        with self.lock:
            if self.should_stop:
                return None
            if self.limit > 0 and self.iteration >= self.limit:
                return None
            self.iteration += 1
            return self.iteration

    def check_progress(self, new_counts: tuple[int, int]) -> bool:
        """Check if progress was made. Returns False if stuck."""
        with self.lock:
            if self.prev_counts == new_counts:
                self.stale_count += 1
                if self.stale_count >= self.max_stale:
                    self.should_stop = True
                    return False
            else:
                self.stale_count = 0
            self.prev_counts = new_counts
            return True

    def stop(self):
        """Signal all workers to stop."""
        with self.lock:
            self.should_stop = True


WORKER_STAGGER_SECONDS = 20


def worker_task(worker_id: int, state: DocsLoopState, dry_run: bool) -> int:
    """Worker function that processes tickets until stopped."""
    completed = 0
    prefix = f"[W{worker_id}]"

    # Stagger worker starts to avoid ticket conflicts
    if worker_id > 1:
        stagger_delay = (worker_id - 1) * WORKER_STAGGER_SECONDS
        logger.info(f"{prefix} Waiting {stagger_delay}s before starting...")
        time.sleep(stagger_delay)

    while not state.should_stop:
        # Get next iteration
        iteration = state.get_next_iteration()
        if iteration is None:
            break

        # Check if there are tickets
        todo_count, done_count = get_counts()
        if todo_count == 0:
            logger.info(f"{prefix} No more tickets in todo status.")
            state.stop()
            break

        logger.info("-" * 60)
        logger.info(f"{prefix} Iteration {iteration}" + (f"/{state.limit}" if state.limit > 0 else ""))
        logger.info(f"{prefix} Remaining: {todo_count} todo | {done_count} done")
        logger.info("-" * 60)

        start_time = datetime.now()

        # Run clauded
        success = run_clauded(worker_id, dry_run=dry_run)

        elapsed = datetime.now() - start_time
        elapsed_str = str(elapsed).split(".")[0]

        # Get updated counts
        new_todo, new_done = get_counts()

        status_str = "SUCCESS" if success else "FAILED"
        latest_commit = get_latest_commit()
        logger.info(f"{prefix} Finished: {status_str}")
        logger.info(f"{prefix} Elapsed: {elapsed_str}")
        logger.info(f"{prefix} Commit: {latest_commit}")
        logger.info(f"{prefix} Updated counts: {new_todo} todo | {new_done} done")

        # Check for stale progress
        if not state.check_progress((new_todo, new_done)):
            logger.error(f"{prefix} Agent stuck: no progress for {state.max_stale} iterations. Stopping.")
            break
        elif state.stale_count > 0:
            logger.warning(f"{prefix} No progress detected ({state.stale_count}/{state.max_stale})")

        if success:
            completed += 1
        else:
            logger.warning(f"{prefix} clauded failed, continuing to next...")

    return completed


@click.command()
@click.option("--dry-run", is_flag=True, help="Preview without running clauded")
@click.option("--limit", type=int, default=0, help="Max issues to process (0 = unlimited)")
@click.option("--max-stale", type=int, default=3, help="Exit after N iterations with no progress")
@click.option("--workers", type=int, default=1, help="Number of parallel workers")
def main(dry_run: bool, limit: int, max_stale: int, workers: int):
    """Loop clauded /docs:WTFM-next for doc-add tickets."""
    logger.info("=" * 60)
    logger.info(f"Starting docs-loop{' [DRY-RUN]' if dry_run else ''}")
    if limit > 0:
        logger.info(f"Limit: {limit} issues")
    logger.info(f"Max stale: {max_stale} iterations")
    logger.info(f"Workers: {workers}")
    logger.info("=" * 60)

    state = DocsLoopState(limit=limit, max_stale=max_stale)

    if workers == 1:
        # Single worker - run directly
        total_completed = worker_task(1, state, dry_run)
    else:
        # Multiple workers - use thread pool
        total_completed = 0
        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = [
                executor.submit(worker_task, i + 1, state, dry_run)
                for i in range(workers)
            ]
            for future in as_completed(futures):
                try:
                    total_completed += future.result()
                except Exception as e:
                    logger.error(f"Worker failed: {e}")

    logger.info("=" * 60)
    logger.info(f"Docs-loop complete. Total iterations: {state.iteration}")
    logger.info(f"Successfully completed: {total_completed}")
    final_todo, final_done = get_counts()
    logger.info(f"Final counts: {final_todo} todo | {final_done} done")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
