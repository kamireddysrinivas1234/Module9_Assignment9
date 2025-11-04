
import pytest
from pydantic import ValidationError
from app.schemas import CalcRequest

def test_invalid_op_raises_validation_error():
    with pytest.raises(ValidationError) as exc:
        CalcRequest(a=1, b=2, op="pow")
    # Ensure our custom message is present
    assert "op must be one of add|sub|mul|div" in str(exc.value)
