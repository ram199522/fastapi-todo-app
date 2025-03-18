from fastapi import FastAPI
from tasks.post_request import router as post_router
from tasks.get_request import router as get_router
from tasks.put_request import router as put_router
from tasks.delete_request import router as delete_router  
app = FastAPI()

# Include all routers
app.include_router(post_router)#This is post_router for post_request file
app.include_router(get_router)#This is get_router for get_request file
app.include_router(put_router)#This is Put_router for Put_request file
app.include_router(delete_router)#This is delete_router for delete_request file

