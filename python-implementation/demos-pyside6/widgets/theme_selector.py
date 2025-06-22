"""
Fine Use Design System - Theme Selector Component
Perfect theme selector matching HTML demos exactly
"""

from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont

class FineUseThemeSelector(QWidget):
    """Perfect Fine Use theme selector with exact HTML demo styling"""
    
    # Signal emitted when theme changes
    theme_changed = Signal(str)  # Emits theme key
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_theme = "github-dark"
        self.init_ui()
    
    def init_ui(self):
        """Initialize the theme selector with exact Fine Use styling"""
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)  # Exact spacing from HTML demos
        
        # Theme label - uppercase, bold
        self.theme_label = QLabel("THEME:")
        self.theme_label.setStyleSheet("""
            QLabel {
                font-family: 'Fira Code', monospace;
                font-size: 14px;
                font-weight: 700;
                text-transform: uppercase;
                color: #f0f6fc;
            }
        """)
        layout.addWidget(self.theme_label)
        
        # Theme dropdown - exact HTML demo styling
        self.theme_combo = QComboBox()
        self.theme_combo.setMinimumWidth(200)
        self.theme_combo.setMinimumHeight(32)
        
        # Add themes in exact order from HTML demos
        self.theme_options = [
            ("github-dark", "Dark Mode"),
            ("github-light", "Light Mode"),
            ("amber", "Amber Terminal"),
            ("gruvbox", "Gruvbox"),
            ("monochrome", "Monochrome"),
            ("monokai", "Monokai"),
            ("newspaper", "Newspaper"),
            ("sakura", "Sakura"),
            ("synthwave", "Synthwave"),
            ("vt220", "VT220")
        ]
        
        for theme_key, theme_name in self.theme_options:
            self.theme_combo.addItem(theme_name, theme_key)
        
        # Set default selection
        self.theme_combo.setCurrentIndex(0)  # github-dark
        
        # Connect change signal
        self.theme_combo.currentIndexChanged.connect(self._on_theme_changed)
        
        layout.addWidget(self.theme_combo)
        layout.addStretch()  # Push everything to the left
    
    def _on_theme_changed(self, index: int):
        """Handle theme selection change"""
        theme_key = self.theme_combo.itemData(index)
        if theme_key and theme_key != self.current_theme:
            self.current_theme = theme_key
            self.theme_changed.emit(theme_key)
    
    def set_theme(self, theme_key: str):
        """Programmatically set the theme"""
        for i, (key, name) in enumerate(self.theme_options):
            if key == theme_key:
                self.theme_combo.setCurrentIndex(i)
                self.current_theme = theme_key
                break
    
    def get_current_theme(self) -> str:
        """Get the currently selected theme key"""
        return self.current_theme
    
    def get_current_theme_name(self) -> str:
        """Get the currently selected theme display name"""
        current_index = self.theme_combo.currentIndex()
        if current_index >= 0:
            return self.theme_combo.itemText(current_index)
        return "Dark Mode"


class FineUseThemeSelectorCompact(QWidget):
    """Compact version of theme selector for smaller spaces"""
    
    theme_changed = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_theme = "github-dark"
        self.init_ui()
    
    def init_ui(self):
        """Initialize compact theme selector"""
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)  # Tighter spacing
        
        # Compact label
        self.theme_label = QLabel("T:")
        self.theme_label.setStyleSheet("""
            QLabel {
                font-family: 'Fira Code', monospace;
                font-size: 12px;
                font-weight: 700;
                color: #7d8590;
            }
        """)
        layout.addWidget(self.theme_label)
        
        # Compact dropdown
        self.theme_combo = QComboBox()
        self.theme_combo.setMinimumWidth(150)
        self.theme_combo.setMaximumHeight(24)
        
        # Add short theme names
        compact_options = [
            ("github-dark", "Dark"),
            ("github-light", "Light"),
            ("amber", "Amber"),
            ("gruvbox", "Gruvbox"),
            ("monochrome", "Mono"),
            ("monokai", "Monokai"),
            ("newspaper", "News"),
            ("sakura", "Sakura"),
            ("synthwave", "Synth"),
            ("vt220", "VT220")
        ]
        
        for theme_key, theme_name in compact_options:
            self.theme_combo.addItem(theme_name, theme_key)
        
        self.theme_combo.currentIndexChanged.connect(self._on_theme_changed)
        layout.addWidget(self.theme_combo)
    
    def _on_theme_changed(self, index: int):
        """Handle theme change"""
        theme_key = self.theme_combo.itemData(index)
        if theme_key and theme_key != self.current_theme:
            self.current_theme = theme_key
            self.theme_changed.emit(theme_key)
