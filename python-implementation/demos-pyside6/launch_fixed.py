#!/usr/bin/env python3
"""
Fine Use Design System - FIXED Launcher
Launches the corrected version that should look exactly like HTML demos
"""

import sys
import os

def main():
    """Launch the fixed Fine Use demo"""
    print("=" * 60)
    print("🔧 FINE USE PYSIDE6 - VISUAL FIXES APPLIED")
    print("=" * 60)
    print()
    print("🎯 This version focuses on:")
    print("   ✅ Exact color matching with HTML demos")
    print("   ✅ Perfect button styling (no blue primary)")
    print("   ✅ Correct progress bar colors")
    print("   ✅ Proper spacing and typography")
    print("   ✅ Dark terminal backgrounds")
    print("   ✅ Sharp rectangular borders")
    print()
    print("🚀 Launching FIXED demo...")
    print("-" * 60)
    
    try:
        # Import and run the fixed demo
        import fixed_demo
        return fixed_demo.main()
        
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        print("Make sure you're in the correct directory")
        return 1
        
    except Exception as e:
        print(f"❌ Launch failed: {e}")
        print("Check that PySide6 is installed: pip install PySide6")
        return 1

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n🛑 Stopped by user")
        sys.exit(0)
