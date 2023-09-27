import os
from pyclickup import ClickUp as PyClickUp


class ClickUp(PyClickUp):
    """ClickUp API wrapper for a specific team"""
    def __init__(
        self,
        token: str,
        team_id: str,
    ) -> None:
        super().__init__(token)
        self.team = self.get_team_by_id(team_id)
        print(f"Succesfully connected to {self.team.name} team")
    
    def get_team_tasks(self, **kwargs):
        return self._get_tasks(self.team.id, **kwargs)


clickup_access_token = os.environ.get("ACCESS_TOKEN")
clickup_team_id = os.environ.get("TEAM_ID")

if clickup_access_token is None:
    print("ACCESS_TOKEN not found in environment variables")
    exit(1)

if clickup_team_id is None:
    print("TEAM_ID not found in environment variables")
    exit(1)

clickup = ClickUp(clickup_access_token, clickup_team_id)

# Get all tasks from the team, Limit to 100 tasks
# TODO: Use filters from original API
tasks = clickup.get_team_tasks()