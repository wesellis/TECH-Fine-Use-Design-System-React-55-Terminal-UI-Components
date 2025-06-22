"""
Fine Use Design System - Adaptive Layout Solutions
================================================

This module provides solutions for the common "content cut off" problem
in Python GUIs by implementing adaptive layouts and spacing.
"""

import tkinter as tk
from tkinter import ttk
from typing import Dict, Tuple, Optional
from fine_use_core import fine_use, get_spacing, get_font


class AdaptiveSpacing:
    """
    Adaptive spacing system that compresses based on window size
    Automatically prevents content from being cut off
    """
    
    def __init__(self, window_height: int = 900):
        self.window_height = window_height
        self.compression_factor = self._calculate_compression_factor()
    
    def _calculate_compression_factor(self) -> float:
        """Calculate how much to compress spacing based on window height"""
        if self.window_height >= 1080:
            return 1.0  # Full spacing
        elif self.window_height >= 900:
            return 0.8  # 80% spacing
        elif self.window_height >= 768:
            return 0.6  # 60% spacing
        else:
            return 0.4  # 40% spacing for small screens
    
    def get_adaptive_spacing(self, size: str) -> int:
        """Get compressed spacing value"""
        base_spacing = get_spacing(size)
        return max(2, int(base_spacing * self.compression_factor))
    
    def get_adaptive_font_size(self, size: str) -> int:
        """Get slightly compressed font sizes if needed"""
        from fine_use_core import fine_use
        base_size = fine_use.typography.FONT_SIZES[size]
        
        if self.window_height < 768:
            return max(10, int(base_size * 0.9))  # 10% smaller on small screens
        return base_size


class FineUseScrollableFrame(tk.Frame):
    """
    Scrollable frame that prevents content cut-off
    Automatically adds scrollbars when content exceeds window size
    """
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        
        # Create canvas and scrollbar
        self.canvas = tk.Canvas(
            self,
            bg=fine_use.colors['bg'],
            highlightthickness=0
        )
        
        self.scrollbar = tk.Scrollbar(
            self,
            orient="vertical",
            command=self.canvas.yview,
            bg=fine_use.colors['border'],
            troughcolor=fine_use.colors['surface'],
            activebackground=fine_use.colors['accent']
        )
        
        self.scrollable_frame = tk.Frame(
            self.canvas,
            bg=fine_use.colors['bg']
        )
        
        # Configure scrolling
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        # Pack elements
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Bind mousewheel
        self.bind_mousewheel()
    
    def bind_mousewheel(self):
        """Bind mousewheel to canvas"""
        def _on_mousewheel(event):
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        self.canvas.bind("<MouseWheel>", _on_mousewheel)  # Windows
        self.canvas.bind("<Button-4>", lambda e: self.canvas.yview_scroll(-1, "units"))  # Linux
        self.canvas.bind("<Button-5>", lambda e: self.canvas.yview_scroll(1, "units"))   # Linux


class AdaptiveFineUseApp:
    """
    Adaptive Fine Use application that prevents content cut-off
    Automatically adjusts spacing and adds scrolling as needed
    """
    
    def __init__(
        self, 
        title: str = "Fine Use Application",
        theme: str = "github-dark",
        width: int = 1400,
        height: int = 900,
        min_height: int = 600,
        adaptive_spacing: bool = True,
        enable_scrolling: bool = True
    ):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.minsize(width=800, height=min_height)
        
        # Set theme
        if hasattr(fine_use, 'set_theme'):
            from fine_use_core import FineUseTheme
            theme_enum = getattr(FineUseTheme, theme.upper().replace('-', '_'))
            fine_use.set_theme(theme_enum)
        
        # Configure adaptive spacing
        self.adaptive_spacing_enabled = adaptive_spacing
        self.adaptive = AdaptiveSpacing(height) if adaptive_spacing else None
        
        # Configure root
        self.root.configure(bg=fine_use.colors['bg'])
        
        # Create main container
        if enable_scrolling:
            # Use scrollable frame
            self.scrollable_container = FineUseScrollableFrame(self.root)
            self.scrollable_container.pack(fill='both', expand=True)
            self.main_frame = self.scrollable_container.scrollable_frame
        else:
            # Use regular frame
            self.main_frame = tk.Frame(
                self.root,
                bg=fine_use.colors['bg']
            )
            self.main_frame.pack(fill='both', expand=True)
        
        # Add padding to main frame
        padding = self.get_spacing('xl') if adaptive_spacing else get_spacing('xl')
        self.main_frame.configure(padx=padding, pady=padding)
        
        # Configure fonts
        self._configure_fonts()
    
    def get_spacing(self, size: str) -> int:
        """Get spacing value (adaptive or normal)"""
        if self.adaptive_spacing_enabled and self.adaptive:
            return self.adaptive.get_adaptive_spacing(size)
        return get_spacing(size)
    
    def get_font(self, size: str, weight: str = 'normal') -> Tuple[str, int, str]:
        """Get font tuple (adaptive or normal)"""
        if self.adaptive_spacing_enabled and self.adaptive:
            font_size = self.adaptive.get_adaptive_font_size(size)
            return (
                fine_use.typography.FONT_FAMILY,
                font_size,
                'bold' if weight in ['semibold', 'bold'] else 'normal'
            )
        return get_font(size, weight)
    
    def _configure_fonts(self):
        """Configure default fonts"""
        try:
            from tkinter import font
            default_font = font.nametofont("TkDefaultFont")
            font_tuple = self.get_font('md')
            default_font.configure(family=font_tuple[0], size=font_tuple[1])
        except:
            pass
    
    def run(self):
        """Start the application"""
        self.root.mainloop()


class CompactFineUseButton(tk.Button):
    """
    Compact Fine Use button with adaptive sizing
    Automatically reduces padding on small screens
    """
    
    def __init__(
        self,
        parent,
        text: str = "",
        variant: str = "secondary",
        size: str = "md",
        adaptive_app: Optional[AdaptiveFineUseApp] = None,
        command: Optional[callable] = None,
        **kwargs
    ):
        # Get colors based on variant
        colors = self._get_variant_colors(variant)
        
        # Get font and padding (adaptive if app provided)
        if adaptive_app:
            font_tuple = adaptive_app.get_font(size, 'bold')
            padding = self._get_adaptive_padding(size, adaptive_app)
        else:
            font_tuple = get_font(size, 'bold')
            padding = self._get_size_padding(size)
        
        super().__init__(
            parent,
            text=text.upper(),
            command=command,
            font=font_tuple,
            bg=colors['bg'],
            fg=colors['fg'],
            activebackground=colors['hover_bg'],
            activeforeground=colors['hover_fg'],
            relief='solid',
            bd=2,  # Always use thin border
            highlightthickness=0,
            padx=padding['x'],
            pady=padding['y'],
            cursor='hand2',
            **kwargs
        )
        
        # Store colors for hover effects
        self.colors = colors
        
        # Bind hover events
        self.bind('<Enter>', self._on_enter)
        self.bind('<Leave>', self._on_leave)
    
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
        else:  # secondary
            return {
                'bg': fine_use.colors['surface'],
                'fg': fine_use.colors['text'],
                'hover_bg': fine_use.colors['border'],
                'hover_fg': fine_use.colors['text']
            }
    
    def _get_adaptive_padding(self, size: str, app: AdaptiveFineUseApp) -> Dict[str, int]:
        """Get adaptive padding based on app settings"""
        if size == "sm":
            return {'x': app.get_spacing('xs'), 'y': app.get_spacing('xs')}
        elif size == "lg":
            return {'x': app.get_spacing('lg'), 'y': app.get_spacing('md')}
        else:  # md
            return {'x': app.get_spacing('md'), 'y': app.get_spacing('sm')}
    
    def _get_size_padding(self, size: str) -> Dict[str, int]:
        """Get standard padding"""
        if size == "sm":
            return {'x': get_spacing('xs'), 'y': get_spacing('xs')}
        elif size == "lg":
            return {'x': get_spacing('lg'), 'y': get_spacing('md')}
        else:  # md
            return {'x': get_spacing('md'), 'y': get_spacing('sm')}
    
    def _on_enter(self, event):
        """Handle hover enter"""
        self.configure(bg=self.colors['hover_bg'], fg=self.colors['hover_fg'])
    
    def _on_leave(self, event):
        """Handle hover leave"""
        self.configure(bg=self.colors['bg'], fg=self.colors['fg'])


class CompactButtonGrid:
    """
    Compact button grid with adaptive spacing
    Prevents buttons from being cut off
    """
    
    def __init__(
        self,
        parent,
        layout: str = "2x2",
        adaptive_app: Optional[AdaptiveFineUseApp] = None
    ):
        self.parent = parent
        self.layout = layout
        self.adaptive_app = adaptive_app
        self.buttons = []
        
        # Get adaptive gap
        gap = adaptive_app.get_spacing('sm') if adaptive_app else get_spacing('sm')
        
        # Create grid frame with adaptive padding
        padding = adaptive_app.get_spacing('md') if adaptive_app else get_spacing('md')
        
        self.grid_frame = tk.Frame(
            parent,
            bg=fine_use.colors['surface'],
            relief='solid',
            bd=2,
            padx=padding,
            pady=padding
        )
        self.grid_frame.pack(fill='x', pady=gap)
        
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
        
        # Configure weights
        for i in range(self.rows):
            self.grid_frame.grid_rowconfigure(i, weight=1)
        for j in range(self.cols):
            self.grid_frame.grid_columnconfigure(j, weight=1)
    
    def add_button(
        self,
        text: str,
        command: Optional[callable] = None,
        variant: str = "secondary",
        **kwargs
    ) -> CompactFineUseButton:
        """Add button to grid"""
        row = len(self.buttons) // self.cols
        col = len(self.buttons) % self.cols
        
        # Get adaptive gap
        gap = self.adaptive_app.get_spacing('xs') if self.adaptive_app else 2
        
        button = CompactFineUseButton(
            self.grid_frame,
            text=text,
            command=command,
            variant=variant,
            adaptive_app=self.adaptive_app,
            **kwargs
        )
        
        button.grid(
            row=row,
            column=col,
            sticky='nsew',
            padx=gap,
            pady=gap
        )
        
        self.buttons.append(button)
        return button


# Utility functions for adaptive layouts
def create_adaptive_app(
    title: str,
    width: int = 1400,
    height: int = 900,
    enable_scrolling: bool = True
) -> AdaptiveFineUseApp:
    """Create an adaptive Fine Use app that prevents cut-off"""
    return AdaptiveFineUseApp(
        title=title,
        width=width,
        height=height,
        adaptive_spacing=True,
        enable_scrolling=enable_scrolling
    )


def calculate_required_height(num_sections: int, buttons_per_section: int = 4) -> int:
    """Calculate minimum required height for given content"""
    base_height = 200  # Header and padding
    section_height = 180  # Per section
    button_height = 120  # Per button group
    
    return base_height + (num_sections * section_height) + (num_sections * button_height)


if __name__ == "__main__":
    # Example of adaptive app
    app = create_adaptive_app("Adaptive Fine Use Demo", height=700)
    
    # This content will automatically adapt and scroll if needed
    from fine_use_tkinter import FineUseLabel
    
    title = FineUseLabel(app.main_frame, "ADAPTIVE LAYOUT DEMO", level="h1")
    title.pack(pady=app.get_spacing('lg'))
    
    # Multiple button grids that will compress on small screens
    for i in range(3):
        grid = CompactButtonGrid(app.main_frame, layout="2x2", adaptive_app=app)
        grid.add_button(f"BUTTON {i*4+1}", variant="primary")
        grid.add_button(f"BUTTON {i*4+2}", variant="success")
        grid.add_button(f"BUTTON {i*4+3}", variant="warning")
        grid.add_button(f"BUTTON {i*4+4}", variant="error")
    
    app.run()
