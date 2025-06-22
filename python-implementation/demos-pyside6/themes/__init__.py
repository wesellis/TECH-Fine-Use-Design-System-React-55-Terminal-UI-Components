# Fine Use Design System - PySide6 Themes
# COMPLETE REWRITE - Pixel-perfect matching HTML demos

from typing import Dict, Any

# Core Fine Use Themes - Exact color values from CSS
FINE_USE_THEMES = {
    "github-dark": {
        "name": "Dark Mode",
        "colors": {
            "bg": "#0d1117",
            "surface": "#161b22", 
            "border": "#30363d",
            "text": "#f0f6fc",
            "comment": "#7d8590",
            "success": "#238636",
            "warning": "#d29922",
            "error": "#da3633",
            "info": "#1f6feb",
            "accent": "#58a6ff",
            "orange": "#fd7d00"
        }
    }
}

def get_theme_qss(theme_name: str) -> str:
    """Generate PERFECT QSS stylesheet matching HTML demos exactly"""
    if theme_name not in FINE_USE_THEMES:
        theme_name = "github-dark"
    
    theme = FINE_USE_THEMES[theme_name]
    colors = theme["colors"]
    
    return f"""
/* Fine Use Design System - PERFECT PIXEL MATCHING */

/* === MAIN APPLICATION === */
QMainWindow, QWidget {{
    background-color: {colors['bg']};
    color: {colors['text']};
    font-family: 'Fira Code', 'SF Mono', 'Monaco', 'Consolas', monospace;
    font-size: 14px;
    font-weight: 500;
}}

/* === REMOVE ALL SCROLLBARS COMPLETELY === */
QScrollBar:vertical, QScrollBar:horizontal {{
    width: 0px;
    height: 0px;
    background: transparent;
    border: none;
}}

QScrollBar::handle, QScrollBar::add-line, QScrollBar::sub-line, QScrollBar::add-page, QScrollBar::sub-page {{
    background: transparent;
    border: none;
    width: 0px;
    height: 0px;
}}

/* === PERFECT THEME SELECTOR === */
QComboBox {{
    background-color: {colors['surface']};
    border: 2px solid {colors['border']};
    color: {colors['text']};
    padding: 8px 16px;
    font-family: 'Fira Code', monospace;
    font-size: 14px;
    font-weight: 700;
    text-transform: uppercase;
    min-width: 200px;
    min-height: 32px;
    border-radius: 0px;
}}

QComboBox:hover {{
    border-color: {colors['accent']};
}}

QComboBox::drop-down {{
    border: none;
    width: 30px;
    background-color: transparent;
}}

QComboBox::down-arrow {{
    width: 0;
    height: 0;
    border-left: 6px solid transparent;
    border-right: 6px solid transparent;
    border-top: 8px solid {colors['accent']};
    margin-right: 8px;
}}

QComboBox QAbstractItemView {{
    background-color: {colors['surface']};
    border: 2px solid {colors['border']};
    color: {colors['text']};
    selection-background-color: {colors['accent']};
    selection-color: {colors['bg']};
    font-family: 'Fira Code', monospace;
    font-weight: 700;
    outline: none;
    border-radius: 0px;
}}

/* === PERFECT HEADERS === */
QLabel[objectName="h1"] {{
    font-family: 'Fira Code', monospace;
    font-size: 24px;
    font-weight: 700;
    color: {colors['text']};
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin: 0px;
    padding: 0px;
}}

QLabel[objectName="h2"] {{
    font-family: 'Fira Code', monospace;
    font-size: 18px;
    font-weight: 700;
    color: {colors['text']};
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin: 0px;
    padding: 0px;
}}

QLabel[objectName="h3"] {{
    font-family: 'Fira Code', monospace;
    font-size: 16px;
    font-weight: 700;
    color: {colors['text']};
    text-transform: uppercase;
    margin: 0px;
    padding: 0px;
}}

/* === PERFECT CONTAINERS === */
QWidget[objectName="fine-use-component"] {{
    background-color: {colors['surface']};
    border: 2px solid {colors['border']};
    border-radius: 0px;
    padding: 16px;
}}

QWidget[objectName="fine-use-component"]:hover {{
    border-color: {colors['accent']};
}}

/* === PERFECT METRIC VALUES === */
QLabel[objectName="metric-value"] {{
    font-family: 'Fira Code', monospace;
    font-size: 36px;
    font-weight: 700;
    color: {colors['accent']};
    qproperty-alignment: AlignCenter;
    margin: 0px;
    padding: 0px;
}}

QLabel[objectName="metric-label"] {{
    font-family: 'Fira Code', monospace;
    font-size: 12px;
    font-weight: 700;
    color: {colors['text']};
    text-transform: uppercase;
    qproperty-alignment: AlignCenter;
    margin-top: 8px;
    padding: 0px;
}}

/* === PERFECT PROGRESS BARS - EXACTLY 16PX === */
QProgressBar {{
    border: 2px solid {colors['border']};
    background-color: {colors['surface']};
    text-align: center;
    height: 16px;
    max-height: 16px;
    min-height: 16px;
    font-family: 'Fira Code', monospace;
    font-size: 11px;
    font-weight: 700;
    color: {colors['text']};
    border-radius: 0px;
}}

QProgressBar::chunk {{
    background-color: {colors['success']};
    border-radius: 0px;
    border: none;
}}

QProgressBar[objectName="warning"]::chunk {{
    background-color: {colors['warning']};
}}

QProgressBar[objectName="error"]::chunk {{
    background-color: {colors['error']};
}}

QProgressBar[objectName="info"]::chunk {{
    background-color: {colors['info']};
}}

/* === PERFECT BUTTONS - EXACTLY LIKE HTML === */
QPushButton {{
    background-color: {colors['surface']};
    border: 2px solid {colors['border']};
    color: {colors['text']};
    font-family: 'Fira Code', monospace;
    font-size: 14px;
    font-weight: 700;
    text-transform: uppercase;
    padding: 12px 24px;
    min-height: 48px;
    border-radius: 0px;
    text-align: center;
}}

QPushButton:hover {{
    border-color: {colors['accent']};
    background-color: {colors['border']};
}}

QPushButton:pressed {{
    background-color: {colors['accent']};
    color: {colors['bg']};
}}

/* PRIMARY BUTTON - ACCENT BACKGROUND */
QPushButton[objectName="primary"] {{
    background-color: {colors['accent']};
    border-color: {colors['accent']};
    color: {colors['bg']};
}}

QPushButton[objectName="primary"]:hover {{
    background-color: {colors['bg']};
    color: {colors['accent']};
    border-color: {colors['accent']};
}}

/* DANGER BUTTON - RED */
QPushButton[objectName="danger"] {{
    background-color: {colors['error']};
    border-color: {colors['error']};
    color: {colors['bg']};
}}

QPushButton[objectName="danger"]:hover {{
    background-color: {colors['bg']};
    color: {colors['error']};
    border-color: {colors['error']};
}}

/* INFO BUTTON - BLUE */
QPushButton[objectName="info"] {{
    background-color: {colors['info']};
    border-color: {colors['info']};
    color: {colors['bg']};
}}

QPushButton[objectName="info"]:hover {{
    background-color: {colors['bg']};
    color: {colors['info']};
    border-color: {colors['info']};
}}

/* SUCCESS BUTTON - GREEN */
QPushButton[objectName="success"] {{
    background-color: {colors['success']};
    border-color: {colors['success']};
    color: {colors['bg']};
}}

QPushButton[objectName="success"]:hover {{
    background-color: {colors['bg']};
    color: {colors['success']};
    border-color: {colors['success']};
}}

/* === PERFECT LOG TERMINAL === */
QTextEdit {{
    background-color: {colors['bg']};
    border: 2px solid {colors['border']};
    color: {colors['text']};
    font-family: 'Fira Code', monospace;
    font-size: 12px;
    font-weight: 500;
    padding: 16px;
    selection-background-color: {colors['accent']};
    selection-color: {colors['bg']};
    border-radius: 0px;
}}

/* === PERFECT SERVICE STATUS === */
QWidget[objectName="status-indicator"] {{
    background-color: {colors['surface']};
    border: 2px solid {colors['border']};
    border-radius: 0px;
    padding: 16px;
}}

QLabel[objectName="service-name"] {{
    font-family: 'Fira Code', monospace;
    font-size: 14px;
    font-weight: 700;
    color: {colors['text']};
    text-transform: uppercase;
    qproperty-alignment: AlignCenter;
    margin: 0px;
    padding: 0px;
}}

QLabel[objectName="service-status"] {{
    font-family: 'Fira Code', monospace;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    qproperty-alignment: AlignCenter;
    padding: 4px 8px;
    border: 1px solid {colors['border']};
    border-radius: 0px;
    margin-top: 8px;
}}

QLabel[objectName="status-operational"] {{
    background-color: {colors['success']};
    color: {colors['bg']};
    border-color: {colors['success']};
}}

QLabel[objectName="status-degraded"] {{
    background-color: {colors['warning']};
    color: {colors['bg']};
    border-color: {colors['warning']};
}}

QLabel[objectName="status-error"] {{
    background-color: {colors['error']};
    color: {colors['bg']};
    border-color: {colors['error']};
}}

QLabel[objectName="status-maintenance"] {{
    background-color: {colors['info']};
    color: {colors['bg']};
    border-color: {colors['info']};
}}

/* === PERFECT SPACING === */
QGridLayout {{
    spacing: 24px;
}}

QVBoxLayout {{
    spacing: 16px;
}}

QHBoxLayout {{
    spacing: 24px;
}}

"""

def get_available_themes() -> Dict[str, str]:
    """Get all available theme names and display names"""
    return {key: value["name"] for key, value in FINE_USE_THEMES.items()}

def get_theme_colors(theme_name: str) -> Dict[str, str]:
    """Get color palette for a specific theme"""
    if theme_name not in FINE_USE_THEMES:
        theme_name = "github-dark"
    return FINE_USE_THEMES[theme_name]["colors"]
