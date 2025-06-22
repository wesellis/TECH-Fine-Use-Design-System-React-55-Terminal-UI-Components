"""
Fine Use Design System - Tkinter Implementation
==============================================

Complete Tkinter component library that perfectly matches 
the Fine Use web implementation.

Usage:
    from fine_use_tkinter import FineUseApp, FineUseButton
    
    app = FineUseApp(title="System Monitor")
    button = FineUseButton(app.main_frame, text="START SERVICES")
"""

import tkinter as tk
from tkinter import ttk, font
from typing import Optional, Callable, Dict, Any
from fine_use_core import fine_use, get_spacing, get_font, get_border_width


class FineUseApp:
    """
    Main Fine Use application window with theme support
    Provides the foundation for all Fine Use Tkinter apps
    """
    
    def __init__(
        self, 
        title: str = "Fine Use Application",
        theme: str = "github-dark",
        width: int = 1400,
        height: int = 900
    ):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        
        # Set Fine Use theme
        if hasattr(fine_use, 'set_theme'):
            from fine_use_core import FineUseTheme
            theme_enum = getattr(FineUseTheme, theme.upper().replace('-', '_'))
            fine_use.set_theme(theme_enum)
        
        # Configure root window
        self.root.configure(bg=fine_use.colors['bg'])
        
        # Create main frame
        self.main_frame = tk.Frame(
            self.root,
            bg=fine_use.colors['bg'],
            padx=get_spacing('xxl'),
            pady=get_spacing('xxl')
        )
        self.main_frame.pack(fill='both', expand=True)
        
        # Configure default fonts
        self._configure_fonts()
    
    def _configure_fonts(self):
        """Configure default fonts for the application"""
        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(
            family=fine_use.typography.FONT_FAMILY,
            size=fine_use.typography.FONT_SIZES['md']
        )
        
        text_font = font.nametofont("TkTextFont")
        text_font.configure(
            family=fine_use.typography.FONT_FAMILY,
            size=fine_use.typography.FONT_SIZES['md']
        )
    
    def run(self):
        """Start the application"""
        self.root.mainloop()


class FineUseButton(tk.Button):
    """
    Fine Use styled button with exact web implementation styling
    
    Variants: primary, secondary, success, warning, error, info
    Sizes: sm, md, lg, xl
    """
    
    def __init__(
        self,
        parent,
        text: str = "",
        variant: str = "secondary",
        size: str = "md",
        command: Optional[Callable] = None,
        **kwargs
    ):
        # Get theme colors based on variant
        colors = self._get_variant_colors(variant)
        
        # Get font based on size
        font_tuple = get_font(size, 'bold')
        
        # Calculate padding based on size
        padding = self._get_size_padding(size)
        
        super().__init__(
            parent,
            text=text.upper(),  # Fine Use uses uppercase text
            command=command,
            font=font_tuple,
            bg=colors['bg'],
            fg=colors['fg'],
            activebackground=colors['hover_bg'],
            activeforeground=colors['hover_fg'],
            relief='solid',
            bd=get_border_width('thin'),
            highlightthickness=0,
            padx=padding['x'],
            pady=padding['y'],
            cursor='hand2',
            **kwargs
        )
        
        # Store original colors for hover effects
        self.colors = colors
        
        # Bind hover events
        self.bind('<Enter>', self._on_enter)
        self.bind('<Leave>', self._on_leave)
        self.bind('<FocusIn>', self._on_focus_in)
        self.bind('<FocusOut>', self._on_focus_out)
    
    def _get_variant_colors(self, variant: str) -> Dict[str, str]:
        """Get colors for button variant"""
        if variant == "primary":
            return {
                'bg': fine_use.colors['accent'],
                'fg': fine_use.colors['bg'],
                'hover_bg': fine_use.colors['bg'],
                'hover_fg': fine_use.colors['accent']
            }
        elif variant == "success":
            return {
                'bg': fine_use.colors['success'],
                'fg': fine_use.colors['bg'],
                'hover_bg': fine_use.colors['bg'],
                'hover_fg': fine_use.colors['success']
            }
        elif variant == "warning":
            return {
                'bg': fine_use.colors['warning'],
                'fg': fine_use.colors['bg'],
                'hover_bg': fine_use.colors['bg'],
                'hover_fg': fine_use.colors['warning']
            }
        elif variant == "error":
            return {
                'bg': fine_use.colors['error'],
                'fg': fine_use.colors['bg'],
                'hover_bg': fine_use.colors['bg'],
                'hover_fg': fine_use.colors['error']
            }
        elif variant == "info":
            return {
                'bg': fine_use.colors['info'],
                'fg': fine_use.colors['bg'],
                'hover_bg': fine_use.colors['bg'],
                'hover_fg': fine_use.colors['info']
            }
        else:  # secondary (default)
            return {
                'bg': fine_use.colors['surface'],
                'fg': fine_use.colors['text'],
                'hover_bg': fine_use.colors['border'],
                'hover_fg': fine_use.colors['text']
            }
    
    def _get_size_padding(self, size: str) -> Dict[str, int]:
        """Get padding for button size"""
        if size == "sm":
            return {'x': get_spacing('sm'), 'y': get_spacing('xs')}
        elif size == "lg":
            return {'x': get_spacing('xl'), 'y': get_spacing('lg')}
        elif size == "xl":
            return {'x': get_spacing('xxl'), 'y': get_spacing('xl')}
        else:  # md (default)
            return {'x': get_spacing('lg'), 'y': get_spacing('md')}
    
    def _on_enter(self, event):
        """Handle mouse enter (hover)"""
        self.configure(
            bg=self.colors['hover_bg'],
            fg=self.colors['hover_fg']
        )
    
    def _on_leave(self, event):
        """Handle mouse leave"""
        self.configure(
            bg=self.colors['bg'],
            fg=self.colors['fg']
        )
    
    def _on_focus_in(self, event):
        """Handle focus in (accessibility)"""
        self.configure(highlightthickness=3, highlightcolor=fine_use.colors['accent'])
    
    def _on_focus_out(self, event):
        """Handle focus out"""
        self.configure(highlightthickness=0)


class FineUseLabel(tk.Label):
    """
    Fine Use styled label with typography hierarchy
    """
    
    def __init__(
        self,
        parent,
        text: str = "",
        level: str = "body",  # h1, h2, h3, body, caption
        color: str = "text",
        **kwargs
    ):
        # Get font based on level
        font_tuple = self._get_level_font(level)
        
        # Get color
        text_color = fine_use.colors.get(color, fine_use.colors['text'])
        
        super().__init__(
            parent,
            text=text.upper() if level.startswith('h') else text,
            font=font_tuple,
            fg=text_color,
            bg=fine_use.colors['bg'],
            **kwargs
        )
    
    def _get_level_font(self, level: str):
        """Get font configuration for text level"""
        level_map = {
            'h1': ('4xl', 'bold'),
            'h2': ('2xl', 'bold'), 
            'h3': ('xl', 'bold'),
            'body': ('md', 'normal'),
            'caption': ('sm', 'normal'),
            'small': ('xs', 'normal')
        }
        size, weight = level_map.get(level, ('md', 'normal'))
        return get_font(size, weight)


class FineUseFrame(tk.Frame):
    """
    Fine Use styled frame with component styling
    """
    
    def __init__(
        self,
        parent,
        padding: str = "lg",
        **kwargs
    ):
        pad = get_spacing(padding)
        
        super().__init__(
            parent,
            bg=fine_use.colors['surface'],
            relief='solid',
            bd=get_border_width('thin'),
            highlightcolor=fine_use.colors['border'],
            padx=pad,
            pady=pad,
            **kwargs
        )


class FineUseEntry(tk.Entry):
    """
    Fine Use styled text input
    """
    
    def __init__(
        self,
        parent,
        placeholder: str = "",
        size: str = "md",
        **kwargs
    ):
        font_tuple = get_font(size, 'medium')
        pad = get_spacing('md')
        
        super().__init__(
            parent,
            font=font_tuple,
            bg=fine_use.colors['surface'],
            fg=fine_use.colors['text'],
            insertbackground=fine_use.colors['accent'],
            relief='solid',
            bd=get_border_width('thin'),
            highlightcolor=fine_use.colors['accent'],
            highlightthickness=0,
            **kwargs
        )
        
        # Add placeholder functionality
        if placeholder:
            self.placeholder = placeholder
            self.placeholder_active = True
            self.insert(0, placeholder)
            self.configure(fg=fine_use.colors['comment'])
            
            self.bind('<FocusIn>', self._on_focus_in)
            self.bind('<FocusOut>', self._on_focus_out)
    
    def _on_focus_in(self, event):
        """Handle focus in - remove placeholder"""
        if self.placeholder_active:
            self.delete(0, tk.END)
            self.configure(fg=fine_use.colors['text'])
            self.placeholder_active = False
        
        self.configure(highlightthickness=3)
    
    def _on_focus_out(self, event):
        """Handle focus out - restore placeholder if empty"""
        if not self.get() and hasattr(self, 'placeholder'):
            self.insert(0, self.placeholder)
            self.configure(fg=fine_use.colors['comment'])
            self.placeholder_active = True
        
        self.configure(highlightthickness=0)


class FineUseButtonGrid:
    """
    Fine Use button grid system with perfect alignment
    Implements the exact grid layouts from the web version
    """
    
    def __init__(
        self,
        parent,
        layout: str = "2x2",  # 2x2, 1x4, halves, thirds
        gap: str = "md"
    ):
        self.parent = parent
        self.layout = layout
        self.gap = get_spacing(gap)
        self.buttons = []
        
        # Create grid frame
        self.grid_frame = FineUseFrame(parent, padding="lg")
        self.grid_frame.pack(fill='x', pady=get_spacing('md'))
        
        # Configure grid
        self._configure_grid()
    
    def _configure_grid(self):
        """Configure grid layout"""
        if self.layout == "2x2":
            self.rows, self.cols = 2, 2
        elif self.layout == "1x4":
            self.rows, self.cols = 4, 1
        elif self.layout == "halves":
            self.rows, self.cols = 1, 2
        elif self.layout == "thirds":
            self.rows, self.cols = 1, 3
        else:
            self.rows, self.cols = 2, 2
        
        # Configure grid weights for equal sizing
        for i in range(self.rows):
            self.grid_frame.grid_rowconfigure(i, weight=1)
        for j in range(self.cols):
            self.grid_frame.grid_columnconfigure(j, weight=1)
    
    def add_button(
        self, 
        text: str, 
        command: Optional[Callable] = None,
        variant: str = "secondary",
        **kwargs
    ) -> FineUseButton:
        """Add button to grid with automatic positioning"""
        row = len(self.buttons) // self.cols
        col = len(self.buttons) % self.cols
        
        button = FineUseButton(
            self.grid_frame,
            text=text,
            command=command,
            variant=variant,
            **kwargs
        )
        
        button.grid(
            row=row, 
            column=col, 
            sticky='nsew',
            padx=self.gap//2, 
            pady=self.gap//2
        )
        
        self.buttons.append(button)
        return button


# Example application demonstrating Fine Use components
def create_demo_app():
    """Create a demo application showing Fine Use components"""
    app = FineUseApp(title="Fine Use Tkinter Demo", theme="github-dark")
    
    # Header
    header = FineUseLabel(app.main_frame, "FINE USE TKINTER DEMO", level="h1")
    header.pack(pady=get_spacing('xl'))
    
    # Subtitle
    subtitle = FineUseLabel(
        app.main_frame, 
        "Complete design system implementation for Python Tkinter",
        level="body",
        color="comment"
    )
    subtitle.pack(pady=get_spacing('md'))
    
    # Create component frame
    component_frame = FineUseFrame(app.main_frame)
    component_frame.pack(fill='x', pady=get_spacing('lg'))
    
    # Section header
    section_label = FineUseLabel(component_frame, "BUTTON VARIANTS", level="h3")
    section_label.pack(pady=get_spacing('md'))
    
    # Button grid
    button_grid = FineUseButtonGrid(component_frame, layout="2x2")
    button_grid.add_button("PRIMARY ACTION", variant="primary")
    button_grid.add_button("SUCCESS ACTION", variant="success") 
    button_grid.add_button("WARNING ACTION", variant="warning")
    button_grid.add_button("DANGER ACTION", variant="error")
    
    # Text input section
    input_frame = FineUseFrame(app.main_frame)
    input_frame.pack(fill='x', pady=get_spacing('lg'))
    
    input_label = FineUseLabel(input_frame, "TEXT INPUT", level="h3")
    input_label.pack(pady=get_spacing('md'))
    
    text_input = FineUseEntry(input_frame, placeholder="Enter server name...")
    text_input.pack(fill='x', pady=get_spacing('md'))
    
    return app


if __name__ == "__main__":
    # Run the demo
    demo = create_demo_app()
    demo.run()
