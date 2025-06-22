#!/usr/bin/env python3
"""
Fine Use Design System - FIXED PySide6 Demo
Focusing on getting the visual styling exactly right
"""

import sys
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                              QHBoxLayout, QGridLayout, QLabel, QComboBox, QPushButton, 
                              QProgressBar, QTextEdit, QFrame)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont

# Import theme system
from themes import get_theme_qss

class FixedFineUseDemo(QMainWindow):
    """Simplified Fine Use demo focusing on perfect visual styling"""
    
    def __init__(self):
        super().__init__()
        self.current_theme = "github-dark"
        self.init_ui()
        self.apply_theme()
    
    def init_ui(self):
        """Initialize UI with proper spacing and styling"""
        self.setWindowTitle("Fine Use Design System - PySide6 FIXED")
        self.setMinimumSize(1200, 800)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout with EXACT spacing
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(24, 24, 24, 24)  # Exact 24px margins
        main_layout.setSpacing(24)  # Exact 24px spacing
        
        # Theme selector
        theme_container = self.create_theme_selector()
        main_layout.addWidget(theme_container)
        
        # Header
        header = self.create_header()
        main_layout.addWidget(header)
        
        # Content grid - EXACT 3 columns
        content_grid = QGridLayout()
        content_grid.setSpacing(24)  # EXACT 24px gaps
        content_grid.setColumnStretch(0, 1)
        content_grid.setColumnStretch(1, 1) 
        content_grid.setColumnStretch(2, 1)
        
        # Left: Metrics
        metrics = self.create_metrics()
        content_grid.addWidget(metrics, 0, 0)
        
        # Middle: Buttons
        buttons = self.create_buttons()
        content_grid.addWidget(buttons, 0, 1)
        
        # Right: Status
        status = self.create_status()
        content_grid.addWidget(status, 0, 2)
        
        main_layout.addLayout(content_grid)
        
        # Bottom: Log
        log = self.create_log()
        main_layout.addWidget(log)
    
    def create_theme_selector(self):
        """Create simple theme selector"""
        container = QWidget()
        layout = QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)
        
        # Label
        label = QLabel("THEME:")
        label.setStyleSheet("""
            font-family: 'Fira Code', monospace;
            font-size: 14px;
            font-weight: 700;
            color: #f0f6fc;
        """)
        layout.addWidget(label)
        
        # Dropdown
        self.theme_combo = QComboBox()
        self.theme_combo.addItem("Dark Mode", "github-dark")
        self.theme_combo.currentIndexChanged.connect(self.on_theme_changed)
        layout.addWidget(self.theme_combo)
        
        layout.addStretch()
        return container
    
    def create_header(self):
        """Create main header"""
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)
        
        # Title
        title = QLabel("FINE USE DESIGN SYSTEM")
        title.setObjectName("h1")
        layout.addWidget(title)
        
        # Status info
        status_layout = QHBoxLayout()
        status_layout.setSpacing(32)
        
        # Version
        version_label = QLabel("VERSION:")
        version_label.setStyleSheet("color: #7d8590; font-size: 14px;")
        status_layout.addWidget(version_label)
        
        version_value = QLabel("1.2.0")
        version_value.setStyleSheet("color: #f0f6fc; font-size: 14px; font-weight: 700;")
        status_layout.addWidget(version_value)
        
        # Status
        status_label = QLabel("STATUS:")
        status_label.setStyleSheet("color: #7d8590; font-size: 14px;")
        status_layout.addWidget(status_label)
        
        status_value = QLabel("OPERATIONAL")
        status_value.setStyleSheet("color: #238636; font-size: 14px; font-weight: 700;")
        status_layout.addWidget(status_value)
        
        status_layout.addStretch()
        layout.addLayout(status_layout)
        
        return container
    
    def create_metrics(self):
        """Create metrics section"""
        container = QFrame()
        container.setObjectName("fine-use-component")
        
        layout = QVBoxLayout(container)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(16)
        
        # Title
        title = QLabel("SYSTEM METRICS")
        title.setObjectName("h3")
        layout.addWidget(title)
        
        # CPU Metric
        cpu_widget = self.create_metric("CPU USAGE", 77, "warning")
        layout.addWidget(cpu_widget)
        
        # Memory Metric
        memory_widget = self.create_metric("MEMORY USAGE", 43, "success")
        layout.addWidget(memory_widget)
        
        # Disk Metric
        disk_widget = self.create_metric("DISK I/O", 14, "success")
        layout.addWidget(disk_widget)
        
        return container
    
    def create_metric(self, label_text, value, status):
        """Create individual metric widget"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)
        
        # Large value - EXACTLY like HTML
        value_label = QLabel(f"{value}%")
        value_label.setObjectName("metric-value")
        layout.addWidget(value_label)
        
        # Label
        label = QLabel(label_text)
        label.setObjectName("metric-label")
        layout.addWidget(label)
        
        # Progress bar - EXACTLY 16px height
        progress = QProgressBar()
        progress.setRange(0, 100)
        progress.setValue(value)
        progress.setObjectName(status)
        progress.setFixedHeight(16)
        progress.setTextVisible(False)
        layout.addWidget(progress)
        
        return widget
    
    def create_buttons(self):
        """Create button section"""
        container = QFrame()
        container.setObjectName("fine-use-component")
        
        layout = QVBoxLayout(container)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(16)
        
        # Title
        title = QLabel("SYSTEM CONTROLS")
        title.setObjectName("h3")
        layout.addWidget(title)
        
        # Button grid - EXACTLY 2x2
        button_grid = QGridLayout()
        button_grid.setSpacing(12)  # EXACT 12px spacing
        
        # Create buttons with EXACT styling
        btn1 = QPushButton("START SERVICES")
        btn1.setObjectName("primary")
        btn1.setMinimumHeight(48)
        button_grid.addWidget(btn1, 0, 0)
        
        btn2 = QPushButton("STOP ALL PROCESSES")
        btn2.setMinimumHeight(48)
        button_grid.addWidget(btn2, 0, 1)
        
        btn3 = QPushButton("RESTART LOAD BALANCER")
        btn3.setMinimumHeight(48)
        button_grid.addWidget(btn3, 1, 0)
        
        btn4 = QPushButton("EMERGENCY SHUTDOWN")
        btn4.setObjectName("danger")
        btn4.setMinimumHeight(48)
        button_grid.addWidget(btn4, 1, 1)
        
        layout.addLayout(button_grid)
        
        return container
    
    def create_status(self):
        """Create status section"""
        container = QFrame()
        container.setObjectName("fine-use-component")
        
        layout = QVBoxLayout(container)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(16)
        
        # Title
        title = QLabel("SERVICE STATUS")
        title.setObjectName("h3")
        layout.addWidget(title)
        
        # Status indicators
        status1 = self.create_status_indicator("DATABASE", "operational", "99.9%")
        layout.addWidget(status1)
        
        status2 = self.create_status_indicator("API GATEWAY", "degraded", "97.2%")
        layout.addWidget(status2)
        
        status3 = self.create_status_indicator("CACHE LAYER", "operational", "99.8%")
        layout.addWidget(status3)
        
        return container
    
    def create_status_indicator(self, name, status, uptime):
        """Create status indicator"""
        widget = QFrame()
        widget.setObjectName("status-indicator")
        
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(8)
        
        # Service name
        name_label = QLabel(name)
        name_label.setObjectName("service-name")
        layout.addWidget(name_label)
        
        # Status badge
        status_label = QLabel(status.upper())
        status_label.setObjectName(f"status-{status}")
        layout.addWidget(status_label)
        
        # Uptime
        uptime_label = QLabel(uptime)
        uptime_label.setStyleSheet("color: #7d8590; font-size: 11px; text-align: center;")
        layout.addWidget(uptime_label)
        
        return widget
    
    def create_log(self):
        """Create log section"""
        container = QWidget()
        layout = QHBoxLayout(container)
        layout.setSpacing(24)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Left log
        log1 = self.create_log_terminal("SYSTEM EVENT LOG")
        layout.addWidget(log1)
        
        # Right log
        log2 = self.create_log_terminal("OPERATIONS STREAM")
        layout.addWidget(log2)
        
        return container
    
    def create_log_terminal(self, title):
        """Create log terminal"""
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Header
        header = QWidget()
        header.setStyleSheet("""
            QWidget {
                background-color: #30363d;
                border: 2px solid #30363d;
                padding: 8px 16px;
            }
        """)
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(8, 8, 8, 8)
        
        title_label = QLabel(title)
        title_label.setStyleSheet("""
            color: #f0f6fc;
            font-family: 'Fira Code', monospace;
            font-size: 14px;
            font-weight: 700;
            background: none;
            border: none;
        """)
        header_layout.addWidget(title_label)
        
        header_layout.addStretch()
        
        # Control buttons
        pause_btn = QPushButton("PAUSE")
        pause_btn.setStyleSheet("""
            QPushButton {
                background-color: #161b22;
                border: 1px solid #30363d;
                color: #f0f6fc;
                font-family: 'Fira Code', monospace;
                font-size: 11px;
                font-weight: 700;
                padding: 4px 8px;
                border-radius: 0px;
            }
        """)
        header_layout.addWidget(pause_btn)
        
        clear_btn = QPushButton("CLEAR")
        clear_btn.setStyleSheet("""
            QPushButton {
                background-color: #161b22;
                border: 1px solid #30363d;
                color: #f0f6fc;
                font-family: 'Fira Code', monospace;
                font-size: 11px;
                font-weight: 700;
                padding: 4px 8px;
                border-radius: 0px;
            }
        """)
        header_layout.addWidget(clear_btn)
        
        layout.addWidget(header)
        
        # Terminal content
        terminal = QTextEdit()
        terminal.setMinimumHeight(150)
        terminal.setReadOnly(True)
        
        # Add sample log entries
        log_entries = [
            "[13:29:01] <span style='color: #d29922; font-weight: 700;'>WARN</span> High CPU usage detected",
            "[13:29:03] <span style='color: #238636; font-weight: 700;'>SUCCESS</span> Database backup completed", 
            "[13:29:05] <span style='color: #da3633; font-weight: 700;'>ERROR</span> Disk space critical",
            "[13:29:07] <span style='color: #d29922; font-weight: 700;'>WARN</span> High CPU usage detected"
        ]
        
        terminal.setHtml("<br>".join(log_entries))
        layout.addWidget(terminal)
        
        return container
    
    def on_theme_changed(self, index):
        """Handle theme change"""
        theme_key = self.theme_combo.itemData(index)
        if theme_key:
            self.current_theme = theme_key
            self.apply_theme()
    
    def apply_theme(self):
        """Apply theme styling"""
        qss = get_theme_qss(self.current_theme)
        self.setStyleSheet(qss)
        
        # Force refresh
        self.style().unpolish(self)
        self.style().polish(self)
        self.update()

def main():
    """Main entry point"""
    app = QApplication(sys.argv)
    
    # Set monospace font
    font = QFont("Fira Code", 14)
    font.setStyleHint(QFont.StyleHint.Monospace)
    app.setFont(font)
    
    # Create window
    window = FixedFineUseDemo()
    window.show()
    
    print("🚀 Fine Use FIXED Demo launched")
    
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
