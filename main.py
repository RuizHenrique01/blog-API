import uvicorn
from blog.main import app

start = app

if __name__ == '__main__':
    uvicorn.run('main:start', reload=True)