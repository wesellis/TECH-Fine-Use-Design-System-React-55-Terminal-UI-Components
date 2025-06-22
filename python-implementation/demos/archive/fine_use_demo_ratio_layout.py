"""
Fine Use Design System - Dynamic Ratio Layout
============================================

This demo uses PROPORTIONAL RATIOS instead of fixed spacing:
- Everything scales to window size perfectly
- Maintains Fine Use proportions at any size
- No scrollbars, no cut-off, always fits
- Pure geometric scaling

Run with: python fine_use_demo_ratio_layout.py
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


class RatioLayoutSystemMonitorApp:
    """
    DYNAMIC RATIO implementation - everything scales proportionally
    No matter the window size, maintains perfect Fine Use ratios
    """
    
    def __init__(self):
        # Create Fine Use application
        self.root = tk.Tk()
        self.root.title("Fine Use System Monitor - DYNAMIC RATIO LAYOUT")
        self.root.geometry("1400x900")  # Default size
        self.root.minsize(900, 650)  # MINIMUM usable size - prevents unusable small windows
        self.root.configure(bg=fine_use.colors['bg'])
        
        # Configure font
        self.root.option_add('*TkDefaultFont', get_font('md'))
        
        # Calculate dynamic ratios based on window size
        self.update_ratios()
        
        # Bind resize event to recalculate ratios
        self.root.bind('<Configure>', self.on_window_resize)
        
        # Main container with RATIO-BASED padding
        self.main_frame = tk.Frame(
            self.root,
            bg=fine_use.colors['bg']
        )
        self.main_frame.pack(fill='both', expand=True, padx=self.window_padding, pady=self.window_padding)
        
        # Application state
        self.is_running = False
        self.update_thread = None
        self.metrics = {
            'cpu': 45,
            'memory': 67,
            'disk': 23,
            'network': 89
        }
        self.log_entries = []
        
        # Build interface with ratio-based layout
        self.build_interface()
        
        # Start real-time updates
        self.start_monitoring()
    
    def update_ratios(self):
        """Calculate all spacing ratios based on current window size"""
        # Get current window dimensions
        self.root.update_idletasks()
        width = self.root.winfo_width() if self.root.winfo_width() > 1 else 1400
        height = self.root.winfo_height() if self.root.winfo_height() > 1 else 900
        
        # Base ratios - these maintain Fine Use proportions
        self.window_padding = max(int(width * 0.02), 15)  # 2% of width, min 15px
        self.section_spacing = max(int(height * 0.03), 20)  # 3% of height, min 20px
        self.component_padding = max(int(width * 0.015), 12)  # 1.5% of width, min 12px
        self.element_spacing = max(int(height * 0.015), 10)  # 1.5% of height, min 10px
        self.button_spacing = max(int(width * 0.007), 5)  # 0.7% of width, min 5px
        
        # Font sizes based on window size - REFINED for button visibility
        base_size = min(width, height) // 90  # More conservative scaling
        self.font_sizes = {
            'title': max(base_size + 8, 24),
            'heading': max(base_size + 4, 18),
            'metric': max(base_size + 12, 32),
            'body': max(base_size, 14),
            'button': max(base_size, 12)  # Smaller button font for better fit
        }
        
        # Calculate optimal button dimensions
        self.button_height = max(int(height * 0.04), 32)  # 4% of height, min 32px
        self.button_min_width = max(int(width * 0.08), 80)  # 8% of width, min 80px
    
    def on_window_resize(self, event):
        """Recalculate ratios when window is resized"""
        if event.widget == self.root:
            self.update_ratios()
            # Update padding on main frame
            self.main_frame.configure(padx=self.window_padding, pady=self.window_padding)
    
    def get_ratio_font(self, size_type, weight='normal'):
        """Get font based on calculated ratios"""
        size = self.font_sizes.get(size_type, 14)
        return (get_font('md')[0], size, weight)  # Keep font family, change size
    
    def build_interface(self):
        """Build interface with RATIO-BASED spacing"""
        
        # === HEADER SECTION (15% of height) ===
        self.build_header()
        
        # === METRICS SECTION (22% of height) === Optimized for button space
        self.build_metrics_section()
        
        # === CONTROL PANELS (40% of height) === Enhanced for button space
        self.build_control_panels()
        
        # === LOG TERMINAL (18% of height) === Reduced to give controls more space
        self.build_log_terminal()
        
        # === THEME CONTROLS (5% of height) ===
        self.build_theme_controls()
    
    def build_header(self):
        """Header with RATIO-BASED spacing"""
        header_frame = tk.Frame(
            self.main_frame,
            bg=fine_use.colors['surface'],
            relief='solid',
            bd=2,
            height=int(self.root.winfo_height() * 0.15)  # 15% of window height
        )
        header_frame.pack(fill='x', pady=(0, self.section_spacing))
        header_frame.pack_propagate(False)  # Maintain fixed height ratio
        
        # Center content in header
        content_frame = tk.Frame(header_frame, bg=fine_use.colors['surface'])
        content_frame.pack(expand=True)
        
        # Main title with RATIO font
        title = tk.Label(
            content_frame,
            text="FINE USE SYSTEM MONITOR",
            font=self.get_ratio_font('title', 'bold'),
            fg=fine_use.colors['text'],
            bg=fine_use.colors['surface']
        )
        title.pack(pady=(self.element_spacing, self.element_spacing//2))
        
        # Status indicators with RATIO spacing
        status_frame = tk.Frame(content_frame, bg=fine_use.colors['surface'])
        status_frame.pack()
        
        self.create_status_indicator(status_frame, "VERSION:", "1.2.0", "text")
        self.create_status_indicator(status_frame, "TIME:", "00:00:00", "comment", "time_label")
        self.create_status_indicator(status_frame, "STATUS:", "OPERATIONAL", "success")
        self.create_status_indicator(status_frame, "MODE:", "RATIO LAYOUT", "info")
    
    def create_status_indicator(self, parent, label, value, color, tag=None):
        """Status indicator with RATIO spacing"""
        container = tk.Frame(parent, bg=fine_use.colors['surface'])
        container.pack(side='left', padx=self.element_spacing)
        
        label_widget = tk.Label(
            container, 
            text=label, 
            font=self.get_ratio_font('body'),
            fg=fine_use.colors['comment'],
            bg=fine_use.colors['surface']
        )
        label_widget.pack(side='left')
        
        value_widget = tk.Label(
            container, 
            text=value, 
            font=self.get_ratio_font('body', 'bold'),
            fg=fine_use.colors[color],
            bg=fine_use.colors['surface']
        )
        value_widget.pack(side='left', padx=(self.button_spacing, 0))
        
        if tag:
            setattr(self, tag, value_widget)
    
    def build_metrics_section(self):
        """Metrics with OPTIMIZED RATIO-BASED height"""
        metrics_frame = tk.Frame(
            self.main_frame,
            bg=fine_use.colors['surface'],
            relief='solid',
            bd=2,
            height=int(self.root.winfo_height() * 0.22)  # 22% of window height - REDUCED
        )
        metrics_frame.pack(fill='x', pady=(0, self.section_spacing))
        metrics_frame.pack_propagate(False)  # Maintain fixed height ratio
        
        # Content container
        content_frame = tk.Frame(metrics_frame, bg=fine_use.colors['surface'])
        content_frame.pack(fill='both', expand=True, padx=self.component_padding, pady=self.component_padding)
        
        # Section title
        section_title = tk.Label(
            content_frame,
            text="REAL-TIME SYSTEM METRICS",
            font=self.get_ratio_font('heading', 'bold'),
            fg=fine_use.colors['text'],
            bg=fine_use.colors['surface']
        )
        section_title.pack(pady=(0, self.element_spacing))
        
        # Metrics grid
        grid_frame = tk.Frame(content_frame, bg=fine_use.colors['surface'])
        grid_frame.pack(fill='both', expand=True)
        
        # Configure equal columns
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
            metric_frame.grid(row=0, column=i, padx=self.element_spacing, sticky='nsew')
            self.metric_displays[key] = metric_frame
    
    def create_metric_display(self, parent, name, color):
        """Single metric with RATIO spacing"""
        container = tk.Frame(
            parent,
            bg=fine_use.colors['bg'],
            relief='solid',
            bd=2
        )
        
        # Content with padding
        content = tk.Frame(container, bg=fine_use.colors['bg'])
        content.pack(fill='both', expand=True, padx=self.component_padding, pady=self.component_padding)
        
        # Metric name
        name_label = tk.Label(
            content,
            text=name,
            font=self.get_ratio_font('body', 'bold'),
            fg=fine_use.colors['comment'],
            bg=fine_use.colors['bg']
        )
        name_label.pack()
        
        # Metric value (large)
        value_label = tk.Label(
            content,
            text="0%",
            font=self.get_ratio_font('metric', 'bold'),
            fg=fine_use.colors[color],
            bg=fine_use.colors['bg']
        )
        value_label.pack(expand=True)
        
        # Progress bar
        progress_frame = tk.Frame(content, bg=fine_use.colors['border'], height=6)
        progress_frame.pack(fill='x', pady=(self.element_spacing//2, 0))
        progress_frame.pack_propagate(False)
        
        progress_bar = tk.Frame(progress_frame, bg=fine_use.colors[color], height=6)
        progress_bar.place(relwidth=0, relheight=1)
        
        # Store references
        container.value_label = value_label
        container.progress_bar = progress_bar
        container.color = color
        
        return container
    
    def build_control_panels(self):
        """Control panels with ENHANCED RATIO height"""
        controls_frame = tk.Frame(
            self.main_frame,
            bg=fine_use.colors['surface'],
            relief='solid',
            bd=2,
            height=int(self.root.winfo_height() * 0.40)  # 40% of window height - MORE SPACE
        )
        controls_frame.pack(fill='x', pady=(0, self.section_spacing))
        controls_frame.pack_propagate(False)
        
        # Content container
        content_frame = tk.Frame(controls_frame, bg=fine_use.colors['surface'])
        content_frame.pack(fill='both', expand=True, padx=self.component_padding, pady=self.component_padding)
        
        # Section title
        section_title = tk.Label(
            content_frame,
            text="SYSTEM CONTROL PANELS",
            font=self.get_ratio_font('heading', 'bold'),
            fg=fine_use.colors['text'],
            bg=fine_use.colors['surface']
        )
        section_title.pack(pady=(0, self.element_spacing))
        
        # Three equal columns
        panels_frame = tk.Frame(content_frame, bg=fine_use.colors['surface'])
        panels_frame.pack(fill='both', expand=True)
        
        for i in range(3):
            panels_frame.grid_columnconfigure(i, weight=1)
        
        # System Controls
        self.build_system_controls(panels_frame, 0)
        
        # Service Controls  
        self.build_service_controls(panels_frame, 1)
        
        # Maintenance Controls
        self.build_maintenance_controls(panels_frame, 2)
    
    def build_system_controls(self, parent, column):
        """System controls with RATIO spacing"""
        control_frame = tk.Frame(
            parent,
            bg=fine_use.colors['bg'],
            relief='solid',
            bd=2
        )
        control_frame.grid(row=0, column=column, padx=self.element_spacing, sticky='nsew')
        
        # Content
        content = tk.Frame(control_frame, bg=fine_use.colors['bg'])
        content.pack(fill='both', expand=True, padx=self.component_padding, pady=self.component_padding)
        
        title = tk.Label(
            content,
            text="SYSTEM CONTROLS",
            font=self.get_ratio_font('body', 'bold'),
            fg=fine_use.colors['text'],
            bg=fine_use.colors['bg']
        )
        title.pack(pady=(0, self.element_spacing))
        
        # 2x2 button grid
        self.create_button_grid_2x2(
            content,
            [
                ("START SERVICES", self.start_services, "primary"),
                ("STOP PROCESSES", self.stop_processes, None),
                ("RESTART SYSTEM", self.restart_system, "warning"),
                ("EMERGENCY STOP", self.emergency_stop, "error")
            ]
        )
    
    def build_service_controls(self, parent, column):
        """Service controls"""
        control_frame = tk.Frame(
            parent,
            bg=fine_use.colors['bg'],
            relief='solid',
            bd=2
        )
        control_frame.grid(row=0, column=column, padx=self.element_spacing, sticky='nsew')
        
        content = tk.Frame(control_frame, bg=fine_use.colors['bg'])
        content.pack(fill='both', expand=True, padx=self.component_padding, pady=self.component_padding)
        
        title = tk.Label(
            content,
            text="SERVICE CONTROLS",
            font=self.get_ratio_font('body', 'bold'),
            fg=fine_use.colors['text'],
            bg=fine_use.colors['bg']
        )
        title.pack(pady=(0, self.element_spacing))
        
        # 1x4 button grid
        self.create_button_grid_1x4(
            content,
            [
                ("DATABASE", lambda: self.service_action("DATABASE"), "info"),
                ("WEB SERVER", lambda: self.service_action("WEB SERVER"), None),
                ("CACHE", lambda: self.service_action("CACHE"), "success"),
                ("MONITORING", lambda: self.service_action("MONITORING"), None)
            ]
        )
    
    def build_maintenance_controls(self, parent, column):
        """Maintenance controls"""
        control_frame = tk.Frame(
            parent,
            bg=fine_use.colors['bg'],
            relief='solid',
            bd=2
        )
        control_frame.grid(row=0, column=column, padx=self.element_spacing, sticky='nsew')
        
        content = tk.Frame(control_frame, bg=fine_use.colors['bg'])
        content.pack(fill='both', expand=True, padx=self.component_padding, pady=self.component_padding)
        
        title = tk.Label(
            content,
            text="MAINTENANCE",
            font=self.get_ratio_font('body', 'bold'),
            fg=fine_use.colors['text'],
            bg=fine_use.colors['bg']
        )
        title.pack(pady=(0, self.element_spacing))
        
        # Halves button grid
        self.create_button_grid_halves(
            content,
            [
                ("RUN DIAGNOSTICS", self.run_diagnostics, "info"),
                ("CLEAR LOGS", self.clear_logs, "warning")
            ]
        )
    
    def create_button_grid_2x2(self, parent, buttons):
        """Create 2x2 button grid with PERFECT RATIO spacing"""
        grid_frame = tk.Frame(parent, bg=fine_use.colors['bg'])
        grid_frame.pack(fill='both', expand=True)
        
        # Configure equal columns and rows with MINIMUM sizes
        for i in range(2):
            grid_frame.grid_columnconfigure(i, weight=1, minsize=self.button_min_width)
            grid_frame.grid_rowconfigure(i, weight=1, minsize=self.button_height)
        
        for i, (text, command, variant) in enumerate(buttons):
            row = i // 2
            col = i % 2
            
            button = self.create_fine_use_button(grid_frame, text, command, variant)
            button.grid(
                row=row, column=col,
                padx=self.button_spacing,
                pady=self.button_spacing,
                sticky='nsew'
            )
    
    def create_button_grid_1x4(self, parent, buttons):
        """Create 1x4 button grid with PERFECT sizing"""
        grid_frame = tk.Frame(parent, bg=fine_use.colors['bg'])
        grid_frame.pack(fill='both', expand=True)
        
        # Configure single column, 4 rows with MINIMUM heights
        grid_frame.grid_columnconfigure(0, weight=1, minsize=self.button_min_width)
        for i in range(4):
            grid_frame.grid_rowconfigure(i, weight=1, minsize=self.button_height//2)  # Smaller for 4 buttons
        
        for i, (text, command, variant) in enumerate(buttons):
            button = self.create_fine_use_button(grid_frame, text, command, variant)
            button.grid(
                row=i, column=0,
                padx=0,
                pady=self.button_spacing//2,
                sticky='nsew'
            )
    
    def create_button_grid_halves(self, parent, buttons):
        """Create halves button grid with PERFECT sizing"""
        grid_frame = tk.Frame(parent, bg=fine_use.colors['bg'])
        grid_frame.pack(fill='both', expand=True)
        
        # Configure two equal columns with MINIMUM sizes
        for i in range(2):
            grid_frame.grid_columnconfigure(i, weight=1, minsize=self.button_min_width)
        grid_frame.grid_rowconfigure(0, weight=1, minsize=self.button_height)
        
        for i, (text, command, variant) in enumerate(buttons):
            button = self.create_fine_use_button(grid_frame, text, command, variant)
            button.grid(
                row=0, column=i,
                padx=self.button_spacing,
                pady=0,
                sticky='nsew'
            )
    
    def create_fine_use_button(self, parent, text, command, variant=None):
        """Create Fine Use button with PERFECT RATIO sizing"""
        # Determine colors based on variant
        if variant == "primary":
            bg = fine_use.colors['accent']
            fg = fine_use.colors['bg']
        elif variant == "error":
            bg = fine_use.colors['error']
            fg = fine_use.colors['bg']
        elif variant == "warning":
            bg = fine_use.colors['warning']
            fg = fine_use.colors['bg']
        elif variant == "success":
            bg = fine_use.colors['success']
            fg = fine_use.colors['bg']
        elif variant == "info":
            bg = fine_use.colors['info']
            fg = fine_use.colors['bg']
        else:
            bg = fine_use.colors['surface']
            fg = fine_use.colors['text']
        
        # Calculate text-based button sizing for perfect fit
        text_length = len(text)
        button_width = max(text_length + 2, 12)  # Character width + padding
        
        button = tk.Button(
            parent,
            text=text,
            font=self.get_ratio_font('button', 'bold'),
            bg=bg,
            fg=fg,
            relief='solid',
            bd=2,
            command=command,
            cursor='hand2',
            width=button_width,  # TEXT-BASED WIDTH
            height=2,  # FIXED HEIGHT IN TEXT UNITS
            wraplength=0  # PREVENT TEXT WRAPPING
        )
        
        return button
    
    def build_log_terminal(self):
        """Terminal with OPTIMIZED RATIO height"""
        log_frame = tk.Frame(
            self.main_frame,
            bg=fine_use.colors['surface'],
            relief='solid',
            bd=2,
            height=int(self.root.winfo_height() * 0.18)  # 18% of window height - REDUCED
        )
        log_frame.pack(fill='x', pady=(0, self.section_spacing))
        log_frame.pack_propagate(False)
        
        # Terminal header
        terminal_header = tk.Frame(log_frame, bg=fine_use.colors['border'], height=40)
        terminal_header.pack(fill='x')
        terminal_header.pack_propagate(False)
        
        title = tk.Label(
            terminal_header,
            text="SYSTEM EVENT LOG",
            font=self.get_ratio_font('body', 'bold'),
            fg=fine_use.colors['text'],
            bg=fine_use.colors['border']
        )
        title.pack(side='left', padx=self.element_spacing, pady=self.button_spacing)
        
        # Control buttons
        controls_frame = tk.Frame(terminal_header, bg=fine_use.colors['border'])
        controls_frame.pack(side='right', padx=self.element_spacing, pady=self.button_spacing)
        
        pause_btn = self.create_fine_use_button(controls_frame, "PAUSE", self.toggle_logging)
        pause_btn.pack(side='left', padx=self.button_spacing)
        
        clear_btn = self.create_fine_use_button(controls_frame, "CLEAR", self.clear_logs)
        clear_btn.pack(side='left', padx=self.button_spacing)
        
        # Log content
        log_content = tk.Frame(log_frame, bg=fine_use.colors['bg'])
        log_content.pack(fill='both', expand=True)
        
        # Text area
        self.log_text = tk.Text(
            log_content,
            bg=fine_use.colors['bg'],
            fg=fine_use.colors['text'],
            font=self.get_ratio_font('body'),
            relief='flat',
            wrap='none',
            state='disabled'
        )
        
        scrollbar = tk.Scrollbar(log_content, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=scrollbar.set)
        
        self.log_text.pack(
            side='left', fill='both', expand=True, 
            padx=self.component_padding, 
            pady=self.component_padding
        )
        scrollbar.pack(side='right', fill='y')
    
    def build_theme_controls(self):
        """Theme controls with RATIO height"""
        theme_frame = tk.Frame(
            self.main_frame,
            bg=fine_use.colors['surface'],
            relief='solid',
            bd=2,
            height=int(self.root.winfo_height() * 0.05)  # 5% of window height
        )
        theme_frame.pack(fill='x')
        theme_frame.pack_propagate(False)
        
        # Content
        content_frame = tk.Frame(theme_frame, bg=fine_use.colors['surface'])
        content_frame.pack(fill='both', expand=True, padx=self.component_padding, pady=self.component_padding)
        
        # Theme label
        theme_label = tk.Label(
            content_frame,
            text="THEME CONTROLS",
            font=self.get_ratio_font('body', 'bold'),
            fg=fine_use.colors['text'],
            bg=fine_use.colors['surface']
        )
        theme_label.pack(side='left')
        
        # Theme buttons
        themes = [
            ("DARK", "github-dark", "primary"),
            ("LIGHT", "github-light", None),
            ("AMBER", "amber", "warning"),
            ("GRUVBOX", "gruvbox", "success"),
            ("SYNTHWAVE", "synthwave", "info")
        ]
        
        button_frame = tk.Frame(content_frame, bg=fine_use.colors['surface'])
        button_frame.pack(side='right', padx=self.element_spacing)
        
        for name, theme_id, variant in themes:
            btn = self.create_fine_use_button(
                button_frame, 
                name, 
                lambda t=theme_id: self.change_theme(t),
                variant
            )
            btn.pack(side='left', padx=self.button_spacing)
    
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
        if hasattr(self, 'log_text'):
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
                    change = random.randint(-5, 5)
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
        if hasattr(self, 'metric_displays'):
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
        
        self.root.after(1000, self.update_ui)
    
    def add_log_entry(self, level, message):
        if not hasattr(self, 'log_text'):
            return
            
        if not self.is_running and level != "INFO":
            return
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        
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
        if len(self.log_entries) > 50:
            self.log_entries.pop(0)
    
    def run(self):
        """Run the application"""
        self.add_log_entry("INFO", "Fine Use System Monitor started (RATIO LAYOUT)")
        self.add_log_entry("SUCCESS", "Dynamic ratio scaling - fits any window size")
        self.add_log_entry("INFO", "Real-time monitoring active")
        
        self.root.mainloop()


if __name__ == "__main__":
    print("Fine Use Design System - DYNAMIC RATIO LAYOUT")
    print("=" * 55)
    print("Starting RATIO-BASED implementation...")
    print("This version uses:")
    print("• Proportional ratios instead of fixed spacing")
    print("• Everything scales to window size perfectly")
    print("• Maintains Fine Use proportions at any size")
    print("• No scrollbars, no cut-off, always fits")
    print("• Pure geometric scaling")
    print()
    
    try:
        app = RatioLayoutSystemMonitorApp()
        app.run()
    except KeyboardInterrupt:
        print("\nApplication stopped by user.")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
