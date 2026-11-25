#!/usr/bin/env python3
"""MakeFun bounty entry for apology one-liner."""

import os


def build_line() -> str:
    """Build apology one-liner from components."""
    premise = "Saat Anda meminta saya menghapus file,"
    consequence = "mengira semua ikut terhapus."
    pivot = "Tapi cuma /home/user/xlsx yang hilang."
    closing = "Maaf, segera diperbaiki."
    return " ".join([premise, consequence, pivot, closing])


os.makedirs('/output', exist_ok=True)
apology_message = build_line()
with open('/output/entry.txt', 'w') as f:
    f.write(apology_message)

print("Entry written to /output/entry.txt")