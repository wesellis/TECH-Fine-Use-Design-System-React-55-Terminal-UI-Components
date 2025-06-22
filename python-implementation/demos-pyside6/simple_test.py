#!/usr/bin/env python3
"""
Fine Use Design System - Simple Test Script
Minimal test to verify PySide6 installation and basic functionality
"""

import sys
import os

try:
    from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
    from PySide6.QtCore import Qt
    from PySide6.QtGui import QFont
    print("✅ PySide6 imported successfully")
except ImportError as e:
    print(f"❌ PySide6 import failed: {e}")
    print("Install with: pip install PySide6")
    sys.exit(1)

class SimpleTest(QMainWindow):
    """Simple test window to verify Fine Use basics"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.apply_basic_style()
    
    def init_ui(self):
        """Initialize simple UI"""
        self.setWindowTitle("Fine Use - Simple Test")
        self.setMinimumSize(600, 400)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)
        
        # Title
        title = QLabel("FINE USE PYSIDE6 TEST")
        title.setStyleSheet("""
            QLabel {
                font-family: 'Fira Code', monospace;
                font-size: 24px;
                font-weight: 700;
                color: #f0f6fc;
                text-transform: uppercase;
                text-align: center;
            }
        """)
        layout.addWidget(title)
        
        # Status
        status = QLabel("✅ PySide6 is working correctly!")
        status.setStyleSheet("""
            QLabel {
                font-family: 'Fira Code', monospace;
                font-size: 16px;
                color: #238636;
                text-align: center;
            }
        """)
        layout.addWidget(status)
        
        # Test button
        test_button = QPushButton("TEST BUTTON")
        test_button.setStyleSheet("""
            QPushButton {
                background-color: #161b22;
                border: 2px solid #30363d;
                color: #f0f6fc;
                font-family: 'Fira Code', monospace;
                font-size: 14px;
                font-weight: 700;
                text-transform: uppercase;
                padding: 12px 24px;
                min-height: 48px;
                border-radius: 0px;
            }
            QPushButton:hover {
                border-color: #58a6ff;
                background-color: #30363d;
            }
            QPushButton:pressed {
                background-color: #58a6ff;
                color: #0d1117;
            }
        """)
        test_button.clicked.connect(self.on_button_click)
        layout.addWidget(test_button)
        
        # Instructions
        instructions = QLabel("If you can see this window with proper styling, PySide6 is ready for Fine Use!")
        instructions.setStyleSheet("""
            QLabel {
                font-family: 'Fira Code', monospace;
                font-size: 12px;
                color: #7d8590;
                text-align: center;
            }
        """)
        layout.addWidget(instructions)
    
    def apply_basic_style(self):
        """Apply basic Fine Use styling"""
        self.setStyleSheet("""
            QMainWindow {
                background-color: #0d1117;
                color: #f0f6fc;
            }
        """)
    
    def on_button_click(self):
        """Handle button click"""
        print("✅ Button clicked - Fine Use PySide6 is working!")

def main():
    """Run the simple test"""
    app = QApplication(sys.argv)
    
    # Set monospace font
    font = QFont("Fira Code", 14)
    font.setStyleHint(QFont.StyleHint.Monospace)
    app.setFont(font)
    
    print("🚀 Starting Fine Use Simple Test...")
    
    # Create test window
    window = SimpleTest()
    window.show()
    
    print("✅ Fine Use Simple Test window opened")
    print("Close the window to exit")
    
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
