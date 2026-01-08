# -*- coding: utf-8 -*-
import globalPluginHandler
import ui
import gui
import wx
import webbrowser
from scriptHandler import script
import addonHandler

# Initialize translation
addonHandler.initTranslation()

class AddressDialog(wx.Dialog):
	def __init__(self, parent):
		super().__init__(parent, title=_("Address Bar"), style=wx.DEFAULT_DIALOG_STYLE)
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		
		# Label and Input Box
		label = wx.StaticText(self, label=_("Address:"))
		self.textCtrl = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
		
		# Buttons Sizer
		btnSizer = wx.BoxSizer(wx.HORIZONTAL)
		okBtn = wx.Button(self, wx.ID_OK, label=_("OK"))
		cancelBtn = wx.Button(self, wx.ID_CANCEL, label=_("Cancel"))
		donateBtn = wx.Button(self, label=_("Donate"))
		
		donateBtn.Bind(wx.EVT_BUTTON, self.onDonate)
		
		btnSizer.Add(okBtn)
		btnSizer.Add(cancelBtn, flag=wx.LEFT, border=5)
		btnSizer.Add(donateBtn, flag=wx.LEFT, border=5)
		
		mainSizer.Add(label, flag=wx.ALL, border=10)
		mainSizer.Add(self.textCtrl, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)
		mainSizer.Add(btnSizer, flag=wx.ALIGN_CENTER|wx.ALL, border=10)
		
		self.SetSizer(mainSizer)
		mainSizer.Fit(self)
		self.textCtrl.SetFocus()

	def onDonate(self, event):
		webbrowser.open("https://www.paytr.com/link/N2IAQKm")

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	@script(
		description=_("Address Bar"),
		category=_("Address Bar")
	)
	def script_openAddressInput(self, gesture): # camelCase
		# Using wx.CallAfter to prevent freeze issues
		wx.CallAfter(self.showDialog)

	def showDialog(self): # camelCase
		with AddressDialog(gui.mainFrame) as dlg:
			if dlg.ShowModal() == wx.ID_OK:
				url = dlg.textCtrl.GetValue().strip()
				if url:
					if not url.startswith(("http://", "https://")):
						url = "https://" + url
					webbrowser.open(url)