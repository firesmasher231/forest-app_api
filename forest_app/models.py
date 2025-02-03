from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass
class Tree:
    is_dead: bool = False
    phase: int = 4
    tree_type: int = 114
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class TreeType:
    gid: int
    title: str
    atlas_image_url: str
    atlas_json_url: str
    tier: int
    owners_only_in_rooms: bool


@dataclass
class Tag:
    id: int
    title: str
    tag_id: int
    user_id: int
    deleted: bool
    created_at: datetime
    updated_at: datetime
    tag_color_tcid: Optional[int]


@dataclass
class User:
    id: int
    name: str
    email: str
    created_at: datetime
    coin: int
    avatar_url: str
    total_minutes: int
    health_tree_count: int
    dead_tree_count: int
    gem: int
    region: str
    language: str
    timezone: int
    remember_token: str
    device_id: Optional[str] = None
    facebook_id: Optional[str] = None
    share_count: int = 0
    weibo_id: Optional[str] = None
    avatar: Optional[str] = None
    has_sn: bool = False
    reset_sent_at: Optional[datetime] = None
    device_token: Optional[str] = None
    platform: Optional[str] = None
    not_shown_in_global: bool = False
    not_shown_in_friend: bool = False
    cheating: bool = False
    price_tier: Optional[int] = None
    boost_end_time: Optional[datetime] = None
    boost_start_time: Optional[datetime] = None
    boost_rate: Optional[float] = None
    avatar_attach_file_name: Optional[str] = None
    avatar_attach_content_type: Optional[str] = None
    avatar_attach_file_size: Optional[int] = None
    avatar_attach_updated_at: Optional[datetime] = None
    xmas2016_redeemed: bool = False
    certificate_name: Optional[str] = None
    is_using_new_friend_system: bool = False
    is_allow_add_friend_from_profile: bool = False
    banned: bool = False
    survey_cake_reward_state: str = "uncompleted"
    disabled: bool = False
    receipt_system_premium_rid: Optional[int] = None
    converted_to_full_at: Optional[datetime] = None
    registration_distribution: Optional[str] = None
    total_ms: Optional[int] = None
    intl_id: Optional[str] = None
    migration_completed_at: Optional[datetime] = None
    is_tracking_allowed: bool = False
    is_tracking_allowed_updated_at: Optional[datetime] = None
    oauth_application_user_id: Optional[int] = None
    is_guest: bool = False
    age_screen_code_id: Optional[int] = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


@dataclass
class Plant:
    start_time: datetime
    end_time: datetime
    note: str = ""
    tag: int = 0
    tree_type_gid: int = 114
    is_success: bool = True
    trees: List[Tree] = None
    id: Optional[int] = None
    user_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    mode: str = "countdown"

    def __post_init__(self):
        if self.trees is None:
            self.trees = [Tree()]
        self.updated_at = datetime.fromtimestamp(self.end_time.timestamp() + 1)

    def to_dict(self) -> dict:
        return {
            "plant": {
                "start_time": self.start_time.isoformat(),
                "end_time": self.end_time.isoformat(),
                "note": self.note,
                "tag": self.tag,
                "tree_type_gid": self.tree_type_gid,
                "is_success": self.is_success,
                "updated_at": self.updated_at.isoformat(),
                "trees": [vars(tree) for tree in self.trees],
            }
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Plant":
        trees = [Tree(**tree) for tree in data.get("trees", [])]
        return cls(
            id=data.get("id"),
            user_id=data.get("user_id"),
            start_time=datetime.fromisoformat(data["start_time"].rstrip("Z")),
            end_time=datetime.fromisoformat(data["end_time"].rstrip("Z")),
            note=data.get("note", ""),
            tag=data.get("tag", 0),
            tree_type_gid=data.get("tree_type_gid", 114),
            is_success=data.get("is_success", True),
            trees=trees,
            created_at=(
                datetime.fromisoformat(data["created_at"].rstrip("Z"))
                if "created_at" in data
                else None
            ),
            updated_at=(
                datetime.fromisoformat(data["updated_at"].rstrip("Z"))
                if "updated_at" in data
                else None
            ),
            mode=data.get("mode", "countdown"),
        )
