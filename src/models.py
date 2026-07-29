from dataclasses import dataclass, field

@dataclass
class Recipe:
    title: str
    category: str
    ingredients: list = field(default_factory=list)
    instructions: str = ""
    favorite: bool = False
