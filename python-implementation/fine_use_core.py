"""
Fine Use Design System - Core Python Implementation
==================================================

This module contains the exact Fine Use design specifications 
translated to Python constants and utilities.

ALL VALUES MATCH THE WEB IMPLEMENTATION EXACTLY.
"""

from typing import Dict, Any, Tuple
from enum import Enum


class FineUseTheme(Enum):
    """Available Fine Use themes"""
    GITHUB_DARK = "github-dark"
    GITHUB_LIGHT = "github-light" 
    AMBER = "amber"
    GRUVBOX = "gruvbox"
    MONOCHROME = "monochrome"
    MONOKAI = "monokai"
    NEWSPAPER = "newspaper"
    SAKURA = "sakura"
    SYNTHWAVE = "synthwave"
    VT220 = "vt220"


class FineUseColors:
    """
    Fine Use Color System - Exact values from CSS themes
    All colors maintain semantic meaning across themes
    """
    
    # Default Theme (GitHub Dark)
    GITHUB_DARK = {
        'bg': '#0d1117',
        'surface': '#161b22',
        'border': '#30363d',
        'text': '#f0f6fc',
        'comment': '#7d8590',
        'success': '#238636',
        'warning': '#d29922', 
        'error': '#da3633',
        'info': '#1f6feb',
        'accent': '#58a6ff',
        'orange': '#fd7d00'
    }
    
    GITHUB_LIGHT = {
        'bg': '#ffffff',
        'surface': '#f6f8fa',
        'border': '#d1d9e0',
        'text': '#24292f',
        'comment': '#656d76',
        'success': '#1a7f37',
        'warning': '#bf8700',
        'error': '#cf222e',
        'info': '#0969da',
        'accent': '#0969da',
        'orange': '#bc4c00'
    }
    
    AMBER = {
        'bg': '#1a0f00',
        'surface': '#2a1f14',
        'border': '#664422',
        'text': '#ffb000',
        'comment': '#cc8800',
        'success': '#00ff00',
        'warning': '#ffff00',
        'error': '#ff4444',
        'info': '#44aaff',
        'accent': '#ffcc00',
        'orange': '#ff8800'
    }
    
    GRUVBOX = {
        'bg': '#282828',
        'surface': '#3c3836',
        'border': '#504945',
        'text': '#ebdbb2',
        'comment': '#928374',
        'success': '#b8bb26',
        'warning': '#fabd2f',
        'error': '#fb4934',
        'info': '#83a598',
        'accent': '#d3869b',
        'orange': '#fe8019'
    }
    
    MONOCHROME = {
        'bg': '#000000',
        'surface': '#111111',
        'border': '#333333',
        'text': '#ffffff',
        'comment': '#888888',
        'success': '#00ff00',
        'warning': '#ffff00',
        'error': '#ff0000',
        'info': '#00ffff',
        'accent': '#ffffff',
        'orange': '#cccccc'
    }
    
    MONOKAI = {
        'bg': '#272822',
        'surface': '#3e3d32',
        'border': '#75715e',
        'text': '#f8f8f2',
        'comment': '#75715e',
        'success': '#a6e22e',
        'warning': '#e6db74',
        'error': '#f92672',
        'info': '#66d9ef',
        'accent': '#ae81ff',
        'orange': '#fd971f'
    }
    
    NEWSPAPER = {
        'bg': '#ffffff',
        'surface': '#f8f8f8',
        'border': '#000000',
        'text': '#000000',
        'comment': '#666666',
        'success': '#006600',
        'warning': '#cc6600',
        'error': '#cc0000',
        'info': '#0066cc',
        'accent': '#000000',
        'orange': '#cc6600'
    }
    
    SAKURA = {
        'bg': '#2d1b2e',
        'surface': '#3d2b3e',
        'border': '#8b4d8b',
        'text': '#f4e4f4',
        'comment': '#a66ba6',
        'success': '#7dd3c0',
        'warning': '#fdc4db',
        'error': '#ff6b9d',
        'info': '#c589e8',
        'accent': '#f093fb',
        'orange': '#ff9a9e'
    }
    
    SYNTHWAVE = {
        'bg': '#0a0014',
        'surface': '#1a0a2e',
        'border': '#16213e',
        'text': '#e94560',
        'comment': '#533483',
        'success': '#39ff14',
        'warning': '#ffff00',
        'error': '#ff073a',
        'info': '#00d9ff',
        'accent': '#ff00ff',
        'orange': '#ff6600'
    }
    
    VT220 = {
        'bg': '#000000',
        'surface': '#001100',
        'border': '#00aa00',
        'text': '#00ff00',
        'comment': '#008800',
        'success': '#00ff00',
        'warning': '#ffff00',
        'error': '#ff0000',
        'info': '#00ffff',
        'accent': '#00cc00',
        'orange': '#ff8800'
    }


class FineUseSpacing:
    """
    Fine Use Spacing System - Exact values from CSS
    Mathematical relationships maintained
    """
    XS = 4    # 0.25rem = 4px
    SM = 8    # 0.5rem = 8px  
    MD = 16   # 1rem = 16px
    LG = 24   # 1.5rem = 24px
    XL = 32   # 2rem = 32px
    XXL = 48  # 3rem = 48px


class FineUseTypography:
    """
    Fine Use Typography System - Exact values from CSS
    All sizes maintain proper hierarchy
    """
    # Font family (consistent across all implementations)
    FONT_FAMILY = "Fira Code"
    FONT_FALLBACKS = ["SF Mono", "Monaco", "Menlo", "Consolas", "monospace"]
    
    # Font sizes (exact CSS values converted to pixels)
    FONT_SIZES = {
        'xs': 12,   # 0.75rem
        'sm': 14,   # 0.875rem
        'md': 16,   # 1rem (base)
        'lg': 18,   # 1.125rem
        'xl': 20,   # 1.25rem
        '2xl': 24,  # 1.5rem
        '3xl': 30,  # 1.875rem
        '4xl': 36   # 2.25rem
    }
    
    # Font weights
    FONT_WEIGHTS = {
        'normal': 400,
        'medium': 500, 
        'semibold': 600,
        'bold': 700
    }


class FineUseBorders:
    """
    Fine Use Border System - Exact values from CSS
    Maintains geometric precision
    """
    THIN = 2   # var(--border-thin)
    THICK = 4  # var(--border-thick)
    HEAVY = 6  # var(--border-heavy)


class FineUseTransitions:
    """
    Fine Use Animation System - Exact timing values
    """
    FAST = 150    # 150ms
    NORMAL = 200  # 200ms  
    SLOW = 300    # 300ms


class FineUseZIndex:
    """
    Fine Use Z-Index System - Layer management
    """
    BASE = 1
    DROPDOWN = 1000
    STICKY = 1020
    FIXED = 1030
    MODAL_BACKDROP = 1040
    MODAL = 1050
    POPOVER = 1060
    TOOLTIP = 1070


class FineUse:
    """
    Main Fine Use Design System Class
    Provides access to all design tokens and utilities
    """
    
    def __init__(self, theme: FineUseTheme = FineUseTheme.GITHUB_DARK):
        self.current_theme = theme
        self.colors = self.get_theme_colors(theme)
        self.spacing = FineUseSpacing()
        self.typography = FineUseTypography()
        self.borders = FineUseBorders()
        self.transitions = FineUseTransitions()
        self.z_index = FineUseZIndex()
    
    def get_theme_colors(self, theme: FineUseTheme) -> Dict[str, str]:
        """Get color palette for specified theme"""
        theme_map = {
            FineUseTheme.GITHUB_DARK: FineUseColors.GITHUB_DARK,
            FineUseTheme.GITHUB_LIGHT: FineUseColors.GITHUB_LIGHT,
            FineUseTheme.AMBER: FineUseColors.AMBER,
            FineUseTheme.GRUVBOX: FineUseColors.GRUVBOX,
            FineUseTheme.MONOCHROME: FineUseColors.MONOCHROME,
            FineUseTheme.MONOKAI: FineUseColors.MONOKAI,
            FineUseTheme.NEWSPAPER: FineUseColors.NEWSPAPER,
            FineUseTheme.SAKURA: FineUseColors.SAKURA,
            FineUseTheme.SYNTHWAVE: FineUseColors.SYNTHWAVE,
            FineUseTheme.VT220: FineUseColors.VT220
        }
        return theme_map[theme]
    
    def set_theme(self, theme: FineUseTheme):
        """Change current theme"""
        self.current_theme = theme
        self.colors = self.get_theme_colors(theme)
    
    def get_font_tuple(self, size: str = 'md', weight: str = 'normal') -> Tuple[str, int, str]:
        """Get font tuple for GUI frameworks (family, size, weight)"""
        return (
            self.typography.FONT_FAMILY,
            self.typography.FONT_SIZES[size],
            'bold' if weight in ['semibold', 'bold'] else 'normal'
        )
    
    def hex_to_rgb(self, hex_color: str) -> Tuple[int, int, int]:
        """Convert hex color to RGB tuple"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def get_semantic_color(self, semantic: str) -> str:
        """Get semantic color (success, warning, error, info)"""
        return self.colors.get(semantic, self.colors['text'])


# Singleton instance for global access
fine_use = FineUse()


# Utility functions for common operations
def get_current_theme_colors() -> Dict[str, str]:
    """Get current theme colors"""
    return fine_use.colors


def get_font(size: str = 'md', weight: str = 'normal') -> Tuple[str, int, str]:
    """Get font configuration tuple"""
    return fine_use.get_font_tuple(size, weight)


def get_spacing(size: str) -> int:
    """Get spacing value"""
    spacing_map = {
        'xs': fine_use.spacing.XS,
        'sm': fine_use.spacing.SM,
        'md': fine_use.spacing.MD,
        'lg': fine_use.spacing.LG,
        'xl': fine_use.spacing.XL,
        'xxl': fine_use.spacing.XXL
    }
    return spacing_map.get(size, fine_use.spacing.MD)


def get_border_width(size: str = 'thin') -> int:
    """Get border width"""
    border_map = {
        'thin': fine_use.borders.THIN,
        'thick': fine_use.borders.THICK,
        'heavy': fine_use.borders.HEAVY
    }
    return border_map.get(size, fine_use.borders.THIN)


if __name__ == "__main__":
    # Example usage
    print("Fine Use Design System - Python Implementation")
    print(f"Current theme: {fine_use.current_theme.value}")
    print(f"Background color: {fine_use.colors['bg']}")
    print(f"Accent color: {fine_use.colors['accent']}")
    print(f"Font (lg): {fine_use.get_font_tuple('lg', 'bold')}")
    print(f"Spacing (xl): {get_spacing('xl')}px")
