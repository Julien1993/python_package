"""
Here we are looking for the principle of the dictionary
"""

# Imports
import random

class Personne():

    def __init__(self, name, surname, id):
        self.name = name
        self.surname = surname
        self.id = id

    def __repr__(self):
        return f"Personne(name={self.name}, surname={self.surname}, id={self.id})"

    def __hash__(self):
        return hash(hash(self.name) + hash(self.surname) + hash(self.id))
    
    def __eq__(self, other):
         assert isinstance(other, Personne), "other is not a Personne object"
         return self.name == other.name and self.surname == other.surname and self.id == other.id
    
    

class PersonnePublique(Personne):
    
        def __init__(self, name, surname, id, profession):
            super().__init__(name, surname, id)
            self.profession = profession

        def __hash__(self):
            return hash(hash(self.name) + hash(self.surname) + hash(self.id) + hash(self.profession))
        
        def __eq__(self, other):
            assert isinstance(other, PersonnePublique), "other is not a PersonnePublique object"
            return super().__eq__(other) and self.profession == other.profession


class Dictionary:
    def __init__(self, initial_size=10):
        self.size = initial_size
        self.entries = [[] for _ in range(initial_size)]
        self.threshold = 0.7
        self.num_entries = 0

    def _hash(self, key):
        return hash(key) % self.size

    def add_entry(self, key, value):
        index = self._hash(key)
        bucket = self.entries[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.num_entries += 1
        if self.num_entries / self.size > self.threshold:
            self._resize()

    def get_entry(self, key):
        index = self._hash(key)
        for k, v in self.entries[index]:
            if k == key:
                return v
        return None

    def remove_entry(self, key):
        index = self._hash(key)
        bucket = self.entries[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.num_entries -= 1
                return

    def _resize(self):
        new_size = self.size * 2
        new_entries = [[] for _ in range(new_size)]

        for bucket in self.entries:
            for key, value in bucket:
                index = hash(key) % new_size
                new_entries[index].append((key, value))

        self.size = new_size
        self.entries = new_entries

    def display_entries(self):
        result = {}
        for bucket in self.entries:
            for k, v in bucket:
                result[k] = v
        return result




# Main

if __name__ == "__main__":
    personne_a = Personne("Jean", "Dupont", 1)
    personne_b = Personne("Jacques", "Henry", 2)
    personne_c = PersonnePublique("George", "Francois", 3, "Professeur")
    personne_d = PersonnePublique("George", "Francois", 3, "Professeur")

    print(personne_a == personne_b)
    print(personne_c == personne_d)
    
    group = [personne_a, personne_b, personne_c]

    my_dict = Dictionary()
    for person in group:
        my_dict.add_entry(person, random.randint(0, 100))
    #print(my_dict.display_entries())
    #print(my_dict.get_entry(personne_a))

    my_dict.remove_entry(personne_a)
    #print(my_dict.display_entries())

    my_dict.add_entry(personne_d, random.randint(0, 100))
    print(my_dict.display_entries())