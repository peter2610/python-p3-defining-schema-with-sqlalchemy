# lib/sqlalchemy_sandbox.py

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base  # Updated for SQLAlchemy 2.0

# Step 1: Create the declarative base
Base = declarative_base()

# Step 2: Define the Student model
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)  # make name required

    def __repr__(self):
        return f"<Student {self.id}: {self.name}>"

# Step 3: Persist the schema
if __name__ == '__main__':
    # Create SQLite database engine
    engine = create_engine('sqlite:///students.db')

    # Create tables based on the models
    Base.metadata.create_all(engine)
    print("Database and 'students' table created successfully!")
