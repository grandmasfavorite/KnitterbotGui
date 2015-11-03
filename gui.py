import pygtk
pygtk.require("2.0")
import gtk

class Base:

	def senddata(self, widget, data=None):
		length = int(self.lengthEntry.get_text())
		if length < 1:
			self.lengthEntry.set_text("INVALID")
			length =  None
		width = int(self.widthEntry.get_text())
		if width < 10:
			self.widthEntry.set_text("INVALID")
			width = None
		elif width > 50:
			self.widthEntry.set_text("INVALID")
			width = None

		#Doing Stuff
		if width and length:
			print "width: %s" % width
			print "length: %s" % length
			self.window.destroy()
		else:
			print "Invalid Entry"
		

	def delete_event(self, widget, event, data = None):
		""" This will make it easy to pop up a window saying
			'Are you sure you want to quit?'. It sends a signal
			to destroy the GTK window
		"""
		print "delete event occured"
		return False #Returning true would close the window

	def destroy(self, widget, data = None):
		gtk.main_quit()

	def __init__(self):
		#Creating the Window
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect("delete_event", self.delete_event)
		self.window.connect("destroy", self.destroy)

		self.vbox = gtk.VBox(gtk.FALSE, 0)
		self.window.add(self.vbox)
		self.vbox.show()

		#Creating A length Entry Box
		self.lengthEntry = gtk.Entry()
		self.lengthEntry.set_text("Scarf Length")
		#self.lengthEntry.connect("activate", self.get_length, self.lengthEntry)
		self.vbox.pack_start(self.lengthEntry, gtk.TRUE, gtk.TRUE, 0)
		self.lengthEntry.show()
 
		#Creating a width entry Box
		self.widthEntry = gtk.Entry()
		self.widthEntry.set_text("Scarf Width")
		#self.widthEntry.connect("activate", self.get_width, self.widthEntry)
		self.vbox.pack_start(self.widthEntry, gtk.TRUE, gtk.TRUE, 0)
		self.widthEntry.show()

		#Creating the Confirm button
		self.button = gtk.Button("Confirm.")
		self.button.connect("clicked", self.senddata, None)
		#self.button.connect_object("clicked", gtk.Widget.destroy, self.window)
		self.vbox.pack_start(self.button, gtk.TRUE, gtk.TRUE, 0)
		self.button.show()
		
		#Displaying Everything
		self.window.show()

	def main(self):
		""" All PyGTK applications must have a gtk.main().
		    Control ends here and waits for an even to occur
	    """
		gtk.main()


print __name__
if __name__ == "__main__":
	base = Base()
	base.main()