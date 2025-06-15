from pymongo import MongoClient
from datetime import datetime
import pandas as pd

# Connect to Database
try:
    client = MongoClient('mongodb://localhost:27017/')
    db = client['eduhub_db']
    print('Connection Successful!')
except Exception as e:
    print(f'Erro connecting to Database: {e}')

# Populate data into the database
# Users data
user_data = [
    {"user_id": 1, "full_name": "Dorcas Williams", "email": "dorcas@gmail.com", "role": "instructor", "dateJoined": datetime.now(), "profile": {
        "bio": "I am Dorcas, an instructor at this academy.",
        "avatar": "https://example.com/avatar1.jpg",
        "skills": ["Python", "MongoDB", "SQL", "JavaScript"]
    }, 'is_active': 'True'},
    {"user_id": 2, "full_name": "Isaac Brown", "email": "isaacb@gmail.com", "role": "student", "dateJoined": datetime.now(), "profile": {
        "bio": "Student passionate about backend development.",
        "avatar": "https://example.com/avatar2.jpg",
        "skills": ["Python", "Flask", "Docker"]
    }, 'is_active': 'True'},
    {"user_id": 3, "full_name": "Clara Osei", "email": "clarao@gmail.com", "role": "instructor", "dateJoined": datetime.now(), "profile": {
        "bio": "Teaching JavaScript and frontend frameworks.",
        "avatar": "https://example.com/avatar3.jpg",
        "skills": ["JavaScript", "React", "HTML", "CSS"]
    }, 'is_active': 'True'},
    {"user_id": 4, "full_name": "Emeka Obi", "email": "emeka@gmail.com", "role": "student", "dateJoined": datetime.now(), "profile": {
        "bio": "Learning data analysis and visualization.",
        "avatar": "https://example.com/avatar4.jpg",
        "skills": ["Excel", "Power BI", "SQL"]
    }, 'is_active': 'True'},
    {"user_id": 5, "full_name": "Aisha Bello", "email": "aisha@gmail.com", "role": "instructor", "dateJoined": datetime.now(), "profile": {
        "bio": "Mentor in machine learning and Python.",
        "avatar": "https://example.com/avatar5.jpg",
        "skills": ["Python", "Scikit-learn", "Pandas", "NumPy"]
    }, 'is_active': 'True'},
    {"user_id": 6, "full_name": "John Doe", "email": "jdoe@gmail.com", "role": "student", "dateJoined": datetime.now(), "profile": {
        "bio": "Exploring web development fundamentals.",
        "avatar": "https://example.com/avatar6.jpg",
        "skills": ["HTML", "CSS", "JavaScript"]
    }, 'is_active': 'True'},
    {"user_id": 7, "full_name": "Grace Mwangi", "email": "gracem@gmail.com", "role": "instructor", "dateJoined": datetime.now(), "profile": {
        "bio": "Guiding students in cloud computing.",
        "avatar": "https://example.com/avatar7.jpg",
        "skills": ["AWS", "Azure", "Docker"]
    }, 'is_active': 'True'},
    {"user_id": 8, "full_name": "Samuel Kim", "email": "samkim@gmail.com", "role": "student", "dateJoined": datetime.now(), "profile": {
        "bio": "Interested in automation and scripting.",
        "avatar": "https://example.com/avatar8.jpg",
        "skills": ["Python", "Bash", "Git"]
    }, 'is_active': 'True'},
    {"user_id": 9, "full_name": "Fatima Yusuf", "email": "fatima@gmail.com", "role": "instructor", "dateJoined": datetime.now(), "profile": {
        "bio": "Instructor focused on database design.",
        "avatar": "https://example.com/avatar9.jpg",
        "skills": ["MySQL", "PostgreSQL", "MongoDB"]
    }, 'is_active': 'True'},
    {"user_id": 10, "full_name": "Michael Chen", "email": "mchen@gmail.com", "role": "student", "dateJoined": datetime.now(), "profile": {
        "bio": "Pursuing a path in AI and deep learning.",
        "avatar": "https://example.com/avatar10.jpg",
        "skills": ["TensorFlow", "Keras", "Python"]
    }, 'is_active': 'True'},
    {"user_id": 11, "full_name": "Linda Kone", "email": "lindak@gmail.com", "role": "instructor", "dateJoined": datetime.now(), "profile": {
        "bio": "Instructor in software engineering principles.",
        "avatar": "https://example.com/avatar11.jpg",
        "skills": ["Java", "Spring Boot", "Git"]
    }, 'is_active': 'True'},
    {"user_id": 12, "full_name": "Omar Diallo", "email": "omard@gmail.com", "role": "student", "dateJoined": datetime.now(), "profile": {
        "bio": "Learning APIs and backend development.",
        "avatar": "https://example.com/avatar12.jpg",
        "skills": ["Node.js", "Express", "MongoDB"]
    }, 'is_active': 'True'},
    {"user_id": 13, "full_name": "Janet Mensah", "email": "janetm@gmail.com", "role": "instructor", "dateJoined": datetime.now(), "profile": {
        "bio": "Frontend expert and UI/UX enthusiast.",
        "avatar": "https://example.com/avatar13.jpg",
        "skills": ["HTML", "CSS", "Figma", "React"]
    }, 'is_active': 'True'},
    {"user_id": 14, "full_name": "Aliyu Musa", "email": "aliyum@gmail.com", "role": "student", "dateJoined": datetime.now(), "profile": {
        "bio": "Beginner exploring full-stack development.",
        "avatar": "https://example.com/avatar14.jpg",
        "skills": ["Python", "React", "Django"]
    }, 'is_active': 'True'},
    {"user_id": 15, "full_name": "Sarah Njeri", "email": "sarahn@gmail.com", "role": "instructor", "dateJoined": datetime.now(), "profile": {
        "bio": "Cybersecurity instructor with 5 years of experience.",
        "avatar": "https://example.com/avatar15.jpg",
        "skills": ["Network Security", "Linux", "Python"]
    }, 'is_active': 'True'},
    {"user_id": 16, "full_name": "Peter Obi", "email": "petero@gmail.com", "role": "student", "dateJoined": datetime.now(), "profile": {
        "bio": "Student aiming to become a DevOps engineer.",
        "avatar": "https://example.com/avatar16.jpg",
        "skills": ["Docker", "Kubernetes", "CI/CD"]
    }, 'is_active': 'True'},
    {"user_id": 17, "full_name": "Fola Adebayo", "email": "fola@gmail.com", "role": "instructor", "dateJoined": datetime.now(), "profile": {
        "bio": "Specialist in data science and analytics.",
        "avatar": "https://example.com/avatar17.jpg",
        "skills": ["Pandas", "NumPy", "Tableau", "SQL"]
    }, 'is_active': 'True'},
    {"user_id": 18, "full_name": "Mariam Jatta", "email": "mariamj@gmail.com", "role": "student", "dateJoined": datetime.now(), "profile": {
        "bio": "Exploring app development and design.",
        "avatar": "https://example.com/avatar18.jpg",
        "skills": ["Flutter", "Dart", "Firebase"]
    }, 'is_active': 'True'},
    {"user_id": 19, "full_name": "Kevin Banda", "email": "kevinb@gmail.com", "role": "instructor", "dateJoined": datetime.now(), "profile": {
        "bio": "Mobile development mentor.",
        "avatar": "https://example.com/avatar19.jpg",
        "skills": ["React Native", "Kotlin", "Swift"]
    }, 'is_active': 'True'},
    {"user_id": 20, "full_name": "Chinwe Okeke", "email": "chinweo@gmail.com", "role": "student", "dateJoined": datetime.now(), "profile": {
        "bio": "Interested in cybersecurity and networking.",
        "avatar": "https://example.com/avatar20.jpg",
        "skills": ["Wireshark", "Linux", "Python"]
    }, 'is_active': 'True'},
]

try:
    user_collection = db["users"]
    insert_data = user_collection.insert_many(user_data)
    print("Users added!!!")
except Exception as e:
    print(f"Unable to add user because of {e}")

# Course
course_data = [
    {
        "course_id": 1,
        "title": "Introduction to Python",
        "description": "Learn the basics of Python programming.",
        "instructor_id": 1,
        "category": "Programming",
        "level": "beginner",
        "duration": 10,
        "price": 49.99,
        "tags": ["Python", "Programming", "Beginner"],
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "is_published": True,
        "rating": 4.7
    },
    {
        "course_id": 2,
        "title": "Data Analysis with Pandas",
        "description": "Analyze data efficiently using Pandas library.",
        "instructor_id": 5,
        "category": "Data Science",
        "level": "intermediate",
        "duration": 8,
        "price": 59.99,
        "tags": ["Data Science", "Pandas", "Analysis"],
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "is_published": True,
        "rating": 4.6
    },
    {
        "course_id": 3,
        "title": "Web Development with HTML & CSS",
        "description": "Build modern websites using HTML and CSS.",
        "instructor_id": 13,
        "category": "Web Development",
        "level": "beginner",
        "duration": 12,
        "price": 39.99,
        "tags": ["HTML", "CSS", "Frontend"],
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "is_published": True,
        "rating": 4.8
    },
    {
        "course_id": 4,
        "title": "JavaScript Essentials",
        "description": "Understand JavaScript for interactive web pages.",
        "instructor_id": 3,
        "category": "Programming",
        "level": "beginner",
        "duration": 14,
        "price": 44.99,
        "tags": ["JavaScript", "Frontend"],
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "is_published": True,
        "rating": 4.5
    },
    {
        "course_id": 5,
        "title": "React for Beginners",
        "description": "Build responsive web apps using React.",
        "instructor_id": 13,
        "category": "Frontend Development",
        "level": "intermediate",
        "duration": 15,
        "price": 69.99,
        "tags": ["React", "JavaScript", "Frontend"],
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "is_published": True,
        "rating": 4.9
    },
    {
        "course_id": 6,
        "title": "Advanced Machine Learning",
        "description": "Dive deep into ML algorithms and model tuning.",
        "instructor_id": 5,
        "category": "Data Science",
        "level": "advanced",
        "duration": 20,
        "price": 99.99,
        "tags": ["ML", "AI", "Scikit-learn"],
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "is_published": True,
        "rating": 4.6
    },
    {
        "course_id": 7,
        "title": "Database Design with SQL",
        "description": "Design and query relational databases effectively.",
        "instructor_id": 9,
        "category": "Databases",
        "level": "intermediate",
        "duration": 10,
        "price": 55.00,
        "tags": ["SQL", "Database", "Design"],
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "is_published": True,
        "rating": 4.4
    },
    {
        "course_id": 8,
        "title": "Cybersecurity Fundamentals",
        "description": "Protect systems with foundational security concepts.",
        "instructor_id": 15,
        "category": "Security",
        "level": "beginner",
        "duration": 9,
        "price": 65.50,
        "tags": ["Security", "Network", "Linux"],
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "is_published": True,
        "rating": 4.3
    }
]

try:
    course_collection = db["courses"]
    insert_course_data = course_collection.insert_many(course_data)
    print("Courses added!!!")
except Exception as e:
    print(f"Unable to add courses because of {e}")

# Enrollment
enrollments_data = [
    {"enrollment_id": 1, "student_id": 4, "course_id": 1, "enrolled_at": datetime.now(), "is_active": True},
    {"enrollment_id": 2, "student_id": 6, "course_id": 3, "enrolled_at": datetime.now(), "is_active": True},
    {"enrollment_id": 3, "student_id": 8, "course_id": 2, "enrolled_at": datetime.now(), "is_active": True},
    {"enrollment_id": 4, "student_id": 10, "course_id": 5, "enrolled_at": datetime.now(), "is_active": True},
    {"enrollment_id": 5, "student_id": 12, "course_id": 4, "enrolled_at": datetime.now(), "is_active": True},
    {"enrollment_id": 6, "student_id": 14, "course_id": 6, "enrolled_at": datetime.now(), "is_active": True},
    {"enrollment_id": 7, "student_id": 16, "course_id": 7, "enrolled_at": datetime.now(), "is_active": True},
    {"enrollment_id": 8, "student_id": 18, "course_id": 8, "enrolled_at": datetime.now(), "is_active": False},
    {"enrollment_id": 9, "student_id": 20, "course_id": 9, "enrolled_at": datetime.now(), "is_active": True},
    {"enrollment_id": 10, "student_id": 4, "course_id": 10, "enrolled_at": datetime.now(), "is_active": True},
    {"enrollment_id": 11, "student_id": 6, "course_id": 12, "enrolled_at": datetime.now(), "is_active": True},
    {"enrollment_id": 12, "student_id": 8, "course_id": 13, "enrolled_at": datetime.now(), "is_active": True},
    {"enrollment_id": 13, "student_id": 10, "course_id": 14, "enrolled_at": datetime.now(), "is_active": False},
    {"enrollment_id": 14, "student_id": 12, "course_id": 15, "enrolled_at": datetime.now(), "is_active": True},
    {"enrollment_id": 15, "student_id": 14, "course_id": 16, "enrolled_at": datetime.now(), "is_active": True},
]

try:
    course_collection = db["enrollments"]
    insert_course_data = course_collection.insert_many(enrollments_data)
    print("Enrollments added!!!")
except Exception as e:
    print(f"Unable to add enrollments because of {e}")

# Lesson
lessons_data = [
    {'lesson_id': 1, 'course_id': 2, 'title': 'Lesson 1: Introduction to HTML', 'content': 'This is the content for lesson 1.', 'video_url': 'https://example.com/videos/lesson1.mp4', 'duration': 11, 'created_at': datetime.now(), 'updated_at': datetime.now()},
    {'lesson_id': 2, 'course_id': 2, 'title': 'Lesson 2: HTML Tags & Elements', 'content': 'Learn about tags and elements.', 'video_url': 'https://example.com/videos/lesson2.mp4', 'duration': 13, 'created_at': datetime.now(), 'updated_at': datetime.now()},
    {'lesson_id': 3, 'course_id': 3, 'title': 'Lesson 3: CSS Basics', 'content': 'Styling with CSS.', 'video_url': 'https://example.com/videos/lesson3.mp4', 'duration': 10, 'created_at': datetime.now(), 'updated_at': datetime.now()},
    {'lesson_id': 4, 'course_id': 3, 'title': 'Lesson 4: CSS Flexbox', 'content': 'Layout using Flexbox.', 'video_url': 'https://example.com/videos/lesson4.mp4', 'duration': 12, 'created_at': datetime.now(), 'updated_at': datetime.now()},
    {'lesson_id': 5, 'course_id': 4, 'title': 'Lesson 5: JavaScript Intro', 'content': 'Basics of JavaScript.', 'video_url': 'https://example.com/videos/lesson5.mp4', 'duration': 15, 'created_at': datetime.now(), 'updated_at': datetime.now()},
    {'lesson_id': 6, 'course_id': 4, 'title': 'Lesson 6: JavaScript Functions', 'content': 'Working with functions.', 'video_url': 'https://example.com/videos/lesson6.mp4', 'duration': 14, 'created_at': datetime.now(), 'updated_at': datetime.now()},
    {'lesson_id': 7, 'course_id': 5, 'title': 'Lesson 7: Python Basics', 'content': 'Getting started with Python.', 'video_url': 'https://example.com/videos/lesson7.mp4', 'duration': 18, 'created_at': datetime.now(), 'updated_at': datetime.now()},
    {'lesson_id': 8, 'course_id': 5, 'title': 'Lesson 8: Python Control Flow', 'content': 'If-else and loops.', 'video_url': 'https://example.com/videos/lesson8.mp4', 'duration': 16, 'created_at': datetime.now(), 'updated_at': datetime.now()},
    {'lesson_id': 9, 'course_id': 6, 'title': 'Lesson 9: Python Functions', 'content': 'Defining and calling functions.', 'video_url': 'https://example.com/videos/lesson9.mp4', 'duration': 13, 'created_at': datetime.now(), 'updated_at': datetime.now()},
    {'lesson_id': 10, 'course_id': 6, 'title': 'Lesson 10: Python Lists', 'content': 'List operations and comprehensions.', 'video_url': 'https://example.com/videos/lesson10.mp4', 'duration': 12, 'created_at': datetime.now(), 'updated_at': datetime.now()},
    {'lesson_id': 11, 'course_id': 7, 'title': 'Lesson 11: Working with APIs', 'content': 'What are APIs?', 'video_url': 'https://example.com/videos/lesson11.mp4', 'duration': 14, 'created_at': datetime.now(), 'updated_at': datetime.now()},
    {'lesson_id': 12, 'course_id': 7, 'title': 'Lesson 12: REST APIs', 'content': 'How REST APIs work.', 'video_url': 'https://example.com/videos/lesson12.mp4', 'duration': 15, 'created_at': datetime.now(), 'updated_at': datetime.now()},
    {'lesson_id': 13, 'course_id': 8, 'title': 'Lesson 13: Flask Intro', 'content': 'Getting started with Flask.', 'video_url': 'https://example.com/videos/lesson13.mp4', 'duration': 12, 'created_at': datetime.now(), 'updated_at': datetime.now()},
    {'lesson_id': 14, 'course_id': 8, 'title': 'Lesson 14: Flask Routing', 'content': 'Handling routes.', 'video_url': 'https://example.com/videos/lesson14.mp4', 'duration': 11, 'created_at': datetime.now(), 'updated_at': datetime.now()},
    {'lesson_id': 15, 'course_id': 9, 'title': 'Lesson 15: SQL Basics', 'content': 'Intro to SQL.', 'video_url': 'https://example.com/videos/lesson15.mp4', 'duration': 17, 'created_at': datetime.now(), 'updated_at': datetime.now()},
    {'lesson_id': 16, 'course_id': 9, 'title': 'Lesson 16: SQL Joins', 'content': 'Combining tables.', 'video_url': 'https://example.com/videos/lesson16.mp4', 'duration': 16, 'created_at': datetime.now(), 'updated_at': datetime.now()},
    {'lesson_id': 17, 'course_id': 10, 'title': 'Lesson 17: MongoDB Intro', 'content': 'NoSQL concepts.', 'video_url': 'https://example.com/videos/lesson17.mp4', 'duration': 12, 'created_at': datetime.now(), 'updated_at': datetime.now()},
    {'lesson_id': 18, 'course_id': 10, 'title': 'Lesson 18: MongoDB Queries', 'content': 'Basic MongoDB queries.', 'video_url': 'https://example.com/videos/lesson18.mp4', 'duration': 14, 'created_at': datetime.now(), 'updated_at': datetime.now()},
    {'lesson_id': 19, 'course_id': 11, 'title': 'Lesson 19: Git Basics', 'content': 'Using Git for version control.', 'video_url': 'https://example.com/videos/lesson19.mp4', 'duration': 10, 'created_at': datetime.now(), 'updated_at': datetime.now()},
    {'lesson_id': 20, 'course_id': 11, 'title': 'Lesson 20: Git Branching', 'content': 'Working with branches.', 'video_url': 'https://example.com/videos/lesson20.mp4', 'duration': 12, 'created_at': datetime.now(), 'updated_at': datetime.now()},
    {'lesson_id': 21, 'course_id': 12, 'title': 'Lesson 21: Linux Commands', 'content': 'Basic terminal commands.', 'video_url': 'https://example.com/videos/lesson21.mp4', 'duration': 15, 'created_at': datetime.now(), 'updated_at': datetime.now()},
    {'lesson_id': 22, 'course_id': 12, 'title': 'Lesson 22: Bash Scripting', 'content': 'Automating with scripts.', 'video_url': 'https://example.com/videos/lesson22.mp4', 'duration': 13, 'created_at': datetime.now(), 'updated_at': datetime.now()},
    {'lesson_id': 23, 'course_id': 13, 'title': 'Lesson 23: Java Basics', 'content': 'Getting started with Java.', 'video_url': 'https://example.com/videos/lesson23.mp4', 'duration': 16, 'created_at': datetime.now(), 'updated_at': datetime.now()},
    {'lesson_id': 24, 'course_id': 14, 'title': 'Lesson 24: C# Introduction', 'content': 'Understanding C# basics.', 'video_url': 'https://example.com/videos/lesson24.mp4', 'duration': 14, 'created_at': datetime.now(), 'updated_at': datetime.now()},
    {'lesson_id': 25, 'course_id': 15, 'title': 'Lesson 25: Data Science Overview', 'content': 'What is data science?', 'video_url': 'https://example.com/videos/lesson25.mp4', 'duration': 17, 'created_at': datetime.now(), 'updated_at': datetime.now()},
]

try:
    course_collection = db["lessons"]
    insert_course_data = course_collection.insert_many(lessons_data)
    print("Lessons added!!!")
except Exception as e:
    print(f"Unable to add lessons because of {e}")

# Assignments
assignments_data = [
    {
        'assignment_id': 1,
        'course_id': 1,
        'title': 'HTML Basics Assignment',
        'description': 'Create a simple web page using basic HTML elements.',
        'due_date': datetime(2025, 6, 25, 0, 0),
        'created_at': datetime(2025, 6, 13, 17, 47, 29, 987382)
    },
    {
        'assignment_id': 2,
        'course_id': 2,
        'title': 'CSS Styling Project',
        'description': 'Style the provided HTML page using CSS to match a given design.',
        'due_date': datetime(2025, 6, 26),
        'created_at': datetime(2025, 6, 13)
    },
    {
        'assignment_id': 3,
        'course_id': 3,
        'title': 'JavaScript Variables and Functions',
        'description': 'Write a script using functions and variables to simulate a calculator.',
        'due_date': datetime(2025, 6, 27),
        'created_at': datetime(2025, 6, 13)
    },
    {
        'assignment_id': 4,
        'course_id': 4,
        'title': 'Python List Operations',
        'description': 'Implement a program that manipulates and analyzes lists.',
        'due_date': datetime(2025, 6, 28),
        'created_at': datetime(2025, 6, 13)
    },
    {
        'assignment_id': 5,
        'course_id': 5,
        'title': 'Data Cleaning with Pandas',
        'description': 'Clean and prepare a dataset using Pandas techniques.',
        'due_date': datetime(2025, 6, 29),
        'created_at': datetime(2025, 6, 13)
    },
    {
        'assignment_id': 6,
        'course_id': 6,
        'title': 'SQL Query Practice',
        'description': 'Write SQL queries to retrieve and manipulate data from a sample database.',
        'due_date': datetime(2025, 6, 30),
        'created_at': datetime(2025, 6, 13)
    },
    {
        'assignment_id': 7,
        'course_id': 7,
        'title': 'MongoDB CRUD Operations',
        'description': 'Create and update documents in a MongoDB collection.',
        'due_date': datetime(2025, 7, 1),
        'created_at': datetime(2025, 6, 13)
    },
    {
        'assignment_id': 8,
        'course_id': 8,
        'title': 'Building Django Models',
        'description': 'Define Django models for a blogging application.',
        'due_date': datetime(2025, 7, 2),
        'created_at': datetime(2025, 6, 13)
    },
    {
        'assignment_id': 9,
        'course_id': 9,
        'title': 'API Design with FastAPI',
        'description': 'Design and test a RESTful API using FastAPI.',
        'due_date': datetime(2025, 7, 3),
        'created_at': datetime(2025, 6, 13)
    },
    {
        'assignment_id': 10,
        'course_id': 10,
        'title': 'Data Analysis with Python',
        'description': 'Analyze a dataset and provide insights using charts and graphs.',
        'due_date': datetime(2025, 7, 4),
        'created_at': datetime(2025, 6, 13)
    },
]

try:
    course_collection = db["assignments"]
    insert_course_data = course_collection.insert_many(assignments_data)
    print("Assignments added!!!")
except Exception as e:
    print(f"Unable to add assignment because of {e}")

# Submission
submissions_data = [
    {
        'submission_id': 1,
        'assignment_id': 1,
        'student_id': 4,
        'content': 'Implemented basic Python functions with comments and examples.',
        'submitted_at': datetime(2025, 6, 14, 15, 44, 53),
        'grade': 60.0,
        'feedback': 'Good start, but missing function docstrings and test cases.'
    },
    {
        'submission_id': 2,
        'assignment_id': 2,
        'student_id': 7,
        'content': 'Analyzed sales data using Pandas and visualized it with Matplotlib.',
        'submitted_at': datetime(2025, 6, 13, 18, 12, 25),
        'grade': 85.5,
        'feedback': 'Excellent analysis. Consider commenting your code more clearly.'
    },
    {
        'submission_id': 3,
        'assignment_id': 1,
        'student_id': 5,
        'content': 'Built a simple calculator app in Python using functions.',
        'submitted_at': datetime(2025, 6, 13, 19, 5, 10),
        'grade': 75.0,
        'feedback': 'Nice effort. Variable naming could be improved for clarity.'
    },
    {
        'submission_id': 4,
        'assignment_id': 3,
        'student_id': 2,
        'content': 'Styled a webpage using HTML and CSS with responsive layout.',
        'submitted_at': datetime(2025, 6, 12, 16, 30, 0),
        'grade': 90.0,
        'feedback': 'Great design and layout. Responsiveness was implemented well.'
    },
    {
        'submission_id': 5,
        'assignment_id': 4,
        'student_id': 8,
        'content': 'Wrote a JavaScript function to dynamically update webpage content.',
        'submitted_at': datetime(2025, 6, 13, 14, 20, 45),
        'grade': 70.5,
        'feedback': 'Function works correctly, but lacks input validation.'
    },
    {
        'submission_id': 6,
        'assignment_id': 2,
        'student_id': 3,
        'content': 'Cleaned and visualized customer churn dataset using Pandas.',
        'submitted_at': datetime(2025, 6, 13, 17, 15, 33),
        'grade': 82.0,
        'feedback': 'Well done. Great use of groupby and plotting techniques.'
    },
    {
        'submission_id': 7,
        'assignment_id': 5,
        'student_id': 6,
        'content': 'Created a React component for a to-do list application.',
        'submitted_at': datetime(2025, 6, 14, 11, 0, 0),
        'grade': 92.5,
        'feedback': 'Excellent use of hooks and component structure.'
    },
    {
        'submission_id': 8,
        'assignment_id': 6,
        'student_id': 9,
        'content': 'Built a classification model using scikit-learn on the Iris dataset.',
        'submitted_at': datetime(2025, 6, 13, 13, 42, 10),
        'grade': 88.0,
        'feedback': 'Model accuracy was good. Feature engineering can be improved.'
    },
    {
        'submission_id': 9,
        'assignment_id': 7,
        'student_id': 1,
        'content': 'Designed an ER diagram and normalized a sample database.',
        'submitted_at': datetime(2025, 6, 12, 9, 15, 0),
        'grade': 78.0,
        'feedback': 'Normalization was accurate. Diagram could use clearer labels.'
    },
    {
        'submission_id': 10,
        'assignment_id': 8,
        'student_id': 10,
        'content': 'Outlined basic cybersecurity protocols for network safety.',
        'submitted_at': datetime(2025, 6, 13, 16, 25, 50),
        'grade': 69.5,
        'feedback': 'Content is relevant, but examples were too general.'
    },
    {
        'submission_id': 11,
        'assignment_id': 3,
        'student_id': 4,
        'content': 'Created a fully functional multi-page HTML site with media queries.',
        'submitted_at': datetime(2025, 6, 14, 10, 12, 18),
        'grade': 91.0,
        'feedback': 'Impressive work! Responsive layout and accessibility were well addressed.'
    },
    {
        'submission_id': 12,
        'assignment_id': 6,
        'student_id': 7,
        'content': 'Trained and tuned a decision tree model on a marketing dataset.',
        'submitted_at': datetime(2025, 6, 13, 15, 57, 39),
        'grade': 86.5,
        'feedback': 'Well-structured submission with clear explanation of parameters.'
    }
]

try:
    course_collection = db["submissions"]
    insert_course_data = course_collection.insert_many(submissions_data)
    print("Submission added!!!")
except Exception as e:
    print(f"Unable to add submission because of {e}")

# Task 3.1: Create Operations
# 1. Add a new student user
try:
    insert_new_student = db.users.insert_one({"user_id": 21, "full_name": "Folarin Shade", "email": "folashade@gmail.com", "role": "student", "dateJoined": datetime.now(), "profile": {
            "bio": "I am Shade, a frontend dev student.",
            "avatar": "https://example.com/avatar1.jpg",
            "skills": ["Python", "HTML", "CSS", "JavaScript"]
        }, 'is_active': 'True'})
    print(f"New student added!!!")
except Exception as e:
    print(f"Unable to add new student because of {e}")

# 2. Create a new course
try:
    insert_new_course = db.courses.insert_one({
        "course_id": 21,
        "title": "Advanced React Development",
        "description": "Deep dive into React with hooks and state management.",
        "instructor_id": 13,
        "category": "Frontend Development",
        "level": "advanced",
        "duration": 25,
        "price": 89.99,
        "tags": ["React", "Hooks", "State Management"],
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "is_published": True
    })
    print(f"New course, with this details {insert_new_course} added!!!")
except Exception as e:
    print(f"Unable to add new course because of {e}")

# 3. Enroll a student in a course
try:
    insert_new_enrollment = db.enrollments.insert_one({
        "enrollment_id": 21,
        "student_id": 21, 
        "course_id": 1, 
        "enrolled_at": datetime.now(),
        "is_active": True
    })
    print(f"New enrollment added!!!")
except Exception as e:
    print(f"Unable to add new enrollment because of {e}")

# 4. Add a new lesson to an existing course
try:
    insert_new_lesson = db.lessons.insert_one({
        'lesson_id': 21,
        'course_id': 1,  
        'title': 'Lesson 21: Advanced Python Concepts',
        'content': 'This lesson covers advanced topics in Python programming.',
        'video_url': 'https://example.com/videos/lesson21.mp4',
        'duration': 30,
        'created_at': datetime.now(),
        'updated_at': datetime.now()
    })
    print(f"New lesson added!!!")
except Exception as e:
    print(f"Unable to add new lesson because of {e}")

# Task 3.2: Read Operations
# 1. Find all active students
try:
    active_students = db.users.find({"role": "student", "is_active": 'True'})
    print("Active Students:")
    for student in active_students:
        print(student)
except Exception as e:
    print(f"Unable to retrieve active students because of {e}")

# 2. Retrieve course details with instructor information
try:
    courses_with_instructors = db.courses.aggregate([
        {
            "$lookup": {
                "from": "users",
                "localField": "instructor_id",
                "foreignField": "user_id",
                "as": "instructor_info"
            }
        },
        {
            "$unwind": "$instructor_info"
        }
    ])
    print("Courses with Instructor Information:")
    for course in courses_with_instructors:
        print(course)
except Exception as e:
    print(f"Unable to retrieve courses with instructor information because of {e}")

# 3. Get all courses in a specific category
try:
    category = "Data Science"  
    courses_in_category = db.courses.find({"category": category})
    print(f"Courses in {category} Category:")
    for course in courses_in_category:
        print(course)
except Exception as e:
    print(f"Unable to retrieve courses in category {category} because of {e}")

# 4. Find students enrolled in a particular course
try:
    course_id = 1  
    enrolled_students = db.enrollments.aggregate([
        {"$match": {"course_id": course_id}},
        {
            "$lookup": {
                "from": "users",
                "localField": "student_id",
                "foreignField": "user_id",
                "as": "student_info"
            }
        },
        {"$unwind": "$student_info"}
    ])
    print(f"Students enrolled in Course ID {course_id}:")
    for enrollment in enrolled_students:
        print(enrollment)
except Exception as e:
    print(f"Unable to retrieve students enrolled in course {course_id} because of {e}")

# 5. Search courses by title (case-insensitive, partial match)
try:
    search_title = "Python"  
    matching_courses = db.courses.find({"title": {"$regex": search_title, "$options": "i"}})
    print(f"Courses matching '{search_title}':")
    for course in matching_courses:
        print(course)
except Exception as e:
    print(f"Unable to search courses by title '{search_title}' because of {e}")

# Task 3.3: Update Operations
# 1. Update a user’s profile information
try:
    user_id_to_update = 21  
    updated_profile = {
        "bio": "I am Shade, a frontend dev student with a passion for design.",
        "avatar": "https://example.com/new_avatar1.jpg",
        "skills": ["Python", "HTML", "CSS", "JavaScript", "React"]
    }
    update_result = db.users.update_one(
        {"user_id": user_id_to_update},
        {"$set": {"profile": updated_profile}}
    )
    if update_result.modified_count > 0:
        print(f"User profile updated successfully for user_id {user_id_to_update}!")
    else:
        print(f"No changes made to the profile of user_id {user_id_to_update}.")
except Exception as e:
    print(f"Unable to update user profile for user_id {user_id_to_update} because of {e}")

# 2. Mark a course as published
try:
    course_id_to_publish = 10  
    update_result = db.courses.update_one(
        {"course_id": course_id_to_publish},
        {"$set": {"is_published": True, "updated_at": datetime.now()}}
    )
    if update_result.modified_count > 0:
        print(f"Course ID {course_id_to_publish} marked as published successfully!")
    else:
        print(f"No changes made to the course ID {course_id_to_publish}.")
except Exception as e:
    print(f"Unable to mark course ID {course_id_to_publish} as published because of {e}")

# 3. Update assignment grades
try:
    assignment_id_to_update = 1  
    updated_assignment = {
        "title": "HTML Basics Assignment - Updated",
        "description": "Create a simple web page using basic HTML elements with additional features.",
        "due_date": datetime(2025, 6, 30, 0, 0),
        "created_at": datetime(2025, 6, 13, 17, 47, 29, 987382)
    }
    update_result = db.assignments.update_one(
        {"assignment_id": assignment_id_to_update},
        {"$set": updated_assignment}
    )
    if update_result.modified_count > 0:
        print(f"Assignment ID {assignment_id_to_update} updated successfully!")
    else:
        print(f"No changes made to the assignment ID {assignment_id_to_update}.")
except Exception as e:
    print(f"Unable to update assignment ID {assignment_id_to_update} because of {e}")

# 4. Add tags to an existing course
try:
    course_id_to_update = 1  
    new_tags = ["HTML5", "Web Development"]
    update_result = db.courses.update_one(
        {
            "course_id": course_id_to_update
        },
        {"$addToSet": {"tags": {"$each": new_tags}}, "$set": {"updated_at": datetime.now()}}
    )
    if update_result.modified_count > 0:
        print(f"Tags added to Course ID {course_id_to_update} successfully!")
    else:
        print(f"No changes made to the course ID {course_id_to_update}.")
except Exception as e:
    print(f"Unable to add tags to course ID {course_id_to_update} because of {e}")

# Task 3.4: Delete Operations
# 1. Remove a user (soft delete by setting isActive to false)
try:
	user_id_to_remove = 15
	update_result = db.users.update_one(
		{"user_id": user_id_to_remove},
		{"$set": {"is_active": 'False'}}
	)
	if update_result.modified_count > 0:
		print(f"User with user_id {user_id_to_remove} has been soft deleted (is_active set to False).")
	else:
		print(f"No user found with user_id {user_id_to_remove}, or already soft deleted.")
except Exception as e:
	print(f"Unable to soft delete user because of {e}")

# 2. Delete an enrollment
try:
	enrollment_id_to_delete = 5
	delete_result = db.enrollments.delete_one({"enrollment_id": enrollment_id_to_delete})
	if delete_result.deleted_count > 0:
		print(f"Enrollment with enrollment_id {enrollment_id_to_delete} deleted successfully!")
	else:
		print(f"No enrollment found with enrollment_id {enrollment_id_to_delete}.")
except Exception as e:
	print(f"Unable to delete enrollment because of {e}")
     
# 3. Remove a lesson from a course
try:
	lesson_id_to_delete = 3
	delete_result = db.lessons.delete_one({"lesson_id": lesson_id_to_delete})
	if delete_result.deleted_count > 0:
		print(f"Lesson with lesson_id {lesson_id_to_delete} deleted successfully!")
	else:
		print(f"No lesson found with lesson_id {lesson_id_to_delete}.")
except Exception as e:
	print(f"Unable to delete lesson because of {e}")
     
# Task 4.1: Complex Queries
# 1. Find courses with price between $50 and $200
try:
	courses_in_price_range = db.courses.find({"price": {"$gte": 50, "$lte": 200}})
	print("Courses with price between $50 and $200:")
	for course in courses_in_price_range:
		print(course)
except Exception as e:
	print(f"Unable to retrieve courses in price range because of {e}")
     
# 2. Get users who joined in the last 6 months
try:
	six_months_ago = datetime.now().replace(microsecond=0) - pd.DateOffset(months=6)
	recent_users = db.users.find({"dateJoined": {"$gte": six_months_ago}})
	print("Users who joined in the last 6 months:")
	for user in recent_users:
		print(user)
except Exception as e:
	print(f"Unable to retrieve users who joined in the last 6 months because of {e}")
     
# 3. Find courses that have specific tags using $in operator
try:
	tags_to_search = ["Python", "React"] 
	courses_with_tags = db.courses.find({"tags": {"$in": tags_to_search}})
	print(f"Courses with tags {tags_to_search}:")
	for course in courses_with_tags:
		print(course)
except Exception as e:
	print(f"Unable to find courses with tags {tags_to_search} because of {e}")
     
# 4. Retrieve assignments with due dates in the next week
try:
	today = datetime.now()
	next_week = today + pd.Timedelta(days=7)
	assignments_next_week = db.assignments.find({
		"due_date": {"$gte": today, "$lte": next_week}
	})
	print("Assignments due in the next week:")
	for assignment in assignments_next_week:
		print(assignment)
except Exception as e:
	print(f"Unable to retrieve assignments due in the next week because of {e}")
     
# Task 4.2: Aggregation Pipeline
# 1. Course Enrollment Statistics:
# Count total enrollments per course, Calculate average course rating, Group by course category

try:
	enrollment_stats = db.courses.aggregate([
		{
			"$lookup": {
				"from": "enrollments",
				"localField": "course_id",
				"foreignField": "course_id",
				"as": "enrollments"
			}
		},
		{
			"$group": {
				"_id": "$category",
				"courses": {"$push": "$$ROOT"},
				"total_courses": {"$sum": 1},
				"total_enrollments_in_category": {"$sum": {"$size": "$enrollments"}},
				"average_rating": {"$avg": "$rating"}
			}
		}
	])
	print("Course Enrollment Statistics by Category:")
	for stat in enrollment_stats:
		print(stat)
except Exception as e:
	print(f"Unable to compute course enrollment statistics because of {e}")
     
# 2. Student Performance Analysis:
# Average grade per student, Completion rate by course, Top-performing students

# Average grade per student
try:
	avg_grade_per_student = db.submissions.aggregate([
		{
			"$group": {
				"_id": "$student_id",
				"average_grade": {"$avg": "$grade"},
				"submission_count": {"$sum": 1}
			}
		},
		{
			"$lookup": {
				"from": "users",
				"localField": "_id",
				"foreignField": "user_id",
				"as": "student_info"
			}
		},
		{"$unwind": "$student_info"},
		{
			"$project": {
				"_id": 0,
				"student_id": "$_id",
				"student_name": "$student_info.full_name",
				"average_grade": 1,
				"submission_count": 1
			}
		}
	])
	print("Average grade per student:")
	for student in avg_grade_per_student:
		print(student)
except Exception as e:
	print(f"Unable to compute average grade per student because of {e}")
     
# Completion rate by course
try:
	# Count total assignments per course
	assignments_per_course = list(db.assignments.aggregate([
		{"$group": {"_id": "$course_id", "total_assignments": {"$sum": 1}}}
	]))
	assignments_dict = {a["_id"]: a["total_assignments"] for a in assignments_per_course}

	# Count submissions per course
	submissions_per_course = db.submissions.aggregate([
		{
			"$lookup": {
				"from": "assignments",
				"localField": "assignment_id",
				"foreignField": "assignment_id",
				"as": "assignment_info"
			}
		},
		{"$unwind": "$assignment_info"},
		{
			"$group": {
				"_id": "$assignment_info.course_id",
				"submission_count": {"$sum": 1},
				"students": {"$addToSet": "$student_id"}
			}
		}
	])
	print("\nCompletion rate by course:")
	for course in submissions_per_course:
		course_id = course["_id"]
		total_assignments = assignments_dict.get(course_id, 0)
		# Number of students who submitted at least one assignment in this course
		num_students = len(course["students"])
		# Completion rate = total submissions / (total assignments * num_students)
		completion_rate = (course["submission_count"] / (total_assignments * num_students)
						   if total_assignments > 0 and num_students > 0 else 0)
		print(f"Course ID {course_id}: Completion Rate = {completion_rate:.2%}")
except Exception as e:
	print(f"Unable to compute completion rate by course because of {e}")
      
# Top-performing students (by average grade)
try:
	top_students = db.submissions.aggregate([
		{
			"$group": {
				"_id": "$student_id",
				"average_grade": {"$avg": "$grade"}
			}
		},
		{
			"$sort": {"average_grade": -1}
		},
		{
			"$limit": 5
		},
		{
			"$lookup": {
				"from": "users",
				"localField": "_id",
				"foreignField": "user_id",
				"as": "student_info"
			}
		},
		{"$unwind": "$student_info"},
		{
			"$project": {
				"_id": 0,
				"student_id": "$_id",
				"student_name": "$student_info.full_name",
				"average_grade": 1
			}
		}
	])
	print("\nTop-performing students (by average grade):")
	for student in top_students:
		print(student)
except Exception as e:
	print(f"Unable to compute top-performing students because of {e}")
      
# 3. Instructor Analytics:
# Total students taught by each instructor, Average course rating per instructor, Revenue generated per instructor
try:
	instructor_analytics = db.courses.aggregate([
		{
			"$lookup": {
				"from": "enrollments",
				"localField": "course_id",
				"foreignField": "course_id",
				"as": "enrollments"
			}
		},
		{
			"$match": {
				"instructor_id": {"$exists": True}
			}
		},
		{
			"$group": {
				"_id": "$instructor_id",
				"courses": {"$push": "$$ROOT"},
				"total_students": {"$sum": {"$size": "$enrollments"}},
				"average_rating": {"$avg": "$rating"},
				"revenue": {"$sum": "$price"}
			}
		},
		{
			"$lookup": {
				"from": "users",
				"localField": "_id",
				"foreignField": "user_id",
				"as": "instructor_info"
			}
		},
		{"$unwind": "$instructor_info"},
		{
			"$project": {
				"_id": 0,
				"instructor_id": "$_id",
				"instructor_name": "$instructor_info.full_name",
				"total_students": 1,
				"average_rating": 1,
				"revenue": 1
			}
		}
	])
	print("Instructor Analytics:")
	for analytics in instructor_analytics:
		print(analytics)
except Exception as e:
	print(f"Unable to compute instructor analytics because of {e}")
      
# 4. Advanced Analytics:

# Monthly enrollment trends
try:
	monthly_enrollments = db.enrollments.aggregate([
		{
			"$group": {
				"_id": {
					"year": {"$year": "$enrolled_at"},
					"month": {"$month": "$enrolled_at"}
				},
				"total_enrollments": {"$sum": 1}
			}
		},
		{"$sort": {"_id.year": 1, "_id.month": 1}}
	])
	print("Monthly Enrollment Trends:")
	for entry in monthly_enrollments:
		print(f"{entry['_id']['year']}-{entry['_id']['month']:02d}: {entry['total_enrollments']} enrollments")
except Exception as e:
	print(f"Unable to compute monthly enrollment trends because of {e}")

# Most popular course categories
try:
	popular_categories = db.courses.aggregate([
		{
			"$lookup": {
				"from": "enrollments",
				"localField": "course_id",
				"foreignField": "course_id",
				"as": "enrollments"
			}
		},
		{
			"$group": {
				"_id": "$category",
				"total_enrollments": {"$sum": {"$size": "$enrollments"}}
			}
		},
		{"$sort": {"total_enrollments": -1}}
	])
	print("\nMost Popular Course Categories:")
	for cat in popular_categories:
		print(f"Category: {cat['_id']}, Enrollments: {cat['total_enrollments']}")
except Exception as e:
	print(f"Unable to compute most popular course categories because of {e}")

# Student engagement metrics (average submissions per student)
try:
	engagement = db.submissions.aggregate([
		{
			"$group": {
				"_id": "$student_id",
				"submission_count": {"$sum": 1}
			}
		},
		{
			"$group": {
				"_id": None,
				"avg_submissions_per_student": {"$avg": "$submission_count"},
				"total_students": {"$sum": 1}
			}
		}
	])
	print("\nStudent Engagement Metrics:")
	for metric in engagement:
		print(f"Average submissions per student: {metric['avg_submissions_per_student']:.2f}")
		print(f"Total students with submissions: {metric['total_students']}")
except Exception as e:
	print(f"Unable to compute student engagement metrics because of {e}")
      
# Task 5.1: Index Creation
# Create appropriate indexes for: User email lookup

from pymongo.errors import OperationFailure

# Unique index on user_id for users collection
try:
	db.users.create_index("user_id", unique=True)
	print("Unique index on user_id created.")
except OperationFailure as e:
	print(f"Could not create unique index on user_id: {e}")

# Unique index on email for users collection
try:
	db.users.create_index("email", unique=True)
	print("Unique index on email created.")
except OperationFailure as e:
	print(f"Could not create unique index on email: {e}")

# Index on instructor_id for courses collection to optimize lookups
try:
	db.courses.create_index("instructor_id")
	print("Index on instructor_id created.")
except OperationFailure as e:
	print(f"Could not create index on instructor_id: {e}")

# Index on course_id for enrollments and lessons collections to optimize lookups
try:
	db.enrollments.create_index("course_id")
	print("Index on course_id for enrollments created.")
except OperationFailure as e:
	print(f"Could not create index on course_id for enrollments: {e}")

try:
	db.lessons.create_index("course_id")
	print("Index on course_id for lessons created.")
except OperationFailure as e:
	print(f"Could not create index on course_id for lessons: {e}")
	
# 2. Course search by title and category

search_title = "Python"
search_category = "Data Science"

try:
	courses = db.courses.find({
		"title": {"$regex": search_title, "$options": "i"},
		"category": search_category
	})
	print(f"Courses with title containing '{search_title}' in category '{search_category}':")
	for course in courses:
		print(course)
except Exception as e:
	print(f"Unable to search courses by title and category because of {e}")
	
# 3. Assignment queries by due date

try:
	assignments_due_soon = db.assignments.find({"due_date": {"$gte": datetime.now()}})
	print("Assignments due after today:")
	for assignment in assignments_due_soon:
		print(assignment)
except Exception as e:
	print(f"Unable to retrieve assignments by due date because of {e}")
	
# 4. Enrollment queries by student and course

student_id = 4  
try:
	student_enrollments = db.enrollments.find({"student_id": student_id})
	print(f"Enrollments for student_id {student_id}:")
	for enrollment in student_enrollments:
		print(enrollment)
except Exception as e:
	print(f"Unable to retrieve enrollments for student_id {student_id} because of {e}")

# Find all enrollments for a specific course
course_id = 1  
try:
	course_enrollments = db.enrollments.find({"course_id": course_id})
	print(f"\nEnrollments for course_id {course_id}:")
	for enrollment in course_enrollments:
		print(enrollment)
except Exception as e:
	print(f"Unable to retrieve enrollments for course_id {course_id} because of {e}")
	
# Task 5.2: Query Optimization
# 1. Analyze query performance using explain() method in PyMongo

try:
	explain_result = db.users.find({"role": "student", "is_active": 'True'}).explain()
	print("Explain output for active students query:")
	print(explain_result)
except Exception as e:
	print(f"Unable to analyze query performance: {e}")
	
# 2. Optimize at least 3 slow queries

# 1. Find all active students (ensure index on 'role' and 'is_active')
try:
	db.users.create_index([("role", 1), ("is_active", 1)])
	print("Compound index on (role, is_active) created.")
except Exception as e:
	print(f"Could not create compound index on (role, is_active): {e}")

# 2. Retrieve course details with instructor information
try:
	courses_with_instructors_optimized = db.courses.aggregate([
		{
			"$lookup": {
				"from": "users",
				"localField": "instructor_id",
				"foreignField": "user_id",
				"as": "instructor_info"
			}
		},
		{"$unwind": "$instructor_info"},
		{
			"$project": {
				"title": 1,
				"category": 1,
				"instructor_id": 1,
				"instructor_info.full_name": 1,
				"instructor_info.email": 1
			}
		}
	])
	print("Optimized: Courses with Instructor Information (limited fields):")
	for course in courses_with_instructors_optimized:
		print(course)
except Exception as e:
	print(f"Unable to retrieve optimized courses with instructor information because of {e}")

# 3. Search courses by title (case-insensitive, partial match)
try:
	db.courses.create_index([("title", "text")])
	print("Text index on title created.")
except Exception as e:
	print(f"Could not create text index on title: {e}")

try:
	# Use $text for optimized search if possible
	matching_courses_optimized = db.courses.find({"$text": {"$search": search_title}})
	print(f"Optimized: Courses matching '{search_title}':")
	for course in matching_courses_optimized:
		print(course)
except Exception as e:
	print(f"Unable to search courses by title '{search_title}' using text index because of {e}")
	
# 3. Document the performance improvements using Python timing functions

import time

# Compare timing for original vs optimized "Find all active students" query

# Original query (before index/optimization)
start_time = time.time()
list(db.users.find({"role": "student", "is_active": 'True'}))
original_duration = time.time() - start_time

# Optimized query (after compound index)
start_time = time.time()
list(active_students)  # active_students uses the same query but benefits from the index
optimized_duration = time.time() - start_time

print(f"Original query duration: {original_duration:.6f} seconds")
print(f"Optimized query duration: {optimized_duration:.6f} seconds")