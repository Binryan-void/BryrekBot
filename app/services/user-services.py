from sqlalchemy.ext.asyncio import AsyncSession
from redis.asyncio import Redis
from app.repository.user_repo import UserRepository
from app.repository.redis_repo import RedisRepository
from app.database_models.user import User

class UserService:
    
    @staticmethod
    async def get_or_create_user(db: AsyncSession, telegram_id: int, first_name: str, username: str | None = None) -> User:
        user = await UserRepository.get_by_id(db, telegram_id)
        if user is None:
            user = await UserRepository.new_user(db, telegram_id, first_name, username) 
        return user

    @staticmethod
    async def get_user_state(redis: Redis, telegram_id: int) -> str | None:
        return await RedisRepository.get_state(redis, telegram_id)

    @staticmethod
    async def set_user_state(redis: Redis, telegram_id: int, state: str) -> None:
        await RedisRepository.set_state(redis, telegram_id, state)

    @staticmethod
    async def clear_user_state(redis: Redis, telegram_id: int) -> None:
        await RedisRepository.delete_state(redis, telegram_id)
