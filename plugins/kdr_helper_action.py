import pcbnew
import os
import wx

class KDRHelperAction(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Kicad Design Rule Helper"
        self.category = "Design Automation"
        self.description = "Helps create design rules between net classes."
        self.show_toolbar_button = True # Optional, defaults to False
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'kdr_helper_dark.png') # Optional

    def Run(self):
        # The entry function of the plugin that is executed on user action
        caption = self.name
        message = "Helps create design rules between net classes!"
        wx.MessageBox(message, caption, wx.OK | wx.ICON_EXCLAMATION)