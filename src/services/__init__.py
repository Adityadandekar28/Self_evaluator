"""Services package — cross-cutting service interfaces (Gemini client, etc.)."""

from src.services.gemini import (
    DEFAULT_MODEL,
    GeminiAPIError,
    GeminiClient,
    GeminiConfigError,
    GeminiError,
    get_api_key,
)

__all__ = [
    "GeminiClient",
    "GeminiError",
    "GeminiConfigError",
    "GeminiAPIError",
    "DEFAULT_MODEL",
    "get_api_key",
]

