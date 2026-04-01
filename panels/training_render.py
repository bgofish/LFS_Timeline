class KeyframeSpreadsheetPanel:
    id = "TIMELINE_PT_spreadsheet"
    label = "Keyframe Spreadsheet"
    # This category determines which sidebar the tab appears in
    category = "LichtFeld" 
    panel_path = "training_render.rml" 

    def draw(self, context):
        # The Studio uses the .rml file for the actual UI
        pass
