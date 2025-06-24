import sys
from qgis.core import (
    QgsField,
    QgsProject,
    QgsVectorLayer,
    edit
)
from PyQt5.QtCore import QVariant

# Layer must be selected
layer = iface.activeLayer()

# Check layer is editable
if not layer.isEditable():
    layer.startEditing()

# Fields to skip during numeric conversion
excluded_fields = [
    "svi_STATE",
    "svi_ST_ABBR",
    "svi_COUNTY",
    "svi_LOCATION"
]

# Track converted fields
conversion_log = []

# Remove?
# Prefix used for SVI fields
svi_prefix = "svi_"

# Loop through fields...
for field in layer.fields():
    name = field.name()

    # Skip already-converted fields, excluded fields, and fields not joined from SVI CSV
    if name in excluded_fields or name.endswith('_num') or not name.startswith('svi_'):
        continue

    # Check if already numeric and exclude
    if field.type() in (QVariant.Double, QVariant.Int, QVariant.LongLong):
        continue

    # Create the new field. Avoid dupes.
    new_field_label = f"{name}_num"
    if new_field_label in layer.fields().names():
        continue
    
    new_field = QgsField(new_field_label, QVariant.Double)
    layer.addAttribute(new_field)
    layer.updateFields()

    new_field_index = layer.fields().indexOf(new_field_label)
    old_field_index = layer.fields().indexOf(name)

    # Track field value conversions
    conversions = 0

    # Convert the field values
    for feature in layer.getFeatures():
        old_value = feature[name]
        try:
            # # Handle -999 or null-like values
            # if old_value in (None, '', '-999', -999):
            #     new_value = None
            # else:
            #     new_value = float(old_value)
            #     conversions += 1

            new_value = float(old_value)
            conversions += 1

            layer.changeAttributeValue(feature.id(), new_field_label, new_value)
        except Exception as e:
            print(f"Error converting {name}: {e}")

    conversion_log.append(f"{name} -> {new_field_label} ({conversions} converted)")

# Commit changes
layer.commitChanges()

# Print conversion summary
for entry in conversion_log:
    print(entry)

print("String to numeric field conversion complete. Excluded fields skipped.")