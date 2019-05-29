from rx import create

def push_five_strings(observer, scheduler):
    """ For what reason we pass the scheduler!? """
    observer.on_next("Alpha")
    observer.on_next("Beta")
    observer.on_next("Gamma")
    observer.on_next("Delta")
    observer.on_next("Epsilon")
    observer.on_completed()

# Mainly define the reactive component here!, with a function that can pass
# observer and scheduler!

source = create(push_five_strings)

source.subscribe(
    # On suscribe we put the event triggers !
    on_next = lambda i: print("Received {0}".format(i)),
    on_error = lambda e: print("Error Occurred: {0}".format(e)),
    on_completed = lambda: print("Done!"),
)
