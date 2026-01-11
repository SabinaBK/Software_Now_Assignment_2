"""
verification.py
---------------
Verifies that decrypted text matches the original raw text.
"""

from __future__ import annotations
from pathlib import Path


def verify_files(
    original_path: str | Path = "Question_1/raw_text.txt",
    decrypted_path: str | Path = "decrypted_text.txt",
    *args,
    **kwargs
) -> bool:
    """
    Compares original and decrypted files character-by-character.

    Optional kwargs:
    - encoding (default: utf-8)

    Returns:
    - True if files match exactly, False otherwise
    """
    encoding = kwargs.get("encoding", "utf-8")

    # Read both files
    original = Path(original_path).read_text(encoding=encoding)
    decrypted = Path(decrypted_path).read_text(encoding=encoding)

    # If contents match exactly
    if original == decrypted:
        print("✅ Decryption successful: decrypted_text.txt matches raw_text.txt")
        return True

    # Find first mismatch position for debugging
    index = next(
        (i for i, (a, b) in enumerate(zip(original, decrypted)) if a != b),
        min(len(original), len(decrypted))
    )

    expected = original[index] if index < len(original) else "<EOF>"
    actual = decrypted[index] if index < len(decrypted) else "<EOF>"

    print("❌ Decryption failed: files do not match.")
    print(f"First difference at position {index}: expected {expected!r} got {actual!r}")

    return False
