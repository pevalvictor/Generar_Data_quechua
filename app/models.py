from sqlalchemy import Column, Integer, Text, String, TIMESTAMP, func
from app.database import Base

class Traduccion(Base):
    __tablename__ = "traducciones"

    id = Column(Integer, primary_key=True, index=True)
    texto_origen = Column(Text, nullable=False)
    idioma_origen = Column(String(10), default="es")
    texto_traducido = Column(Text, nullable=True)
    idioma_destino = Column(String(10), default="qu")
    fuente = Column(String(20), default="manual")
    fecha = Column(TIMESTAMP, server_default=func.now())
    fecha_modificacion = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
