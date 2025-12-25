# -*- coding: utf-8 -*-
import globalPluginHandler
import ui
import scriptHandler
import gui
import wx
import webbrowser
import speech

class GoogleAramaPenceresi(wx.Dialog):
	def __init__(self):
		# NVDA'nın ana çerçevesi üzerinden başlığı güncelledik
		super(GoogleAramaPenceresi, self).__init__(gui.mainFrame, title="Google Search v2.0 - Volkan Özdemir Yazılım", size=(450, 200))
		
		panel = wx.Panel(self)
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		
		label = wx.StaticText(panel, label="Aranacak kelime / Search query:")
		self.edit = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
		self.edit.Bind(wx.EVT_TEXT_ENTER, self.onSearch)
		
		mainSizer.Add(label, 0, wx.ALL, 10)
		mainSizer.Add(self.edit, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
		
		# Butonlar
		btnSizer = wx.BoxSizer(wx.HORIZONTAL)
		self.okBtn = wx.Button(panel, wx.ID_OK, label="Ara / Search")
		self.cancelBtn = wx.Button(panel, wx.ID_CANCEL, label="Kapat / Close")
		self.donateBtn = wx.Button(panel, label="Bağış Yap / Donate")
		
		btnSizer.Add(self.okBtn, 0, wx.ALL, 5)
		btnSizer.Add(self.cancelBtn, 0, wx.ALL, 5)
		btnSizer.Add(self.donateBtn, 0, wx.ALL, 5)
		
		mainSizer.Add(btnSizer, 0, wx.ALIGN_CENTER | wx.ALL, 10)
		panel.SetSizer(mainSizer)
		
		self.okBtn.Bind(wx.EVT_BUTTON, self.onSearch)
		self.donateBtn.Bind(wx.EVT_BUTTON, self.onDonate)
		
		self.CenterOnScreen()
		self.edit.SetFocus()

	def onDonate(self, event):
		webbrowser.open("https://www.paytr.com/link/N2IAQKm")

	def onSearch(self, event):
		sorgu = self.edit.GetValue().strip()
		if sorgu:
			speech.speakMessage(f"{sorgu} aranıyor / searching...")
			webbrowser.open(f"https://www.google.com/search?q={sorgu}")
		self.Destroy()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = "Google Hızlı Arama v2.0"
	
	@scriptHandler.script(
		description="Google Search",
		gestures=["kb:NVDA+0"]
	)
	def script_googleArama(self, gesture):
		wx.CallAfter(self.ekrani_goster)

	def ekrani_goster(self):
		dlg = GoogleAramaPenceresi()
		dlg.Show()