"""
Fine Use Design System - PyQt Implementation
==========================================

Complete PyQt5/6 component library that perfectly matches 
the Fine Use web implementation using QSS (Qt Style Sheets).

Usage:
    from fine_use_pyqt import FineUseApp, FineUseButton
    
    app = FineUseApp()
    window = FineUseWindow("System Monitor")
    button = FineUseButton("START SERVICES", variant="primary")
"""

import sys
from typing import Optional, Callable, Dict, Any

try:
    from PyQt6.QtWidgets import *
    from PyQt6.QtCore import *
    from PyQt6.QtGui import *
    PYQT_VERSION = 6
except ImportError:
    try:
        from PyQt5.QtWidgets import *
        from PyQt5.QtCore import *
        from PyQt5.QtGui import *
        PYQT_VERSION = 5
    except ImportError:
        raise ImportError("PyQt5 or PyQt6 is required for Fine Use PyQt implementation")

from fine_use_core import fine_use, get_spacing, get_font, get_border_width


class FineUseStyleSheet:
    """
    Fine Use QSS (Qt Style Sheets) generator
    Converts Fine Use design tokens to QSS
    """
    
    @staticmethod
    def generate_app_stylesheet() -> str:
        """Generate complete application stylesheet"""
        colors = fine_use.colors
        spacing = fine_use.spacing
        borders = fine_use.borders
        
        return f"""
        /* Fine Use Application Styles */
        QMainWindow {{
            background-color: {colors['bg']};
            color: {colors['text']};
            font-family: "{fine_use.typography.FONT_FAMILY}";
            font-size: {fine_use.typography.FONT_SIZES['md']}px;
        }}
        
        QWidget {{
            background-color: {colors['bg']};
            color: {colors['text']};
            font-family: "{fine_use.typography.FONT_FAMILY}";
        }}
        
        /* Fine Use Button Base */
        QPushButton {{
            background-color: {colors['surface']};
            color: {colors['text']};
            border: {borders.THIN}px solid {colors['border']};
            padding: {spacing.MD}px {spacing.LG}px;
            font-family: "{fine_use.typography.FONT_FAMILY}";
            font-size: {fine_use.typography.FONT_SIZES['md']}px;
            font-weight: bold;
            text-transform: uppercase;
            min-height: 20px;
        }}
        
        QPushButton:hover {{
            background-color: {colors['border']};
            border-color: {colors['accent']};
        }}
        
        QPushButton:pressed {{
            background-color: {colors['accent']};
            color: {colors['bg']};
        }}
        
        QPushButton:focus {{
            outline: 3px solid {colors['accent']};
            outline-offset: 2px;
        }}
        
        /* Primary Button */
        QPushButton[variant="primary"] {{
            background-color: {colors['accent']};
            color: {colors['bg']};
            border-color: {colors['accent']};
        }}
        
        QPushButton[variant="primary"]:hover {{
            background-color: {colors['bg']};
            color: {colors['accent']};
        }}
        
        /* Success Button */
        QPushButton[variant="success"] {{
            background-color: {colors['success']};
            color: {colors['bg']};
            border-color: {colors['success']};
        }}
        
        QPushButton[variant="success"]:hover {{
            background-color: {colors['bg']};
            color: {colors['success']};
        }}
        
        /* Warning Button */
        QPushButton[variant="warning"] {{
            background-color: {colors['warning']};
            color: {colors['bg']};
            border-color: {colors['warning']};
        }}
        
        QPushButton[variant="warning"]:hover {{
            background-color: {colors['bg']};
            color: {colors['warning']};
        }}
        
        /* Error Button */
        QPushButton[variant="error"] {{
            background-color: {colors['error']};
            color: {colors['bg']};
            border-color: {colors['error']};
        }}
        
        QPushButton[variant="error"]:hover {{
            background-color: {colors['bg']};
            color: {colors['error']};
        }}
        
        /* Info Button */
        QPushButton[variant="info"] {{
            background-color: {colors['info']};
            color: {colors['bg']};
            border-color: {colors['info']};
        }}
        
        QPushButton[variant="info"]:hover {{
            background-color: {colors['bg']};
            color: {colors['info']};
        }}
        
        /* Fine Use Input Fields */
        QLineEdit {{
            background-color: {colors['surface']};
            color: {colors['text']};
            border: {borders.THIN}px solid {colors['border']};
            padding: {spacing.MD}px {spacing.LG}px;
            font-family: "{fine_use.typography.FONT_FAMILY}";
            font-size: {fine_use.typography.FONT_SIZES['md']}px;
            selection-background-color: {colors['accent']};
        }}
        
        QLineEdit:focus {{
            border-color: {colors['accent']};
            outline: 3px solid {colors['accent']};
            outline-offset: 2px;
        }}
        
        QTextEdit {{
            background-color: {colors['surface']};
            color: {colors['text']};
            border: {borders.THIN}px solid {colors['border']};
            padding: {spacing.MD}px;
            font-family: "{fine_use.typography.FONT_FAMILY}";
            font-size: {fine_use.typography.FONT_SIZES['md']}px;
            selection-background-color: {colors['accent']};
        }}
        
        QTextEdit:focus {{
            border-color: {colors['accent']};
            outline: 3px solid {colors['accent']};
            outline-offset: 2px;
        }}
        
        /* Fine Use Labels */
        QLabel {{
            color: {colors['text']};
            background-color: transparent;
            font-family: "{fine_use.typography.FONT_FAMILY}";
        }}
        
        QLabel[level="h1"] {{
            font-size: {fine_use.typography.FONT_SIZES['4xl']}px;
            font-weight: bold;
        }}
        
        QLabel[level="h2"] {{
            font-size: {fine_use.typography.FONT_SIZES['2xl']}px;
            font-weight: bold;
        }}
        
        QLabel[level="h3"] {{
            font-size: {fine_use.typography.FONT_SIZES['xl']}px;
            font-weight: bold;
        }}
        
        QLabel[color="comment"] {{
            color: {colors['comment']};
        }}
        
        QLabel[color="accent"] {{
            color: {colors['accent']};
        }}
        
        QLabel[color="success"] {{
            color: {colors['success']};
        }}
        
        QLabel[color="warning"] {{
            color: {colors['warning']};
        }}
        
        QLabel[color="error"] {{
            color: {colors['error']};
        }}
        
        QLabel[color="info"] {{
            color: {colors['info']};
        }}
        
        /* Fine Use Frames/Groups */
        QFrame {{
            background-color: {colors['surface']};
            border: {borders.THIN}px solid {colors['border']};
            padding: {spacing.LG}px;
        }}
        
        QGroupBox {{
            background-color: {colors['surface']};
            border: {borders.THIN}px solid {colors['border']};
            font-family: "{fine_use.typography.FONT_FAMILY}";
            font-size: {fine_use.typography.FONT_SIZES['lg']}px;
            font-weight: bold;
            color: {colors['text']};
            padding: {spacing.LG}px;
            margin-top: {spacing.MD}px;
        }}
        
        QGroupBox::title {{
            subcontrol-origin: margin;
            left: {spacing.MD}px;
            padding: 0 {spacing.SM}px 0 {spacing.SM}px;
        }}
        
        /* Fine Use Tables */
        QTableWidget {{
            background-color: {colors['surface']};
            alternate-background-color: {colors['bg']};
            color: {colors['text']};
            border: {borders.THIN}px solid {colors['border']};
            font-family: "{fine_use.typography.FONT_FAMILY}";
            font-size: {fine_use.typography.FONT_SIZES['md']}px;
            gridline-color: {colors['border']};
            selection-background-color: {colors['accent']};
            selection-color: {colors['bg']};
        }}
        
        QHeaderView::section {{
            background-color: {colors['border']};
            color: {colors['text']};
            border: {borders.THIN}px solid {colors['border']};
            padding: {spacing.MD}px;
            font-weight: bold;
            text-transform: uppercase;
        }}
        
        /* Fine Use Scrollbars */
        QScrollBar:vertical {{
            background-color: {colors['surface']};
            width: 16px;
            border: {borders.THIN}px solid {colors['border']};
        }}
        
        QScrollBar::handle:vertical {{
            background-color: {colors['border']};
            min-height: 20px;
        }}
        
        QScrollBar::handle:vertical:hover {{
            background-color: {colors['accent']};
        }}
        
        QScrollBar:horizontal {{
            background-color: {colors['surface']};
            height: 16px;
            border: {borders.THIN}px solid {colors['border']};
        }}
        
        QScrollBar::handle:horizontal {{
            background-color: {colors['border']};
            min-width: 20px;
        }}
        
        QScrollBar::handle:horizontal:hover {{
            background-color: {colors['accent']};
        }}
        
        /* Fine Use Combo Box */
        QComboBox {{
            background-color: {colors['surface']};
            color: {colors['text']};
            border: {borders.THIN}px solid {colors['border']};
            padding: {spacing.MD}px {spacing.LG}px;
            font-family: "{fine_use.typography.FONT_FAMILY}";
            font-size: {fine_use.typography.FONT_SIZES['md']}px;
        }}
        
        QComboBox:focus {{
            border-color: {colors['accent']};
            outline: 3px solid {colors['accent']};
            outline-offset: 2px;
        }}
        
        QComboBox QAbstractItemView {{
            background-color: {colors['surface']};
            color: {colors['text']};
            border: {borders.THIN}px solid {colors['border']};
            selection-background-color: {colors['accent']};
            selection-color: {colors['bg']};
        }}
        """


class FineUseApp(QApplication):
    """
    Fine Use PyQt Application
    Sets up the application with Fine Use styling
    """
    
    def __init__(self, theme: str = "github-dark"):
        super().__init__(sys.argv)
        
        # Set Fine Use theme
        if hasattr(fine_use, 'set_theme'):
            from fine_use_core import FineUseTheme
            theme_enum = getattr(FineUseTheme, theme.upper().replace('-', '_'))
            fine_use.set_theme(theme_enum)
        
        # Apply Fine Use stylesheet
        self.setStyleSheet(FineUseStyleSheet.generate_app_stylesheet())
        
        # Set application properties
        self.setApplicationName("Fine Use Application")
        self.setOrganizationName("Fine Use Design System")
        
        # Set default font
        font = QFont(fine_use.typography.FONT_FAMILY)
        font.setPixelSize(fine_use.typography.FONT_SIZES['md'])
        self.setFont(font)


class FineUseWindow(QMainWindow):
    """
    Fine Use main window with proper styling and layout
    """
    
    def __init__(self, title: str = "Fine Use Application", width: int = 1400, height: int = 900):
        super().__init__()
        
        self.setWindowTitle(title)
        self.resize(width, height)
        
        # Create central widget with Fine Use layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Main layout with Fine Use spacing
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(
            get_spacing('xxl'), get_spacing('xxl'),
            get_spacing('xxl'), get_spacing('xxl')
        )
        self.main_layout.setSpacing(get_spacing('xl'))


class FineUseButton(QPushButton):
    """
    Fine Use styled button with exact web implementation
    """
    
    def __init__(
        self,
        text: str = "",
        variant: str = "secondary",
        size: str = "md",
        parent: Optional[QWidget] = None
    ):
        super().__init__(text.upper(), parent)
        
        # Set variant property for QSS styling
        self.setProperty("variant", variant)
        
        # Set size-specific properties
        self._apply_size_styling(size)
        
        # Ensure styling is applied
        self.style().unpolish(self)
        self.style().polish(self)
    
    def _apply_size_styling(self, size: str):
        """Apply size-specific styling"""
        size_map = {
            'sm': ('sm', 'xs'),
            'md': ('md', 'md'),
            'lg': ('lg', 'lg'),
            'xl': ('xl', 'xl')
        }
        
        font_size, padding_size = size_map.get(size, ('md', 'md'))
        
        # Set font size
        font = self.font()
        font.setPixelSize(fine_use.typography.FONT_SIZES[font_size])
        font.setWeight(QFont.Weight.Bold if hasattr(QFont.Weight, 'Bold') else QFont.Bold)
        self.setFont(font)
        
        # Set padding
        padding = get_spacing(padding_size)
        self.setStyleSheet(f"padding: {padding}px {padding * 2}px;")


class FineUseLabel(QLabel):
    """
    Fine Use styled label with typography hierarchy
    """
    
    def __init__(
        self,
        text: str = "",
        level: str = "body",
        color: str = "text",
        parent: Optional[QWidget] = None
    ):
        super().__init__(text, parent)
        
        # Set properties for QSS styling
        self.setProperty("level", level)
        self.setProperty("color", color)
        
        # Apply text transformation for headers
        if level.startswith('h'):
            self.setText(text.upper())
        
        # Ensure styling is applied
        self.style().unpolish(self)
        self.style().polish(self)


class FineUseFrame(QFrame):
    """
    Fine Use styled frame for component grouping
    """
    
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        
        # Set frame style
        self.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Plain)
        self.setLineWidth(get_border_width('thin'))
        
        # Set background
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(fine_use.colors['surface']))
        self.setPalette(palette)


class FineUseLineEdit(QLineEdit):
    """
    Fine Use styled line edit input
    """
    
    def __init__(
        self,
        placeholder: str = "",
        size: str = "md",
        parent: Optional[QWidget] = None
    ):
        super().__init__(parent)
        
        if placeholder:
            self.setPlaceholderText(placeholder)
        
        # Set font size
        font = self.font()
        font.setPixelSize(fine_use.typography.FONT_SIZES[size])
        self.setFont(font)


class FineUseButtonGrid(QWidget):
    """
    Fine Use button grid with perfect alignment
    """
    
    def __init__(
        self,
        layout: str = "2x2",
        gap: int = None,
        parent: Optional[QWidget] = None
    ):
        super().__init__(parent)
        
        if gap is None:
            gap = get_spacing('md')
        
        # Create grid layout
        self.grid_layout = QGridLayout(self)
        self.grid_layout.setSpacing(gap)
        
        # Configure layout based on type
        self.layout_type = layout
        self.buttons = []
        
        # Set uniform sizing
        self.grid_layout.setRowStretch(0, 1)
        self.grid_layout.setColumnStretch(0, 1)
    
    def add_button(
        self,
        text: str,
        variant: str = "secondary",
        callback: Optional[Callable] = None
    ) -> FineUseButton:
        """Add button to grid with automatic positioning"""
        button = FineUseButton(text, variant, parent=self)
        
        if callback:
            button.clicked.connect(callback)
        
        # Calculate position based on layout
        if self.layout_type == "2x2":
            row = len(self.buttons) // 2
            col = len(self.buttons) % 2
        elif self.layout_type == "1x4":
            row = len(self.buttons)
            col = 0
        elif self.layout_type == "halves":
            row = 0
            col = len(self.buttons)
        elif self.layout_type == "thirds":
            row = 0
            col = len(self.buttons)
        else:
            row = len(self.buttons) // 2
            col = len(self.buttons) % 2
        
        self.grid_layout.addWidget(button, row, col)
        
        # Ensure equal sizing
        self.grid_layout.setRowStretch(row, 1)
        self.grid_layout.setColumnStretch(col, 1)
        
        self.buttons.append(button)
        return button


# Example application
def create_demo_app():
    """Create a demo application showing Fine Use PyQt components"""
    app = FineUseApp(theme="github-dark")
    
    window = FineUseWindow("Fine Use PyQt Demo")
    
    # Header
    header = FineUseLabel("FINE USE PYQT DEMO", level="h1")
    window.main_layout.addWidget(header)
    
    # Subtitle
    subtitle = FineUseLabel(
        "Complete design system implementation for PyQt5/6",
        level="body",
        color="comment"
    )
    window.main_layout.addWidget(subtitle)
    
    # Component group
    component_group = QGroupBox("BUTTON VARIANTS")
    component_layout = QVBoxLayout(component_group)
    
    # Button grid
    button_grid = FineUseButtonGrid(layout="2x2")
    button_grid.add_button("PRIMARY ACTION", "primary")
    button_grid.add_button("SUCCESS ACTION", "success")
    button_grid.add_button("WARNING ACTION", "warning")
    button_grid.add_button("DANGER ACTION", "error")
    
    component_layout.addWidget(button_grid)
    window.main_layout.addWidget(component_group)
    
    # Input group
    input_group = QGroupBox("TEXT INPUT")
    input_layout = QVBoxLayout(input_group)
    
    text_input = FineUseLineEdit(placeholder="Enter server name...")
    input_layout.addWidget(text_input)
    
    window.main_layout.addWidget(input_group)
    
    # Add stretch to push content to top
    window.main_layout.addStretch()
    
    window.show()
    return app, window


if __name__ == "__main__":
    app, window = create_demo_app()
    sys.exit(app.exec())
