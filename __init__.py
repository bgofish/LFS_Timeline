from .panels.training_render import setup_spreadsheet_data, KeyframeSpreadsheetPanel
from .operators.start import StartEditorOperator

def register(context):
    setup_spreadsheet_data(context)
    
    # Force registration as a panel specifically
    if hasattr(context.registry, 'register_panel'):
        context.registry.register_panel(KeyframeSpreadsheetPanel)
    else:
        context.registry.register_class(KeyframeSpreadsheetPanel)
        
    context.registry.register_class(StartEditorOperator)
    print("Forcing Spreadsheet Panel Registration...")

def initialize(context):
    register(context)
