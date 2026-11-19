"""
Custom template filters for the advisor app.
Provides formatting helpers like Indian number format.
"""
from django import template

register = template.Library()


@register.filter
def format_inr(value):
    """Format a number with commas (Indian style display)."""
    try:
        return "{:,}".format(int(value))
    except (ValueError, TypeError):
        return "0"


@register.filter
def score_percent(value):
    """Convert score to percentage for progress bar width."""
    try:
        pct = int(float(value) / 150 * 100)
        return max(10, min(pct, 100))
    except (ValueError, TypeError):
        return 10
