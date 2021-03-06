from typing import List

class Student:
    def __init__(self, name:str, age:int, tracks:List[str], score: float):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, new_name:str):
        self.name = new_name

    def change_age(self, new_age:int):
        self.age = new_age

    def add_track(self, new_track:str):
        self.tracks.append(new_track)

    def get_score(self):
        return self.score

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
