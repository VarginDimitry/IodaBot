from datetime import datetime
from typing import Optional


def datetime_msg_parser(text: str) -> Optional[datetime]:
    text = text.strip()

    dt = None

    try:
        dt = datetime.fromtimestamp(int(text))
    except:
        pass

    try:
        dt = datetime.fromisoformat(text)
    except:
        pass

    return dt
