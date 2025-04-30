import os
import shutil
from typing import Optional, Dict, Any
from utils.path_utils import PathUtils  # Changed from relative to absolute

class FileOperations:
    def __init__(self):
        self.path_utils = PathUtils()
    
    def create_file(self, file_path: str, content: Optional[str] = "") -> Dict[str, Any]:
        """Create a new file at specified path with optional content."""
        try:
            # Normalize and validate path
            file_path = self.path_utils.normalize_path(file_path)
            
            # Check if file already exists
            if os.path.exists(file_path):
                return {
                    "status": "error",
                    "message": f"File already exists at {file_path}"
                }
            
            # Ensure directory exists
            directory = os.path.dirname(file_path)
            if not self.path_utils.ensure_directory(directory):
                return {
                    "status": "error",
                    "message": f"Failed to create directory {directory}"
                }
            
            # Create and write to file
            with open(file_path, 'w') as f:
                f.write(content or "")
            
            return {
                "status": "success",
                "message": f"File created successfully at {file_path}"
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }
    
    def delete_file(self, file_path: str) -> Dict[str, Any]:
        """Delete a file at specified path."""
        try:
            # Normalize and validate path
            file_path = self.path_utils.normalize_path(file_path)
            
            # Check if file exists
            if not os.path.exists(file_path):
                return {
                    "status": "error",
                    "message": f"File does not exist at {file_path}"
                }
            
            # Check if it's a file
            if not os.path.isfile(file_path):
                return {
                    "status": "error",
                    "message": f"{file_path} is not a file"
                }
            
            # Check if file is accessible
            if not self.path_utils.is_file_accessible(file_path):
                return {
                    "status": "error",
                    "message": f"File {file_path} is not accessible"
                }
            
            # Delete file
            os.remove(file_path)
            
            return {
                "status": "success",
                "message": f"File deleted successfully: {file_path}"
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }
    
    def move_file(self, source_path: str, destination_path: str) -> Dict[str, Any]:
        """Move a file from source to destination path."""
        try:
            # Normalize and validate paths
            source_path = self.path_utils.normalize_path(source_path)
            destination_path = self.path_utils.normalize_path(destination_path)
            
            # Check if source file exists
            if not os.path.exists(source_path):
                return {
                    "status": "error",
                    "message": f"Source file does not exist at {source_path}"
                }
            
            # Check if source is a file
            if not os.path.isfile(source_path):
                return {
                    "status": "error",
                    "message": f"{source_path} is not a file"
                }
            
            # Check if destination directory exists, create if not
            dest_dir = os.path.dirname(destination_path)
            if not self.path_utils.ensure_directory(dest_dir):
                return {
                    "status": "error",
                    "message": f"Failed to create destination directory {dest_dir}"
                }
            
            # Check if destination file already exists
            if os.path.exists(destination_path):
                return {
                    "status": "error",
                    "message": f"Destination file already exists at {destination_path}"
                }
            
            # Move file
            shutil.move(source_path, destination_path)
            
            return {
                "status": "success",
                "message": f"File moved successfully from {source_path} to {destination_path}"
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }
    
    def rename_file(self, file_path: str, new_name: str) -> Dict[str, Any]:
        """Rename a file while keeping it in the same directory."""
        try:
            # Normalize and validate path
            file_path = self.path_utils.normalize_path(file_path)
            
            # Check if file exists
            if not os.path.exists(file_path):
                return {
                    "status": "error",
                    "message": f"File does not exist at {file_path}"
                }
            
            # Check if it's a file
            if not os.path.isfile(file_path):
                return {
                    "status": "error",
                    "message": f"{file_path} is not a file"
                }
            
            # Validate new filename
            if not self.path_utils.is_valid_filename(new_name):
                return {
                    "status": "error",
                    "message": f"{new_name} is not a valid filename"
                }
            
            # Get directory and create new path
            directory = os.path.dirname(file_path)
            new_path = os.path.join(directory, new_name)
            
            # Check if new path already exists
            if os.path.exists(new_path):
                return {
                    "status": "error",
                    "message": f"File already exists at {new_path}"
                }
            
            # Rename file
            os.rename(file_path, new_path)
            
            return {
                "status": "success",
                "message": f"File renamed successfully from {file_path} to {new_path}"
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }
    
    def read_file(self, file_path: str) -> Dict[str, Any]:
        """Read content from a file."""
        try:
            # Normalize and validate path
            file_path = self.path_utils.normalize_path(file_path)
            
            # Check if file exists
            if not os.path.exists(file_path):
                return {
                    "status": "error",
                    "message": f"File does not exist at {file_path}"
                }
            
            # Check if it's a file
            if not os.path.isfile(file_path):
                return {
                    "status": "error",
                    "message": f"{file_path} is not a file"
                }
            
            # Check if file is accessible
            if not self.path_utils.is_file_accessible(file_path):
                return {
                    "status": "error",
                    "message": f"File {file_path} is not accessible"
                }
            
            # Read file content
            with open(file_path, 'r') as f:
                content = f.read()
            
            return {
                "status": "success",
                "content": content,
                "message": "File read successfully"
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }
    
    def write_file(self, file_path: str, content: str, append: bool = False) -> Dict[str, Any]:
        """Write or append content to a file."""
        try:
            # Normalize and validate path
            file_path = self.path_utils.normalize_path(file_path)
            
            # Check if file exists for append mode
            if append and not os.path.exists(file_path):
                return {
                    "status": "error",
                    "message": f"File does not exist at {file_path} for append operation"
                }
            
            # Ensure directory exists
            directory = os.path.dirname(file_path)
            if not self.path_utils.ensure_directory(directory):
                return {
                    "status": "error",
                    "message": f"Failed to create directory {directory}"
                }
            
            # Write or append to file
            mode = 'a' if append else 'w'
            with open(file_path, mode) as f:
                f.write(content)
            
            return {
                "status": "success",
                "message": f"Content {'appended' if append else 'written'} successfully to {file_path}"
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }