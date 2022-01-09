from app import create_app
from uvicorn import run

if __name__ == '__main__':
    run(create_app())