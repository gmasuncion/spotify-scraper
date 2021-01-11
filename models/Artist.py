class Artist:
    """
    The Artist class will represent each artist in the top 100 chart.
    """
    def __init__(self, name, url, streams):
        self.name = name
        self.url = url
        self.streams = streams
        self.songs = []
