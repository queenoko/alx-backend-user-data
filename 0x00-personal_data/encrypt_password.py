#!/usr/bin/env python3
"""This module is for encrypting passwords...
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """The function for Hashes a password
    using a random salt.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """This function Checks if a hashed password
    was formed from the given password.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
