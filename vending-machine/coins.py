from money import Money


class OneRupeeCoin(Money):
    def __init__(self) -> None:
        super().__init__(1)

class TwoRupeeCoin(Money):
    def __init__(self) -> None:
        super().__init__(2)

class FiveRupeeCoin(Money):
    def __init__(self) -> None:
        super().__init__(5)
