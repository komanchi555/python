class NoteBook:
    def __init__(self):
        self.notes = dict()

    def add_note(self, unique_key, note):
        self.notes[unique_key] = note

    def get_note(self, unique_key):
        self.notes.get(unique_key, None)

    def get_notes(self):
        notes = list()
        notes.extend(self.notes.values())
        return notes

    def remove_note(self, unique_key):
        self.notes.pop(unique_key, None)


notebook1 = NoteBook()

notebook1.add_note(1, "A first note")
notebook1.add_note(2, "A second bigger note")
print(notebook1.notes)

print(notebook1.get_note(2))  # should print "A second bigger note"

notebook1.add_note(2, "A third much bigger note")

print(notebook1.get_note(2))  # should print "A third much bigger note"

print(notebook1.get_notes())  # should print ["A first note", "A second note of the second notebook"]

print(notebook1.get_note(3))  # should print None

notebook1.remove_note(2)

print(notebook1.get_notes())  # should print ["A first note"]

print(notebook1.get_note(2))  # should print None
