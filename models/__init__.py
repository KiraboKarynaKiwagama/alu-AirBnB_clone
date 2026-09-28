#!/usr/bin/python3
"""Creates the unique FileStorage instance used by the application."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
