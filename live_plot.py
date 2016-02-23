"""
Live_Plot.py

    An example using matplotlib with the TkAgg backend
    to creat a plot as you watch, with updating text,
    with Start and Pause buttons.

    Inspired by stackoverflow.com/questions/3294989

    Copyright (c) 2011 University of Toronto
    Last Modification:   23 September 2011 by David Bailey
    Original Version :   17 August 2011 by David Bailey
    Contact: David Bailey <dbailey@physics.utoronto.ca>
                (www.physics.utoronto.ca/~dbailey)
    License: Released under the MIT License; the full terms are appended
                to the end of this file, and are also available
                at www.opensource.org/licenses/mit-license.php
"""

ticks = []  # initialize timer store for speed optimization
from time import clock
ticks.append(clock()) # time at start

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from numpy import random, sin, exp
from matplotlib import pyplot
from matplotlib.figure import Figure
from Tkinter import Tk, Frame, Button

ticks.append(clock()) # time at start of plotting

root = Tk()
root.wm_title("Live Plot") # title for window

class RealTimePlot(Frame) :
    def __init__(self) :
        Frame.__init__(self)
        self.top=Frame()
        self.top.grid()
        self.top.update_idletasks()

        self.x = 0
        self.i = 0
        self.delta_i = 1
        self.update = 10
        # to speed things up, never plot more than n_points on screen
        self.n_points = 500
        self.n_data = 10000     # maximum number of points to acquire
        self.xy_data = []

        self.figure = pyplot.figure()
        # figsize (w,h tuple in inches) dpi (dots per inch)
        self.figure.set_size_inches((4,3), dpi=100, forward=True)
        self.subplot = self.figure.add_subplot(211)

        self.line, = self.subplot.plot([],[]) # initialize line to be drawn
        # Note: The comma after line is because the right hand size returns
        #   a one element list, and we want to unpack that single element
        #   into line, not assign the list to line.
        self.text = pyplot.figtext(0.05,0.25,"") # initialize text section

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.top)
        self.canvas.get_tk_widget().grid(row=3,column=0,columnspan=3)

        self.button_text = ['Start','Pause']
        self.buttons = [None] * len(self.button_text)

        for button_index in range(len(self.button_text)) :
            button_id = Button(self.top,text=self.button_text[button_index])
            button_id.grid(row=0, column=button_index)
            self.buttons[button_index] = button_id

            def button_handler(event, self=self, button=button_index):
                return self.service_buttons(button)

            button_id.bind("<Button-1>", button_handler)

    # buttons can be used to start and pause plotting
    def service_buttons(self, toolbar_index):
        if toolbar_index == 0 :
            self.stop = False
            self.plotter()
        else:
            self.stop = True

    # while in start, check if stop is clicked, if not, call blink recursivly
    def plotter(self):
        if not self.stop :
            self.x += 0.1
            self.y = exp(-self.i*0.005)*sin(self.x)+0.1*random.randn()
            self.xy_data += [[self.x,self.y]]
            # If there are many data points, it is a waste of time to plot all
            #   of them once the screen resolution is reached,
            #   so when the maximum number of points is reached,
            #   halve the number of points plotted. This is repeated
            #   every time the number of data points has doubled.
            if self.i == self.n_points :
                self.n_points *= 2
                # frequency of plotted points
                self.delta_i *= self.n_points/self.i
                self.update = max(self.delta_i, self.update)
                print "updating n_rescale = ",\
            	    self.n_points, self.update, self.delta_i
            # drawing the canvas takes most of the CPU time, so only update plot
            #   every so often
            if self.i == self.n_data-1 or not (self.i % self.update)  :
                # remove previous version of line plot
                self.subplot.lines.remove(self.line)
                self.figure.texts.remove(self.text)
                self.line, = self.subplot.plot(
                            [row[0] for row in self.xy_data[0::self.delta_i]],
                                [row[1] for row in self.xy_data[0::self.delta_i]],
                                color="blue")
                self.text = pyplot.figtext(0.05,0.25,
                                  "Point # " + str(self.i+1) +
                                  "\nx,y = " + str(self.x) + ", " + str(self.y))
            self.i += 1
            # stop if desired number of points plotted
            if self.i == self.n_data :
                self.service_buttons(1)
            self.canvas.draw()
            self.canvas.get_tk_widget().update_idletasks()
            self.after(2,self.plotter)

RealTimePlot().mainloop()

ticks.append(clock()) # time at end

# Print timings
print( "Initialization took : {} seconds".format(ticks[1]-ticks[0]) )
print( "Drawing took        : {} seconds".format(ticks[2]-ticks[1]) )


# End of Live_Plot.py


"""
Full text of MIT License:

    Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
