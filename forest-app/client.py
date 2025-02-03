import requests
from datetime import datetime, timedelta
from typing import Optional, List
from .models import Plant, User, Tag, TreeType

class ForestClient:
    def __init__(self, remember_token: str):
        self.base_url = "https://c88fef96.forestapp.cc/api/v1"
        self.remember_token = remember_token
        self.session = requests.Session()
        self.session.cookies.set("remember_token", remember_token)
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Origin": "chrome-extension://kjacjjdnoddnpbbcjilcajfhhbdhkpgk"
        })

    def plant_tree(self, 
                   duration_minutes: int = 10, 
                   start_time: Optional[datetime] = None,
                   is_success: bool = True,
                   tree_type_gid: int = 114,
                   tag: int = 0,
                   note: str = "") -> Plant:
        """Plant a tree with the specified duration"""
        if start_time is None:
            start_time = datetime.now()
        
        end_time = start_time + timedelta(minutes=duration_minutes)
        
        plant = Plant(
            start_time=start_time,
            end_time=end_time,
            is_success=is_success,
            tree_type_gid=tree_type_gid,
            tag=tag,
            note=note
        )

        response = self.session.post(
            f"{self.base_url}/plants",
            json=plant.to_dict()
        )
        response.raise_for_status()
        return Plant.from_dict(response.json())

    def get_plants(self) -> List[Plant]:
        """Get list of planted trees"""
        response = self.session.get(f"{self.base_url}/plants")
        response.raise_for_status()
        return [Plant.from_dict(plant) for plant in response.json()]

    def get_user_info(self) -> User:
        """Get current user information"""
        response = self.session.get(f"{self.base_url}/users/{self.get_user_id()}")
        response.raise_for_status()
        return User(**response.json())

    def get_tags(self) -> List[Tag]:
        """Get user's tags"""
        response = self.session.get(f"{self.base_url}/tags")
        response.raise_for_status()
        return [Tag(**tag) for tag in response.json()['tags']]

    def get_unlocked_trees(self) -> List[TreeType]:
        """Get list of unlocked tree types"""
        response = self.session.get(f"{self.base_url}/tree_types/unlocked")
        response.raise_for_status()
        return [TreeType(**tree) for tree in response.json()]

    def get_user_id(self) -> int:
        """Helper method to get user ID from a plant"""
        plants = self.get_plants()
        if plants:
            return plants[0].user_id
        raise ValueError("No plants found to determine user ID") 