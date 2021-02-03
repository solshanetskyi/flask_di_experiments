from dataclasses import dataclass


@dataclass(frozen=True)
class FreshBooker:
    first_name: str
    last_name: str
