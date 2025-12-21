#Here we can write test cases for CreateBooking
# #class we can define as testsuite as TestCreateBooking
import allure
import pytest

from src.moduler.payload_manager.payload_manager import payload_create_booking
from src.moduler.wrappers.api_request_wrapper import post_request
from src.endpoints.api_enpoint_constant import APIConstants
from src.utilities.utility import Utils
from src.moduler.verification.common_verification import *


class TestCreateBooking:


    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID shouldn't be null")
    @allure.description("Creating a Booking from the paylaod and verfiy that booking id should not be null and status code should be 200 for the correct payload")
    def test_create_booking_positive(self):
        response = post_request(url=APIConstants().url_create_booking(),
                     auth=None,
                     headers=Utils().common_headers_json(),
                     payload = payload_create_booking(),
                     in_json=False

        )
        verify_http_status_code(response_data_status=response.status_code, expected_data=200)
        verify_json_key_for_not_null(response.json()["bookingid"])

        # auth ->  basic auth ( admin, password -> base64)
        # auth -> bearer auth ( api token) eydalkskldjasjdkja....

    def test_create_booking_negative_tc1(self):
        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload={},
            in_json=False
        )
        verify_http_status_code(response_data_status=response.status_code, expected_data=500)

    def test_create_booking_negative_tc2(self):
        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload={"firstname": "pramod"},
            in_json=False
        )
        verify_http_status_code(response_data_status=response.status_code, expected_data=500)

