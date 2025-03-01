from finance.models import Base
from config import engine

def run_migrations():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    run_migrations()
    print("Migrations applied successfully.")
