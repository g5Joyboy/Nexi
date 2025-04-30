from typing import Dict, Any, List
from abc import ABC, abstractmethod
from config.intent_params import INTENT_PARAMS  # Changed to import from intent_params

class BaseIntent(ABC):
    def __init__(self):
        self.intent_name = self.__class__.__name__.replace("Intent", "").lower()
    
    def validate_params(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Validate that all required parameters are present."""
        required_params = INTENT_PARAMS.get(self.intent_name, [])
        
        # Check if all required parameters are present
        missing_params = [param for param in required_params if param not in params]
        
        if missing_params:
            return {
                "valid": False,
                "message": f"Missing required parameters: {', '.join(missing_params)}"
            }
        
        return {"valid": True}
    
    @abstractmethod
    def execute(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the intent with the given parameters."""
        pass