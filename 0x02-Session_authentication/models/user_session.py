#!/usr/bin/env python3
""" This script is the UserSession module
"""
from models.base import Base


class UserSession(Base):
    """
    This is the UserSession class
    """

    def __init__(self, *args: list, **kwargs: dict):
        """
        Function to initialize a UserSession instance
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
