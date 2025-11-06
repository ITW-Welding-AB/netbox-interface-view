# Interface Grid Visualization - Screenshots

## Demo View

![Interface Grid Demo](https://github.com/user-attachments/assets/556a7895-5ee5-4cb6-9846-c66a532e9e5a)

This screenshot demonstrates a 48-port switch configured with a 2×24 grid layout. Key features shown:

### Visual Features

1. **Grid Layout**: 2 rows × 24 columns matching a typical 48-port rack switch
2. **Connection Status Indicators**: Green, gray, and red dots showing connection/enabled status
3. **VLAN Color-Coding**: Border colors indicate untagged VLAN assignments
4. **Tagged VLANs**: Small colored dots within cells represent tagged VLANs
5. **Interface Information**: Each cell shows interface name and type

### Color Scheme Demonstrated

- **Blue (#0066CC)**: Management VLAN (VLAN 10)
- **Green (#00CC66)**: Data VLAN (VLAN 20)
- **Orange (#FF9900)**: Voice VLAN (VLAN 30)
- **Purple (#9966CC)**: Guest VLAN (VLAN 40)
- **Gray (#cccccc)**: No VLAN assigned

### Interactive Features (in actual plugin)

The actual NetBox plugin includes:
- Clickable cells that link to interface detail pages
- Real-time connection status from NetBox database
- Dynamic VLAN color assignment via custom fields
- Interface type filtering
- Hover effects and tooltips
- Responsive layout

## Usage Examples

### Example 1: 48-Port Switch
```
Grid Rows: 2
Grid Columns: 24
Result: Perfect for standard 1U/2U rack switches
```

### Example 2: 24-Port Switch
```
Grid Rows: 3
Grid Columns: 8
Result: Compact view for smaller switches
```

### Example 3: 96-Port Switch
```
Grid Rows: 4
Grid Columns: 24
Result: High-density visualization
```

## Benefits

1. **At-a-Glance Status**: Quickly see which ports are connected and their VLAN assignments
2. **Physical Layout Representation**: Grid matches actual port arrangement on devices
3. **Color-Coded VLANs**: Instantly identify VLAN assignments across all ports
4. **Filtering Capability**: Hide virtual/logical interfaces to focus on physical ports
5. **Easy Navigation**: Click any port to view full interface details

## Configuration Requirements

To achieve this visualization:
1. Set `grid_rows` custom field on the device (e.g., 2)
2. Set `grid_columns` custom field on the device (e.g., 24)
3. Set `color` custom field on VLANs (hex color codes)
4. Assign VLANs to interfaces (tagged and/or untagged)
5. Click "View Interface Grid" button on device page

See [CUSTOM_FIELDS_SETUP.md](CUSTOM_FIELDS_SETUP.md) for detailed setup instructions.
