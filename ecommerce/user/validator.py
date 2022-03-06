from sqlalchemy.orm import Session

from .models import User


def verify_email_exit(email: str, db_session: Session) -> Optional[User]:
    return None
