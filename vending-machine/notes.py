from money import Money


class TenRupeeNote(Money):
    def __init__(self) -> None:
        super().__init__(10)

class TwentyRupeeNote(Money):
    def __init__(self) -> None:
        super().__init__(20)

class FifetyRupeeNote(Money):
    def __init__(self) -> None:
        super().__init__(50)

class HundredRupeeNote(Money):
    def __init__(self) -> None:
        super().__init__(100)
