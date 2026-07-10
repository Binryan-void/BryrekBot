from sqlalchemy import Column, BigInteger, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    # Nombre de la tabla en PostgreSQL
    __tablename__ = "users"

    # Columnas principales
    telegram_id = Column(BigInteger, primary_key=True, index=True, unique=True, nullable=False)
    
    # Datos que nos da el perfil de Telegram del usuario
    username = Column(String, nullable=True)     # Puede ser None si el usuario no tiene @alias
    first_name = Column(String, nullable=False)   # El nombre visible (siempre obligatorio)
    gender = Column(String, default="desconocido", nullable=False)

    is_active = Column(Boolean, default=True)
    # si se pone en False desactivamos al usuario
    
    # 4. Fechas automáticas (Postgres se encarga de poner la hora del servidor)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    # hora de primera interaccion
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    # cada que algo cambia

    # Esto sirve para que cuando imprimas el usuario en consola se vea limpio
    def __repr__(self):
        return f"<User {self.telegram_id} - {self.username or self.first_name}>"
