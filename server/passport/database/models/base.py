from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseModel(DeclarativeBase):
    __table_args__ = {"schema": "passport"}

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    def as_dict(self, exclude: list[str] | None = None) -> dict:
        res_dict = {}

        for column in self.__table__.columns:
            if not exclude or column.name not in exclude:
                res_dict[column.name] = getattr(self, column.name)

        return res_dict
