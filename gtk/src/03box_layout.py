#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        # Gtk.Window.__init__(self, title="Hello World")
        super().__init__(title="Hello World")

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)
        
        self.label = Gtk.Label()
        self.label.set_text("aa")
        self.label.set_angle(25)
        self.label.set_halign(Gtk.Align.END)
        self.box.pack_start(self.label, True, True, 0)

        self.button = Gtk.Button(label="こんにちわ")
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button, True, True, 0)

        self.button2 = Gtk.Button(label="さようなら")
        self.button2.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button2, True, True, 0)
        
    def on_button_clicked(self, widgit):
        self.label.set_text(widgit.get_label())
        
        
        

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
