#!/usr/bin/env python3
"""
Installation Verification Script for NetBox Interface View Plugin

This script checks if the plugin is properly structured and can be imported.
"""

import os
import sys
from pathlib import Path


def check_file_exists(filepath, description):
    """Check if a file exists"""
    if os.path.exists(filepath):
        print(f"✓ {description}: {filepath}")
        return True
    else:
        print(f"✗ {description} missing: {filepath}")
        return False


def main():
    print("NetBox Interface View Plugin - Installation Verification")
    print("=" * 60)
    
    base_dir = Path(__file__).parent
    plugin_dir = base_dir / 'netbox_interface_view'
    
    checks = []
    
    # Check core Python files
    print("\n1. Checking core Python files...")
    checks.append(check_file_exists(plugin_dir / '__init__.py', 'Plugin config'))
    checks.append(check_file_exists(plugin_dir / 'views.py', 'Views'))
    checks.append(check_file_exists(plugin_dir / 'urls.py', 'URLs'))
    checks.append(check_file_exists(plugin_dir / 'template_content.py', 'Template extension'))
    
    # Check templates
    print("\n2. Checking templates...")
    template_dir = plugin_dir / 'templates' / 'netbox_interface_view'
    checks.append(check_file_exists(template_dir / 'interface_grid.html', 'Grid template'))
    
    # Check template content
    print("\n3. Checking template content...")
    template_content_dir = plugin_dir / 'template_content'
    checks.append(check_file_exists(template_content_dir / 'device.html', 'Device template content'))
    
    # Check documentation
    print("\n4. Checking documentation...")
    checks.append(check_file_exists(base_dir / 'README.md', 'README'))
    checks.append(check_file_exists(base_dir / 'CUSTOM_FIELDS_SETUP.md', 'Custom fields setup guide'))
    checks.append(check_file_exists(base_dir / 'EXAMPLES.md', 'Examples guide'))
    
    # Check packaging files
    print("\n5. Checking packaging files...")
    checks.append(check_file_exists(base_dir / 'setup.py', 'Setup script'))
    checks.append(check_file_exists(base_dir / 'MANIFEST.in', 'Manifest'))
    
    # Try to import the plugin config
    print("\n6. Checking plugin importability...")
    try:
        sys.path.insert(0, str(base_dir))
        from netbox_interface_view import NetBoxInterfaceViewConfig
        print(f"✓ Plugin config imported successfully")
        print(f"  - Name: {NetBoxInterfaceViewConfig.name}")
        print(f"  - Version: {NetBoxInterfaceViewConfig.version}")
        print(f"  - Base URL: {NetBoxInterfaceViewConfig.base_url}")
        checks.append(True)
    except ImportError as e:
        if 'extras' in str(e) or 'django' in str(e):
            print(f"⚠ Skipping import test (NetBox dependencies not available)")
            print(f"  This is expected when running outside of NetBox environment")
            checks.append(True)  # Consider this OK
        else:
            print(f"✗ Failed to import plugin config: {e}")
            checks.append(False)
    except Exception as e:
        print(f"✗ Failed to import plugin config: {e}")
        checks.append(False)
    
    # Summary
    print("\n" + "=" * 60)
    passed = sum(checks)
    total = len(checks)
    
    if passed == total:
        print(f"✓ All checks passed ({passed}/{total})")
        print("\nThe plugin appears to be correctly installed!")
        print("\nNext steps:")
        print("1. Install the plugin: pip install .")
        print("2. Add 'netbox_interface_view' to PLUGINS in NetBox configuration.py")
        print("3. Run migrations: python manage.py migrate")
        print("4. Restart NetBox services")
        print("5. Set up custom fields (see CUSTOM_FIELDS_SETUP.md)")
        return 0
    else:
        print(f"✗ Some checks failed ({passed}/{total})")
        print("\nPlease review the errors above.")
        return 1


if __name__ == '__main__':
    sys.exit(main())
