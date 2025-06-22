#!/usr/bin/env python3
"""
Fine Use Design System - Run Script
Handles PySide6 compatibility and launches the demo
"""

import sys
import os

def check_requirements():
    """Check if all requirements are met"""
    print("🔍 Checking Fine Use PySide6 requirements...")
    
    # Check Python version
    if sys.version_info < (3, 7):
        print(f"❌ Python 3.7+ required, found {sys.version}")
        return False
    
    print(f"✅ Python {sys.version.split()[0]}")
    
    # Check PySide6
    try:
        import PySide6
        print(f"✅ PySide6 {PySide6.__version__}")
    except ImportError:
        print("❌ PySide6 not found")
        print("Install with: pip install PySide6")
        return False
    
    # Check specific PySide6 modules
    try:
        from PySide6.QtWidgets import QApplication
        from PySide6.QtCore import Qt
        from PySide6.QtGui import QFont
        print("✅ PySide6 modules available")
    except ImportError as e:
        print(f"❌ PySide6 module import failed: {e}")
        return False
    
    return True

def run_simple_test():
    """Run the simple test"""
    print("🚀 Launching Simple Test...")
    try:
        import simple_test
        return simple_test.main()
    except Exception as e:
        print(f"❌ Simple test failed: {e}")
        return 1

def run_quick_test():
    """Run the quick component test"""
    print("🚀 Launching Quick Test...")
    try:
        import quick_test
        return quick_test.main()
    except Exception as e:
        print(f"❌ Quick test failed: {e}")
        print("Falling back to simple test...")
        return run_simple_test()

def run_full_demo():
    """Run the full demo"""
    print("🚀 Launching Full Demo...")
    try:
        import fine_use_pyside6_demo
        return fine_use_pyside6_demo.main()
    except Exception as e:
        print(f"❌ Full demo failed: {e}")
        print("Falling back to quick test...")
        return run_quick_test()

def main():
    """Main entry point"""
    print("=" * 60)
    print("FINE USE DESIGN SYSTEM - PYSIDE6 LAUNCHER")
    print("=" * 60)
    
    # Check requirements
    if not check_requirements():
        print("❌ Requirements not met. Please install PySide6 and try again.")
        return 1
    
    # Get command line argument
    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()
    else:
        mode = "auto"
    
    print(f"📋 Launch mode: {mode}")
    print("-" * 60)
    
    # Launch based on mode
    if mode == "simple":
        return run_simple_test()
    elif mode == "quick":
        return run_quick_test()
    elif mode == "full":
        return run_full_demo()
    else:
        # Auto mode - try full demo, fallback to simpler versions
        print("🔄 Auto mode - trying full demo first...")
        return run_full_demo()

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n🛑 Interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        sys.exit(1)
