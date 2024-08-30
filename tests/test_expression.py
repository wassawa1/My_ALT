import os
import sys
import pandas as pd
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from sample import Expression, execute  # この部分は適切なモジュール名に変更してください

# CSVファイルからテストベクトルを読み込む関数
def load_test_vectors(filepath):
    df = pd.read_csv(filepath, dtype={'expected': str, 'error': bool})
    return df.to_dict(orient='records')

# テストベクトルを使用したパラメータ化テスト
@pytest.mark.parametrize("params", load_test_vectors(r"./tests/test_patterns.csv"))
def test_expression_evaluation(params):
    input_value = params['input']
    expected = params['expected']
    is_error = params['error']

    if is_error:
        # エラーが予期される場合のテスト
        with pytest.raises(ValueError):
            result = execute(input_value)
    else:
        # 正常ケースのテスト
        result = execute(input_value)
        assert result == expected, f"Expected {expected}, got {result}"

if __name__ == "__main__":
    pytest.main()
