"""
Fine Use Design System - Complete Python Demo (FIXED VERSION)
============================================================

This demo fixes the common "cut-off content" problem by implementing:
- Adaptive spacing that compresses on smaller screens
- Scrollable interface when content exceeds window height
- Better height calculations
- Responsive layout adjustments

Run with: python fine_use_demo_fixed.py
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
from fine_use_adaptive import (
    AdaptiveFineUseApp, CompactFineUseButton, CompactButtonGrid,
    FineUseScrollableFrame, calculate_required_height
)


class FixedSystemMonitorApp:
    """
    FIXED version of system monitoring application that prevents cut-off
    Uses adaptive spacing and scrolling to fit all content
    """
    
    def __init__(self):
        # Create adaptive Fine Use application with PROPER FINE USE sizing
        self.app = AdaptiveFineUseApp(
            title="Fine Use System Monitor - FIXED (No Cut-off)",
            theme="github-dark",
            width=1400,
            height=800,  # Proper height for Fine Use spacing
            min_height=700,
            adaptive_spacing=True,    # Enable adaptive spacing
            enable_scrolling=True     # Enable scrolling if needed
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
        """Build the complete Fine Use interface with adaptive sizing"""
        
        # === HEADER SECTION ===
        self.build_header()
        
        # === METRICS SECTION ===
        self.build_metrics_section()
        
        # === CONTROL PANELS ===
        self.build_control_panels()
        
        # === LOG TERMINAL (COMPACT) ===
        self.build_log_terminal()
        
        # === THEME CONTROLS ===
        self.build_theme_controls()
    
    def build_header(self):
        """Build application header with adaptive typography"""
        header_frame = tk.Frame(
            self.app.main_frame,
            bg=fine_use.colors['surface'],
            relief='solid',
            bd=2,
            padx=self.app.get_spacing('md'),
            pady=self.app.get_spacing('md')
        )
        header_frame.pack(fill='x', pady=self.app.get_spacing('lg'))
        
        # Main title with PROPER Fine Use font
        title_font = self.app.get_font('3xl', 'bold')  # Proper Fine Use heading
        title = tk.Label(
            header_frame,
            text="FINE USE SYSTEM MONITOR",
            font=title_font,
            fg=fine_use.colors['text'],
            bg=fine_use.colors['surface']
        )
        title.pack()
        
        # Status line with compact spacing
        status_frame = tk.Frame(header_frame, bg=fine_use.colors['surface'])
        status_frame.pack(pady=self.app.get_spacing('md'))
        
        # Compact status indicators
        self.create_status_indicator(status_frame, "VERSION:", "1.2.0", "text")
        self.create_status_indicator(status_frame, "TIME:", "00:00:00", "comment", "time_label")
        self.create_status_indicator(status_frame, "STATUS:", "OPERATIONAL", "success")
        self.create_status_indicator(status_frame, "MODE:", "FIXED DEMO", "info")
    
    def create_status_indicator(self, parent, label, value, color, tag=None):
        """Create a compact status indicator"""
        container = tk.Frame(parent, bg=fine_use.colors['surface'])
        container.pack(side='left', padx=self.app.get_spacing('lg'))
        
        # Use PROPER Fine Use font sizes
        label_font = self.app.get_font('md', 'normal')
        value_font = self.app.get_font('md', 'bold')
        
        label_widget = tk.Label(
            container, 
            text=label, 
            font=label_font,
            fg=fine_use.colors['comment'],
            bg=fine_use.colors['surface']
        )
        label_widget.pack(side='left')
        
        value_widget = tk.Label(
            container, 
            text=value, 
            font=value_font,
            fg=fine_use.colors[color],
            bg=fine_use.colors['surface']
        )
        value_widget.pack(side='left', padx=(self.app.get_spacing('md'), 0))
        
        if tag:
            setattr(self, tag, value_widget)
    
    def build_metrics_section(self):
        """Build compact real-time metrics display"""
        metrics_frame = tk.Frame(
            self.app.main_frame,
            bg=fine_use.colors['surface'],
            relief='solid',
            bd=2,
            padx=self.app.get_spacing('md'),
            pady=self.app.get_spacing('sm')
        )
        metrics_frame.pack(fill='x', pady=self.app.get_spacing('xl'))
        
        # Section title with adaptive font
        section_title = tk.Label(
            metrics_frame,
            text="REAL-TIME SYSTEM METRICS",
            font=self.app.get_font('lg', 'bold'),
            fg=fine_use.colors['text'],
            bg=fine_use.colors['surface']
        )
        section_title.pack(pady=self.app.get_spacing('lg'))
        
        # Compact metrics grid
        grid_frame = tk.Frame(metrics_frame, bg=fine_use.colors['surface'])
        grid_frame.pack(fill='x', pady=self.app.get_spacing('lg'))
        
        # Configure grid
        for i in range(4):
            grid_frame.grid_columnconfigure(i, weight=1)
        
        # Create compact metric displays
        self.metric_displays = {}
        metrics = [
            ('CPU', 'cpu', 'success'),
            ('MEMORY', 'memory', 'warning'),
            ('DISK', 'disk', 'error'),
            ('NETWORK', 'network', 'info')
        ]
        
        for i, (name, key, color) in enumerate(metrics):
            metric_frame = self.create_compact_metric_display(grid_frame, name, color)
            metric_frame.grid(row=0, column=i, padx=self.app.get_spacing('md'), sticky='nsew')
            self.metric_displays[key] = metric_frame
    
    def create_compact_metric_display(self, parent, name, color):
        """Create a compact metric display widget"""
        container = tk.Frame(
            parent,
            bg=fine_use.colors['bg'],
            relief='solid',
            bd=2,
            padx=self.app.get_spacing('lg'),
            pady=self.app.get_spacing('lg')
        )
        
        # Metric name (proper Fine Use font)
        name_label = tk.Label(
            container,
            text=name,
            font=self.app.get_font('md', 'bold'),
            fg=fine_use.colors['comment'],
            bg=fine_use.colors['bg']
        )
        name_label.pack()
        
        # Metric value (proper Fine Use large font)
        value_label = tk.Label(
            container,
            text="0%",
            font=self.app.get_font('3xl', 'bold'),  # Proper Fine Use scale
            fg=fine_use.colors[color],
            bg=fine_use.colors['bg']
        )
        value_label.pack(pady=self.app.get_spacing('md'))
        
        # Compact progress bar
        progress_frame = tk.Frame(container, bg=fine_use.colors['border'], height=3)
        progress_frame.pack(fill='x', pady=self.app.get_spacing('md'))
        progress_frame.pack_propagate(False)
        
        progress_bar = tk.Frame(progress_frame, bg=fine_use.colors[color], height=3)
        progress_bar.place(relwidth=0, relheight=1)
        
        # Store references
        container.value_label = value_label
        container.progress_bar = progress_bar
        container.color = color
        
        return container
    
    def build_control_panels(self):
        """Build compact control panel with button grids"""
        controls_frame = tk.Frame(
            self.app.main_frame,
            bg=fine_use.colors['surface'],
            relief='solid',
            bd=2,
            padx=self.app.get_spacing('md'),
            pady=self.app.get_spacing('sm')
        )
        controls_frame.pack(fill='x', pady=self.app.get_spacing('xl'))
        
        section_title = tk.Label(
            controls_frame,
            text="SYSTEM CONTROL PANELS",
            font=self.app.get_font('lg', 'bold'),
            fg=fine_use.colors['text'],
            bg=fine_use.colors['surface']
        )
        section_title.pack(pady=self.app.get_spacing('lg'))
        
        # Create three compact control sections
        panels_frame = tk.Frame(controls_frame, bg=fine_use.colors['surface'])
        panels_frame.pack(fill='x', pady=self.app.get_spacing('lg'))
        
        for i in range(3):
            panels_frame.grid_columnconfigure(i, weight=1)
        
        # System Controls
        self.build_system_controls(panels_frame, 0)
        
        # Service Controls  
        self.build_service_controls(panels_frame, 1)
        
        # Maintenance Controls
        self.build_maintenance_controls(panels_frame, 2)
    
    def build_system_controls(self, parent, column):
        """Build compact system control buttons"""
        control_frame = tk.Frame(
            parent,
            bg=fine_use.colors['bg'],
            relief='solid',
            bd=2,
            padx=self.app.get_spacing('xs'),
            pady=self.app.get_spacing('xs')
        )
        control_frame.grid(row=0, column=column, padx=self.app.get_spacing('lg'), sticky='nsew')
        
        title = tk.Label(
            control_frame,
            text="SYSTEM CONTROLS",
            font=self.app.get_font('sm', 'bold'),
            fg=fine_use.colors['text'],
            bg=fine_use.colors['bg']
        )
        title.pack(pady=self.app.get_spacing('md'))
        
        # Compact button grid
        button_grid = CompactButtonGrid(control_frame, layout="2x2", adaptive_app=self.app)
        button_grid.add_button("START SERVICES", command=self.start_services, variant="primary")
        button_grid.add_button("STOP PROCESSES", command=self.stop_processes)
        button_grid.add_button("RESTART SYSTEM", command=self.restart_system, variant="warning")
        button_grid.add_button("EMERGENCY STOP", command=self.emergency_stop, variant="error")
    
    def build_service_controls(self, parent, column):
        """Build compact service control buttons"""
        control_frame = tk.Frame(
            parent,
            bg=fine_use.colors['bg'],
            relief='solid',
            bd=2,
            padx=self.app.get_spacing('xs'),
            pady=self.app.get_spacing('xs')
        )
        control_frame.grid(row=0, column=column, padx=self.app.get_spacing('xs'), sticky='nsew')
        
        title = tk.Label(
            control_frame,
            text="SERVICE CONTROLS",
            font=self.app.get_font('sm', 'bold'),
            fg=fine_use.colors['text'],
            bg=fine_use.colors['bg']
        )
        title.pack(pady=self.app.get_spacing('xs'))
        
        # Compact button grid
        button_grid = CompactButtonGrid(control_frame, layout="1x4", adaptive_app=self.app)
        button_grid.add_button("DATABASE", command=lambda: self.service_action("DATABASE"), variant="info")
        button_grid.add_button("WEB SERVER", command=lambda: self.service_action("WEB SERVER"))
        button_grid.add_button("CACHE", command=lambda: self.service_action("CACHE"), variant="success")
        button_grid.add_button("MONITORING", command=lambda: self.service_action("MONITORING"))
    
    def build_maintenance_controls(self, parent, column):
        """Build compact maintenance control buttons"""
        control_frame = tk.Frame(
            parent,
            bg=fine_use.colors['bg'],
            relief='solid',
            bd=2,
            padx=self.app.get_spacing('xs'),
            pady=self.app.get_spacing('xs')
        )
        control_frame.grid(row=0, column=column, padx=self.app.get_spacing('xs'), sticky='nsew')
        
        title = tk.Label(
            control_frame,
            text="MAINTENANCE",
            font=self.app.get_font('sm', 'bold'),
            fg=fine_use.colors['text'],
            bg=fine_use.colors['bg']
        )
        title.pack(pady=self.app.get_spacing('xs'))
        
        # Compact button grid
        button_grid = CompactButtonGrid(control_frame, layout="halves", adaptive_app=self.app)
        button_grid.add_button("RUN DIAGNOSTICS", command=self.run_diagnostics, variant="info")
        button_grid.add_button("CLEAR LOGS", command=self.clear_logs, variant="warning")
    
    def build_log_terminal(self):
        """Build compact terminal-style log display"""
        log_frame = tk.Frame(
            self.app.main_frame,
            bg=fine_use.colors['surface'],
            relief='solid',
            bd=2,
            padx=self.app.get_spacing('md'),
            pady=self.app.get_spacing('sm')
        )
        log_frame.pack(fill='x', pady=self.app.get_spacing('xl'))
        
        # Compact terminal header
        terminal_header = tk.Frame(log_frame, bg=fine_use.colors['border'])
        terminal_header.pack(fill='x')
        
        title = tk.Label(
            terminal_header,
            text="SYSTEM EVENT LOG",
            font=self.app.get_font('sm', 'bold'),
            fg=fine_use.colors['text'],
            bg=fine_use.colors['border']
        )
        title.pack(side='left', padx=self.app.get_spacing('lg'), pady=self.app.get_spacing('md'))
        
        # Control buttons
        controls_frame = tk.Frame(terminal_header, bg=fine_use.colors['border'])
        controls_frame.pack(side='right', padx=self.app.get_spacing('lg'), pady=self.app.get_spacing('md'))
        
        pause_btn = CompactFineUseButton(
            controls_frame, 
            "PAUSE", 
            size="sm", 
            adaptive_app=self.app,
            command=self.toggle_logging
        )
        pause_btn.pack(side='left', padx=self.app.get_spacing('md'))
        
        clear_btn = CompactFineUseButton(
            controls_frame, 
            "CLEAR", 
            size="sm", 
            adaptive_app=self.app,
            command=self.clear_logs
        )
        clear_btn.pack(side='left', padx=self.app.get_spacing('md'))
        
        # Compact log content (limited height)
        log_content = tk.Frame(log_frame, bg=fine_use.colors['bg'])
        log_content.pack(fill='x')
        
        # Compact scrollable text area
        self.log_text = tk.Text(
            log_content,
            bg=fine_use.colors['bg'],
            fg=fine_use.colors['text'],
            font=self.app.get_font('sm'),  # Proper readable font for logs
            relief='flat',
            wrap='none',
            state='disabled',
            height=8  # Proper height for Fine Use terminal
        )
        
        scrollbar = tk.Scrollbar(log_content, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=scrollbar.set)
        
        self.log_text.pack(side='left', fill='both', expand=True, padx=self.app.get_spacing('lg'), pady=self.app.get_spacing('lg'))
        scrollbar.pack(side='right', fill='y')
    
    def build_theme_controls(self):
        """Build compact theme switching controls"""
        theme_frame = tk.Frame(
            self.app.main_frame,
            bg=fine_use.colors['surface'],
            relief='solid',
            bd=2,
            padx=self.app.get_spacing('md'),
            pady=self.app.get_spacing('sm')
        )
        theme_frame.pack(fill='x', pady=self.app.get_spacing('xl'))
        
        # Theme label
        theme_label = tk.Label(
            theme_frame,
            text="THEME CONTROLS",
            font=self.app.get_font('sm', 'bold'),
            fg=fine_use.colors['text'],
            bg=fine_use.colors['surface']
        )
        theme_label.pack(side='left')
        
        # Compact theme buttons
        themes = [
            ("DARK", "github-dark", "primary"),
            ("LIGHT", "github-light", "secondary"),
            ("AMBER", "amber", "warning"),
            ("GRUVBOX", "gruvbox", "success"),
            ("SYNTHWAVE", "synthwave", "info")
        ]
        
        button_frame = tk.Frame(theme_frame, bg=fine_use.colors['surface'])
        button_frame.pack(side='right', padx=self.app.get_spacing('lg'))
        
        for name, theme_id, variant in themes:
            btn = CompactFineUseButton(
                button_frame, 
                name, 
                size="sm", 
                variant=variant,
                adaptive_app=self.app,
                command=lambda t=theme_id: self.change_theme(t)
            )
            btn.pack(side='left', padx=self.app.get_spacing('md'))
    
    # === EVENT HANDLERS ===
    def start_services(self):
        self.add_log_entry("INFO", "Starting all system services...")
        self.add_log_entry("SUCCESS", "All services started successfully")
    
    def stop_processes(self):
        self.add_log_entry("WARNING", "Stopping system processes...")
        self.add_log_entry("INFO", "Processes stopped gracefully")
    
    def restart_system(self):
        self.add_log_entry("WARNING", "System restart initiated...")
        self.add_log_entry("INFO", "System restart in progress")
    
    def emergency_stop(self):
        self.add_log_entry("ERROR", "EMERGENCY STOP ACTIVATED")
        self.add_log_entry("ERROR", "All systems halted immediately")
    
    def service_action(self, service_name):
        self.add_log_entry("INFO", f"{service_name} service action triggered")
    
    def run_diagnostics(self):
        self.add_log_entry("INFO", "Running system diagnostics...")
        self.add_log_entry("SUCCESS", "Diagnostics completed - system healthy")
    
    def clear_logs(self):
        self.log_text.configure(state='normal')
        self.log_text.delete(1.0, tk.END)
        self.log_text.configure(state='disabled')
        self.log_entries = []
        self.add_log_entry("INFO", "Log cleared")
    
    def toggle_logging(self):
        self.is_running = not self.is_running
        status = "resumed" if self.is_running else "paused"
        self.add_log_entry("INFO", f"Logging {status}")
    
    def change_theme(self, theme_id):
        self.add_log_entry("INFO", f"Theme changed to {theme_id.upper()}")
    
    # === REAL-TIME UPDATES ===
    def start_monitoring(self):
        self.is_running = True
        self.update_thread = threading.Thread(target=self.update_loop, daemon=True)
        self.update_thread.start()
        self.update_ui()
    
    def update_loop(self):
        while True:
            if self.is_running:
                for key in self.metrics:
                    change = random.randint(-10, 10)
                    self.metrics[key] = max(0, min(100, self.metrics[key] + change))
                
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
        if hasattr(self, 'time_label'):
            current_time = datetime.now().strftime("%H:%M:%S")
            self.time_label.configure(text=current_time)
        
        # Update metric displays
        for key, display in self.metric_displays.items():
            value = self.metrics[key]
            display.value_label.configure(text=f"{value}%")
            display.progress_bar.place(relwidth=value/100)
            
            if value > 80:
                color = fine_use.colors['error']
            elif value > 60:
                color = fine_use.colors['warning']
            else:
                color = fine_use.colors[display.color]
            
            display.progress_bar.configure(bg=color)
        
        self.app.root.after(1000, self.update_ui)
    
    def add_log_entry(self, level, message):
        if not self.is_running and level != "INFO":
            return
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        color_map = {
            'INFO': fine_use.colors['comment'],
            'SUCCESS': fine_use.colors['success'],
            'WARNING': fine_use.colors['warning'],
            'ERROR': fine_use.colors['error']
        }
        
        self.log_text.configure(state='normal')
        
        self.log_text.insert(tk.END, f"[{timestamp}] ", 'timestamp')
        self.log_text.insert(tk.END, f"{level:8} ", level.lower())
        self.log_text.insert(tk.END, f"{message}\n")
        
        self.log_text.tag_configure('timestamp', foreground=fine_use.colors['comment'])
        self.log_text.tag_configure('info', foreground=fine_use.colors['comment'])
        self.log_text.tag_configure('success', foreground=fine_use.colors['success'])
        self.log_text.tag_configure('warning', foreground=fine_use.colors['warning'])
        self.log_text.tag_configure('error', foreground=fine_use.colors['error'])
        
        self.log_text.see(tk.END)
        self.log_text.configure(state='disabled')
        
        self.log_entries.append((timestamp, level, message))
        if len(self.log_entries) > 50:  # Limit log entries
            self.log_entries.pop(0)
    
    def run(self):
        """Run the application"""
        self.add_log_entry("INFO", "Fine Use System Monitor started (FIXED VERSION)")
        self.add_log_entry("SUCCESS", "Adaptive layout prevents content cut-off")
        self.add_log_entry("INFO", "Real-time monitoring active")
        
        self.app.run()


if __name__ == "__main__":
    print("Fine Use Design System - FIXED Python Implementation")
    print("=" * 55)
    print("Starting adaptive system monitoring application...")
    print("This version FIXES the content cut-off problem with:")
    print("• Adaptive spacing that compresses on smaller screens")
    print("• Scrollable interface when content exceeds window height")
    print("• Better height calculations")
    print("• Responsive layout adjustments")
    print()
    
    try:
        app = FixedSystemMonitorApp()
        app.run()
    except KeyboardInterrupt:
        print("\nApplication stopped by user.")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
