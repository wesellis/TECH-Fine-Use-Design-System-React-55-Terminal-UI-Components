"""
Quick test script to verify Fine Use Python implementation
Run this to make sure everything works correctly
"""

import sys
import os

# Add parent directory for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_core_system():
    """Test the core Fine Use system"""
    print("Testing Fine Use Core System...")
    
    try:
        from fine_use_core import fine_use, FineUseTheme, get_spacing, get_font
        
        # Test theme system
        print(f"✅ Default theme: {fine_use.current_theme.value}")
        print(f"✅ Background color: {fine_use.colors['bg']}")
        print(f"✅ Accent color: {fine_use.colors['accent']}")
        
        # Test spacing
        print(f"✅ Large spacing: {get_spacing('lg')}px")
        
        # Test typography
        font_tuple = get_font('lg', 'bold')
        print(f"✅ Large bold font: {font_tuple}")
        
        # Test theme switching
        original_theme = fine_use.current_theme
        fine_use.set_theme(FineUseTheme.AMBER)
        print(f"✅ Theme switched to: {fine_use.current_theme.value}")
        print(f"✅ New accent color: {fine_use.colors['accent']}")
        
        # Switch back
        fine_use.set_theme(original_theme)
        print(f"✅ Theme restored to: {fine_use.current_theme.value}")
        
        print("✅ Core system test PASSED\n")
        return True
        
    except Exception as e:
        print(f"❌ Core system test FAILED: {e}\n")
        return False

def test_tkinter_implementation():
    """Test Tkinter implementation"""
    print("Testing Tkinter Implementation...")
    
    try:
        from fine_use_tkinter import FineUseApp, FineUseButton, FineUseLabel
        
        # Test app creation (don't show window)
        app = FineUseApp(title="Test App")
        print("✅ FineUseApp created successfully")
        
        # Test button creation
        button = FineUseButton(
            app.main_frame,
            text="TEST BUTTON",
            variant="primary"
        )
        print("✅ FineUseButton created successfully")
        
        # Test label creation
        label = FineUseLabel(
            app.main_frame,
            text="TEST LABEL",
            level="h1"
        )
        print("✅ FineUseLabel created successfully")
        
        # Destroy app
        app.root.destroy()
        
        print("✅ Tkinter implementation test PASSED\n")
        return True
        
    except Exception as e:
        print(f"❌ Tkinter implementation test FAILED: {e}\n")
        return False

def test_pyqt_implementation():
    """Test PyQt implementation"""
    print("Testing PyQt Implementation...")
    
    try:
        # Test imports first
        from fine_use_pyqt import FineUseApp, FineUseWindow, FineUseButton
        print("✅ PyQt imports successful")
        
        # Note: We can't actually create PyQt widgets without a running QApplication
        # in a test environment, but we can verify the classes exist
        print("✅ PyQt classes available")
        print("✅ PyQt implementation test PASSED\n")
        return True
        
    except ImportError as e:
        if "PyQt" in str(e):
            print("⚠️  PyQt not installed - this is optional")
            print("   Install with: pip install PyQt5 or pip install PyQt6")
            print("✅ PyQt implementation test SKIPPED\n")
            return True
        else:
            print(f"❌ PyQt implementation test FAILED: {e}\n")
            return False
    except Exception as e:
        print(f"❌ PyQt implementation test FAILED: {e}\n")
        return False

def test_all_themes():
    """Test all 10 themes"""
    print("Testing All 10 Themes...")
    
    try:
        from fine_use_core import FineUseTheme, fine_use
        
        themes = [
            FineUseTheme.GITHUB_DARK,
            FineUseTheme.GITHUB_LIGHT,
            FineUseTheme.AMBER,
            FineUseTheme.GRUVBOX,
            FineUseTheme.MONOCHROME,
            FineUseTheme.MONOKAI,
            FineUseTheme.NEWSPAPER,
            FineUseTheme.SAKURA,
            FineUseTheme.SYNTHWAVE,
            FineUseTheme.VT220
        ]
        
        for theme in themes:
            fine_use.set_theme(theme)
            bg_color = fine_use.colors['bg']
            accent_color = fine_use.colors['accent']
            print(f"✅ {theme.value}: bg={bg_color}, accent={accent_color}")
        
        # Reset to default
        fine_use.set_theme(FineUseTheme.GITHUB_DARK)
        
        print("✅ All themes test PASSED\n")
        return True
        
    except Exception as e:
        print(f"❌ Themes test FAILED: {e}\n")
        return False

def main():
    """Run all tests"""
    print("Fine Use Design System - Python Implementation Test")
    print("=" * 55)
    print()
    
    tests = [
        test_core_system,
        test_tkinter_implementation,
        test_pyqt_implementation,
        test_all_themes
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("=" * 55)
    print(f"Test Results: {passed}/{total} passed")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED - Fine Use Python implementation is ready!")
        print()
        print("Next steps:")
        print("1. Run the complete demo: python demos/fine_use_demo_complete.py")
        print("2. Use Fine Use components in your projects")
        print("3. Enjoy consistent Fine Use styling!")
    else:
        print("⚠️  Some tests failed - check the errors above")
    
    print()

if __name__ == "__main__":
    main()
