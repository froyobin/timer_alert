import wx
import mainframe
import thread
import time
from gi.repository import Notify


class MsgEvent(wx.PyCommandEvent):
    """Event to signal that a count value is ready"""
    def __init__(self, etype, eid):
        """Creates the event object"""
        wx.PyCommandEvent.__init__(self, etype, eid)



class MyMainFrame(mainframe.MainFrame):
    def __init__(self):
        super(MyMainFrame,self).__init__(None)

        self.m_spinCtrl1.SetRange(0, 59)
        self.m_spinCtrl2.SetRange(0, 59)
        self.resetflag = False
        self.m_led.SetBackgroundColour("yellow")
        self.m_led.SetForegroundColour("red")
        self.h = 0
        self.m = 0
        val = "{:0>2d}".format(self.h) + " " + "{:0>2d}".format(self.m)
        self.m_led.SetValue(val)
        self.myEvt_Done = wx.NewEventType()
        self.EVT_MSG = wx.PyEventBinder(self.myEvt_Done, 1)
        self.evt = MsgEvent(self.myEvt_Done, -1)
        self.Bind(self.EVT_MSG, self.PoPMsg)
        Notify.init("Timer App")
        self.notification = Notify.Notification.new(
            "Ding!",
            "Time is up.",
            "/home/yb/Pictures/11331.jpg"
        )




    def PoPMsg(self, event):
        self.notification.show()

    def OnFileChange(self, event):
        self.m_text.SetValue(self.m_filePicker1.GetPath())
    def OnClearFunc(self, event):
        self.text.SetValue(str(''))

    def OnReset( self, event ):
        self.resetflag = True
        self.start.Enable()
        self.m_spinCtrl2.SetValue(0)
        self.m_spinCtrl1.SetValue(0)
        self.m = 0
        self.h = 0
        val = "{:0>2d}".format(self.h) + " " + "{:0>2d}".format(self.m)
        self.m_led.SetValue(val)

    def OnSpinH(self, event):
        self.h = self.m_spinCtrl1.GetValue()
        val = "{:0>2d}".format(self.h) + " " +  "{:0>2d}".format(self.m)
        self.m_led.SetValue(val)

    def OnSpinM(self, event):
        self.m = self.m_spinCtrl2.GetValue()
        val = "{:0>2d}".format(self.h) + " " +  "{:0>2d}".format(self.m)
        self.m_led.SetValue(val)

    def OnStart( self, event ):
        self.start.Disable()
        self.resetflag = False
        thread.start_new_thread(self.CountDown, ())

    def CountDown(self):
        seconds = 60 * self.m_spinCtrl1.GetValue() + self.m_spinCtrl2.GetValue()
        if seconds == 0:
            return
        for i in range(0, seconds):
            if self.resetflag == True:
                self.m = 0
                self.h = 0
                val = "{:0>2d}".format(self.h) + " " + "{:0>2d}".format(self.m)
                self.m_led.SetValue(val)
                thread.exit()
            time.sleep(1)
            if self.m == 0:
                self.h = self.h -1
                self.m = 60
            self.m = self.m - 1
            val = "{:0>2d}".format(self.h) + " " + "{:0>2d}".format(self.m)
            self.m_led.SetValue(val)
        self.OnReset(None)
        wx.PostEvent(frame, self.evt)




        # if dlg.ShowModal() == wx.ID_YES:
        #     self.Close(True)
        # dlg.Destroy()


app = wx.App(False)
frame = MyMainFrame()
frame.Show()
app.MainLoop()