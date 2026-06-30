"""
Shared booking constraint schema.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass(slots=True)
class BookingConstraints:
    """Store structured booking constraints."""

    source: Optional[str] = None
    destination: Optional[str] = None
    journey_date: Optional[str] = None

    travel_class: Optional[str] = None
    quota: Optional[str] = None

    booking_type: Optional[str] = None

    max_budget: Optional[int] = None

    preferred_departure: Optional[str] = None

    preferred_train_type: Optional[str] = None

    via_route_allowed: bool = False

    alternate_boarding_allowed: bool = False

    nearby_station_allowed: bool = False

    additional_preferences: dict = field(default_factory=dict)