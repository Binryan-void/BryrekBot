from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database_models.user import User

class UserRepository:
    # Función para buscar un usuario por su ID de telegram_id
    @staticmethod
    async def get_by_id(db: AsyncSession, telegram_id: int) -> User | None:
        query = select(User).where(User.telegram_id == telegram_id)
        result = await db.execute(query)
        return result.scalars().first()

    # Función para registrar un usuario nuevo en la base de datos
    @staticmethod
    async def new_user(db: AsyncSession, telegram_id: int, first_name: str, username: str | None = None) -> User:
        # gender tomará "NB" por defecto automáticamente
        new_user = User(
            telegram_id=telegram_id,
            first_name=first_name,
            username=username
        )
        
        #preparamos
        db.add(new_user)
        #guardamos
        await db.commit()
        #actualizamos
        await db.refresh(new_user)
        
        return new_user

    # Actualizar el género
    @staticmethod
    async def update_gender(db: AsyncSession, telegram_id: int, new_gender: str) -> User | None:
        # buscamos al usuario 
        user = await UserRepository.get_by_id(db, telegram_id)
        if user:
            user.gender = new_gender  # Cambiamos el valor 
            await db.commit()
            await db.refresh(user)
        return user 
