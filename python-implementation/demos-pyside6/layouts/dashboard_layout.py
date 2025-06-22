"""Dashboard Layout - Main Fine Use dashboard with perfect proportional layout"""

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, 
    QSplitter, QLabel, QFrame
)
from PySide6.QtCore import Qt, QSize
from datetime import datetime

# Import Fine Use widgets
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from widgets import FineUseButton, MetricWidget, LogTerminal, ThemeSelector

class DashboardLayout(QMainWindow):
    """Main Fine Use dashboard with perfect proportional layout"""
    
    def __init__(self):
        super().__init__()
        self.setup_main_layout()
    
    def setup_main_layout(self):
        """Create the main dashboard layout structure"""
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main vertical layout with PERFECT spacing
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(16)
        
        # Header section (fixed height)
        header_widget = self.create_header_section()
        main_layout.addWidget(header_widget)
        
        # Metrics section (fixed height)  
        metrics_widget = self.create_metrics_section()
        main_layout.addWidget(metrics_widget)
        
        # Control panels section (expanding) - THE CRITICAL SECTION
        controls_widget = self.create_controls_section()
        main_layout.addWidget(controls_widget, stretch=1)  # Takes remaining space
        
        # Log terminal section (fixed height)
        terminal_widget = self.create_terminal_section() 
        main_layout.addWidget(terminal_widget)
        
        # Status bar (fixed height)
        status_widget = self.create_status_section()
        main_layout.addWidget(status_widget)
    
    def create_header_section(self) -> QWidget:
        """Create the header section with title and theme selector"""
        
        header_container = QWidget()
        header_layout = QHBoxLayout(header_container)
        header_layout.setContentsMargins(0, 0, 0, 0)
        
        # Title section
        title_widget = QWidget()
        title_layout = QVBoxLayout(title_widget)
        title_layout.setContentsMargins(0, 0, 0, 0)
        
        # Main title
        title = QLabel("FINE USE SYSTEM MONITOR")
        title.setObjectName("FineUseHeader")
        title.setProperty("class", "FineUseHeader")
        
        # Subtitle with current time
        subtitle = QLabel("PYSIDE6 IMPLEMENTATION • REAL-TIME DATA")
        subtitle.setObjectName("FineUseLabel")
        subtitle.setProperty("class", "FineUseLabel")
        
        title_layout.addWidget(title)
        title_layout.addWidget(subtitle)
        
        # Theme selector
        self.theme_selector = ThemeSelector()
        
        # Add to header layout
        header_layout.addWidget(title_widget)
        header_layout.addStretch()
        header_layout.addWidget(self.theme_selector)
        
        # Set fixed height for header
        header_container.setFixedHeight(80)
        
        return header_container
    
    def create_metrics_section(self) -> QWidget:
        """Create the metrics section with three equal-width metrics"""
        
        metrics_container = QWidget()
        metrics_layout = QHBoxLayout(metrics_container)
        metrics_layout.setContentsMargins(0, 0, 0, 0)
        metrics_layout.setSpacing(16)
        
        # Create three metrics with PERFECT equal widths
        self.cpu_metric = MetricWidget("CPU USAGE", "%", 45)
        self.memory_metric = MetricWidget("MEMORY", "%", 67)
        self.disk_metric = MetricWidget("DISK I/O", "%", 23)
        
        # Add to layout with equal stretch factors (GUARANTEED equal widths)
        metrics_layout.addWidget(self.cpu_metric, stretch=1)
        metrics_layout.addWidget(self.memory_metric, stretch=1)
        metrics_layout.addWidget(self.disk_metric, stretch=1)
        
        # Set fixed height for metrics section
        metrics_container.setFixedHeight(160)
        
        return metrics_container
    
    def create_controls_section(self) -> QWidget:
        """Create the three-panel control section with PERFECT equal widths"""
        
        # Use QSplitter for MATHEMATICAL precision in width distribution
        splitter = QSplitter(Qt.Horizontal)
        splitter.setChildrenCollapsible(False)  # Prevent panels from collapsing
        
        # System Controls Panel (33.33%)
        system_panel = self.create_system_controls_panel()
        splitter.addWidget(system_panel)
        
        # Service Controls Panel (33.33%) - THE SOLUTION TO THE PROBLEM
        service_panel = self.create_service_controls_panel()
        splitter.addWidget(service_panel)
        
        # Maintenance Panel (33.33%)
        maintenance_panel = self.create_maintenance_panel()
        splitter.addWidget(maintenance_panel)
        
        # MATHEMATICAL PERFECTION: Force exactly equal sizes
        splitter.setSizes([100, 100, 100])  # Equal proportions
        splitter.setStretchFactor(0, 1)    # Each panel gets equal stretch
        splitter.setStretchFactor(1, 1)
        splitter.setStretchFactor(2, 1)
        
        return splitter
    
    def create_system_controls_panel(self) -> QWidget:
        """Create the system controls panel"""
        
        panel = QWidget()
        panel.setObjectName("FineUsePanel")
        panel.setProperty("class", "FineUsePanel")
        
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)
        
        # Panel title
        title = QLabel("SYSTEM CONTROLS")
        title.setObjectName("FineUsePanelHeader")
        title.setProperty("class", "FineUsePanelHeader")
        layout.addWidget(title)
        
        # Button grid (2x2) using QVBoxLayout for PERFECT button heights
        buttons_layout = QVBoxLayout()
        buttons_layout.setSpacing(8)
        
        # Create buttons
        start_btn = FineUseButton("START SERVICES", "primary")
        stop_btn = FineUseButton("STOP PROCESSES", "default")
        restart_btn = FineUseButton("RESTART SYSTEM", "warning")
        shutdown_btn = FineUseButton("EMERGENCY SHUTDOWN", "error")
        
        # Add buttons - QVBoxLayout AUTOMATICALLY makes them equal height
        buttons_layout.addWidget(start_btn)
        buttons_layout.addWidget(stop_btn)
        buttons_layout.addWidget(restart_btn)
        buttons_layout.addWidget(shutdown_btn)
        
        layout.addLayout(buttons_layout, stretch=1)  # Buttons take all space
        
        return panel
    
    def create_service_controls_panel(self) -> QWidget:
        """Create the service controls panel - THE PERFECT SOLUTION"""
        
        panel = QWidget()
        panel.setObjectName("FineUsePanel")
        panel.setProperty("class", "FineUsePanel")
        
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)
        
        # Panel title
        title = QLabel("SERVICE CONTROLS")
        title.setObjectName("FineUsePanelHeader")
        title.setProperty("class", "FineUsePanelHeader")
        layout.addWidget(title)
        
        # PERFECT button layout using QVBoxLayout
        # This GUARANTEES mathematically equal button heights
        buttons_layout = QVBoxLayout()
        buttons_layout.setSpacing(8)
        
        # Create 4 buttons
        self.database_btn = FineUseButton("DATABASE SERVER", "info")
        self.webserver_btn = FineUseButton("WEB SERVER", "default") 
        self.cache_btn = FineUseButton("CACHE LAYER", "success")
        self.monitoring_btn = FineUseButton("MONITORING", "default")
        
        # Add buttons to layout - AUTOMATICALLY EQUAL HEIGHTS
        # QVBoxLayout distributes space mathematically perfectly
        buttons_layout.addWidget(self.database_btn)    # 25% of available space
        buttons_layout.addWidget(self.webserver_btn)   # 25% of available space
        buttons_layout.addWidget(self.cache_btn)       # 25% of available space  
        buttons_layout.addWidget(self.monitoring_btn)  # 25% of available space
        
        layout.addLayout(buttons_layout, stretch=1)  # Buttons take all remaining space
        
        return panel
    
    def create_maintenance_panel(self) -> QWidget:
        """Create the maintenance panel"""
        
        panel = QWidget()
        panel.setObjectName("FineUsePanel")
        panel.setProperty("class", "FineUsePanel")
        
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)
        
        # Panel title
        title = QLabel("MAINTENANCE")
        title.setObjectName("FineUsePanelHeader")
        title.setProperty("class", "FineUsePanelHeader")
        layout.addWidget(title)
        
        # Maintenance buttons
        buttons_layout = QVBoxLayout()
        buttons_layout.setSpacing(8)
        
        backup_btn = FineUseButton("BACKUP SYSTEM", "info")
        update_btn = FineUseButton("SYSTEM UPDATE", "warning")
        diagnostics_btn = FineUseButton("RUN DIAGNOSTICS", "default")
        cleanup_btn = FineUseButton("CLEANUP LOGS", "default")
        
        buttons_layout.addWidget(backup_btn)
        buttons_layout.addWidget(update_btn)
        buttons_layout.addWidget(diagnostics_btn)
        buttons_layout.addWidget(cleanup_btn)
        
        layout.addLayout(buttons_layout, stretch=1)
        
        return panel
    
    def create_terminal_section(self) -> QWidget:
        """Create the log terminal section"""
        
        terminal_container = QWidget()
        terminal_layout = QHBoxLayout(terminal_container)
        terminal_layout.setContentsMargins(0, 0, 0, 0)
        terminal_layout.setSpacing(16)
        
        # Create two terminals side by side
        self.system_log = LogTerminal("SYSTEM EVENT LOG")
        self.operations_log = LogTerminal("OPERATIONS LOG")
        
        # Add with equal widths
        terminal_layout.addWidget(self.system_log, stretch=1)
        terminal_layout.addWidget(self.operations_log, stretch=1)
        
        # Set fixed height for terminal section
        terminal_container.setFixedHeight(200)
        
        return terminal_container
    
    def create_status_section(self) -> QWidget:
        """Create the status bar section"""
        
        status_container = QWidget()
        status_layout = QHBoxLayout(status_container)
        status_layout.setContentsMargins(8, 8, 8, 8)
        
        # Status information
        self.status_label = QLabel("STATUS: OPERATIONAL • UPTIME: 24D 7H 32M • ERRORS: 0")
        self.status_label.setObjectName("FineUseLabel")
        self.status_label.setProperty("class", "FineUseLabel")
        
        # Time display
        self.time_label = QLabel(datetime.now().strftime("%H:%M:%S"))
        self.time_label.setObjectName("FineUseValue")
        self.time_label.setProperty("class", "FineUseValue")
        
        status_layout.addWidget(self.status_label)
        status_layout.addStretch()
        status_layout.addWidget(self.time_label)
        
        # Set fixed height for status bar
        status_container.setFixedHeight(32)
        
        return status_container
    
    def get_theme_selector(self) -> ThemeSelector:
        """Get the theme selector widget for connecting signals"""
        return self.theme_selector
    
    def get_metrics(self) -> tuple:
        """Get metric widgets for updating values"""
        return (self.cpu_metric, self.memory_metric, self.disk_metric)
    
    def get_terminals(self) -> tuple:
        """Get terminal widgets for adding log entries"""
        return (self.system_log, self.operations_log)
    
    def update_time_display(self):
        """Update the time display"""
        self.time_label.setText(datetime.now().strftime("%H:%M:%S"))
