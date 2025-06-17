# We are defining a model that represents a course and a list of courses, with fields like: 
# title, description, presenter, imageUrl, courseURL 


from pydantic import BaseModel
from typing import List

# Define the structure of a single course
class DeeplearningCourse(BaseModel):
    title: str
    description: str
    presenter: List[str]
    imageUrl: str
    courseURL: str

# Define the structure of a list of courses
class DeeplearningCourseList(BaseModel):
    courses: List[DeeplearningCourse]
