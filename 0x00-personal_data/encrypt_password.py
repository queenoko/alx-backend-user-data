#!/usr/bin/env python3
"""This module is for encrypting passwords...
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """The function for Hashes a password
    using a random salt.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())