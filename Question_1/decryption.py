"""
decryption.py
-------------
Handles decryption of text encrypted using encryption.py rules.
Uses exact inverse operations to restore original text.
"""

from __future__ import annotations
from pathlib import Path
from encryption import _shift_in_half  # Reuse same shifting logic


def decrypt_char(ch: str, shift1: int, shift2: int, *args, **kwargs) -> str:
    """
    Decrypts a single character by reversing encryption rules.

    *args and **kwargs are included for extensibility.
    """
    if ch.islower():
        # Reverse lowercase rules
        if "a" <= ch <= "m":
            return _shift_in_half(ch, -(shift1 * shift2), "a")
        return _shift_in_half(ch, shift1 + shift2, "n")

    if ch.isupper():
        # Reverse uppercase rules
        if "A" <= ch <= "M":
            return _shift_in_half(ch, shift1, "A")
        return _shift_in_half(ch, -(shift2 ** 2), "N")

    # Non-alphabetic characters remain unchanged
    return ch


def decrypt_file(
    input_path: str | Path = "encrypted_text.txt",
    output_path: str | Path = "decrypted_text.txt",
    *,
    shift1: int,
    shift2: int,
    **kwargs
) -> str:
    """
    Reads encrypted text, decrypts it, and writes decrypted output.

    Keyword-only parameters:
    - shift1, shift2: same values used during encryption

    Optional kwargs:
    - encoding (default: utf-8)

    Returns:
    - decrypted text as a string
    """
    encoding = kwargs.get("encoding", "utf-8")

    # To read encrypted text
    text = Path(input_path).read_text(encoding=encoding)

    # To decrypt character-by-character
    decrypted_text = "".join(decrypt_char(c, shift1, shift2) for c in text)

    # To write decrypted output
    Path(output_path).write_text(decrypted_text, encoding=encoding)

    return decrypted_text
