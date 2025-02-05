# main.py
from fastapi import FastAPI
from database import engine
import models 
from routes.materias import router as materias_router
from routes.trabajador import router as trabajadores_router
from routes.proyecto import router as proyectos_router
from routes.proyectoAsignado import router as proyectos_asignados
from routes.jefe import router as jefes_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI();

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


models.Base.metadata.create_all(bind=engine)

app.include_router(materias_router,prefix="/materias",tags=["Materias"])
app.include_router(trabajadores_router,prefix="/trabajadores",tags=["Trabajadores"])
app.include_router(jefes_router,prefix="/jefe",tags=["Jefe de Proyecto"])
app.include_router(proyectos_asignados,prefix="/proyectos_asignados",tags=["Proyectos Asignados"])
app.include_router(proyectos_router,prefix="/proyectos",tags=["Proyectos"])