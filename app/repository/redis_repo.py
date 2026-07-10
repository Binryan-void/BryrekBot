from redis.asyncio import Redis

class RedisRepository:
    
    # Guardar el estado de un usuario (expira en 1 hora)
    @staticmethod
    async def set_state(redis: Redis, telegram_id: int, state: str, ex_seconds: int = 3600) -> None:
        key = f"user_state:{telegram_id}"
        await redis.set(key, state, ex=ex_seconds)

    # Obtener el estado actual del usuario
    @staticmethod
    async def get_state(redis: Redis, telegram_id: int) -> str | None:
        key = f"user_state:{telegram_id}"
        state = await redis.get(key)
        return str(state) if state is not None else None

    # Borrar el estado cuando el usuario termine una acción
    @staticmethod
    async def delete_state(redis: Redis, telegram_id: int) -> None:
        key = f"user_state:{telegram_id}"
        await redis.delete(key)
