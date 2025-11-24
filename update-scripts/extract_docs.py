#!/usr/bin/env python3
"""
Git Repository Documentation Extractor

This script extracts specified folders from git repositories based on
configuration defined in repo_config.yaml.
"""

import os
import sys
import shutil
import tempfile
import logging
from pathlib import Path
from typing import Dict, List, Any, Optional

try:
    import git
    import yaml
except ImportError as e:
    print(f"Missing required dependency: {e}")
    print("Please install required packages:")
    print("pip install gitpython pyyaml")
    sys.exit(1)


class DocumentationExtractor:
    """Handles extraction of documentation folders from git repositories."""
    
    def __init__(self, config_file: str = None):
        # Auto-detect config file location
        if config_file is None:
            script_dir = Path(__file__).parent
            config_file = script_dir / "repo_config.yaml"
            
            # Fallback to current directory for backward compatibility
            if not config_file.exists():
                config_file = Path("repo_config.yaml")
        
        self.config_file = config_file
        self.config = self._load_config()
        self._setup_logging()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file."""
        try:
            with open(self.config_file, 'r') as f:
                config = yaml.safe_load(f)
            return config
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file '{self.config_file}' not found")
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing YAML config: {e}")
    
    def _setup_logging(self):
        """Setup logging configuration."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def _validate_repo_config(self, repo_config: Dict[str, Any]) -> bool:
        """Validate repository configuration."""
        required_fields = ['name', 'repo_url', 'source_folder', 'target_folder']
        for field in required_fields:
            if field not in repo_config:
                self.logger.error(f"Missing required field '{field}' in repository config")
                return False
        return True
    
    def _clone_repository(self, repo_url: str, temp_dir: str, branch: Optional[str] = None) -> git.Repo:
        """Clone repository to temporary directory."""
        self.logger.info(f"Cloning repository: {repo_url}")
        
        clone_kwargs = {
            'to_path': temp_dir,
            'depth': 1,  # Shallow clone for efficiency
        }
        
        if branch:
            clone_kwargs['branch'] = branch
        
        try:
            # Get timeout from config
            timeout = self.config.get('settings', {}).get('clone_timeout', 300)
            
            # Clone repository
            repo = git.Repo.clone_from(repo_url, **clone_kwargs)
            self.logger.info(f"Successfully cloned repository to {temp_dir}")
            return repo
            
        except git.GitCommandError as e:
            raise RuntimeError(f"Failed to clone repository: {e}")
        except Exception as e:
            raise RuntimeError(f"Unexpected error during clone: {e}")
    
    def _extract_folder(self, repo_path: str, source_folder: str, target_folder: str) -> bool:
        """Extract specified folder from repository to target location."""
        source_path = Path(repo_path) / source_folder
        target_path = Path.cwd() / target_folder
        
        # Check if source folder exists
        if not source_path.exists():
            self.logger.error(f"Source folder '{source_folder}' not found in repository")
            return False
        
        # Check if target already exists
        if target_path.exists():
            overwrite = self.config.get('settings', {}).get('overwrite_existing', True)
            if overwrite:
                self.logger.info(f"Target folder '{target_folder}' exists, removing...")
                shutil.rmtree(target_path)
            else:
                self.logger.error(f"Target folder '{target_folder}' already exists and overwrite is disabled")
                return False
        
        try:
            # Ensure parent directories exist
            target_path.parent.mkdir(parents=True, exist_ok=True)

            # Copy the folder
            self.logger.info(f"Copying '{source_folder}' to '{target_folder}'...")
            shutil.copytree(source_path, target_path)
            self.logger.info(f"Successfully extracted folder to '{target_folder}'")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to copy folder: {e}")
            return False
    
    def _get_folder_stats(self, folder_path: Path) -> Dict[str, int]:
        """Get statistics about extracted folder."""
        if not folder_path.exists():
            return {"files": 0, "folders": 0, "size_bytes": 0}
        
        file_count = 0
        folder_count = 0
        total_size = 0
        
        for item in folder_path.rglob("*"):
            if item.is_file():
                file_count += 1
                try:
                    total_size += item.stat().st_size
                except OSError:
                    pass  # Skip files we can't access
            elif item.is_dir():
                folder_count += 1
        
        return {
            "files": file_count,
            "folders": folder_count,
            "size_bytes": total_size
        }
    
    def extract_repository(self, repo_config: Dict[str, Any]) -> bool:
        """Extract documentation from a single repository."""
        if not self._validate_repo_config(repo_config):
            return False
        
        name = repo_config['name']
        repo_url = repo_config['repo_url']
        source_folder = repo_config['source_folder']
        target_folder = repo_config['target_folder']
        branch = repo_config.get('branch')
        
        self.logger.info(f"Starting extraction for repository: {name}")
        
        # Create temporary directory
        temp_dir_base = self.config.get('settings', {}).get('temp_dir_base')
        with tempfile.TemporaryDirectory(dir=temp_dir_base) as temp_dir:
            try:
                # Clone repository
                repo = self._clone_repository(repo_url, temp_dir, branch)
                
                # Extract folder
                success = self._extract_folder(temp_dir, source_folder, target_folder)
                
                if success:
                    # Get statistics
                    target_path = Path.cwd() / target_folder
                    stats = self._get_folder_stats(target_path)
                    self.logger.info(f"Extraction completed: {stats['files']} files, "
                                   f"{stats['folders']} folders, "
                                   f"{stats['size_bytes']:,} bytes")
                
                return success
                
            except Exception as e:
                self.logger.error(f"Error extracting repository '{name}': {e}")
                return False
    
    def extract_all(self) -> bool:
        """Extract documentation from all configured repositories."""
        repositories = self.config.get('repositories', [])
        
        if not repositories:
            self.logger.warning("No repositories configured for extraction")
            return True
        
        self.logger.info(f"Starting extraction for {len(repositories)} repositories")
        
        success_count = 0
        for repo_config in repositories:
            if self.extract_repository(repo_config):
                success_count += 1
        
        self.logger.info(f"Extraction completed: {success_count}/{len(repositories)} successful")
        return success_count == len(repositories)


def main():
    """Main entry point."""
    try:
        extractor = DocumentationExtractor()
        success = extractor.extract_all()
        sys.exit(0 if success else 1)
        
    except Exception as e:
        logging.error(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()