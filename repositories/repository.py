from sqlalchemy.orm import Session

from google.cloud.firestore import Client


class Repository:
    def __init__(self, session: Client) -> None:
        self._session = session
