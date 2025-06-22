#!/usr/bin/env python3
"""
Fine Use Design System - Quick Test Script
Test the core components after fixes
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

# Import fixed components
from themes import get_theme_qss, get_available_themes
from widgets.metric_widget import FineUseMetricWidget, FineUseStatusIndicator, FineUseComponentContainer
from widgets.fine_use_button import FineUseButtonGrid
from widgets.log_terminal import FineUseLogTerminalWithControls
from widgets.theme_selector import FineUseThemeSelector

class QuickTest(QMainWindow):
    """Quick test of fixed Fine Use components"""
    
    def __init__(self):
        super().__init__()
        self.current_theme = "github-dark"
        self.init_ui()
        self.apply_theme()
    
    def init_ui(self):
        """Initialize test UI"""
        self.setWindowTitle("Fine Use - Quick Component Test")
        self.setMinimumSize(800, 600)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(24)
        
        # Theme selector
        self.theme_selector = FineUseThemeSelector()
        self.theme_selector.theme_changed.connect(self.on_theme_changed)
        layout.addWidget(self.theme_selector)
        
        # Test components in a row
        test_row = QHBoxLayout()
        test_row.setSpacing(24)
        
        # Metric widget test
        metric_container = FineUseComponentContainer("TEST METRIC")
        self.test_metric = FineUseMetricWidget("CPU USAGE", 67)
        metric_container.add_widget(self.test_metric)
        test_row.addWidget(metric_container)
        
        # Button grid test
        button_container = FineUseComponentContainer("TEST BUTTONS")
        self.test_buttons = FineUseButtonGrid(2, 2)
        self.test_buttons.set_button(0, 0, "PRIMARY", "primary")
        self.test_buttons.set_button(0, 1, "SECONDARY", "")
        self.test_buttons.set_button(1, 0, "INFO", "info")
        self.test_buttons.set_button(1, 1, "DANGER", "danger")
        button_container.add_widget(self.test_buttons)
        test_row.addWidget(button_container)
        
        # Status indicator test
        status_container = FineUseComponentContainer("TEST STATUS")
        self.test_status = FineUseStatusIndicator("TEST SERVICE", "operational", "99.9%")
        status_container.add_widget(self.test_status)
        test_row.addWidget(status_container)
        
        layout.addLayout(test_row)
        
        # Log terminal test
        self.test_log = FineUseLogTerminalWithControls("TEST LOG TERMINAL")
        layout.addWidget(self.test_log)
    
    def on_theme_changed(self, theme_key: str):
        """Handle theme change"""
        self.current_theme = theme_key
        self.apply_theme()
        print(f"Theme changed to: {theme_key}")
    
    def apply_theme(self):
        """Apply the current theme"""
        qss = get_theme_qss(self.current_theme)
        self.setStyleSheet(qss)
        
        # Force style refresh
        self.style().unpolish(self)
        self.style().polish(self)
        self.update()

def main():
    """Run the quick test"""
    app = QApplication(sys.argv)
    
    # Set monospace font
    font = QFont("Fira Code", 14)
    font.setStyleHint(QFont.StyleHint.Monospace)
    app.setFont(font)
    
    # Create test window
    window = QuickTest()
    window.show()
    
    print("Fine Use Quick Test Started")
    print("Available themes:", list(get_available_themes().keys()))
    
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
