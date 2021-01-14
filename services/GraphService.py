import matplotlib.pyplot as plot

import numpy

class GraphService:
    
    artist1 = None
    artist2 = None
    artist1songs = None
    artist2songs = None

    def __init__(self, artist1, artist2):
        self.artist1 = artist1
        #self.artist1songs = self.generateSongList(artist1)
        self.artist2 = artist2
        #self.artist2songs = self.generateSongList(artist2)       

    def createPlot(self):
        width = 0.4
        x = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

        fig = plot.figure()

        bar1 = numpy.arange(len(self.artist1songs))
        bar2 = [i+width for i in bar1]

        fig.bar(bar1, self.artist1.songs, width, label = self.artist1.name)
        fig.bar(bar2, self.artist2.songs, width, label = self.artist2.name)

        fig.xlabel("Top Hits")
        fig.ylabel("Number of Streams")
        fig.title(self.artist1.name + " vs " + self.artist2.name)
        fig.xticks(bar1 + width/2, x)
        fig.legend()

        return fig

        


  


        

