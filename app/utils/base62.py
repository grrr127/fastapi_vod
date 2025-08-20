import string
from typing import Final

# Final은 재할당은 막지만 mutable한걸 immutable하게 만들진 못한다


class Base62:
    BASE: Final[str] = string.ascii_letters + string.digits
    BASE_LEN: Final[int] = len(BASE)

    @classmethod
    def encode(cls, num: int) -> str:
        if num < 0:
            raise ValueError(f"{cls}.encode() needs positive integer but you passed: {num}")

        if num == 0:
            return cls.BASE[0]

        result = []
        while num:
            num, remainder = divmod(num, cls.BASE_LEN)
            result.append(cls.BASE[remainder])
        return "".join(result)


# print(Base62.encode(62))
# print(Base62.encode(uuid.uuid4().int))
