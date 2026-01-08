# -*- coding: utf-8 -*-
import globalPluginHandler
import ui
import scriptHandler
import gui
import wx
import webbrowser
import addonHandler

addonHandler.initTranslation()

class GoogleSearchDialog(wx.Dialog):
    def __init__(self):
        # Başlık ve butonlar tamamen İngilizce
        super().__init__(gui.mainFrame, title=_("Google Quick Search v5.0"), size=(450, 200))
        panel = wx.Panel(self)
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(panel, label=_("Search query:"))
        self.edit = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
        self.edit.Bind(wx.EVT_TEXT_ENTER, self.onSearch)
        mainSizer.Add(label, 0, wx.ALL, 10)
        mainSizer.Add(self.edit, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.okBtn = wx.Button(panel, wx.ID_OK, label=_("Search"))
        self.cancelBtn = wx.Button(panel, wx.ID_CANCEL, label=_("Close"))
        self.donateBtn = wx.Button(panel, label=_("Donate"))
        
        btnSizer.Add(self.okBtn, 0, wx.ALL, 5)
        btnSizer.Add(self.cancelBtn, 0, wx.ALL, 5)
        btnSizer.Add(self.donateBtn, 0, wx.ALL, 5)
        mainSizer.Add(btnSizer, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        panel.SetSizer(mainSizer)
        
        self.okBtn.Bind(wx.EVT_BUTTON, self.onSearch)
        self.donateBtn.Bind(wx.EVT_BUTTON, self.onDonate)
        self.CenterOnScreen()
        self.edit.SetFocus()

    def onSearch(self, event):
        query = self.edit.GetValue().strip()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            self.Destroy()

    def onDonate(self, event):
        webbrowser.open("https://www.paytr.com/link/N2IAQKm")

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    @scriptHandler.script(description=_("Google Search"), category=_("Google Search"))
    def script_openSearch(self, gesture): # camelCase yapıldı
        wx.CallAfter(GoogleSearchDialog().ShowModal)