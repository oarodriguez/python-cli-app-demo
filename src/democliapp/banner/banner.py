"""Routines to generate ASCII banners."""
from dataclasses import dataclass
from typing import Optional

from art import text2art

HEADLINE_TEMPLATE = """
{headline}
"""


@dataclass
class Banner:
    """A banner built using ASCII art."""

    headline: str
    font_name: Optional[str] = None

    def __post_init__(self):
        """Post initialization tasks."""
        self.font_name = self.font_name or "standard"

    @property
    def text(self):
        """The banner's ASCII representation."""
        headline_ascii = text2art(self.headline, font=self.font_name)
        headline_content = HEADLINE_TEMPLATE.format(headline=headline_ascii)
        return headline_content
