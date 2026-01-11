"""
main.py
-------
Main entry point for Assignment 2.

Program flow:
1. Prompt user for shift1 and shift2
2. Encrypt raw_text.txt
3. Decrypt encrypted_text.txt
4. Verify decrypted output matches original
"""

from __future__ import annotations
from encryption import encrypt_file
from decryption import decrypt_file
from verification import verify_files


def _get_int(prompt: str, *, min_value=None, max_value=None, **kwargs) -> int:
    """
    Safely prompts the user for an integer input.

    Optional keyword arguments:
    - min_value: minimum allowed value
    - max_value: maximum allowed value
    """
    while True:
        try:
            value = int(input(prompt).strip())

            # Validate range if provided
            if (min_value is not None and value < min_value) or \
               (max_value is not None and value > max_value):
                raise ValueError

            return value

        except ValueError:
            print("Please enter a valid integer.")


def main(*args, **kwargs) -> None:
    """
    Executes the full encryption-decryption-verification pipeline.
    """
    # Get shift values from user
    shift1 = _get_int("Enter shift1 value (integer): ")
    shift2 = _get_int("Enter shift2 value (integer): ")

    # Shared options (extensible)
    options = {"encoding": kwargs.get("encoding", "utf-8")}

    # Perform encryption
    encrypt_file(shift1=shift1, shift2=shift2, **options)
    print("[INFO] Encryption complete. Encrypted text saved to 'encrypted_text.txt'.")

    # Perform decryption
    decrypt_file(shift1=shift1, shift2=shift2, **options)
    print("[INFO] Decryption complete. Decrypted text saved to 'decrypted_text.txt'.")

    # Verify correctness
    verify_files(**options)


# Run only when executed directly (not when imported)
if __name__ == "__main__":
    main()
