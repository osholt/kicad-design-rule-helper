from .kdr_helper_action import KDRHelperAction # Note the relative import!
KDRHelperAction().register() # Instantiate and register to Pcbnew

# -*- coding: utf-8 -*-
try:
    # Note the relative import!
    from .kdr_helper_action import KDRHelperAction
    # Instantiate and register to Pcbnew
    KDRHelperAction().register()
# if failed, log the error and let the user know
except Exception as e:
    # log the error
    import os
    plugin_dir = os.path.dirname(os.path.realpath(__file__))
    log_file = os.path.join(plugin_dir, 'kdr_helper_error.log')
    with open(log_file, 'w') as f:
        f.write(repr(e))
    # register dummy plugin, to let the user know of the problems
    import pcbnew
    import wx

    class KDRHelper(pcbnew.ActionPlugin):
        """
        Notify user of error when initializing the plugin
        """
        def defaults(self):
            self.name = "KiCad Design Rule Helper"
            self.category = "Design Automation"
            self.description = "Helps create design rules between net classes."

        def Run(self):
            caption = self.name
            message = "There was an error while loading plugin \n" \
                      "Please take a look in the plugin folder for kdr_helper_error.log\n" \
                      "You can raise an issue on GitHub page.\n" \
                      "Please attach the .log file"
            wx.MessageBox(message, caption, wx.OK | wx.ICON_ERROR)

    KDRHelper().register()