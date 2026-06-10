"""Embedding server management with auto-restart."""

import os
import sys
import time
import signal
import subprocess
import requests
from pathlib import Path
from typing import Optional
import logging

logger = logging.getLogger(__name__)


class EmbeddingServerManager:
    """Manages embedding server lifecycle with auto-restart."""

    def __init__(
        self,
        server_dir: str = "/tmp/qwen3-embeddings-mlx",
        port: int = 10001,
        max_restart_attempts: int = 3,
    ):
        self.server_dir = Path(server_dir)
        self.port = port
        self.max_restart_attempts = max_restart_attempts
        self.process: Optional[subprocess.Popen] = None
        self.health_url = f"http://localhost:{port}/health"

    def is_server_healthy(self, timeout: int = 5) -> bool:
        """Check if server is responding."""
        try:
            response = requests.get(self.health_url, timeout=timeout)
            return response.status_code == 200
        except Exception:
            return False

    def start_server(self) -> bool:
        """Start the embedding server."""
        if not self.server_dir.exists():
            logger.error(f"Server directory not found: {self.server_dir}")
            return False

        # Check if already running
        if self.is_server_healthy():
            logger.info(f"Server already running on port {self.port}")
            return True

        # Kill any existing process on this port
        self._kill_port()

        # Start server
        log_file = Path(f"/tmp/qwen-server-{self.port}.log")
        log_handle = open(log_file, "w")

        env = os.environ.copy()
        env["PORT"] = str(self.port)

        try:
            self.process = subprocess.Popen(
                [sys.executable, "server.py"],
                cwd=self.server_dir,
                env=env,
                stdout=log_handle,
                stderr=subprocess.STDOUT,
                start_new_session=True,  # Detach from parent
            )

            # Wait for server to be ready
            logger.info(f"Starting server on port {self.port}...")
            for i in range(30):  # 30 second timeout
                time.sleep(1)
                if self.is_server_healthy():
                    logger.info(f"✓ Server ready on port {self.port}")
                    return True

            logger.error("Server failed to become healthy within 30 seconds")
            return False

        except Exception as e:
            logger.error(f"Failed to start server: {e}")
            return False

    def restart_server(self) -> bool:
        """Restart the server."""
        logger.warning("Restarting embedding server...")
        self.stop_server()
        time.sleep(2)
        return self.start_server()

    def stop_server(self):
        """Stop the server process."""
        if self.process:
            try:
                os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
                self.process.wait(timeout=5)
            except Exception:
                pass
        self._kill_port()

    def _kill_port(self):
        """Kill any process on the server port."""
        try:
            subprocess.run(
                f"lsof -ti:{self.port} | xargs kill -9 2>/dev/null",
                shell=True,
                check=False,
            )
        except Exception:
            pass

    def ensure_server_running(self) -> bool:
        """Ensure server is running, restart if needed."""
        if self.is_server_healthy():
            return True

        logger.warning("Server not responding, attempting restart...")
        for attempt in range(self.max_restart_attempts):
            logger.info(f"Restart attempt {attempt + 1}/{self.max_restart_attempts}")
            if self.start_server():
                return True
            time.sleep(5)

        logger.error(f"Failed to restart server after {self.max_restart_attempts} attempts")
        return False

    def __enter__(self):
        """Context manager entry."""
        self.ensure_server_running()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - keep server running."""
        # Don't stop server on exit - let it keep running
        pass


# Global instance
_server_manager: Optional[EmbeddingServerManager] = None


def get_server_manager() -> EmbeddingServerManager:
    """Get global server manager instance."""
    global _server_manager
    if _server_manager is None:
        _server_manager = EmbeddingServerManager()
    return _server_manager
