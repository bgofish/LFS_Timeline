from .panels.training_render import setup_spreadsheet_data, KeyframeSpreadsheetPanel
from .operators.start import StartEditorOperator

def register(context):
    setup_spreadsheet_data(context)
    
    # register_panel is specifically for sidebar UI elements
    context.registry.register_panel(KeyframeSpreadsheetPanel)
    context.registry.register_operator(StartEditorOperator)
    
    print("Spreadsheet UI Registered")

def initialize(context):
    register(context)
