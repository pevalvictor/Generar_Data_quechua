from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.database import SessionLocal
from app.models import Traduccion

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
def formulario(request: Request):
    db = SessionLocal()
    pendientes = db.query(Traduccion).filter(
        (Traduccion.texto_traducido == "") | (Traduccion.texto_traducido == None)
    ).order_by(Traduccion.id).all()

    registrados = db.query(Traduccion)\
        .filter(Traduccion.texto_traducido != "")\
        .order_by(Traduccion.fecha_modificacion.desc())\
        .all()
        
    db.close()
    return templates.TemplateResponse("traduccion.html", {
        "request": request,
        "pendientes": pendientes,
        "registrados": registrados
    })

@router.post("/guardar")
def guardar_traduccion(request: Request, id: int = Form(...), texto_traducido: str = Form(...)):
    db = SessionLocal()
    frase = db.query(Traduccion).filter(Traduccion.id == id).first()
    if frase:
        frase.texto_traducido = texto_traducido
        # se actualiza fecha_modificacion automáticamente si está definido en el modelo
        db.commit()
    db.close()
    return RedirectResponse("/", status_code=303)

@router.post("/editar")
def editar_traduccion(request: Request, id: int = Form(...), texto_traducido: str = Form(...)):
    db = SessionLocal()
    frase = db.query(Traduccion).filter(Traduccion.id == id).first()
    if frase:
        frase.texto_traducido = texto_traducido
        db.commit()
    db.close()
    return RedirectResponse("/", status_code=303)
