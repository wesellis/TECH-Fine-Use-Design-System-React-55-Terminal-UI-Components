#!/usr/bin/env python3
"""
Fine Use Design System - PySide6 Demo Application
Complete system demo with pixel-perfect Fine Use implementation
"""

import sys
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                              QHBoxLayout, QGridLayout, QLabel, QComboBox)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont

# Import Fine Use components
from themes import get_theme_qss, get_available_themes
from widgets.metric_widget import (FineUseMetricWidget, FineUseStatusIndicator, 
                                  FineUseComponentContainer, FineUseProgressGroup)
from widgets.fine_use_button import FineUseButtonGrid, FineUseActionButtons
from widgets.log_terminal import FineUseLogTerminalWithControls
from widgets.theme_selector import FineUseThemeSelector

class FineUsePySide6Demo(QMainWindow):
    """Main Fine Use demo application with perfect styling"""
    
    def __init__(self):
        super().__init__()
        self.current_theme = "github-dark"
        self.init_fonts()
        self.init_ui()
        self.apply_theme()
        self.setup_live_updates()
    
    def init_fonts(self):
        """Load Fira Code font for authentic Fine Use typography"""
        # Set default application font to Fira Code
        fira_code_font = QFont("Fira Code", 14, QFont.Weight.Medium)
        fira_code_font.setStyleHint(QFont.StyleHint.Monospace)
        QApplication.instance().setFont(fira_code_font)
    
    def init_ui(self):
        """Initialize the main user interface"""
        self.setWindowTitle("Fine Use Design System - PySide6 Demo")
        self.setMinimumSize(1400, 900)
        
        # Central widget with proper Fine Use margins
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout with exact Fine Use spacing
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(24, 24, 24, 24)  # Exact 24px margins
        main_layout.setSpacing(24)  # Exact 24px spacing
        
        # Theme selector at top
        self.theme_selector = self.create_theme_selector()
        main_layout.addWidget(self.theme_selector)
        
        # Header section
        header = self.create_header()
        main_layout.addWidget(header)
        
        # Main content grid - three equal columns (33% each)
        content_grid = QGridLayout()
        content_grid.setSpacing(24)  # Exact 24px gaps
        content_grid.setColumnStretch(0, 1)  # Equal column weights
        content_grid.setColumnStretch(1, 1)
        content_grid.setColumnStretch(2, 1)
        
        # Left column - Metrics
        metrics_container = self.create_metrics_section()
        content_grid.addWidget(metrics_container, 0, 0)
        
        # Middle column - System Controls  
        controls_container = self.create_controls_section()
        content_grid.addWidget(controls_container, 0, 1)
        
        # Right column - Service Status
        status_container = self.create_status_section()
        content_grid.addWidget(status_container, 0, 2)
        
        main_layout.addLayout(content_grid)
        
        # Bottom section - Log terminals (full width)
        logs_container = self.create_logs_section()
        main_layout.addWidget(logs_container)
    
    def create_theme_selector(self) -> QWidget:
        """Create theme selector with exact Fine Use styling"""
        self.theme_selector_widget = FineUseThemeSelector()
        self.theme_selector_widget.theme_changed.connect(self.on_theme_changed)
        return self.theme_selector_widget
    
    def create_header(self) -> QWidget:
        """Create the main header matching HTML demo"""
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)
        
        # Main title
        title = QLabel("FINE USE DESIGN SYSTEM")
        title.setObjectName("h1")
        layout.addWidget(title)
        
        # Status line
        status_layout = QHBoxLayout()
        status_layout.setSpacing(32)  # Larger spacing for status items
        
        status_items = [
            ("VERSION:", "1.2.0", "text"),
            ("TIME:", "14:23:17", "text"),
            ("STATUS:", "OPERATIONAL", "success"),
            ("DEMO MODE:", "ACTIVE", "info")
        ]
        
        for label_text, value_text, style_class in status_items:
            # Label
            label = QLabel(label_text)
            label.setStyleSheet("color: #7d8590; font-size: 14px; font-weight: 500;")
            status_layout.addWidget(label)
            
            # Value with appropriate styling
            value = QLabel(value_text)
            if style_class == "success":
                value.setStyleSheet("color: #238636; font-size: 14px; font-weight: 700;")
            elif style_class == "info":
                value.setStyleSheet("color: #1f6feb; font-size: 14px; font-weight: 700;")
            else:
                value.setStyleSheet("color: #f0f6fc; font-size: 14px; font-weight: 700;")
            status_layout.addWidget(value)
        
        status_layout.addStretch()
        layout.addLayout(status_layout)
        
        return container
    
    def create_metrics_section(self) -> QWidget:
        """Create metrics section with exact HTML demo widgets"""
        container = FineUseComponentContainer("SYSTEM METRICS")
        
        # Add metric widgets with realistic initial values
        self.cpu_metric = FineUseMetricWidget("CPU USAGE", 67)
        self.memory_metric = FineUseMetricWidget("MEMORY USAGE", 45)
        self.disk_metric = FineUseMetricWidget("DISK I/O", 23)
        
        container.add_widget(self.cpu_metric)
        container.add_widget(self.memory_metric)
        container.add_widget(self.disk_metric)
        
        return container
    
    def create_controls_section(self) -> QWidget:
        """Create system controls section"""
        container = FineUseComponentContainer("SYSTEM CONTROLS")
        
        # Add button grid with exact HTML demo buttons
        self.control_buttons = FineUseButtonGrid(2, 2)
        self.control_buttons.set_button(0, 0, "START SERVICES", "primary")
        self.control_buttons.set_button(0, 1, "STOP ALL PROCESSES", "")
        self.control_buttons.set_button(1, 0, "RESTART LOAD BALANCER", "")
        self.control_buttons.set_button(1, 1, "EMERGENCY SHUTDOWN", "danger")
        
        container.add_widget(self.control_buttons)
        
        return container
    
    def create_status_section(self) -> QWidget:
        """Create service status section"""
        container = FineUseComponentContainer("SERVICE STATUS")
        
        # Add service status indicators
        self.status_indicators = [
            FineUseStatusIndicator("DATABASE", "operational", "99.9%"),
            FineUseStatusIndicator("API GATEWAY", "degraded", "97.2%"),
            FineUseStatusIndicator("CACHE LAYER", "operational", "99.8%")
        ]
        
        for indicator in self.status_indicators:
            container.add_widget(indicator)
        
        return container
    
    def create_logs_section(self) -> QWidget:
        """Create log terminals section"""
        container = QWidget()
        layout = QHBoxLayout(container)
        layout.setSpacing(24)  # Exact spacing
        layout.setContentsMargins(0, 0, 0, 0)
        
        # System log terminal
        self.system_log = FineUseLogTerminalWithControls("SYSTEM EVENT LOG")
        layout.addWidget(self.system_log)
        
        # Operations log terminal
        self.operations_log = FineUseLogTerminalWithControls("OPERATIONS STREAM")
        layout.addWidget(self.operations_log)
        
        return container
    
    def on_theme_changed(self, theme_key: str):
        """Handle theme selection change"""
        self.current_theme = theme_key
        self.apply_theme()
        print(f"Theme changed to: {theme_key}")
    
    def apply_theme(self):
        """Apply the current theme to the entire application"""
        qss = get_theme_qss(self.current_theme)
        self.setStyleSheet(qss)
        
        # Force style refresh
        self.style().unpolish(self)
        self.style().polish(self)
        self.update()
    
    def setup_live_updates(self):
        """Setup live data updates like HTML demo"""
        # Update time every second
        self.time_timer = QTimer()
        self.time_timer.timeout.connect(self.update_time)
        self.time_timer.start(1000)
        
        # Update metrics every 3 seconds
        self.metrics_timer = QTimer()
        self.metrics_timer.timeout.connect(self.update_metrics)
        self.metrics_timer.start(3000)
    
    def update_time(self):
        """Update the time display"""
        # Find and update time label if it exists
        # This would be more robust with proper widget references
        pass
    
    def update_metrics(self):
        """Update metric values"""
        # Metrics widgets handle their own updates
        pass


def main():
    """Main application entry point"""
    # Create Qt application
    app = QApplication(sys.argv)
    
    # Set application properties
    app.setApplicationName("Fine Use Design System")
    app.setApplicationVersion("1.2.0")
    app.setOrganizationName("Fine Use")
    
    # Set monospace font as fallback
    font = QFont("Fira Code", 14)
    font.setStyleHint(QFont.StyleHint.Monospace)
    app.setFont(font)
    
    # Create and show main window
    window = FineUsePySide6Demo()
    window.show()
    
    print("Fine Use PySide6 Demo Started")
    print("Available themes:", list(get_available_themes().keys()))
    
    # Start event loop
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
