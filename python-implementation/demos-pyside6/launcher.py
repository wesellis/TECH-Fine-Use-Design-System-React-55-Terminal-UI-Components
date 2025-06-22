import sys
import os
import random
from datetime import datetime

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QFont, QFontDatabase

# Import themes directly
from themes import THEMES
from layouts.dashboard_layout import DashboardLayout

class FineUseSystemMonitor(DashboardLayout):
    def __init__(self):
        super().__init__()
        self.current_theme = 'github-dark'
        self.setup_window()
        self.setup_theme_system()
        self.setup_real_time_updates()
        self.setup_demo_data()
        self.apply_theme(self.current_theme)
        self.show_startup_logs()
    
    def setup_window(self):
        self.setWindowTitle("Fine Use System Monitor - PySide6 Demo")
        self.setGeometry(100, 100, 1400, 900)
        self.setMinimumSize(800, 600)
    
    def setup_theme_system(self):
        theme_selector = self.get_theme_selector()
        theme_selector.theme_changed.connect(self.apply_theme)
    
    def setup_real_time_updates(self):
        self.metrics_timer = QTimer()
        self.metrics_timer.timeout.connect(self.update_metrics)
        self.metrics_timer.start(3000)
        
        self.time_timer = QTimer()
        self.time_timer.timeout.connect(self.update_time_display)
        self.time_timer.start(1000)
        
        self.log_timer = QTimer()
        self.log_timer.timeout.connect(self.generate_random_log)
        self.log_timer.start(7000)
    
    def setup_demo_data(self):
        pass
    
    def apply_theme(self, theme_name):
        if theme_name not in THEMES:
            return
        
        theme = THEMES[theme_name]
        stylesheet = theme.get_stylesheet()
        self.setStyleSheet(stylesheet)
        self.current_theme = theme_name
        
        system_log, _ = self.get_terminals()
        system_log.add_log_entry("SUCCESS", f"Theme changed to {theme.name}")
    
    def update_metrics(self):
        cpu_metric, memory_metric, disk_metric = self.get_metrics()
        
        cpu_change = random.randint(-10, 10)
        memory_change = random.randint(-5, 5)
        disk_change = random.randint(-15, 15)
        
        new_cpu = max(10, min(95, cpu_metric.get_value() + cpu_change))
        new_memory = max(20, min(90, memory_metric.get_value() + memory_change))
        new_disk = max(5, min(85, disk_metric.get_value() + disk_change))
        
        cpu_metric.update_value(new_cpu)
        memory_metric.update_value(new_memory)
        disk_metric.update_value(new_disk)
    
    def generate_random_log(self):
        system_log, operations_log = self.get_terminals()
        
        system_messages = [
            ("INFO", "Service health check completed"),
            ("WARN", "Memory usage approaching threshold"),
            ("SUCCESS", "Backup operation completed"),
            ("INFO", "Network connectivity verified"),
            ("WARN", "Disk usage above 80%"),
            ("SUCCESS", "Cache cleanup completed"),
            ("INFO", "Security scan initiated"),
            ("ERROR", "Connection timeout to external service"),
            ("SUCCESS", "Database optimization completed"),
            ("INFO", "Load balancer configuration updated")
        ]
        
        operations_messages = [
            ("INFO", "Deployment pipeline started"),
            ("SUCCESS", "Service restart completed"),
            ("INFO", "Configuration synchronization"),
            ("SUCCESS", "Database migration completed"),
            ("WARN", "Service degraded performance"),
            ("INFO", "Monitoring alert resolved"),
            ("SUCCESS", "Log rotation completed"),
            ("INFO", "SSL certificate renewal"),
            ("SUCCESS", "Cache invalidation completed"),
            ("INFO", "User session cleanup")
        ]
        
        if random.choice([True, False]):
            level, message = random.choice(system_messages)
            system_log.add_log_entry(level, message)
        else:
            level, message = random.choice(operations_messages)
            operations_log.add_log_entry(level, message)
    
    def show_startup_logs(self):
        system_log, operations_log = self.get_terminals()
        
        system_log.add_log_entry("SUCCESS", "Fine Use System Monitor started")
        system_log.add_log_entry("INFO", "PySide6 implementation initialized")
        system_log.add_log_entry("SUCCESS", "All 10 themes loaded successfully")
        
        operations_log.add_log_entry("INFO", "Dashboard layout manager active")
        operations_log.add_log_entry("SUCCESS", "Real-time metrics system online")
        operations_log.add_log_entry("INFO", "Perfect button alignment achieved")

def main():
    app = QApplication(sys.argv)
    
    QApplication.setApplicationName("Fine Use System Monitor")
    QApplication.setApplicationVersion("2.0.0")
    
    font_db = QFontDatabase()
    available_fonts = font_db.families()
    
    if "Fira Code" in available_fonts:
        default_font = QFont("Fira Code", 10)
    elif "Consolas" in available_fonts:
        default_font = QFont("Consolas", 10)
    else:
        default_font = QFont("monospace", 10)
    
    default_font.setStyleHint(QFont.Monospace)
    QApplication.setFont(default_font)
    
    window = FineUseSystemMonitor()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
