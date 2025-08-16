"""
Locust performance testing entry point
"""
from tests.scenarios.public_api import PublicApiUser

# Explicitly declare classes to be included in the test
__all__ = ["PublicApiUser"]