import re
from typing import Any

class Expression:
    """
    Description: 式を表現するクラス
    Format: <{count}[{sub_expression}{value}>
    Var.:
        - count: 繰り返し処理の回数
        - sub_expression: 再帰的に評価する式
        - value: 処理される値
        - PATTERN: 式のフォーマット
    """

    count: int
    sub_expression: str
    value: str

    PATTERN: str = r"^<([0-9]+)\|((\[0-9A-Z\<\>\ ]*)<([A-Z]*)>$"

    def __init__(self, _value: str) -> None:
        """
        Description: 入力の妥当性確認とメンバ変数の初期化を行う。
        """
        _match: re.Match[str] | None = re.fullmatch(self.PATTERN, _value)
        if _match is None:
            raise ValueError(f"[ValueError] Invalid input: {_value}")
        _params: tuple[str | Any, ...] = _match.groups()
        self.count: int = int(_params[0])
        self.sub_expression: str = str(_params[1])
        self.value: str = str(_params[2])

    def evaluate(self) -> str:
        """
        Description: 式の評価を実行し、結果を文字列で返す。
        """
        ans: str = ""
        for _ in range(self.count):
            if self.sub_expression:
                sub_expression: Expression = Expression(self.sub_expression)
                ans += sub_expression.evaluate()
            ans += self.value
        return ans

def execute(input_value: str) -> str:
    """
    Description: 式の妥当性を確認し、評価を実行する。
    """
    try:
        expression = Expression(input_value)
        return expression.evaluate()
    except Exception as e:
        return str(e)

def demonstrate(input_value: str) -> None:
    print("___________________")
    print("input: ", input_value)
    print("result: ", execute(input_value))

if __name__ == "__main__":
    demonstrate("<30|A>")
    demonstrate("<30|A[aA]>")
    demonstrate("<3|<12|B>A>")
