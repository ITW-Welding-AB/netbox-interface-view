# Quick Start Guide

## 1. Install the Plugin

```bash
pip install netbox-interface-view
```

Or install from source:
```bash
git clone https://github.com/Tolfx/netbox-plugin-interface-view.git
cd netbox-plugin-interface-view
pip install .
```

## 2. Enable in NetBox

Edit `/opt/netbox/netbox/netbox/configuration.py`:

```python
PLUGINS = [
    'netbox_interface_view',
]

PLUGINS_CONFIG = {
    'netbox_interface_view': {
        # No additional configuration required
    }
}
```

## 3. Restart NetBox

```bash
sudo systemctl restart netbox netbox-rq
```

## 4. Create Custom Fields

Three custom fields are required. You can create them via the UI or use this Django shell script:

```bash
cd /opt/netbox/netbox/
source /opt/netbox/venv/bin/activate
python3 manage.py shell
```

```python
from django.contrib.contenttypes.models import ContentType
from extras.models import CustomField
from dcim.models import Device
from ipam.models import VLAN

# Get content types
device_ct = ContentType.objects.get_for_model(Device)
vlan_ct = ContentType.objects.get_for_model(VLAN)

# Create grid_rows field
grid_rows, created = CustomField.objects.get_or_create(
    name='grid_rows',
    defaults={
        'label': 'Grid Rows',
        'type': 'integer',
        'required': False,
        'default': 2,
        'description': 'Number of rows in the interface grid layout',
        'validation_minimum': 1,
        'validation_maximum': 100
    }
)
grid_rows.content_types.set([device_ct])
print(f"✓ grid_rows field {'created' if created else 'already exists'}")

# Create grid_columns field
grid_columns, created = CustomField.objects.get_or_create(
    name='grid_columns',
    defaults={
        'label': 'Grid Columns',
        'type': 'integer',
        'required': False,
        'default': 24,
        'description': 'Number of columns in the interface grid layout',
        'validation_minimum': 1,
        'validation_maximum': 100
    }
)
grid_columns.content_types.set([device_ct])
print(f"✓ grid_columns field {'created' if created else 'already exists'}")

# Create color field for VLANs
color, created = CustomField.objects.get_or_create(
    name='color',
    defaults={
        'label': 'Color',
        'type': 'text',
        'required': False,
        'default': '#cccccc',
        'description': 'Hex color code for VLAN visualization',
        'validation_regex': '^#[0-9A-Fa-f]{6}$'
    }
)
color.content_types.set([vlan_ct])
print(f"✓ color field {'created' if created else 'already exists'}")

print("\n✓ All custom fields created successfully!")
```

## 5. Configure a Device

1. Navigate to a device in NetBox
2. Click **Edit**
3. Set custom fields:
   - **Grid Rows**: 2 (for a 2-row switch)
   - **Grid Columns**: 24 (for 24 ports per row)
4. Click **Save**

## 6. Configure VLAN Colors (Optional)

1. Navigate to a VLAN
2. Click **Edit**
3. Set custom field:
   - **Color**: `#0066CC` (or any hex color)
4. Click **Save**

## 7. View the Grid

1. Navigate to the device
2. Click the **"View Interface Grid"** button
3. The grid visualization will display all interfaces

## Common Grid Configurations

| Device Type | Ports | Rows | Columns | Example |
|-------------|-------|------|---------|---------|
| 48-port switch | 48 | 2 | 24 | Standard rack switch |
| 24-port switch | 24 | 3 | 8 | Small switch |
| 96-port switch | 96 | 4 | 24 | High-density switch |
| 12-port switch | 12 | 2 | 6 | Edge switch |

## VLAN Color Recommendations

```python
# Common VLAN colors
VLAN_COLORS = {
    'Management': '#0066CC',  # Blue
    'Data': '#00CC66',        # Green
    'Voice': '#FF9900',       # Orange
    'Guest': '#9966CC',       # Purple
    'Server': '#CC0000',      # Red
    'DMZ': '#FFCC00',         # Yellow
    'Storage': '#00CCCC',     # Cyan
}
```

## Troubleshooting

**Problem**: Button doesn't appear on device page

**Solution**: 
- Ensure plugin is in PLUGINS list
- Restart NetBox: `sudo systemctl restart netbox netbox-rq`
- Clear browser cache

---

**Problem**: Grid shows all gray cells

**Solution**: 
- Set VLAN colors using the `color` custom field
- Default is `#cccccc` (light gray)

---

**Problem**: Too many empty cells

**Solution**: 
- Adjust grid_rows and grid_columns to match actual interface count
- Example: 24 interfaces → 3 rows × 8 columns = 24 cells

---

**Problem**: Can't see physical ports

**Solution**: 
- Use the interface type filter
- Exclude: Virtual, LAG, Loopback, Bridge

## Next Steps

- See **CUSTOM_FIELDS_SETUP.md** for detailed custom field instructions
- See **EXAMPLES.md** for usage examples and best practices
- See **README.md** for complete documentation

## Support

For issues or questions:
- GitHub Issues: https://github.com/Tolfx/netbox-plugin-interface-view/issues
