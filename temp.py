import eventhor

class EventSample(eventhor.Event):
    def __init__(self):
        super().__init__()
        self.cnt = 0

    def main(self):
        if self.cnt % 100 == 0:
            self.fire() # if condition is met to event, then you should call Event.fire()
        self.cnt += 1

def callback():
    print("callback")

ev = eventhor.Eventhor()
ev.register(EventSample, func)
ev.loop_forever() # loop with calling main() method of registered events.
