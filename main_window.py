#-*- encoding: utf-8 -*-
import pygtk
pygtk.require('2.0')
import gtk, gobject, cairo
import sys

class MainWindow(object):
    def __init__(self, w, h, Widget):
        self.window = gtk.Window()
        self.window.resize(w, h)
        self.window.connect("delete-event", gtk.main_quit)

        self.menu_bar = gtk.MenuBar()
        self.file_menu = gtk.Menu()
        self.file_item = gtk.MenuItem("File")
        self.file_item.set_submenu(self.file_menu)
        self.menu_bar.append(self.file_item)

        self.open_project_item = gtk.MenuItem("Open project ...")
        self.save_project_item = gtk.MenuItem("Save project ...")
        sep_export_import = gtk.SeparatorMenuItem()
        self.export_item = gtk.MenuItem("Export ...")
        self.quit_item = gtk.MenuItem("Quit")
        sep_quit = gtk.SeparatorMenuItem()

        self.file_menu.append(self.open_project_item)
        self.file_menu.append(self.save_project_item)
        self.file_menu.append(sep_export_import)
        self.file_menu.append(self.export_item)
        self.file_menu.append(sep_quit)
        self.file_menu.append(self.quit_item)

        self.export_item.connect("activate", lambda *args: ep.push_event(EVEnum.export_click, args))
        self.open_project_item.connect("activate", lambda *args: ep.push_event(EVEnum.load_project_click, args))
        self.save_project_item.connect("activate", lambda *args: ep.push_event(EVEnum.save_project_click, args))
        self.quit_item.connect("activate", lambda *args: ep.push_event(EVEnum.quit_click, args))

        self.window_vbox = gtk.VBox(homogeneous=False, spacing=0)
        self.window_vbox.pack_start(self.menu_bar, expand=False, fill=False, padding=0)
        self.window.add(self.window_vbox)

        self.widget = Widget()
        self.widget.connect("button_press_event", self.widget.button_press_event)
        self.widget.connect("button_release_event", self.widget.button_release_event)
        self.widget.connect("motion_notify_event", self.widget.motion_notify_event)
        self.widget.connect("scroll_event", self.widget.scroll_event)
        self.window.connect("key_press_event", self.widget.key_press_event)
        self.window.connect("key_release_event", self.widget.key_release_event)
        self.window.set_events(gtk.gdk.KEY_PRESS_MASK | gtk.gdk.KEY_RELEASE_MASK)
        self.widget.set_events(gtk.gdk.BUTTON_PRESS_MASK | gtk.gdk.BUTTON_RELEASE_MASK | gtk.gdk.POINTER_MOTION_MASK)

        gobject.timeout_add(30, self.widget.periodic)

        self.hbox = gtk.HBox(homogeneous=False, spacing=0)
        #self.hbox.pack_start(self.left_vbox, expand=False, fill=False, padding=0)

        self.widget_hbox = gtk.HBox(homogeneous=False, spacing=0)
        self.widget_vbox = gtk.VBox(homogeneous=False, spacing=0)
        self.widget_hscroll = gtk.HScrollbar(gtk.Adjustment(0.0, 0.0, 0.0, 10.0, 100.0, 1.0))
        self.widget_hscroll.connect("value-changed", lambda *args: ep.push_event(EVEnum.hscroll, (args)))
        self.widget_vscroll = gtk.VScrollbar(gtk.Adjustment(0.0, 0.0, 0.0, 10.0, 100.0, 1.0))
        self.widget_vscroll.connect("value-changed", lambda *args: ep.push_event(EVEnum.vscroll, (args)))
        self.widget_hbox.pack_start(self.widget, expand=True, fill=True, padding=0)
        self.widget_hbox.pack_start(self.widget_vscroll, expand=False, fill=False, padding=0)
        self.widget_vbox.pack_start(self.widget_hbox, expand=True, fill=True)
        self.widget_vbox.pack_start(self.widget_hscroll, expand=False, fill=False, padding=0)
        self.hbox.pack_start(self.widget_vbox, expand=True, fill=True, padding=0)
        self.window_vbox.pack_start(self.hbox, expand=True, fill=True, padding=0)


    def run(self):
        self.window.show_all()
        self.window.present()
        gtk.main()

