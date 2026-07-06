from pydantic_settings import BaseSettings, SettingsConfigDict



class Configuracion(BaseSettings):
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    SECRET_KEY: str

    model_config = SettingsConfigDict(
        env_file="app/.env",
        extra="ignore"
    )

    @property
    def DATABASE_URL(self):
        return (
            f"postgresql+psycopg://"
            f"{self.DATABASE_USER}:"
            f"{self.DATABASE_PASSWORD}@"
            f"{self.DATABASE_HOST}:"
            f"{self.DATABASE_PORT}/"
            f"{self.DATABASE_NAME}"
        )

    @property
    def DATABASE_URL(self):
       return "postgresql+psycopg://postgres:1234@localhost:5432/revenfy"

configuracion = Configuracion()

print("HOST:", configuracion.DATABASE_HOST)
print("PUERTO:", configuracion.DATABASE_PORT)
print("BD:", configuracion.DATABASE_NAME)
print("USUARIO:", configuracion.DATABASE_USER)
print("PASSWORD:", configuracion.DATABASE_PASSWORD)
