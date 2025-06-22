"""
Fine Use Design System - Log Terminal Component
Perfect log formatting matching HTML demos exactly
"""

from PySide6.QtWidgets import QTextEdit, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt, QTimer, Signal
from PySide6.QtGui import QTextCursor, QFont, QTextCharFormat, QColor
from datetime import datetime
import random

class FineUseLogTerminal(QTextEdit):
    """Perfect Fine Use log terminal with exact HTML demo formatting"""
    
    LOG_LEVELS = {
        'INFO': {'color': '#58a6ff', 'weight': 700},     # Accent blue
        'WARN': {'color': '#d29922', 'weight': 700},     # Warning yellow
        'ERROR': {'color': '#da3633', 'weight': 700},    # Error red
        'SUCCESS': {'color': '#238636', 'weight': 700},  # Success green
        'DEBUG': {'color': '#7d8590', 'weight': 700}     # Comment gray
    }
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.max_lines = 50  # Limit log lines like HTML demo
        self.init_styling()
        self.setup_auto_logging()
    
    def init_styling(self):
        """Initialize terminal with perfect Fine Use styling"""
        # Set exact log terminal styling
        self.setObjectName("log-terminal")
        self.setReadOnly(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        # Font and basic styling
        self.setStyleSheet("""
            QTextEdit {
                background-color: #0d1117;
                border: 2px solid #30363d;
                color: #f0f6fc;
                font-family: 'Fira Code', monospace;
                font-size: 12px;
                font-weight: 500;
                padding: 16px;
                border-radius: 0px;
            }
        """)
        
        # Enable rich text for colored log levels
        self.setAcceptRichText(True)
    
    def add_log_entry(self, level: str, message: str, timestamp: datetime = None):
        """Add a log entry with proper formatting"""
        if timestamp is None:
            timestamp = datetime.now()
        
        # Format timestamp like HTML demo
        time_str = timestamp.strftime("%H:%M:%S")
        
        # Get level styling
        level_style = self.LOG_LEVELS.get(level.upper(), self.LOG_LEVELS['INFO'])
        
        # Format entry exactly like HTML demo: [timestamp] LEVEL message
        log_html = f"""
        <div style="margin-bottom: 4px; font-family: 'Fira Code', monospace; font-size: 12px;">
            <span style="color: #7d8590;">[{time_str}]</span>
            <span style="color: {level_style['color']}; font-weight: {level_style['weight']}; margin-left: 8px;">{level.upper()}</span>
            <span style="color: #f0f6fc; margin-left: 8px;">{message}</span>
        </div>
        """
        
        # Add to terminal
        cursor = self.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        cursor.insertHtml(log_html)
        
        # Auto-scroll to bottom
        self.setTextCursor(cursor)
        self.ensureCursorVisible()
        
        # Limit number of lines
        self._limit_lines()
    
    def _limit_lines(self):
        """Limit the number of log lines to prevent memory issues"""
        # Get all text and split into lines
        all_text = self.toPlainText()
        lines = all_text.split('\\n')
        
        if len(lines) > self.max_lines:
            # Keep only the most recent lines
            recent_lines = lines[-self.max_lines:]
            
            # Clear and re-add with formatting
            self.clear()
            
            # Note: We lose formatting here, but it prevents memory issues
            # In a real implementation, you'd want to track formatted entries
            for line in recent_lines:
                if line.strip():
                    # Try to parse back the log level for re-formatting
                    self._parse_and_add_line(line)
    
    def _parse_and_add_line(self, line: str):
        """Parse a plain text line and re-add with formatting"""
        # Simple parsing to restore formatting
        try:
            if '] INFO ' in line:
                parts = line.split('] INFO ', 1)
                timestamp = parts[0].replace('[', '')
                message = parts[1]
                self.add_log_entry('INFO', message, datetime.strptime(timestamp, '%H:%M:%S'))
            elif '] WARN ' in line:
                parts = line.split('] WARN ', 1)
                timestamp = parts[0].replace('[', '')
                message = parts[1]
                self.add_log_entry('WARN', message, datetime.strptime(timestamp, '%H:%M:%S'))
            elif '] ERROR ' in line:
                parts = line.split('] ERROR ', 1)
                timestamp = parts[0].replace('[', '')
                message = parts[1]
                self.add_log_entry('ERROR', message, datetime.strptime(timestamp, '%H:%M:%S'))
            elif '] SUCCESS ' in line:
                parts = line.split('] SUCCESS ', 1)
                timestamp = parts[0].replace('[', '')
                message = parts[1]
                self.add_log_entry('SUCCESS', message, datetime.strptime(timestamp, '%H:%M:%S'))
        except:
            # If parsing fails, just add as plain text
            pass
    
    def setup_auto_logging(self):
        """Setup automatic log generation like HTML demo"""
        self.log_timer = QTimer()
        self.log_timer.timeout.connect(self._generate_random_log)
        self.log_timer.start(2000)  # New log every 2 seconds
        
        # Sample log messages like HTML demo
        self.sample_messages = [
            ("INFO", "Service mesh configuration updated"),
            ("WARN", "Memory threshold exceeded"),
            ("ERROR", "Connection pool exhausted"),
            ("SUCCESS", "Cache invalidation triggered"),
            ("INFO", "Security scan initiated"),
            ("WARN", "Load balancer reconfigured"),
            ("SUCCESS", "Database backup completed"),
            ("ERROR", "Authentication timeout"),
            ("INFO", "System health check passed"),
            ("WARN", "High CPU usage detected"),
            ("SUCCESS", "Service restart completed"),
            ("ERROR", "Disk space critical"),
            ("INFO", "Configuration sync finished"),
            ("DEBUG", "Network latency: 45ms")
        ]
    
    def _generate_random_log(self):
        """Generate a random log entry"""
        level, message = random.choice(self.sample_messages)
        self.add_log_entry(level, message)
    
    def clear_logs(self):
        """Clear all log entries"""
        self.clear()
    
    def pause_auto_logging(self):
        """Pause automatic log generation"""
        self.log_timer.stop()
    
    def resume_auto_logging(self):
        """Resume automatic log generation"""
        self.log_timer.start(2000)


class FineUseLogTerminalWithControls(QWidget):
    """Log terminal with control buttons matching HTML demo"""
    
    def __init__(self, title: str = "SYSTEM EVENT LOG", parent=None):
        super().__init__(parent)
        self.title = title
        self.is_paused = False
        self.init_ui()
    
    def init_ui(self):
        """Initialize terminal with header and controls"""
        layout = QVBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Terminal header with title and controls
        header = QWidget()
        header.setStyleSheet("""
            QWidget {
                background-color: #30363d;
                border: 2px solid #30363d;
                border-bottom: 1px solid #30363d;
                padding: 8px 16px;
            }
        """)
        
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(8, 8, 8, 8)
        
        # Title
        title_label = QLabel(self.title)
        title_label.setStyleSheet("""
            QLabel {
                color: #f0f6fc;
                font-family: 'Fira Code', monospace;
                font-size: 14px;
                font-weight: 700;
                text-transform: uppercase;
                background: transparent;
                border: none;
            }
        """)
        header_layout.addWidget(title_label)
        
        header_layout.addStretch()
        
        # Control buttons
        self.pause_button = QPushButton("PAUSE")
        self.pause_button.setStyleSheet("""
            QPushButton {
                background-color: #161b22;
                border: 1px solid #30363d;
                color: #f0f6fc;
                font-family: 'Fira Code', monospace;
                font-size: 11px;
                font-weight: 700;
                text-transform: uppercase;
                padding: 4px 8px;
                border-radius: 0px;
            }
            QPushButton:hover {
                background-color: #30363d;
            }
        """)
        self.pause_button.clicked.connect(self._toggle_pause)
        header_layout.addWidget(self.pause_button)
        
        self.clear_button = QPushButton("CLEAR")
        self.clear_button.setStyleSheet("""
            QPushButton {
                background-color: #161b22;
                border: 1px solid #30363d;
                color: #f0f6fc;
                font-family: 'Fira Code', monospace;
                font-size: 11px;
                font-weight: 700;
                text-transform: uppercase;
                padding: 4px 8px;
                border-radius: 0px;
            }
            QPushButton:hover {
                background-color: #30363d;
            }
        """)
        self.clear_button.clicked.connect(self._clear_logs)
        header_layout.addWidget(self.clear_button)
        
        layout.addWidget(header)
        
        # Log terminal
        self.terminal = FineUseLogTerminal()
        self.terminal.setMinimumHeight(200)
        layout.addWidget(self.terminal)
    
    def _toggle_pause(self):
        """Toggle pause state"""
        self.is_paused = not self.is_paused
        
        if self.is_paused:
            self.terminal.pause_auto_logging()
            self.pause_button.setText("RESUME")
        else:
            self.terminal.resume_auto_logging()
            self.pause_button.setText("PAUSE")
    
    def _clear_logs(self):
        """Clear all logs"""
        self.terminal.clear_logs()
    
    def add_log(self, level: str, message: str):
        """Add a log entry"""
        self.terminal.add_log_entry(level, message)
    
    def get_terminal(self) -> FineUseLogTerminal:
        """Get the underlying terminal widget"""
        return self.terminal
