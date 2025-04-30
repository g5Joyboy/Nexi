from typing import Dict, Any
from core.file_operations import FileOperations
from intents.base_intent import BaseIntent

class CreateFileIntent(BaseIntent):
    def __init__(self):
        super().__init__()
        self.file_ops = FileOperations()
    
    def execute(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the create file intent."""
        file_path = params.get("file_path")
        content = params.get("content", "")
        
        return self.file_ops.create_file(file_path, content)