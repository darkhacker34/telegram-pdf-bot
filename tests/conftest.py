import random
import string
from pathlib import Path
from typing import Callable, List, cast
from unittest.mock import MagicMock

import pytest
from telegram import Bot, Document, File, Message, Update, User
from telegram.ext import CallbackContext

TEST_DATA_PATH = Path(__file__).parent.resolve() / "data"


@pytest.fixture
def get_data_file() -> Callable[[str], Path]:
    def _func(filename: str):
        return TEST_DATA_PATH / filename

    return _func


@pytest.fixture
def context_manager_side_effect() -> Callable[[str], MagicMock]:
    def _func(return_value: str):
        mock = MagicMock()
        mock.__enter__.return_value = return_value
        return mock

    return _func


@pytest.fixture(name="user_id")
def fixture_user_id() -> int:
    return random.randint(0, 100)


@pytest.fixture(name="document_id")
def fixture_document_id() -> str:
    return "".join(random.choices(string.ascii_letters, k=10))


@pytest.fixture
def language_code() -> str:
    return "en_GB"


@pytest.fixture(name="telegram_user")
def fixture_telegram_user(user_id: int) -> User:
    user = cast(User, MagicMock())
    user.id = user_id
    return user


@pytest.fixture(name="telegram_document")
def fixture_telegram_document(document_id: int) -> Document:
    doc = cast(Document, MagicMock())
    doc.file_id = document_id
    return doc


@pytest.fixture
def document_ids_generator() -> Callable[[int], List[str]]:
    def _func(n: int):
        return ["".join(random.choices(string.ascii_letters, k=10)) for _ in range(n)]

    return _func


@pytest.fixture(name="telegram_file")
def fixture_telegram_file() -> Document:
    return cast(File, MagicMock())


@pytest.fixture(name="telegram_message")
def fixture_telegram_message(
    telegram_user: User, telegram_document: Document
) -> Message:
    msg = cast(Message, MagicMock())
    msg.from_user = telegram_user
    msg.document = telegram_document
    return msg


@pytest.fixture()
def telegram_bot() -> Bot:
    return cast(Bot, MagicMock())


@pytest.fixture
def telegram_update(telegram_message: Message) -> Update:
    update = cast(Update, MagicMock())
    update.effective_message = telegram_message
    return update


@pytest.fixture
def telegram_context() -> CallbackContext:
    context = cast(CallbackContext, MagicMock())
    return context
