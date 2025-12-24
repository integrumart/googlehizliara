# -*- coding: utf-8 -*-
import globalPluginHandler
import ui
import scriptHandler
import gui
import wx
import webbrowser

class GoogleAramaPenceresi(wx.Dialog):
    def __init__(self):
        # NVDA'nın ana çerçevesini (parent) belirterek çakışmayı önlüyoruz
        super(GoogleAramaPenceresi, self).__init__(gui.mainFrame, title="Google'da Ara - Volkan Özdemir")
        
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(self, label="Aranacak kelimeyi yazın ve Enter'a basın:")
        self.edit = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        
        self.edit.Bind(wx.EVT_TEXT_ENTER, self.onSearch)
        
        mainSizer.Add(label, 0, wx.ALL, 10)
        mainSizer.Add(self.edit, 0, wx.EXPAND | wx.ALL, 10)
        
        self.SetSizerAndFit(mainSizer)
        self.CenterOnScreen()
        self.edit.SetFocus()

    def onSearch(self, event):
        sorgu = self.edit.GetValue()
        if sorgu:
            webbrowser.open(f"https://www.google.com/search?q={sorgu}")
        self.Destroy() # Close yerine Destroy kullanarak belleği temizliyoruz

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    
    @scriptHandler.script(
        description="Google Hızlı Arama",
        category="Volkan Özdemir Yazılım",
        gestures=["kb:NVDA+0"]
    )
    def script_googleArama(self, gesture):
        # wx.CallAfter kullanarak NVDA'nın konuşma motorunu kilitlemesini engelliyoruz
        wx.CallAfter(self.ekrani_goster)

    def ekrani_goster(self):
        dlg = GoogleAramaPenceresi()
        dlg.Show() # ShowModal yerine Show kullanarak NVDA'nın arka planda çalışmasını sağlıyoruz