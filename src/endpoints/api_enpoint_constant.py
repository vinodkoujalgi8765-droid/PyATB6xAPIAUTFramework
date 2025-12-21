#API Endpoints nothing but constants which contain all type of endpoints suchas:
#Base url. auth, booking, bookingID, create booking, PUT/PATCH on booking, delete booking

class APIConstants:

    def base_url(self):
        return 'https://restful-booker.herokuapp.com'

    def url_create_booking(self):
        return 'https://restful-booker.herokuapp.com/booking'

    def url_create_token(self):
        return 'https://restful-booker.herokuapp.com/auth'

    # Update -> PUT, PATCH, DELETE required bookingId

    def url_patch_put_delete(self,booking_id):
        return 'https://restful-booker.herokuapp.com/booking/' + str(booking_id)