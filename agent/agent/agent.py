class DriveDocAgent:
    """Main agent for autonomous Google Drive document analysis."""

    def __init__(self):
        self.name = "DriveDoc Agent"

    def run(self, task: str):
        return f"Agent received task: {task}"
