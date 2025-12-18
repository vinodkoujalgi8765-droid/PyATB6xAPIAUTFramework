import pytest
import allure

@allure.title("Verify PASS ✅ ! that the framework is working")
def test_sample_pass():
    assert True == True

@allure.title("Verify FAIL ❌ ! thst framework is working")
def test_sample_fail():
    assert False == True


