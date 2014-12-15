#! /usr/bin/env python
import pygtk
pygtk.require('2.0')
import gtk, gobject, cairo

from main_window import MainWindow
import defaults
from state import state

class Screen(gtk.DrawingArea):

    __gsignals__ = { "expose-event": "override" }

    def periodic(self):
        self.update()
        return True
        
    def update(self):
        self.queue_draw()

    def scroll_event(self, widget, event):
        print "event:", event
        if (event.direction == gtk.gdk.SCROLL_UP):
            state.decrease_scale()
        elif (event.direction == gtk.gdk.SCROLL_DOWN):
            state.increase_scale()
    
    def button_press_event(self, widget, event):
        print "button press:", event.button

    def key_press_event(self, widget, event):
        pass

    def key_release_event(self, widget, event):
        pass

    def button_release_event(self, widget, event):
        pass

    def motion_notify_event(self, widget, event):
        pass

    def do_expose_event(self, event):
        cr_gdk = self.window.cairo_create()
        surface = cr_gdk.get_target()
        cr_surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, event.area.width, event.area.height)
        cr = cairo.Context(cr_surf)
        
        # Restrict Cairo to the exposed area; avoid extra work
        cr.rectangle(event.area.x, event.area.y, event.area.width, event.area.height)
        cr.clip()

        cr.set_source_rgb(1.0, 1.0, 1.0)
        cr.rectangle(0, 0, int(event.area.width), int(event.area.height))
        cr.fill()

        w = event.area.width
        h = event.area.height
        scale = state.get_scale()
        print "scale:", scale
        grid = state.get_grid()

        cr.set_source_rgb(0, 0, 0)
        cr.set_line_width(0.1)
        for y in range(0, h, scale*grid):
            cr.move_to(0, y)
            cr.line_to(w, y)

        for x in range(0, w, scale*grid):
            cr.move_to(x, 0)
            cr.line_to(x, h)
        cr.stroke()
                

        cr_gdk.set_source_surface(cr_surf)
        cr_gdk.paint()

mw = MainWindow(defaults.d_width, defaults.d_height, Screen)

# GTK mumbo-jumbo to show the widget in a window and quit when it's closed

if __name__ == "__main__":
    mw.run()
