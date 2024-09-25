class Level:
    def __init__(self, level_id: int, parameters: Dict[str, Any]):
        self.level_id = level_id
        self.parameters = parameters

    def get_parameters(self) -> Dict[str, Any]:
        return self.parameters
