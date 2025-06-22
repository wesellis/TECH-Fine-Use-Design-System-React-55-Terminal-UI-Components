"""
Fine Use Design System - Proper Spacing Demo
===========================================

This demo shows the CORRECT Fine Use spacing implementation:
- Proper geometric spacing hierarchy
- No cramped/compressed layouts  
- Professional appearance matching HTML demos
- Full visibility with proper spacing

This is the REFERENCE implementation for Fine Use spacing in Python.

Run with: python fine_use_demo_proper_spacing.py
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


class ProperSpacingSystemMonitorApp:
    """
    REFERENCE implementation showing proper Fine Use spacing
    This matches the HTML demo spacing and geometric precision
    """
    
    def __init__(self):
        # Create Fine Use application with SMART responsive dimensions
        self.root = tk.Tk()
        self.root.title("Fine Use System Monitor - PROPER SPACING REFERENCE")
        
        # Smart window sizing - elegant solution for all content
        screen_height = self.root.winfo_screenheight()
        optimal_height = min(950, int(screen_height * 0.85))  # 950px or 85% of screen
        self.root.geometry(f"1400x{optimal_height}")
        self.root.configure(bg=fine_use.colors['bg'])
        
        # Configure font
        self.root.option_add('*TkDefaultFont', get_font('md'))
        
        # Smart spacing calculation based on available height
        self.spacing_mode = self.calculate_spacing_mode(optimal_height)
        
        # Main container with SMART Fine Use window padding
        window_padding = self.get_smart_spacing('window')
        self.main_frame = tk.Frame(
            self.root,
            bg=fine_use.colors['bg'],
            padx=window_padding,
            pady=window_padding
        )
        self.main_frame.pack(fill='both', expand=True)
        
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
        
        # Build interface with proper spacing
        self.build_interface()
        
        # Start real-time updates
        self.start_monitoring()
    
    def calculate_spacing_mode(self, window_height):
        """Calculate optimal spacing mode based on available height"""
        if window_height >= 950:
            return 'optimal'    # Full Fine Use spacing
        elif window_height >= 800:
            return 'standard'   # Slightly reduced but still elegant
        else:
            return 'compact'    # Compressed but maintains proportions
    
    def get_smart_spacing(self, context):
        """Get spacing value based on context and current mode"""
        spacing_map = {
            'optimal': {
                'window': get_spacing('xxl'),     # 30px
                'section': get_spacing('xxl'),    # 30px
                'component': get_spacing('xl'),   # 20px
                'element': get_spacing('lg'),     # 15px
                'button': get_spacing('md')       # 10px
            },
            'standard': {
                'window': get_spacing('xl'),      # 20px
                'section': get_spacing('xl'),     # 20px  
                'component': get_spacing('lg'),   # 15px
                'element': get_spacing('md'),     # 10px
                'button': get_spacing('sm')       # 5px
            },
            'compact': {
                'window': get_spacing('lg'),      # 15px
                'section': get_spacing('lg'),     # 15px
                'component': get_spacing('md'),   # 10px
                'element': get_spacing('sm'),     # 5px
                'button': get_spacing('xs')       # 2px
            }
        }
        return spacing_map[self.spacing_mode][context]
    
    def get_smart_font(self, base_size, weight='normal'):
        """Get font size based on spacing mode"""
        font_scale = {
            'optimal': 1.0,    # Full size
            'standard': 0.9,   # Slightly smaller
            'compact': 0.8     # Compressed but readable
        }
        
        scale = font_scale[self.spacing_mode]
        if base_size == '4xl':
            return get_font('3xl' if scale < 1.0 else '4xl', weight)
        elif base_size == '3xl':
            return get_font('2xl' if scale < 0.9 else '3xl', weight)
        elif base_size == '2xl':
            return get_font('xl' if scale < 0.9 else '2xl', weight)
        elif base_size == 'xl':
            return get_font('lg' if scale < 0.9 else 'xl', weight)
        else:
            return get_font(base_size, weight)
    
    def build_interface(self):
        """Build interface with PROPER Fine Use spacing hierarchy"""
        
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
        """Header with PROPER Fine Use typography and spacing"""
        header_frame = tk.Frame(
            self.main_frame,
            bg=fine_use.colors['surface'],
            relief='solid',
            bd=2,
            padx=self.get_smart_spacing('component'),
            pady=self.get_smart_spacing('component')
        )
        header_frame.pack(fill='x', pady=(0, self.get_smart_spacing('section')))
        
        # Main title with SMART Fine Use scale
        title = tk.Label(
            header_frame,
            text="FINE USE SYSTEM MONITOR",
            font=self.get_smart_font('4xl', 'bold'),
            fg=fine_use.colors['text'],
            bg=fine_use.colors['surface']
        )
        title.pack()
        
        # Status line with PROPER spacing
        status_frame = tk.Frame(header_frame, bg=fine_use.colors['surface'])
        status_frame.pack(pady=self.get_smart_spacing('element'))
        
        # Status indicators with PROPER Fine Use spacing
        self.create_status_indicator(status_frame, "VERSION:", "1.2.0", "text")
        self.create_status_indicator(status_frame, "TIME:", "00:00:00", "comment", "time_label")
        self.create_status_indicator(status_frame, "STATUS:", "OPERATIONAL", "success")
        self.create_status_indicator(status_frame, "MODE:", "PROPER SPACING", "info")
    
    def create_status_indicator(self, parent, label, value, color, tag=None):
        """Status indicator with PROPER Fine Use spacing"""
        container = tk.Frame(parent, bg=fine_use.colors['surface'])
        container.pack(side='left', padx=self.get_smart_spacing('element'))
        
        # SMART font sizes
        label_font = self.get_smart_font('lg', 'normal')
        value_font = self.get_smart_font('lg', 'bold')
        
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
        value_widget.pack(side='left', padx=(self.get_smart_spacing('button'), 0))
        
        if tag:
            setattr(self, tag, value_widget)
    
    def build_metrics_section(self):
        """Metrics with PROPER Fine Use spacing"""
        metrics_frame = tk.Frame(
            self.main_frame,
            bg=fine_use.colors['surface'],
            relief='solid',
            bd=2,
            padx=get_spacing('xl'),
            pady=get_spacing('xl')
        )
        metrics_frame.pack(fill='x', pady=(0, self.get_smart_spacing('section')))
        
        # Section title
        section_title = tk.Label(
            metrics_frame,
            text="REAL-TIME SYSTEM METRICS",
            font=get_font('2xl', 'bold'),
            fg=fine_use.colors['text'],
            bg=fine_use.colors['surface']
        )
        section_title.pack(pady=(0, self.get_smart_spacing('element')))
        
        # Metrics grid with PROPER spacing
        grid_frame = tk.Frame(metrics_frame, bg=fine_use.colors['surface'])
        grid_frame.pack(fill='x')
        
        # Configure equal columns
        for i in range(4):
            grid_frame.grid_columnconfigure(i, weight=1)
        
        # Create metric displays with PROPER spacing
        self.metric_displays = {}
        metrics = [
            ('CPU', 'cpu', 'success'),
            ('MEMORY', 'memory', 'warning'),
            ('DISK', 'disk', 'error'),
            ('NETWORK', 'network', 'info')
        ]
        
        for i, (name, key, color) in enumerate(metrics):
            metric_frame = self.create_metric_display(grid_frame, name, color)
            metric_frame.grid(
                row=0, column=i, 
                padx=self.get_smart_spacing('element'),
                sticky='nsew'
            )
            self.metric_displays[key] = metric_frame
    
    def create_metric_display(self, parent, name, color):
        """Single metric with PROPER Fine Use spacing"""
        container = tk.Frame(
            parent,
            bg=fine_use.colors['bg'],
            relief='solid',
            bd=2,
            padx=get_spacing('xl'),  # 20px internal padding
            pady=get_spacing('xl')   # 20px internal padding
        )
        
        # Metric name
        name_label = tk.Label(
            container,
            text=name,
            font=self.get_smart_font('lg', 'bold'),
            fg=fine_use.colors['comment'],
            bg=fine_use.colors['bg']
        )
        name_label.pack()
        
        # Metric value (SMART large scale)
        value_label = tk.Label(
            container,
            text="0%",
            font=self.get_smart_font('4xl', 'bold'),
            fg=fine_use.colors[color],
            bg=fine_use.colors['bg']
        )
        value_label.pack(pady=self.get_smart_spacing('element'))
        
        # Progress bar with PROPER dimensions
        progress_frame = tk.Frame(
            container, 
            bg=fine_use.colors['border'], 
            height=6  # Thicker progress bar
        )
        progress_frame.pack(fill='x')
        progress_frame.pack_propagate(False)
        
        progress_bar = tk.Frame(progress_frame, bg=fine_use.colors[color], height=6)
        progress_bar.place(relwidth=0, relheight=1)
        
        # Store references
        container.value_label = value_label
        container.progress_bar = progress_bar
        container.color = color
        
        return container
    
    def build_control_panels(self):
        """Control panels with PROPER Fine Use button grid spacing"""
        controls_frame = tk.Frame(
            self.main_frame,
            bg=fine_use.colors['surface'],
            relief='solid',
            bd=2,
            padx=get_spacing('xl'),
            pady=get_spacing('xl')
        )
        controls_frame.pack(fill='x', pady=(0, self.get_smart_spacing('section')))
        
        section_title = tk.Label(
            controls_frame,
            text="SYSTEM CONTROL PANELS",
            font=get_font('2xl', 'bold'),
            fg=fine_use.colors['text'],
            bg=fine_use.colors['surface']
        )
        section_title.pack(pady=(0, self.get_smart_spacing('element')))
        
        # Three equal columns with PROPER spacing
        panels_frame = tk.Frame(controls_frame, bg=fine_use.colors['surface'])
        panels_frame.pack(fill='x')
        
        for i in range(3):
            panels_frame.grid_columnconfigure(i, weight=1)
        
        # System Controls
        self.build_system_controls(panels_frame, 0)
        
        # Service Controls  
        self.build_service_controls(panels_frame, 1)
        
        # Maintenance Controls
        self.build_maintenance_controls(panels_frame, 2)
    
    def build_system_controls(self, parent, column):
        """System controls with PROPER button grid spacing"""
        control_frame = tk.Frame(
            parent,
            bg=fine_use.colors['bg'],
            relief='solid',
            bd=2,
            padx=get_spacing('lg'),
            pady=get_spacing('lg')
        )
        control_frame.grid(
            row=0, column=column, 
            padx=self.get_smart_spacing('element'),
            sticky='nsew'
        )
        
        title = tk.Label(
            control_frame,
            text="SYSTEM CONTROLS",
            font=get_font('xl', 'bold'),
            fg=fine_use.colors['text'],
            bg=fine_use.colors['bg']
        )
        title.pack(pady=(0, self.get_smart_spacing('element')))
        
        # PROPER Fine Use 2x2 button grid
        self.create_button_grid_2x2(
            control_frame,
            [
                ("START SERVICES", self.start_services, "primary"),
                ("STOP PROCESSES", self.stop_processes, None),
                ("RESTART SYSTEM", self.restart_system, "warning"),
                ("EMERGENCY STOP", self.emergency_stop, "error")
            ]
        )
    
    def build_service_controls(self, parent, column):
        """Service controls with PROPER spacing"""
        control_frame = tk.Frame(
            parent,
            bg=fine_use.colors['bg'],
            relief='solid',
            bd=2,
            padx=get_spacing('lg'),
            pady=get_spacing('lg')
        )
        control_frame.grid(
            row=0, column=column, 
            padx=get_spacing('lg'),
            sticky='nsew'
        )
        
        title = tk.Label(
            control_frame,
            text="SERVICE CONTROLS",
            font=get_font('xl', 'bold'),
            fg=fine_use.colors['text'],
            bg=fine_use.colors['bg']
        )
        title.pack(pady=(0, get_spacing('lg')))
        
        # 1x4 vertical button stack
        self.create_button_grid_1x4(
            control_frame,
            [
                ("DATABASE", lambda: self.service_action("DATABASE"), "info"),
                ("WEB SERVER", lambda: self.service_action("WEB SERVER"), None),
                ("CACHE", lambda: self.service_action("CACHE"), "success"),
                ("MONITORING", lambda: self.service_action("MONITORING"), None)
            ]
        )
    
    def build_maintenance_controls(self, parent, column):
        """Maintenance controls with PROPER spacing"""
        control_frame = tk.Frame(
            parent,
            bg=fine_use.colors['bg'],
            relief='solid',
            bd=2,
            padx=get_spacing('lg'),
            pady=get_spacing('lg')
        )
        control_frame.grid(
            row=0, column=column, 
            padx=get_spacing('lg'),
            sticky='nsew'
        )
        
        title = tk.Label(
            control_frame,
            text="MAINTENANCE",
            font=get_font('xl', 'bold'),
            fg=fine_use.colors['text'],
            bg=fine_use.colors['bg']
        )
        title.pack(pady=(0, get_spacing('lg')))
        
        # Halves button grid
        self.create_button_grid_halves(
            control_frame,
            [
                ("RUN DIAGNOSTICS", self.run_diagnostics, "info"),
                ("CLEAR LOGS", self.clear_logs, "warning")
            ]
        )
    
    def create_button_grid_2x2(self, parent, buttons):
        """Create PROPER Fine Use 2x2 button grid"""
        grid_frame = tk.Frame(parent, bg=fine_use.colors['bg'])
        grid_frame.pack(fill='x')
        
        # Configure equal columns and rows
        for i in range(2):
            grid_frame.grid_columnconfigure(i, weight=1)
            grid_frame.grid_rowconfigure(i, weight=1)
        
        for i, (text, command, variant) in enumerate(buttons):
            row = i // 2
            col = i % 2
            
            button = self.create_fine_use_button(grid_frame, text, command, variant)
            button.grid(
                row=row, column=col,
                padx=self.get_smart_spacing('button'),
                pady=self.get_smart_spacing('button'),
                sticky='nsew'
            )
    
    def create_button_grid_1x4(self, parent, buttons):
        """Create PROPER Fine Use 1x4 button grid"""
        grid_frame = tk.Frame(parent, bg=fine_use.colors['bg'])
        grid_frame.pack(fill='x')
        
        # Configure single column, 4 rows
        grid_frame.grid_columnconfigure(0, weight=1)
        for i in range(4):
            grid_frame.grid_rowconfigure(i, weight=1)
        
        for i, (text, command, variant) in enumerate(buttons):
            button = self.create_fine_use_button(grid_frame, text, command, variant)
            button.grid(
                row=i, column=0,
                padx=0,
                pady=self.get_smart_spacing('button'),
                sticky='ew'
            )
    
    def create_button_grid_halves(self, parent, buttons):
        """Create PROPER Fine Use halves button grid"""
        grid_frame = tk.Frame(parent, bg=fine_use.colors['bg'])
        grid_frame.pack(fill='x')
        
        # Configure two equal columns
        for i in range(2):
            grid_frame.grid_columnconfigure(i, weight=1)
        
        for i, (text, command, variant) in enumerate(buttons):
            button = self.create_fine_use_button(grid_frame, text, command, variant)
            button.grid(
                row=0, column=i,
                padx=self.get_smart_spacing('button'),
                pady=0,
                sticky='ew'
            )
    
    def create_fine_use_button(self, parent, text, command, variant=None):
        """Create PROPER Fine Use button with correct styling"""
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
        
        button = tk.Button(
            parent,
            text=text,
            font=get_font('lg', 'bold'),
            bg=bg,
            fg=fg,
            relief='solid',
            bd=2,
            padx=self.get_smart_spacing('element'),
            pady=self.get_smart_spacing('button'),
            command=command,
            cursor='hand2'
        )
        
        return button
    
    def build_log_terminal(self):
        """Terminal with PROPER Fine Use spacing"""
        log_frame = tk.Frame(
            self.main_frame,
            bg=fine_use.colors['surface'],
            relief='solid',
            bd=2,
            padx=get_spacing('xl'),
            pady=get_spacing('xl')
        )
        log_frame.pack(fill='both', expand=True, pady=(0, self.get_smart_spacing('section')))
        
        # Terminal header
        terminal_header = tk.Frame(log_frame, bg=fine_use.colors['border'])
        terminal_header.pack(fill='x')
        
        title = tk.Label(
            terminal_header,
            text="SYSTEM EVENT LOG",
            font=get_font('lg', 'bold'),
            fg=fine_use.colors['text'],
            bg=fine_use.colors['border']
        )
        title.pack(side='left', padx=self.get_smart_spacing('element'), pady=self.get_smart_spacing('button'))
        
        # Control buttons
        controls_frame = tk.Frame(terminal_header, bg=fine_use.colors['border'])
        controls_frame.pack(side='right', padx=self.get_smart_spacing('element'), pady=self.get_smart_spacing('button'))
        
        pause_btn = self.create_fine_use_button(controls_frame, "PAUSE", self.toggle_logging)
        pause_btn.pack(side='left', padx=self.get_smart_spacing('button'))
        
        clear_btn = self.create_fine_use_button(controls_frame, "CLEAR", self.clear_logs)
        clear_btn.pack(side='left', padx=self.get_smart_spacing('button'))
        
        # Log content with PROPER dimensions
        log_content = tk.Frame(log_frame, bg=fine_use.colors['bg'])
        log_content.pack(fill='both', expand=True)
        
        # Text area with PROPER font and dimensions
        self.log_text = tk.Text(
            log_content,
            bg=fine_use.colors['bg'],
            fg=fine_use.colors['text'],
            font=self.get_smart_font('md'),  # Smart readable font size
            relief='flat',
            wrap='none',
            state='disabled'
        )
        
        scrollbar = tk.Scrollbar(log_content, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=scrollbar.set)
        
        self.log_text.pack(
            side='left', fill='both', expand=True, 
            padx=self.get_smart_spacing('component'), 
            pady=self.get_smart_spacing('component')
        )
        scrollbar.pack(side='right', fill='y')
    
    def build_theme_controls(self):
        """Theme controls with PROPER Fine Use spacing"""
        theme_frame = tk.Frame(
            self.main_frame,
            bg=fine_use.colors['surface'],
            relief='solid',
            bd=2,
            padx=get_spacing('xl'),
            pady=get_spacing('lg')
        )
        theme_frame.pack(fill='x')
        
        # Theme label
        theme_label = tk.Label(
            theme_frame,
            text="THEME CONTROLS",
            font=get_font('lg', 'bold'),
            fg=fine_use.colors['text'],
            bg=fine_use.colors['surface']
        )
        theme_label.pack(side='left')
        
        # Theme buttons with PROPER spacing
        themes = [
            ("DARK", "github-dark", "primary"),
            ("LIGHT", "github-light", None),
            ("AMBER", "amber", "warning"),
            ("GRUVBOX", "gruvbox", "success"),
            ("SYNTHWAVE", "synthwave", "info")
        ]
        
        button_frame = tk.Frame(theme_frame, bg=fine_use.colors['surface'])
        button_frame.pack(side='right', padx=self.get_smart_spacing('element'))
        
        for name, theme_id, variant in themes:
            btn = self.create_fine_use_button(
                button_frame, 
                name, 
                lambda t=theme_id: self.change_theme(t),
                variant
            )
            btn.pack(side='left', padx=self.get_smart_spacing('button'))
    
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
        if len(self.log_entries) > 50:
            self.log_entries.pop(0)
    
    def run(self):
        """Run the application"""
        self.add_log_entry("INFO", "Fine Use System Monitor started (PROPER SPACING)")
        self.add_log_entry("SUCCESS", "Reference implementation with correct Fine Use spacing")
        self.add_log_entry("INFO", "Real-time monitoring active")
        
        self.root.mainloop()


if __name__ == "__main__":
    print("Fine Use Design System - PROPER SPACING REFERENCE")
    print("=" * 55)
    print("Starting REFERENCE implementation with correct Fine Use spacing...")
    print("This version demonstrates:")
    print("• Proper Fine Use spacing hierarchy (30px window, 20px internal, 15px between)")
    print("• Correct typography scales (4xl for big numbers, 2xl for headings)")
    print("• Perfect button grid alignment with geometric precision")
    print("• Professional appearance matching HTML demos")
    print("• Full content visibility with proper spacing")
    print()
    
    try:
        app = ProperSpacingSystemMonitorApp()
        app.run()
    except KeyboardInterrupt:
        print("\nApplication stopped by user.")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
