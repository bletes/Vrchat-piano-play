import win32api
import win32con
import win32gui
import win32ui
from win32gui import *
from win32api import *
from win32process import *
from ctypes import *
from ctypes import wintypes
import time
##hwnd=win32gui.FindWindow("YodaoMainWndClass", u"网易有道词典")
##print(hwnd)
##if hwnd!=0:
##    if win32gui.IsIconic(hwnd):
##        win32gui.ShowWindow(hwnd,win32con.SW_SHOWMAXIMIZED)
##    else:
##        win32gui.ShowWindow(hwnd,win32con.SW_SHOWMINIMIZED)
##    win32gui.SetForegroundWindow(hwnd)
##    win32gui.PostMessage(hwnd,win32con.WM_CLOSE,0,0)
##GetWindowText=windll.user32.GetWindowTextA
##def getWinTitle(self):
##    if self.win_hd is None:
##        return None
##    buffer=create_string_buffer(255,'\0')
##    GetWindowText(self.win_hd,buffer,255)
##    value=buffer.value.decode('gbk')
##    return value
##aa=getWinTitle(GetWindowText)
##hwnd=GetForegroundWindow()
##print(hwnd)
##FormThreadID=GetCurrentThreadId()
##print(FormThreadID)
##CwndThreadID=GetWindowThreadProcessId(hwnd)
##print(CwndThreadID)
##AttachThreadInput(CwndThreadID[0],FormThreadID,True)
##hwnd=GetFocus()
##print(hwnd)
##AttachThreadInput(CwndThreadID[0],FormThreadID,False)
##length=SendMessage(hwnd,win32con.WM_GETTEXTLENGTH)+1
##print(length)
##buf='0'*length
##print('get:',SendMessage(hwnd,win32con.WM_GETTEXT,length,buf))
##print('text:',buf)
##handle=win32gui.FindWindow('Notepad',None)
##left,top,right,bottom=win32gui.GetWindowRect(handle)
##title=win32gui.GetWindowText(handle)
##clsname=win32gui.GetClassName(handle)
##print(handle)
##print('%x'%(handle))
##hwndChildList=[]
##win32gui.EnumChildWindows(handle,lambda hwnd,param:param.append(hwnd),hwndChildList)
##subHandle=win32gui.FindWindowEx(handle,0,'EDIT',None)
####menuHandle=win32gui.GetMenu(subHandle)m
####subMenuHandle=win32gui.GetSubMenu(menuHandle,0)
####menuItemHandle=win32gui.GetMenuItemID(subMenuHandle,0)
##
####win32gui.postMessage(subHandle,win32con.WM_COMMAND,menuItemHandle,0)
####win32api.SetCursorPos([30,150])
##win32gui.SendMessage(subHandle, win32con.WM_SETTEXT, None, 'hell122o')
##time.sleep(2)
####win32api.keybd_event(77,0,0,0)
##win32api.SendMessage(hwnd, win32con.WM_SETFOCUS, 0, 0)
##hwndDC= win32gui.GetWindowDC(hwnd)
##time.sleep(3)
def click_point(x, y, hwnd=None):
    get_focus()
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, 0, ((y) << 16 | (x)));
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, ((y) << 16 | (x)));
def send_enter(hwnd,numvk):
##    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN,numvk, 0)
##    win32api.PostMessage(hwnd, win32con.WM_KEYUP,numvk, 0)
    win32api.PostMessage(hwnd, win32con.WM_HOTKEY,numvk, 0)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP,numvk, 0)
##    win32api.keybd_event(numvk,0,0,0)
##    win32api.keybd_event(numvk,0,win32con.KEYEVENTF_KEYUP,0)
##send_enter(hwndDC)
wdname = u'VRChat'  # 窗口名
handle = win32gui.FindWindow(None,wdname)
print(handle)
time.sleep(3)
send_enter(handle,77)
time.sleep(1)
send_enter(handle,73)
time.sleep(1)
send_enter(handle,77)
