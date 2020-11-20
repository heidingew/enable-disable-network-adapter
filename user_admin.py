import os
import ctypes


class AdminStateUnknownError(Exception):
    """Cannot determine whether the user is an admin."""
    pass


# Function checks if application is running as Administrator
# type: () -> bool
def is_user_admin():
    """Return True if user has admin privileges.

    Raises:
        AdminStateUnknownError if user privileges cannot be determined.
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() == 1
    except AttributeError:
        raise AdminStateUnknownError
