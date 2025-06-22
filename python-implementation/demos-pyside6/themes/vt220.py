"""VT220 Theme - Vintage Terminal"""

from . import FineUseTheme

VT220 = FineUseTheme(
    name="VT220",
    colors={
        'bg': '#000000',
        'surface': '#001100',
        'border': '#00aa00',
        'text': '#00ff00',
        'comment': '#008800',
        'accent': '#00cc00',
        'success': '#00ff00',
        'warning': '#ffff00',
        'error': '#ff0000',
        'info': '#00ffff'
    }
)
