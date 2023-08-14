from django.shortcuts import render,get_object_or_404,redirect

from .models import Payment
from.paystack import Paystack
from django.contrib import messages
from django.contrib.sessions.models import Session
from .models import Payment
from accounts.models import Fee
# Create your views here.

# Payment initiation view
def initiate_payment(request):
    # Get the user ID or any other relevant information
    user_id = request.user.id
    try:
        # Retrieve the student based on the user ID
        student = Student.objects.get(user_id=user_id)

        # Retrieve the classroom of the student
        classroom = student.classroom

        # Retrieve the fees associated with the classroom
        fees = classroom.class_fee.all()

        # Check if there are any mandatory fees
        mandatory_fees = fees.filter(is_mandatory=True)

        if mandatory_fees.exists():
            # Get the total payment amount for mandatory fees
            payment_amount = mandatory_fees.aggregate(total_amount=models.Sum('price'))['total_amount']
            
            # Create a payment session
            request.session['payment_data'] = {
                'amount': payment_amount,
                'user_id': user_id,
                'fee_ids': list(mandatory_fees.values_list('id', flat=True)),
            }

            # Redirect to the payment gateway with the necessary parameters
            # (e.g., payment amount, reference)
            return redirect('payment_gateway:payment', amount=payment_amount, ref='ABC123')
        else:
            messages.error(request, 'No mandatory fees found.')
    except Student.DoesNotExist:
        messages.error(request, 'Student not found.')
    
    return redirect('error')

# Payment callback/return view
def payment_callback(request):
    # Retrieve the payment session data
    payment_data = request.session.get('payment_data')
    if not payment_data:
        # Session data not found, handle the error or redirect to an error page
        return redirect('error')

    # Retrieve the payment response from the payment gateway
    payment_status = request.GET.get('status')  # Example payment status
    payment_ref = request.GET.get('ref')  # Example payment reference

    # Verify the payment response
    if payment_status == 'success':
        # Payment success
        amount = payment_data['amount']
        user_id = payment_data['user_id']

        # Update the payment record in your database
        payment = Payment.objects.create(amount=amount, user_id=user_id, ref=payment_ref, verified=True)
        payment.save()

        # Update the session and provide success feedback to the user
        request.session['payment_data'] = None
        messages.success(request, 'Payment successful!')
    else:
        # Payment failure
        messages.error(request, 'Payment failed.')

    # Redirect to a payment completion or confirmation page
    return redirect('payment_completion')


def pay(request,ref):
    payment = Payment.objects.get(ref=ref)
    return render(request=request,template_name='pay.html',context={"payment":payment,"paystack_pk":Paystack.PAYSTACK_PUBLIC_TEST})



def verify_payment(request,ref):
    payment = get_object_or_404(Payment,ref=ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request,"Verification Success")
    else:
        messages.error(request,"Verification Failed")
    return redirect("accounts:pay")