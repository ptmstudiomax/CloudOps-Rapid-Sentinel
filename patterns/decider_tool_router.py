"""
Reusable Decision Pattern: Strands Decider Tool Router
Tag: #tool-selection
"""
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class RouteDecision:
    selected_tool: str
    confidence: float
    is_confident: bool

class StrandsToolRouter:
    def __init__(self, decider_model, min_confidence: float = 0.75):
        self.model = decider_model
        self.min_confidence = min_confidence

    def select_tool(self, system_state: str, candidate_tools: List[str]) -> RouteDecision:
        typed_question = "Which action should be executed immediately based on the state?"
        
        # Strands Decider 2B prediction call
        prediction = self.model.predict(
            state=system_state,
            question=typed_question,
            choices=candidate_tools
        )
        
        confidence = float(prediction.confidence)
        choice = prediction.choice
        
        return RouteDecision(
            selected_tool=choice,
            confidence=confidence,
            is_confident=(confidence >= self.min_confidence)
        )
