from subprocess import call

class SlaveDriver:
    def __init__(file):
        self.playing = false

    def playSong(file):
        if not self.playing:
            call(["mplayer", "-slave", "-input", "file=/tmp/lcdmsuicPipe", file)
            self.playing = True
        else:
            print "Already playing something"
        

    def TogglePlay():
        open("/tmp/lcdmusicPipe", "w").write(
        False if self.Playing else True
          
    
