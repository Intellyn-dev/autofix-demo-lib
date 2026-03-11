"""User management helpers.

v2.0.0 — renamed get_user_by_id → fetch_user (breaking change).
v1.x callers that use get_user_by_id will get AttributeError.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    id: int
    name: str
    email: str
    active: bool = True


# In-memory store for demo purposes
_USERS: dict[int, User] = {
    1: User(id=1, name="Alice", email="alice@example.com"),
    2: User(id=2, name="Bob",   email="bob@example.com"),
    3: User(id=3, name="Carol", email="carol@example.com"),
}


def fetch_user(user_id: int) -> Optional[User]:
    """Fetch a user by ID. Returns None if not found.

    NOTE: renamed from get_user_by_id in v2.0.0
    """
    return _USERS.get(user_id)


def list_users(active_only: bool = True) -> list[User]:
    """Return all users, optionally filtered to active only."""
    if active_only:
        return [u for u in _USERS.values() if u.active]
    return list(_USERS.values())


def create_user(user_id: int, name: str, email: str) -> User:
    """Create a new user."""
    user = User(id=user_id, name=name, email=email)
    _USERS[user_id] = user
    return user
