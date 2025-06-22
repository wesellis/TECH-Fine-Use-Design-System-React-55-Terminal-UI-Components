"""
Fine Use Design System - Metric Widget Component
Pixel-perfect metric displays matching HTML demos exactly
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QProgressBar, QFrame, QGridLayout, QPushButton
from PySide6.QtCore import Qt, QTimer, Signal
from PySide6.QtGui import QFont
import random

class FineUseMetricWidget(QWidget):
    """Perfect Fine Use metric widget with exact HTML demo styling"""
    
    def __init__(self, label_text: str, initial_value: int = 0, max_value: int = 100, parent=None):
        super().__init__(parent)
        self.max_value = max_value
        self.current_value = initial_value
        self.label_text = label_text.upper()
        
        self.init_ui()
        self.setup_auto_update()
    
    def init_ui(self):
        """Initialize the metric widget with exact Fine Use styling"""
        # Main container with proper Fine Use spacing
        self.setFixedSize(280, 140)  # Exact size from HTML demos
        self.setContentsMargins(16, 16, 16, 16)
        
        # Main layout
        layout = QVBoxLayout(self)
        layout.setSpacing(8)  # Consistent 8px spacing
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Metric value - LARGE BLUE ACCENT COLOR, CENTERED
        self.value_label = QLabel(f"{self.current_value}%")
        self.value_label.setObjectName("metric-value")
        self.value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.value_label.setStyleSheet("""
            font-family: 'Fira Code', monospace;
            font-size: 36px;
            font-weight: 700;
            margin: 0;
            padding: 0;
        """)
        layout.addWidget(self.value_label)
        
        # Metric label - 12px uppercase, centered
        self.label = QLabel(self.label_text)
        self.label.setObjectName("metric-label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("""
            font-family: 'Fira Code', monospace;
            font-size: 12px;
            font-weight: 700;
            text-transform: uppercase;
            margin: 0;
            padding: 0;
        """)
        layout.addWidget(self.label)
        
        # Progress bar - EXACTLY 16px height
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, self.max_value)
        self.progress_bar.setValue(self.current_value)
        self.progress_bar.setFixedHeight(16)  # EXACT 16px height
        self.progress_bar.setTextVisible(False)  # No text overlay
        
        # Set color based on value
        self._update_progress_color()
        
        layout.addWidget(self.progress_bar)
        
        # Set object name for container styling
        self.setObjectName("fine-use-component")
    
    def _update_progress_color(self):
        """Update progress bar color based on value (like HTML demo)"""
        if self.current_value >= 80:
            self.progress_bar.setObjectName("error")
        elif self.current_value >= 60:
            self.progress_bar.setObjectName("warning") 
        else:
            self.progress_bar.setObjectName("success")
    
    def set_value(self, value: int):
        """Update the metric value"""
        self.current_value = max(0, min(value, self.max_value))
        self.value_label.setText(f"{self.current_value}%")
        self.progress_bar.setValue(self.current_value)
        self._update_progress_color()
    
    def setup_auto_update(self):
        """Setup automatic value updates like HTML demo"""
        self.timer = QTimer()
        self.timer.timeout.connect(self._auto_update)
        self.timer.start(3000)  # Update every 3 seconds
    
    def _auto_update(self):
        """Automatically update values (simulate real-time data)"""
        # Simulate realistic metric changes
        change = random.randint(-10, 10)
        new_value = max(0, min(100, self.current_value + change))
        self.set_value(new_value)


class FineUseStatusIndicator(QWidget):
    """Service status indicator matching HTML demos exactly"""
    
    STATUS_COLORS = {
        "operational": "success",
        "degraded": "warning", 
        "error": "error",
        "maintenance": "info"
    }
    
    def __init__(self, service_name: str, status: str = "operational", uptime: str = "99.9%", parent=None):
        super().__init__(parent)
        self.service_name = service_name.upper()
        self.status = status
        self.uptime = uptime
        
        self.init_ui()
    
    def init_ui(self):
        """Initialize the status indicator with exact Fine Use styling"""
        # Set fixed size for perfect alignment
        self.setFixedSize(200, 100)
        self.setObjectName("status-indicator")
        
        # Main layout
        layout = QVBoxLayout(self)
        layout.setSpacing(8)
        layout.setContentsMargins(16, 16, 16, 16)
        
        # Service name - centered, bold, uppercase
        self.name_label = QLabel(self.service_name)
        self.name_label.setObjectName("service-name")
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.name_label)
        
        # Status badge - colored background with white text
        self.status_label = QLabel(self.status.upper())
        self.status_label.setObjectName(f"status-{self.status}")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setStyleSheet(f"""
            font-family: 'Fira Code', monospace;
            font-size: 12px;
            font-weight: 700;
            text-transform: uppercase;
            padding: 4px 8px;
            border: 1px solid;
            border-radius: 0px;
        """)
        layout.addWidget(self.status_label)
        
        # Uptime percentage
        self.uptime_label = QLabel(self.uptime)
        self.uptime_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.uptime_label.setStyleSheet("""
            font-family: 'Fira Code', monospace;
            font-size: 11px;
            font-weight: 500;
        """)
        layout.addWidget(self.uptime_label)
    
    def update_status(self, status: str, uptime: str = None):
        """Update the service status"""
        self.status = status
        if uptime:
            self.uptime = uptime
            
        self.status_label.setText(status.upper())
        self.status_label.setObjectName(f"status-{status}")
        
        if uptime:
            self.uptime_label.setText(uptime)


class FineUseButtonGrid(QWidget):
    """Perfect button grid system matching HTML demos"""
    
    def __init__(self, rows: int = 2, cols: int = 2, parent=None):
        super().__init__(parent)
        self.rows = rows
        self.cols = cols
        self.buttons = []
        
        self.init_ui()
    
    def init_ui(self):
        """Initialize the button grid with perfect alignment"""
        # Grid layout with exact Fine Use spacing
        self.grid_layout = QGridLayout(self)
        self.grid_layout.setSpacing(12)  # Exact 12px grid gaps
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        
        # Create button placeholders
        for row in range(self.rows):
            button_row = []
            for col in range(self.cols):
                # Create placeholder button
                button = QPushButton("BUTTON")
                button.setObjectName("primary" if (row == 0 and col == 0) else "")
                button.setMinimumHeight(48)  # Exact 48px minimum height
                button.setSizePolicy(button.sizePolicy().Expanding, button.sizePolicy().Fixed)
                
                self.grid_layout.addWidget(button, row, col)
                button_row.append(button)
            
            self.buttons.append(button_row)
    
    def set_button(self, row: int, col: int, text: str, variant: str = "", callback=None):
        """Set button text, variant, and callback"""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            button = self.buttons[row][col]
            button.setText(text.upper())
            button.setObjectName(variant)
            
            if callback:
                button.clicked.connect(callback)
    
    def get_button(self, row: int, col: int) -> QPushButton:
        """Get button at specific position"""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.buttons[row][col]
        return None


class FineUseProgressGroup(QWidget):
    """Group of progress bars matching HTML demos"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.progress_items = []
        self.init_ui()
    
    def init_ui(self):
        """Initialize the progress group"""
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(16)  # Standard Fine Use spacing
        self.layout.setContentsMargins(0, 0, 0, 0)
    
    def add_progress_item(self, label: str, value: int = 0, max_value: int = 100):
        """Add a progress item to the group"""
        item_widget = QWidget()
        item_layout = QVBoxLayout(item_widget)
        item_layout.setSpacing(4)
        item_layout.setContentsMargins(0, 0, 0, 0)
        
        # Progress label
        label_widget = QLabel(label.upper())
        label_widget.setStyleSheet("""
            font-family: 'Fira Code', monospace;
            font-size: 12px;
            font-weight: 700;
            text-transform: uppercase;
        """)
        item_layout.addWidget(label_widget)
        
        # Progress container with bar and value
        progress_container = QWidget()
        progress_layout = QHBoxLayout(progress_container)
        progress_layout.setSpacing(8)
        progress_layout.setContentsMargins(0, 0, 0, 0)
        
        # Progress bar
        progress_bar = QProgressBar()
        progress_bar.setRange(0, max_value)
        progress_bar.setValue(value)
        progress_bar.setFixedHeight(16)  # Exact 16px height
        progress_bar.setTextVisible(False)
        
        # Value label
        value_label = QLabel(f"{value}%")
        value_label.setFixedWidth(40)
        value_label.setStyleSheet("""
            font-family: 'Fira Code', monospace;
            font-size: 12px;
            font-weight: 700;
        """)
        
        progress_layout.addWidget(progress_bar)
        progress_layout.addWidget(value_label)
        
        item_layout.addWidget(progress_container)
        
        self.layout.addWidget(item_widget)
        
        # Store references
        self.progress_items.append({
            'widget': item_widget,
            'progress': progress_bar,
            'value_label': value_label,
            'label': label
        })
        
        # Set initial color
        self._update_progress_color(len(self.progress_items) - 1, value)
    
    def _update_progress_color(self, index: int, value: int):
        """Update progress bar color based on value"""
        if index < len(self.progress_items):
            progress = self.progress_items[index]['progress']
            
            if value >= 80:
                progress.setObjectName("error")
            elif value >= 60:
                progress.setObjectName("warning")
            else:
                progress.setObjectName("success")
    
    def update_progress(self, index: int, value: int):
        """Update a specific progress item"""
        if index < len(self.progress_items):
            item = self.progress_items[index]
            item['progress'].setValue(value)
            item['value_label'].setText(f"{value}%")
            self._update_progress_color(index, value)


class FineUseComponentContainer(QFrame):
    """Container widget that wraps components with Fine Use styling"""
    
    def __init__(self, title: str = "", parent=None):
        super().__init__(parent)
        self.title = title
        self.init_ui()
    
    def init_ui(self):
        """Initialize the container with Fine Use styling"""
        self.setObjectName("fine-use-component")
        self.setContentsMargins(16, 16, 16, 16)
        
        # Main layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setSpacing(16)
        self.main_layout.setContentsMargins(16, 16, 16, 16)
        
        # Add title if provided
        if self.title:
            title_label = QLabel(self.title.upper())
            title_label.setObjectName("h3")
            self.main_layout.addWidget(title_label)
        
        # Content area
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        
        self.main_layout.addWidget(self.content_widget)
    
    def add_widget(self, widget: QWidget):
        """Add a widget to the container"""
        self.content_layout.addWidget(widget)
    
    def set_content_layout(self, layout):
        """Set a custom layout for the content area"""
        # Remove existing layout
        old_layout = self.content_widget.layout()
        if old_layout:
            while old_layout.count():
                child = old_layout.takeAt(0)
                if child.widget():
                    child.widget().setParent(None)
        
        # Set new layout
        self.content_widget.setLayout(layout)
