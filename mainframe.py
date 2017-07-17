# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.gizmos as gizmos


###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		#self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap,
		# wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_led = gizmos.LEDNumberCtrl(self, -1, wx.DefaultPosition,
										  wx.DefaultSize,
										  gizmos.LED_ALIGN_CENTER)

		# default colours are green on black
		bSizer6.Add( self.m_led, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_spinCtrl1 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer5.Add( self.m_spinCtrl1, 0, wx.ALL, 5 )
		self.m_spinCtrl2 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer5.Add( self.m_spinCtrl2, 0, wx.ALL, 5 )

		bSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.start = wx.Button( self, wx.ID_ANY, u"start", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.start, 0, wx.ALL, 5 )
		
		self.reset = wx.Button( self, wx.ID_ANY, u"reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.reset, 0, wx.ALL, 5 )
		
		
		bSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer17.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_text, 1, wx.ALL, 5 )
		
		self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer18.Add( self.m_filePicker1, 0, wx.ALL, 5 )
		
		
		bSizer17.Add( bSizer18, 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( bSizer17, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer6 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.start.Bind( wx.EVT_LEFT_UP, self.OnStart )
		self.reset.Bind( wx.EVT_LEFT_UP, self.OnReset )
		self.m_filePicker1.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnFileChange )
		self.m_spinCtrl1.Bind(wx.EVT_SPINCTRL, self.OnSpinH)
		self.m_spinCtrl2.Bind(wx.EVT_SPINCTRL, self.OnSpinM)

	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnStart( self, event ):
		event.Skip()
	
	def OnReset( self, event ):
		event.Skip()
	
	def OnFileChange( self, event ):
		event.Skip()
	
	def OnSpinM( self, event ):
		event.Skip()
	
	def OnSpinH(self, event):
		event.Skip()
