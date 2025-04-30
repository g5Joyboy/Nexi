from typing import Dict, Any
from config.intent_config import INTENT_MAPPINGS  # Change to absolute import

class IntentHandler:
    def __init__(self):
        self.intent_mappings = INTENT_MAPPINGS
    
    def process_intent(self, intent: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Process an intent with the given parameters."""
        # Check if intent is supported
        if intent not in self.intent_mappings:
            return {
                "status": "error",
                "message": f"Unsupported intent: {intent}"
            }
        
        # Get the intent handler class
        intent_handler_class = self.intent_mappings[intent]
        intent_handler = intent_handler_class()
        
        # Validate parameters
        validation_result = intent_handler.validate_params(params)
        if not validation_result["valid"]:
            return {
                "status": "error",
                "message": validation_result["message"]
            }
        
        # Execute the intent
        return intent_handler.execute(params)