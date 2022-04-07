#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyoo

#start type 1
#soffice --accept="socket,host=localhost,port=2002;urp;" --norestore --nologo --nodefault --headless &
#desktop = pyoo.Desktop('localhost', 2002)

#start type 2
#soffice --accept="pipe,name=hello;urp;" --norestore --nologo --nodefault --headless &
desktop = pyoo.Desktop(pipe='hello')



#new spreadsheet
doc = desktop.create_spreadsheet()
# doc = doc = desktop.open_spreadsheet("~/DL/test11.ods")

#sheet
sheet = doc.sheets[0]
#sheet = doc.sheets['Sheet1']

#create sheet
doc.sheets.create('My Sheet', index=1)

#copy sheet
doc.sheets.copy('My Sheet', 'Copied Sheet', 2)

#delete sheet
#del doc.sheets[1]
#del doc.sheets['Copied sheet']

#cell set
sheet[0,0].value = 1
sheet[0,1].value = 2
sheet[0,2].formula = '=$A1+$B1'

#cell get
print("value=", sheet[0,0].value, "\n")
print("formula=", sheet[0,2].formula, "\n")

#range set
sheet[1:3,0:2].values = [[3, 4], [5, 6]]
sheet[3, 0:2].formulas = ['=$A$1+$A$2+$A$3', '=$B$1+$B$2+$B$3']

#range get
print("values=", sheet[1:4,2].values, "\n")

#format
cells = sheet[:4,:3]

#format font
cells.font_size = 20
cells[3, :].font_weight = pyoo.FONT_WEIGHT_BOLD
cells[:, 2].text_align = pyoo.TEXT_ALIGN_LEFT
cells[-1,-1].underline = pyoo.UNDERLINE_DOUBLE

# Colors:
cells[:3,:2].text_color = 0xFF0000                 # 0xRRGGBB
cells[:-1,:-1].background_color = 0x0000FF         # 0xRRGGBB

# Borders
cells[:,:].border_width = 100
cells[:,:].border_color = 0xFFFF00
cells[-4:-1,-3:-1].inner_border_width = 50

#save

print("save file=~/DL/test11.xlsx", "\n")

# doc.save("~/DL/test11.xlsx", pyoo.FILTER_EXCEL_2007)
doc.save("/home/user/DL/test11.xlsx", pyoo.FILTER_EXCEL_2007)
#doc.save()

#close
doc.close()


