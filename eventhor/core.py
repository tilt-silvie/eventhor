class Dispatcher(object):
    def __init__(self):
        self._dispatch_table = []

    def register(self, event_class, callback):
        self._dispatch_table.append([event_class, callback])

    def dispatch(self, event_class):
        def search_callback(event_class):
            return [x[1] for x in self._dispatch_table if x[0] == event_class]

        callbacks = search_callback(event_class)
        for callback in callbacks:
            callback()


class Event(object):
    def __init__(self):
        self._dispatcher = None

    def register_dispatcher(self, dispatcher: Dispatcher) -> None:
        self._dispatcher = dispatcher

    def fire(self):
        self._dispatcher.dispatch(self.__class__)

    def main(self):
        pass


class Eventhor(object):
    def __init__(self):
        self._dispatcher = Dispatcher()
        self._event_list = []

    def register(self, event_class, callback):
        def is_event_in_list(event_class):
            y = [x for x in self._event_list if x.__class__ == event_class]
            if y: # y is not empty
                return True
            else:
                return False

        if not is_event_in_list(event_class):
            event = event_class()
            event.register_dispatcher(self._dispatcher)
            self._event_list.append(event)

        self._dispatcher.register(event_class, callback)

    def loop_forever(self):
        while True:
            for event in self._event_list:
                event.main()



