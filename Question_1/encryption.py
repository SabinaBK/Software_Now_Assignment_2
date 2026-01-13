"""
encryption.py
-------------
Handles encryption of text using user-provided shift values.

Encryption rules:
- Lowercase letters:
  - a-m → shift forward by (shift1 * shift2)
  - n-z → shift backward by (shift1 + shift2)
- Uppercase letters:
  - A-M → shift backward by shift1
  - N-Z → shift forward by (shift2 ** 2)
- Non-alphabetic characters: 
  Spaces, tabs, newlines, special characters, and numbers remain unchanged.

Half-alphabet wrapping (13 letters) is used to ensure reversibility.
"""

from __future__ import annotations
from pathlib import Path


def _shift_in_half(ch: str, delta: int, start: str) -> str:
    """
    Shifts a character within a 13-letter half of the alphabet.

    Parameters:
    - ch: character to shift
    - delta: number of positions to shift (positive or negative)
    - start: starting character of the half ('a', 'n', 'A', 'N')

    Returns:
    - shifted character within the same half
    """
    base = ord(start)                     # ASCII value of half start
    offset = ord(ch) - base               # Position of character within the half
    return chr(base + (offset + delta) % 13)  # Wrap inside 13 letters


def encrypt_char(ch: str, shift1: int, shift2: int, *args, **kwargs) -> str:
    """
    Encrypts a single character according to requirements.

    *args and **kwargs are included for extensibility.
    """
    if ch.islower():
        # First half lowercase (a-m): forward shift
        if "a" <= ch <= "m":
            return _shift_in_half(ch, shift1 * shift2, "a")
        # Second half lowercase (n-z): backward shift
        return _shift_in_half(ch, -(shift1 + shift2), "n")

    if ch.isupper():
        # First half uppercase (A-M): backward shift
        if "A" <= ch <= "M":
            return _shift_in_half(ch, -shift1, "A")
        # Second half uppercase (N-Z): forward squared shift
        return _shift_in_half(ch, shift2 ** 2, "N")

    # Non-alphabetic characters remain unchanged
    return ch


def encrypt_file(
    input_path: str | Path = "Question_1/raw_text.txt",
    output_path: str | Path = "encrypted_text.txt",
    *,
    shift1: int,
    shift2: int,
    **kwargs
) -> str:
    """
    Reads text from input file, encrypts it, and writes encrypted output.

    Keyword-only parameters:
    - shift1, shift2: encryption shift values

    Optional kwargs:
    - encoding (default: utf-8)

    Returns:
    - encrypted text as a string
    """
    encoding = kwargs.get("encoding", "utf-8")

    # To read original text
    text = Path(input_path).read_text(encoding=encoding)

    # To encrypt character-by-character
    encrypted_text = "".join(encrypt_char(c, shift1, shift2) for c in text)

    # To write encrypted output
    Path(output_path).write_text(encrypted_text, encoding=encoding)

    return encrypted_text
