# 📚 MongoDB NoSQL Project

This project showcases a complete NoSQL workflow using **MongoDB** — from database creation to schema design, data population, aggregation, indexing, and query optimization — implemented with **MongoDB Compass** and **PyMongo** in Python.

---

## ✅ Project Highlights

- NoSQL schema design
- Data modeling and insertion
- Read, update, and delete operations
- Advanced querying and filtering
- Aggregation pipelines
- Index creation
- Query performance optimization

---

## 🚀 Project Workflow

### 🏗️ Step 1: Database & Collections Setup
- Created a MongoDB database named `EducationPlatform` using **MongoDB Compass**.
- Defined and created the following collections:
  - `users`
  - `courses`
  - `lessons`
  - `assignments`
  - `submissions`
  - `enrollments`

### 🔌 Step 2: Connecting with PyMongo
Connected using the following connection string:
```python
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["EducationPlatform"]
```

### 🧩 Step 3: Data Insertion
- Created and inserted sample data into all collections.
- Populated:
  - Users (students and instructors)
  - Courses with metadata
  - Lessons tied to courses
  - Assignments and submissions
  - Enrollment records

### ✍️ Step 4: Dynamic Data Manipulation
- Added a new user
- Created a new course
- Enrolled a new student
- Added a new lesson to an existing course

### 🔍 Step 5: Read Operations
Queried for:
- All **active students**
- Course details with **instructor info**
- Courses by **category**
- Students in a **specific course**
- Courses using **partial title matches**

### 🛠 Step 6: Update Operations
Performed updates on:
- User profile information
- Marked courses as `published`
- Updated assignment grades
- Added tags to courses using `$addToSet`

### 🗑️ Step 7: Delete Operations
Deleted:
- A user
- An enrollment record
- A lesson from a course

### 🧠 Step 8: Complex Queries
Filtered and queried:
- Courses within a **price range**
- Users by **registration date range**
- Courses with specific **tags**
- Assignments with **specific due dates**

### 📊 Step 9: Aggregation Pipelines
Built analytics using aggregation:
- Course **enrollment statistics**
- Student **performance analysis**
- Instructor **course/activity summary**
- Advanced reports (e.g., most active students)

### ⚙️ Step 10: Indexing
Created indexes to improve performance:
- Single-field index on `email`
- Unique index on `user_id`
- Compound indexes for common query paths

### ⚡ Step 11: Query Optimization
- Identified slow queries using `.explain()`
- Optimized 3 queries using indexing and structure
- Logged performance gains before/after optimization

---

## 🛠 Tools Used

| Tool            | Purpose                         |
|-----------------|---------------------------------|
| MongoDB         | NoSQL database                  |
| MongoDB Compass | GUI for database management     |
| PyMongo         | Python-MongoDB driver           |
| Python          | Scripting language              |

---

## 👨‍💻 Author
**Martha Imoh**  
_Data Engineer_