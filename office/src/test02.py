#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uno

#https://ugcj.com/python%E3%81%A7libreoffice%E3%81%AE%E3%83%9E%E3%82%AF%E3%83%AD/


def sample():


    doc = XSCRIPTCONTEXT.getDocument()

    # シートを選択
      #sheet = doc.getSheets().getByName('Sheet1')
      #sheet = doc.getSheets().getByIndex(0)
      sheet = doc.CurrentController.getActiveSheet()

      # C1 = A1 + B1
      A1 = sheet.getCellRangeByName('A1')
      B1 = sheet.getCellRangeByName('B1')
      C1 = sheet.getCellRangeByName('C1')
      C1.Value = A1.Value + B1.Value

      # C2 = A2 + B2
      A2 = sheet.getCellByPosition(0, 1)
      B2 = sheet.getCellByPosition(1, 1)
      C2 = sheet.getCellByPosition(2, 1)
      C2.String = A2.String + B2.String

