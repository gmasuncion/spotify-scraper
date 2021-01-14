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

        

        bar1 = numpy.arange(len(self.artist1.songs))
        bar2 = [i+width for i in bar1]

        artist1streams = self.getStreamsList(self.artist1)
        artist2streams = self.getStreamsList(self.artist2)

        plot.bar(bar1, artist1streams, width, label = self.artist1.name)
        plot.bar(bar2, artist2streams, width, label = self.artist2.name)

        plot.xlabel("Top Hits")
        plot.ylabel("Number of Streams")
        plot.title(self.artist1.name + " vs " + self.artist2.name)
        plot.xticks(bar1 + width/2, x)
        plot.legend()

        fig = plot.figure(figsize=(8, 6))

        return fig

    def getStreamsList(self, artist):
        streamsList = []
        for song in artist.songs:
            streamsList.append(song.streams)
        return streamsList

        


  


        

