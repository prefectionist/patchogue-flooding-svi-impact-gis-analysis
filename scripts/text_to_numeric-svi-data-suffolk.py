import sys
from qgis.core import (
    QgsField,
    QgsExpression,
    QgsExpressionContext,
    QgsExpressionContextUtils,
    edit
)
from PyQt5.QtCore import QVariant


# Get the active layer
layer = iface.activeLayer()
if not layer:
    iface.messageBar().pushMessage("Error", "No active layer selected.", level=Qgis.Critical)
    sys.exit("Le faile.")
else:
    layer_name = layer.name()
    iface.messageBar().pushMessage("Info", f"Running on layer: {layer_name}", level=Qgis.Info)

   
provider = layer.dataProvider()

# Prefix used for SVI fields
svi_prefix = "svi_"

# Fields to skip during numeric conversion
excluded_fields = [
    "svi_STATE",
    "svi_ST_ABBR",
    "svi_COUNTY",
    "svi_LOCATION"
]

# Loop through and create new numeric fields
for field in layer.fields():
    name = field.name()
    if (
        name.startswith(svi_prefix)
        and field.typeName() == 'String'
        and name not in excluded_fields
    ):
        new_name = name + "_num"
        provider.addAttributes([QgsField(new_name, QVariant.Double)])
        layer.updateFields()

# Prepare expression context
context = QgsExpressionContext()
context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(layer))

# Start editing session
layer.startEditing()
try:
    for field in layer.fields():
        name = field.name()
        if (
            name.startswith(svi_prefix)
            and name.endswith("_num")
            and name[:-4] not in excluded_fields  # get original name
        ):
            original_name = name[:-4]
            expr = QgsExpression(f'to_real("{original_name}")')
            for f in layer.getFeatures():
                context.setFeature(f)
                f[name] = expr.evaluate(context)
                layer.updateFeature(f)
finally:
    layer.commitChanges()

print("Numeric conversion complete. Excluded fields skipped.")
