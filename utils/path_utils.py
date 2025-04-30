import os
import re
from typing import Optional, Tuple

class PathUtils:
    @staticmethod
    def normalize_path(path: str) -> str:
        """Normalize a file path to use correct separators and absolute path."""
        # Convert to absolute path and normalize separators
        abs_path = os.path.abspath(os.path.expanduser(path))
        return os.path.normpath(abs_path)
    
    @staticmethod
    def is_safe_path(base_path: str, path: str) -> bool:
        """Check if the path is safe (doesn't try to access parent directories)."""
        # Normalize both paths
        base_path = PathUtils.normalize_path(base_path)
        path = PathUtils.normalize_path(path)
        
        # Check if path is within base_path
        try:
            return os.path.commonpath([base_path, path]).startswith(base_path)
        except ValueError:
            return False
    
    @staticmethod
    def split_path(path: str) -> Tuple[str, str]:
        """Split path into directory and filename."""
        path = PathUtils.normalize_path(path)
        return os.path.split(path)
    
    @staticmethod
    def get_extension(path: str) -> str:
        """Get file extension (lowercase)."""
        return os.path.splitext(path)[1].lower()
    
    @staticmethod
    def is_valid_filename(filename: str) -> bool:
        """Check if filename is valid for Windows systems."""
        # Windows invalid characters and names
        invalid_chars = r'[<>:"/\\|?*]'
        invalid_names = {
            'CON', 'PRN', 'AUX', 'NUL',
            'COM1', 'COM2', 'COM3', 'COM4',
            'LPT1', 'LPT2', 'LPT3', 'LPT4'
        }
        
        # Check if filename is empty or contains invalid characters
        if not filename or re.search(invalid_chars, filename):
            return False
            
        # Check if filename (without extension) is in invalid names
        name_without_ext = os.path.splitext(filename)[0].upper()
        if name_without_ext in invalid_names:
            return False
            
        return True
    
    @staticmethod
    def ensure_directory(path: str) -> bool:
        """Ensure directory exists, create if it doesn't."""
        try:
            os.makedirs(path, exist_ok=True)
            return True
        except Exception:
            return False
    
    @staticmethod
    def get_unique_path(path: str) -> str:
        """Get a unique path by adding a number if file exists."""
        if not os.path.exists(path):
            return path
            
        directory, filename = os.path.split(path)
        name, ext = os.path.splitext(filename)
        
        counter = 1
        while True:
            new_path = os.path.join(directory, f"{name}_{counter}{ext}")
            if not os.path.exists(new_path):
                return new_path
            counter += 1
    
    @staticmethod
    def is_file_accessible(path: str) -> bool:
        """Check if file is accessible for reading/writing."""
        if not os.path.exists(path):
            return True  # New file can be created
        
        # Check if file can be opened for reading and writing
        try:
            with open(path, 'a'): pass
            with open(path, 'r'): pass
            return True
        except (IOError, PermissionError):
            return False