
import requests
import time

class Paystack:
    PAYSTACK_SECRET_TEST="sk_test_8078720239fe13d41b08767a7459c85b7d70a12c"
    PAYSTACK_PUBLIC_TEST="pk_test_c0ba813a720035f4330f228b86886193d34f748d"
    base_url = "https://api.paystack.co"

    def verify_payment(self,ref,*args,**kwargs):
        path = f'/transaction/verify/{ref}'

        headers = {
            "Authorization":f"Bearer {self.PAYSTACK_SECRET_TEST}","Content-Type": "application/json",
        }
        url = self.base_url+path
        response = requests.get(url,headers=headers)
        time.sleep(1)
        response_data = response.json()
        return response_data["status"], response_data["message"],response_data['data']
        

    