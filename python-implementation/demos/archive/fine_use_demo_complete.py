"""
Fine Use Design System - Complete Python Demo
============================================

This demo shows a complete system monitoring application
built with Fine Use design principles in Python.

Demonstrates:
- Real-time data updates
- Button grid systems
- Typography hierarchy  
- Component styling
- Theme system
- Terminal aesthetics

Run with: python fine_use_demo_complete.py
"""

import tkinter as tk
from tkinter import ttk
import threading
import time
import random
from datetime import datetime
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fine_use_core import fine_use, FineUseTheme, get_spacing, get_font
from fine_use_tkinter import (
    FineUseApp, FineUseButton, FineUseLabel, 
    FineUseFrame, FineUseEntry, FineUseButtonGrid
)


class SystemMonitorApp:
    """
    Complete system monitoring application demonstrating
    Fine Use design system implementation in Python
    """
    
    def __init__(self):
        # Create Fine Use application
        self.app = FineUseApp(
            title="Fine Use System Monitor - Python Demo",
            theme="github-dark",
            width=1400,
            height=900
        )
        
        # Application state
        self.is_running = False
        self.update_thread = None
        self.metrics = {
            'cpu': 0,
            'memory': 0,
            'disk': 0,
            'network': 0
        }
        self.log_entries = []
        
        # Build interface
        self.build_interface()
        
        # Start real-time updates
        self.start_monitoring()
    
    def build_interface(self):
        """Build the complete Fine Use interface"""
        
        # === HEADER SECTION ===
        self.build_header()
        
        # === METRICS SECTION ===
        self.build_metrics_section()
        
        # === CONTROL PANELS ===
        self.build_control_panels()
        
        # === LOG TERMINAL ===
        self.build_log_terminal()
        
        # === THEME CONTROLS ===
        self.build_theme_controls()
    
    def build_header(self):
        """Build application header with Fine Use typography"""
        header_frame = FineUseFrame(self.app.main_frame, padding="xl")
        header_frame.pack(fill='x', pady=get_spacing('lg'))
        
        # Main title
        title = FineUseLabel(
            header_frame,
            "FINE USE SYSTEM MONITOR",
            level="h1"
        )
        title.pack()
        
        # Status line
        status_frame = tk.Frame(header_frame, bg=fine_use.colors['surface'])
        status_frame.pack(pady=get_spacing('md'))
        
        # Status indicators
        self.create_status_indicator(status_frame, "VERSION:", "1.2.0", "text")
        self.create_status_indicator(status_frame, "TIME:", "00:00:00", "comment", "time_label")
        self.create_status_indicator(status_frame, "STATUS:", "OPERATIONAL", "success")
        self.create_status_indicator(status_frame, "MODE:", "PYTHON DEMO", "info")
    
    def create_status_indicator(self, parent, label, value, color, tag=None):
        """Create a status indicator with Fine Use styling"""
        container = tk.Frame(parent, bg=fine_use.colors['surface'])
        container.pack(side='left', padx=get_spacing('lg'))
        
        label_widget = FineUseLabel(container, label, level="body", color="comment")
        label_widget.pack(side='left')
        
        value_widget = FineUseLabel(container, value, level="body", color=color)
        value_widget.pack(side='left', padx=(get_spacing('sm'), 0))
        
        if tag:
            setattr(self, tag, value_widget)
    
    def build_metrics_section(self):
        """Build real-time metrics display"""
        metrics_frame = FineUseFrame(self.app.main_frame, padding="xl")
        metrics_frame.pack(fill='x', pady=get_spacing('lg'))
        
        section_title = FineUseLabel(metrics_frame, "REAL-TIME SYSTEM METRICS", level="h2")
        section_title.pack(pady=get_spacing('md'))
        
        # Metrics grid
        grid_frame = tk.Frame(metrics_frame, bg=fine_use.colors['surface'])
        grid_frame.pack(fill='x', pady=get_spacing('lg'))
        
        # Configure grid
        for i in range(4):
            grid_frame.grid_columnconfigure(i, weight=1)
        
        # Create metric displays
        self.metric_displays = {}
        metrics = [
            ('CPU', 'cpu', 'success'),
            ('MEMORY', 'memory', 'warning'),
            ('DISK', 'disk', 'error'),
            ('NETWORK', 'network', 'info')
        ]
        
        for i, (name, key, color) in enumerate(metrics):
            metric_frame = self.create_metric_display(grid_frame, name, color)
            metric_frame.grid(row=0, column=i, padx=get_spacing('md'), sticky='nsew')
            self.metric_displays[key] = metric_frame
    
    def create_metric_display(self, parent, name, color):
        """Create a single metric display widget"""
        container = FineUseFrame(parent, padding="lg")
        
        # Metric name
        name_label = FineUseLabel(container, name, level="body", color="comment")
        name_label.pack()
        
        # Metric value (large)
        value_label = FineUseLabel(container, "0%", level="h1", color=color)
        value_label.pack(pady=get_spacing('sm'))
        
        # Progress bar (simplified with label)
        progress_frame = tk.Frame(container, bg=fine_use.colors['border'], height=8)
        progress_frame.pack(fill='x', pady=get_spacing('sm'))
        
        progress_bar = tk.Frame(progress_frame, bg=fine_use.colors[color], height=8)
        progress_bar.place(relwidth=0, relheight=1)
        
        # Store references
        container.value_label = value_label
        container.progress_bar = progress_bar
        container.color = color
        
        return container
    
    def build_control_panels(self):
        """Build control panel with button grids"""
        controls_frame = FineUseFrame(self.app.main_frame, padding="xl")
        controls_frame.pack(fill='x', pady=get_spacing('lg'))
        
        section_title = FineUseLabel(controls_frame, "SYSTEM CONTROL PANELS", level="h2")
        section_title.pack(pady=get_spacing('md'))
        
        # Create three control sections
        panels_frame = tk.Frame(controls_frame, bg=fine_use.colors['surface'])
        panels_frame.pack(fill='x', pady=get_spacing('lg'))
        
        for i in range(3):
            panels_frame.grid_columnconfigure(i, weight=1)
        
        # System Controls
        self.build_system_controls(panels_frame, 0)
        
        # Service Controls  
        self.build_service_controls(panels_frame, 1)
        
        # Maintenance Controls
        self.build_maintenance_controls(panels_frame, 2)
    
    def build_system_controls(self, parent, column):
        """Build system control buttons"""
        control_frame = FineUseFrame(parent, padding="lg")
        control_frame.grid(row=0, column=column, padx=get_spacing('md'), sticky='nsew')
        
        title = FineUseLabel(control_frame, "SYSTEM CONTROLS", level="h3")
        title.pack(pady=get_spacing('md'))
        
        # Button grid
        button_grid = FineUseButtonGrid(control_frame, layout="2x2")
        button_grid.add_button("START SERVICES", command=self.start_services, variant="primary")
        button_grid.add_button("STOP PROCESSES", command=self.stop_processes)
        button_grid.add_button("RESTART SYSTEM", command=self.restart_system, variant="warning")
        button_grid.add_button("EMERGENCY STOP", command=self.emergency_stop, variant="error")
    
    def build_service_controls(self, parent, column):
        """Build service control buttons"""
        control_frame = FineUseFrame(parent, padding="lg")
        control_frame.grid(row=0, column=column, padx=get_spacing('md'), sticky='nsew')
        
        title = FineUseLabel(control_frame, "SERVICE CONTROLS", level="h3")
        title.pack(pady=get_spacing('md'))
        
        # Button grid
        button_grid = FineUseButtonGrid(control_frame, layout="1x4")
        button_grid.add_button("DATABASE", command=lambda: self.service_action("DATABASE"), variant="info")
        button_grid.add_button("WEB SERVER", command=lambda: self.service_action("WEB SERVER"))
        button_grid.add_button("CACHE", command=lambda: self.service_action("CACHE"), variant="success")
        button_grid.add_button("MONITORING", command=lambda: self.service_action("MONITORING"))
    
    def build_maintenance_controls(self, parent, column):
        """Build maintenance control buttons"""
        control_frame = FineUseFrame(parent, padding="lg")
        control_frame.grid(row=0, column=column, padx=get_spacing('md'), sticky='nsew')
        
        title = FineUseLabel(control_frame, "MAINTENANCE", level="h3")
        title.pack(pady=get_spacing('md'))
        
        # Button grid
        button_grid = FineUseButtonGrid(control_frame, layout="halves")
        button_grid.add_button("RUN DIAGNOSTICS", command=self.run_diagnostics, variant="info")
        button_grid.add_button("CLEAR LOGS", command=self.clear_logs, variant="warning")
    
    def build_log_terminal(self):
        """Build terminal-style log display"""
        log_frame = FineUseFrame(self.app.main_frame, padding="xl")
        log_frame.pack(fill='both', expand=True, pady=get_spacing('lg'))
        
        # Terminal header
        terminal_header = tk.Frame(log_frame, bg=fine_use.colors['border'], height=40)
        terminal_header.pack(fill='x')
        terminal_header.pack_propagate(False)
        
        title = FineUseLabel(terminal_header, "SYSTEM EVENT LOG", level="body", color="text")
        title.pack(side='left', padx=get_spacing('lg'), pady=get_spacing('md'))
        
        # Control buttons
        controls_frame = tk.Frame(terminal_header, bg=fine_use.colors['border'])
        controls_frame.pack(side='right', padx=get_spacing('lg'), pady=get_spacing('sm'))
        
        pause_btn = FineUseButton(controls_frame, "PAUSE", size="sm", command=self.toggle_logging)
        pause_btn.pack(side='left', padx=get_spacing('xs'))
        
        clear_btn = FineUseButton(controls_frame, "CLEAR", size="sm", command=self.clear_logs)
        clear_btn.pack(side='left', padx=get_spacing('xs'))
        
        # Log content
        log_content = tk.Frame(log_frame, bg=fine_use.colors['bg'])
        log_content.pack(fill='both', expand=True)
        
        # Scrollable text area
        self.log_text = tk.Text(
            log_content,
            bg=fine_use.colors['bg'],
            fg=fine_use.colors['text'],
            font=get_font('md'),
            relief='flat',
            wrap='none',
            state='disabled'
        )
        
        scrollbar = tk.Scrollbar(log_content, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=scrollbar.set)
        
        self.log_text.pack(side='left', fill='both', expand=True, padx=get_spacing('lg'), pady=get_spacing('lg'))
        scrollbar.pack(side='right', fill='y')
    
    def build_theme_controls(self):
        """Build theme switching controls"""
        theme_frame = FineUseFrame(self.app.main_frame, padding="lg")
        theme_frame.pack(fill='x', pady=get_spacing('lg'))
        
        # Theme label
        theme_label = FineUseLabel(theme_frame, "THEME CONTROLS", level="h3")
        theme_label.pack(side='left')
        
        # Theme buttons
        themes = [
            ("DARK", "github-dark", "primary"),
            ("LIGHT", "github-light", "secondary"),
            ("AMBER", "amber", "warning"),
            ("GRUVBOX", "gruvbox", "success"),
            ("SYNTHWAVE", "synthwave", "info")
        ]
        
        button_frame = tk.Frame(theme_frame, bg=fine_use.colors['surface'])
        button_frame.pack(side='right', padx=get_spacing('lg'))
        
        for name, theme_id, variant in themes:
            btn = FineUseButton(
                button_frame, 
                name, 
                size="sm", 
                variant=variant,
                command=lambda t=theme_id: self.change_theme(t)
            )
            btn.pack(side='left', padx=get_spacing('xs'))
    
    # === EVENT HANDLERS ===
    
    def start_services(self):
        """Start services action"""
        self.add_log_entry("INFO", "Starting all system services...")
        self.add_log_entry("SUCCESS", "All services started successfully")
    
    def stop_processes(self):
        """Stop processes action"""
        self.add_log_entry("WARNING", "Stopping system processes...")
        self.add_log_entry("INFO", "Processes stopped gracefully")
    
    def restart_system(self):
        """Restart system action"""
        self.add_log_entry("WARNING", "System restart initiated...")
        self.add_log_entry("INFO", "System restart in progress")
    
    def emergency_stop(self):
        """Emergency stop action"""
        self.add_log_entry("ERROR", "EMERGENCY STOP ACTIVATED")
        self.add_log_entry("ERROR", "All systems halted immediately")
    
    def service_action(self, service_name):
        """Generic service action"""
        self.add_log_entry("INFO", f"{service_name} service action triggered")
    
    def run_diagnostics(self):
        """Run system diagnostics"""
        self.add_log_entry("INFO", "Running system diagnostics...")
        self.add_log_entry("SUCCESS", "Diagnostics completed - system healthy")
    
    def clear_logs(self):
        """Clear log display"""
        self.log_text.configure(state='normal')
        self.log_text.delete(1.0, tk.END)
        self.log_text.configure(state='disabled')
        self.log_entries = []
        self.add_log_entry("INFO", "Log cleared")
    
    def toggle_logging(self):
        """Toggle log updates"""
        self.is_running = not self.is_running
        status = "resumed" if self.is_running else "paused"
        self.add_log_entry("INFO", f"Logging {status}")
    
    def change_theme(self, theme_id):
        """Change application theme"""
        # Note: In a real implementation, this would rebuild the interface
        # For demo purposes, we'll just log the action
        self.add_log_entry("INFO", f"Theme changed to {theme_id.upper()}")
    
    # === REAL-TIME UPDATES ===
    
    def start_monitoring(self):
        """Start real-time monitoring thread"""
        self.is_running = True
        self.update_thread = threading.Thread(target=self.update_loop, daemon=True)
        self.update_thread.start()
        
        # Start UI update timer
        self.update_ui()
    
    def update_loop(self):
        """Background thread for generating data"""
        while True:
            if self.is_running:
                # Update metrics
                for key in self.metrics:
                    # Simulate metric changes
                    change = random.randint(-10, 10)
                    self.metrics[key] = max(0, min(100, self.metrics[key] + change))
                
                # Occasionally add log entries
                if random.random() < 0.3:
                    messages = [
                        ("INFO", "System checkpoint completed"),
                        ("WARNING", "High memory usage detected"),
                        ("SUCCESS", "Backup process completed"),
                        ("ERROR", "Connection timeout on port 8080"),
                        ("INFO", "Cache refresh initiated"),
                        ("SUCCESS", "Security scan passed")
                    ]
                    level, message = random.choice(messages)
                    self.add_log_entry(level, message)
            
            time.sleep(2)
    
    def update_ui(self):
        """Update UI elements (called from main thread)"""
        if hasattr(self, 'time_label'):
            current_time = datetime.now().strftime("%H:%M:%S")
            self.time_label.configure(text=current_time)
        
        # Update metric displays
        for key, display in self.metric_displays.items():
            value = self.metrics[key]
            display.value_label.configure(text=f"{value}%")
            
            # Update progress bar
            display.progress_bar.place(relwidth=value/100)
            
            # Update color based on value
            if value > 80:
                color = fine_use.colors['error']
            elif value > 60:
                color = fine_use.colors['warning']
            else:
                color = fine_use.colors[display.color]
            
            display.progress_bar.configure(bg=color)
        
        # Schedule next update
        self.app.root.after(1000, self.update_ui)
    
    def add_log_entry(self, level, message):
        """Add entry to log terminal"""
        if not self.is_running and level != "INFO":
            return
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        # Color mapping
        color_map = {
            'INFO': fine_use.colors['comment'],
            'SUCCESS': fine_use.colors['success'],
            'WARNING': fine_use.colors['warning'],
            'ERROR': fine_use.colors['error']
        }
        
        self.log_text.configure(state='normal')
        
        # Insert timestamp
        self.log_text.insert(tk.END, f"[{timestamp}] ", 'timestamp')
        
        # Insert level
        self.log_text.insert(tk.END, f"{level:8} ", level.lower())
        
        # Insert message
        self.log_text.insert(tk.END, f"{message}\n")
        
        # Configure tags for colors
        self.log_text.tag_configure('timestamp', foreground=fine_use.colors['comment'])
        self.log_text.tag_configure('info', foreground=fine_use.colors['comment'])
        self.log_text.tag_configure('success', foreground=fine_use.colors['success'])
        self.log_text.tag_configure('warning', foreground=fine_use.colors['warning'])
        self.log_text.tag_configure('error', foreground=fine_use.colors['error'])
        
        # Auto-scroll to bottom
        self.log_text.see(tk.END)
        self.log_text.configure(state='disabled')
        
        # Limit log entries
        self.log_entries.append((timestamp, level, message))
        if len(self.log_entries) > 100:
            self.log_entries.pop(0)
    
    def run(self):
        """Run the application"""
        # Add initial log entries
        self.add_log_entry("INFO", "Fine Use System Monitor started")
        self.add_log_entry("SUCCESS", "All subsystems initialized")
        self.add_log_entry("INFO", "Real-time monitoring active")
        
        # Start the application
        self.app.run()


if __name__ == "__main__":
    print("Fine Use Design System - Python Implementation Demo")
    print("=" * 50)
    print("Starting complete system monitoring application...")
    print("This demonstrates the full Fine Use design system in Python.")
    print()
    
    try:
        app = SystemMonitorApp()
        app.run()
    except KeyboardInterrupt:
        print("\nApplication stopped by user.")
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure fine_use_core.py and fine_use_tkinter.py are in the parent directory.")
