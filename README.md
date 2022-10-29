# Overview

[![PyPI Version][pypi-image]][pypi-url]

This package includes simple pure python telegram bot that sends logs to chat.

## Algorithm

```python
from logger2telegram import Logger2tlg


tlg = Logger2tlg(chat_id="123456789", bot_id="123456789:ABCDEF1234567890ABCDEF1234567890ABC")
tlg.log("Hello world!")
```

1. Create bot via bot_father bot in telegram
2. Insert bot token to class
3. Insert chat id to class: https://stackoverflow.com/a/32572159/9142932
4. Create instance of logger via `tlg = Logger2tlg(chat_id = "-123456789", bot_id = "BOT TOKEN FROM BOT FATHER")`
5. Send urgent logs via `tlg.log("This is message")`
6. You may create multiple loggers to different chats or bots.

## Installation

`pip install logger2tlg`

<!-- Badges -->
[pypi-image]: https://img.shields.io/pypi/v/logger2telegram
[pypi-url]: https://pypi.org/project/logger2telegram

