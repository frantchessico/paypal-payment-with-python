
# PayPal Payment API with FastAPI

This is an example of a FastAPI-based API in Python that allows you to create and execute PayPal payments. The API is configured to accept POST requests and interact with the PayPal API for payment processing.

## Prerequisites

- Python installed in your environment.
- FastAPI library installed. You can install it using pip: `pip install fastapi`.
- PayPal REST SDK library installed. You can install it using pip: `pip install paypalrestsdk`.
- PayPal Sandbox or Live credentials: Replace `"seu_client_id_do_paypal_aqui"` and `"seu_client_secret_do_paypal_aqui"` with your actual PayPal client ID and client secret.

## Configuration

1. Set your PayPal credentials in the code.

2. Run the FastAPI server:

   ```shell
   uvicorn app:app --host 0.0.0.0 --port 8080
   ```

The server will be running on port 8080.

## Endpoints

### 1. Create Payment

- **URL:** `/create-payment`
- **Method:** `POST`
- **Request Body (JSON):** 

  ```json
  {
      "amount": 1000
  }
  ```

- **Example Response:**

  ```json
  {
      "approval_url": "https://www.sandbox.paypal.com/checkoutnow?token=EC-1234567890"
  }
  ```

### 2. Execute Payment

- **URL:** `/execute-payment`
- **Method:** `POST`
- **Request Body (JSON):** 

  ```json
  {
      "payment_id": "payment_id_here",
      "payer_id": "payer_id_here"
  }
  ```

- **Example Response:**

  ```json
  {
      "message": "Payment executed successfully"
  }
  ```

## Workflow

1. To create a payment, make a POST request to `/create-payment` with the desired payment amount in the request body.

2. The API will interact with the PayPal API to create a payment and respond with an approval URL. The user should be redirected to this URL for payment approval.

3. After the user approves the payment on the PayPal website, they will be redirected back to your specified return URL.

4. To execute the payment, make a POST request to `/execute-payment` with the payment ID and payer ID received from PayPal.

5. The API will interact with the PayPal API to execute the payment.

Ensure that you follow best security practices when handling sensitive information and payment details.

---

This is a simple example of a PayPal payment API with FastAPI in Python. Customize and enhance this code as needed to meet the specific requirements of your project.

## Developed By: 
**Francisco Inoque**