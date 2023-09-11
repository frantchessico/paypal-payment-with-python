from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import paypalrestsdk


# Configure the PayPal SDK
paypalrestsdk.configure(
    {
        "mode": "sandbox",  # Switch to "live" in production
        "client_id": "your_client_id_of_paypal_here",
        "client_secret": "your_client_secret_do_paypal_aqui",
    }
)

app = FastAPI()

class PaymentRequest(BaseModel):
    amount: int

@app.post("/create-payment")
async def create_payment(payment_request: PaymentRequest):
    try:
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "transactions": [
                {
                    "amount": {
                        "total": str(payment_request.amount),
                        "currency": "USD"
                    }
                }
            ],
            "redirect_urls": {
                "return_url": "http://example.com/success",
                "cancel_url": "http://example.com/cancel"
            }
        })

        if payment.create():
            return {"approval_url": payment.links[1].href}
        else:
            raise HTTPException(status_code=500, detail="Payment creation failed")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/execute-payment")
async def execute_payment(request: Request):
    try:
        data = await request.json()
        payment_id = data.get("payment_id")
        payer_id = data.get("payer_id")

        if not payment_id or not payer_id:
            raise HTTPException(status_code=400, detail="Invalid request data")

        payment = paypalrestsdk.Payment.find(payment_id)
        if payment.execute({"payer_id": payer_id}):
            return {"message": "Payment executed successfully"}
        else:
            raise HTTPException(status_code=500, detail="Payment execution failed")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
