#!/usr/bin/python
# -*- coding: utf-8 -*- 
#-------------------------------------
# Useage£ºCapture the screen and save it to bitmap format
#
#-------------------------------------


import time
import os, win32gui, win32ui, win32con, win32api

def window_capture():
    hwnd = 0
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()

    MoniterDev = win32api.EnumDisplayMonitors(None,None)
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]

    print w, h

    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0,0),(w, h) , mfcDC, (0,0), win32con.SRCCOPY)
    bmpname=win32api.GetTempFileName(".","")[0]+'.bmp'
    saveBitMap.SaveBitmapFile(saveDC, bmpname)
    return bmpname

os.system(window_capture())