from typing import NewType, List

test_type = NewType('test_type', int)

def get_user_name(user_id: test_type) -> test_type:
    return f"User {user_id}"




