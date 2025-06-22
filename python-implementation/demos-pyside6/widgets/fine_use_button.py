"""
Fine Use Design System - Button Component
Perfect button styling matching HTML demos exactly
"""

from PySide6.QtWidgets import QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont

class FineUseButton(QPushButton):
    """Perfect Fine Use button with exact HTML demo styling"""
    
    def __init__(self, text: str = "BUTTON", variant: str = "", parent=None):
        super().__init__(text.upper(), parent)
        self.variant = variant
        self.init_styling()
    
    def init_styling(self):
        """Initialize button with perfect Fine Use styling"""
        # Set object name for CSS targeting
        self.setObjectName(self.variant if self.variant else "default")
        
        # Exact Fine Use button specifications
        self.setMinimumHeight(48)  # Exact 48px minimum height
        self.setMinimumWidth(120)  # Minimum width for consistency
        
        # Force uppercase text
        self.setText(self.text().upper())
        
        # Base styling (overridden by QSS)
        self.setStyleSheet(f"""
            QPushButton {{
                font-family: 'Fira Code', monospace;
                font-size: 14px;
                font-weight: 700;
                text-transform: uppercase;
                padding: 12px 24px;
                min-height: 48px;
                border-radius: 0px;
                border: 2px solid;
            }}
        """)
    
    def set_variant(self, variant: str):
        """Change button variant"""
        self.variant = variant
        self.setObjectName(variant if variant else "default")
    
    def setText(self, text: str):
        """Override to force uppercase"""
        super().setText(text.upper())


class FineUseButtonGroup(QWidget):
    """Button group with perfect grid alignment"""
    
    def __init__(self, orientation: str = "horizontal", parent=None):
        super().__init__(parent)
        self.orientation = orientation
        self.buttons = []
        self.init_ui()
    
    def init_ui(self):
        """Initialize the button group layout"""
        if self.orientation == "horizontal":
            self.layout = QHBoxLayout(self)
        else:
            self.layout = QVBoxLayout(self)
        
        self.layout.setSpacing(12)  # Exact 12px spacing
        self.layout.setContentsMargins(0, 0, 0, 0)
    
    def add_button(self, text: str, variant: str = "", callback=None) -> FineUseButton:
        """Add a button to the group"""
        button = FineUseButton(text, variant)
        
        if callback:
            button.clicked.connect(callback)
        
        self.layout.addWidget(button)
        self.buttons.append(button)
        
        return button
    
    def get_button(self, index: int) -> FineUseButton:
        """Get button by index"""
        if 0 <= index < len(self.buttons):
            return self.buttons[index]
        return None


class FineUseButtonGrid(QWidget):
    """Perfect button grid system matching HTML demos exactly"""
    
    def __init__(self, rows: int = 2, cols: int = 2, parent=None):
        super().__init__(parent)
        self.rows = rows
        self.cols = cols
        self.buttons = []
        self.init_ui()
    
    def init_ui(self):
        """Initialize the grid with perfect alignment"""
        # Grid layout with exact Fine Use spacing
        self.grid_layout = QGridLayout(self)
        self.grid_layout.setSpacing(12)  # Exact 12px grid gaps
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        
        # Make columns equal width
        for col in range(self.cols):
            self.grid_layout.setColumnStretch(col, 1)
        
        # Create button matrix
        for row in range(self.rows):
            button_row = []
            for col in range(self.cols):
                # Create placeholder button
                button = FineUseButton("BUTTON")
                
                # Set size policy for perfect grid alignment
                size_policy = button.sizePolicy()
                size_policy.setHorizontalPolicy(size_policy.Policy.Expanding)
                size_policy.setVerticalPolicy(size_policy.Policy.Fixed)
                button.setSizePolicy(size_policy)
                
                self.grid_layout.addWidget(button, row, col)
                button_row.append(button)
            
            self.buttons.append(button_row)
    
    def set_button(self, row: int, col: int, text: str, variant: str = "", callback=None):
        """Configure a specific button in the grid"""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            button = self.buttons[row][col]
            button.setText(text.upper())
            button.set_variant(variant)
            
            if callback:
                # Disconnect any existing connections
                try:
                    button.clicked.disconnect()
                except:
                    pass
                button.clicked.connect(callback)
    
    def get_button(self, row: int, col: int) -> FineUseButton:
        """Get button at specific grid position"""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.buttons[row][col]
        return None
    
    def set_grid_buttons(self, button_config: list):
        """Set multiple buttons from configuration"""
        for config in button_config:
            row = config.get('row', 0)
            col = config.get('col', 0)
            text = config.get('text', 'BUTTON')
            variant = config.get('variant', '')
            callback = config.get('callback', None)
            
            self.set_button(row, col, text, variant, callback)


# Predefined button grid configurations for common layouts
class FineUseButtonGridPresets:
    """Common button grid configurations"""
    
    @staticmethod
    def system_controls_2x2():
        """System control 2x2 grid like HTML demos"""
        return [
            {'row': 0, 'col': 0, 'text': 'START SERVICES', 'variant': 'primary'},
            {'row': 0, 'col': 1, 'text': 'STOP ALL PROCESSES', 'variant': ''},
            {'row': 1, 'col': 0, 'text': 'RESTART LOAD BALANCER', 'variant': ''},
            {'row': 1, 'col': 1, 'text': 'EMERGENCY SHUTDOWN', 'variant': 'danger'}
        ]
    
    @staticmethod
    def deployment_controls():
        """Deployment control buttons"""
        return [
            {'row': 0, 'col': 0, 'text': 'DEPLOY', 'variant': 'primary'},
            {'row': 0, 'col': 1, 'text': 'ROLLBACK', 'variant': ''},
            {'row': 1, 'col': 0, 'text': 'BACKUP', 'variant': 'info'},
            {'row': 1, 'col': 1, 'text': 'MAINTENANCE', 'variant': ''}
        ]
    
    @staticmethod
    def confirmation_buttons():
        """Confirmation dialog buttons"""
        return [
            {'row': 0, 'col': 0, 'text': 'CONFIRM', 'variant': 'primary'},
            {'row': 0, 'col': 1, 'text': 'CANCEL', 'variant': ''}
        ]
    
    @staticmethod
    def form_actions():
        """Form action buttons"""
        return [
            {'row': 0, 'col': 0, 'text': 'SAVE CONFIGURATION', 'variant': 'primary'},
            {'row': 0, 'col': 1, 'text': 'RESET TO DEFAULTS', 'variant': ''},
            {'row': 1, 'col': 0, 'text': 'TEST CONNECTION', 'variant': 'info'},
            {'row': 1, 'col': 1, 'text': 'DELETE SETTINGS', 'variant': 'danger'}
        ]


class FineUseActionButtons(QWidget):
    """Pre-configured action button sets"""
    
    # Signals for common actions
    primary_clicked = Signal()
    secondary_clicked = Signal()
    danger_clicked = Signal()
    info_clicked = Signal()
    
    def __init__(self, button_set: str = "system_controls", parent=None):
        super().__init__(parent)
        self.button_set = button_set
        self.init_ui()
    
    def init_ui(self):
        """Initialize with predefined button set"""
        # Create 2x2 grid by default
        self.button_grid = FineUseButtonGrid(2, 2)
        
        # Set layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.button_grid)
        
        # Configure buttons based on set
        self._configure_button_set()
    
    def _configure_button_set(self):
        """Configure buttons based on the selected set"""
        if self.button_set == "system_controls":
            config = FineUseButtonGridPresets.system_controls_2x2()
            
            # Connect to signals
            self.button_grid.set_button(0, 0, config[0]['text'], config[0]['variant'], 
                                       lambda: self.primary_clicked.emit())
            self.button_grid.set_button(0, 1, config[1]['text'], config[1]['variant'],
                                       lambda: self.secondary_clicked.emit())
            self.button_grid.set_button(1, 0, config[2]['text'], config[2]['variant'],
                                       lambda: self.info_clicked.emit())
            self.button_grid.set_button(1, 1, config[3]['text'], config[3]['variant'],
                                       lambda: self.danger_clicked.emit())
        
        elif self.button_set == "deployment":
            config = FineUseButtonGridPresets.deployment_controls()
            for item in config:
                self.button_grid.set_button(
                    item['row'], item['col'], item['text'], item['variant']
                )
        
        elif self.button_set == "form_actions":
            config = FineUseButtonGridPresets.form_actions()
            for item in config:
                self.button_grid.set_button(
                    item['row'], item['col'], item['text'], item['variant']
                )
    
    def get_grid(self) -> FineUseButtonGrid:
        """Get the underlying button grid"""
        return self.button_grid
